#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("speaker_model.py")
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("speaker_model", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SpeakerModelTests(unittest.TestCase):
    def test_scribe_fallback_uses_inclusive_eighty_percent_threshold(self) -> None:
        participants = [
            {"id": "p1", "name": "One", "gameRole": "One"},
            {"id": "p2", "name": "Two", "gameRole": "Two"},
        ]
        utterances = []
        overrides = {}
        model_ids = []
        assignments = [
            ("speaker_0", "p1"),
            ("speaker_0", "p1"),
            ("speaker_0", "p1"),
            ("speaker_0", "p1"),
            ("speaker_0", "p2"),
            ("speaker_1", "p1"),
            ("speaker_1", "p1"),
            ("speaker_1", "p1"),
            ("speaker_1", "p2"),
            ("speaker_1", "p2"),
        ]
        for index, (scribe_id, participant_id) in enumerate(assignments, start=1):
            utterance_id = f"model-{index}"
            model_ids.append(utterance_id)
            utterances.append(
                {
                    "id": utterance_id,
                    "recordingId": "r1",
                    "groupId": "mixed",
                    "start": float(index),
                    "end": float(index + 2),
                    "durationSeconds": 2.0,
                    "wordCount": 5,
                    "text": utterance_id,
                    "scribeSpeakerIds": [scribe_id],
                }
            )
            overrides[utterance_id] = {
                "status": "assigned",
                "participantId": participant_id,
            }
        utterances.extend(
            [
                {
                    "id": "short-accepted",
                    "recordingId": "r1",
                    "groupId": "mixed",
                    "start": 20.0,
                    "end": 20.5,
                    "durationSeconds": 0.5,
                    "wordCount": 1,
                    "text": "yes",
                    "scribeSpeakerIds": ["speaker_0"],
                },
                {
                    "id": "short-rejected",
                    "recordingId": "r1",
                    "groupId": "mixed",
                    "start": 21.0,
                    "end": 21.5,
                    "durationSeconds": 0.5,
                    "wordCount": 1,
                    "text": "no",
                    "scribeSpeakerIds": ["speaker_1"],
                },
            ]
        )
        review = {
            "schemaVersion": 1,
            "reviewId": "model-assisted",
            "participants": participants,
            "groups": [
                {
                    "id": "mixed",
                    "recordingId": "r1",
                    "memberUtteranceIds": [item["id"] for item in utterances],
                    "representativeUtteranceIds": [],
                }
            ],
            "utterances": utterances,
            "recordings": [],
            "verification": {"samplesPerParticipant": 1},
            "modelAttribution": {
                "minimumDurationSeconds": 1.5,
                "minimumWordCount": 4,
            },
        }
        attributions = {
            "schemaVersion": 1,
            "reviewId": "model-assisted",
            "groupLabels": {"mixed": {"status": "mixed", "participantId": None}},
            "utteranceOverrides": overrides,
            "verification": {
                "p1": {"status": "confirmed", "sampleUtteranceIds": ["model-1"]},
                "p2": {"status": "confirmed", "sampleUtteranceIds": ["model-5"]},
            },
            "modelAttribution": {"modelOverrideUtteranceIds": model_ids},
        }
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "review.json"
            attributions_path = root / "attributions.json"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            attributions_path.write_text(json.dumps(attributions), encoding="utf-8")
            output_review, output_attributions, summary = (
                MODULE.materialize_scribe_fallback_layer(
                    review=review,
                    attributions=attributions,
                    review_id="scribe-fallback",
                    review_path=review_path,
                    attributions_path=attributions_path,
                    minimum_accuracy=0.8,
                )
            )
        self.assertEqual(output_review["reviewId"], "scribe-fallback")
        self.assertEqual(output_attributions["groupLabels"], {})
        self.assertEqual(
            output_attributions["utteranceOverrides"]["short-accepted"][
                "participantId"
            ],
            "p1",
        )
        self.assertNotIn(
            "short-rejected", output_attributions["utteranceOverrides"]
        )
        self.assertEqual(summary["acceptedScribeIdCount"], 1)
        self.assertEqual(summary["shortCueFallbackCount"], 1)
        self.assertEqual(summary["unresolvedCueCount"], 1)
        self.assertEqual(
            output_attributions["verification"], attributions["verification"]
        )

    def test_materialize_preserves_manual_and_short_cues(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        review, attributions = self.fixtures()
        embeddings = {
            "p1-g1": np.array([1.0, 0.0]),
            "p1-g2": np.array([0.9, 0.1]),
            "p2-g1": np.array([0.0, 1.0]),
            "p2-g2": np.array([0.1, 0.9]),
            "target": np.array([0.05, 0.95]),
            "manual": np.array([1.0, 0.0]),
            "excluded": np.array([0.05, 0.95]),
        }
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "review.json"
            attribution_path = root / "attributions.json"
            embedding_path = root / "embeddings.npz"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            attribution_path.write_text(json.dumps(attributions), encoding="utf-8")
            np.savez(
                embedding_path,
                ids=np.array(list(embeddings)),
                embeddings=np.vstack(list(embeddings.values())),
            )
            output_review, output_attributions, summary = MODULE.materialize_model_layer(
                np=np,
                review=review,
                attributions=attributions,
                review_id="derived",
                review_path=review_path,
                attributions_path=attribution_path,
                embeddings_path=embedding_path,
                embedding_dimension=2,
                embedding_by_id=embeddings,
                model_name="test-model",
                minimum_duration_seconds=1.5,
                minimum_word_count=4,
                excluded_ids={"excluded"},
                allow_unresolved_verification=True,
            )
        self.assertEqual(
            output_attributions["utteranceOverrides"]["target"]["participantId"],
            "p2",
        )
        self.assertEqual(
            output_attributions["utteranceOverrides"]["manual"]["participantId"],
            "p1",
        )
        self.assertNotIn("short", output_attributions["utteranceOverrides"])
        self.assertNotIn("excluded", output_attributions["utteranceOverrides"])
        self.assertTrue(output_review["verification"]["allowUnresolved"])
        self.assertEqual(summary["modelOverrideCount"], 5)
        self.assertEqual(summary["manualOverrideCountPreserved"], 1)
        self.assertEqual(summary["shortCueCountPreserved"], 1)
        self.assertEqual(summary["explicitExclusionCountPreserved"], 1)

    def test_reference_selection_uses_only_current_confirmed_assignments(self) -> None:
        review, attributions = self.fixtures()
        attributions["verification"] = {
            "p1": {
                "status": "confirmed",
                "sampleUtteranceIds": ["p1-g1", "p1-g2", "manual"],
            },
            "p2": {
                "status": "confirmed",
                "sampleUtteranceIds": ["p2-g1", "p2-g2", "target"],
            },
        }
        attributions["utteranceOverrides"]["target"] = {
            "status": "assigned",
            "participantId": "p2",
        }
        selected = MODULE.select_verified_reference_samples(review, attributions, 2)
        by_participant: dict[str, list[str]] = {}
        for item in selected:
            by_participant.setdefault(item["participant"]["id"], []).append(
                item["utterance"]["id"]
            )
        self.assertEqual(len(by_participant["p1"]), 2)
        self.assertEqual(len(by_participant["p2"]), 2)

    def test_reference_bank_matches_current_participants_by_name_not_old_id(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        review, _attributions = self.fixtures()
        manifest = {
            "schemaVersion": 1,
            "clips": [
                {
                    "participantId": "old-p99",
                    "name": "One",
                    "gameRole": "One",
                    "utteranceId": "old-one",
                    "clipSha256": "hash-one",
                },
                {
                    "participantId": "old-p01",
                    "name": "Two",
                    "gameRole": "Old Role",
                    "utteranceId": "old-two",
                    "clipSha256": "hash-two",
                },
            ],
        }
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            manifest_path = root / "reference-bank.json"
            embeddings_path = root / "reference.npz"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            embeddings_path.write_bytes(b"embedding-cache")
            references, metadata = MODULE.build_reference_bank_references(
                review=review,
                manifest=manifest,
                embedding_by_id={
                    "hash-one": np.array([1.0, 0.0]),
                    "hash-two": np.array([0.0, 1.0]),
                },
                manifest_path=manifest_path,
                embeddings_path=embeddings_path,
            )
        by_utterance = {item["utteranceId"]: item["participantId"] for item in references}
        self.assertEqual(by_utterance, {"old-one": "p1", "old-two": "p2"})
        self.assertEqual(metadata["roleMismatches"][0]["name"], "Two")

    @staticmethod
    def fixtures() -> tuple[dict, dict]:
        participants = [
            {"id": "p1", "name": "One", "gameRole": "One", "display": "One / One"},
            {"id": "p2", "name": "Two", "gameRole": "Two", "display": "Two / Two"},
        ]
        utterances = []
        groups = []
        group_rows = [
            ("g1", "p1-g1", 0.0),
            ("g2", "p1-g2", 10.0),
            ("h1", "p2-g1", 20.0),
            ("h2", "p2-g2", 30.0),
            ("t1", "target", 40.0),
            ("m1", "manual", 50.0),
            ("e1", "excluded", 60.0),
        ]
        for group_id, utterance_id, start in group_rows:
            groups.append(
                {
                    "id": group_id,
                    "recordingId": "r1",
                    "memberUtteranceIds": [utterance_id],
                    "representativeUtteranceIds": [utterance_id],
                }
            )
            utterances.append(
                {
                    "id": utterance_id,
                    "recordingId": "r1",
                    "groupId": group_id,
                    "start": start,
                    "end": start + 2.0,
                    "durationSeconds": 2.0,
                    "wordCount": 5,
                    "text": utterance_id,
                    "scribeSpeakerIds": ["speaker_0"],
                }
            )
        utterances.append(
            {
                "id": "short",
                "recordingId": "r1",
                "groupId": "t1",
                "start": 70.0,
                "end": 70.5,
                "durationSeconds": 0.5,
                "wordCount": 1,
                "text": "short",
                "scribeSpeakerIds": ["speaker_0"],
            }
        )
        next(item for item in groups if item["id"] == "t1")[
            "memberUtteranceIds"
        ].append("short")
        review = {
            "schemaVersion": 1,
            "reviewId": "source",
            "participants": participants,
            "recordings": [{"id": "r1", "audioPath": "/tmp/audio.m4a"}],
            "groups": groups,
            "utterances": utterances,
            "exceptions": {"unclusteredUtteranceIds": []},
            "verification": {"samplesPerParticipant": 10},
        }
        attributions = {
            "schemaVersion": 1,
            "reviewId": "source",
            "updatedAt": None,
            "groupLabels": {
                "g1": {"status": "assigned", "participantId": "p1"},
                "g2": {"status": "assigned", "participantId": "p1"},
                "h1": {"status": "assigned", "participantId": "p2"},
                "h2": {"status": "assigned", "participantId": "p2"},
                "t1": {"status": "assigned", "participantId": "p1"},
                "m1": {"status": "assigned", "participantId": "p2"},
                "e1": {"status": "assigned", "participantId": "p1"},
            },
            "utteranceOverrides": {
                "manual": {"status": "assigned", "participantId": "p1"}
            },
            "verification": {},
        }
        return review, attributions


if __name__ == "__main__":
    unittest.main()
