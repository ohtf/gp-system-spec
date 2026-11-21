# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

import importlib.util
import sys
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory


def load_tool(name):
    path = Path(__file__).resolve().parents[1] / "tools" / f"{name}.py"
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(module)
    finally:
        sys.path.pop(0)
    return module


site = load_tool("prepare-site")
catalogue = load_tool("check-catalogue")
tables = load_tool("confluence_tables")


class SiteTest(unittest.TestCase):
    def test_attachment_links_preserve_parentheses_spaces_and_link_titles(self):
        url = "https://example.org/A%20%28v2%29.pdf"
        targets = {"DCSDCS/1/att2-": [("A (v2).pdf", url)]}
        text = '[One](../../attachments/DCSDCS/1/att2-A (v2).pdf "PDF")\n' \
            '![Two](../attachments/DCSDCS/1/att2-A%20%28v2%29.pdf)'
        self.assertEqual(site.link_attachments(text, targets), f'[One]({url} "PDF")\n![Two]({url})')

    def test_untracked_local_attachment_fails_closed(self):
        with self.assertRaisesRegex(ValueError, "unmatched local attachment"):
            site.link_attachments('[One](../attachments/GPITF/1/att2-local-only.pdf)', {})

    def test_capability_index_keeps_deprecated_status_and_uses_archived_page(self):
        entries = [("Productivity", Path("DCSDCS/Productivity.md"), "C41", "1.0.1", "Deprecated", "", 0)]
        index = site.capability_index(entries)
        self.assertIn("## Deprecated capabilities", index)
        self.assertIn("[Productivity](nhs-snapshot/DCSDCS/Productivity.md) | C41 | 1.0.1 | Deprecated | None", index)

    def test_restore_table_anchor_without_changing_link_or_cell_text(self):
        text = '[Testing](#Validation%26Testing)\n| Testing {#Validation&Testing} must pass |\n'
        expected = '[Testing](#Validation%26Testing)\n| Testing <span id="Validation&amp;Testing"></span> must pass |\n'
        self.assertEqual(site.restore_anchors(text, "0"), expected)

    def test_restore_short_alias_without_replacing_original_heading_id(self):
        long_id = "Communicationhttps://nhse-dsic.atlassian.net/wiki/spaces/DCSDCS/pages/1391134087/Communication"
        text = f"[Communication](#Communication)\n\n### Communication {{#{long_id}}}\n"
        self.assertEqual(
            site.restore_anchors(text, "0"),
            text.replace("###", '<span id="Communication"></span>\n\n###'),
        )
        ambiguous = text + "### Other {#" + long_id + "-Other}\n"
        self.assertEqual(site.restore_anchors(ambiguous, "0"), ambiguous)

    def test_rbac_alias_is_limited_to_the_reviewed_edition(self):
        text = "[RBAC](#InformationGovernance-Standard-RBAC)\n\n| Role-based Access Control {#InformationGovernancev2.0.0-RBACRole-basedAccessControl} |\n"
        self.assertEqual(site.restore_anchors(text, "0"), text)
        self.assertIn('<span id="InformationGovernance-Standard-RBAC"></span>', site.restore_anchors(text, "1956184126"))

    def test_rendered_check_accepts_entities_and_detects_broken_imported_links(self):
        with TemporaryDirectory() as temp:
            root = Path(temp).resolve()
            source = root / "index.html"
            target = root / "target.html"
            source.write_text('<a href="target.html#Rules%26Exceptions">Working</a><a href="#broken">Broken</a>', encoding="utf-8")
            target.write_text('<h2 id="Rules&amp;Exceptions">Rules and exceptions</h2>', encoding="utf-8")
            pages = {path: catalogue.Page(path) for path in (source, target)}
            self.assertEqual(
                catalogue.check_links(root, "https://example.org/archive/", pages, set()),
                ["index.html: missing anchor: #broken"],
            )

    def test_restore_epics_as_prose_with_confluence_ids_and_criteria(self):
        raw = '''<table><tr><td><p><strong>MUST Epics - Required</strong></p></td></tr><tr><td>
        <h3 id="E99">E99 - Manage appointments</h3><p>As a user</p><p>I want to book a slot</p>
        <h4 id="first-criterion">Acceptance criterion 1</h4><p>Given a free slot</p><p>When it is booked</p>
        <ul><li>Then the slot is reserved<ul><li>Confirmation appears</li></ul></li></ul><hr>
        <h3 id="E100">E100 - Cancel an appointment</h3></td></tr></table>'''
        text = 'Before\n\n| |\n| --- |\n| MUST Epics - Required |\n\nAfter\n'
        source = (Path("GPITF/Example.md"), tables.NHS + "/wiki/pages/1", set())
        result, count = tables.restore_tables(text, raw, source, {}, {}, {})
        self.assertEqual(count, 1)
        self.assertTrue(result.startswith("Before\n\n"))
        self.assertTrue(result.endswith("\nAfter\n"))
        self.assertNotIn("<table", result)
        self.assertIn('<h3 id="E99">E99 - Manage appointments</h3><p>As a user</p><p>I want to book a slot</p>', result)
        self.assertIn('<h4 id="first-criterion">Acceptance criterion 1</h4><p>Given a free slot</p>', result)
        self.assertIn('<ul><li>Then the slot is reserved<ul><li>Confirmation appears</li></ul></li></ul>', result)

    def test_restore_real_tables_with_merged_cells_and_safe_local_links(self):
        raw = '''<table style="width:4000px"><tr onclick="remove()"><th colspan="2">Scope</th></tr>
        <tr><td rowspan="2">R1</td><td><p><a href="/wiki/spaces/GPITF/pages/99/Foo#criteria">See criteria</a></p>
        <a href="/wiki/spaces/GPITF/pages/99/Foo?preview=/99/88/A.pdf">Attachment</a>
        <a href="javascript:example()">Label</a><script>untrusted()</script></td></tr>
        <tr><td>Continued</td></tr></table>'''
        source = (Path("DCSDCS/Source.md"), tables.NHS + "/wiki/pages/1", set())
        target = (Path("GPITF/Foo/index.md"), tables.NHS + "/wiki/pages/99", {"criteria"})
        result, _ = tables.restore_tables(
            '| Scope |\n| --- |\n', raw, source, {"99": target},
            {("99", "88", "A.pdf"): "https://example.org/A.pdf"}, {},
        )
        self.assertIn('<th colspan="2">Scope</th>', result)
        self.assertIn('<td rowspan="2">R1</td>', result)
        self.assertIn('href="../GPITF/Foo/index.md#criteria"', result)
        self.assertIn('href="https://example.org/A.pdf"', result)
        self.assertIn("<a>Label</a>", result)
        for unwanted in ("style=", "onclick=", "javascript:", "untrusted()"):
            self.assertNotIn(unwanted, result)

    def test_does_not_silently_skip_a_source_table(self):
        source = (Path("Example.md"), tables.NHS + "/wiki/pages/1", set())
        raw = '<table><tr><td>some text</td></tr></table>'
        with self.assertRaisesRegex(ValueError, "1 source tables, 0 Markdown tables"):
            tables.restore_tables('|\n', raw, source, {}, {}, {})
        with self.assertRaisesRegex(ValueError, "does not match the captured Markdown"):
            tables.restore_tables('| --- |\n| unrelated |\n', raw, source, {}, {}, {})

    def test_fragment_resolution_prefers_the_archive_only_for_unambiguous_matches(self):
        source = (Path("GPITF/Source.md"), tables.NHS + "/wiki/pages/1", set())
        url = tables.NHS + "/wiki/pages/99/Foo#E99---Manage-appointments"
        target = (Path("DCSDCS/Foo.md"), tables.NHS + "/wiki/pages/99", {"Foo-E99-Manageappointments"})
        self.assertEqual(tables.link_target(url, source, {"99": target}, {}), "../DCSDCS/Foo.md#Foo-E99-Manageappointments")
        target[2].add("Foo-other-E99-Manageappointments")
        self.assertEqual(tables.link_target(url, source, {"99": target}, {}), url)
