# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Assemble one Zensical source tree without changing the captured files."""

import json
import re
import shutil
import subprocess
from collections import defaultdict
from html import escape
from pathlib import Path
from tempfile import TemporaryDirectory
from urllib.parse import quote, unquote

from bs4 import BeautifulSoup

from confluence_tables import ANCHOR_MARKER, NHS, restore_tables

MIRROR = Path("nhs-futures/docs")
STAGE = Path("site/source")
SNAPSHOT = "nhs-snapshot"
SPACES = {"BG", "CPCSH", "DCSDCS", "DFOCVCL", "DPSR", "GIFTIF", "GPITF"}
RAW_DOWNLOAD = "https://raw.githubusercontent.com/ohtf/gp-system-spec/main/nhs-futures/docs/"
ATTACHMENT = re.compile(r"(\]\(<?)(?:\.\./)*attachments/([A-Z]+/\d+/att\d+-)")
EPIC = re.compile(r"\b(E\d{5})\s*[-–—]")
CAPABILITY_MARKER = "<!-- capability index -->"
OMITTED_VIDEO_PAGE = "GPITF/1483309062/"
OMISSIONS_RECORD = "https://github.com/ohtf/gp-system-spec/blob/main/nhs-futures/docs/archive-omissions.md"
CONFLUENCE_PAGE_SUFFIX = re.compile(r"https://nhse-dsic\.atlassian\.net/wiki/spaces/[A-Z]+/pages/\d+(?:/.*)?$")
# This stale fragment points to the RBAC section in this particular source edition.
LEGACY_ANCHORS = {
    "1956184126": {"InformationGovernancev2.0.0-RBACRole-basedAccessControl": "InformationGovernance-Standard-RBAC"},
}


def tracked_mirror_files():
    paths = subprocess.check_output(["git", "ls-files", "-z", "--", str(MIRROR)])
    return {Path(path.decode()).relative_to(MIRROR) for path in paths.split(b"\0") if path}


def mirror_pages(tracked):
    return {path for path in tracked if path.suffix == ".md" and path.parts[0] in SPACES} | {
        Path("index.md"), Path("archive-omissions.md")
    }


def attachment_targets(tracked):
    targets = defaultdict(list)
    for path in sorted(tracked):
        if path.parts[0] != "attachments":
            continue
        match = re.fullmatch(r"(attachments/[A-Z]+/\d+/att\d+-)(.+)", path.as_posix())
        if match:
            prefix, name = match.groups()
            targets[prefix.removeprefix("attachments/")].append((name, RAW_DOWNLOAD + quote(path.as_posix())))
    omissions = (MIRROR / "archive-omissions.md").read_text(encoding="utf-8")
    for prefix, name in re.findall(r"`(att\d+-)([^`]+\.mp4)`", omissions):
        targets[OMITTED_VIDEO_PAGE + prefix].append((name, OMISSIONS_RECORD))
    return targets


def confluence_downloads(attachments):
    downloads = defaultdict(set)
    for prefix, entries in attachments.items():
        _, page_id, attachment_id = prefix.removesuffix("-").split("/")
        for name, url in entries:
            downloads[page_id, attachment_id.removeprefix("att"), name].add(url)
            downloads[page_id, None, name].add(url)
    return {key: next(iter(urls)) for key, urls in downloads.items() if len(urls) == 1}


def link_attachments(text, targets):
    # Match the complete tracked filename, including spaces and parentheses.
    # Confluence also produced local links with percent-encoded filenames.
    parts = []
    cursor = 0
    for match in ATTACHMENT.finditer(text):
        end = match.end()
        candidates = [(form, url) for name, url in targets.get(match[2], ()) for form in {name, quote(name)}]
        for name, url in sorted(candidates, key=lambda item: (-len(item[0]), item[0])):
            finish = end + len(name)
            if text.startswith(name, end) and text[finish:finish + 1] in {')', '>', ' ', '\t'}:
                parts.extend((text[cursor:match.start()], match[1], url))
                cursor = finish
                break
        else:
            location = text.count("\n", 0, match.start()) + 1
            raise ValueError(f"line {location}: unmatched local attachment {match[2]}")
    return "".join([*parts, text[cursor:]])


