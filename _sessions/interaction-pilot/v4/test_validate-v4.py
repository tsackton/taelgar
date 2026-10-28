"""Boundary and provenance checks; run with python -m unittest discover -s scripts."""
import copy
import hashlib
import tempfile
import unittest
from pathlib import Path

from validate import render, validate, upgrade_v3


class ExtractionValidationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        source = '[u0001 | 00:00 | DM] A guide waits.\n[u0002 | 00:01 | Guide] Follow me.\n[u0003 | 00:02 | DM] They leave.\n'
        (self.vault / 'source.md').write_text(source)
        scene = {'index': 1, 'type': 'conversation', 'startUid': 'u0001', 'endUid': 'u0002', 'boundary': 'Departure follows.',
                 'location': 'Gate', 'date': {'start': None, 'end': None, 'time': None,
                 'basis': 'No date in source.', 'evidence': ['source.md']}}
        self.data = {'schema_version': 3, 'campaign': 'test', 'session': 'test-001', 'segmentation_revision': 1,
                     'source': {'kind': 'transcript', 'path': 'source.md', 'sha256': hashlib.sha256(source.encode()).hexdigest()},
                     'supporting_sources': [], 'scenes': [scene, {**copy.deepcopy(scene), 'index': 2,
                     'startUid': 'u0003', 'endUid': 'u0003', 'location': 'Road'}], 'excluded_ranges': [],
                     'entities': [{'id': 'guide', 'kind': 'npc', 'label': 'Guide', 'canonical_name': None, 'note': None,
                     'eligibility': 'individual', 'basis': 'Distinct guide speaks to party.', 'session_overview': 'The guide offers to lead the party.', 'overview_records': ['s01-guide'], 'quote_review': 'no_suitable_dialogue'}],
                     'interactions': [{'id': 's01-guide', 'entity': 'guide', 'scenes': [1], 'interaction': 'interacted',
                     'importance': 'supporting', 'overview': 'The guide asks the party to follow.',
                     'transcript': [{'startUid': 'u0001', 'endUid': 'u0002'}],
                     'introduction': {'startUid': 'u0001', 'endUid': 'u0001', 'kind': 'description', 'quote': 'A guide waits.'}}],
                     'review_notes': []}

    def test_valid_and_rendered_links(self):
        rows, span = validate(self.data, self.vault)
        self.assertIn(f'source.md:1>', render(self.data, self.vault, rows, span))
        self.assertNotIn('**u0002', render(self.data, self.vault, rows, span))
        self.assertIn('Follow me.', render(self.data, self.vault, rows, span, excerpts=True))

    def test_source_change_rejected(self):
        (self.vault / 'source.md').write_text('Changed source')
        with self.assertRaisesRegex(ValueError, 'hash changed'):
            validate(self.data, self.vault)

    def test_cross_scene_excerpt_rejected(self):
        self.data['interactions'][0]['transcript'][0]['endUid'] = 'u0003'
        with self.assertRaisesRegex(ValueError, 'crosses scene'):
            validate(self.data, self.vault)

    def test_unsupported_quote_rejected(self):
        self.data['interactions'][0]['introduction']['quote'] = 'A friendly guide waits.'
        with self.assertRaisesRegex(ValueError, 'not verbatim'):
            validate(self.data, self.vault)

    def test_missing_coverage_rejected(self):
        self.data['scenes'].pop()
        with self.assertRaisesRegex(ValueError, 'Incomplete source coverage'):
            validate(self.data, self.vault)

    def test_duplicate_record_rejected(self):
        self.data['interactions'].append({**copy.deepcopy(self.data['interactions'][0]), 'id': 'second'})
        self.data['interactions'][1].pop('introduction')
        self.data['entities'][0]['overview_records'].append('second')
        with self.assertRaisesRegex(ValueError, 'Overlapping duplicate'):
            validate(self.data, self.vault)

    def test_multiscene_encounter(self):
        r = self.data['interactions'][0]
        r['scenes'] = [1, 2]
        r['transcript'][0]['endUid'] = 'u0003'
        r['continuity'] = 'Same guide leads party onto road.'
        validate(self.data, self.vault)
        del r['continuity']
        with self.assertRaisesRegex(ValueError, 'continuity'):
            validate(self.data, self.vault)

    def test_present_requires_evidence(self):
        r = self.data['interactions'][0]
        r['interaction'] = 'present'
        with self.assertRaisesRegex(ValueError, 'affirmatively'):
            validate(self.data, self.vault)
        r['presence_basis'] = 'u0001 explicitly places guide at gate.'
        validate(self.data, self.vault)

    def test_session_overview_joins(self):
        self.data['entities'][0]['overview_records'] = ['wrong']
        with self.assertRaisesRegex(ValueError, 'all and only'):
            validate(self.data, self.vault)

    def test_pull_quote_provenance(self):
        r = self.data['interactions'][0]
        r['quotes'] = [{'id': 'guide-quote', 'startUid': 'u0002', 'endUid': 'u0002', 'kind': 'dialogue',
                           'quote': 'Follow me.', 'speaker': 'guide', 'attribution': 'Guide speaks directly.'}]
        e = self.data['entities'][0]
        e['quote_review'] = 'selected'
        e['featured_quote_ids'] = ['guide-quote']
        validate(self.data, self.vault)
        r['quotes'][0]['speaker'] = 'someone-else'
        with self.assertRaisesRegex(ValueError, 'another NPC'):
            validate(self.data, self.vault)
        r['quotes'][0]['speaker'] = 'guide'
        r['quotes'][0]['quote'] = 'Please follow me.'
        with self.assertRaisesRegex(ValueError, 'not verbatim'):
            validate(self.data, self.vault)

    def test_highlights_cannot_replace_bounds(self):
        self.data['interactions'][0]['excerpts'] = [{'startUid': 'u0003', 'endUid': 'u0003'}]
        with self.assertRaisesRegex(ValueError, 'Highlight outside'):
            validate(self.data, self.vault)

    def test_scene_type_required(self):
        for value in (None, 'mixed', 'talking'):
            self.data['scenes'][0]['type'] = value
            with self.assertRaisesRegex(ValueError, 'scene type'):
                validate(self.data, self.vault)

    def test_item_card_and_source_quote(self):
        e = self.data['entities'][0]
        e.update(kind='item', eligibility='distinctive', label='Stone box')
        r = self.data['interactions'][0]
        r['quotes'] = [{'id': 'box-quote', 'kind': 'description', 'quote': 'A guide waits.',
                       'startUid': 'u0001', 'endUid': 'u0001', 'speaker': None, 'attribution': 'Fixture narration.'}]
        e.update(quote_review='selected', featured_quote_ids=['box-quote'])
        rows, span = validate(self.data, self.vault)
        self.assertIn('Stone box · ITEM', render(self.data, self.vault, rows, span))
        r['quotes'][0].update(kind='dialogue', speaker='guide')
        with self.assertRaisesRegex(ValueError, 'actual speaker'):
            validate(self.data, self.vault)

    def test_multiple_quotes_one_interaction(self):
        r = self.data['interactions'][0]
        e = self.data['entities'][0]
        r['quotes'] = [
            {'id': 'first', 'kind': 'dialogue', 'quote': 'Follow', 'startUid': 'u0002', 'endUid': 'u0002', 'speaker': 'guide', 'attribution': 'Test fixture.'},
            {'id': 'second', 'kind': 'dialogue', 'quote': 'me.', 'startUid': 'u0002', 'endUid': 'u0002', 'speaker': 'guide', 'attribution': 'Test fixture.'}]
        e.update(quote_review='selected', featured_quote_ids=['second', 'first'])
        rows, span = validate(self.data, self.vault)
        output = render(self.data, self.vault, rows, span)
        self.assertLess(output.index('> me.'), output.index('> Follow'))
        self.assertEqual(len(self.data['interactions']), 1)
        e['featured_quote_ids'].append('unknown')
        with self.assertRaisesRegex(ValueError, 'belong to this entity'):
            validate(self.data, self.vault)

    def test_duplicate_quote_ids_rejected(self):
        r = self.data['interactions'][0]
        quote = {'id': 'q', 'kind': 'dialogue', 'quote': 'Follow me.', 'startUid': 'u0002',
                 'endUid': 'u0002', 'speaker': 'guide', 'attribution': 'Guide says this.'}
        r['quotes'] = [quote, copy.deepcopy(quote)]
        with self.assertRaisesRegex(ValueError, 'duplicate quote ID'):
            validate(self.data, self.vault)

    def test_old_interaction_enum_rejected(self):
        self.data['interactions'][0]['interaction'] = 'met'
        with self.assertRaisesRegex(ValueError, 'Invalid interaction'):
            validate(self.data, self.vault)


    def with_notes(self):
        self.data = upgrade_v3(self.data)
        text = 'Afterward the guide leaves. The guide returns the next day.\nThe guide says: "Farewell."\n'
        (self.vault / 'notes.md').write_text(text)
        self.data['sources'].append({'id': 'note', 'kind': 'session_notes', 'path': 'notes.md',
                                    'sha256': hashlib.sha256(text.encode()).hexdigest()})
        return {'source': 'note', 'startLine': 1, 'endLine': 1, 'text': 'Afterward the guide leaves.'}

    def note_event(self):
        selector = self.with_notes()
        scene = copy.deepcopy(self.data['scenes'][1])
        scene.update(index=3, evidence=[selector])
        self.data['scenes'].append(scene)
        record = {'id': 'later', 'entity': 'guide', 'scenes': [3], 'interaction': 'observed',
                  'importance': 'cameo', 'overview': 'The notes record the guide leaving.',
                  'evidence': [selector], 'perspective': 'session_record',
                  'observation_basis': 'No party witness is identified.'}
        self.data['interactions'].append(record)
        self.data['entities'][0]['overview_records'].append('later')
        return selector, record

    def test_note_only_event_and_original_link(self):
        selector, record = self.note_event()
        rows, span = validate(self.data, self.vault)
        output = render(self.data, self.vault, rows, span, excerpts=True)
        self.assertIn('Session note L1–L1', output)
        self.assertIn('notes.md:1>', output)
        self.assertIn('Documented event; party witnessing is not established.', output)
        self.assertIn('> Afterward the guide leaves.', output)
        self.assertEqual(len(self.data['entities']), 1)

    def test_notes_only_input_without_uid_copy(self):
        selector, record = self.note_event()
        self.data['sources'] = self.data['sources'][1:]
        self.data['scenes'] = [self.data['scenes'][-1]]
        self.data['scenes'][0]['index'] = 1
        self.data['interactions'] = [record]
        record['scenes'] = [1]
        self.data['entities'][0]['overview_records'] = ['later']
        validate(self.data, self.vault)

    def test_note_selector_exact_and_unambiguous(self):
        selector, record = self.note_event()
        selector['text'] = 'The friendly guide leaves.'
        with self.assertRaisesRegex(ValueError, 'exact, unambiguous'):
            validate(self.data, self.vault)
        selector['text'] = 'guide'
        with self.assertRaisesRegex(ValueError, 'exact, unambiguous'):
            validate(self.data, self.vault)

    def test_note_source_change_rejected(self):
        self.note_event()
        (self.vault / 'notes.md').write_text('Changed notes')
        with self.assertRaisesRegex(ValueError, 'hash changed'):
            validate(self.data, self.vault)

    def test_notes_cannot_use_fabricated_uids(self):
        selector, record = self.note_event()
        selector['startUid'] = selector['endUid'] = 'u0001'
        with self.assertRaisesRegex(ValueError, 'fabricated UIDs'):
            validate(self.data, self.vault)

    def test_note_evidence_cannot_cross_scene(self):
        selector, record = self.note_event()
        record['evidence'] = [{**selector, 'text': 'The guide returns the next day.'}]
        with self.assertRaisesRegex(ValueError, 'crosses scene'):
            validate(self.data, self.vault)

    def test_merge_note_evidence_into_one_encounter(self):
        selector = self.with_notes()
        selector.update(startLine=2, endLine=2, text='The guide says: "Farewell."')
        self.data['scenes'][0]['evidence'].append(selector)
        record = self.data['interactions'][0]
        record['evidence'].append(selector)
        record['continuity'] = 'The note documents the close of the same conversation.'
        validate(self.data, self.vault)
        self.assertEqual(len(self.data['interactions']), 1)

    def test_note_dialogue_must_be_labeled(self):
        selector, record = self.note_event()
        selector.update(startLine=2, endLine=2, text='The guide says: "Farewell."')
        quote = {**selector, 'id': 'farewell', 'kind': 'dialogue', 'speaker': 'guide',
                 'quote': 'Farewell.', 'attribution': 'Guide speech explicitly quoted by the note.'}
        record['quotes'] = [quote]
        self.data['entities'][0].update(quote_review='selected', featured_quote_ids=['farewell'])
        with self.assertRaisesRegex(ValueError, 'reported_in_notes'):
            validate(self.data, self.vault)
        quote['verification'] = 'reported_in_notes'
        rows, span = validate(self.data, self.vault)
        self.assertIn('Reported in notes; not transcript-verified.', render(self.data, self.vault, rows, span))

    def test_same_note_paragraph_can_document_separate_events(self):
        selector, record = self.note_event()
        selector['text'] += ' The guide returns the next day.'
        scene = copy.deepcopy(self.data['scenes'][-1])
        scene['index'] = 4
        self.data['scenes'].append(scene)
        returned = copy.deepcopy(record)
        returned.update(id='returned', scenes=[4], overview='The notes record the guide returning the following day.')
        self.data['interactions'].append(returned)
        self.data['entities'][0]['overview_records'].append('returned')
        validate(self.data, self.vault)
        returned['scenes'] = [3]
        with self.assertRaisesRegex(ValueError, 'Overlapping duplicate'):
            validate(self.data, self.vault)

    def test_transcript_uid_collisions_across_sources(self):
        self.data = upgrade_v3(self.data)
        text = (self.vault / 'source.md').read_text()
        (self.vault / 'second.md').write_text(text)
        self.data['sources'].append({'id': 'second', 'kind': 'transcript', 'path': 'second.md',
                                    'sha256': hashlib.sha256(text.encode()).hexdigest()})
        scene = copy.deepcopy(self.data['scenes'][0])
        scene.update(index=3, evidence=[{'source': 'second', 'startUid': 'u0001', 'endUid': 'u0003'}])
        self.data['scenes'].append(scene)
        validate(self.data, self.vault)
        self.data['scenes'].pop()
        with self.assertRaisesRegex(ValueError, 'Incomplete source coverage'):
            validate(self.data, self.vault)

    def test_unknown_evidence_source_rejected(self):
        selector, record = self.note_event()
        selector['source'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Unknown evidence source'):
            validate(self.data, self.vault)


if __name__ == '__main__':
    unittest.main()
