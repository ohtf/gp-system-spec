# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Extract a local implementation reference from the pinned July NHS capture."""

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, urljoin, urlsplit

from bs4 import BeautifulSoup, NavigableString, Tag
from markdown import markdown
from markdownify import markdownify
import yaml

CAPTURE = "2026-07-31"
REVISION = "96ece2be24ce5a311b2f7df09a5c73e354eab38c"
BASE = Path("nhs-futures/docs")
OUTPUT = Path("spec/nhs-england") / CAPTURE
ARCHIVE = "https://ohtf.github.io/gp-system-spec/nhs-snapshot/"
EPIC = re.compile(r"(E\d{5})\s+[-–—]\s+(.+)")
LEVEL = re.compile(r"(MUST|SHOULD|MAY|COULD|WON'T) Epics\b")
DATA_RULE = "WPAD-DI-016"


def captured(path):
    result = subprocess.run(["git", "show", f"{REVISION}:{BASE / path}"], capture_output=True)
    if result.returncode:
        raise ValueError(f"Cannot read July capture file {path}. Fetch the nhs-futures/2026-07-31 tag.")
    return result.stdout


def require(condition, message):
    if not condition:
        raise ValueError(message)


def read_page(manifest, page_id):
    raw_path = Path(f".raw/DCSDCS/{page_id}.html")
    raw = captured(raw_path)
    path = Path(manifest[f"DCSDCS/{page_id}"]["path"])
    header = yaml.safe_load(captured(path).decode().split("---", 2)[1])
    soup = BeautifulSoup(raw, "html.parser")
    metadata = {}
    for row in soup.find("table").find_all("tr"):
        label, value = row.find_all(["th", "td"], recursive=False)
        name = label.get_text(strip=True)
        metadata[name] = ([link.get_text(strip=True) for link in value.select("a")]
                          if name == "Contracting Vehicle(s)" else value.get_text(" ", strip=True))

    reference = {
        "publisher": "NHS England", "jurisdiction": "England", "capture_date": CAPTURE,
        "snapshot_tag": f"nhs-futures/{CAPTURE}", "snapshot_commit": REVISION,
        "confluence_page_id": page_id, "confluence_version": header["version"],
        "title": header["title"], "source_url": header["source_url"],
        "archive_url": ARCHIVE + quote(path.with_suffix("").as_posix()) + "/",
        "source_file": (BASE / raw_path).as_posix(), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "specification_id": metadata["ID"], "publisher_version": metadata["Version"],
        "status_at_capture": metadata["Status"], "effective_date": metadata["Effective Date"],
        "type": metadata["Type"], "contracting_vehicles": metadata["Contracting Vehicle(s)"],
    }
    if category := metadata.get("Category"):
        reference["category"] = category
    return soup, reference


def visible_text(node):
    """Compare words and punctuation, ignoring whitespace introduced by layout."""
    if isinstance(node, NavigableString):
        return str(node)
    text = "".join(visible_text(child) for child in node.children)
    return f" {text} " if node.name in {"div", "p", "ul", "ol", "li", "h2", "h3", "h4", "br", "tr", "td", "th"} else text


def render_blocks(nodes, source_url):
    original = BeautifulSoup("".join(str(node) for node in nodes), "html.parser")
    for tag in original.find_all(True):
        require(tag.name in {"div", "span", "strong", "b", "em", "i", "a", "p", "ul", "ol", "li", "br", "hr", "h4", "sup", "sub"},
                f"Unreviewed source element: {tag.name}")
        if tag.name == "h4":
            tag.name = "h2"
    for link in original.select("a[href]"):
        href = urljoin(source_url, link["href"])
        require(urlsplit(href).scheme in {"http", "https"}, "Unexpected source link scheme")
        link["href"] = href

    output = markdownify(str(original), heading_style="ATX", bullets="-", strip_document="strip").strip()
    rendered = BeautifulSoup(markdown(output), "html.parser")
    require(visible_text(original).split() == visible_text(rendered).split(), "Markdown changed source wording or block boundaries")
    require([link["href"] for link in original.select("a[href]")] == [link["href"] for link in rendered.select("a[href]")],
            "Markdown changed a source link")
    return output


