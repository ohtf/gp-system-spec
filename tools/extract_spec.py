# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Extract an implementation reference from the pinned July NHS capture."""

import argparse
from collections import Counter
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess
from urllib.parse import quote, unquote, urljoin, urlsplit

from bs4 import BeautifulSoup, Comment, NavigableString, Tag
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
RULE_PATH = Path(f"standards/S62-appointments-data-reporting/4.0.1/{DATA_RULE}.md")
MATRIX_RAW = Path(".raw/GPITF/1391134009.html")
PAGE_LINK = re.compile(r"/wiki/spaces/DCSDCS/pages/(\d+)(?:/.*)?")
CRITERION = re.compile(r"Acceptance criteri(?:on|a)\b", re.I)
HTML_TAGS = set("div span strong b em i u a p ul ol li br hr h2 h3 h4 sup sub time table thead tbody tr td th colgroup col".split())
HTML_ATTRS = {"a": {"href"}, "time": {"datetime"}, "ol": {"start"}, "td": {"colspan", "rowspan"}, "th": {"colspan", "rowspan"}}
BLOCK_TAGS = set("div p ul ol hr h2 h3 h4 table".split())


def captured(path):
    result = subprocess.run(["git", "show", f"{REVISION}:{BASE / path}"], capture_output=True)
    if result.returncode:
        raise ValueError(f"Cannot read July capture file {path}. Fetch the nhs-futures/2026-07-31 tag.")
    return result.stdout


def require(condition, message):
    if not condition:
        raise ValueError(message)


def linked_page(url):
    parts = urlsplit(url)
    match = PAGE_LINK.fullmatch(parts.path)
    return match[1] if parts.hostname in {"nhse-dsic.atlassian.net", "gpitbjss.atlassian.net"} and match else None


def matrix_capabilities(raw):
    table = BeautifulSoup(raw, "html.parser").find("table")
    require(table is not None and table.tr is not None, "Missing matrix table")
    columns = [cell.get_text(" ", strip=True) for cell in table.tr.find_all("td", recursive=False)]
    require(len(columns) == 3 and columns[0] == "Overarching Standards"
            and all(label.startswith("Capabilities that can") for label in columns[1:]), "Unexpected matrix columns")
    pages = []
    for row in table.find_all("tr"):
        for cell in row.find_all("td", recursive=False)[1:]:  # First column lists overarching standards.
            for heading in cell.find_all("h3"):
                links = heading.select("a[href]")
                require(len(links) == 1 and (page_id := linked_page(links[0]["href"])),
                        f"Unrecognised matrix capability: {heading.get_text(strip=True)}")
                require(page_id not in pages, f"Duplicate matrix capability page: {page_id}")
                pages.append(page_id)
    require(len(pages) == 37, f"Unexpected matrix capability count: {len(pages)}")
    return pages


def archive_url(path):
    page = path.parent if path.name == "index.md" else path.with_suffix("")
    return ARCHIVE + quote(page.as_posix()) + "/"


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
        metadata[name] = ([p.get_text(strip=True) for p in value.select("p") if p.get_text(strip=True)]
                          if name in {"Contracting Vehicle(s)", "Framework(s)"} else value.get_text(" ", strip=True))

    reference = {
        "publisher": "NHS England", "jurisdiction": "England", "capture_date": CAPTURE,
        "snapshot_tag": f"nhs-futures/{CAPTURE}", "snapshot_commit": REVISION,
        "confluence_page_id": page_id, "confluence_version": header["version"],
        "title": header["title"], "source_url": header["source_url"],
        "archive_url": archive_url(path),
        "source_file": (BASE / raw_path).as_posix(), "source_sha256": hashlib.sha256(raw).hexdigest(),
        "specification_id": metadata["ID"], "publisher_version": metadata["Version"],
        "status_at_capture": metadata["Status"], "effective_date": metadata["Effective Date"],
        "type": metadata["Type"],
    }
    for label, key in (("Contracting Vehicle(s)", "contracting_vehicles"), ("Framework(s)", "frameworks"), ("Category", "category")):
        if label in metadata:
            reference[key] = metadata[label]
    return soup, reference


