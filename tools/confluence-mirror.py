#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""
Confluence space mirror scraper.

Fetches pages, attachments and rendered HTML from Confluence REST API v2,
converts to Markdown, and writes a Git-friendly directory tree.

Usage:
    s/scrape [--space KEY] [--output-dir DIR] [--full-refresh] [--dry-run] [--validate]

Environment variables (optional - anonymous access used by default):
    CONFLUENCE_EMAIL      Atlassian account email
    CONFLUENCE_API_TOKEN  Atlassian API token
"""

import argparse
import json
import os
import re
import sys
import time
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs, quote, unquote_plus

import requests
from bs4 import BeautifulSoup, NavigableString
from markdownify import markdownify as md

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

TENANTS = {
    "nhse-dsic": {
        "base": "https://nhse-dsic.atlassian.net/wiki",
        "spaces": ["DCSDCS", "GPITF", "GIFTIF", "DFOCVCL", "CPCSH", "DPSR", "BG"],
    },
}

DOCS_ROOT = Path(__file__).parent.parent / "docs"

# Raw rendered HTML is an archival input for reprocessing, so it lives in a
# dot-directory the site generator ignores. Attachments are different: pages link
# to them, so they must sit in a published directory or every attachment link on
# the site 404s.
def set_output_root(root: Path) -> None:
    global DOCS_ROOT, MANIFEST_PATH, FAILURE_REPORT_PATH, RAW_ROOT, ATTACHMENTS_ROOT
    DOCS_ROOT = root.resolve()
    MANIFEST_PATH = DOCS_ROOT / ".mirror-manifest.json"
    FAILURE_REPORT_PATH = DOCS_ROOT / ".mirror-failures.json"
    RAW_ROOT = DOCS_ROOT / ".raw"
    ATTACHMENTS_ROOT = DOCS_ROOT / "attachments"


set_output_root(DOCS_ROOT)

REQUEST_INTERVAL = 1.5  # seconds between requests, including redirects
MAX_RETRY_WAIT = 120    # stop rather than scheduling a long unattended wait
MAX_RETRIES = 4
PAGE_LIMIT = 250


# ---------------------------------------------------------------------------
# HTTP session
# ---------------------------------------------------------------------------

class StopMirror(RuntimeError):
    """Stop all requests when access is blocked or throttling persists."""


class PacedSession(requests.Session):
    next_request = 0.0

    def send(self, request, **kwargs):
        wait = self.next_request - time.monotonic()
        if wait > 0:
            time.sleep(wait)
        self.next_request = time.monotonic() + REQUEST_INTERVAL
        return super().send(request, **kwargs)


def make_session() -> requests.Session:
    session = PacedSession()
    email = os.environ.get("CONFLUENCE_EMAIL")
    token = os.environ.get("CONFLUENCE_API_TOKEN")
    if email and token:
        session.auth = (email, token)
        print("INFO: using authenticated access", file=sys.stderr)
    else:
        print("INFO: using anonymous access", file=sys.stderr)
    session.headers["Accept"] = "application/json"
    return session


def retry_after(value: str | None, fallback: int) -> float:
    if value is not None:
        try:
            return max(float(int(value)), REQUEST_INTERVAL)
        except ValueError:
            try:
                when = parsedate_to_datetime(value)
                if when.tzinfo is None:
                    when = when.replace(tzinfo=timezone.utc)
                return max((when - datetime.now(timezone.utc)).total_seconds(), REQUEST_INTERVAL)
            except (ValueError, TypeError, OverflowError):
                pass
    return fallback


def get(session: requests.Session, url: str, **kwargs) -> requests.Response:
    kwargs.setdefault("timeout", 30)
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, **kwargs)
        except (requests.Timeout, requests.ConnectionError):
            if attempt == MAX_RETRIES:
                raise
            time.sleep(2 ** attempt)
            continue
        status = resp.status_code
        if status in (401, 403) or urlparse(resp.url).hostname == "id.atlassian.com":
            resp.close()
            raise StopMirror(f"access denied or sign-in required (HTTP {status})")
        if status in (429, 502, 503, 504):
            wait = retry_after(resp.headers.get("Retry-After"), 15 * 2 ** (attempt - 1))
            resp.close()
            if status == 429 and (attempt == MAX_RETRIES or wait > MAX_RETRY_WAIT):
                raise StopMirror(f"rate limit persists; retry no sooner than {wait:.0f}s")
            if attempt < MAX_RETRIES and wait <= MAX_RETRY_WAIT:
                print(f"  HTTP {status}; waiting {wait:.0f}s before retry", file=sys.stderr)
                time.sleep(wait)
                continue
        if status >= 400:
            resp.close()
            raise RuntimeError(f"HTTP {status}")
        return resp
    raise RuntimeError(f"failed after {MAX_RETRIES} retries: {url}")


# ---------------------------------------------------------------------------
# Manifest (incremental runs)
# ---------------------------------------------------------------------------

def load_manifest() -> dict:
    if MANIFEST_PATH.exists():
        return json.loads(MANIFEST_PATH.read_text())
    return {}


def save_manifest(manifest: dict) -> None:
    MANIFEST_PATH.parent.mkdir(parents=True, exist_ok=True)
    MANIFEST_PATH.write_text(json.dumps(manifest, indent=2, sort_keys=True))


def load_failure_report() -> dict:
    if FAILURE_REPORT_PATH.exists():
        return json.loads(FAILURE_REPORT_PATH.read_text(encoding="utf-8"))
    return {"schema_version": 1, "failures": []}


def record_failures(failures: list[str]) -> None:
    """Merge newly observed failures into the durable unresolved failure report."""
    report = load_failure_report()
    known_messages = {failure["message"] for failure in report["failures"]}
    for message in failures:
        if message not in known_messages:
            report["failures"].append({"kind": "scrape", "message": message, "status": "unresolved"})
    report["failures"].sort(key=lambda failure: failure["message"])
    FAILURE_REPORT_PATH.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")


# ---------------------------------------------------------------------------
# Slug / path helpers
# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
    text = text.strip()
    text = re.sub(r"[^\w\s\-]", "", text, flags=re.UNICODE)
    text = re.sub(r"\s+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-")[:120]


def build_ancestor_chain(page_id: str, pages_by_id: dict) -> list[str]:
    """Return list of ancestor titles from root to immediate parent."""
    chain = []
    current = pages_by_id.get(page_id, {})
    parent_id = current.get("parentId")
    while parent_id and parent_id in pages_by_id:
        parent = pages_by_id[parent_id]
        chain.append(parent["title"])
        parent_id = parent.get("parentId")
    chain.reverse()
    return chain


def page_output_path(space_key: str, ancestors: list[str], title: str, has_children: bool) -> Path:
    """
    Pages with children -> <space>/<ancestor...>/<slug>/index.md
    Leaf pages          -> <space>/<ancestor...>/<slug>.md
    """
    parts = [space_key] + [slugify(a) for a in ancestors]
    slug = slugify(title)
    if has_children:
        parts.append(slug)
        return DOCS_ROOT.joinpath(*parts) / "index.md"
    return DOCS_ROOT.joinpath(*parts) / f"{slug}.md"


# ---------------------------------------------------------------------------
# Space enumeration - builds full page list from parentId, no extra calls
# ---------------------------------------------------------------------------

def enumerate_pages(session: requests.Session, base_url: str, space_key: str) -> list[dict]:
    resp = get(session, f"{base_url}/api/v2/spaces", params={"keys": space_key})
    spaces = resp.json().get("results", [])
    if not spaces:
        print(f"  {space_key}: not found", file=sys.stderr)
        return []
    space_id = spaces[0]["id"]

    pages = list(iter_results(session, f"{base_url}/api/v2/spaces/{space_id}/pages", PAGE_LIMIT))
    print(f"  {space_key}: {len(pages)} pages enumerated", file=sys.stderr)
    return pages


def iter_results(session: requests.Session, url: str, limit: int):
    cursor = None
    seen = set()
    while True:
        params = {"limit": limit}
        if cursor:
            params["cursor"] = cursor
        with get(session, url, params=params) as resp:
            data = resp.json()
        yield from data["results"]
        next_link = data.get("_links", {}).get("next")
        if not next_link:
            break
        qs = parse_qs(urlparse(next_link).query)
        cursor = qs.get("cursor", [None])[0]
        if not cursor or cursor in seen:
            raise RuntimeError("missing or repeated pagination cursor")
        seen.add(cursor)


# ---------------------------------------------------------------------------
# Page body fetch
# ---------------------------------------------------------------------------

def fetch_page_body(session: requests.Session, base_url: str, page_id: str) -> tuple[str, dict]:
    """Fetch rendered body and full metadata for a single page."""
    resp = get(
        session,
        f"{base_url}/api/v2/pages/{page_id}",
        params={"body-format": "export_view", "include-labels": "true"},
    )
    detail = resp.json()
    html = (
        detail.get("body", {}).get("export_view", {}).get("value", "")
        or detail.get("body", {}).get("view", {}).get("value", "")
    )
    return html, detail


# ---------------------------------------------------------------------------
# Attachment download
# ---------------------------------------------------------------------------

def download_attachments(
    session: requests.Session, base_url: str, page_id: str, space_key: str
) -> list[dict]:
    att_dir = ATTACHMENTS_ROOT / space_key / page_id
    results = []
    cursor = None
    while True:
        params = {"limit": 50}
        if cursor:
            params["cursor"] = cursor
        resp = get(session, f"{base_url}/api/v2/pages/{page_id}/attachments", params=params)
        data = resp.json()
        for att in data.get("results", []):
            att_id = att["id"]
            filename = att.get("title", att_id)
            download_url = att.get("downloadLink") or att.get("_links", {}).get("download")
            if not download_url:
                results.append({"id": att_id, "filename": filename, "status": "failed", "error": "no download link"})
                continue
            if not download_url.startswith("http"):
                download_url = base_url.removesuffix("/wiki") + download_url if download_url.startswith("/wiki/") else base_url + download_url
            # `filename` stays as Confluence reports it (used for the download URL
            # and shown in the page), but the on-disk name is sanitised: some
            # attachment titles are URL-encoded strings carrying query parameters.
            safe_name = re.sub(r"[^\w\s.\-\[\]()]", "_", filename)[:150].strip() or att_id
            att_path = att_dir / f"{att_id}-{safe_name}"
            if att_path.is_file() and att_path.stat().st_size > 0 and (
                not att.get("fileSize") or att_path.stat().st_size == att["fileSize"]
            ):
                results.append({"id": att_id, "filename": filename, "path": str(att_path), "status": "ok"})
                continue
            att_dir.mkdir(parents=True, exist_ok=True)
            # Attachments with status "archived" 404 on the REST download link but
            # remain retrievable from the legacy /download/attachments path, so try
            # that before giving up.
            candidates = [
                download_url,
                f"{base_url}/download/attachments/{page_id}/{quote(filename)}",
            ]
            last_error = None
            for url in candidates:
                partial = att_path.with_suffix(att_path.suffix + ".part")
                try:
                    # Stream to disk: some attachments are >100MB webinar
                    # recordings, which a flat socket timeout on a buffered
                    # read aborts part-way through.
                    with get(session, url, timeout=(30, 120), stream=True) as r:
                        # The legacy endpoint answers 202 with an empty body for
                        # phantom attachment records (duplicates whose title is a
                        # URL-encoded string). Writing those would create 0-byte
                        # files that look like successfully archived content.
                        if r.status_code != 200:
                            raise RuntimeError(f"no content (HTTP {r.status_code})")
                        written = 0
                        with partial.open("wb") as fh:
                            for chunk in r.iter_content(chunk_size=1 << 20):
                                if chunk:
                                    fh.write(chunk)
                                    written += len(chunk)
                        if not written:
                            raise RuntimeError("no content (empty body)")
                        if att.get("fileSize") and written != att["fileSize"]:
                            raise RuntimeError(f"size mismatch ({written} of {att['fileSize']} bytes)")
                    # Only publish the final name once the body is fully written,
                    # so an interrupted transfer cannot masquerade as a good file.
                    partial.replace(att_path)
                    results.append({"id": att_id, "filename": filename, "path": str(att_path), "status": "ok"})
                    last_error = None
                    break
                except StopMirror:
                    partial.unlink(missing_ok=True)
                    raise
                except Exception as exc:
                    last_error = exc
                    partial.unlink(missing_ok=True)
            if last_error is not None:
                print(f"  WARN: attachment failed {filename}: {last_error}", file=sys.stderr)
                results.append({"id": att_id, "filename": filename, "status": "failed", "error": str(last_error)})

        next_link = data.get("_links", {}).get("next")
        if not next_link:
            break
        qs = parse_qs(urlparse(next_link).query)
        cursor = qs.get("cursor", [None])[0]
        if not cursor:
            break
    return results


# ---------------------------------------------------------------------------
# HTML -> Markdown
# ---------------------------------------------------------------------------

def is_auth_wall(html: str) -> bool:
    """
    True when a body looks like Confluence served a login/permission page
    instead of content.

    The naive check (any occurrence of "login"/"access denied" in a short body)
    false-positives on the pagetree macro, whose hidden inputs always carry a
    `loginUrl` field and a "do not have permission" i18n error string even when
    the page rendered perfectly well. Ignore that macro's markup before testing.
    """
    if not html:
        return False
    stripped = re.sub(r"<div class=\"plugin_pagetree\".*?</div>\s*</p>", "", html, flags=re.DOTALL)
    if len(stripped) >= 2000:
        return False
    return bool(re.search(r"(you (do not|don't) have permission|access denied|please log ?in)",
                          stripped, re.IGNORECASE))


def child_index_markdown(
    page_id: str,
    pages_by_id: dict[str, dict],
    id_to_relpath: dict[str, str],
    current_path: Path,
) -> str:
    """Render a bullet list linking to a page's direct children, or "" if none."""
    children = [
        p for p in pages_by_id.values()
        if p.get("parentId") == page_id
    ]
    if not children:
        return ""
    children.sort(key=lambda p: p.get("title", ""))

    lines = []
    for child in children:
        target = id_to_relpath.get(child["id"])
        if not target:
            continue
        rel = os.path.relpath(DOCS_ROOT / target, current_path.parent)
        lines.append(f"- [{child['title']}]({rel})")
    if not lines:
        return ""
    return "\n".join(lines)


