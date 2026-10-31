from __future__ import annotations

import importlib.util
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = SKILL_ROOT / "scripts" / "manage_beat_transcripts.py"
SPEC = importlib.util.spec_from_file_location("manage_beat_transcripts", SCRIPT_PATH)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"Could not import {SCRIPT_PATH}")
manager = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = manager
SPEC.loader.exec_module(manager)


class ManageBeatTranscriptsTest(unittest.TestCase):
    def make_workspace(self) -> Path:
        tmpdir = Path(tempfile.mkdtemp(prefix="manage-beat-transcripts-test."))
        self.addCleanup(lambda: shutil.rmtree(tmpdir, ignore_errors=True))
        return tmpdir

    def test_read_recap_blocks_uses_recap_markdown_metadata(self) -> None:
        workspace = self.make_workspace()
        recap_path = workspace / "session-recap.md"
        recap_path.write_text(
            "# Session Recap\n\n"
            "## Recap\n\n"
            "### recap-001 | Campfire Tales\n\n"
            "- Kind: beat\n"
            "- Beat IDs: B01, B02\n"
            "- Source Range: u0001 -> u0698\n"
            "- Polished Transcript: old/path.md\n\n"
            "#### Short\n"
            "The party camps in the woods.\n\n"
            "#### Long\n"
            "- Source Range: u9999 -> u9999\n\n"
            "### recap-003 | The Journey\n\n"
            "- Kind: beat\n"
            "- Beat IDs: B03\n"
            "- Source Range: u0699 -> u1415\n\n"
            "## Cast\n",
            encoding="utf-8",
        )

        blocks = manager.read_recap_blocks(recap_path)

        self.assertEqual([block["blockId"] for block in blocks], ["recap-001", "recap-003"])
        self.assertEqual(blocks[0]["title"], "Campfire Tales")
        self.assertEqual(blocks[0]["beatIds"], ["B01", "B02"])
        self.assertEqual(blocks[0]["startUid"], "u0001")
        self.assertEqual(blocks[0]["endUid"], "u0698")
        self.assertEqual(blocks[1]["beatIds"], ["B03"])
        self.assertEqual(blocks[1]["sourceEntries"][0]["title"], "The Journey")

    def test_main_ignores_missing_context_json(self) -> None:
        workspace = self.make_workspace()
        transcript_path = workspace / "source-cleaned.md"
        recap_path = workspace / "session-recap.md"
        output_dir = workspace / "beat-transcripts"
        transcript_path.write_text(
            "# Session\n\n- Status: Complete\n\n## Transcript\n\n"
            "%% u0001:0-15 %%\nDM: The door opens.\n\n"
            "%% u0002:0-20 %%\nKaito: What could go wrong?\n\n"
            "%% u0003:0-11 %%\nDM: Everything.\n",
            encoding="utf-8",
        )
        recap_path.write_text(
            "# Session Recap\n\n"
            "## Recap\n\n"
            "### recap-001 | Opening the Door\n\n"
            "- Kind: beat\n"
            "- Beat IDs: B01\n"
            "- Source Range: u0001 -> u0003\n\n"
            "#### Short\n"
            "The door opens.\n",
            encoding="utf-8",
        )

        old_argv = sys.argv
        try:
            sys.argv = [
                "manage_beat_transcripts.py",
                "--transcript",
                str(transcript_path),
                "--context-json",
                str(workspace / "missing-context.json"),
                "--session-recap-md",
                str(recap_path),
                "--output-dir",
                str(output_dir),
                "--file-prefix",
                "test-session-001",
            ]
            result = manager.main()
        finally:
            sys.argv = old_argv

        self.assertEqual(result, 0)
        transcript_file = output_dir / "test-session-001-recap-001-transcript.md"
        self.assertTrue(transcript_file.exists())
        self.assertIn("- Polished Transcript: beat-transcripts/test-session-001-recap-001-transcript.md", recap_path.read_text(encoding="utf-8"))
        self.assertIn("%% u0001:0-15 %%", transcript_file.read_text(encoding="utf-8"))

    def test_sync_recap_review_media_from_highlights_summary(self) -> None:
        workspace = self.make_workspace()
        recap_path = workspace / "session-recap.md"
        summary_path = workspace / "beat-transcripts" / "test-transcript-highlights.md"
        summary_path.parent.mkdir(parents=True)
        recap_path.write_text(
            "# Session Recap\n\n"
            "## Source Files\n\n"
            "- Cleaned Source: source.md\n",
            encoding="utf-8",
        )
        summary_path.write_text(
            "# Transcript Highlights\n\n"
            "## Pull Quotes\n\n"
            "### beat-001 | Arrival\n\n"
            "- Recap Block: recap-001\n"
            "- Transcript: test-recap-001-transcript.md\n"
            "- Source Range: u0001 -> u0010\n"
            "- Pull Quotes:\n"
            "  - ID: quote-beat-001-001\n"
            "    - Quote: \"The maze remembers.\"\n"
            "    - Speaker: Kalima\n"
            "    - Source Lines: u0004-u0006\n\n"
            "## Audio Monologue Candidates\n\n"
            "- ID: audio-001\n"
            "  - Source Lines: u0020-u0040\n"
            "  - Speaker: DM\n"
            "  - Summary: Holda tells his story.\n"
            "  - Why Called Out: Central exposition.\n",
            encoding="utf-8",
        )

        manager.sync_recap_review_media(recap_path, summary_path)

        recap_text = recap_path.read_text(encoding="utf-8")
        self.assertIn("## Pull Quotes", recap_text)
        self.assertIn("- ID: quote-beat-001-001", recap_text)
        self.assertIn("  - Quote: \"The maze remembers.\"", recap_text)
        self.assertIn("## Audio Highlights", recap_text)
        self.assertIn("- ID: audio-001", recap_text)
        self.assertIn("  - Title: Holda tells his story.", recap_text)
        self.assertIn("  - Output: audio-001.m4a", recap_text)
        self.assertIn("## Source Files", recap_text)

    def fixture(self, start='u0002', end='u0002'):
        root = self.make_workspace()
        source = root / 'polished.md'
        # Connected shared-UID turns require expansion beyond both recap edges.
        body = (
            '%% u0001:0-8, u0002:0-4 %%\nYezali: [[Place]]!\n\n'
            '%% u0002:4-10, u0003:0-6 %%\nRai: [garbled] {{perhaps}}\n\n'
            'A second paragraph.\n\n'
            '%% u0003:6-12 %%\nDM: [cross-talk]\n\n'
            '%% u0004:0-5 %%\nKenzo: After.\n\n'
        )
        source.write_text('# Session\n\n- Status: Complete with retained uncertainty\n\n## Transcript\n\n' + body)
        recap = root / 'recap.md'
        recap.write_text(f'# Recap\n\n## Recap\n\n### recap-001 | Arrival\n\n- Beat IDs: beat-001\n- Source Range: {start} -> {end}\n\n#### Short\nSummary.\n')
        output = root / 'beat-transcripts'
        args = ['manager', '--transcript', str(source), '--session-recap-md', str(recap),
                '--output-dir', str(output), '--file-prefix', 'example']
        return source, recap, output, args, body

    def run_helper(self, args, *options):
        with patch.object(sys, 'argv', args + list(options)), redirect_stdout(StringIO()) as out:
            result = manager.main()
        return result, out.getvalue()

    def test_extracts_exact_polished_shared_uid_turns_and_boundary_context(self):
        source, recap, output, args, body = self.fixture()
        before = source.read_bytes()
        result, log = self.run_helper(args)
        self.assertEqual(result, 0, log)
        excerpt = output / 'example-recap-001-transcript.md'
        text = excerpt.read_text()
        self.assertEqual(text.split('## Transcript\n\n', 1)[1], body.split('%% u0004:', 1)[0])
        self.assertIn('- Source Range: u0001 -> u0003', text)
        self.assertIn('- Recap Source Range: u0002 -> u0002', text)
        self.assertIn('whole-turn context', log)
        self.assertNotIn('unresolved [[', log)
        self.assertEqual(source.read_bytes(), before)
        snapshot = {p: p.read_bytes() for p in [source, recap, *output.iterdir()]}
        self.assertEqual(self.run_helper(args, '--validate-only')[0], 0)
        self.assertEqual(snapshot, {p: p.read_bytes() for p in snapshot})
        self.assertEqual(self.run_helper(args)[0], 0)
        self.assertEqual(snapshot, {p: p.read_bytes() for p in snapshot})

    def test_detects_changed_word_speaker_or_span_without_overwriting(self):
        for before, after in [('Yezali:', 'Oskar:'), ('[[Place]]!', 'A different place!'), ('u0002:4-10', 'u0002:5-10')]:
            with self.subTest(after=after):
                _, _, output, args, _ = self.fixture()
                self.assertEqual(self.run_helper(args)[0], 0)
                excerpt = output / 'example-recap-001-transcript.md'
                original = excerpt.read_text()
                edited = original.replace(before, after)
                excerpt.write_text(edited)
                self.assertEqual(self.run_helper(args, '--validate-only')[0], 1)
                self.assertEqual(self.run_helper(args)[0], 1)
                self.assertEqual(excerpt.read_text(), edited)
                self.assertEqual(self.run_helper(args, '--overwrite')[0], 0)
                self.assertEqual(excerpt.read_text(), original)

    def test_default_and_overwrite_preserve_reviewed_highlights_and_candidates(self):
        _, recap, output, args, _ = self.fixture()
        selected = ('\n## Pull Quotes\n\n- ID: custom-b\n  - Quote: "Edited"\n'
                    '  - Speaker: Rai\n  - Source Lines: u0002-u0002\n\n'
                    '- ID: custom-a\n  - Quote: "Reordered"\n\n'
                    '## Audio Highlights\n\n- ID: audio-009\n  - Title: My title\n'
                    '  - Output: personal.m4a\n\n%% keep my comment %%\n\n')
        recap.write_text(recap.read_text() + selected)
        self.assertEqual(self.run_helper(args)[0], 0)
        summary = output / 'example-transcript-highlights.md'
        candidates = summary.read_bytes()
        before = recap.read_bytes()
        for options in [(), ('--overwrite',), ('--seed-highlights',)]:
            self.assertEqual(self.run_helper(args, *options)[0], 0)
            self.assertEqual(recap.read_bytes(), before)
            self.assertEqual(summary.read_bytes(), candidates)

    def test_removed_or_empty_sections_are_not_restored_on_normal_rerun(self):
        for selected in ['', '\n## Pull Quotes\n\n## Audio Highlights\n\n']:
            with self.subTest(selected=selected):
                _, recap, output, args, _ = self.fixture()
                self.run_helper(args)
                summary = output / 'example-transcript-highlights.md'
                summary.write_text(summary.read_text().replace('TODO: Quote text.', 'A real quote.').replace('Speaker: TODO', 'Speaker: Rai').replace('Source Lines: TODO', 'Source Lines: u0002-u0002'))
                recap.write_text(recap.read_text() + selected)
                before = recap.read_bytes()
                self.assertEqual(self.run_helper(args, '--overwrite')[0], 0)
                self.assertEqual(recap.read_bytes(), before)
                if selected:
                    self.assertEqual(self.run_helper(args, '--seed-highlights')[0], 0)
                    self.assertEqual(recap.read_bytes(), before)

    def test_seeding_skips_unfinished_candidates(self):
        _, recap, _, args, _ = self.fixture()
        self.assertEqual(self.run_helper(args, '--seed-highlights')[0], 0)
        self.assertNotIn('## Pull Quotes', recap.read_text())
        self.assertNotIn('## Audio Highlights', recap.read_text())

    def test_rejects_raw_or_unfinished_or_broken_mapping_before_writes(self):
        for text in ['[u0001 | DM] Raw source.\n',
                     '# Draft\n- Status: Draft awaiting quality review\n%% u0002:0-4 %%\nDM: Test\n',
                     '# Done\n- Status: Complete\n%% u0002:0-4 %%\nDM: Test\n\n%% u0002:5-8 %%\nRai: More\n']:
            with self.subTest(text=text):
                source, recap, output, args, _ = self.fixture()
                source.write_text(text)
                original = recap.read_bytes()
                with self.assertRaises(SystemExit):
                    self.run_helper(args)
                self.assertFalse(output.exists())
                self.assertEqual(recap.read_bytes(), original)

    def test_late_single_block_keeps_prior_candidates_and_selections(self):
        _, recap, output, args, _ = self.fixture('u0004', 'u0004')
        self.assertEqual(self.run_helper(args)[0], 0)
        extra = '\n### recap-002 | Later\n\n- Beat IDs: beat-002\n- Source Range: u0001 -> u0003\n\n#### Short\nLater.\n'
        recap.write_text(recap.read_text() + extra)
        summary = output / 'example-transcript-highlights.md'
        before = summary.read_bytes()
        result, log = self.run_helper(args, '--recap-block-id', 'recap-002')
        # The candidate document is never regenerated; missing beat section is actionable.
        self.assertEqual(result, 1)
        self.assertIn('missing beat heading for beat-002', log)
        self.assertEqual(summary.read_bytes(), before)
        self.assertTrue((output / 'example-recap-002-transcript.md').exists())


if __name__ == "__main__":
    unittest.main()