def visible_text(node):
    """Compare words and punctuation, ignoring whitespace introduced by layout."""
    if isinstance(node, Comment):
        return ""
    if isinstance(node, NavigableString):
        return str(node)
    text = "".join(visible_text(child) for child in node.children)
    return f" {text} " if node.name in {"div", "p", "ul", "ol", "li", "h2", "h3", "h4", "br", "tr", "td", "th"} else text


def source_fragment(nodes):
    return BeautifulSoup("".join(node.output_ready() if isinstance(node, NavigableString) else str(node)
                                 for node in nodes), "html.parser")


def hrefs(fragment):
    return [link["href"] for link in fragment.select("a[href]")]


def structure(fragment):
    """Check list ownership, table cell boundaries, headings and explicit line breaks."""
    selector = "ul, ol, li, h2, h3, h4, br, table, thead, tbody, tr, td, th, u, time"
    structural = set(selector.split(", "))
    return [(node.name, tuple(p.name for p in node.parents if p.name in structural), node.attrs,
             " ".join(visible_text(node).split())) for node in fragment.select(selector)]


def render_blocks(nodes, source_url):
    original = source_fragment(nodes)
    wording = visible_text(original).split()
    links = [urljoin(source_url, href) for href in hrefs(original)]
    for comment in original.find_all(string=lambda s: isinstance(s, Comment)):
        comment.extract()
    for tag in original.find_all(True):
        require(tag.name in HTML_TAGS, f"Unreviewed source element: {tag.name}")
        tag.attrs = {key: value for key, value in tag.attrs.items() if key in HTML_ATTRS.get(tag.name, ())}
        if tag.name == "h4":
            tag.name = "h2"
    for link, href in zip(original.select("a[href]"), links, strict=True):
        require(urlsplit(href).scheme in {"http", "https"}, "Unexpected source link scheme")
        link["href"] = href

    def signature(fragment):
        return visible_text(fragment).split(), hrefs(fragment), structure(fragment)

    def markdown_signature(output):
        return signature(BeautifulSoup(markdown(output), "html.parser"))

    def as_markdown(html):
        return markdownify(html, heading_style="ATX", bullets="-", strip_document="strip").strip()

    output = as_markdown(str(original))
    expected = wording, links, structure(original)
    if markdown_signature(output) == expected:
        return output

    # Keep clean HTML only where Markdown loses structure or wording. Group adjacent
    # inline nodes (including bare text) so they don't gain paragraph breaks.
    chunks = []
    inline = []
    for node in original.children:
        if isinstance(node, Tag) and node.name in BLOCK_TAGS:
            if inline:
                chunks.append(inline)
                inline = []
            chunks.append([node])
        else:
            inline.append(node)
    if inline:
        chunks.append(inline)
    blocks = []
    for chunk in chunks:
        source = source_fragment(chunk)
        plain = as_markdown(str(source))
        if markdown_signature(plain) == signature(source):
            blocks.append(plain)
        else:
            # HTML block lines can be long; preserve inline spacing without prettify().
            blocks.append(f"<div>{str(source).strip()}</div>")
    output = "\n\n".join(block for block in blocks if block)
    require(markdown_signature(output) == expected, "Rendering changed source wording, links or structure")
    return output


def heading_text(node):
    return " ".join(visible_text(node).split())


def extract_epics(container, pattern):
    epics = []
    for node in container.children:
        if not isinstance(node, Tag) and not heading_text(node):
            continue
        if isinstance(node, Tag) and node.name == "h3":
            label = heading_text(node)
            match = pattern.fullmatch(label)
            require(match is not None and node.get("id"), f"Unrecognised epic heading or missing source anchor: {label}")
            epics.append({"id": match[1], "label": label, "anchor": node["id"], "blocks": []})
        elif epics:
            epics[-1]["blocks"].append(node)
        else:
            require(not heading_text(node), "Unexpected content before first epic")
    for epic in epics:
        blocks = epic["blocks"]
        while blocks and (not isinstance(blocks[-1], Tag) or blocks[-1].name in {"p", "hr"}) and not heading_text(blocks[-1]):
            blocks.pop()  # Blank lines and epic dividers.
        require(len(blocks) > 3 and all(isinstance(node, Tag) and node.name == "p" for node in blocks[:3])
                and isinstance(blocks[3], Tag) and blocks[3].name == "h4",
                f"Unrecognised user story: {epic['id']}")
        epic["criteria"] = sum(bool(CRITERION.match(heading_text(node))) for node in blocks[3:]
                               if isinstance(node, Tag) and node.name == "h4")
        require(epic["criteria"] > 0, f"No acceptance criteria for {epic['id']}")
    return epics