def restore_anchors(text, page_id):
    """Repair imported in-page anchors in the staged copy only."""
    lines = text.splitlines(keepends=True)
    locations = defaultdict(list)
    for i, line in enumerate(lines):
        for marker in ANCHOR_MARKER.finditer(line):
            locations[marker[1]].append(i)

    def linked(anchor):
        return any(f"](#{form})" in text for form in {anchor, quote(anchor, safe="")})

    def element(anchor):
        return f'<span id="{escape(anchor, quote=True).replace("|", "&#124;")}"></span>'

    aliases = defaultdict(list)
    cells = defaultdict(set)
    for anchor, indexes in locations.items():
        if len(indexes) != 1:
            continue
        i = indexes[0]
        line = lines[i]
        in_table = line.startswith("|")
        if in_table and linked(anchor):
            # attr_list works on standalone headings, not text flattened into cells.
            cells.setdefault((i, anchor), set())
        if in_table or re.match(r"^#{1,6} ", line):
            # Some older headings have their linked Confluence page URL appended
            # to the ID, but the original TOC still links to the short form.
            alias = LEGACY_ANCHORS.get(page_id, {}).get(anchor) or CONFLUENCE_PAGE_SUFFIX.sub("", anchor)
            if alias and alias not in locations and linked(alias):
                aliases[alias].append((i, anchor, in_table))
    for alias, candidates in aliases.items():
        if len(candidates) == 1:
            i, anchor, in_table = candidates[0]
            if in_table:
                cells[i, anchor].add(alias)
            else:
                lines[i] = element(alias) + "\n\n" + lines[i]
    for (i, anchor), variants in cells.items():
        replacement = element(anchor) + "".join(element(alias) for alias in sorted(variants))
        lines[i] = lines[i].replace(f"{{#{anchor}}}", replacement, 1)
    return "".join(lines)


def capability_data(tracked, manifest):
    gp_home = Path(".raw/GPITF/1391134009.html")
    if gp_home not in tracked:
        raise ValueError("GP IT Futures source matrix is not tracked")
    matrix = BeautifulSoup((MIRROR / gp_home).read_text(encoding="utf-8"), "html.parser").find("table")
    # The first column contains overarching standards. Remaining columns
    # contain capabilities. The link in each cell heading is its identity.
    ids = {}
    for row in matrix.find_all("tr"):
        for cell in row.find_all(["th", "td"], recursive=False)[1:]:
            heading = cell.find(["h1", "h2", "h3", "h4"])
            link = heading.find("a", href=True) if heading else None
            if link and (match := re.search(r"/spaces/(DCSDCS)/pages/(\d+)", unquote(link["href"]))):
                ids["/".join(match.groups())] = link.get_text(" ", strip=True)
    if not ids:
        raise ValueError("No capabilities found in the GP IT Futures source matrix")

    entries = []
    pages = mirror_pages(tracked)
    for key, title in ids.items():
        path = Path(manifest[key]["path"])
        raw_path = Path(f".raw/{key}.html")
        if raw_path not in tracked or path not in pages:
            raise ValueError(f"Missing tracked capability source: {key}")
        markdown = (MIRROR / path).read_text(encoding="utf-8")
        raw = BeautifulSoup((MIRROR / raw_path).read_text(encoding="utf-8"), "html.parser")
        epics = set(EPIC.findall(raw.get_text(" ", strip=True)))
        if epics != set(EPIC.findall(markdown)):
            raise ValueError(f"Epic IDs differ between raw and converted capability: {key}")

        meta = dict(re.findall(r"^\| \*\*([^*]+)\*\* \| ([^|\n]+) \|$", markdown, flags=re.M))
        if not re.search(r"^#+ (?:\*\*)?Description\b", markdown, flags=re.M):
            raise ValueError(f"Missing Description heading: {key}")
        entries.append((title, path, meta["ID"], meta["Version"], meta["Status"], meta.get("Category", ""), len(epics)))
    return entries


def capability_index(entries):
    groups = defaultdict(list)
    for title, path, code, version, status, category, epics in entries:
        group = "Deprecated capabilities" if status.casefold() == "deprecated" else category.capitalize()
        label = title.replace("[", "\\[").replace("]", "\\]").replace("|", "\\|")
        link = f"[{label}]({SNAPSHOT}/{path.as_posix()})"
        groups[group].append((title, f"| {link} | {code} | {version} | {status} | {epics or 'None'} |"))
    summary = f"{len(entries)} capabilities · {sum(entry[-1] for entry in entries)} epic IDs (counted per capability)"
    table = "| Capability | ID | Version | Captured status | Epics |\n| --- | --- | --- | --- | ---: |"
    lines = [f"**{summary}**"]
    for name in sorted(groups, key=lambda name: (name == "Deprecated capabilities", name)):
        lines += [f"## {name}", table + "\n" + "\n".join(row for _, row in sorted(groups[name]))]
    return "\n\n".join(lines)


