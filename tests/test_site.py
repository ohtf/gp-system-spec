# SPDX-FileCopyrightText: 2026 Open Health Technology Foundation contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

import importlib.util
import unittest
from pathlib import Path


spec = importlib.util.spec_from_file_location(
    "prepare_site", Path(__file__).resolve().parents[1] / "tools/prepare-site.py"
)
site = importlib.util.module_from_spec(spec)
spec.loader.exec_module(site)


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