def capability_sections(soup, specification_id):
    """Read the captured Confluence layout in cell order, including bare description text."""
    sections = []
    metadata = soup.select_one("div.plugin-tabmeta-details")
    require(metadata is not None, "Missing capability metadata block")
    headings = set()
    for node in (child for cell in soup.select("div.innerCell") for child in cell.children):
        if node is metadata:
            continue
        if isinstance(node, Tag) and node.name in {"h1", "h2"}:
            title = heading_text(node)
            require(title in {"Description", "Outcomes", "Roadmap"} and node.get("id"), f"Unknown source section: {title}")
            headings.add(id(node))
            sections.append({"id": title.lower(), "title": title, "anchor": node["id"], "blocks": []})
            continue
        table = node.find("table") if isinstance(node, Tag) else None
        group = LEVEL.match(heading_text(table.tr)) if table else None
        if group:
            cells = table.find_all("td")
            require(len(cells) == 2 and len(table.find_all("tr")) == 2, f"Unexpected {group[1]} epic layout")
            headings.update(map(id, cells[1].find_all("h3", recursive=False)))
            sections.append({"id": f"{group[1].lower()}-epics", "title": f"{group[1]} Epics",
                             "priority": group[1], "blocks": cells[0].contents, "epics": extract_epics(cells[1], EPIC)})
        elif isinstance(node, Tag) and "panel" in node.get("class", []):
            require(specification_id == "C41", "Unreviewed capability panel")
            header, content = node.find_all(recursive=False)
            title = heading_text(header)
            if LEVEL.match(title):
                headings.update(map(id, content.find_all("h3", recursive=False)))
                examples = extract_epics(content, re.compile(r"(C41E[12])\s+-\s+(.+)"))
                require([item["id"] for item in examples] == ["C41E1", "C41E2"], "Unexpected C41 examples")
                sections.append({"id": "must-epic-guidance", "title": "MUST Epics", "blocks": header.contents,
                                 "examples": examples})
            else:
                labels = {"Capability Specific Standards": "capability-specific-standards",
                          "Other Applicable Standards": "other-applicable-standards",
                          "Items on the Roadmap which impact or relate to this Capability": "roadmap"}
                require(title in labels, f"Unreviewed C41 panel: {title}")
                sections.append({"id": labels[title], "title": title, "blocks": content.contents})
        elif sections and not ({"epics", "examples"} & sections[-1].keys()):
            sections[-1]["blocks"].append(node)
        else:
            require(not heading_text(node), "Unexpected content outside capability sections")
    expected = (["description", "outcomes", "must-epic-guidance", "capability-specific-standards",
                 "other-applicable-standards", "roadmap"] if specification_id == "C41"
                else ["description", "outcomes", "must-epics", "may-epics", "roadmap"])
    require([section["id"] for section in sections] == expected, "Unreviewed capability section order")
    require({id(node) for node in soup.select("h1, h2, h3")} == headings, "Unmapped capability headings")
    epic_ids = [epic["id"] for section in sections for epic in section.get("epics", [])]
    require(len(epic_ids) == len(set(epic_ids)), "Duplicate epic IDs in capability edition")
    return sections


def document(reference, title, body):
    frontmatter = yaml.safe_dump(reference, allow_unicode=True, sort_keys=False, width=120)
    url = reference["archive_url"]
    anchor = f"#{quote(reference['anchor'], safe='')}" if reference.get("anchor") else ""
    return (f"---\n{frontmatter}---\n\n# {title}\n\n"
            f"[Archived source](<{url}{anchor}>) · [Publisher](<{reference['source_url']}{anchor}>)\n\n{body}\n")


def relative_link(label, path, origin):
    label = re.sub(r"([\\\[\]*_`<>])", r"\\\1", label)
    return f"[{label}]({os.path.relpath(path, origin.parent)})"


def capability_path(source):
    spec_id, version = source["specification_id"], source["publisher_version"]
    require(re.fullmatch(r"C\d+", spec_id) and re.fullmatch(r"\d+\.\d+\.\d+", version), "Unrecognised capability edition")
    slug = re.sub(r"[^a-z0-9]+", "-", source["title"].lower()).strip("-")
    return Path("capabilities") / f"{spec_id}-{slug}" / version


