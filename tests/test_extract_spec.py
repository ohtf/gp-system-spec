# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

from collections import Counter
import hashlib
import importlib.util
import json
from pathlib import Path
import re
from tempfile import TemporaryDirectory
import unittest
from urllib.parse import urlsplit

from bs4 import BeautifulSoup
from markdown import markdown
import yaml

module_path = Path(__file__).resolve().parents[1] / "tools/extract_spec.py"
module_spec = importlib.util.spec_from_file_location("extract_spec", module_path)
extract = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(extract)


class ExtractionTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = extract.generate()
        cls.catalogue = json.loads(cls.files[Path("index.json")])
        cls.records = cls.catalogue["records"]

    def record(self, record_id, capability="C5"):
        entry = next(item for item in self.records if (item["id"], item["specification_id"]) == (record_id, capability))
        body = self.files[Path(entry["path"])]
        _, metadata, text = body.split("---", 2)
        return entry, yaml.safe_load(metadata), text

    def test_catalogue_covers_pinned_matrix_and_source_heading_counts(self):
        self.assertEqual(self.catalogue["schema_version"], 2)
        self.assertEqual(self.catalogue["summary"], {
            "capability_count": 37, "epic_counts": {"MUST": 124, "MAY": 347},
            "acceptance_criterion_counts": {"MUST": 301, "MAY": 585}, "source_example_count": 2,
        })
        matrix = extract.captured(extract.MATRIX_RAW)
        self.assertEqual(hashlib.sha256(matrix).hexdigest(), self.catalogue["matrix"]["source_sha256"])
        self.assertTrue(self.catalogue["matrix"]["archive_url"].endswith("/GPITF/GP-IT-Futures-Capabilities-and-Standards-Home/"))
        table = BeautifulSoup(matrix, "html.parser").table
        rows = table.find_all("tr")[2:]
        expected_pages = [re.search(r"/pages/(\d+)", a["href"])[1] for row in rows
                          for cell in row.find_all("td", recursive=False)[1:] for a in cell.select("h3 a[href]")]
        entries = self.catalogue["capabilities"]
        self.assertEqual([cap["confluence_page_id"] for cap in entries], expected_pages)
        epics = [item for item in self.records if item["kind"] == "epic"]
        self.assertEqual(len({item["id"] for item in epics}), 429)
        for cap in entries:
            spec_id = cap["specification_id"]
            with self.subTest(capability=spec_id):
                raw = extract.captured(Path(cap["source_file"]).relative_to(extract.BASE))
                self.assertEqual(hashlib.sha256(raw).hexdigest(), cap["source_sha256"])
                source = BeautifulSoup(raw, "html.parser")
                expected = [(h["id"], h.get_text(strip=True)[:6]) for h in source.select("td > h3")]
                actual = [item for item in epics if item["specification_id"] == spec_id]
                self.assertEqual([(record["anchor"], record["id"]) for record in actual], expected)
                self.assertEqual(Counter(r["priority"] for r in actual), cap["epic_counts"])
                for priority, count in cap["acceptance_criterion_counts"].items():
                    self.assertEqual(sum(r["acceptance_criterion_count"] for r in actual if r["priority"] == priority), count)
                self.assertEqual(sum(cap["acceptance_criterion_counts"].values()),
                                 sum(h.get_text(strip=True).lower().startswith("acceptance criteri") for h in source.select("td > h4")))

    def test_every_index_path_and_local_link_resolves(self):
        indexed = [Path(entry["path"]) for entry in self.records + self.catalogue["capabilities"]]
        self.assertEqual(len(indexed), len(set(indexed)))
        self.assertEqual(set(indexed), set(self.files) - {Path("README.md"), Path("index.json")})
        absolute_paths = {path.resolve() for path in self.files}
        for path, text in self.files.items():
            if path.suffix != ".md":
                continue
            body = text.split("---", 2)[-1] if text.startswith("---\n") else text
            html = BeautifulSoup(markdown(body, extensions=["tables"]), "html.parser")
            for link in html.select("a[href]"):
                parts = urlsplit(link["href"])
                if not parts.scheme and not parts.netloc:
                    self.assertIn((path.parent / parts.path).resolve(), absolute_paths, (path, link["href"]))

    def test_duplicate_ids_keep_their_own_priority_and_provenance(self):
        gp, _, _ = self.record("E00310", "C1")
        other, _, _ = self.record("E00310", "C3")
        self.assertNotEqual(gp["path"], other["path"])
        self.assertNotEqual(gp["anchor"], other["anchor"])

    def test_deprecated_productivity_keeps_guidance_and_examples_separate(self):
        _, metadata, description = self.record("description", "C41")
        self.assertEqual(metadata["status_at_capture"], "Deprecated")
        self.assertEqual(metadata["frameworks"], ["GP IT Futures"])
        self.assertNotIn("contracting_vehicles", metadata)
        self.assertIn("The Productivity Capability is used to describe", description)
        _, metadata, guidance = self.record("must-epic-guidance", "C41")
        self.assertNotIn("priority", metadata)
        self.assertIn("requirements for Productivity are to be defined by Suppliers", guidance)
        for example in ("C41E1", "C41E2"):
            entry, metadata, text = self.record(example, "C41")
            self.assertEqual(entry["kind"], "source-example")
            self.assertNotIn("priority", metadata)
            self.assertIn("## Acceptance criterion 1: title", text)

    def test_index_covers_pinned_capability_and_links_to_every_epic(self):
        epics = [item for item in self.records if item["kind"] == "epic" and item["specification_id"] == "C5"]
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
        self.assertNotIn("E00222", text)
        rendered = BeautifulSoup(markdown(text), "html.parser")
        self.assertIn("E00221 - Supporting Information", [h.get_text() for h in rendered.select("h2")])
        self.assertIn("../../../../C1-appointments-management-citizen/1.1.0/README.md",
                      [a["href"] for a in rendered.select("a[href]")])
        item = next(li for li in rendered.select("li") if li.get_text(strip=True).startswith("Examples of amending a Session"))
        self.assertIsNone(item.find_parent("li"))

    def test_reporting_rule_is_separate_from_the_capability_and_cross_linked(self):
        entry, metadata, text = self.record("WPAD-DI-016", "S62")
        self.assertEqual((metadata["specification_id"], metadata["publisher_version"], metadata["priority"]), ("S62", "4.0.1", "MUST"))
        self.assertIn("- Not an Appointment", text)
        self.assertNotIn("WPAD-DI-017", text)
        epic, _, text = self.record("E00219")
        reference = Path(epic["path"]).parent / "../../../../../standards/S62-appointments-data-reporting/4.0.1/WPAD-DI-016.md"
        self.assertEqual(reference.resolve(), Path(entry["path"]).resolve())
        self.assertIn("## Archive cross-reference", text)
        self.assertIn("../../../../../standards/S62-appointments-data-reporting/4.0.1/WPAD-DI-016.md", text)

    def test_bare_description_fragments_keep_text_and_link(self):
        _, _, text = self.record("description", "C3")
        rendered = BeautifulSoup(markdown(text), "html.parser")
        self.assertIn("Enables Patients to request for a Repeat medication", rendered.get_text())
        self.assertIn("to be issued online.", rendered.get_text())

    def test_regeneration_is_deterministic(self):
        self.assertEqual(self.files, extract.generate())

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