def extract_epics(soup):
    epics = []
    introductions = {}
    for table in soup.find_all("table"):
        cells = table.find_all("td")
        if not cells or not (group := LEVEL.match(cells[0].get_text(" ", strip=True))):
            continue
        priority = group[1]
        require(len(cells) == 2 and priority not in introductions, f"Unexpected {priority} epic layout")
        introductions[priority] = cells[0]
        epic = None
        for node in cells[1].children:
            if not isinstance(node, Tag):
                require(not str(node).strip(), f"Unexpected text between {priority} epic blocks")
            elif node.name == "h3":
                match = EPIC.fullmatch(node.get_text(" ", strip=True))
                require(match is not None and node.get("id"), "Unrecognised epic heading or missing source anchor")
                epic = {"id": match[1], "label": node.get_text(" ", strip=True), "priority": priority,
                        "anchor": node["id"], "blocks": []}
                epics.append(epic)
            elif node.name != "hr":  # Divider between epics, not a requirement.
                require(epic is not None, f"Content before first {priority} epic")
                epic["blocks"].append(node)
    require(len({epic["id"] for epic in epics}) == len(epics), "Duplicate epic IDs in capability edition")
    return epics, introductions


def document(reference, title, body):
    frontmatter = yaml.safe_dump(reference, allow_unicode=True, sort_keys=False, width=120)
    url = reference["archive_url"]
    anchor = f"#{quote(reference['anchor'], safe='')}" if reference.get("anchor") else ""
    return (f"---\n{frontmatter}---\n\n# {title}\n\n"
            f"[Archived source](<{url}{anchor}>) · [Publisher](<{reference['source_url']}{anchor}>)\n\n{body}\n")