def attachment_disk_name(attachment_id: str, filename: str) -> str:
    """On-disk name for an attachment, matching download_attachments()."""
    safe_name = re.sub(r"[^\w\s.\-\[\]()]", "_", filename)[:150].strip() or attachment_id
    return f"{attachment_id}-{safe_name}"


def local_attachment_link(href: str, current_path: Path) -> str | None:
    """
    Resolve a Confluence attachment-preview href to the mirrored file.

    Returns a path relative to the page, or None when the href is not an
    attachment preview or the file was not downloaded.
    """
    query = parse_qs(urlparse(href).query)
    preview = query.get("preview", [None])[0]
    if not preview:
        return None
    # preview is "/<pageId>/<attachmentId>/<filename>", percent- and plus-encoded.
    parts = unquote_plus(preview).strip("/").split("/")
    if len(parts) != 3:
        return None
    page_id, attachment_id, filename = parts

    try:
        space_key = current_path.relative_to(DOCS_ROOT).parts[0]
    except (ValueError, IndexError):
        return None

    # The API reports attachment ids with an "att" prefix; the preview URL does not.
    if not attachment_id.startswith("att"):
        attachment_id = f"att{attachment_id}"

    attachment_dir = ATTACHMENTS_ROOT / space_key / page_id
    # Files fetched before filename sanitisation was introduced kept the raw
    # Confluence title on disk, so accept either spelling.
    candidates = [
        attachment_dir / attachment_disk_name(attachment_id, filename),
        attachment_dir / f"{attachment_id}-{filename}",
    ]
    for target in candidates:
        if target.exists():
            return os.path.relpath(target, current_path.parent)

    # Last resort: match on the attachment id prefix, whatever the stored name.
    if attachment_dir.is_dir():
        for target in attachment_dir.glob(f"{attachment_id}-*"):
            return os.path.relpath(target, current_path.parent)
    return None


