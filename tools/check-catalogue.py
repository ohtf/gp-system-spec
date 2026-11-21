# SPDX-License-Identifier: AGPL-3.0-or-later

"""Check the site's navigation, archive coverage and publication boundary."""

import filecmp
import json
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml


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


def check_rendered(config):
    root = Path(config["site_dir"]).resolve()
    if not (root / "index.html").is_file():
        return ["Catalogue is missing its rendered index.html."]

    base = config["site_url"]
    origin = urlsplit(base).netloc
    prefix = urlsplit(base).path
    errors = check_rcgp(root, base)
    manifest = json.loads(Path("nhs-futures/docs/.mirror-manifest.json").read_text(encoding="utf-8"))
    expected = {Path("nhs-snapshot/index.html"), Path("nhs-snapshot/archive-omissions/index.html")}
    for item in manifest.values():
        path = Path("nhs-snapshot") / item["path"]
        expected.add(path.with_suffix(".html") if path.name == "index.md" else path.with_suffix("") / "index.html")
    observed = {path.relative_to(root) for path in (root / "nhs-snapshot").rglob("*") if path.is_file()}
    errors += [f"Archive page missing from build: {path}" for path in sorted(expected - observed)]
    errors += [f"Unexpected archive output: {path}" for path in sorted(observed - expected)]

    # Imported hyperlinks include known broken source fragments. Enforce new
    # links on the authored pages without silently hiding those legacy warnings.
    authored = {root / "index.html", root / "404.html"}
    authored.update(root / path.stem / "index.html" for path in Path("docs").glob("*.md") if path.name != "index.md")
    for path in sorted(authored):
        if not path.is_file():
            errors.append(f"Missing rendered navigation or guide page: {path.relative_to(root)}")
            continue
        page = Page(path)
        relative = path.relative_to(root).as_posix()
        page_url = urljoin(base, relative)
        for link in sorted(page.links):
            url = urlsplit(urljoin(page_url, link))
            if url.scheme not in {"http", "https"} or url.netloc != origin:
                continue
            if not url.path.startswith(prefix):
                errors.append(f"{relative}: link leaves the Pages project path: {link}")
                continue
            target = (root / unquote(url.path.removeprefix(prefix))).resolve()
            if target.is_dir():
                target /= "index.html"
            if not target.is_relative_to(root) or not target.is_file():
                errors.append(f"{relative}: missing internal target: {link}")
            elif target.suffix == ".html" and url.fragment and unquote(url.fragment) not in Page(target).anchors:
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
