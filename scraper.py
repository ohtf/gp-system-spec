#!/usr/bin/env python3
# SPDX-License-Identifier: AGPL-3.0-or-later
"""
Confluence space mirror scraper.

Fetches pages, attachments and rendered HTML from Confluence REST API v2,
converts to Markdown, and writes a Git-friendly directory tree.

Usage:
    python3 scraper.py [--space KEY] [--full-refresh] [--dry-run] [--validate]

Environment variables (optional - anonymous access used by default):
    CONFLUENCE_EMAIL      Atlassian account email
    CONFLUENCE_API_TOKEN  Atlassian API token
"""

import argparse
import json
import os
import random
import re
import sys
import time
from pathlib import Path
from urllib.parse import urljoin, urlparse, parse_qs

import requests
from bs4 import BeautifulSoup
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

MIRROR_ROOT = Path(__file__).parent / "mirror"
MANIFEST_PATH = MIRROR_ROOT / ".mirror-manifest.json"

REQUEST_DELAY_MIN = 1.0   # seconds
REQUEST_DELAY_MAX = 1.8   # seconds (jitter added to avoid bursty patterns)
MAX_RETRIES = 4
PAGE_LIMIT = 250


# ---------------------------------------------------------------------------
# HTTP session
# ---------------------------------------------------------------------------

def make_session() -> requests.Session:
    session = requests.Session()
    email = os.environ.get("CONFLUENCE_EMAIL")
    token = os.environ.get("CONFLUENCE_API_TOKEN")
    if email and token:
        session.auth = (email, token)
        print("INFO: using authenticated access", file=sys.stderr)
    else:
        print("INFO: using anonymous access", file=sys.stderr)
    session.headers["Accept"] = "application/json"
    return session


def delay() -> None:
    time.sleep(random.uniform(REQUEST_DELAY_MIN, REQUEST_DELAY_MAX))


def get(session: requests.Session, url: str, **kwargs) -> requests.Response:
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            resp = session.get(url, timeout=30, **kwargs)
            if resp.status_code == 429:
                wait = int(resp.headers.get("Retry-After", 15))
                print(f"  rate-limited, waiting {wait}s", file=sys.stderr)
                time.sleep(wait)
                continue
            resp.raise_for_status()
            delay()
            return resp
        except requests.RequestException as exc:
            if attempt == MAX_RETRIES:
                raise
            wait = 2 ** attempt
            print(f"  retry {attempt}/{MAX_RETRIES} after {wait}s: {exc}", file=sys.stderr)
            time.sleep(wait)
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
        return MIRROR_ROOT.joinpath(*parts) / "index.md"
    return MIRROR_ROOT.joinpath(*parts) / f"{slug}.md"


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

    pages = []
    cursor = None
    while True:
        params = {"limit": PAGE_LIMIT}
        if cursor:
            params["cursor"] = cursor
        resp = get(session, f"{base_url}/api/v2/spaces/{space_id}/pages", params=params)
        data = resp.json()
        pages.extend(data["results"])
        next_link = data.get("_links", {}).get("next")
        if not next_link:
            break
        qs = parse_qs(urlparse(next_link).query)
        cursor = qs.get("cursor", [None])[0]
        if not cursor:
            break

    print(f"  {space_key}: {len(pages)} pages enumerated", file=sys.stderr)
    return pages


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
    att_dir = MIRROR_ROOT / ".raw" / space_key / "attachments" / page_id
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
                continue
            if not download_url.startswith("http"):
                download_url = base_url + download_url
            att_path = att_dir / f"{att_id}-{filename}"
            if att_path.exists():
                results.append({"id": att_id, "filename": filename, "path": str(att_path), "status": "ok"})
                continue
            att_dir.mkdir(parents=True, exist_ok=True)
            try:
                r = session.get(download_url, timeout=60)
                r.raise_for_status()
                att_path.write_bytes(r.content)
                delay()
                results.append({"id": att_id, "filename": filename, "path": str(att_path), "status": "ok"})
            except Exception as exc:
                print(f"  WARN: attachment failed {filename}: {exc}", file=sys.stderr)
                results.append({"id": att_id, "filename": filename, "status": "failed", "error": str(exc)})

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

def html_to_markdown(html: str, base_url: str, id_to_relpath: dict) -> str:
    soup = BeautifulSoup(html, "html.parser")

    # Rewrite internal page links
    for a in soup.find_all("a", href=True):
        href = a["href"]
        m = re.search(r"/pages/(\d+)", href)
        if m:
            pid = m.group(1)
            a["href"] = id_to_relpath.get(pid, urljoin(base_url, href))
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
            att_section += f"- [{a['filename']}]({a['path']})\n"
    if fail_atts:
        att_section += "\n\n> **Warning**: attachment download failed for:\n"
        for a in fail_atts:
            att_section += f"> - {a['filename']}: {a.get('error', '')}\n"

    path.write_text(
        frontmatter + f"# {title}\n\n" + markdown + att_section,
        encoding="utf-8",
    )


