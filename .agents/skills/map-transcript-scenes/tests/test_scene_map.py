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
            '%% u0005:0-10 %%\nPC: We reach the mountain shrine.\n\n'
            '%% u0006:0-10 %%\nDM: Afterwards: the old king also used this hall.\n\n', encoding='utf-8', newline='\n')
        self.yaml.write_text('sourceType: transcript\nrealWorldDate: 2020-10-02\n'
            'drStart: 1748-04-12\ndrEnd: 1748-04-14\ntranscriptProcessing:\n  artifacts:\n'
            '    polishedMarkdown:\n      path: cleaned/demo-transcript.md\n', encoding='utf-8', newline='\n')
        self.bundle = self.load()
        self.originals = {p: p.read_bytes() for p in (self.yaml, self.source)}
        self.proposal = {
            'review': {'confidence': 'high', 'status': 'unreviewed'},
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
        self.assertNotIn('We reach the mountain shrine', view)

    def test_polished_parentheses_do_not_require_draft_compatibility(self):
        self.source.write_text(self.source.read_text(encoding='utf-8').replace(
            'Grash greets you', 'Grash ((the guide)) greets you'), encoding='utf-8', newline='\n')
        bundle = self.load()
        original = self.source.read_bytes()
        self.assertIn('Grash ((the guide))', m.window(bundle, 'u0002', 'u0004', 'polished'))
        m.save(bundle, self.proposal)
        with self.assertRaisesRegex(ValueError, 'reserved'):
            m.draft.initialize(bundle)
        self.assertFalse(bundle['draft'].exists())
        self.assertEqual(self.source.read_bytes(), original)

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
        path.write_text(path.read_text(encoding='utf-8').replace('Grash greets', 'Grash attacks'), encoding='utf-8', newline='\n')
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
        doc = m.build(self.bundle, {'review': self.proposal['review'], 'scenes': [], 'contextBlocks': [{
            'kind': 'loreDiscussion', 'source': m.source('u0001', 'u0006'),
            'aiSummary': 'Campaign planning and historical context; no current play.'}]})
        self.assertEqual(m.validate(self.bundle, doc)['scenes'], 0)

    def test_dates_allow_yaml_extension_and_nonchronological_source(self):
        doc = self.document()
        doc['scenes'][0].update(dateStart='1748-04-13', dateEnd=None)
        doc['scenes'][1].update(dateStart='1748-04-12')
        self.assertEqual(m.validate(self.bundle, doc)['issues'], [])
        doc['scenes'][1]['dateStart'] = '1748-04-11'
        result = m.validate(self.bundle, doc)
        self.assertEqual(result['issues'], [])  # Validation does not author AI concerns.

    def test_invalid_dates_and_reversed_ranges(self):
        for fields in ({'dateStart': '1748-02-31'}, {'dateStart': '1748-04-14', 'dateEnd': '1748-04-12'}):
            doc = self.document()
            doc['scenes'][0].update(fields)
            with self.assertRaises(m.MapError):
                m.validate(self.bundle, doc)

    def test_ai_concerns_roundtrip_with_multiple_evidence_ranges(self):
        self.proposal['issues'] = [{
            'description': 'The explicit current date disagrees with YAML drStart; check both endpoints.',
            'evidence': [m.source('u0001', 'u0001'), m.source('u0002', 'u0004')]}]
        doc = m.save(self.bundle, self.proposal)
        self.assertEqual(m.read_map(self.bundle)['issues'], self.proposal['issues'])
        self.assertEqual(m.validate(self.bundle, doc)['issues'], self.proposal['issues'])
        text = m.preview(self.bundle, doc)
        self.assertLess(text.index('AI-generated concerns:'), text.index('| Scene / context |'))
        self.assertIn(self.proposal['issues'][0]['description'], text)
        self.assertIn('u0001–u0001', text)
        self.assertIn('u0002–u0004', text)
        self.assertNotIn('dateValidation', doc)
        self.assertNotIn('findings', doc)

    def test_stale_source_and_semantic_yaml_change(self):
        doc = self.document()
        self.yaml.write_text(self.yaml.read_text(encoding='utf-8') + '\n# formatting only\ninteractionExtraction: {}\n', encoding='utf-8', newline='\n')
        m.validate(self.load(), doc)
        self.yaml.write_text(self.yaml.read_text(encoding='utf-8').replace('drEnd: 1748-04-14', 'drEnd: 1748-04-15'), encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(m.MapError, 'inputs changed'):
            m.validate(self.load(), doc)
        self.yaml.write_bytes(self.originals[self.yaml])
        self.source.write_text(self.source.read_text(encoding='utf-8').replace('Grash', 'Gresh'), encoding='utf-8', newline='\n')
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
        self.source.write_text(self.source.read_text(encoding='utf-8') + '\n', encoding='utf-8', newline='\n')
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
        place.write_text('# Gate\n', encoding='utf-8', newline='\n')
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
        lines = self.source.read_text(encoding='utf-8').splitlines()
        for uid in ('u0001', 'u0002', 'u0005', 'u0006'):
            line = self.bundle['lines'][uid]
            self.assertTrue(lines[line - 1].startswith('%% ' + uid + ':'))
            self.assertIn(m.quote(str(self.source), safe='/') + f':{line}', text)

    def test_preview_links_places_and_shows_a_common_date_once_above_rows(self):
        place = self.vault / 'Places/The Gate.md'
        place.parent.mkdir()
        place.write_text('# Gate\n', encoding='utf-8')
        doc = self.document()
        for row in doc['scenes']:
            row.update(dateStart='1748-04-12', dateEnd='1748-04-12')
        doc['scenes'][0].update(location='Places/The Gate.md', locationDetail='Outer gate',
                                timeStart='Afternoon', timeEnd='Sunset')
        text = m.preview(self.bundle, doc)
        self.assertIn(f'[The Gate](<{m.quote(str(place), safe="/")}>) / Outer gate', text)
        self.assertIn('Played scenes: 1748-04-12.', text)
        self.assertIn('| Place | Start time | End time |', text)
        rows = [line for line in text.splitlines() if line.startswith('| Scene ')]
        self.assertTrue(all('1748-04-12' not in line for line in rows))
        self.assertTrue(any('Afternoon' in line for line in rows))
        self.assertTrue(any('Sunset' in line for line in rows))
        doc['scenes'][1].update(dateStart='1748-04-13', dateEnd='1748-04-14')
        text = m.preview(self.bundle, doc)
        self.assertNotIn('Played scenes:', text)
        self.assertIn('| Place | Start | End |', text)
        self.assertIn('1748-04-13 | 1748-04-14', text)

    def test_time_endpoints_roundtrip_independently_without_inventing_missing_values(self):
        cases = ({'timeStart': 'After breakfast'}, {'timeEnd': 'About sunset'},
                 {'timeStart': None, 'timeEnd': None},
                 {'dateStart': '1748-04-12', 'timeStart': 'Late evening',
                  'dateEnd': '1748-04-13', 'timeEnd': 'Before dawn'})
        for values in cases:
            with self.subTest(values=values):
                proposal = copy.deepcopy(self.proposal)
                proposal['scenes'][0].update(values)
                path = self.bundle['mapPath']
                expected = m.draft.sha(path.read_bytes()) if path.exists() else None
                doc = m.save(self.bundle, proposal, expected)
                self.assertEqual(m.read_map(self.bundle), doc)
                self.assertNotIn('time', doc['scenes'][0])
                for key in ('timeStart', 'timeEnd'):
                    self.assertEqual(key in doc['scenes'][0], key in values)
                    self.assertEqual(doc['scenes'][0].get(key), values.get(key))
        for field in ('timeStart', 'timeEnd'):
            for invalid in ('', 'Two\nlines', 9, []):
                doc = self.document()
                doc['scenes'][0][field] = invalid
                with self.assertRaises(m.MapError):
                    m.validate(self.bundle, doc)
        doc = self.document()
        doc['scenes'][0]['time'] = 'Afternoon to evening'
        with self.assertRaisesRegex(m.MapError, 'unknown fields.*time'):
            m.validate(self.bundle, doc)

    def test_legacy_time_remains_verbatim_without_synthesized_endpoints(self):
        doc = self.document()
        doc['schemaVersion'] = 1
        del doc['review']
        doc['scenes'][0]['time'] = 'After dinner through an eight-hour rest'
        raw = m.encoded(doc)
        self.bundle['mapPath'].write_bytes(raw)
        self.assertEqual(m.read_map(self.bundle), doc)
        text = m.preview(self.bundle, doc)
        self.assertIn('Date/Time (legacy)', text)
        self.assertIn('After dinner through an eight-hour rest', text)
        self.assertNotIn('timeStart', doc['scenes'][0])
        self.assertNotIn('timeEnd', doc['scenes'][0])
        self.assertEqual(self.bundle['mapPath'].read_bytes(), raw)

    def test_issues_can_be_omitted_without_creating_a_date_assessment(self):
        doc = m.save(self.bundle, self.proposal)
        self.assertNotIn('issues', doc)
        result = m.validate(self.bundle, doc)
        self.assertEqual(result['issues'], [])
        self.assertNotIn('dateValidation', result)
        self.assertNotIn('findings', result)
        text = m.preview(self.bundle, doc)
        for unwanted in ('Session date validation', 'notChecked', 'AI-generated concerns:'):
            self.assertNotIn(unwanted, text)
        proposal = copy.deepcopy(self.proposal)
        proposal['issues'] = []
        m.build(self.bundle, proposal)

    def test_issues_allow_map_wide_concerns_and_validate_supplied_evidence(self):
        doc = self.document()
        doc['issues'] = [{'description': 'The recording gap makes the route boundary uncertain.'}]
        m.validate(self.bundle, doc)
        self.assertIn(doc['issues'][0]['description'], m.preview(self.bundle, doc))
        for value in ('wrong', None, [{}], [{'description': ''}],
                      [{'description': 'Two\nlines'}],
                      [{'description': 'Question', 'status': 'unreviewed'}],
                      [{'description': 'Question', 'evidence': []}],
                      [{'description': 'Question', 'evidence': [m.source('u9999', 'u9999')]}],
                      [{'description': 'Question', 'evidence': [m.source('u0003', 'u0003')]}]):
            with self.subTest(issues=value):
                doc['issues'] = value
                with self.assertRaises(m.MapError):
                    m.validate(self.bundle, doc)

    def test_retired_date_assessment_and_findings_are_rejected_in_v2(self):
        for retired, value in (
            ('dateValidation', {'result': 'consistent', 'reason': 'Old pass.',
                                'evidence': [m.source('u0001', 'u0001')]}),
            ('findings', []),
        ):
            with self.subTest(field=retired):
                proposal = dict(self.proposal, **{retired: value})
                with self.assertRaisesRegex(m.MapError, 'unknown fields.*' + retired):
                    m.save(self.bundle, proposal)
                self.assertFalse(self.bundle['mapPath'].exists())

    def test_legacy_concerns_remain_visible_without_positive_assessments_or_writes(self):
        doc = self.document()
        doc['schemaVersion'] = 1
        del doc['review']
        doc['findings'] = [{'kind': 'dateConflict', 'source': m.source('u0002', 'u0004'),
                            'yamlFields': ['drStart'], 'reason': 'The spoken current date differs.'}]
        doc['dateValidation'] = {'result': 'conflict', 'reason': 'Former date assessment.',
                                 'evidence': [m.source('u0002', 'u0004')]}
        raw = m.encoded(doc)
        self.bundle['mapPath'].write_bytes(raw)
        self.assertEqual(m.read_map(self.bundle), doc)
        text = m.preview(self.bundle, doc)
        self.assertIn('The spoken current date differs.', text)
        self.assertIn('drStart', text)
        self.assertNotIn('Former date assessment.', text)
        self.assertEqual(self.bundle['mapPath'].read_bytes(), raw)
        doc['findings'] = []
        doc['dateValidation'] = {'result': 'consistent', 'reason': 'Old compatible timeline.',
                                 'evidence': [m.source('u0002', 'u0004')]}
        self.assertEqual(m.validate(self.bundle, doc)['issues'], [])
        self.assertNotIn('Old compatible timeline.', m.preview(self.bundle, doc))
        doc['dateValidation'] = {'result': 'insufficientEvidence',
            'reason': 'Uncertain travel may exceed YAML drEnd.', 'evidence': []}
        issues = m.validate(self.bundle, doc)['issues']
        self.assertEqual(issues, [{'description': 'Uncertain travel may exceed YAML drEnd.'}])

    def test_map_review_roundtrips_all_shared_values_and_previews_once(self):
        for confidence in ('high', 'medium', 'low'):
            for status in ('unreviewed', 'automatedReviewed', 'humanReviewed'):
                with self.subTest(confidence=confidence, status=status):
                    self.proposal['review'] = {'confidence': confidence, 'status': status}
                    path = self.bundle['mapPath']
                    expected = m.draft.sha(path.read_bytes()) if path.exists() else None
                    doc = m.save(self.bundle, self.proposal, expected)
                    self.assertEqual(doc['schemaVersion'], 2)
                    self.assertNotIn('splitConfidence', doc)
                    self.assertEqual(m.read_map(self.bundle)['review'], self.proposal['review'])
                    self.assertEqual(m.validate(self.bundle, doc)['review'], self.proposal['review'])
                    text = m.preview(self.bundle, doc)
                    self.assertEqual(text.count('Scene map review:'), 1)
                    self.assertIn(f'**{confidence} / {status}**', text)
                    self.assertLess(text.index('Scene map review:'), text.index('| Scene / context |'))

    def test_legacy_maps_stay_readable_without_inventing_review(self):
        for old_confidence in (None, {'rating': 'high', 'reason': 'A former boundary assessment.'}):
            doc = self.document()
            doc['schemaVersion'] = 1
            del doc['review']
            if old_confidence:
                doc['splitConfidence'] = old_confidence
            raw = m.encoded(doc)
            self.bundle['mapPath'].write_bytes(raw)
            self.assertIsNone(m.validate(self.bundle, doc)['review'])
            self.assertNotIn('review', doc)
            self.assertIn('**not recorded**', m.preview(self.bundle, doc))
            self.assertEqual(m.read_map(self.bundle), doc)
            self.assertEqual(self.bundle['mapPath'].read_bytes(), raw)
        proposal = copy.deepcopy(self.proposal)
        del proposal['review']
        with self.assertRaisesRegex(m.MapError, 'review'):
            m.save(self.bundle, proposal, m.draft.sha(raw))
        self.assertEqual(self.bundle['mapPath'].read_bytes(), raw)

    def test_review_rejects_wrong_shapes_extra_prose_and_per_scene_scores(self):
        for value in (None, 'high', {}, {'confidence': 'high'}, {'status': 'unreviewed'},
                      {'rating': 'high', 'reason': 'Old shape.'},
                      {'confidence': 'notAssessed', 'status': 'unreviewed'},
                      {'confidence': 0.9, 'status': 'unreviewed'},
                      {'confidence': 'high', 'status': 'accepted'},
                      {'confidence': 'high', 'status': 'unreviewed', 'reason': 'Extra prose.'}):
            with self.subTest(value=value):
                proposal = copy.deepcopy(self.proposal)
                proposal['review'] = value
                with self.assertRaises(m.MapError):
                    m.save(self.bundle, proposal)
                self.assertFalse(self.bundle['mapPath'].exists())
        for key in ('confidence', 'splitConfidence', 'review'):
            doc = self.document()
            doc['scenes'][0][key] = 'high'
            with self.assertRaises(m.MapError):
                m.validate(self.bundle, doc)
        doc = self.document()
        doc['splitConfidence'] = {'rating': 'high', 'reason': 'Retired field.'}
        with self.assertRaisesRegex(m.MapError, 'unknown fields.*splitConfidence'):
            m.validate(self.bundle, doc)

    def test_v2_requires_review_and_does_not_infer_it_from_validation(self):
        doc = self.document()
        del doc['review']
        with self.assertRaisesRegex(m.MapError, 'missing fields.*review'):
            m.validate(self.bundle, doc)
        doc = self.document()
        self.assertEqual(doc['review']['status'], 'unreviewed')
        m.validate(self.bundle, doc)
        self.assertEqual(doc['review']['status'], 'unreviewed')

    def test_a_date_concern_does_not_automatically_change_map_review(self):
        doc = self.document()
        doc['issues'] = [{'description': 'The current date may disagree with YAML drStart.',
                          'evidence': [m.source('u0002', 'u0004')]}]
        result = m.validate(self.bundle, doc)
        self.assertEqual(result['review'], {'confidence': 'high', 'status': 'unreviewed'})
        self.assertEqual(doc['review']['status'], 'unreviewed')


if __name__ == '__main__':
    unittest.main()
