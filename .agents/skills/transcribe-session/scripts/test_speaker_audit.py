#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("speaker_audit.py")
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("speaker_audit", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SpeakerAuditTests(unittest.TestCase):
    def test_proportional_allocation_covers_small_strata_and_total(self) -> None:
        sizes = {("p1", "p2"): 25, ("p1", "p3"): 10, ("p2", "p3"): 2}
        allocation = MODULE.allocate_strata(sizes, 12, balanced=False)
        self.assertEqual(sum(allocation.values()), 12)
        self.assertTrue(all(value >= 1 for value in allocation.values()))
        self.assertGreater(allocation[("p1", "p2")], allocation[("p2", "p3")])

    def test_balanced_allocation_is_even_when_capacity_allows(self) -> None:
        sizes = {("p1",): 100, ("p2",): 80, ("p3",): 60}
        allocation = MODULE.allocate_strata(sizes, 9, balanced=True)
        self.assertEqual(allocation, {("p1",): 3, ("p2",): 3, ("p3",): 3})

    def test_candidate_scoring_excludes_current_group_references(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        embedding_by_id = {
            "candidate": np.array([1.0, 0.0]),
            "g1-a": np.array([1.0, 0.0]),
            "g1-b": np.array([1.0, 0.0]),
            "g1-c": np.array([1.0, 0.0]),
            "g2-a": np.array([0.0, 1.0]),
            "h1-a": np.array([0.8, 0.6]),
            "h2-a": np.array([0.8, 0.6]),
        }
        references = [
            {"utteranceId": "g1-a", "participantId": "p1", "groupId": "g1", "embedding": embedding_by_id["g1-a"]},
            {"utteranceId": "g1-b", "participantId": "p1", "groupId": "g1", "embedding": embedding_by_id["g1-b"]},
            {"utteranceId": "g1-c", "participantId": "p1", "groupId": "g1", "embedding": embedding_by_id["g1-c"]},
            {"utteranceId": "g2-a", "participantId": "p1", "groupId": "g2", "embedding": embedding_by_id["g2-a"]},
            {"utteranceId": "h1-a", "participantId": "p2", "groupId": "h1", "embedding": embedding_by_id["h1-a"]},
            {"utteranceId": "h2-a", "participantId": "p2", "groupId": "h2", "embedding": embedding_by_id["h2-a"]},
        ]
        review = {
            "utterances": [
                {
                    "id": "candidate",
                    "recordingId": "r1",
                    "groupId": "g1",
                    "start": 10.0,
                    "durationSeconds": 2.0,
                    "wordCount": 5,
                }
            ]
        }
        candidates = MODULE.build_candidates(
            np=np,
            review=review,
            participant_ids=["p1", "p2"],
            references=references,
            embedding_by_id=embedding_by_id,
            group_labels={"g1": {"status": "assigned", "participantId": "p1"}},
            overrides={},
        )
        self.assertEqual(len(candidates), 1)
        self.assertEqual(candidates[0]["predictedParticipantId"], "p2")
        self.assertEqual(candidates[0]["kind"], "disagreement")

    def test_public_payload_omits_comparison_labels(self) -> None:
        audit = self.audit_fixture()
        public = MODULE.public_audit_payload(audit)
        self.assertNotIn("hidden", public["items"][0])
        self.assertNotIn("audioPath", public["recordings"][0])
        self.assertEqual(public["items"][0]["utteranceId"], "u1")

    def test_decisions_reject_unknown_participant(self) -> None:
        audit = self.audit_fixture()
        decisions = {
            "schemaVersion": 1,
            "auditId": "audit-1",
            "decisions": {
                "a001": {
                    "status": "assigned",
                    "participantId": "not-a-person",
                    "transcriptRevealed": False,
                }
            },
        }
        with self.assertRaises(MODULE.SpeakerReviewError):
            MODULE.validate_decisions(audit, decisions)

    def test_report_separates_disagreement_and_control_outcomes(self) -> None:
        audit = self.audit_fixture()
        decisions = {
            "schemaVersion": 1,
            "auditId": "audit-1",
            "decisions": {
                "a001": {"status": "assigned", "participantId": "p2", "transcriptRevealed": False},
                "a002": {"status": "assigned", "participantId": "p1", "transcriptRevealed": True},
            },
        }
        report = MODULE.build_report(audit, decisions)
        self.assertEqual(report["disagreementOutcomes"]["modelCorrect"], 1)
        self.assertEqual(report["controlOutcomes"]["bothCorrect"], 1)
        self.assertEqual(report["completion"]["transcriptRevealedCount"], 1)
        self.assertEqual(report["weightedPopulationEstimate"]["modelAccuracy"], 1.0)
        self.assertEqual(report["weightedPopulationEstimate"]["currentAccuracy"], 0.3333)

    def test_overlap_is_excluded_from_accuracy_denominator(self) -> None:
        audit = self.audit_fixture()
        decisions = {
            "schemaVersion": 1,
            "auditId": "audit-1",
            "decisions": {
                "a001": {
                    "status": "overlap",
                    "participantId": None,
                    "transcriptRevealed": False,
                },
                "a002": {
                    "status": "assigned",
                    "participantId": "p1",
                    "transcriptRevealed": False,
                },
            },
        }
        MODULE.validate_decisions(audit, decisions)
        report = MODULE.build_report(audit, decisions)
        self.assertEqual(report["completion"]["overlapCount"], 1)
        self.assertEqual(report["completion"]["unknownCount"], 0)
        self.assertEqual(report["disagreementOutcomes"]["overlap"], 1)
        self.assertEqual(report["weightedPopulationEstimate"]["modelAccuracy"], 1.0)

    @staticmethod
    def audit_fixture() -> dict:
        return {
            "schemaVersion": 1,
            "auditId": "audit-1",
            "participants": [
                {"id": "p1", "name": "One", "gameRole": "One", "display": "One / One"},
                {"id": "p2", "name": "Two", "gameRole": "Two", "display": "Two / Two"},
            ],
            "recordings": [{"id": "r1", "audioPath": "/tmp/audio.m4a"}],
            "items": [
                {
                    "id": "a001",
                    "utteranceId": "u1",
                    "recordingId": "r1",
                    "start": 1.0,
                    "end": 3.0,
                    "durationSeconds": 2.0,
                    "text": "First clip",
                    "hidden": {
                        "kind": "disagreement",
                        "currentParticipantId": "p1",
                        "predictedParticipantId": "p2",
                        "margin": 0.3,
                        "samplingGroup": "p1 -> p2",
                        "populationSize": 10,
                        "sampleSize": 1,
                        "analysisWeight": 10.0,
                    },
                },
                {
                    "id": "a002",
                    "utteranceId": "u2",
                    "recordingId": "r1",
                    "start": 4.0,
                    "end": 6.0,
                    "durationSeconds": 2.0,
                    "text": "Second clip",
                    "hidden": {
                        "kind": "control",
                        "currentParticipantId": "p1",
                        "predictedParticipantId": "p1",
                        "margin": 0.4,
                        "samplingGroup": "p1",
                        "populationSize": 5,
                        "sampleSize": 1,
                        "analysisWeight": 5.0,
                    },
                },
            ],
        }


if __name__ == "__main__":
    unittest.main()