def save_raw_html(space_key: str, page_id: str, html: str) -> None:
    raw_path = MIRROR_ROOT / ".raw" / space_key / f"{page_id}.html"
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
) -> tuple[int, int, list[str]]:
    print(f"\n=== Mirroring {space_key} ===", file=sys.stderr)
    pages = enumerate_pages(session, base_url, space_key)
    if not pages:
        return 0, 0, [f"{space_key}: no pages found"]

    # Build lookup and child sets from enumeration data (no extra API calls)
    pages_by_id: dict[str, dict] = {p["id"]: p for p in pages}
    has_children: set[str] = {p["parentId"] for p in pages if p.get("parentId")}

    # Build id -> relative path map for link rewriting
    id_to_relpath: dict[str, str] = {}
    for pid, page in pages_by_id.items():
        ancestors = build_ancestor_chain(pid, pages_by_id)
        out_path = page_output_path(space_key, ancestors, page["title"], pid in has_children)
        try:
            id_to_relpath[pid] = str(out_path.relative_to(MIRROR_ROOT))
        except ValueError:
            id_to_relpath[pid] = str(out_path)

    if dry_run:
        print(f"  [dry-run] {len(pages)} pages found, {len(has_children)} have children", file=sys.stderr)
        print(f"  [dry-run] sample paths:")
        for pid in list(pages_by_id)[:5]:
            print(f"    {id_to_relpath.get(pid, '?')}", file=sys.stderr)
        return len(pages), 0, []

    success = 0
    skipped = 0
    failures = []

    for pid, page in pages_by_id.items():
        title = page["title"]
        version = page.get("version", {}).get("number", 0)
        manifest_key = f"{space_key}/{pid}"

        if not full_refresh and manifest.get(manifest_key, {}).get("version") == version:
            skipped += 1
            continue

        try:
            html, detail = fetch_page_body(session, base_url, pid)

            if not html:
                print(f"  WARN: empty body for {title} ({pid})", file=sys.stderr)
                failures.append(f"{space_key}/{pid} ({title}): empty body")
                continue

            if re.search(r"(log.?in|access denied)", html, re.IGNORECASE) and len(html) < 2000:
                print(f"  WARN: possible auth wall for {title} ({pid})", file=sys.stderr)
                failures.append(f"{space_key}/{pid} ({title}): possible auth wall")

            save_raw_html(space_key, pid, html)
            markdown = html_to_markdown(html, base_url, id_to_relpath)

            ancestors = build_ancestor_chain(pid, pages_by_id)
            out_path = page_output_path(space_key, ancestors, title, pid in has_children)

            attachments = download_attachments(session, base_url, pid, space_key)
            for a in attachments:
                if a["status"] == "failed":
                    failures.append(f"{space_key}/{pid} attachment {a['filename']}: {a.get('error','')}")

            write_page(out_path, pid, space_key, title, detail, markdown, base_url, attachments)

            manifest[manifest_key] = {
                "version": version,
                "path": str(out_path.relative_to(MIRROR_ROOT)),
                "title": title,
            }
            success += 1
            if success % 25 == 0:
                save_manifest(manifest)
                print(f"  ...{success}/{len(pages_by_id)} pages done", file=sys.stderr)

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
        for key, entry in entries.items():
            pid = key.split("/", 1)[1]
            raw = MIRROR_ROOT / ".raw" / space_key / f"{pid}.html"
            md_path = MIRROR_ROOT / entry["path"]
            if not raw.exists():
                issues.append(f"missing raw HTML: {key}")
            if not md_path.exists():
                issues.append(f"missing markdown: {key}")
            elif content := md_path.read_text():
                if re.search(r"(log.?in|access denied)", content, re.IGNORECASE) and len(content) < 500:
                    issues.append(f"possible auth wall: {key}")
                if len(content.strip()) < 100:
                    issues.append(f"suspiciously short output: {key}")
    return issues


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> int:
    parser = argparse.ArgumentParser(description="Mirror Confluence spaces to Markdown.")
    parser.add_argument("--space", help="Mirror only this space key")
    parser.add_argument("--full-refresh", action="store_true", help="Re-fetch all pages ignoring manifest")
    parser.add_argument("--dry-run", action="store_true", help="Enumerate only, do not write files")
    parser.add_argument("--validate", action="store_true", help="Validate existing mirror completeness")
    args = parser.parse_args()

    if args.validate:
        all_spaces = [s for t in TENANTS.values() for s in t["spaces"]]
        issues = validate([args.space] if args.space else all_spaces)
        if issues:
            print(f"VALIDATION FAILED: {len(issues)} issue(s):")
            for iss in issues:
                print(f"  - {iss}")
            return 1
        print("Validation passed.")
        return 0

    session = make_session()
    manifest = load_manifest()
    all_failures = []
    total_success = total_skipped = 0

    for tenant in TENANTS.values():
        base_url = tenant["base"]
        spaces = [args.space] if args.space else tenant["spaces"]
        for space_key in spaces:
            try:
                ok, skipped, failures = mirror_space(
                    session, base_url, space_key, manifest, args.full_refresh, args.dry_run
                )
                total_success += ok
                total_skipped += skipped
                all_failures.extend(failures)
                print(
                    f"  {space_key}: {ok} fetched, {skipped} skipped, {len(failures)} failures",
                    file=sys.stderr,
                )
            except Exception as exc:
                msg = f"FATAL: {space_key}: {exc}"
                print(f"  {msg}", file=sys.stderr)
                all_failures.append(msg)

    print(f"\nDone: {total_success} fetched, {total_skipped} skipped, {len(all_failures)} failures")
    if all_failures:
        print("\nFailures:")
        for f in all_failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