def generate():
    manifest = json.loads(captured(Path(".mirror-manifest.json")))
    soup, capability = read_page(manifest, "1391134029")
    require((capability["specification_id"], capability["publisher_version"]) == ("C5", "1.5.0"), "Wrong C5 edition")
    epics, introductions = extract_epics(soup)
    counts = Counter(epic["priority"] for epic in epics)
    require(counts == {"MUST": 9, "MAY": 27}, f"Unexpected C5 epic coverage: {counts}")

    files = {}
    records = []
    cap = Path("capabilities/C5-appointments-management-gp/1.5.0")
    standard = Path("standards/S62-appointments-data-reporting/4.0.1")
    context = ["This file contains the source's description and outcomes. Epic groups are indexed below."]
    for title in ("Description", "Outcomes"):
        anchor = soup.find(id=f"AppointmentsManagement-GP-{title}")
        block = anchor.find_next_sibling()
        if title == "Description":
            body = render_blocks([block], capability["source_url"])
        else:
            body = "\n\n".join("\n\n".join(render_blocks(cell.contents, capability["source_url"]) for cell in row.find_all("td"))
                               for row in block.select("table tr"))
        context += [f"## {title}\n\n{body}"]
    criteria_total = 0
    for priority, intro in introductions.items():
        context += [f"## {priority} epics\n\n{render_blocks(intro.contents, capability['source_url'])}"]
        links = []
        for epic in (item for item in epics if item["priority"] == priority):
            blocks = epic["blocks"]
            first_heading = next(i for i, node in enumerate(blocks) if node.name == "h4" or node.find("h4"))
            require(first_heading > 0 and all(node.name == "p" for node in blocks[:first_heading]),
                    f"Unrecognised user story: {epic['id']}")
            criterion_count = sum(h.get_text(strip=True).lower().startswith("acceptance criterion")
                                  for h in blocks if h.name == "h4")
            require(criterion_count > 0, f"No acceptance criteria for {epic['id']}")
            criteria_total += criterion_count
            reference = {**capability, "epic_id": epic["id"], "priority": priority, "anchor": epic["anchor"],
                         "acceptance_criterion_count": criterion_count}
            user_story = render_blocks(blocks[:first_heading], capability["source_url"])
            details = render_blocks(blocks[first_heading:], capability["source_url"])
            path = cap / "epics" / priority.lower() / f"{epic['id']}.md"
            body = f"## User story\n\n{user_story}\n\n{details}"
            if DATA_RULE in details:
                relative = os.path.relpath(standard / f"{DATA_RULE}.md", path.parent)
                body += f"\n\n## Archive cross-reference\n\n[Open the extracted `{DATA_RULE}` rule]({relative})."
            files[path] = document(reference, epic["label"], body)
            links.append(f"- [{epic['label']}]({path.relative_to(cap).as_posix()})")
            records.append({"kind": "epic", "id": epic["id"], "path": path.as_posix(), "title": epic["label"],
                            "specification_id": "C5", "publisher_version": capability["publisher_version"],
                            "priority": priority, "anchor": epic["anchor"], "acceptance_criterion_count": criterion_count})
        context.append("\n".join(links))
    require(criteria_total == 56, f"Unexpected C5 acceptance-criterion coverage: {criteria_total}")
    files[cap / "README.md"] = document(capability, capability["title"], "\n\n".join(context))

    soup, source = read_page(manifest, "1391133692")
    require((source["specification_id"], source["publisher_version"]) == ("S62", "4.0.1"), "Wrong S62 edition")
    rows = [row for row in soup.find_all("tr") if row.find("td") and row.find("td").get_text(strip=True) == DATA_RULE]
    require(len(rows) == 1, f"Expected one {DATA_RULE} row")
    cells = rows[0].find_all("td", recursive=False)
    require(len(cells) == 4 and not any({"rowspan", "colspan"} & cell.attrs.keys() for cell in cells),
            f"Unreviewed layout for {DATA_RULE}")
    source.update(requirement_id=DATA_RULE, priority=cells[3].get_text(strip=True),
                  anchor="GeneralPracticeAppointmentsDataReporting-Requirements")
    require(source["priority"] == "MUST", f"Unexpected obligation for {DATA_RULE}")
    rule = standard / f"{DATA_RULE}.md"
    body = "\n\n".join(f"## {label}\n\n{render_blocks(cell.contents, source['source_url'])}"
                       for label, cell in zip(("Data item", "Requirement text", "Level"), cells[1:], strict=True))
    files[rule] = document(source, f"{DATA_RULE} - {cells[1].get_text(' ', strip=True)}", body)
    records.append({"kind": "standard-rule", "id": DATA_RULE, "path": rule.as_posix(), "specification_id": "S62",
                    "publisher_version": source["publisher_version"], "priority": source["priority"], "anchor": source["anchor"]})
    files[Path("index.json")] = json.dumps({"schema_version": 1, "snapshot_commit": REVISION, "records": records}, indent=2) + "\n"
    files[Path("README.md")] = (f"# NHS England - {CAPTURE}\n\n"
        f"- [C5 Appointments Management - GP, version 1.5.0]({cap.as_posix()}/README.md): "
        "9 MUST epics, 27 MAY epics and 56 acceptance criteria.\n"
        f"- [S62 version 4.0.1: {DATA_RULE}]({rule.as_posix()}): appointment mode only.\n"
        "- [Machine-readable index](index.json)\n\n"
        "This pilot does not extract the entire S62 standard or other capabilities and dependencies. "
        "Priority labels and requirement wording come from the publisher; do not infer missing priorities or current applicability.\n")
    return files


def write_or_check(root, files, check):
    for path, text in files.items():
        target = root / path
        require(not any(parent.is_symlink() for parent in (target, *target.parents)), f"Refusing symlink: {target}")
        if target.exists() or check:
            require(target.is_file() and target.read_text(encoding="utf-8") == text,
                    f"Missing or changed generated file: {target}. Move old output aside before regenerating.")
    if not check:
        for path, text in files.items():
            target = root / path
            if not target.exists():
                target.parent.mkdir(parents=True, exist_ok=True)
                with target.open("x", encoding="utf-8") as file:
                    file.write(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify existing files without writing them")
    args = parser.parse_args()
    try:
        files = generate()
        write_or_check(OUTPUT, files, args.check)
    except (OSError, ValueError) as exc:
        parser.exit(1, f"s/extract-spec: {exc}\n")
    print(f"{'Verified' if args.check else 'Generated'} the C5/S62 pilot ({len(files)} files) in {OUTPUT}/")
