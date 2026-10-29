import copy
import importlib.util
import os
from pathlib import Path
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
spec = importlib.util.spec_from_file_location('scene_map', Path(__file__).resolve().parents[1] / 'scripts/scene_map.py')
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class SceneMapTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        self.root = self.vault / '_sessions/demo'
        (self.root / 'cleaned').mkdir(parents=True)
        self.yaml = self.root / 'cleaned/demo-session.yaml'
        self.source = self.root / 'cleaned/demo-transcript.md'
        self.source.write_text('# Demo\n\n'
            '%% u0001:0-10 %%\nDM: Last time Grash escaped.\n\n'
            '%% u0002:0-10, u0003:0-10 %%\nDM: Grash greets you at the gate.\n\n'
            '%% u0004:0-5 %%\nPC: I roll a 12.\n\n'
            '%% u0004:5-10 %%\nDM: He invites you inside.\n\n'
            '%% u0005:0-10 %%\nPC: We enter the hall.\n\n'
            '%% u0006:0-10 %%\nDM: Afterwards: the old king also used this hall.\n\n')
        self.yaml.write_text('sourceType: transcript\nrealWorldDate: 2020-10-02\n'
            'drStart: 1748-04-12\ndrEnd: 1748-04-14\ntranscriptProcessing:\n  artifacts:\n'
            '    polishedMarkdown:\n      path: cleaned/demo-transcript.md\n')
        self.bundle = self.load()
        self.originals = {p: p.read_bytes() for p in (self.yaml, self.source)}
        self.proposal = {
            'dateValidation': {'result': 'insufficientEvidence',
                               'reason': 'This recording supplies no usable calendar anchors.', 'evidence': []},
            'scenes': [
                {'index': 1, 'source': m.source('u0002', 'u0004'), 'type': 'conversation',
                 'aiSummary': 'Grash greets the party and invites them inside.'},
                {'index': 2, 'source': m.source('u0005', 'u0005'), 'type': 'exploration'}],
            'contextBlocks': [
                {'kind': 'recap', 'source': m.source('u0001', 'u0001'), 'aiSummary': 'Previous escape, recounted.'},
                {'kind': 'loreDiscussion', 'source': m.source('u0006', 'u0006'), 'aiSummary': 'Postgame historical clarification.'}]}

    def load(self):
        return m.load(self.yaml, self.vault)

    def document(self):
        return m.build(self.bundle, copy.deepcopy(self.proposal))

    def test_partition_and_minimal_scene(self):
        doc = self.document()
        result = m.validate(self.bundle, doc)
        self.assertEqual((result['sourceUids'], result['scenes'], result['contextBlocks']), (6, 2, 2))
        self.assertNotIn('realWorldDate', doc)
        self.assertNotIn('participants', doc)
        self.assertIn('not established', result['semanticReview'])
        del doc['scenes'][0]['type']
        del doc['scenes'][0]['aiSummary']
        m.validate(self.bundle, doc)

    def test_gaps_overlaps_and_omitted_context_fail(self):
        for mutate in (
            lambda d: d['contextBlocks'].pop(),
            lambda d: d['scenes'].pop(),
            lambda d: d['scenes'][1]['source'].update(startUid='u0004'),
            lambda d: d['contextBlocks'][0]['source'].update(endUid='u0003'),
        ):
            doc = self.document()
            mutate(doc)
            with self.assertRaises(m.MapError):
                m.validate(self.bundle, doc)

    def test_combined_uid_turn_is_indivisible(self):
        doc = self.document()
        doc['scenes'][0]['source']['startUid'] = 'u0003'
        with self.assertRaisesRegex(m.MapError, 'splits a polished turn'):
            m.validate(self.bundle, doc)

    def test_shared_uid_read_window_includes_both_turns(self):
        view = m.window(self.bundle, 'u0004', 'u0004')
        self.assertIn('I roll a 12.', view)
        self.assertIn('He invites you inside.', view)
        self.assertEqual(view.count('[u0004–u0004]'), 1)
        self.assertNotIn('We enter the hall', view)

    def test_read_window_expands_combined_uids(self):
        view = m.window(self.bundle, 'u0003', 'u0003')
        self.assertIn('[u0002–u0003]', view)
        self.assertIn('Grash greets', view)
        self.assertNotIn('Last time', view)

    def test_draft_reading_and_cross_boundary_snip_fallback(self):
        m.draft.initialize(self.bundle)
        m.draft.snip(self.bundle, 2, 5, 'combat against Grash', ['Grash'])
        view = m.window(self.bundle, 'u0002', 'u0005')
        self.assertIn('((combat against Grash))', view)
        self.assertIn('labels)) are generated', view)
        view = m.window(self.bundle, 'u0004', 'u0004')
        self.assertIn('showing polished source', view)
        self.assertIn('He invites you inside', view)
        self.assertNotIn('((combat against Grash))', view)

    def test_invalid_draft_fails_auto_but_polished_remains_available(self):
        m.draft.initialize(self.bundle)
        path = self.bundle['draft']
        path.write_text(path.read_text().replace('Grash greets', 'Grash attacks'))
        with self.assertRaises(ValueError):
            m.window(self.bundle)
        self.assertIn('Grash greets', m.window(self.bundle, view='polished'))

    def test_source_kind_id_and_uid_checked(self):
        for key, value in [('kind', 'email'), ('sourceId', 'local-copy'), ('startUid', 'u9999'), ('endUid', 'u0001')]:
            doc = self.document()
            doc['scenes'][0]['source'][key] = value
            with self.assertRaises(m.MapError):
                m.validate(self.bundle, doc)

    def test_scene_order_indexes_and_unknown_keys(self):
        for mutate in (
            lambda d: d['scenes'].reverse(),
            lambda d: d['scenes'][1].update(index=1),
            lambda d: d['scenes'][0].update(index=True),
            lambda d: d['scenes'][0].update(dateStrat='1748-04-12'),
            lambda d: d.update(entities=[]),
            lambda d: d['scenes'][0].update(type='recap'),
            lambda d: d['contextBlocks'][0].update(kind='combat'),
        ):
            doc = self.document()
            mutate(doc)
            with self.assertRaises(m.MapError):
                m.validate(self.bundle, doc)

    def test_discussion_only_recording(self):
        doc = m.build(self.bundle, {'dateValidation': self.proposal['dateValidation'], 'scenes': [], 'contextBlocks': [{
            'kind': 'loreDiscussion', 'source': m.source('u0001', 'u0006'),
            'aiSummary': 'Campaign planning and historical context; no current play.'}]})
        self.assertEqual(m.validate(self.bundle, doc)['scenes'], 0)

    def test_dates_allow_yaml_extension_and_nonchronological_source(self):
        doc = self.document()
        doc['scenes'][0].update(dateStart='1748-04-13', dateEnd=None)
        doc['scenes'][1].update(dateStart='1748-04-12')
        self.assertEqual(m.validate(self.bundle, doc)['findings'], [])
        doc['scenes'][1]['dateStart'] = '1748-04-11'
        result = m.validate(self.bundle, doc)
        self.assertEqual(result['findings'][0]['severity'], 'warning')

    def test_invalid_dates_and_reversed_ranges(self):
        for fields in ({'dateStart': '1748-02-31'}, {'dateStart': '1748-04-14', 'dateEnd': '1748-04-12'}):
            doc = self.document()
            doc['scenes'][0].update(fields)
            with self.assertRaises(m.MapError):
                m.validate(self.bundle, doc)

    def test_clear_date_conflict_is_critical_with_yaml_and_source_evidence(self):
        doc = self.document()
        doc['findings'] = [{'kind': 'dateConflict', 'source': m.source('u0002', 'u0004'),
                            'yamlFields': ['drStart'], 'reason': 'Explicit current date differs from YAML.'}]
        doc['dateValidation'] = {'result': 'conflict', 'reason': 'The current date contradicts YAML drStart.',
                                 'evidence': [m.source('u0002', 'u0004')]}
        self.assertEqual(m.validate(self.bundle, doc)['findings'][0]['severity'], 'critical')
        del doc['findings'][0]['yamlFields']
        with self.assertRaisesRegex(m.MapError, 'affected YAML'):
            m.validate(self.bundle, doc)

    def test_stale_source_and_semantic_yaml_change(self):
        doc = self.document()
        self.yaml.write_text(self.yaml.read_text() + '\n# formatting only\ninteractionExtraction: {}\n')
        m.validate(self.load(), doc)
        self.yaml.write_text(self.yaml.read_text().replace('drEnd: 1748-04-14', 'drEnd: 1748-04-15'))
        with self.assertRaisesRegex(m.MapError, 'inputs changed'):
            m.validate(self.load(), doc)
        self.yaml.write_bytes(self.originals[self.yaml])
        self.source.write_text(self.source.read_text().replace('Grash', 'Gresh'))
        with self.assertRaisesRegex(m.MapError, 'inputs changed'):
            m.validate(self.load(), doc)

    def test_save_preserves_inputs_and_uses_only_one_output(self):
        m.draft.initialize(self.bundle)
        before_draft = self.bundle['draft'].read_bytes()
        doc = m.save(self.bundle, self.proposal)
        self.assertEqual(m.read_map(self.bundle), doc)
        self.assertEqual(self.bundle['draft'].read_bytes(), before_draft)
        for p, raw in self.originals.items():
            self.assertEqual(p.read_bytes(), raw)
        self.assertEqual({p for p in self.root.rglob('*') if p.is_file()},
                         set(self.originals) | {self.bundle['draft'], self.bundle['mapPath']})

    def test_existing_map_and_concurrent_changes_are_preserved(self):
        m.save(self.bundle, self.proposal)
        path = self.bundle['mapPath']
        original = path.read_bytes()
        for expected in (None, 'wrong'):
            with self.assertRaisesRegex(m.MapError, 'inspected --expect-sha256'):
                m.save(self.bundle, self.proposal, expected)
            self.assertEqual(path.read_bytes(), original)
        self.proposal['scenes'][0]['aiSummary'] = 'Revised after reading the conversation.'
        m.save(self.bundle, self.proposal, m.draft.sha(original))
        self.assertNotEqual(path.read_bytes(), original)

    def test_changed_input_during_write_is_rejected(self):
        self.source.write_text(self.source.read_text() + '\n')
        with self.assertRaisesRegex(m.MapError, 'Input changed during mapping'):
            m.save(self.bundle, self.proposal)
        self.assertFalse(self.bundle['mapPath'].exists())

    def test_symlink_and_hardlink_output_are_rejected(self):
        path = self.bundle['mapPath']
        path.symlink_to(self.source)
        with self.assertRaises(ValueError):
            m.save(self.bundle, self.proposal)
        path.unlink()
        os.link(self.source, path)
        with self.assertRaisesRegex(m.MapError, 'hard link'):
            m.save(self.bundle, self.proposal, m.draft.sha(path.read_bytes()))
        self.assertEqual(self.source.read_bytes(), self.originals[self.source])

    def test_location_path_is_optional_but_must_resolve_when_supplied(self):
        place = self.vault / 'Places/Gate.md'
        place.parent.mkdir()
        place.write_text('# Gate\n')
        doc = self.document()
        doc['scenes'][0]['location'] = 'Places/Gate.md'
        m.validate(self.bundle, doc)
        for path in ('../outside.md', 'Places/Missing.md'):
            doc['scenes'][0]['location'] = path
            with self.assertRaises(ValueError):
                m.validate(self.bundle, doc)

    def test_preview_is_compact_ordered_and_does_not_copy_source(self):
        text = m.preview(self.bundle, self.document())
        self.assertLess(text.index('| recap |'), text.index('| Scene 1 |'))
        self.assertLess(text.index('| Scene 2 |'), text.index('| loreDiscussion |'))
        self.assertNotIn('DM: Grash', text)
        self.assertIn('does not establish semantic review', text)
        self.assertFalse(self.bundle['mapPath'].exists())

    def test_preview_source_links_point_to_actual_mapping_lines(self):
        text = m.preview(self.bundle, self.document())
        lines = self.source.read_text().splitlines()
        for uid in ('u0001', 'u0002', 'u0005', 'u0006'):
            line = self.bundle['lines'][uid]
            self.assertTrue(lines[line - 1].startswith('%% ' + uid + ':'))
            self.assertIn(f'{self.source}:{line}', text)

    def test_undated_scenes_do_not_automatically_validate_yaml(self):
        doc = self.document()
        del doc['dateValidation']
        result = m.validate(self.bundle, doc)
        self.assertEqual(result['coverage'], 'complete')
        self.assertEqual(result['dateValidation']['result'], 'notChecked')
        self.assertIn('**notChecked**', m.preview(self.bundle, doc))
        proposal = copy.deepcopy(self.proposal)
        del proposal['dateValidation']
        with self.assertRaisesRegex(m.MapError, 'dateValidation'):
            m.save(self.bundle, proposal)
        self.assertFalse(self.bundle['mapPath'].exists())

    def test_consistent_assessment_needs_positive_source_evidence(self):
        doc = self.document()
        doc['dateValidation']['result'] = 'consistent'
        with self.assertRaisesRegex(m.MapError, 'requires transcript evidence'):
            m.validate(self.bundle, doc)
        doc['dateValidation']['evidence'] = [m.source('u0002', 'u0004')]
        doc['dateValidation']['reason'] = 'The current-day anchor is compatible; the final endpoint is unconfirmed.'
        self.assertEqual(m.validate(self.bundle, doc)['dateValidation']['result'], 'consistent')
        doc['dateValidation']['evidence'][0]['endUid'] = 'u9999'
        with self.assertRaisesRegex(m.MapError, 'unknown endUid'):
            m.validate(self.bundle, doc)

    def test_conflict_cannot_be_hidden_by_clean_assessment_or_undated_scenes(self):
        doc = self.document()
        doc['findings'] = [{'kind': 'dateConflict', 'source': m.source('u0002', 'u0004'),
                            'yamlFields': ['drStart', 'drEnd'], 'reason': 'Explicit current date contradicts the YAML span.'}]
        for outcome in ('consistent', 'insufficientEvidence'):
            doc['dateValidation'] = {'result': outcome, 'reason': 'Attempted clean outcome.',
                                     'evidence': [m.source('u0002', 'u0004')]}
            with self.assertRaisesRegex(m.MapError, 'must agree'):
                m.validate(self.bundle, doc)
        doc['dateValidation']['result'] = 'conflict'
        result = m.validate(self.bundle, doc)
        self.assertEqual(result['findings'][0]['severity'], 'critical')
        text = m.preview(self.bundle, doc)
        self.assertLess(text.index('Date findings:'), text.index('| Scene / context |'))
        self.assertIn('drStart=1748-04-12', text)
        self.assertIn('drEnd=1748-04-14', text)
        self.assertIn('u0002–u0004', text)
        doc['findings'] = []
        with self.assertRaisesRegex(m.MapError, 'must agree'):
            m.validate(self.bundle, doc)

    def test_insufficient_evidence_can_save_without_claiming_an_error(self):
        doc = m.save(self.bundle, self.proposal)
        result = m.validate(self.bundle, doc)
        self.assertEqual(result['dateValidation']['result'], 'insufficientEvidence')
        self.assertEqual(result['findings'], [])
        self.assertIn('**insufficientEvidence**', m.preview(self.bundle, doc))


if __name__ == '__main__':
    unittest.main()
