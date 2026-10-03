import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from review_timeline import check_current, input_records, review_timeline


class TimelineReviewTest(unittest.TestCase):
    def setUp(self):
        self.rows = [{"uid": f"u{i:04}", "text": text} for i, text in enumerate(
            ["It is evening.", "You sleep.", "The following dawn.", "You arrive."], 1)]
        self.beats = [
            {"beatId": "b1", "startUid": "u0001", "endUid": "u0002", "dateStart": "1749-09-16", "timeWindow": "evening"},
            {"beatId": "b2", "startUid": "u0003", "endUid": "u0004", "dateStart": "1749-09-17", "timeWindow": "morning"}]
        self.facts = copy.deepcopy(self.beats)
        self.session = {"drStart": "1749-09-16", "drEnd": "1749-09-17"}
        self.evidence = {"inferredStart": "1749-09-16", "inferredEnd": "1749-09-17", "transitions": [
            {"uid": "u0001", "date": "1749-09-16", "time": "evening", "basis": "explicit", "evidence": "It is evening."},
            {"uid": "u0003", "date": "1749-09-17", "time": "morning", "basis": "explicit", "evidence": "Following dawn after sleeping."}]}

    def run_review(self):
        return review_timeline(self.session, self.beats, self.facts, self.evidence, self.rows)

    def test_consistent_timeline_continues_without_review(self):
        result = self.run_review()
        self.assertFalse(result["needsHumanInput"])
        self.assertEqual(result["transitions"][1]["beatId"], "b2")

    def test_blank_end_is_proposed_without_modifying_yaml(self):
        self.session["drEnd"] = None
        result = self.run_review()
        self.assertTrue(result["needsHumanInput"])
        self.assertEqual(result["proposedYamlChanges"], [{"field": "drEnd", "current": None, "proposed": "1749-09-17"}])
        self.assertIsNone(self.session["drEnd"])
        self.evidence["resolutions"] = {"yaml:drEnd": {"by": "source", "reason": "Clearly the next day."}}
        with self.assertRaisesRegex(ValueError, "Only the user"):
            self.run_review()
        self.evidence["resolutions"]["yaml:drEnd"] = {"by": "human", "reason": "User deliberately kept YAML end unknown."}
        self.assertFalse(self.run_review()["needsHumanInput"])

    def test_date_conflict_and_annotation_drift_are_flagged(self):
        self.session["drEnd"] = "1749-09-16"
        self.facts[1]["dateStart"] = "1749-09-18"
        keys = {item["key"] for item in self.run_review()["issues"]}
        self.assertIn("yaml:drEnd", keys)
        self.assertIn("b2:dateStart", keys)

    def test_internal_transition_in_one_beat_is_preserved(self):
        self.beats = [{**self.beats[0], "endUid": "u0004", "dateEnd": "1749-09-17"}]
        self.facts = copy.deepcopy(self.beats)
        result = self.run_review()
        self.assertFalse(result["needsHumanInput"])
        self.assertEqual([t["beatId"] for t in result["transitions"]], ["b1", "b1"])

    def test_source_ambiguity_requires_resolution(self):
        self.evidence["issues"] = [{"detail": "Unclear whether the second rest occurred.", "evidence": "u0003 is garbled."}]
        self.assertTrue(self.run_review()["needsHumanInput"])

    def test_all_inputs_must_still_match(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "session.yaml"
            path.write_text("drEnd: null\n")
            report = {"inputs": input_records({"session": path})}
            check_current(report)
            path.write_text("drEnd: 1749-09-17\n")
            with self.assertRaisesRegex(ValueError, "stale"):
                check_current(report)


if __name__ == "__main__":
    unittest.main()
