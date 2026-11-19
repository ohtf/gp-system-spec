# SPDX-License-Identifier: AGPL-3.0-or-later

import importlib.util
import json
from collections import deque
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from unittest.mock import Mock, patch

import requests


spec = importlib.util.spec_from_file_location(
    "confluence_mirror", Path(__file__).resolve().parents[1] / "tools/confluence-mirror.py"
)
mirror = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mirror)


def response(status, data=None, retry_after=None):
    result = requests.Response()
    result.status_code = status
    result.url = "https://nhse-dsic.atlassian.net/wiki/api/v2/pages"
    result._content = json.dumps(data).encode()
    result._content_consumed = True
    if retry_after is not None:
        result.headers["Retry-After"] = retry_after
    return result


class RequestTests(unittest.TestCase):
    def test_rate_limit_waits_before_reissuing_request(self):
        session = Mock()
        session.get.side_effect = [response(429, retry_after="30"), response(200)]
        with patch.object(mirror.time, "sleep") as sleep:
            self.assertEqual(mirror.get(session, "url").status_code, 200)
        sleep.assert_called_once_with(30)

    def test_http_date_is_understood(self):
        later = datetime.now(timezone.utc) + timedelta(seconds=45)
        self.assertGreater(mirror.retry_after(format_datetime(later, usegmt=True), 15), 42)

    def test_long_rate_limit_does_not_issue_another_request(self):
        session = Mock()
        session.get.return_value = response(429, retry_after="3600")
        with self.assertRaisesRegex(mirror.StopMirror, "3600"):
            mirror.get(session, "url")
        session.get.assert_called_once()

    def test_access_denied_is_not_retried(self):
        session = Mock()
        session.get.return_value = response(403)
        with self.assertRaises(mirror.StopMirror):
            mirror.get(session, "url")
        session.get.assert_called_once()

    def test_requests_use_a_single_pacing_clock(self):
        clock = deque([0, 0, 0.5, 1.5])
        request = Mock()
        session = mirror.PacedSession()
        with patch.object(mirror.time, "monotonic", side_effect=clock), \
                patch.object(mirror.time, "sleep") as sleep, \
                patch.object(requests.Session, "send") as send:
            session.send(request)
            session.send(request)
        sleep.assert_called_once_with(1.0)
        self.assertEqual(send.call_count, 2)

    def test_repeated_cursor_is_not_a_complete_enumeration(self):
        session = Mock()
        session.get.side_effect = [
            response(200, {"results": [], "_links": {"next": "?cursor=x"}}),
            response(200, {"results": [], "_links": {"next": "?cursor=x"}}),
        ]
        with self.assertRaisesRegex(RuntimeError, "repeated pagination cursor"):
            list(mirror.iter_results(session, "url", 250))


class ArchiveTests(unittest.TestCase):
    def test_attachment_audit_checks_all_inventoried_pages_and_reports_gaps(self):
        old_root = mirror.DOCS_ROOT
        self.addCleanup(mirror.set_output_root, old_root)
        with TemporaryDirectory() as tmp:
            root = Path(tmp)
            mirror.set_output_root(root)
            inventory_dir = root / ".inventory"
            inventory_dir.mkdir()
            (inventory_dir / "GPITF.json").write_text(json.dumps({"current_pages": {"1": 1, "2": 2}}))
            saved = root / "file"
            saved.write_bytes(b"data")
            downloads = [[{"path": str(saved), "status": "ok"}], [{"status": "failed"}]]
            with patch.object(mirror, "download_attachments", side_effect=downloads):
                self.assertEqual(mirror.audit_attachments(Mock(), "https://example.test", ["GPITF"]), 1)
            lines = (inventory_dir / "GPITF-attachments.jsonl").read_text().splitlines()
            self.assertEqual(json.loads(lines[0]), {
                "page_id": "1", "attachments": [{"path": "file", "status": "ok", "bytes": 4}],
            })
            self.assertEqual(json.loads(lines[1])["page_id"], "2")

    def test_collision_does_not_overwrite_prior_archive(self):
        old_root = mirror.DOCS_ROOT
        self.addCleanup(mirror.set_output_root, old_root)
        with TemporaryDirectory() as tmp:
            mirror.set_output_root(Path(tmp))
            original = Path(tmp) / "DCSDCS/Title.md"
            original.parent.mkdir()
            original.write_text("historical")
            manifest = {"DCSDCS/1": {"version": 1, "path": "DCSDCS/Title.md", "title": "Title"}}
            pages = [{"id": "2", "title": "Title", "version": {"number": 1}}]
            with patch.object(mirror, "enumerate_pages", return_value=pages), \
                    patch.object(mirror, "fetch_page_body", return_value=("<p>Hello</p>", pages[0])), \
                    patch.object(mirror, "download_attachments", return_value=[]):
                result = mirror.mirror_space(Mock(), "https://example.test/wiki", "DCSDCS", manifest, False, False, set())
            self.assertEqual(result, (1, 0, []))
            self.assertEqual(original.read_text(), "historical")
            self.assertIn("Hello", (Path(tmp) / "DCSDCS/_by-id/2.md").read_text())
            inventory = json.loads((Path(tmp) / ".inventory/DCSDCS.json").read_text())
            self.assertEqual(inventory["prior_pages_not_listed"], ["1"])
