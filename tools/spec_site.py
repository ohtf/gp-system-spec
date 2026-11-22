# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

"""Stage the approved extract as browsable pages, not a copy of local output."""

import json
import os
from pathlib import Path
import re

from extract_spec import generate, require

# Publication sign-off in LICENCE.md covers this capture and the single S62 rule.
APPROVED_REVISION = "96ece2be24ce5a311b2f7df09a5c73e354eab38c"
SPEC_DIR = Path("implementation-reference/2026-07-31")


def stage_path(path):
    return path.with_name("index.md") if path.name == "README.md" else path


def page_route(path):
    return path.parent.as_posix() + "/" if path.name == "index.md" else path.with_suffix("").as_posix() + "/"


def stage_spec(root):
    files = generate()
    catalogue = json.loads(files.pop(Path("index.json")))
    require(catalogue["snapshot_commit"] == APPROVED_REVISION, "Spec snapshot not approved for publication")
    records = {Path(entry["path"]): entry for entry in catalogue["records"]}
    capabilities = {Path(entry["path"]): entry for entry in catalogue["capabilities"]}
    require(set(files) == {*records, *capabilities, Path("README.md")}, "Uncatalogued spec output")
    require({path.as_posix() for path in records if path.parts[0] == "standards"}
            == {"standards/S62-appointments-data-reporting/4.0.1/WPAD-DI-016.md"}, "Unexpected standard extract")
    editions = {(cap["specification_id"], cap["publisher_version"]): (path, cap) for path, cap in capabilities.items()}
    for path, text in files.items():
        # The local tree uses README.md; Zensical folder landing pages use index.md.
        text = re.sub(r"(\]\([.\w/-]*)README\.md\)", r"\1index.md)", text)
        if path in records or path in capabilities:
            entry = records[path] if path in records else capabilities[path]
            identity = (entry["specification_id"], entry["publisher_version"])
            context = [f"NHS England · {identity[0]} v{identity[1]} · 31 July 2026 capture"]
            if edition := editions.get(identity):
                cap_path, cap = edition
                context.append(f"Status at capture: {cap['status_at_capture']}")
                if path != cap_path:
                    back = os.path.relpath(stage_path(cap_path), path.parent)
                    context.append(f"[Capability contents]({back})")
            if priority := entry.get("priority"):
                context.append(f"Publisher priority: {priority}")
            index = os.path.relpath("index.md", path.parent)
            context.append(f"[All capabilities]({index})")
            text = text.replace("\n\n[Archived source]", "\n\n" + " · ".join(context) + "\n\n[Archived source]", 1)
        target = root / SPEC_DIR / stage_path(path)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text, encoding="utf-8")

    for path, entry in (records | capabilities).items():
        entry["path"] = page_route(stage_path(path))
    (root / SPEC_DIR / "index.json").write_text(json.dumps(catalogue, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
