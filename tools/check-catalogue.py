# SPDX-License-Identifier: AGPL-3.0-or-later

"""Check the site's navigation, archive coverage and publication boundary."""

import filecmp
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml
from bs4 import BeautifulSoup
from markdown import markdown

from extract_spec import hrefs, structure, visible_text
from spec_site import APPROVED_REVISION, SPEC_DIR, page_route


def check_source(config):
    if config.get("docs_dir") != "site/source" or config.get("site_dir") != "site/archive":
        return ["Build must use staged site/source/ and publish only site/archive/."]

    errors = []
    root = Path("docs")
    pages = set()
    for path in [root, *root.rglob("*")]:
        if path.is_symlink():
            errors.append(f"Catalogue must not contain symlinks: {path}")
        elif path.is_file():
            if path.suffix == ".md":
                pages.add(path.relative_to(root).as_posix())
            elif path.suffix not in {".css", ".svg"}:
                errors.append(f"Unexpected catalogue asset: {path}")

    nav = [entry for item in config["nav"] for entry in item.values()]
    errors += [f"Page missing from navigation: {path}" for path in sorted(pages - set(nav))]
    errors += [f"Navigation points to a missing page: {path}" for path in sorted(set(nav) - pages)]
    if len(nav) != len(set(nav)):
        errors.append("A page appears more than once in navigation.")
    return errors


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__()
        self.anchors = set()
        self.links = set()
        self.feed(path.read_text(encoding="utf-8"))
        self.close()

    def handle_starttag(self, tag, attrs):
        for key, value in attrs:
            if not value:
                continue
            if key == "id" or (tag == "a" and key == "name"):
                self.anchors.add(value)
            if key in {"href", "src"}:
                self.links.add(value)


def check_rcgp(root, base):
    relative_pdf = Path("rcgp-1980/computers-in-primary-care.pdf")
    pdf = root / relative_pdf
    transcript = root / "rcgp-1980/transcript/index.html"
    errors = []
    if not pdf.is_file() or not filecmp.cmp(relative_pdf, pdf, shallow=False):
        errors.append("The published RCGP PDF must be byte-identical to the original scan.")
    if not transcript.is_file():
        return errors + ["The rendered RCGP transcript is missing."]

    page = Page(transcript)
    page_url = urljoin(base, transcript.relative_to(root).as_posix())
    pdf_url = urljoin(base, relative_pdf.as_posix())
    destinations = {urljoin(page_url, link) for link in page.links}
    for number in range(1, 37):
        if f"pdf-page-{number:02d}" not in page.anchors or f"{pdf_url}#page={number}" not in destinations:
            errors.append(f"RCGP transcript page {number} is missing its heading or direct PDF link.")
    return errors


def check_spec(root, source):
    output = root / SPEC_DIR
    staged = source / SPEC_DIR
    index = output / "index.json"
    if not index.is_file() or not filecmp.cmp(index, staged / "index.json", shallow=False):
        return ["The published spec catalogue must match the staged catalogue."]
    catalogue = json.loads(index.read_text(encoding="utf-8"))
    if catalogue["snapshot_commit"] != APPROVED_REVISION:
        return ["The spec catalogue does not use the approved capture."]
    markdown_by_route = {page_route(path.relative_to(staged)): path for path in staged.rglob("*.md")}
    entries = catalogue["capabilities"] + catalogue["records"]
    routes = [entry["path"] for entry in entries]
    if len(set(routes)) != len(routes) or set(routes) | {"./"} != markdown_by_route.keys():
        return ["Spec catalogue entries must match the staged pages one-to-one."]
    targets = {Path(route) / "index.html": path for route, path in markdown_by_route.items()}
    expected = {Path("index.json"), *targets}
    observed = {path.relative_to(output) for path in output.rglob("*") if path.is_file()}
    errors = [f"Missing spec output: {path}" for path in sorted(expected - observed)]
    errors += [f"Unexpected spec output: {path}" for path in sorted(observed - expected)]
    for path in sorted(targets.keys() & observed):
        text = targets[path].read_text(encoding="utf-8")
        if text.startswith("---\n"):
            text = text.split("---", 2)[2]
        expected_body = BeautifulSoup(markdown(text, extensions=["tables"]), "html.parser")
        article = BeautifulSoup((output / path).read_bytes(), "html.parser").select_one("article.md-content__inner")
        if article is None:
            errors.append(f"Missing spec article: {path}")
            continue
        for permalink in article.select("a.headerlink"):
            permalink.decompose()
        for heading in article.select("h2, h3, h4"):
            heading.attrs.pop("id", None)
        external = lambda body: [link for link in hrefs(body) if urlsplit(link).scheme in {"http", "https"}]
        if (visible_text(article).split() != visible_text(expected_body).split()
                or structure(article) != structure(expected_body) or external(article) != external(expected_body)):
            errors.append(f"Published spec article changed wording, structure or source links: {path}")

    search = json.loads((root / "search.json").read_text(encoding="utf-8"))
    searchable = {item["location"] for item in search["items"]}
    for entry in catalogue["records"]:
        if entry["kind"] == "epic" and f"{SPEC_DIR.as_posix()}/{entry['path']}" not in searchable:
            errors.append(f"Epic missing from site search: {entry['path']}")
    return errors


