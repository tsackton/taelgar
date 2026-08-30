#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).with_name("speaker_review.py")
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("speaker_review", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SpeakerReviewTests(unittest.TestCase):
    def test_render_refuses_output_under_vault_sessions(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "test.speaker-review.json"
            labels_path = root / "test.speaker-attributions.json"
            output_path = root / "Taelgar" / "_sessions" / "test.vtt"
            review_path.write_text(json.dumps(self.review_fixture()), encoding="utf-8")
            labels_path.write_text(json.dumps(self.attribution_fixture()), encoding="utf-8")
            result = MODULE.main(
                [
                    "render",
                    str(review_path),
                    "--attributions",
                    str(labels_path),
                    "--output",
                    str(output_path),
                    "--allow-unresolved",
                ]
            )
        self.assertEqual(result, 2)
        self.assertFalse(output_path.exists())

    def test_utterances_split_without_relying_on_scribe_identity(self) -> None:
        items = [
            {"text": "First", "start": 0.0, "end": 0.4, "type": "word", "speaker_id": "speaker_0"},
            {"text": " sentence.", "start": 0.4, "end": 1.4, "type": "word", "speaker_id": "speaker_0"},
            {"text": "Different", "start": 1.45, "end": 2.0, "type": "word", "speaker_id": "speaker_0"},
            {"text": " person.", "start": 2.0, "end": 2.6, "type": "word", "speaker_id": "speaker_0"},
        ]
        utterances = MODULE.build_utterances(items, "r01")
        self.assertEqual(len(utterances), 2)
        self.assertEqual(utterances[0]["text"], "First sentence.")
        self.assertEqual(utterances[1]["text"], "Different person.")
        self.assertEqual(utterances[0]["scribeSpeakerIds"], ["speaker_0"])

    def test_kmeans_is_deterministic_and_separates_simple_groups(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        features = np.array(
            [[0.0, 0.0], [0.1, 0.0], [9.9, 10.0], [10.0, 10.1]], dtype=float
        )
        labels_one, _ = MODULE.kmeans(np, features, 2, seed=7)
        labels_two, _ = MODULE.kmeans(np, features, 2, seed=7)
        self.assertTrue(np.array_equal(labels_one, labels_two))
        self.assertEqual(labels_one[0], labels_one[1])
        self.assertEqual(labels_one[2], labels_one[3])
        self.assertNotEqual(labels_one[0], labels_one[2])

    def test_attributions_reject_unknown_groups(self) -> None:
        review = self.review_fixture()
        labels = self.attribution_fixture()
        labels["groupLabels"]["not-a-group"] = {
            "status": "assigned",
            "participantId": "p01",
        }
        with self.assertRaises(MODULE.SpeakerReviewError):
            MODULE.validate_attributions(review, labels)

    def test_attributions_reject_unknown_verification_samples(self) -> None:
        review = self.review_fixture()
        labels = self.attribution_fixture()
        labels["verification"]["p01"] = {
            "status": "confirmed",
            "sampleUtteranceIds": ["not-an-utterance"],
        }
        with self.assertRaises(MODULE.SpeakerReviewError):
            MODULE.validate_attributions(review, labels)

    def test_representative_selection_honors_requested_count(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        features = np.array([[0.0], [0.1], [0.2], [0.3]], dtype=float)
        feature_ids = [f"r01-u{index:05d}" for index in range(1, 5)]
        by_id = {
            utterance_id: {
                "start": index * 30.0,
                "durationSeconds": 2.0,
                "wordCount": 5,
            }
            for index, utterance_id in enumerate(feature_ids)
        }
        selected = MODULE.choose_representatives(
            np,
            features,
            np.array([0.15]),
            [0, 1, 2, 3],
            by_id,
            feature_ids,
            3,
        )
        self.assertEqual(len(selected), 3)

    def test_render_refuses_unresolved_pipeline_vtt(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "test.speaker-review.json"
            labels_path = root / "test.speaker-attributions.json"
            output_path = root / "test.vtt"
            review_path.write_text(json.dumps(self.review_fixture()), encoding="utf-8")
            labels_path.write_text(json.dumps(self.attribution_fixture()), encoding="utf-8")
            result = MODULE.main(
                [
                    "render",
                    str(review_path),
                    "--attributions",
                    str(labels_path),
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(result, 2)
            self.assertFalse(output_path.exists())

    def test_render_uses_confirmed_game_role(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "test.speaker-review.json"
            labels_path = root / "test.speaker-attributions.json"
            output_path = root / "test.vtt"
            review_path.write_text(json.dumps(self.review_fixture()), encoding="utf-8")
            labels = self.attribution_fixture()
            labels["groupLabels"]["r01-g001"] = {
                "status": "assigned",
                "participantId": "p01",
            }
            labels["verification"]["p01"] = {
                "status": "confirmed",
                "sampleUtteranceIds": ["r01-u00001"],
            }
            labels_path.write_text(json.dumps(labels), encoding="utf-8")
            result = MODULE.main(
                [
                    "render",
                    str(review_path),
                    "--attributions",
                    str(labels_path),
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(result, 0)
            self.assertIn("DM: Hello there.", output_path.read_text(encoding="utf-8"))

    def test_render_allows_optional_unclustered_unknown(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review = self.review_fixture()
            review["utterances"][0]["groupId"] = None
            review["groups"] = []
            review["exceptions"]["unclusteredUtteranceIds"] = ["r01-u00001"]
            review_path = root / "test.speaker-review.json"
            labels_path = root / "test.speaker-attributions.json"
            output_path = root / "test.vtt"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            labels_path.write_text(json.dumps(self.attribution_fixture()), encoding="utf-8")
            result = MODULE.main(
                [
                    "render",
                    str(review_path),
                    "--attributions",
                    str(labels_path),
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(result, 0)
            self.assertIn("Unknown: Hello there.", output_path.read_text(encoding="utf-8"))

    def test_render_treats_mixed_group_as_unknown_not_overlap(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "test.speaker-review.json"
            labels_path = root / "test.speaker-attributions.json"
            output_path = root / "test.vtt"
            review_path.write_text(json.dumps(self.review_fixture()), encoding="utf-8")
            labels = self.attribution_fixture()
            labels["groupLabels"]["r01-g001"] = {
                "status": "mixed",
                "participantId": None,
            }
            labels_path.write_text(json.dumps(labels), encoding="utf-8")
            result = MODULE.main(
                [
                    "render",
                    str(review_path),
                    "--attributions",
                    str(labels_path),
                    "--output",
                    str(output_path),
                    "--allow-unresolved",
                ]
            )
            self.assertEqual(result, 0)
            rendered = output_path.read_text(encoding="utf-8")
            self.assertIn("Unknown: Hello there.", rendered)
            self.assertNotIn("Overlap:", rendered)

    def test_render_requires_verification_for_assigned_participant(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "test.speaker-review.json"
            labels_path = root / "test.speaker-attributions.json"
            output_path = root / "test.vtt"
            review_path.write_text(json.dumps(self.review_fixture()), encoding="utf-8")
            labels = self.attribution_fixture()
            labels["groupLabels"]["r01-g001"] = {
                "status": "assigned",
                "participantId": "p01",
            }
            labels_path.write_text(json.dumps(labels), encoding="utf-8")
            result = MODULE.main(
                [
                    "render",
                    str(review_path),
                    "--attributions",
                    str(labels_path),
                    "--output",
                    str(output_path),
                ]
            )
            self.assertEqual(result, 2)
            self.assertFalse(output_path.exists())

    def test_refine_replaces_only_mixed_group_and_carries_assignments(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            audio_path = root / "test.m4a"
            audio_path.write_bytes(b"not-empty")
            review = self.review_fixture()
            review["recordings"][0]["audioPath"] = str(audio_path)
            review["groups"].append(
                {
                    "id": "r01-g002",
                    "recordingId": "r01",
                    "memberUtteranceIds": ["r01-u00002", "r01-u00003", "r01-u00004"],
                    "representativeUtteranceIds": ["r01-u00002"],
                    "utteranceCount": 3,
                    "speechSeconds": 3.0,
                    "scribeSpeakerIds": ["speaker_0", "speaker_1"],
                }
            )
            for index in range(2, 5):
                review["utterances"].append(
                    {
                        "id": f"r01-u{index:05d}",
                        "recordingId": "r01",
                        "start": float(index),
                        "end": float(index + 1),
                        "text": f"Example {index} words here.",
                        "wordCount": 4,
                        "durationSeconds": 1.0,
                        "scribeSpeakerIds": [f"speaker_{index % 2}"],
                        "groupId": "r01-g002",
                    }
                )
            review_path = root / "test.speaker-review.json"
            labels_path = root / "test.speaker-attributions.json"
            output_dir = root / "refined"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            labels = self.attribution_fixture()
            labels["groupLabels"] = {
                "r01-g001": {"status": "assigned", "participantId": "p01"},
                "r01-g002": {"status": "mixed", "participantId": None},
            }
            labels_path.write_text(json.dumps(labels), encoding="utf-8")

            def fake_decode(_audio_path, pcm_path, _decoder):
                pcm_path.write_bytes(b"\0\0" * 100)
                return 1.0, 16000

            def fake_features(_np, _samples, *, start, **_kwargs):
                return np.array([start, start % 2], dtype=float)

            with mock.patch.object(MODULE, "resolve_pcm_decoder", return_value=("ffmpeg", "/tmp/ffmpeg")), mock.patch.object(MODULE, "decode_to_pcm", side_effect=fake_decode), mock.patch.object(MODULE, "acoustic_feature_vector", side_effect=fake_features):
                result = MODULE.main(
                    [
                        "refine",
                        str(review_path),
                        "--attributions",
                        str(labels_path),
                        "--output-dir",
                        str(output_dir),
                        "--review-id",
                        "test-r2",
                        "--groups-per-parent",
                        "2",
                    ]
                )
            self.assertEqual(result, 0)
            refined = json.loads((output_dir / "test-r2.speaker-review.json").read_text())
            refined_labels = json.loads((output_dir / "test-r2.speaker-attributions.json").read_text())
            group_ids = {item["id"] for item in refined["groups"]}
            self.assertIn("r01-g001", group_ids)
            self.assertNotIn("r01-g002", group_ids)
            self.assertEqual(len([item for item in group_ids if item.startswith("r01-g002-r")]), 2)
            self.assertEqual(refined_labels["groupLabels"], {"r01-g001": {"status": "assigned", "participantId": "p01"}})

    @staticmethod
    def review_fixture() -> dict[str, object]:
        return {
            "schemaVersion": 1,
            "reviewId": "test",
            "participants": [
                {"id": "p01", "name": "Tim Sackton", "gameRole": "DM", "display": "Tim Sackton / DM"}
            ],
            "recordings": [{"id": "r01", "audioPath": "/tmp/test.m4a"}],
            "groups": [
                {
                    "id": "r01-g001",
                    "recordingId": "r01",
                    "memberUtteranceIds": ["r01-u00001"],
                    "representativeUtteranceIds": ["r01-u00001"],
                }
            ],
            "utterances": [
                {
                    "id": "r01-u00001",
                    "recordingId": "r01",
                    "start": 0.0,
                    "end": 1.0,
                    "text": "Hello there.",
                    "groupId": "r01-g001",
                }
            ],
            "exceptions": {"unclusteredUtteranceIds": []},
            "verification": {"samplesPerParticipant": 1},
        }

    @staticmethod
    def attribution_fixture() -> dict[str, object]:
        return {
            "schemaVersion": 1,
            "reviewId": "test",
            "updatedAt": None,
            "groupLabels": {},
            "utteranceOverrides": {},
            "verification": {},
        }


if __name__ == "__main__":
    unittest.main()