def html_to_markdown(
    html: str, base_url: str, id_to_relpath: dict[str, str], current_path: Path
) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Drop tags whose text content is not page content. markdownify extracts the
    # text of any tag outside its `convert` allowlist, so <style>/<script> bodies
    # (Confluence TOC macro CSS, colour-macro CSS) leak into the Markdown unless
    # the elements are removed from the tree first.
    for tag in soup.find_all(["style", "script"]):
        tag.decompose()

    # Confluence UI chrome that carries no archival content.
    for tag in soup.find_all(class_=re.compile(r"aui-icon|expand-control-icon")):
        tag.decompose()

    # Preserve Confluence heading anchors. Confluence's TOC macro and its
    # cross-page links target ids like "ClinicalSafety-Introduction", but a
    # Markdown renderer derives its own slug ("introduction"), so every one of
    # those links would 404 in-page. Carry the original id through as an
    # attr_list attribute so both the mirrored TOCs and inbound anchor links
    # keep working, and the anchors still match the original source URLs.
    for heading in soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        heading_id = heading.get("id")
        if heading_id and heading.get_text(strip=True):
            heading.append(NavigableString(f" {{#{heading_id}}}"))

    # Rewrite internal page links
    for a in soup.find_all("a", href=True):
        href = a["href"]

        # Confluence links an attachment as a preview of its parent page:
        #   /wiki/spaces/BG/pages/<pageId>/Title?preview=/<pageId>/<attId>/<name>
        # The path matches the page-link pattern below, so without this branch the
        # link collapses to the page itself and the attachment reference is lost.
        if attachment := local_attachment_link(href, current_path):
            a["href"] = attachment
            continue

        m = re.search(r"/pages/(\d+)", href)
        if m and not parse_qs(urlparse(href).query).get("preview"):
            pid = m.group(1)
            if target := id_to_relpath.get(pid):
                fragment = urlparse(href).fragment
                a["href"] = os.path.relpath(DOCS_ROOT / target, current_path.parent) + (f"#{fragment}" if fragment else "")
            else:
                a["href"] = urljoin(base_url, href)
        elif href.startswith("/"):
            a["href"] = urljoin(base_url, href)

    result = md(
        str(soup),
        heading_style="ATX",
        bullets="-",
        # Keep tables that have rowspan/colspan as HTML by not stripping the tags
        convert=["a", "b", "strong", "i", "em", "code", "pre", "h1", "h2", "h3",
                 "h4", "h5", "h6", "p", "br", "hr", "ul", "ol", "li",
                 "blockquote", "img", "table", "thead", "tbody", "tr", "th", "td"],
    )

    # Strip Confluence inline CSS fragments that survive HTML parsing
    # e.g. [data-colorid=abc123]{color:#fff} html[data-color-mode=dark] ...
    result = re.sub(r"\[data-colorid=[^\]]+\]\{[^}]+\}[^\n]*", "", result)
    result = re.sub(r"html\[data-color-mode=[^\]]+\][^\n]*", "", result)

    result = re.sub(r"\n{3,}", "\n\n", result)
    return result.strip()


