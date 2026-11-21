# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Restore tables from captured Confluence HTML in the staging tree only."""

import posixpath
import re
import unicodedata
from urllib.parse import parse_qs, quote, unquote, urljoin, urlsplit

from bs4 import BeautifulSoup, Comment

NHS = "https://nhse-dsic.atlassian.net"
NHS_HOSTS = {"nhse-dsic.atlassian.net", "gpitbjss.atlassian.net"}
TABLE_BLOCK = re.compile(r"(?m)(?:^\|[^\n]*(?:\n|\Z))+")
ANCHOR_MARKER = re.compile(r"\{#([^\s{}]+)\}")
TABLE_TAGS = set("table caption thead tbody tfoot tr th td".split())
CONTENT_TAGS = set("h1 h2 h3 h4 h5 h6 p br hr ul ol li blockquote div span strong b em i u del s sub sup a img pre code time".split())
DISCARD = set("script style iframe svg math object embed template input button select textarea fieldset noscript".split())
EPIC_GROUP = re.compile(r"^(?:MUST|SHOULD|MAY)\s+Epics\b", re.I)
RASTER_EXTENSIONS = (".png", ".jpg", ".jpeg", ".gif", ".webp")


def normalise(text):
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", text).casefold())


def chapter_fragment(fragment, anchors):
    fragment = unquote(fragment)
    if fragment in anchors:
        return fragment
    # Some source links use a heading slug without Confluence's page-title prefix.
    # Only an exact or unique normalised suffix is accepted, never a fuzzy match.
    key = normalise(fragment)
    if len(key) < 10 or ":~:" in fragment:
        return None
    matches = [anchor for anchor in anchors if normalise(anchor).endswith(key)]
    return matches[0] if len(matches) == 1 else None


def link_target(value, source, pages, downloads, image=False):
    """Resolve trusted Confluence references without emitting active URLs."""
    if not value or re.search(r"[\x00-\x1f\x7f\\]", value):
        return None
    value = value.strip()
    if not value:
        return None
    source_path, source_url, source_ids = source
    try:
        url = urlsplit(urljoin(source_url, value))
    except ValueError:
        return None
    if url.scheme == "mailto" and not image:
        return value
    if url.scheme not in {"https", "http"} or not url.hostname or url.username is not None:
        return None
    if value.startswith("#"):
        if image:
            return None
        if fragment := chapter_fragment(url.fragment, source_ids):
            return "#" + quote(fragment, safe="")
        return url.geturl()  # Preserve the original source link instead of inventing a target.
    if url.hostname in NHS_HOSTS:
        if preview := parse_qs(url.query).get("preview"):
            parts = preview[0].strip("/").split("/", 2)
            if len(parts) == 3 and not image:
                page_id, attachment_id, name = parts
                if target := downloads.get((page_id, attachment_id.removeprefix("att"), name)):
                    return target
        if match := re.fullmatch(r"/wiki/download/attachments/(\d+)/(.+)", url.path):
            page_id, name = match[1], unquote(match[2])
            if target := downloads.get((page_id, None, name)):
                if not image or name.lower().endswith(RASTER_EXTENSIONS):
                    return target
            if image:
                return None
        if not image and not url.query and (match := re.search(r"/pages/(\d+)(?:/|$)", url.path)):
            if target := pages.get(match[1]):
                path, _, anchors = target
                fragment = chapter_fragment(url.fragment, anchors) if url.fragment else ""
                if fragment is not None:
                    suffix = "#" + quote(fragment, safe="") if fragment else ""
                    if path == source_path and suffix:
                        return suffix
                    # Zensical rewrites HTML hrefs relative to the Markdown source.
                    return quote(posixpath.relpath(path, source_path.parent), safe="/") + suffix
    return None if image else url.geturl()


