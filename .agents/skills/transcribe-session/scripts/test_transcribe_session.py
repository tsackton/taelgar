#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock


SCRIPT_PATH = Path(__file__).with_name("transcribe_session.py")
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("transcribe_session", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


SAMPLE_RESPONSE = {
    "language_code": "eng",
    "language_probability": 0.99,
    "text": "Hello Kenzo. [laughs] Hello Delwath.",
    "transcription_id": "test-transcription",
    "audio_duration_secs": 4.0,
    "words": [
        {
            "text": "Hello",
            "start": 0.1,
            "end": 0.4,
            "type": "word",
            "speaker_id": "speaker_0",
        },
        {
            "text": " ",
            "start": 0.4,
            "end": 0.41,
            "type": "spacing",
            "speaker_id": "speaker_0",
        },
        {
            "text": "Kenzo.",
            "start": 0.41,
            "end": 0.8,
            "type": "word",
            "speaker_id": "speaker_0",
        },
        {
            "text": "[laughs]",
            "start": 1.0,
            "end": 1.2,
            "type": "audio_event",
            "speaker_id": "speaker_1",
        },
        {
            "text": " Hello",
            "start": 1.2,
            "end": 1.5,
            "type": "word",
            "speaker_id": "speaker_1",
        },
        {
            "text": " Delwath.",
            "start": 1.5,
            "end": 2.0,
            "type": "word",
            "speaker_id": "speaker_1",
        },
    ],
}


class TranscribeSessionTests(unittest.TestCase):
    def test_refuses_transcription_output_under_vault_sessions(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            audio_path = root / "Session-Test.m4a"
            participants_path = root / "participants.yaml"
            audio_path.write_bytes(b"not-empty")
            participants_path.write_text(
                "participants:\n- name: Tim Sackton\n  gameRole: DM\n",
                encoding="utf-8",
            )
            output_dir = root / "Taelgar" / "_sessions" / "campaign" / "session"
            result = MODULE.main(
                [
                    str(audio_path),
                    "--participants",
                    str(participants_path),
                    "--output-dir",
                    str(output_dir),
                    "--dry-run",
                ]
            )
        self.assertEqual(result, 2)
        self.assertFalse(output_dir.exists())

    def test_participants_create_player_parts_and_roles(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            path = Path(raw_dir) / "participants.yaml"
            path.write_text(
                "participants:\n"
                "- name: David Kong\n"
                "  gameRole: Kenzo\n"
                "- name: Mike Sackton\n"
                "  gameRole: Delwath\n",
                encoding="utf-8",
            )
            terms, count = MODULE.load_participant_terms(path)
        self.assertEqual(count, 2)
        self.assertEqual(
            terms,
            [
                "David Kong",
                "David",
                "Kong",
                "Kenzo",
                "Mike Sackton",
                "Mike",
                "Sackton",
                "Delwath",
            ],
        )

    def test_keyterms_are_validated_and_deduplicated(self) -> None:
        terms = MODULE.validate_keyterms(["Kenzo", " kenzo ", "Heartroot Vale"])
        self.assertEqual(terms, ["Kenzo", "Heartroot Vale"])
        with self.assertRaises(MODULE.TranscriptionError):
            MODULE.validate_keyterms(["one two three four five six"])

    def test_api_key_environment_precedes_legacy_env_file(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            env_file = Path(raw_dir) / ".env"
            env_file.write_text('ELEVEN_LABS_API="legacy-file-key"\n', encoding="utf-8")
            with mock.patch.dict(
                os.environ,
                {"ELEVENLABS_API_KEY": "standard-env-key", "ELEVEN_LABS_API": ""},
                clear=False,
            ):
                key, source = MODULE.resolve_api_key(env_file, required=True)
        self.assertEqual(key, "standard-env-key")
        self.assertEqual(source, "environment:ELEVENLABS_API_KEY")

    def test_curl_receives_api_key_on_stdin_not_in_process_arguments(self) -> None:
        completed = mock.Mock(returncode=0, stdout="200", stderr="")
        with mock.patch.object(MODULE.shutil, "which", return_value="/usr/bin/curl"), mock.patch.object(
            MODULE.subprocess, "run", return_value=completed
        ) as run_mock:
            status = MODULE.invoke_curl(
                api_key="test-secret-key",
                audio_path=Path("/tmp/Test Session.m4a"),
                response_path=Path("/tmp/response.json"),
                language_code="eng",
                num_speakers=5,
                keyterms=["Taelgar", "Kenzo"],
            )
        self.assertEqual(status, 200)
        command = run_mock.call_args.args[0]
        self.assertNotIn("test-secret-key", " ".join(command))
        self.assertIn("test-secret-key", run_mock.call_args.kwargs["input"])

    def test_curl_omits_num_speakers_for_auto_detection(self) -> None:
        completed = mock.Mock(returncode=0, stdout="200", stderr="")
        with mock.patch.object(MODULE.shutil, "which", return_value="/usr/bin/curl"), mock.patch.object(
            MODULE.subprocess, "run", return_value=completed
        ) as run_mock:
            status = MODULE.invoke_curl(
                api_key="test-secret-key",
                audio_path=Path("/tmp/Test Session.m4a"),
                response_path=Path("/tmp/response.json"),
                language_code="eng",
                num_speakers=None,
                keyterms=["Taelgar"],
            )
        self.assertEqual(status, 200)
        command = run_mock.call_args.args[0]
        self.assertFalse(any("num_speakers=" in value for value in command))

    def test_rendered_vtt_and_preview_preserve_speaker_turns(self) -> None:
        payload = MODULE.load_and_validate_response(self.write_response_fixture())
        turns = MODULE.build_turns(payload["words"])
        vtt = MODULE.render_vtt(turns)
        preview = MODULE.render_speaker_preview(turns, "test.m4a")
        self.assertIn("speaker_0: Hello Kenzo.", vtt)
        self.assertIn("speaker_1: [laughs] Hello Delwath.", vtt)
        self.assertIn("## speaker_0", preview)
        self.assertIn("## speaker_1", preview)

    def test_speaker_sample_selection_keeps_speakers_separate(self) -> None:
        turns = [
            MODULE.Turn("speaker_0", 10.0, 20.0, "one two three four five six seven"),
            MODULE.Turn("speaker_1", 30.0, 39.0, "alpha beta gamma delta epsilon zeta"),
        ]
        plans = MODULE.select_speaker_sample_plans(turns)
        self.assertEqual([plan.speaker for plan in plans], ["speaker_0", "speaker_1"])
        self.assertTrue(all(plan.end - plan.start <= MODULE.MAX_SAMPLE_SECONDS for plan in plans))

    def test_full_run_uses_mocked_upload_and_writes_no_api_key(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            audio = root / "Session-Test.m4a"
            audio.write_bytes(b"fake m4a data")
            participants = root / "participants.yaml"
            participants.write_text(
                "participants:\n"
                "- name: David Kong\n"
                "  gameRole: Kenzo\n"
                "- name: Mike Sackton\n"
                "  gameRole: Delwath\n",
                encoding="utf-8",
            )
            keyterms = root / "keyterms.txt"
            keyterms.write_text("Taelgar\nHeartroot Vale\n", encoding="utf-8")
            output_dir = root / "output"

            def fake_curl(**kwargs: object) -> int:
                self.assertEqual(kwargs["api_key"], "test-secret-key")
                Path(kwargs["response_path"]).write_text(
                    json.dumps(SAMPLE_RESPONSE), encoding="utf-8"
                )
                return 200

            def fake_extract(
                source: Path,
                output: Path,
                *,
                start_seconds: float,
                end_seconds: float,
                backend: object,
            ) -> None:
                self.assertGreater(end_seconds, start_seconds)
                output.write_bytes(b"fake audio sample")

            with mock.patch.dict(
                os.environ,
                {"ELEVENLABS_API_KEY": "test-secret-key", "ELEVEN_LABS_API": ""},
                clear=False,
            ), mock.patch.object(
                MODULE, "invoke_curl", side_effect=fake_curl
            ), mock.patch.object(
                MODULE,
                "resolve_clip_backend",
                return_value=MODULE.MediaBackend("fake", "/fake/media-tool"),
            ), mock.patch.object(
                MODULE, "extract_audio_clip", side_effect=fake_extract
            ):
                result = MODULE.main(
                    [
                        str(audio),
                        "--participants",
                        str(participants),
                        "--keyterms",
                        str(keyterms),
                        "--output-dir",
                        str(output_dir),
                        "--confirm-upload",
                    ]
                )

            self.assertEqual(result, 0)
            expected_files = [
                output_dir / "Session-Test.scribe-v2.json",
                output_dir / "Session-Test.transcript.vtt",
                output_dir / "Session-Test.transcription.json",
                output_dir / "Session-Test.speaker-preview.md",
            ]
            for path in expected_files:
                self.assertTrue(path.is_file(), path)
                self.assertNotIn("test-secret-key", path.read_text(encoding="utf-8"))

            samples_dir = output_dir / "Session-Test.speaker-samples"
            self.assertTrue(samples_dir.is_dir())
            self.assertEqual(len(list(samples_dir.glob("*.m4a"))), 2)

            manifest = json.loads(expected_files[2].read_text(encoding="utf-8"))
            self.assertEqual(manifest["request"]["model"], "scribe_v2")
            self.assertEqual(
                manifest["response"]["speakerIds"], ["speaker_0", "speaker_1"]
            )
            self.assertIn("Taelgar", manifest["request"]["keyterms"])
            self.assertEqual(len(manifest["outputs"]["speakerSamples"]), 2)

    def test_dry_run_requires_no_api_key_and_writes_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            audio = root / "Session-Test.m4a"
            audio.write_bytes(b"fake m4a data")
            participants = root / "participants.yaml"
            participants.write_text(
                "participants:\n- name: Tim Sackton\n  gameRole: DM\n",
                encoding="utf-8",
            )
            output_dir = root / "output"
            with mock.patch.dict(
                os.environ,
                {"ELEVENLABS_API_KEY": "", "ELEVEN_LABS_API": ""},
                clear=False,
            ), mock.patch.object(
                MODULE,
                "resolve_clip_backend",
                return_value=MODULE.MediaBackend("fake", "/fake/media-tool"),
            ):
                result = MODULE.main(
                    [
                        str(audio),
                        "--participants",
                        str(participants),
                        "--output-dir",
                        str(output_dir),
                        "--dry-run",
                    ]
                )
        self.assertEqual(result, 0)
        self.assertFalse(output_dir.exists())

    def test_auto_speakers_dry_run_records_automatic_detection(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            audio = root / "Session-Test.m4a"
            audio.write_bytes(b"fake m4a data")
            participants = root / "participants.yaml"
            participants.write_text(
                "participants:\n- name: Tim Sackton\n  gameRole: DM\n",
                encoding="utf-8",
            )
            output_dir = root / "output"
            with mock.patch.dict(
                os.environ,
                {"ELEVENLABS_API_KEY": "", "ELEVEN_LABS_API": ""},
                clear=False,
            ), mock.patch.object(
                MODULE,
                "resolve_clip_backend",
                return_value=MODULE.MediaBackend("fake", "/fake/media-tool"),
            ), mock.patch("sys.stdout", new_callable=lambda: __import__("io").StringIO()) as stdout:
                result = MODULE.main(
                    [
                        str(audio),
                        "--participants",
                        str(participants),
                        "--output-dir",
                        str(output_dir),
                        "--auto-speakers",
                        "--dry-run",
                    ]
                )
            plan = json.loads(stdout.getvalue())
        self.assertEqual(result, 0)
        self.assertIsNone(plan["numSpeakers"])
        self.assertEqual(plan["speakerDetection"], "automatic")
        self.assertFalse(output_dir.exists())

    def test_speaker_sample_preflight_failure_prevents_upload(self) -> None:
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            audio = root / "Session-Test.m4a"
            audio.write_bytes(b"fake m4a data")
            participants = root / "participants.yaml"
            participants.write_text(
                "participants:\n- name: Tim Sackton\n  gameRole: DM\n",
                encoding="utf-8",
            )
            with mock.patch.dict(
                os.environ,
                {"ELEVENLABS_API_KEY": "test-secret-key", "ELEVEN_LABS_API": ""},
                clear=False,
            ), mock.patch.object(
                MODULE,
                "resolve_clip_backend",
                return_value=MODULE.MediaBackend("fake", "/fake/media-tool"),
            ), mock.patch.object(
                MODULE,
                "extract_audio_clip",
                side_effect=MODULE.MediaToolError("unsupported source codec"),
            ), mock.patch.object(MODULE, "invoke_curl") as curl_mock:
                result = MODULE.main(
                    [
                        str(audio),
                        "--participants",
                        str(participants),
                        "--output-dir",
                        str(root / "output"),
                        "--confirm-upload",
                    ]
                )
        self.assertEqual(result, 2)
        curl_mock.assert_not_called()

    def write_response_fixture(self) -> Path:
        temporary = tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False)
        self.addCleanup(lambda: Path(temporary.name).unlink(missing_ok=True))
        json.dump(SAMPLE_RESPONSE, temporary)
        temporary.close()
        return Path(temporary.name)


if __name__ == "__main__":
    unittest.main()
