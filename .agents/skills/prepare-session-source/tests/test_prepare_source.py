from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
import unittest
import yaml
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(SKILL_ROOT / "scripts"))

from prepare_source import (  # noqa: E402
    SOURCE_TYPE_NARRATIVE,
    SOURCE_TYPE_TRANSCRIPT,
    build_bundle_stem,
    infer_source_audio_path,
    resolve_source_audio_path,
)


class PrepareSourceTest(unittest.TestCase):
    def test_decimal_session_number_keeps_fraction_in_bundle_name(self) -> None:
        self.assertEqual(
            build_bundle_stem(
                "Cleenseau", "12.1", scope="session", source_path=Path("email.md")
            ),
            "cleenseau-012.1",
        )
        self.assertEqual(
            build_bundle_stem(
                "Cleenseau", "12.10", scope="session", source_path=Path("email.md")
            ),
            "cleenseau-012.10",
        )

    def test_whole_session_number_keeps_existing_bundle_name(self) -> None:
        self.assertEqual(
            build_bundle_stem(
                "Cleenseau", 12, scope="session", source_path=Path("email.md")
            ),
            "cleenseau-012",
        )

    def test_malformed_session_number_is_rejected(self) -> None:
        with self.assertRaisesRegex(SystemExit, "whole or x.y number"):
            build_bundle_stem(
                "Cleenseau", "12.1.2", scope="session", source_path=Path("email.md")
            )

    def test_prepares_decimal_session_bundle(self) -> None:
        workspace = self.make_workspace()
        source_path = workspace / "email.md"
        source_path.write_text("First turn.\n\nSecond turn.\n", encoding="utf-8")
        participants_path = workspace / "participants.yaml"
        participants_path.write_text(
            "participants:\n- name: Mike Sackton\n  gameRole: DM\n", encoding="utf-8"
        )
        config_path = workspace / "source-prep.yaml"
        config_path.write_text(
            f"sourcePath: {source_path.as_posix()}\n"
            "sourceType: narrative\n"
            f"outputDir: {workspace.as_posix()}\n"
            "campaign: Cleenseau\n"
            "sessionNumber: '12.1'\n"
            "realWorldDate: '2024-02-16'\n"
            "drStart: '1749-09-16'\n"
            "drEnd: null\n"
            f"participantsPath: {participants_path.as_posix()}\n"
            "narrativeUnit: paragraph\n",
            encoding="utf-8",
        )

        result = subprocess.run(
            [sys.executable, str(SKILL_ROOT / "scripts" / "prepare_source.py"),
             "--config", str(config_path)],
            capture_output=True, text=True, check=False,
        )

        self.assertEqual(result.returncode, 0, result.stderr)
        cleaned = workspace / "cleenseau-012.1" / "cleaned"
        self.assertTrue((cleaned / "cleenseau-012.1-session.yaml").exists())
        manifest = yaml.safe_load((cleaned / "cleenseau-012.1-session.yaml").read_text())
        self.assertEqual(manifest["drStart"], "1749-09-16")
        self.assertIsNone(manifest["drEnd"])
        self.assertIn(
            "[u0002] Second turn.",
            (cleaned / "cleenseau-012.1-source-prepared.md").read_text(encoding="utf-8"),
        )

    def make_workspace(self) -> Path:
        tmpdir = Path(tempfile.mkdtemp(prefix="prepare-source-test."))
        self.addCleanup(lambda: shutil.rmtree(tmpdir, ignore_errors=True))
        return tmpdir

    def test_infers_source_audio_path_from_transcript_suffix(self) -> None:
        workspace = self.make_workspace()
        transcript_path = workspace / "GMT20260603-004350_Recording.transcript.vtt"
        audio_path = workspace / "GMT20260603-004350_Recording.m4a"
        transcript_path.write_text("WEBVTT\n", encoding="utf-8")
        audio_path.write_bytes(b"audio")

        self.assertEqual(infer_source_audio_path(transcript_path), audio_path.resolve())

    def test_infers_source_audio_path_from_matching_stem(self) -> None:
        workspace = self.make_workspace()
        transcript_path = workspace / "session-source.vtt"
        audio_path = workspace / "session-source.mp3"
        transcript_path.write_text("WEBVTT\n", encoding="utf-8")
        audio_path.write_bytes(b"audio")

        self.assertEqual(infer_source_audio_path(transcript_path), audio_path.resolve())

    def test_resolve_source_audio_path_uses_explicit_config_path(self) -> None:
        workspace = self.make_workspace()
        transcript_path = workspace / "session-source.vtt"
        audio_path = workspace / "recordings" / "session-audio.wav"
        audio_path.parent.mkdir()
        transcript_path.write_text("WEBVTT\n", encoding="utf-8")
        audio_path.write_bytes(b"audio")

        self.assertEqual(
            resolve_source_audio_path(
                source_path=transcript_path,
                configured_path=str(audio_path),
                source_type=SOURCE_TYPE_TRANSCRIPT,
            ),
            audio_path.resolve(),
        )

    def test_resolve_source_audio_path_skips_inference_for_non_transcripts(self) -> None:
        workspace = self.make_workspace()
        source_path = workspace / "session-notes.md"
        audio_path = workspace / "session-notes.m4a"
        source_path.write_text("Notes.\n", encoding="utf-8")
        audio_path.write_bytes(b"audio")

        self.assertIsNone(
            resolve_source_audio_path(
                source_path=source_path,
                configured_path=None,
                source_type=SOURCE_TYPE_NARRATIVE,
            )
        )


if __name__ == "__main__":
    unittest.main()