def epic_path(cap, epic, priority):
    folder = cap / "epics" / priority.lower() if priority else cap / "examples"
    return folder / f"{epic['id']}.md"


def extracted_links(blocks, source_url, path, destinations):
    links = {}
    for href in hrefs(source_fragment(blocks)):
        url = urljoin(source_url, href)
        if target := destinations.get((linked_page(url), unquote(urlsplit(url).fragment))):
            target_path, label = target
            if target_path != path:
                links[target_path] = relative_link(label, target_path, path)
    return list(links.values())


def render_capability(source, sections, cap, destinations, files, records):
    index = cap / "README.md"
    intro = "Read the source sections and epics below. Status and priorities are those in the capture."
    if source["specification_id"] == "C41":
        intro = "This deprecated capability has supplier-defined requirements. Its two templates are source examples, not numbered requirements."
    context = []
    priorities = Counter()
    criteria = Counter()
    examples = 0
    for section in sections:
        title = section["title"]
        section_path = cap / "sections" / f"{section['id']}.md"
        context.append(f"\n## {relative_link(title, section_path, index)}\n")
        locator = {key: section[key] for key in ("anchor", "priority") if key in section}
        priority = section.get("priority")
        body = render_blocks(section["blocks"], source["source_url"])
        records.append({"kind": "section", "id": section["id"], "path": section_path.as_posix(), "title": title,
                        "specification_id": source["specification_id"], "publisher_version": source["publisher_version"], **locator})
        links = []
        for epic in section.get("epics", section.get("examples", [])):
            path = epic_path(cap, epic, priority)
            epic_metadata = {"anchor": epic["anchor"]}
            if priority:
                priorities[priority] += 1
                criteria[priority] += epic["criteria"]
                epic_metadata.update(epic_id=epic["id"], priority=priority, acceptance_criterion_count=epic["criteria"])
            else:
                examples += 1
                epic_metadata.update(example_id=epic["id"], sample_acceptance_criterion_count=epic["criteria"])
            story = render_blocks(epic["blocks"][:3], source["source_url"])
            details = render_blocks(epic["blocks"][3:], source["source_url"])
            epic_body = f"## User story\n\n{story}\n\n{details}"
            if not priority:
                epic_body = "Publisher example, not a numbered requirement.\n\n" + epic_body
            local_links = extracted_links(epic["blocks"], source["source_url"], path, destinations)
            if DATA_RULE in details:
                local_links.append(relative_link(f"Open the extracted {DATA_RULE} rule", RULE_PATH, path))
            if local_links:
                epic_body += "\n\n## Archive cross-reference\n\n" + "\n".join(f"- {link}" for link in local_links)
            files[path] = document({**source, **epic_metadata}, epic["label"], epic_body)
            links.append(f"- {relative_link(epic['label'], path, section_path)}")
            context.append(f"- {relative_link(epic['label'], path, index)}")
            records.append({"kind": "epic" if priority else "source-example", "id": epic["id"],
                            "path": path.as_posix(), "title": epic["label"], "specification_id": source["specification_id"],
                            "publisher_version": source["publisher_version"], **epic_metadata})
        if links:
            body += ("\n\n## Epic index\n\n" if priority else "\n\n## Source examples\n\n") + "\n".join(links)
        files[section_path] = document({**source, "section_id": section["id"], **locator}, title, body)
    files[index] = document(source, source["title"], intro + "\n" + "\n".join(context).rstrip())
    return {**source, "path": index.as_posix(), "epic_counts": dict(priorities),
            "acceptance_criterion_counts": dict(criteria), "source_example_count": examples}


def extract_standard(manifest, files, records):

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
    body = "\n\n".join(f"## {label}\n\n{render_blocks(cell.contents, source['source_url'])}"
                       for label, cell in zip(("Data item", "Requirement text", "Level"), cells[1:], strict=True))
    files[RULE_PATH] = document(source, f"{DATA_RULE} - {cells[1].get_text(' ', strip=True)}", body)
    records.append({"kind": "standard-rule", "id": DATA_RULE, "path": RULE_PATH.as_posix(), "specification_id": "S62",
                    "publisher_version": source["publisher_version"], "priority": source["priority"], "anchor": source["anchor"]})


