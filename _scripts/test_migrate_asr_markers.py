import contextlib
import hashlib
import io
import os
from pathlib import Path
import re
import tempfile
import unittest
from unittest import mock

import migrate_asr_markers as migration


class MarkerMigrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        self.folder = self.vault / "_sessions/dunmar-frontier/dunmari-frontier-001/cleaned"
        self.folder.mkdir(parents=True)
        self.path = self.folder / "dunmari-frontier-001-source-cleaned.md"

    def source(self, body, newline="\n"):
        text = "[u0001 | 00:00:00.000-00:00:01.000 | DM] " + body + newline
        self.path.write_bytes(text.encode())
        return self.path

    def plan(self, body, names=frozenset(), newline="\n"):
        return self.reviewed(self.source(body, newline), names)

    def reviewed(self, path, names=frozenset()):
        raw = path.read_bytes()
        confirmed = {(m.start(), m[0]) for m in re.finditer(r"\[\[.*?\]\]", raw.decode())
                     if m[0][2:-2].casefold() not in names}
        return migration.plan_file(self.vault, path, names, confirmed, hashlib.sha256(raw).hexdigest())

    def test_double_and_explicit_single(self):
        p = self.plan('Before [[wrong word]] and [unclear; possibly "name"].')
        self.assertIn(b'Before {{wrong word}} and {{unclear; possibly "name"}}.', p.proposed)
        self.assertEqual([e.kind for e in p.edits], ["double", "single"])

    def test_stage_directions_and_ordinary_brackets(self):
        p = self.plan("[laughs] [dice rolling] [2d6] [sic] [Coughs]")
        self.assertEqual(p.original, p.proposed)
        self.assertFalse(p.findings)

    def test_unknown_single_is_ambiguous(self):
        p = self.plan("[a proper noun]")
        self.assertEqual(p.original, p.proposed)
        self.assertEqual(p.findings[0]["kind"], "ambiguous-single")

    def test_explicit_wikilinks_and_markdown_links(self):
        body = "[[Note|alias]] [[#Heading]] [[folder/Note]] ![[Map.png]] [label](https://example.com)"
        p = self.plan(body)
        self.assertEqual(p.original, p.proposed)
        self.assertFalse(p.findings)

    def test_existing_note_name_is_ambiguous_not_replaced(self):
        p = self.plan("[[Existing Note]] and [[ASR phrase]]", {"existing note"})
        self.assertIn(b"[[Existing Note]] and {{ASR phrase}}", p.proposed)
        self.assertEqual(p.findings[0]["kind"], "possible-wikilink")
        with self.assertRaises(migration.Refused):
            migration.apply_plans(self.vault, [p])
        self.assertEqual(self.path.read_bytes(), p.original)

    def test_existing_curly_idempotence(self):
        p = self.plan("{{already unclear}} [[new error]]")
        self.path.write_bytes(p.proposed)
        second = migration.plan_file(self.vault, self.path, set())
        self.assertEqual(p.proposed, second.proposed)
        self.assertFalse(second.edits)

    def test_delimiters_only_preserves_unicode_crlf_and_headers(self):
        p = self.plan("Élan: [[strange—words]] [garbled] [laughs]", newline="\r\n")
        self.assertEqual(p.proposed, p.original.replace(b"[[strange\xe2\x80\x94words]]", b"{{strange\xe2\x80\x94words}}").replace(b"[garbled]", b"{{garbled}}"))
        self.assertTrue(p.proposed.endswith(b"\r\n"))

    def test_nested_and_unclosed_markers_refuse_entire_file(self):
        for body in ("[[good]] [[bad [nested]]]", "[[good]] [[unclosed", "[[good]] stray ]]", "{{bad [[nested]]}}"):
            with self.subTest(body=body):
                p = self.plan(body)
                self.assertEqual(p.original, p.proposed)
                self.assertFalse(p.edits)
                self.assertTrue(p.findings)
                with self.assertRaises(migration.Refused):
                    migration.apply_plans(self.vault, [p])

    def test_inline_code_and_escapes_preserved(self):
        p = self.plan(r"`[[code]]` \[literal\] [[actual ASR]]")
        self.assertIn(br"`[[code]]` \[literal\] {{actual ASR}}", p.proposed)

    def test_filename_and_path_exclusions(self):
        paths = [
            self.folder / "dunmari-frontier-001-source-prepared.md",
            self.folder / "cleanup-artifacts/dunmari-frontier-001-source-cleaned.md",
            self.folder / "dunmari-frontier-002-source-cleaned.md",
            self.folder / "dunmari-frontier-001-source-cleaned 2.md",
            self.folder / "beat-transcripts/dunmari-frontier-001-transcript-highlights.md",
            self.vault / "_sessions/proposed-deletions/dunmar-frontier/dunmari-frontier-001/cleaned/dunmari-frontier-001-source-cleaned.md",
            self.vault / "_sessions/dunmar-frontier/dunmari-frontier-001/cleaned/../cleaned/dunmari-frontier-001-source-cleaned.md",
        ]
        for path in paths:
            with self.subTest(path=path), self.assertRaises(migration.Refused):
                migration.target_kind(self.vault, path)

    def test_narrative_and_malformed_source_format(self):
        for text in ("[u0001 | source] Narrative [[link]]\n", "# Not a transcript\n", "[u0002 | 00:00:00.000-00:00:01.000 | DM] text\n", "[u0001 | 00:61:00.000-00:62:00.000 | DM] text\n"):
            self.path.write_text(text)
            with self.subTest(text=text), self.assertRaises(migration.Refused):
                migration.plan_file(self.vault, self.path, set())

    def test_symlink_file_and_parent_refused(self):
        self.source("[[error]]")
        link = self.folder / "link.md"
        link.symlink_to(self.path)
        with self.assertRaises(migration.Refused):
            migration.safe_path(self.vault, link)
        parent = self.vault / "linked"
        parent.symlink_to(self.folder, target_is_directory=True)
        with self.assertRaises(migration.Refused):
            migration.safe_path(self.vault, parent / self.path.name)

    def beat(self, coverage="%% u0001-u0002 %%"):
        path = self.folder / "beat-transcripts/dunmari-frontier-001-recap-001-transcript.md"
        path.parent.mkdir(exist_ok=True)
        path.write_text("# recap-001 | Title\n\n- Recap Block: recap-001\n- Beat IDs: B01\n- Source Range: u0001 -> u0002\n- Source Transcript: ../dunmari-frontier-001-source-cleaned.md\n\n## Transcript\n\n" + coverage + "\nDM: [[uncertain phrase]] [laughs]\n")
        return path

    def test_beat_format_and_provenance_preserved(self):
        p = self.reviewed(self.beat())
        self.assertIn(b"%% u0001-u0002 %%\nDM: {{uncertain phrase}} [laughs]", p.proposed)
        self.assertEqual(p.original.split(b"DM: ")[0], p.proposed.split(b"DM: ")[0])

    def test_beat_missing_or_duplicate_uid_coverage(self):
        with self.assertRaises(migration.Refused):
            migration.plan_file(self.vault, self.beat("%% u0001 %%"), set())

    def test_beat_extra_blank_separator_is_preserved(self):
        path = self.beat()
        path.write_bytes(path.read_bytes().replace(b"\n\n## Transcript", b"\n\n\n## Transcript"))
        p = self.reviewed(path)
        self.assertIn(b"\n\n\n## Transcript", p.proposed)

    def test_hardlink_refused(self):
        self.source("[[old]]")
        os.link(self.path, self.folder / "unrelated.md")
        with self.assertRaises(migration.Refused):
            migration.plan_file(self.vault, self.path, set())

    def test_missing_final_newline_preserved(self):
        p = self.plan("[[old]]", newline="")
        self.assertTrue(p.proposed.endswith(b"{{old}}"))
        self.assertFalse(p.proposed.endswith(b"\n"))

    def test_no_content_change_edit_validation(self):
        with self.assertRaises(migration.Refused):
            migration.render("[[old]]", [migration.Edit(0, 7, "[[old]]", "{{new}}", "double")])

    def test_apply_refuses_concurrent_edit(self):
        p = self.plan("[[old]]")
        self.source("a concurrent user edit")
        with self.assertRaises(migration.Refused):
            migration.apply_plans(self.vault, [p])
        self.assertIn(b"concurrent user edit", self.path.read_bytes())

    def test_apply_writes_only_selected_allowlisted_file(self):
        p = self.plan("[[old]] [garbled] [laughs]")
        unrelated = self.folder / "dunmari-frontier-001-source-prepared.md"
        unrelated.write_bytes(p.original)
        migration.apply_plans(self.vault, [p])
        self.assertEqual(self.path.read_bytes(), p.proposed)
        self.assertEqual(unrelated.read_bytes(), p.original)

    def test_unsupported_second_plan_prevents_all_writes(self):
        p = self.plan("[[old]]")
        unrelated = self.folder / "dunmari-frontier-001-source-prepared.md"
        unrelated.write_bytes(p.original)
        bad = migration.Plan(unrelated, p.original, p.proposed)
        with self.assertRaises(migration.Refused):
            migration.apply_plans(self.vault, [p, bad])
        self.assertEqual(self.path.read_bytes(), p.original)
        self.assertEqual(unrelated.read_bytes(), p.original)

    def test_cli_default_dry_run_does_not_write(self):
        self.source("[[uncertain]]")
        before = self.path.read_bytes()
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(migration.main(["--vault", str(self.vault)]), 0)
        self.assertEqual(before, self.path.read_bytes())

    def test_unconfirmed_bare_double_link_is_not_assumed_asr(self):
        self.source("[[Uncreated genuine note]]")
        p = migration.plan_file(self.vault, self.path, set())
        self.assertEqual(p.original, p.proposed)
        self.assertEqual(p.findings[0]["kind"], "unconfirmed-double")

    def test_transcript_note_targets_are_in_note_catalog(self):
        self.source("[[dunmari-frontier-030-source-cleaned]]")
        target = self.folder / "dunmari-frontier-030-source-cleaned.md"
        target.write_text("Existing note target")
        names = migration.note_names(self.vault)
        self.assertIn(target.stem, names)
        p = migration.plan_file(self.vault, self.path, names)
        self.assertEqual(p.original, p.proposed)
        self.assertEqual(p.findings[0]["kind"], "possible-wikilink")

    def test_multiple_backtick_code_spans_are_protected(self):
        for code in ("`` `literal` [[code]] ``", "``` [[code]] `` still code ```"):
            p = self.plan(code + " [[actual]]")
            self.assertIn(code.encode(), p.proposed)
            self.assertTrue(p.proposed.endswith(b"{{actual}}\n"))
            self.assertEqual(len(p.edits), 1)

    def test_markdown_link_destinations_and_titles_are_protected(self):
        body = '[label](https://example.com/[[code]] "[unclear] title") [[actual]]'
        p = self.plan(body)
        self.assertIn(b'[label](https://example.com/[[code]] "[unclear] title")', p.proposed)
        self.assertTrue(p.proposed.endswith(b"{{actual}}\n"))
        self.assertEqual(len(p.edits), 1)

    def test_asr_followed_by_colon_is_not_a_link_definition(self):
        p = self.plan("[[Speaker]]: [[other]]")
        self.assertTrue(p.proposed.endswith(b"{{Speaker}}: {{other}}\n"))
        self.assertEqual(len(p.edits), 2)

    def test_adjacent_asr_spans_are_not_reference_links(self):
        p = self.plan("[[first]][[second]]")
        self.assertTrue(p.proposed.endswith(b"{{first}}{{second}}\n"))

    def test_apostrophe_in_markdown_destination_is_protected(self):
        p = self.plan("[label](https://example.com/o'brien/[[code]]) [[actual]]")
        self.assertIn(b"o'brien/[[code]]", p.proposed)
        self.assertEqual(len(p.edits), 1)

    def test_stale_confirmation_refused(self):
        self.source("[[old]]")
        text = self.path.read_text()
        with self.assertRaises(migration.Refused):
            migration.plan_file(self.vault, self.path, set(), {(text.index("[["), "[[old]]")}, "0" * 64)

    def test_parent_symlink_replacement_detected_after_fd_open(self):
        self.source("[[old]]")
        elsewhere = self.vault / "elsewhere"
        elsewhere.mkdir()
        outside = elsewhere / self.path.name
        outside.write_bytes(b"Do not change this file")
        with migration.opened_transcript(self.vault, self.path, writable=True) as (fd, anchors):
            self.folder.rename(self.folder.with_name("cleaned-before-race"))
            self.folder.symlink_to(elsewhere, target_is_directory=True)
            with self.assertRaises(migration.Refused):
                migration._check_anchors(self.vault, self.path, anchors, fd)
        self.assertEqual(outside.read_bytes(), b"Do not change this file")

    def test_observed_edit_after_apply_preflight_is_preserved(self):
        p = self.plan("[[old]]")
        original_open = migration.opened_transcript
        concurrent = b"A concurrent user update"
        @contextlib.contextmanager
        def racing_open(vault, path, writable=False):
            with original_open(vault, path, writable=writable) as result:
                if writable:
                    path.write_bytes(concurrent)
                yield result
        with mock.patch.object(migration, "opened_transcript", racing_open):
            with self.assertRaises(migration.Refused):
                migration.apply_plans(self.vault, [p])
        self.assertEqual(self.path.read_bytes(), concurrent)

    def test_reports_cannot_be_written_inside_repository(self):
        with self.assertRaises(migration.Refused):
            migration.temporary_output(str(self.folder / "report.json"), self.vault)


if __name__ == "__main__":
    unittest.main()