def clean_table(table, source, pages, downloads):
    for tag in list(table.find_all(True)):
        if not tag.name:  # The parent was already removed.
            continue
        name, attrs = tag.name, tag.attrs
        if name in DISCARD or set(attrs.get("class", ())) & {"aui-icon", "expand-control-icon"}:
            tag.decompose()
            continue
        if name not in TABLE_TAGS | CONTENT_TAGS:
            if name == "colgroup":
                tag.decompose()  # Keep semantic spans, not Confluence's fixed widths.
            else:
                tag.unwrap()
            continue
        tag.attrs = {}
        if anchor := attrs.get("id"):
            tag["id"] = anchor
        for attr in ({"rowspan", "colspan"} if name in {"td", "th"} else {"start"} if name == "ol" else ()):
            if re.fullmatch(r"\d{1,3}", attrs.get(attr, "")):
                tag[attr] = attrs[attr]
        if name == "th" and attrs.get("scope") in {"row", "col", "rowgroup", "colgroup"}:
            tag["scope"] = attrs["scope"]
        if name == "a":
            if attrs.get("name"):
                tag["name"] = attrs["name"]
            if href := link_target(attrs.get("href", ""), source, pages, downloads):
                tag["href"] = href
        if name == "img":
            if src := link_target(attrs.get("src", ""), source, pages, downloads, image=True):
                tag.attrs.update(src=src, alt=attrs.get("alt", ""), loading="lazy")
            else:
                alt = attrs.get("data-emoji-fallback") or attrs.get("alt", "")
                if alt:
                    tag.replace_with(alt)
                else:
                    tag.decompose()
        if name == "time" and attrs.get("datetime"):
            tag["datetime"] = attrs["datetime"]
    for comment in table.find_all(string=lambda text: isinstance(text, Comment)):
        comment.extract()
    table.attrs = {"id": table["id"]} if table.has_attr("id") else {}


def render_table(table, source, pages, downloads):
    clean_table(table, source, pages, downloads)
    rows = [row.find_all(["th", "td"], recursive=False) for row in table.find_all("tr")]
    layout_only = (
        rows
        and all(len(row) == 1 and row[0].name == "td" and not {"rowspan", "colspan"} & row[0].attrs.keys() for row in rows)
        and EPIC_GROUP.match(rows[0][0].get_text(" ", strip=True))
        and table.find("h3")
        and not table.has_attr("id")
        and not any(tag.has_attr("id") for tag in table.find_all(["tbody", "tr", "td"]))
    )
    if layout_only:
        # These are prose sections that Confluence wrapped in a one-column table.
        return '<section class="archive-epics">' + "\n".join(row[0].decode_contents() for row in rows) + "</section>"
    return '<div class="archive-table">' + str(table) + '</div>'


def restore_tables(text, raw, source, pages, downloads, legacy_anchors):
    source_path, _, _ = source
    soup = BeautifulSoup(raw, "html.parser")
    tables = [table for table in soup.find_all("table") if table.find_parent("table") is None]
    # The old renderer emitted malformed separators for a few nested tables.
    # A stray standalone pipe is not a table (two consultations pages have one).
    blocks = [m for m in TABLE_BLOCK.finditer(text) if len(m[0].splitlines()) > 1]
    if len(tables) != len(blocks):
        raise ValueError(f"table alignment in {source_path}: {len(tables)} source tables, {len(blocks)} Markdown tables")
    parts = []
    cursor = 0
    for number, (table, block) in enumerate(zip(tables, blocks, strict=True), 1):
        # Fail closed if the two snapshots pair a table with unrelated content.
        words = {normalise(word)[:72] for word in table.stripped_strings}
        witnesses = sorted(words - {""}, key=lambda word: (-len(word), word))[:10]
        old = normalise(block[0])
        if witnesses and not any(word in old for word in witnesses):
            raise ValueError(f"table {number} in {source_path} does not match the captured Markdown")
        parts.append(text[cursor:block.start()])
        # Keep explicitly verified legacy fragments when the table is rebuilt.
        for canonical, alias in legacy_anchors.items():
            if tag := table.find(id=canonical):
                marker = soup.new_tag("span", id=alias)
                tag.insert(0, marker)
        parts.append(render_table(table, source, pages, downloads) + "\n")
        cursor = block.end()
    parts.append(text[cursor:])
    return "".join(parts), len(tables)
