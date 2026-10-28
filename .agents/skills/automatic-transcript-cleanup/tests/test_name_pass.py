import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "name_pass.py"
SPEC = importlib.util.spec_from_file_location("name_pass", SCRIPT)
np = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(np)


class NamePassTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.path = self.root / "_sessions/dunmar-frontier/dunmari-frontier-001/cleaned/dunmari-frontier-001-source-cleaned.md"
        self.path.parent.mkdir(parents=True)
        self.original = (
            "[u0001 | 00:00:00.000-00:00:01.000 | DM] User’s existing edit; [[Real Note]] [laughs].\r\n"
            "[u0002 | 00:00:01.000-00:00:02.000 | PC] {{sarah}} and {{sarah}}; {{Sura}}.\r\n"
            "[u0003 | 00:00:02.000-00:00:03.000 | DM] {{unknown name}} and {{mumbling}}.\r\n"
        ).encode("utf-8")
        self.path.write_bytes(self.original)
        self.evidence = self.root / "People/Sura.md"
        self.evidence.parent.mkdir()
        self.evidence.write_text("---\nname: Sura\n---\n# Sura\nA known contact.\n")

    def group(self, id, action, marker_ids=None, replacements=None, confidence=None):
        return {"id": id, "action": action,
                "confidence": confidence or {"replace": "high", "review": "unresolved", "leave": "not_applicable"}[action],
                "reason": "The named contact matches the conversation." if action == "replace" else "Uncertain name." if action == "review" else "Ordinary wording outside the name pass.",
                "evidence": ["People/Sura.md"] if action == "replace" else [],
                "candidates": ["Nura"] if action == "review" else [],
                "markerIds": marker_ids or [], "replacements": replacements or {}}

    def plan(self):
        return {"schemaVersion": 1, "passVersion": "names-v1", "transcriptSha256": np.digest(self.path.read_bytes()),
                "groups": [self.group("sura", "replace", replacements={"u0002:m1": "Sura", "u0002:m2": "Sura", "u0002:m3": "Sura"}),
                           self.group("unknown", "review", ["u0003:m1"]),
                           self.group("outside", "leave", ["u0003:m2"])]}

    def test_no_markers_never_decodes_or_full_reads(self):
        self.path.write_bytes(b"not even a transcript \xff\n")
        with patch.object(Path, "read_bytes", side_effect=AssertionError("Full read forbidden")):
            value = np.scan(self.root, self.path)
            self.assertEqual(value["status"], "skipped_no_markers")
            result, log = np.apply(self.root, self.path, None)
        self.assertIsNone(log)
        self.assertEqual(result["markerCount"], 0)
        self.assertFalse((self.path.parent / "cleanup-artifacts").exists())

    def test_cli_zero_guard_precedes_opening_missing_plan(self):
        self.path.write_text("[u0001 | notes] Fine.\n")
        run = subprocess.run([sys.executable, str(SCRIPT), "apply", "--vault-root", str(self.root),
                              "--transcript", str(self.path), "--plan", str(self.root / "absent.json")], capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stderr)
        self.assertIn("skipped_no_markers", run.stdout)
        self.assertFalse((self.path.parent / "cleanup-artifacts").exists())

    def test_duplicate_occurrences_have_independent_ids(self):
        value = np.scan(self.root, self.path)
        self.assertEqual([m["markerId"] for m in value["markers"]], ["u0002:m1", "u0002:m2", "u0002:m3", "u0003:m1", "u0003:m2"])
        self.assertIn("[[Real Note]]", value["markers"][0]["contextBefore"][0])

    def test_preview_has_no_writes(self):
        record = np.enrich_retained(self.root, self.path, np.validate_plan(self.root, self.path, self.plan()))
        output = np.render_report(record)
        self.assertIn("## Name decisions left for review", output)
        self.assertIn("{{unknown name}}", output)
        self.assertEqual(self.path.read_bytes(), self.original)
        self.assertFalse((self.path.parent / "cleanup-artifacts").exists())

    def test_apply_logs_exact_bytes_and_full_undo(self):
        record, log = np.apply(self.root, self.path, self.plan())
        expected = self.original.replace(b"{{sarah}}", b"Sura").replace(b"{{Sura}}", b"Sura")
        self.assertEqual(self.path.read_bytes(), expected)
        self.assertEqual(np.counts(record)["markerOnly"], 1)
        self.assertEqual(np.counts(record)["markersAfter"], 2)
        self.assertEqual(record["lines"]["u0002"]["before"].encode(), self.original.splitlines(keepends=True)[1])
        self.assertEqual({p.name for p in log.parent.iterdir()}, {"journal.json", "review.md", "changes.diff"})
        self.assertIn("{{sarah}}", (log.parent / "review.md").read_text())
        self.assertIn("People/Sura.md", (log.parent / "review.md").read_text())
        np.undo(self.root, log)
        self.assertEqual(self.path.read_bytes(), self.original)
        self.assertEqual(np.read_json(log)["state"], "reverted")

    def test_supported_confidence_is_applied_and_labeled(self):
        plan = self.plan()
        plan["groups"][0]["confidence"] = "supported"
        record, log = np.apply(self.root, self.path, plan)
        self.assertEqual(np.counts(record)["appliedSupported"], 3)
        self.assertIn("supported", (log.parent / "review.md").read_text())

    def test_selective_undo_and_repeated_undo(self):
        _, log = np.apply(self.root, self.path, self.plan())
        record, _ = np.undo(self.root, log, ["u0002:m2"])
        self.assertIn(b"Sura and {{sarah}}; Sura.", self.path.read_bytes())
        self.assertEqual(np.counts(record)["undone"], 1)
        before_log = log.read_bytes()
        np.undo(self.root, log, ["u0002:m2"])
        self.assertEqual(log.read_bytes(), before_log)
        np.undo(self.root, log)
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_undo_preserves_later_changes_on_other_lines(self):
        _, log = np.apply(self.root, self.path, self.plan())
        later = self.path.read_bytes().replace(b"User", b"Later user")
        self.path.write_bytes(later)
        np.undo(self.root, log)
        self.assertEqual(self.path.read_bytes(), self.original.replace(b"User", b"Later user"))

    def test_undo_refuses_changed_affected_line_without_overwriting(self):
        _, log = np.apply(self.root, self.path, self.plan())
        later = self.path.read_bytes().replace(b"Sura and", b"Sura now and")
        self.path.write_bytes(later)
        journal_before = log.read_bytes()
        with self.assertRaisesRegex(ValueError, "Undo conflict"):
            np.undo(self.root, log)
        self.assertEqual(self.path.read_bytes(), later)
        self.assertEqual(log.read_bytes(), journal_before)

    def test_invalid_plans_leave_no_artifacts(self):
        variants = []
        for change in ["stale", "missing", "duplicate", "newline", "marker", "wikilink", "extra", "archival", "outside-root"]:
            p = copy.deepcopy(self.plan())
            if change == "stale": p["transcriptSha256"] = "0" * 64
            elif change == "missing": p["groups"].pop()
            elif change == "duplicate": p["groups"][1]["markerIds"].append("u0002:m1")
            elif change == "newline": p["groups"][0]["replacements"]["u0002:m1"] = "Sura\nOther"
            elif change == "marker": p["groups"][0]["replacements"]["u0002:m1"] = "{{Sura}}"
            elif change == "wikilink": p["groups"][0]["replacements"]["u0002:m1"] = "[[Sura]]"
            elif change == "extra": p["groups"][0]["extra"] = True
            elif change == "archival":
                source = self.root / "_sessions/dunmar-frontier/dunmari-frontier-001/sources/raw.md"
                source.parent.mkdir(exist_ok=True)
                source.write_text("Sura")
                p["groups"][0]["evidence"] = [str(source)]
            else: p["groups"][0]["evidence"] = ["../outside.md"]
            variants.append((change, p))
        for label, plan in variants:
            with self.subTest(label=label):
                with self.assertRaises(ValueError): np.apply(self.root, self.path, plan)
                self.assertEqual(self.path.read_bytes(), self.original)
                self.assertFalse((self.path.parent / "cleanup-artifacts").exists())

    def test_malformed_marker_and_duplicate_uid_block(self):
        for raw in [b"[u0001 | DM] {{bad\n", b"[u0001 | DM] {{{bad}}}\n", b"[u0001 | DM] {{x}}\n[u0001 | DM] More.\n"]:
            self.path.write_bytes(raw)
            with self.assertRaises(ValueError): np.scan(self.root, self.path)

    def test_plan_cannot_be_replayed_after_input_changes(self):
        plan = self.plan()
        np.apply(self.root, self.path, plan)
        with self.assertRaisesRegex(ValueError, "Stale plan"):
            np.apply(self.root, self.path, plan)

    def test_zero_replacements_records_review_without_changing_source(self):
        plan = self.plan()
        plan["groups"][0] = self.group("sura", "review", ["u0002:m1", "u0002:m2", "u0002:m3"])
        record, log = np.apply(self.root, self.path, plan)
        self.assertEqual(record["state"], "reviewed_no_changes")
        self.assertTrue(log.is_file())
        self.assertEqual(self.path.read_bytes(), self.original)
        rows = np.batch(self.root, "_sessions/dunmar-frontier")["sessions"]
        self.assertEqual(rows[0]["status"], "reviewed_current")

    def test_evidence_change_invalidates_resume(self):
        np.apply(self.root, self.path, self.plan())
        self.assertEqual(np.batch(self.root, "_sessions/dunmar-frontier")["sessions"][0]["status"], "reviewed_current")
        self.evidence.write_text("Changed evidence.")
        self.assertEqual(np.batch(self.root, "_sessions/dunmar-frontier")["sessions"][0]["status"], "ready")

    def test_write_ahead_survives_failure_before_transcript_write(self):
        original_write = np.atomic_write
        def fail_target(path, raw):
            if Path(path).resolve() == self.path.resolve(): raise OSError("Simulated failure")
            original_write(path, raw)
        with patch.object(np, "atomic_write", side_effect=fail_target):
            with self.assertRaises(OSError): np.apply(self.root, self.path, self.plan())
        log = next((self.path.parent / "cleanup-artifacts").glob("automatic-transcript-cleanup/*/journal.json"))
        self.assertEqual(np.read_json(log)["state"], "prepared")
        self.assertEqual(self.path.read_bytes(), self.original)
        record, _ = np.recover(self.root, log)
        self.assertEqual(record["state"], "aborted")

    def test_recover_after_transcript_write_before_final_log(self):
        save = np.save_outputs
        def fail_final(path, record):
            if record["state"] == "applied": raise OSError("Simulated final-log failure")
            save(path, record)
        with patch.object(np, "save_outputs", side_effect=fail_final):
            with self.assertRaises(OSError): np.apply(self.root, self.path, self.plan())
        log = next((self.path.parent / "cleanup-artifacts").glob("automatic-transcript-cleanup/*/journal.json"))
        self.assertNotEqual(self.path.read_bytes(), self.original)
        record, _ = np.recover(self.root, log)
        self.assertEqual(record["state"], "applied")
        np.undo(self.root, log)
        self.assertEqual(self.path.read_bytes(), self.original)

    def test_recover_interrupted_selective_undo(self):
        _, log = np.apply(self.root, self.path, self.plan())
        write = np.atomic_write
        def fail_after_target(path, raw):
            write(path, raw)
            if Path(path).resolve() == self.path.resolve(): raise OSError("Simulated crash after undo write")
        with patch.object(np, "atomic_write", side_effect=fail_after_target):
            with self.assertRaises(OSError): np.undo(self.root, log, ["u0002:m2"])
        record, _ = np.recover(self.root, log)
        self.assertEqual(record["undoneMarkerIds"], ["u0002:m2"])
        self.assertIn(b"Sura and {{sarah}}; Sura.", self.path.read_bytes())

    def test_recovery_refuses_unrelated_current_content(self):
        save = np.save_outputs
        def fail_final(path, record):
            if record["state"] == "applied": raise OSError("stop")
            save(path, record)
        with patch.object(np, "save_outputs", side_effect=fail_final):
            with self.assertRaises(OSError): np.apply(self.root, self.path, self.plan())
        log = next((self.path.parent / "cleanup-artifacts").glob("automatic-transcript-cleanup/*/journal.json"))
        self.path.write_bytes(self.path.read_bytes().replace(b"User", b"Later"))
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, "Recovery conflict"): np.recover(self.root, log)
        self.assertEqual(self.path.read_bytes(), before)

    def test_batch_reports_zero_missing_and_ambiguous(self):
        campaign = self.path.parents[2]
        (campaign / "dunmari-frontier-002").mkdir()
        empty = campaign / "dunmari-frontier-003/cleaned"
        empty.mkdir(parents=True)
        (empty / "dunmari-frontier-003-source-cleaned.md").write_text("No markers.\n")
        duplicate = campaign / "dunmari-frontier-004/cleaned"
        duplicate.mkdir(parents=True)
        for prefix in ["a", "b"]: (duplicate / f"{prefix}-source-cleaned.md").write_text("{{x}}")
        self.assertEqual([r["status"] for r in np.batch(self.root, campaign)["sessions"]],
                         ["ready", "missing_cleaned", "skipped_no_markers", "ambiguous_cleaned"])

    def test_batch_summary_counts_invocation_journals_only(self):
        _, journal = np.apply(self.root, self.path, self.plan())
        manifest = np.batch(self.root, "_sessions/dunmar-frontier")
        with_run = np.render_batch(self.root, manifest, [journal])
        self.assertIn("| 5 | 3 | 0 | 1 | 1 | 2 |", with_run)
        self.assertIn("[review log]", with_run)
        resumed = np.render_batch(self.root, manifest, [])
        self.assertIn("reviewed_current", resumed)
        self.assertIn("| Total | evaluated this invocation | 0 | 0 | 0 | 0 | 0 | 0 |", resumed)
        with self.assertRaisesRegex(ValueError, "one invocation journal"):
            np.render_batch(self.root, manifest, [journal, journal])


if __name__ == "__main__":
    unittest.main()
