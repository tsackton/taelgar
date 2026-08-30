#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).with_name("media_tools.py")
SPEC = importlib.util.spec_from_file_location("media_tools_test_target", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class MediaToolsTests(unittest.TestCase):
    def test_afinfo_duration_is_parsed(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            source = Path(raw_dir) / "audio.m4a"
            source.write_bytes(b"audio")
            completed = mock.Mock(
                returncode=0,
                stdout="estimated duration: 1112.184 sec\n",
                stderr="",
            )
            with mock.patch.object(MODULE.subprocess, "run", return_value=completed):
                duration = MODULE.probe_duration(
                    source,
                    backend=MODULE.MediaBackend("afinfo", "/usr/bin/afinfo"),
                )
        self.assertEqual(duration, 1112.184)

    def test_swift_asset_reader_helper_is_compiled_locally(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            source = root / "audio.m4a"
            source.write_bytes(b"compressed audio")

            def fake_run(command: list[str], **kwargs: object) -> mock.Mock:
                output_index = command.index("-o") + 1
                Path(command[output_index]).write_bytes(b"compiled helper")
                return mock.Mock(returncode=0, stdout="", stderr="")

            with mock.patch.object(MODULE.subprocess, "run", side_effect=fake_run) as run_mock:
                prepared_source, prepared_backend = MODULE.prepare_clip_source(
                    source,
                    backend=MODULE.MediaBackend(
                        "swift-asset-reader-source", "/usr/bin/swiftc"
                    ),
                    work_dir=root,
                )
            command = run_mock.call_args.args[0]
            self.assertEqual(prepared_backend.name, "swift-asset-reader")
            self.assertEqual(prepared_source, source.resolve())
            self.assertIn("extract_audio_clip.swift", " ".join(command))
            self.assertTrue(Path(prepared_backend.executable).is_file())

    def test_prepared_asset_reader_extracts_clip(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            source = root / "audio.m4a"
            output = root / "clip.m4a"
            source.write_bytes(b"audio")

            def fake_run(command: list[str], **kwargs: object) -> mock.Mock:
                Path(command[2]).write_bytes(b"fake m4a clip")
                return mock.Mock(returncode=0, stdout="", stderr="")

            with mock.patch.object(MODULE.subprocess, "run", side_effect=fake_run) as run_mock:
                MODULE.extract_audio_clip(
                    source,
                    output,
                    start_seconds=2.0,
                    end_seconds=5.0,
                    backend=MODULE.MediaBackend(
                        "swift-asset-reader", "/tmp/extract-audio-clip"
                    ),
                )
            command = run_mock.call_args.args[0]
            self.assertEqual(command[1], str(source.resolve()))
            self.assertEqual(command[2], str(output.resolve()))
            self.assertEqual(command[3:], ["2.000", "3.000"])
            self.assertTrue(output.is_file())


if __name__ == "__main__":
    unittest.main()