def generate():
    manifest = json.loads(captured(Path(".mirror-manifest.json")))
    matrix = captured(MATRIX_RAW)
    pages = matrix_capabilities(matrix)
    files, records, capabilities, destinations = {}, [], [], {}
    for page in pages:
        soup, source = read_page(manifest, page)
        spec_id = source["specification_id"]
        require(source["type"] == "Capability", f"Matrix entry is not a capability: {spec_id}")
        try:
            sections = capability_sections(soup, spec_id)
        except ValueError as exc:
            raise ValueError(f"{spec_id}: {exc}") from exc
        cap = capability_path(source)
        capabilities.append((source, sections, cap))
        destinations[page, ""] = (cap / "README.md", f"{spec_id} {source['title']}")
        for section in sections:
            if "anchor" in section:
                destinations[page, section["anchor"]] = (cap / "sections" / f"{section['id']}.md", f"{spec_id} {section['title']}")
            for epic in section.get("epics", section.get("examples", [])):
                destinations[page, epic["anchor"]] = (epic_path(cap, epic, section.get("priority")), f"{spec_id} {epic['label']}")
    require(len({source["specification_id"] for source, _, _ in capabilities}) == len(pages), "Duplicate capability IDs")
    catalogue = []
    for source, sections, cap in capabilities:
        try:
            catalogue.append(render_capability(source, sections, cap, destinations, files, records))
        except ValueError as exc:
            raise ValueError(f"{source['specification_id']}: {exc}") from exc
    catalogue.sort(key=lambda entry: int(entry["specification_id"][1:]))
    extract_standard(manifest, files, records)
    epics, criteria = Counter(), Counter()
    for entry in catalogue:
        epics.update(entry["epic_counts"])
        criteria.update(entry["acceptance_criterion_counts"])
    require(epics == {"MUST": 124, "MAY": 347} and criteria == {"MUST": 301, "MAY": 585}, "Unexpected snapshot epic or criterion coverage")

    matrix_page = manifest["GPITF/1391134009"]
    matrix_url = archive_url(Path(matrix_page["path"]))
    inventory = {"archive_url": matrix_url, "confluence_page_id": "1391134009", "confluence_version": matrix_page["version"],
                 "source_file": (BASE / MATRIX_RAW).as_posix(),
                 "source_sha256": hashlib.sha256(matrix).hexdigest()}
    summary = {"capability_count": len(catalogue), "epic_counts": dict(epics), "acceptance_criterion_counts": dict(criteria),
               "source_example_count": sum(entry["source_example_count"] for entry in catalogue)}
    files[Path("index.json")] = json.dumps({"schema_version": 2, "snapshot_commit": REVISION, "capture_date": CAPTURE,
                                            "matrix": inventory, "summary": summary, "capabilities": catalogue,
                                            "records": records}, indent=2, ensure_ascii=False) + "\n"
    index = Path("README.md")
    lines = [f"# NHS England - {CAPTURE}", "",
             f"All {len(catalogue)} capabilities linked from the [captured GP IT Futures matrix]({matrix_url}). "
             f"{epics.total()} numbered epics ({epics['MUST']} MUST, {epics['MAY']} MAY), {criteria.total()} acceptance criteria "
             f"and {summary['source_example_count']} source examples. This is a historical reference, not a statement of current applicability.",
             "", "[Machine-readable catalogue](index.json)", "", "## Capabilities", "",
             "| Capability | Version | Status at capture | MUST | MAY | Criteria |", "| --- | --- | --- | ---: | ---: | ---: |"]
    for entry in catalogue:
        link = relative_link(f"{entry['specification_id']} {entry['title']}", Path(entry["path"]), index)
        lines.append(f"| {link} | {entry['publisher_version']} | {entry['status_at_capture']} | "
                     f"{entry['epic_counts'].get('MUST', 0)} | {entry['epic_counts'].get('MAY', 0)} | "
                     f"{sum(entry['acceptance_criterion_counts'].values())} |")
    lines.extend(("", "## Standard extract", "", f"- [S62 v4.0.1: {DATA_RULE}]({RULE_PATH}): appointment mode only. "
                  "Other standards, matrix dependencies and attachment contents are not extracted."))
    files[index] = "\n".join(lines) + "\n"
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
    print(f"{'Verified' if args.check else 'Generated'} the GP IT Futures reference ({len(files)} files) in {OUTPUT}/")
