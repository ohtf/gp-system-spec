# SPDX-License-Identifier: AGPL-3.0-or-later

"""Check the public catalogue, not the preserved third-party mirror."""

import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit

import yaml


def check_source(config):
    if config.get("docs_dir") != "docs" or config.get("site_dir") != "site/catalogue":
        return ["Catalogue build must use docs/ and site/catalogue/."]

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


def check_rendered(config):
    root = Path(config["site_dir"]).resolve()
    if not (root / "index.html").is_file():
        return ["Catalogue is missing its rendered index.html."]

    base = config["site_url"]
    origin = urlsplit(base).netloc
    prefix = urlsplit(base).path
    pages = {path: Page(path) for path in root.rglob("*.html")}
    errors = []
    for path, page in sorted(pages.items()):
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
