import importlib.util
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('interaction_draft', Path(__file__).resolve().parents[1] / 'scripts/interaction_draft.py')
d = importlib.util.module_from_spec(spec)
spec.loader.exec_module(d)


class DraftTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'cleaned').mkdir()
        self.manifest = self.root / 'cleaned/demo-session.yaml'
        self.source = self.root / 'cleaned/demo-transcript.md'
        self.source.write_text('# Demo\n\n## Transcript\n\n'
            '%% u0001:0-10 %%\nDM: Grash attacks.\n\n'
            '%% u0002:0-5 %%\nPC: I roll.\n\n'
            '%% u0002:5-10 %%\nDM: Ten damage.\n\n'
            '%% u0003:0-40 %%\nDM: Grash says the gate opens tomorrow.\n\n'
            '%% u0004:0-10 %%\nPC: I roll again.\n\n', encoding='utf-8', newline='\n')
        self.manifest.write_text('sourceType: transcript\nrealWorldDate: 2020-10-02\n'
            'drStart: 1748-04-12\ndrEnd: 1748-04-12\ntranscriptProcessing:\n  artifacts:\n'
            '    polishedMarkdown:\n      path: cleaned/demo-transcript.md\n', encoding='utf-8', newline='\n')
        self.before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.bundle = d.load(self.manifest)

    def tearDown(self):
        self.assertTrue({p for p in self.root.rglob('*') if p.is_file()} <= set(self.before) | {self.bundle['draft']})

    def test_copy_snip_split_uid_restore(self):
        d.initialize(self.bundle)
        d.snip(self.bundle, 2, 3, 'dice rolls')
        self.assertEqual(d.stats(self.bundle)['sourceUids'], 4)
        self.assertIn('u0002:0-5, u0002:5-10', self.bundle['draft'].read_text(encoding='utf-8'))
        d.restore(self.bundle, 2)
        self.assertEqual(d.stats(self.bundle)['snips'], 0)
        for p, data in self.before.items():
            self.assertEqual(p.read_bytes(), data)

    def test_combat_preserves_dialogue_and_restores_without_encounter_state(self):
        d.initialize(self.bundle)
        d.snip(self.bundle, 1, 3, 'Combat against Grash.', ['Grash'])
        d.snip(self.bundle, 5, 5, 'combat continues')
        _, blocks, snippets = d.inspect_draft(self.bundle)
        self.assertEqual(len(blocks), 3)
        self.assertEqual(len(snippets), 2)
        self.assertIn('gate opens tomorrow', self.bundle['draft'].read_text(encoding='utf-8'))
        # Either range can be restored independently; there is no encounter ledger.
        d.restore(self.bundle, 1)
        self.assertEqual(d.stats(self.bundle)['snips'], 1)
        self.assertIn(self.bundle['turns'][0]['raw'], self.bundle['draft'].read_text(encoding='utf-8'))
        self.assertIn('((combat continues))', self.bundle['draft'].read_text(encoding='utf-8'))

    def test_missing_dates_no_draft(self):
        for field in ('realWorldDate', 'drStart', 'drEnd'):
            self.manifest.write_text('\n'.join(s for s in self.before[self.manifest].decode().splitlines() if not s.startswith(field + ':')), encoding='utf-8', newline='\n')
            with self.assertRaisesRegex(d.DraftError, field):
                d.load(self.manifest)
        self.assertFalse(self.bundle['draft'].exists())

    def test_bad_dates(self):
        for end in ('1748-04-11', '1748-02-31'):
            self.manifest.write_text(self.before[self.manifest].decode().replace('drEnd: 1748-04-12', 'drEnd: ' + end), encoding='utf-8', newline='\n')
            with self.assertRaises(d.DraftError):
                d.load(self.manifest)

    def test_missing_path_no_guessing(self):
        self.manifest.write_text(self.manifest.read_text(encoding='utf-8').replace('cleaned/demo-transcript.md', 'missing.md'), encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(d.DraftError, 'cannot be located'):
            d.load(self.manifest)
        self.assertFalse(self.bundle['draft'].exists())

    def test_changed_source_is_rejected_but_yaml_can_be_updated(self):
        d.initialize(self.bundle)
        self.source.write_bytes(self.before[self.source] + b'\n')
        with self.assertRaisesRegex(d.DraftError, 'source or metadata changed'):
            d.inspect_draft(d.load(self.manifest))
        self.source.write_bytes(self.before[self.source])
        # Valid canonical date corrections do not make unchanged transcript work stale.
        self.manifest.write_text(self.manifest.read_text(encoding='utf-8').replace('drEnd: 1748-04-12', 'drEnd: 1748-04-13'), encoding='utf-8', newline='\n')
        d.inspect_draft(d.load(self.manifest))

    def test_source_changed_after_load(self):
        d.initialize(self.bundle)
        before = self.bundle['draft'].read_bytes()
        self.source.write_bytes(self.before[self.source] + b'\n')
        with self.assertRaisesRegex(d.DraftError, 'Input changed'):
            d.snip(self.bundle, 2, 3, 'dice rolls')
        self.assertEqual(before, self.bundle['draft'].read_bytes())

    def test_declared_hash(self):
        self.manifest.write_text(self.manifest.read_text(encoding='utf-8') + '      sha256: wrong\n', encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(d.DraftError, 'fingerprint'):
            d.load(self.manifest)

    def test_cleaned_reference_coverage(self):
        # A registered cleaned reference must agree with every UID's final offset.
        path = self.root / 'cleaned/demo-source-cleaned.md'
        path.write_text(''.join(f'[u{i:04d} | 0-1 | DM] ' + ('x' * n) + '\n' for i,n in [(1,10),(2,10),(3,40),(4,10)]), encoding='utf-8', newline='\n')
        self.before[path] = path.read_bytes()
        self.manifest.write_text(self.manifest.read_text(encoding='utf-8') + '    cleaned:\n      path: cleaned/demo-source-cleaned.md\n', encoding='utf-8', newline='\n')
        self.assertEqual(len(d.load(self.manifest)['coverage']),4)
        path.write_text(path.read_text(encoding='utf-8').replace('x' * 40, 'x' * 41), encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(d.DraftError,'completely cover'):
            d.load(self.manifest)

    def test_malformed_source_comment_not_silently_ignored(self):
        self.source.write_text(self.source.read_text(encoding='utf-8').replace('%% u0002:5-10 %%','%% u0002:five-ten %%'), encoding='utf-8', newline='\n')
        with self.assertRaises(d.DraftError):
            d.load(self.manifest)

    def test_existing_draft_preserved(self):
        d.initialize(self.bundle)
        before = self.bundle['draft'].read_bytes()
        with self.assertRaisesRegex(d.DraftError, 'already exists'):
            d.initialize(self.bundle)
        self.assertEqual(before, self.bundle['draft'].read_bytes())

    def test_symlink_escape_and_hardlink(self):
        self.bundle['draft'].symlink_to(self.source)
        with self.assertRaises(ValueError):
            d.load(self.manifest)
        self.bundle['draft'].unlink()
        d.initialize(self.bundle)
        import os
        with tempfile.TemporaryDirectory() as temp:
            os.link(self.bundle['draft'], Path(temp) / 'alias')
            before = self.bundle['draft'].read_bytes()
            with self.assertRaisesRegex(d.DraftError, 'hard link'):
                d.snip(self.bundle, 2, 3, 'dice rolls')
            self.assertEqual(before, self.bundle['draft'].read_bytes())
        self.manifest.write_text(self.manifest.read_text(encoding='utf-8').replace('cleaned/demo-transcript.md', '../outside.md'), encoding='utf-8', newline='\n')
        with self.assertRaises(ValueError):
            d.load(self.manifest)

    def test_unmarked_edits_and_missing_or_overlapping_spans(self):
        d.initialize(self.bundle)
        text = self.bundle['draft'].read_text(encoding='utf-8')
        for changed in (text.replace('gate opens tomorrow', 'gate is open'),
                        text.replace('u0002:5-10', 'u0002:6-10'),
                        text.replace('%% u0004:0-10 %%\nPC: I roll again.\n\n', ''),
                        text + 'Untracked words.\n'):
            with self.assertRaises(d.DraftError):
                d.inspect_draft(self.bundle, changed)

    def test_reassigned_span_partition(self):
        d.initialize(self.bundle)
        d.snip(self.bundle, 2, 3, 'dice rolls')
        text = self.bundle['draft'].read_text(encoding='utf-8').replace('u0002:0-5, u0002:5-10', 'u0002:0-10')
        with self.assertRaisesRegex(d.DraftError, 'source map'):
            d.inspect_draft(self.bundle, text)

    def test_names_and_short_single_sentence(self):
        d.initialize(self.bundle)
        for label, names in [('Combat against orcs.', ['Grash']), ('Combat against Zara.', ['Zara']),
                             ('Combat happens. Grash flees.', ['Grash']), ('word ' * 41, [])]:
            with self.assertRaises(d.DraftError):
                d.snip(self.bundle, 1, 3, label, names)
        self.assertEqual(d.stats(self.bundle)['snips'], 0)

    def test_minimal_metadata_and_no_snip_records(self):
        d.initialize(self.bundle)
        d.snip(self.bundle, 1, 3, 'Combat against Grash.', ['Grash'])
        meta, _, _ = d.inspect_draft(self.bundle)
        self.assertEqual(meta, {'version': 4, 'sessionYaml': 'cleaned/demo-session.yaml',
                                'sourceSha256': d.sha(self.source.read_bytes())})
        text = self.bundle['draft'].read_text(encoding='utf-8')
        self.assertNotIn('interactions-snip:', text)
        self.assertIn('%% u0001:0-10, u0002:0-5, u0002:5-10 %%\n((Combat against Grash.))', text)
        before = self.bundle['draft'].read_bytes()
        d.stats(self.bundle)
        self.assertEqual(before, self.bundle['draft'].read_bytes())

    def test_no_overlapping_snips(self):
        d.initialize(self.bundle)
        d.snip(self.bundle, 2, 3, 'dice rolls')
        with self.assertRaises(d.DraftError):
            d.snip(self.bundle, 1, 4, 'dice rolls')

    def test_metadata_tampering_and_old_format_rejected(self):
        d.initialize(self.bundle)
        text = self.bundle['draft'].read_text(encoding='utf-8')
        for changed in (text.replace('"version":4', '"version":3'),
                        text.replace('cleaned/demo-session.yaml', 'cleaned/other-session.yaml'),
                        text.replace(d.sha(self.source.read_bytes()), 'wrong'),
                        text.replace('"version":4', '"version":4,"review":true')):
            with self.assertRaises(d.DraftError):
                d.inspect_draft(self.bundle, changed)

    def mixed(self, speech='I rolled a 12. With my bonus that is 17. Grash says the gate opens tomorrow.'):
        self.source.write_text(self.source.read_text(encoding='utf-8').replace('Grash says the gate opens tomorrow.', speech), encoding='utf-8', newline='\n')
        self.before[self.source] = self.source.read_bytes()
        self.bundle = d.load(self.manifest)
        d.initialize(self.bundle)

    def test_inline_cut_preserves_lore_and_original_map(self):
        self.mixed()
        d.cut(self.bundle, 4, 'I rolled a 12. With my bonus that is 17.', 'rolls')
        text = self.bundle['draft'].read_text(encoding='utf-8')
        self.assertIn('%% u0003:0-40 %%\nDM: ((rolls)) Grash says the gate opens tomorrow.', text)
        self.assertNotIn('interactions-cuts', text)
        self.assertEqual(d.stats(self.bundle)['inlineSnips'], 1)
        self.assertEqual(d.stats(self.bundle)['sourceUids'], 4)
        for p, before in self.before.items():
            self.assertEqual(p.read_bytes(), before)

    def test_multiple_cuts_restore_whole_turn(self):
        self.mixed('Roll a 12. Grash speaks. I rolled a 17. The gate opens tomorrow.')
        d.cut(self.bundle, 4, 'I rolled a 17.', 'rolls')
        d.cut(self.bundle, 4, 'Roll a 12.', 'rolls')
        self.assertIn('DM: ((rolls)) Grash speaks. ((rolls)) The gate opens tomorrow.', self.bundle['draft'].read_text(encoding='utf-8'))
        d.restore(self.bundle, 4)
        self.assertEqual(d.stats(self.bundle)['inlineSnips'], 0)
        self.assertIn(self.bundle['turns'][3]['raw'], self.bundle['draft'].read_text(encoding='utf-8'))

    def test_restore_turn_does_not_restore_neighbor_sharing_uid(self):
        self.mixed('“Ésa?” I rolled a 12.\n\nGrash speaks.')
        d.cut(self.bundle, 4, 'I rolled a 12.', 'rolls')
        d.cut(self.bundle, 2, 'roll', 'rolls')
        d.cut(self.bundle, 3, 'Ten', 'damage')
        self.assertIn('“Ésa?” ((rolls))\n\nGrash speaks.', self.bundle['draft'].read_text(encoding='utf-8'))
        d.restore(self.bundle, 3)
        self.assertIn(self.bundle['turns'][2]['raw'], self.bundle['draft'].read_text(encoding='utf-8'))
        self.assertIn('%% u0002:0-5 %%\nPC: I ((rolls)).', self.bundle['draft'].read_text(encoding='utf-8'))
        self.assertEqual(d.stats(self.bundle)['inlineSnips'], 2)
        self.assertEqual(d.stats(self.bundle)['sourceUids'], 4)

    def test_inline_invalid_selection_has_no_effect(self):
        self.mixed()
        before = self.bundle['draft'].read_bytes()
        for text in ('not in the source', 'DM: ', 'roll', '12. With my bonus that is 17. Grash says the gate opens tomorrow.\n\n'):
            with self.assertRaises(d.DraftError):
                d.cut(self.bundle, 4, text, 'rolls')
            self.assertEqual(self.bundle['draft'].read_bytes(), before)
        with self.assertRaises(d.DraftError):
            d.cut(self.bundle, 4, self.bundle['turns'][3]['body'][4:].strip(), 'rolls')

    def test_inline_overlap_and_whole_turn_snip_guard(self):
        self.mixed()
        d.cut(self.bundle, 4, 'I rolled a 12.', 'rolls')
        before = self.bundle['draft'].read_bytes()
        for text in ('I rolled a 12.', '12', 'rolls', '((rolls))'):
            with self.assertRaises(d.DraftError):
                d.cut(self.bundle, 4, text, 'rolls')
        with self.assertRaisesRegex(d.DraftError, 'restore'):
            d.snip(self.bundle, 4, 4, 'rolls')
        self.assertEqual(self.bundle['draft'].read_bytes(), before)
        d.restore(self.bundle, 4)
        d.snip(self.bundle, 4, 4, 'rolls')
        with self.assertRaisesRegex(d.DraftError, 'whole-turn snip'):
            d.cut(self.bundle, 4, 'I rolled a 12.', 'rolls')

    def test_inline_repeated_text_uses_occurrence(self):
        self.mixed('Rolls. Grash speaks. Rolls. The gate opens tomorrow.')
        with self.assertRaisesRegex(d.DraftError, 'exactly once'):
            d.cut(self.bundle, 4, 'Rolls.', 'rolls')
        for occurrence in (0, 3, True):
            with self.assertRaises(d.DraftError):
                d.cut(self.bundle, 4, 'Rolls.', 'rolls', occurrence)
        d.cut(self.bundle, 4, 'Rolls.', 'rolls', occurrence=2)
        self.assertIn('DM: Rolls. Grash speaks. ((rolls)) The gate opens tomorrow.', self.bundle['draft'].read_text(encoding='utf-8'))
        d.cut(self.bundle, 4, 'Rolls.', 'rolls')
        self.assertEqual(d.stats(self.bundle)['inlineSnips'], 2)

    def test_inline_preserves_uncertainty_and_links(self):
        self.mixed('I rolled a 12. {{Grash?}} says to visit [[The Gate]].')
        for text in ('{{Grash?}}', 'Grash', 'The Gate', '[[The Gate]]'):
            with self.assertRaisesRegex(d.DraftError, 'overlaps an uncertainty'):
                d.cut(self.bundle, 4, text, 'chatter')

    def test_inline_unmarked_changes(self):
        self.mixed()
        d.cut(self.bundle, 4, 'I rolled a 12.', 'rolls')
        text = self.bundle['draft'].read_text(encoding='utf-8')
        for changed in (text.replace('gate opens tomorrow','gate opens today'),
                        text.replace('DM: ((rolls))','PC: ((rolls))'),
                        text.replace('((rolls))','(rolls)'),
                        text.replace('((rolls))','((rolls)'),
                        text.replace('((rolls))','((rolls)))')):
            with self.assertRaises(d.DraftError):
                d.inspect_draft(self.bundle, changed)

    def test_restore_multi_turn_snip_by_contained_turn(self):
        self.mixed()
        d.snip(self.bundle, 2, 3, 'rolls')
        self.assertIn('((rolls))', self.bundle['draft'].read_text(encoding='utf-8'))
        d.restore(self.bundle, 3)
        self.assertEqual(d.stats(self.bundle)['snips'], 0)
        for turn in self.bundle['turns']:
            self.assertIn(turn['raw'], self.bundle['draft'].read_text(encoding='utf-8'))

    def test_inline_labels_and_original_parentheses(self):
        self.mixed('I rolled a 12. Grash (the guard) speaks.')
        for label in ('rolls\nmore', '(rolls)', '', 'one two three four five six seven'):
            with self.assertRaises(d.DraftError):
                d.cut(self.bundle, 4, 'I rolled a 12.', label)
        d.cut(self.bundle, 4, 'I rolled a 12.', 'rolls')
        self.assertIn('Grash (the guard) speaks.', self.bundle['draft'].read_text(encoding='utf-8'))
        self.assertEqual(d.stats(self.bundle)['inlineSnips'], 1)

    def test_combined_uids_need_no_saved_turn_range(self):
        self.source.write_text(self.source.read_text(encoding='utf-8').replace(
            '%% u0003:0-40 %%', '%% u0003:0-40, u0004:0-5 %%').replace(
            '%% u0004:0-10 %%', '%% u0004:5-10 %%'), encoding='utf-8', newline='\n')
        self.bundle = d.load(self.manifest)
        d.initialize(self.bundle)
        d.snip(self.bundle, 4, 5, 'combat ends')
        _, _, snippets = d.inspect_draft(self.bundle)
        self.assertEqual((snippets[0]['startTurn'], snippets[0]['endTurn']), (4, 5))
        d.restore(self.bundle, 5)
        for turn in self.bundle['turns']:
            self.assertIn(turn['raw'], self.bundle['draft'].read_text(encoding='utf-8'))

    def test_reserved_syntax_in_source_fails_without_writes(self):
        self.source.write_text(self.source.read_text(encoding='utf-8').replace('Grash attacks.', 'Grash ((attacks)).'), encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(d.DraftError, 'reserved'):
            d.load(self.manifest)
        self.assertFalse(self.bundle['draft'].exists())


if __name__ == '__main__':
    unittest.main()
