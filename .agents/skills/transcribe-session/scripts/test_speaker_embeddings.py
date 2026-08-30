#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("speaker_embeddings.py")
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("speaker_embeddings", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SpeakerEmbeddingTests(unittest.TestCase):
    def test_review_plan_defaults_to_durable_cues(self) -> None:
        utterances = [
            {
                "id": "durable",
                "recordingId": "r1",
                "start": 1.0,
                "end": 3.0,
                "durationSeconds": 2.0,
                "wordCount": 5,
            },
            {
                "id": "short",
                "recordingId": "r1",
                "start": 4.0,
                "end": 4.8,
                "durationSeconds": 0.8,
                "wordCount": 2,
            },
        ]
        plan = MODULE.build_review_plan(
            utterances,
            minimum_duration_seconds=1.5,
            minimum_word_count=4,
        )
        self.assertEqual([item["id"] for item in plan], ["durable"])

    def test_reference_plan_uses_clip_hash_as_stable_id(self) -> None:
        manifest = {
            "schemaVersion": 1,
            "clips": [
                {"clipPath": "/tmp/one.m4a", "clipSha256": "abc"},
                {"clipPath": "/tmp/two.m4a", "clipSha256": "def"},
            ],
        }
        plan = MODULE.build_reference_plan(manifest)
        self.assertEqual([item["id"] for item in plan], ["abc", "def"])

    def test_cache_round_trip_preserves_resume_metadata(self) -> None:
        try:
            np = MODULE.load_numpy_for_cache()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        plan = [{"id": "u1"}, {"id": "u2"}]
        metadata = {
            "schemaVersion": 1,
            "sourceType": "speaker-review",
            "sourceSha256": "source",
            "modelName": "model",
            "modelSource": "/model",
            "plannedCount": 2,
            "createdAt": "created",
            "selection": {"minimumDurationSeconds": 1.5},
        }
        with tempfile.TemporaryDirectory() as raw_dir:
            path = Path(raw_dir) / "cache.npz"
            MODULE.write_cache(
                np,
                path,
                plan,
                {"u1": np.array([1.0, 0.0]), "u2": np.array([0.0, 1.0])},
                metadata,
                complete=True,
            )
            cached, restored = MODULE.load_cache_with_metadata(np, path)
        self.assertEqual(set(cached), {"u1", "u2"})
        self.assertTrue(restored["complete"])
        self.assertEqual(restored["completedCount"], 2)


if __name__ == "__main__":
    unittest.main()
