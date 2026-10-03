import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from manage_recap_scenes import read_timed_source, render_preview, scene_duration
from review_timeline import input_records, read_source, review_timeline


class SceneReviewTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.transcript = self.root / "source.md"
        self.transcript.write_text(
            "[u0001 | 00:00:00.000-00:00:04.000 | DM] Evening.\n"
            "[u0002 | 00:00:03.000-00:00:05.000 | PC] Rest.\n"
            "[u0003 | 00:10:00.000-00:10:05.000 | DM] Dawn.\n"
            "[u0004 | 00:20:00.000-00:20:04.000 | PC] Arrive.\n")
        self.beats = [dict(beatId="b1", title="Rest", startUid="u0001", endUid="u0002", dateStart="1749-09-16", timeWindow="evening"),
                      dict(beatId="b2", title="Travel", startUid="u0003", endUid="u0004", dateStart="1749-09-17", timeWindow="morning")]
        self.facts = [{**beat, "shortSummary": "Some action."} for beat in self.beats]
        self.scenes = {"schemaVersion": "1.0", "scenes": [dict(sceneId="scene-001", title="Rest | travel", beatIds=["b1", "b2"], rationale="One journey", overview="Rest, then travel.", transitionToNext="Session ends")]}
        self.session = {"drStart": "1749-09-16", "drEnd": "1749-09-17"}
        self.evidence = {"inferredStart": "1749-09-16", "inferredEnd": "1749-09-17", "transitions": [
            dict(uid="u0001", date="1749-09-16", time="evening", basis="explicit", evidence="Evening."),
            dict(uid="u0003", date="1749-09-17", time="morning", basis="explicit", evidence="Dawn after sleeping.")]}
        for name, value in (("session", self.session), ("beats", {"beats": self.beats}), ("facts", {"facts": self.facts}), ("scenes", self.scenes), ("evidence", self.evidence)):
            (self.root / f"{name}.json").write_text(json.dumps(value))
        self.timeline = review_timeline(self.session, self.beats, self.facts, self.evidence, read_source(self.transcript))
        paths = {key: self.root / f"{key}.json" for key in ("session", "beats", "facts", "evidence")}
        paths["transcript"] = self.transcript
        self.timeline["inputs"] = input_records(paths)
        (self.root / "timeline.json").write_text(json.dumps(self.timeline))

    def command(self, *extra):
        args = [sys.executable, str(ROOT / "scripts" / "manage_recap_scenes.py"),
                "--beats-json", str(self.root / "beats.json"), "--beat-facts-json", str(self.root / "facts.json"),
                "--recap-scenes-json", str(self.root / "scenes.json"), "--transcript", str(self.transcript),
                "--timeline-review", str(self.root / "timeline.json"), "--output-dir", str(self.root),
                "--file-prefix", "test", "--require-review-fields", *extra]
        return subprocess.run(args, capture_output=True, text=True)

    def test_duration_uses_elapsed_timestamps_and_handles_overlap(self):
        duration = scene_duration(self.scenes["scenes"][0], {b["beatId"]: b for b in self.beats}, read_timed_source(self.transcript))
        self.assertEqual(duration, "00:00:00–00:20:04 (20.1 min)")

    def test_timestamp_reset_is_not_a_negative_or_guessed_duration(self):
        self.transcript.write_text(self.transcript.read_text().replace("00:20:00.000-00:20:04.000", "00:00:00.000-00:00:04.000"))
        duration = scene_duration(self.scenes["scenes"][0], {b["beatId"]: b for b in self.beats}, read_timed_source(self.transcript))
        self.assertIn("discontinuous", duration)

    def test_note_based_input_has_no_invented_duration(self):
        self.transcript.write_text("[u0001] Evening.\n[u0002] Rest.\n[u0003] Dawn.\n[u0004] Arrival.\n")
        duration = scene_duration(self.scenes["scenes"][0], {b["beatId"]: b for b in self.beats}, read_timed_source(self.transcript))
        self.assertIn("Unavailable", duration)

    def test_source_preparation_short_timecodes_and_placeholder_times(self):
        self.transcript.write_text("[u0001 | 01:02.5-63.5 | DM] Start.\n[u0002 | 63.5-65 | PC] Rest.\n[u0003 | 01:05-66 | DM] Dawn.\n[u0004 | 66-68 | PC] Arrive.\n")
        duration = scene_duration(self.scenes["scenes"][0], {b["beatId"]: b for b in self.beats}, read_timed_source(self.transcript))
        self.assertIn("00:01:02–00:01:08", duration)
        self.transcript.write_text("\n".join(f"[u{i:04} | 00:00:00-00:00:00 | Unknown] Untimed." for i in range(1, 5)))
        duration = scene_duration(self.scenes["scenes"][0], {b["beatId"]: b for b in self.beats}, read_timed_source(self.transcript))
        self.assertIn("Unavailable", duration)

    def test_tables_include_internal_scene_transition_and_escape_pipes(self):
        preview = render_preview(self.scenes, self.beats, self.facts, read_timed_source(self.transcript), self.timeline)
        self.assertIn("Rest \\| travel", preview)
        self.assertIn("u0003 (explicit): Dawn after sleeping.", preview)
        self.assertIn("Session ends", preview)

    def test_existing_valid_scene_json_does_not_count_as_approval(self):
        result = self.command("--require-approval", "--validate-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("approval", result.stdout + result.stderr)
        self.assertEqual(self.command("--record-approval", "User approved these tables.").returncode, 0)
        self.assertEqual(self.command("--require-approval", "--validate-only").returncode, 0)
        self.scenes["scenes"][0]["overview"] = "A different description."
        (self.root / "scenes.json").write_text(json.dumps(self.scenes))
        self.assertNotEqual(self.command("--require-approval", "--validate-only").returncode, 0)

    def test_upstream_change_invalidates_review(self):
        self.assertEqual(self.command("--record-approval", "Approved.").returncode, 0)
        self.transcript.write_text(self.transcript.read_text().replace("Dawn.", "Another day."))
        result = self.command("--require-approval", "--validate-only")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("stale", result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