def check_rendered(config):
    root = Path(config["site_dir"]).resolve()
    if not (root / "index.html").is_file():
        return ["Catalogue is missing its rendered index.html."]

    base = config["site_url"]
    errors = check_rcgp(root, base)
    errors += check_spec(root, Path(config["docs_dir"]))
    manifest = json.loads(Path("nhs-futures/docs/.mirror-manifest.json").read_text(encoding="utf-8"))
    expected = {Path("nhs-snapshot/index.html"), Path("nhs-snapshot/archive-omissions/index.html")}
    for item in manifest.values():
        path = Path("nhs-snapshot") / item["path"]
        expected.add(path.with_suffix(".html") if path.name == "index.md" else path.with_suffix("") / "index.html")
    observed = {path.relative_to(root) for path in (root / "nhs-snapshot").rglob("*") if path.is_file()}
    errors += [f"Archive page missing from build: {path}" for path in sorted(expected - observed)]
    errors += [f"Unexpected archive output: {path}" for path in sorted(observed - expected)]

    authored = {root / "index.html", root / "404.html"}
    authored.update(root / path.stem / "index.html" for path in Path("docs").glob("*.md") if path.name != "index.md")
    pages = {path: Page(path) for path in sorted(root.rglob("*.html"))}
    errors += [f"Missing rendered navigation or guide page: {path.relative_to(root)}" for path in sorted(authored - pages.keys())]
    spec_pages = {path for path in pages if path.is_relative_to(root / SPEC_DIR)}
    errors += check_links(root, base, pages, authored | spec_pages)
    return errors


def check_links(root, base, pages, authored):
    """Check actual browser fragment targets throughout the rendered archive."""
    origin = urlsplit(base).netloc
    prefix = urlsplit(base).path
    errors = []
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        page_url = urljoin(base, relative)
        for link in sorted(page.links):
            url = urlsplit(urljoin(page_url, link))
            if url.scheme not in {"http", "https"} or url.netloc != origin or (path not in authored and not url.fragment):
                continue
            if not url.path.startswith(prefix):
                errors.append(f"{relative}: link leaves the Pages project path: {link}")
                continue
            target = (root / unquote(url.path.removeprefix(prefix))).resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f"{relative}: missing internal target: {link}")
            elif target in pages and url.fragment and unquote(url.fragment) not in pages[target].anchors:
                errors.append(f"{relative}: missing anchor: {link}")
    return errors


if __name__ == "__main__":
    checks = {"source": check_source, "rendered": check_rendered}
    config = yaml.safe_load(Path("mkdocs.yml").read_text(encoding="utf-8"))
    phase = sys.argv[1]
    errors = checks[phase](config)
    if errors:
        print("\n".join(errors), file=sys.stderr)
        sys.exit(1)
    print(f"Catalogue {phase} checks passed.")