# ---------------------------------------------------------------------------
# Write page to disk
# ---------------------------------------------------------------------------

def write_page(
    path: Path,
    page_id: str,
    space_key: str,
    title: str,
    detail: dict,
    markdown: str,
    base_url: str,
    attachments: list[dict],
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    version = detail.get("version", {}).get("number", "?")
    updated = detail.get("version", {}).get("createdAt", "")
    labels = [lbl.get("name", "") for lbl in detail.get("labels", {}).get("results", [])]
    source_url = base_url + detail.get("_links", {}).get("webui", f"/pages/{page_id}")

    frontmatter = (
        "---\n"
        f'page_id: "{page_id}"\n'
        f'space: "{space_key}"\n'
        f'title: "{title.replace(chr(34), chr(39))}"\n'
        f"version: {version}\n"
        f'updated: "{updated}"\n'
        f'source_url: "{source_url}"\n'
        f"labels: {json.dumps(labels)}\n"
        "---\n\n"
    )

    att_section = ""
    ok_atts = [a for a in attachments if a["status"] == "ok"]
    fail_atts = [a for a in attachments if a["status"] == "failed"]
    if ok_atts:
        att_section += "\n\n## Attachments\n\n"
        for a in ok_atts:
            relative_path = os.path.relpath(a["path"], path.parent)
            att_section += f"- [{a['filename']}]({relative_path})\n"
    if fail_atts:
        att_section += "\n\n> **Warning**: attachment download failed for:\n"
        for a in fail_atts:
            att_section += f"> - {a['filename']}: {a.get('error', '')}\n"

    path.write_text(
        frontmatter + f"# {title}\n\n" + markdown + att_section,
        encoding="utf-8",
    )


def save_raw_html(space_key: str, page_id: str, html: str) -> None:
    raw_path = RAW_ROOT / space_key / f"{page_id}.html"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(html, encoding="utf-8")


# ---------------------------------------------------------------------------
# Mirror one space
# ---------------------------------------------------------------------------

def mirror_space(
    session: requests.Session,
    base_url: str,
    space_key: str,
    manifest: dict,
    full_refresh: bool,
    dry_run: bool,
    refresh_pages: set[str],
) -> tuple[int, int, list[str]]:
    print(f"\n=== Mirroring {space_key} ===", file=sys.stderr)
    pages = enumerate_pages(session, base_url, space_key)
    if not pages:
        return 0, 0, [f"{space_key}: no pages found"]

    # Build lookup and child sets from enumeration data (no extra API calls)
    pages_by_id: dict[str, dict] = {p["id"]: p for p in pages}
    if len(pages_by_id) != len(pages):
        return 0, 0, [f"{space_key}: duplicate page IDs in API enumeration"]
    has_children: set[str] = {p["parentId"] for p in pages if p.get("parentId")}

    # Build id -> relative path map for link rewriting
    id_to_relpath: dict[str, str] = {}
    claimed_paths = {entry["path"]: key for key, entry in manifest.items()}
    for pid, page in pages_by_id.items():
        ancestors = build_ancestor_chain(pid, pages_by_id)
        out_path = page_output_path(space_key, ancestors, page["title"], pid in has_children)
        try:
            id_to_relpath[pid] = str(out_path.relative_to(DOCS_ROOT))
        except ValueError:
            id_to_relpath[pid] = str(out_path)
        key = f"{space_key}/{pid}"
        relpath = id_to_relpath[pid]
        if claimed_paths.get(relpath, key) != key:
            # Preserve the earlier file and give the colliding page an ID-based path.
            relpath = manifest.get(key, {}).get("path") or f"{space_key}/_by-id/{pid}.md"
            print(f"  {key}: using {relpath} to avoid a path collision", file=sys.stderr)
        if claimed_paths.setdefault(relpath, key) != key:
            return 0, 0, [f"{key}: path collision with {claimed_paths[relpath]} at {relpath}"]
        id_to_relpath[pid] = relpath

    if dry_run:
        print(f"  [dry-run] {len(pages)} pages found, {len(has_children)} have children", file=sys.stderr)
        print(f"  [dry-run] sample paths:")
        for pid in list(pages_by_id)[:5]:
            print(f"    {id_to_relpath.get(pid, '?')}", file=sys.stderr)
        return len(pages), 0, []

    inventory_dir = DOCS_ROOT / ".inventory"
    inventory_dir.mkdir(parents=True, exist_ok=True)
    inventory = {
        "source": base_url,
        "enumerated_at": datetime.now(timezone.utc).isoformat(),
        "current_pages": {pid: page.get("version", {}).get("number") for pid, page in pages_by_id.items()},
        "prior_pages_not_listed": sorted(
            key.split("/", 1)[1] for key in manifest
            if key.startswith(f"{space_key}/") and key.split("/", 1)[1] not in pages_by_id
        ),
    }
    (inventory_dir / f"{space_key}.json").write_text(json.dumps(inventory, indent=2, sort_keys=True) + "\n")
    id_to_relpath = {
        **{key.split("/", 1)[1]: entry["path"] for key, entry in manifest.items()},
        **id_to_relpath,
    }
    success = 0
    skipped = 0
    failures = []

    for pid, page in pages_by_id.items():
        title = page["title"]
        version = page.get("version", {}).get("number", 0)
        manifest_key = f"{space_key}/{pid}"

        out_path = DOCS_ROOT / id_to_relpath[pid]
        saved = manifest.get(manifest_key, {})
        if (not full_refresh and pid not in refresh_pages and saved.get("version") == version
            and saved.get("path") == id_to_relpath[pid] and out_path.is_file()
            and (RAW_ROOT / space_key / f"{pid}.html").is_file()):
            skipped += 1
            continue

        try:
            html, detail = fetch_page_body(session, base_url, pid)

            if is_auth_wall(html):
                print(f"  WARN: possible auth wall for {title} ({pid})", file=sys.stderr)
                failures.append(f"{space_key}/{pid} ({title}): possible auth wall")
                continue

            if not html.strip() and pid not in has_children:
                failures.append(f"{space_key}/{pid} ({title}): empty body")
                continue
            save_raw_html(space_key, pid, html)
            attachments = download_attachments(session, base_url, pid, space_key)
            markdown = html_to_markdown(html, base_url, id_to_relpath, out_path)

            # Container pages (empty body, or a body consisting only of the
            # Confluence pagetree macro) carry no prose of their own - the source
            # page just renders its children. Synthesise that listing so the
            # mirrored tree stays navigable instead of leaving a bare directory.
            if not markdown.strip():
                markdown = child_index_markdown(pid, pages_by_id, id_to_relpath, out_path)
                if not markdown:
                    print(f"  WARN: empty body for {title} ({pid})", file=sys.stderr)
                    failures.append(f"{space_key}/{pid} ({title}): empty body")

            for a in attachments:
                if a["status"] == "failed":
                    failures.append(f"{space_key}/{pid} attachment {a['filename']}: {a.get('error','')}")

            write_page(out_path, pid, space_key, title, detail, markdown, base_url, attachments)

            manifest[manifest_key] = {
                "version": detail.get("version", {}).get("number", version),
                "path": str(out_path.relative_to(DOCS_ROOT)),
                "title": title,
            }
            success += 1
            if success % 25 == 0:
                save_manifest(manifest)
                print(f"  ...{success}/{len(pages_by_id)} pages done", file=sys.stderr)

        except StopMirror:
            save_manifest(manifest)
            record_failures(failures)
            raise
        except Exception as exc:
            print(f"  ERROR: {title} ({pid}): {exc}", file=sys.stderr)
            failures.append(f"{space_key}/{pid} ({title}): {exc}")

    save_manifest(manifest)
    return success, skipped, failures


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------

def validate(spaces: list[str]) -> list[str]:
    issues = []
    manifest = load_manifest()
    for space_key in spaces:
        entries = {k: v for k, v in manifest.items() if k.startswith(f"{space_key}/")}
        if not entries:
            issues.append(f"{space_key}: no entries in manifest")
            continue
        inventory_path = DOCS_ROOT / ".inventory" / f"{space_key}.json"
        if inventory_path.exists():
            inventory = json.loads(inventory_path.read_text())
            for pid, source_version in inventory["current_pages"].items():
                key = f"{space_key}/{pid}"
                saved_version = entries.get(key, {}).get("version")
                if saved_version is None or source_version is None or saved_version < source_version:
                    issues.append(f"{key}: enumerated version {source_version}, saved {saved_version}")
        for key, entry in entries.items():
            pid = key.split("/", 1)[1]
            raw = RAW_ROOT / space_key / f"{pid}.html"
            md_path = DOCS_ROOT / entry["path"]
            if not raw.exists():
                issues.append(f"missing raw HTML: {key}")
            if not md_path.exists():
                issues.append(f"missing markdown: {key}")
            else:
                content = md_path.read_text()
                if re.search(r"(log.?in|access denied)", content, re.IGNORECASE) and len(content) < 500:
                    issues.append(f"possible auth wall: {key}")
                if len(content.strip()) < 100:
                    issues.append(f"suspiciously short output: {key}")
    for failure in load_failure_report()["failures"]:
        if failure["status"] == "unresolved":
            issues.append(f"unresolved failure: {failure['message']}")
        elif failure["status"] == "deferred":
            # Deferred items are known, recorded omissions awaiting a decision.
            # They must not fail validation, but must never become invisible.
            print(f"NOTE: deferred - {failure['message']}", file=sys.stderr)
    return issues


def audit_attachments(session: requests.Session, base_url: str, spaces: list[str]) -> int:
    """Check each current page, including pages skipped by the version refresh."""
    inventory_dir = DOCS_ROOT / ".inventory"
    if not all((inventory_dir / f"{space}.json").is_file() for space in spaces):
        print("An attachment audit requires a live page inventory for each selected space.", file=sys.stderr)
        return 1
    failure_count = 0
    for space in spaces:
        inventory = json.loads((inventory_dir / f"{space}.json").read_text())
        pages = inventory["current_pages"]
        print(f"  {space}: checking attachments for {len(pages)} current pages", file=sys.stderr)
        with (inventory_dir / f"{space}-attachments.jsonl").open("w", encoding="utf-8", buffering=1) as log:
            for pid in pages:
                try:
                    attachments = download_attachments(session, base_url, pid, space)
                except StopMirror as exc:
                    log.write(json.dumps({"page_id": pid, "error": str(exc)}) + "\n")
                    print(f"STOP: {space}/{pid}: {exc}", file=sys.stderr)
                    return 1
                except Exception as exc:
                    log.write(json.dumps({"page_id": pid, "error": str(exc)}) + "\n")
                    failure_count += 1
                    continue

                for attachment in attachments:
                    if attachment["status"] == "ok":
                        path = Path(attachment["path"])
                        attachment["bytes"] = path.stat().st_size
                        attachment["path"] = str(path.relative_to(DOCS_ROOT))
                    else:
                        failure_count += 1
                log.write(json.dumps({"page_id": pid, "attachments": attachments}) + "\n")
    print(f"Attachment audit: {failure_count} failed page listings or attachment records.")
    return int(failure_count > 0)


def rebuild_markdown() -> list[str]:
    """Regenerate Markdown from preserved raw HTML without API access."""
    manifest = load_manifest()
    id_to_relpath = {key.split("/", 1)[1]: entry["path"] for key, entry in manifest.items()}
    issues = []

    for key, entry in manifest.items():
        space_key, page_id = key.split("/", 1)
        raw_path = RAW_ROOT / space_key / f"{page_id}.html"
        md_path = DOCS_ROOT / entry["path"]
        if not raw_path.exists() or not md_path.exists():
            issues.append(f"cannot rebuild {key}: missing raw HTML or Markdown")
            continue

        existing = md_path.read_text(encoding="utf-8")
        frontmatter_end = existing.find("\n---\n\n")
        if frontmatter_end == -1:
            issues.append(f"cannot rebuild {key}: missing YAML frontmatter")
            continue
        frontmatter = existing[:frontmatter_end + len("\n---\n\n")]

        attachment_start = min(
            (index for index in (existing.find("\n\n## Attachments\n"), existing.find("\n\n> **Warning**")) if index != -1),
            default=len(existing),
        )
        attachment_section = existing[attachment_start:]

        def rewrite_attachment(match: re.Match) -> str:
            target = match.group(1)
            if "/attachments/" in target:
                tail = target.split("/attachments/", 1)[1]
                # Mirrors written before attachments moved out of the archival
                # dot-directory used .raw/<space>/attachments/<page>/<file>;
                # the published layout is attachments/<space>/<page>/<file>.
                if "/.raw/" in target:
                    space_key = target.split("/.raw/", 1)[1].split("/", 1)[0]
                    tail = f"{space_key}/{tail}"
                resolved = ATTACHMENTS_ROOT / tail
            elif "/.raw/" in target:
                resolved = RAW_ROOT / target.split("/.raw/", 1)[1]
            else:
                return match.group(0)
            return "](" + os.path.relpath(resolved, md_path.parent) + ")"

        attachment_section = re.sub(r"\]\(([^)]+)\)", rewrite_attachment, attachment_section)
        markdown = html_to_markdown(
            raw_path.read_text(encoding="utf-8"),
            "https://nhse-dsic.atlassian.net/wiki",
            id_to_relpath,
            md_path,
        )
        md_path.write_text(frontmatter + f"# {entry['title']}\n\n" + markdown + attachment_section, encoding="utf-8")

    return issues


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Mirror Confluence spaces to Markdown.")
    parser.add_argument("--space", help="Mirror only this space key")
    parser.add_argument("--output-dir", type=Path, help="Use a separate archive directory instead of docs/")
    parser.add_argument("--refresh-page", action="append", default=[], metavar="ID", help="Re-fetch a specific page even if unchanged; repeat as needed")
    parser.add_argument("--full-refresh", action="store_true", help="Re-fetch all pages ignoring manifest")
    parser.add_argument("--dry-run", action="store_true", help="Enumerate only, do not write files")
    parser.add_argument("--validate", action="store_true", help="Validate existing mirror completeness")
    parser.add_argument("--rebuild-markdown", action="store_true", help="Regenerate Markdown from preserved raw HTML")
    parser.add_argument("--audit-attachments", action="store_true", help="Check and retrieve attachments for every inventoried page")
    args = parser.parse_args()
    if args.output_dir:
        set_output_root(args.output_dir.expanduser())
    known_spaces = [s for tenant in TENANTS.values() for s in tenant["spaces"]]
    if args.space and args.space not in known_spaces:
        parser.error(f"unknown space: {args.space}")
    if sum([args.dry_run, args.validate, args.rebuild_markdown, args.audit_attachments]) > 1:
        parser.error("choose only one of --dry-run, --validate, --rebuild-markdown, --audit-attachments")

    if args.validate:
        issues = validate([args.space] if args.space else known_spaces)
        if issues:
            print(f"VALIDATION FAILED: {len(issues)} issue(s):")
            for iss in issues:
                print(f"  - {iss}")
            return 1
        print("Validation passed.")
        return 0

    if args.rebuild_markdown:
        issues = rebuild_markdown()
        if issues:
            print(f"REBUILD FAILED: {len(issues)} issue(s):")
            for issue in issues:
                print(f"  - {issue}")
            return 1
        print("Markdown rebuilt from raw HTML.")
        return 0

    session = make_session()
    if args.audit_attachments:
        return audit_attachments(session, TENANTS["nhse-dsic"]["base"], [args.space] if args.space else known_spaces)
    manifest = load_manifest()
    all_failures = []
    total_success = total_skipped = 0

    for tenant in TENANTS.values():
        base_url = tenant["base"]
        spaces = [args.space] if args.space else tenant["spaces"]
        for space_key in spaces:
            try:
                ok, skipped, failures = mirror_space(
                    session, base_url, space_key, manifest, args.full_refresh, args.dry_run, set(args.refresh_page)
                )
                total_success += ok
                total_skipped += skipped
                all_failures.extend(failures)
                print(
                    f"  {space_key}: {ok} fetched, {skipped} skipped, {len(failures)} failures",
                    file=sys.stderr,
                )
            except StopMirror as exc:
                msg = f"STOP: {space_key}: {exc}"
                print(f"  {msg}", file=sys.stderr)
                if not args.dry_run:
                    record_failures([*all_failures, msg])
                return 1
            except Exception as exc:
                msg = f"FATAL: {space_key}: {exc}"
                print(f"  {msg}", file=sys.stderr)
                all_failures.append(msg)

    if not args.dry_run:
        record_failures(all_failures)

    print(f"\nDone: {total_success} fetched, {total_skipped} skipped, {len(all_failures)} failures")
    if all_failures:
        print("\nFailures:")
        for f in all_failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
