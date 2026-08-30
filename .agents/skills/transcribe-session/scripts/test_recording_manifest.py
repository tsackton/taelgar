#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).with_name("recording_manifest.py")
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("recording_manifest", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class RecordingManifestTests(unittest.TestCase):
    def test_resolves_ordered_parts_and_alternate_alignment(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            for name in ("tim-01.m4a", "tim-02.m4a", "kong-01.m4a"):
                (root / name).write_bytes(name.encode("utf-8"))
            manifest = root / "session-recordings.yaml"
            manifest.write_text(
                "schemaVersion: 1\n"
                "campaign: Dunmar Frontier\n"
                "sessionNumber: 135\n"
                "tracks:\n"
                "- trackId: tim\n"
                "  role: primary\n"
                "  parts:\n"
                "  - sequence: 1\n"
                "    path: tim-01.m4a\n"
                "  - sequence: 2\n"
                "    path: tim-02.m4a\n"
                "    gapBeforeSeconds: 2\n"
                "- trackId: kong\n"
                "  role: alternate\n"
                "  alignment:\n"
                "    referenceTrackId: tim\n"
                "    offsetSeconds: 3.5\n"
                "  parts:\n"
                "  - sequence: 1\n"
                "    path: kong-01.m4a\n",
                encoding="utf-8",
            )

            durations = {
                "tim-01.m4a": 10.0,
                "tim-02.m4a": 20.0,
                "kong-01.m4a": 8.0,
            }
            with mock.patch.object(
                MODULE,
                "probe_duration",
                side_effect=lambda path, backend: durations[path.name],
            ):
                resolved = MODULE.resolve_manifest(
                    manifest,
                    probe_backend=MODULE.MediaBackend("fake", "/fake/probe"),
                )

        self.assertEqual(resolved["primaryTrackId"], "tim")
        tim_parts = resolved["tracks"][0]["parts"]
        self.assertEqual(tim_parts[0]["trackStartSeconds"], 0.0)
        self.assertEqual(tim_parts[1]["trackStartSeconds"], 12.0)
        self.assertEqual(tim_parts[1]["sessionStartSeconds"], 12.0)
        kong_part = resolved["tracks"][1]["parts"][0]
        self.assertEqual(kong_part["sessionStartSeconds"], 3.5)

    def test_unresolved_alternate_has_no_session_start(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            (root / "primary.m4a").write_bytes(b"one")
            (root / "alternate.m4a").write_bytes(b"two")
            manifest = root / "session-recordings.yaml"
            manifest.write_text(
                "schemaVersion: 1\n"
                "campaign: Test\n"
                "sessionNumber: 1\n"
                "tracks:\n"
                "- trackId: primary\n"
                "  role: primary\n"
                "  parts:\n"
                "  - sequence: 1\n"
                "    path: primary.m4a\n"
                "- trackId: alternate\n"
                "  role: alternate\n"
                "  parts:\n"
                "  - sequence: 1\n"
                "    path: alternate.m4a\n",
                encoding="utf-8",
            )
            with mock.patch.object(MODULE, "probe_duration", return_value=5.0):
                resolved = MODULE.resolve_manifest(
                    manifest,
                    probe_backend=MODULE.MediaBackend("fake", "/fake/probe"),
                )
        alternate = resolved["tracks"][1]
        self.assertEqual(alternate["alignment"]["referenceTrackId"], "primary")
        self.assertEqual(alternate["alignment"]["status"], "unresolved")
        self.assertIsNone(alternate["parts"][0]["sessionStartSeconds"])

    def test_rejects_nonconsecutive_sequences(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            (root / "audio.m4a").write_bytes(b"audio")
            manifest = root / "bad.yaml"
            manifest.write_text(
                "schemaVersion: 1\n"
                "campaign: Test\n"
                "sessionNumber: 1\n"
                "tracks:\n"
                "- trackId: test\n"
                "  role: candidate\n"
                "  parts:\n"
                "  - sequence: 2\n"
                "    path: audio.m4a\n",
                encoding="utf-8",
            )
            with self.assertRaises(MODULE.ManifestError):
                MODULE.resolve_manifest(
                    manifest,
                    probe_backend=MODULE.MediaBackend("fake", "/fake/probe"),
                )

    def test_candidate_offsets_without_primary_do_not_claim_session_time(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            (root / "a.m4a").write_bytes(b"a")
            (root / "b.m4a").write_bytes(b"b")
            manifest = root / "candidates.yaml"
            manifest.write_text(
                "schemaVersion: 1\n"
                "campaign: Test\n"
                "sessionNumber: 1\n"
                "tracks:\n"
                "- trackId: a\n"
                "  role: candidate\n"
                "  parts:\n"
                "  - sequence: 1\n"
                "    path: a.m4a\n"
                "- trackId: b\n"
                "  role: candidate\n"
                "  alignment:\n"
                "    referenceTrackId: a\n"
                "    offsetSeconds: 2\n"
                "  parts:\n"
                "  - sequence: 1\n"
                "    path: b.m4a\n",
                encoding="utf-8",
            )
            with mock.patch.object(MODULE, "probe_duration", return_value=5.0):
                resolved = MODULE.resolve_manifest(
                    manifest,
                    probe_backend=MODULE.MediaBackend("fake", "/fake/probe"),
                )
        self.assertIsNone(resolved["tracks"][1]["sessionOffsetSeconds"])
        self.assertIsNone(resolved["tracks"][1]["parts"][0]["sessionStartSeconds"])

    def test_rejects_unknown_fields(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            (root / "audio.m4a").write_bytes(b"audio")
            manifest = root / "typo.yaml"
            manifest.write_text(
                "schemaVersion: 1\n"
                "campaign: Test\n"
                "sessionNumber: 1\n"
                "tracks:\n"
                "- trackId: test\n"
                "  role: candidate\n"
                "  parts:\n"
                "  - sequence: 1\n"
                "    path: audio.m4a\n"
                "    gapBeforeSecond: 0\n",
                encoding="utf-8",
            )
            with self.assertRaisesRegex(MODULE.ManifestError, "unknown fields"):
                MODULE.resolve_manifest(
                    manifest,
                    probe_backend=MODULE.MediaBackend("fake", "/fake/probe"),
                )


if __name__ == "__main__":
    unittest.main()
