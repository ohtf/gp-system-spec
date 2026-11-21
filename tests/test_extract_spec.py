# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

from collections import Counter
import importlib.util
import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

import yaml

module_path = Path(__file__).resolve().parents[1] / "tools/extract-spec.py"
module_spec = importlib.util.spec_from_file_location("extract_spec", module_path)
extract = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(extract)


class ExtractionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = extract.generate()
        cls.records = json.loads(cls.files[Path("index.json")])["records"]

    def record(self, record_id):
        entry = next(item for item in self.records if item["id"] == record_id)
        body = self.files[Path(entry["path"])]
        _, metadata, text = body.split("---", 2)
        return entry, yaml.safe_load(metadata), text

    def test_index_covers_pinned_capability_and_links_to_every_epic(self):
        epics = [item for item in self.records if item["kind"] == "epic"]
        self.assertEqual(Counter(item["priority"] for item in epics), {"MUST": 9, "MAY": 27})
        self.assertEqual(sum(item["acceptance_criterion_count"] for item in epics), 56)
        self.assertEqual(len({item["id"] for item in epics}), 36)
        cap = Path("capabilities/C5-appointments-management-gp/1.5.0")
        for item in epics:
            path = Path(item["path"])
            self.assertIn(path, self.files)
            self.assertIn(f"]({path.relative_to(cap).as_posix()})", self.files[cap / "README.md"])

    def test_appointment_slot_source_headings_stay_in_the_right_epic(self):
        _, source, text = self.record("E00221")
        self.assertEqual(source["confluence_version"], 25)
        self.assertEqual(source["publisher_version"], "1.5.0")
        self.assertEqual(source["acceptance_criterion_count"], 4)
        self.assertIn("I want to manage Appointment Slots within a Session for the Healthcare Organisation", text)
        self.assertEqual(text.count("## Acceptance criterion "), 4)
        self.assertIn("## E00221 - Additional Implementation Details", text)
        self.assertIn("## E00221 - Supporting Information", text)
        self.assertNotIn("E00222", text)

    def test_reporting_rule_is_separate_from_the_capability_and_cross_linked(self):
        entry, metadata, text = self.record("WPAD-DI-016")
        self.assertEqual((metadata["specification_id"], metadata["publisher_version"], metadata["priority"]), ("S62", "4.0.1", "MUST"))
        self.assertIn("- Not an Appointment", text)
        self.assertNotIn("WPAD-DI-017", text)
        epic, _, text = self.record("E00219")
        reference = Path(epic["path"]).parent / "../../../../../standards/S62-appointments-data-reporting/4.0.1/WPAD-DI-016.md"
        self.assertEqual(reference.resolve(), Path(entry["path"]).resolve())
        self.assertIn("## Archive cross-reference", text)
        self.assertIn("../../../../../standards/S62-appointments-data-reporting/4.0.1/WPAD-DI-016.md", text)

    def test_regeneration_never_overwrites_an_edited_file(self):
        with TemporaryDirectory() as temp:
            root = Path(temp)
            extract.write_or_check(root, self.files, check=False)
            extract.write_or_check(root, self.files, check=True)
            edited = root / "README.md"
            edited.write_text("Local edits", encoding="utf-8")
            for check in (True, False):
                with self.assertRaisesRegex(ValueError, "changed generated file"):
                    extract.write_or_check(root, self.files, check=check)
            self.assertEqual(edited.read_text(encoding="utf-8"), "Local edits")