def prepare():
    tracked = tracked_mirror_files()
    manifest = json.loads((MIRROR / ".mirror-manifest.json").read_text(encoding="utf-8"))
    pages = mirror_pages(tracked)
    for item in manifest.values():
        if Path(item["path"]) not in pages:
            raise ValueError(f"Snapshot page not staged: {item['path']}")
    entries = capability_data(tracked, manifest)
    attachments = attachment_targets(tracked)
    page_keys = {Path(item["path"]): key for key, item in manifest.items()}
    pages_by_id = {}
    for path, key in page_keys.items():
        page_id = key.split("/", 1)[1]
        reference = (MIRROR / path).read_text(encoding="utf-8")
        url = re.search(r'^source_url: "(https?://[^"<>]+)"$', reference, flags=re.M)
        anchors = set(ANCHOR_MARKER.findall(reference)) | set(LEGACY_ANCHORS.get(page_id, {}).values())
        pages_by_id[page_id] = (path, url[1] if url else f"{NHS}/wiki/pages/{page_id}", anchors)
    downloads = confluence_downloads(attachments)
    table_count = 0

    # Build off to the side so a failed validation never leaves half a tree.
    STAGE.parent.mkdir(exist_ok=True)
    with TemporaryDirectory(dir=STAGE.parent, prefix="source-") as temp:
        staging = Path(temp) / "tree"
        shutil.copytree("docs", staging)
        # Publish only these two historical files, not the whole source directory.
        rcgp = staging / "rcgp-1980"
        rcgp.mkdir()
        for name in ("computers-in-primary-care.pdf", "transcript.md"):
            source = Path("rcgp-1980") / name
            if source.is_symlink():
                raise ValueError(f"Unsafe historical source: {source}")
            shutil.copyfile(source, rcgp / name)
        index = staging / "capabilities.md"
        template = index.read_text(encoding="utf-8")
        if template.count(CAPABILITY_MARKER) != 1:
            raise ValueError("Expected one capability index marker")
        index.write_text(template.replace(CAPABILITY_MARKER, capability_index(entries)), encoding="utf-8")
        for path in sorted(pages):
            source = MIRROR / path
            if source.is_symlink() or not source.resolve().is_relative_to(MIRROR.resolve()):
                raise ValueError(f"Unsafe mirror source: {source}")
            target = staging / SNAPSHOT / path
            target.parent.mkdir(parents=True, exist_ok=True)
            try:
                text = link_attachments(source.read_text(encoding="utf-8"), attachments)
                if key := page_keys.get(path):
                    raw_path = Path(f".raw/{key}.html")
                    if raw_path not in tracked or (MIRROR / raw_path).is_symlink():
                        raise ValueError(f"Missing tracked raw page: {key}")
                    text, count = restore_tables(
                        text, (MIRROR / raw_path).read_text(encoding="utf-8"), pages_by_id[key.split("/", 1)[1]],
                        pages_by_id, downloads, LEGACY_ANCHORS.get(key.split("/", 1)[1], {}),
                    )
                    table_count += count
                    text = restore_anchors(text, key.split("/", 1)[1])
            except ValueError as exc:
                raise ValueError(f"{source}: {exc}") from exc
            if path == Path("index.md"):
                text = text.replace("](.mirror-failures.json)", "](https://github.com/ohtf/gp-system-spec/blob/main/nhs-futures/docs/.mirror-failures.json)")
            # The capture's source link is metadata, not a rendered link.
            if match := re.match(r'\A---\n(?:(?!^---$).)*?^source_url: "(https?://[^"<>]+)"\n(?:(?!^---$).)*?^---\n', text, flags=re.M | re.S):
                text = text[:match.end()] + f"\n[Original NHS source](<{match[1]}>)\n" + text[match.end():]
            target.write_text(text, encoding="utf-8")
        if STAGE.exists():
            shutil.rmtree(STAGE)
        staging.rename(STAGE)
    print(f"Staged {len(manifest)} archive pages, restored {table_count} source tables and indexed {len(entries)} GP IT Futures capabilities.")


if __name__ == "__main__":
    prepare()
