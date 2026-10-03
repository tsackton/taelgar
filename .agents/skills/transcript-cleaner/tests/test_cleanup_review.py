import json
import sys
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch
from urllib.error import HTTPError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import review_cleanup as review
import report_cleanup_diff as report


class CleanupReviewTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / "cleaned.md"
        self.source.write_bytes(
            b"[u0001 | 00:00:00.000-00:00:01.000 | DM] Before.\r\n"
            b"[u0002 | 00:00:01.000-00:00:02.000 | PC] Meet [[garbled name]].\r\n"
            b"[u0003 | 00:00:02.000-00:00:03.000 | Unknown] [[mumbling]]\r\n"
            b"[u0004 | 00:00:03.000-00:00:04.000 | DM] After.\r\n")
        self.assessment = {"transcriptSha256": review.digest(self.source), "issues": [
            {"uid": "u0002", "importance": "material", "reason": "Recipient's identity."},
            {"uid": "u0003", "importance": "incidental", "reason": "Unrelated table chatter."}]}
        self.review = review.inventory(self.source, self.assessment)
        self.decisions = self.root / "decisions.json"

    def test_context_and_materiality(self):
        self.assertEqual(self.review["pendingMaterialCount"], 1)
        self.assertEqual(self.review["incidentalCount"], 1)
        self.assertIn("Before.", self.review["issues"][0]["before"][0])
        self.assertIn("After.", self.review["issues"][0]["after"][-1])

    def test_source_preparation_timecode_formats(self):
        self.assertEqual(review.seconds("90:02.5"), 5402.5)
        self.assertEqual(review.seconds("62.5"), 62.5)
        self.assertEqual(review.seconds("01:30:02.5"), 5402.5)
        self.source.write_text("[u0001 | 01:02.5-63.5 | DM] [[A name]].\n")
        self.assertEqual(review.inventory(self.source)["issues"][0]["start"], 62.5)

    def test_acceptance_preserves_text_and_survives_resume(self):
        before = self.source.read_bytes()
        value = review.save_decision(self.review, self.decisions, {"skipRemaining": True})
        self.assertEqual(self.source.read_bytes(), before)
        resumed = review.inventory(self.source, self.assessment, value)
        self.assertEqual(resumed["pendingMaterialCount"], 0)
        self.assertEqual(resumed["acceptedCount"], 2)

    def test_apply_preserves_headers_crlf_and_skipped_line(self):
        before = self.source.read_bytes()
        review.save_decision(self.review, self.decisions, {"uid": "u0002", "status": "correct", "text": "Meet Nura."})
        review.save_decision(self.review, self.decisions, {"skipRemaining": True})
        self.assertEqual(review.apply_decisions(self.review, self.decisions), 1)
        self.assertEqual(self.source.read_bytes(), before.replace(b"Meet [[garbled name]].", b"Meet Nura."))
        self.assertEqual(review.apply_decisions(self.review, self.decisions), 0)
        resumed = review.inventory(self.source, decisions=review.read_json(self.decisions))
        self.assertEqual(resumed["pendingMaterialCount"], 0)
        self.assertEqual((self.root / "decisions.before-apply.md").read_bytes(), before)

    def test_stale_corrections_and_assessments_fail(self):
        review.save_decision(self.review, self.decisions, {"uid": "u0002", "status": "correct", "text": "Meet Nura."})
        self.source.write_bytes(self.source.read_bytes().replace(b"Before.", b"New text."))
        before = self.source.read_bytes()
        with self.assertRaisesRegex(ValueError, "stale"):
            review.apply_decisions(self.review, self.decisions)
        self.assertEqual(self.source.read_bytes(), before)
        with self.assertRaisesRegex(ValueError, "stale"):
            review.inventory(self.source, self.assessment)
        self.assertEqual(review.inventory(self.source, decisions=review.read_json(self.decisions))["pendingMaterialCount"], 2)

    def test_correction_after_skip_only_apply_is_not_lost(self):
        review.save_decision(self.review, self.decisions, {"skipRemaining": True})
        self.assertEqual(review.apply_decisions(self.review, self.decisions), 0)
        review.save_decision(self.review, self.decisions, {"uid": "u0002", "status": "correct", "text": "Meet Nura."})
        self.assertEqual(review.apply_decisions(self.review, self.decisions), 1)
        self.assertIn("Meet Nura.", self.source.read_text())

    def test_changed_review_position_cannot_overwrite_another_line(self):
        review.save_decision(self.review, self.decisions, {"uid": "u0002", "status": "correct", "text": "Meet Nura."})
        self.review["issues"][0]["index"] = 0
        before = self.source.read_bytes()
        with self.assertRaisesRegex(ValueError, "position"):
            review.apply_decisions(self.review, self.decisions)
        self.assertEqual(self.source.read_bytes(), before)

    def test_invalid_correction_does_not_write_decisions(self):
        for text in ("", "split\nline", "still [[unclear]]"):
            with self.assertRaises(ValueError):
                review.save_decision(self.review, self.decisions, {"uid": "u0002", "status": "correct", "text": text})
        self.assertFalse(self.decisions.exists())

    def test_report_context_without_structural_failure_for_markers(self):
        rows = report.read_transcript(self.source)
        result, _ = report.build_reports(rows, rows)
        self.assertEqual(result["validationErrors"], [])
        self.assertEqual(result["unresolvedCount"], 2)
        self.assertIn("Before.", result["unresolvedPhrases"][0]["contextBefore"][0])
        altered = [dict(row) for row in rows]
        altered[0]["header"] = "[u0001 | 00:00:00.000-00:00:01.000 | Someone else]"
        result, _ = report.build_reports(rows, altered)
        self.assertTrue(result["validationErrors"])

    def test_local_server_save_and_token(self):
        path = self.root / "review.json"
        review.write_json(path, self.review)
        server = review.make_server(path, self.decisions)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        base = f"http://127.0.0.1:{server.server_port}"
        with urlopen(base) as response:
            html = response.read().decode()
        token = html.split('const token="')[1].split('";')[0]
        body = json.dumps({"uid": "u0002", "status": "skip"}).encode()
        with self.assertRaises(HTTPError) as caught:
            urlopen(Request(base + "/api/decision", data=body))
        self.assertEqual(caught.exception.code, 403)
        with urlopen(Request(base + "/api/decision", data=body, headers={"X-Review-Token": token})) as response:
            value = json.load(response)
        self.assertEqual(value["decisions"]["u0002"]["status"], "skip")

    def test_audio_mapping_offsets_and_missing_mapping(self):
        audio = self.root / "recording.m4a"
        audio.write_bytes(b"test")
        media_path = ROOT.parent / "transcribe-session" / "scripts"
        sys.path.insert(0, str(media_path))
        import media_tools
        with patch.object(media_tools, "resolve_clip_backend", return_value="backend"), \
             patch.object(media_tools, "prepare_clip_source", return_value=(audio, "backend")), \
             patch.object(media_tools, "probe_duration", return_value=20), \
             patch.object(media_tools, "extract_audio_clip") as extract:
            mappings = [{"startUid": "u0001", "endUid": "u0004", "audioPath": str(audio), "offsetSeconds": 10}]
            review.add_clips(self.review, mappings, self.root)
            self.assertEqual(extract.call_args_list[0].kwargs["start_seconds"], 10)
            self.assertEqual(extract.call_args_list[0].kwargs["end_seconds"], 14)
            self.assertEqual(self.review["issues"][0]["clip"], "u0002.m4a")
            mappings[0]["endUid"] = "u0002"
            with self.assertRaisesRegex(ValueError, "exactly one"):
                review.add_clips(self.review, mappings, self.root)


if __name__ == "__main__":
    unittest.main()
