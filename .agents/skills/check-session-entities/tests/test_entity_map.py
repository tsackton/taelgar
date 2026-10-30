import copy
import importlib.util
import os
from pathlib import Path
import sys
import unittest

sys.dont_write_bytecode = True
BASE = Path(__file__).resolve().parents[2]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


e = module('entity_map', BASE / 'check-session-entities/scripts/entity_map.py')
fixtures = module('scene_fixtures', BASE / 'map-transcript-scenes/tests/test_scene_map.py')


class EntityMapTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.SceneMapTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        f = self.fixture
        self.note = f.vault / 'People/Grash.md'
        self.note.parent.mkdir()
        self.note.write_text('---\nname: Grash\n---\n# Grash\nA camp leader.\n', encoding='utf-8', newline='\n')
        self.bundle = self.load()
        self.proposal = {'entities': [{
            'id': 'e001', 'kind': 'npc', 'label': 'Grash', 'note': 'People/Grash.md',
            'occurrences': [{'source': e.scenes.source('u0001', 'u0001')},
                            {'source': e.scenes.source('u0002', 'u0004')}],
            'review': {'confidence': 'high', 'status': 'unreviewed'}}]}

    def load(self, notes=('People/Grash.md',)):
        return e.load(self.fixture.yaml, self.fixture.vault, notes)

    def document(self):
        return e.build(self.bundle, copy.deepcopy(self.proposal))

    def test_works_from_polished_source_without_scene_map(self):
        doc = self.document()
        self.assertEqual(e.validate(self.bundle, doc)['entities'], 1)
        self.assertFalse(self.bundle['mapPath'].exists())
        self.assertEqual(doc['schemaVersion'], 3)
        self.assertNotIn('sceneMapSha256', doc['inputs'])
        self.assertNotIn('pcs', doc)
        self.assertNotIn('scenes', doc)

    def test_entity_reads_preserve_literal_double_parentheses(self):
        source = self.fixture.source
        source.write_text(source.read_text(encoding='utf-8').replace(
            'Grash greets you', 'Grash ((the guide)) greets you'), encoding='utf-8', newline='\n')
        original = source.read_bytes()
        bundle = self.load()
        e.save(bundle, self.proposal)
        self.assertIn('Grash ((the guide))', e.preview(bundle, e.read_map(bundle), 'e001'))
        self.assertEqual(source.read_bytes(), original)
        self.assertFalse(bundle['draft'].exists())
        self.assertFalse(bundle['mapPath'].exists())

    def test_evidence_can_cross_prospective_scene_and_context_boundaries(self):
        doc = self.document()
        doc['entities'][0]['occurrences'] = [{'source': e.scenes.source('u0001', 'u0006')}]
        self.assertEqual(e.validate(self.bundle, doc)['entities'], 1)

    def test_partial_turn_unknown_and_reversed_ranges_rejected(self):
        for start, end in [('u0003', 'u0004'), ('u0002', 'u0002'),
                           ('u0004', 'u0002'), ('u0009', 'u0009')]:
            doc = self.document()
            doc['entities'][0]['occurrences'] = [{'source': e.scenes.source(start, end)}]
            with self.assertRaises(ValueError):
                e.validate(self.bundle, doc)

    def test_unlinked_high_confidence_identity_needs_no_reason(self):
        p = copy.deepcopy(self.proposal)
        row = p['entities'][0]
        del row['note']
        row['label'] = 'Unnamed camp spokesman'
        doc = e.build(self.load(notes=()), p)
        self.assertEqual(e.validate(self.load(notes=()), doc)['matched'], 0)
        self.assertNotIn('reason', doc['entities'][0])

    def test_entity_reasons_are_rejected_without_changing_existing_output(self):
        e.save(self.bundle, self.proposal)
        before = self.bundle['entityPath'].read_bytes()
        p = copy.deepcopy(self.proposal)
        p['entities'][0]['reason'] = 'Repeated identity explanation.'
        with self.assertRaisesRegex(ValueError, 'unknown fields.*reason'):
            e.save(self.bundle, p, e.scenes.draft.sha(before))
        self.assertEqual(self.bundle['entityPath'].read_bytes(), before)

    def test_no_duplicate_ids_or_matching_two_people_to_same_page(self):
        for change_id in (False, True):
            doc = self.document()
            second = copy.deepcopy(doc['entities'][0])
            if change_id:
                second['id'] = 'e002'
            doc['entities'].append(second)
            with self.assertRaises(ValueError):
                e.validate(self.bundle, doc)

    def test_unresolved_candidates_and_medium_confidence(self):
        p = copy.deepcopy(self.proposal)
        row = p['entities'][0]
        row['candidates'] = [row.pop('note')]
        row['review']['confidence'] = 'medium'
        doc = e.build(self.bundle, p)
        self.assertEqual(e.validate(self.bundle, doc)['reviewPriority'], ['e001'])
        self.assertIn('Unresolved candidates', e.preview(self.bundle, doc))
        self.assertIn('People/Grash.md', e.preview(self.bundle, doc))
        row['note'] = 'People/Grash.md'
        with self.assertRaisesRegex(ValueError, 'not both'):
            e.build(self.bundle, p)

    def test_later_identification_preserves_session_label_and_is_flagged(self):
        p = copy.deepcopy(self.proposal)
        row = p['entities'][0]
        row.update(label='Unnamed camp leader', identifiedLater=True)
        doc = e.build(self.bundle, p)
        e.save(self.bundle, p)
        reopened = e.read_map(self.load())
        self.assertEqual(reopened['entities'][0]['label'], 'Unnamed camp leader')
        self.assertEqual(reopened['entities'][0]['review']['confidence'], 'high')
        self.assertEqual(reopened['entities'][0]['occurrences'], row['occurrences'])
        preview = e.preview(self.bundle, doc)
        self.assertIn('identified later', preview)
        self.assertNotIn('reason', reopened['entities'][0])
        self.assertNotIn('Matched against source', e.preview(self.bundle, doc, 'e001'))

    def test_later_identification_requires_boolean_and_chosen_note(self):
        for value in ('true', 1, None):
            doc = self.document()
            doc['entities'][0]['identifiedLater'] = value
            with self.assertRaisesRegex(ValueError, 'must be a boolean'):
                e.validate(self.bundle, doc)
        doc = self.document()
        row = doc['entities'][0]
        row['identifiedLater'] = True
        row.pop('note')
        doc['evidenceNotes'] = ['People/Grash.md']
        with self.assertRaisesRegex(ValueError, 'requires a chosen note'):
            e.validate(self.bundle, doc)

    def test_scene_maps_are_not_read_or_fingerprinted(self):
        doc = self.document()
        scene_path = self.bundle['mapPath']
        scene_path.write_text('not even JSON', encoding='utf-8')
        self.assertEqual(self.bundle['entityInputDigest'], self.load()['entityInputDigest'])
        e.save(self.bundle, self.proposal)
        scene_path.write_text('changed scene map', encoding='utf-8')
        self.assertEqual(e.read_map(self.load()), doc)
        self.assertIn('Grash', e.preview(self.load(), doc))
        scene_path.unlink()
        self.assertEqual(e.read_map(self.load()), doc)

    def test_source_and_yaml_changes_invalidate_review_and_save(self):
        for path, suffix in [(self.fixture.source, '\n'),
                             (self.fixture.yaml, 'participants: []\n')]:
            with self.subTest(path=path.name):
                before = path.read_bytes()
                bundle = self.load()
                doc = e.build(bundle, self.proposal)
                path.write_bytes(before + suffix.encode())
                try:
                    with self.assertRaisesRegex(ValueError, 'inputs changed'):
                        e.validate(self.load(), doc)
                    with self.assertRaisesRegex(ValueError, 'Input changed'):
                        e.save(bundle, self.proposal)
                finally:
                    path.write_bytes(before)

    def test_legacy_scene_bound_maps_require_explicit_recheck(self):
        doc = self.document()
        doc['schemaVersion'] = 1
        doc['inputs']['sceneMapSha256'] = 'old-scene-hash'
        with self.assertRaisesRegex(ValueError, 'recheck legacy decisions'):
            e.validate(self.bundle, doc)

    def test_v2_requires_explicit_removal_before_guarded_v3_save(self):
        old = self.document()
        old['schemaVersion'] = 2
        old['entities'][0]['reason'] = 'Former v2 explanation.'
        raw = e.scenes.encoded(old)
        self.bundle['entityPath'].write_bytes(raw)
        with self.assertRaisesRegex(ValueError, 'explicit removal of entity reasons'):
            e.read_map(self.bundle)
        with self.assertRaisesRegex(ValueError, 'expect-sha256'):
            e.save(self.bundle, self.proposal)
        self.assertEqual(self.bundle['entityPath'].read_bytes(), raw)
        migrated = e.save(self.bundle, self.proposal, e.scenes.draft.sha(raw))
        self.assertEqual(migrated['schemaVersion'], 3)
        self.assertNotIn('reason', migrated['entities'][0])
        self.assertEqual(migrated['entities'][0]['review'], old['entities'][0]['review'])

    def test_note_changed_after_read_invalidates_review_and_save(self):
        doc = self.document()
        self.note.write_text(self.note.read_text(encoding='utf-8') + 'Different identity.\n', encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ValueError, 'inputs changed'):
            e.validate(self.load(), doc)
        with self.assertRaisesRegex(ValueError, 'evidence changed'):
            e.save(self.bundle, self.proposal)

    def test_new_evidence_must_be_inspected(self):
        with self.assertRaisesRegex(ValueError, 'differs from inspection'):
            e.build(self.load(notes=()), self.proposal)

    def test_source_preservation_and_only_one_output(self):
        before = {p: p.read_bytes() for p in self.fixture.vault.rglob('*') if p.is_file()}
        e.save(self.bundle, self.proposal)
        for p, content in before.items():
            self.assertEqual(p.read_bytes(), content)
        after = {p for p in self.fixture.vault.rglob('*') if p.is_file()}
        self.assertEqual(after - before.keys(), {self.bundle['entityPath']})
        self.assertEqual(e.read_map(self.bundle)['entities'], self.proposal['entities'])
        self.assertFalse(self.bundle['mapPath'].exists())

    def test_concurrent_output_and_unsafe_paths_rejected(self):
        e.save(self.bundle, self.proposal)
        for expected in (None, 'wrong'):
            with self.assertRaisesRegex(ValueError, 'expect-sha256'):
                e.save(self.bundle, self.proposal, expected)
        for path in ('../escape.md', str(self.note), '_dm_notes/Secret.md', '.agents/hidden.md'):
            with self.assertRaises(ValueError):
                e.note_path(self.bundle, path)

    def test_symlinks_and_hard_links_cannot_overwrite_source(self):
        path = self.bundle['entityPath']
        path.symlink_to(self.note)
        with self.assertRaises(ValueError):
            e.save(self.bundle, self.proposal)
        path.unlink()
        os.link(self.note, path)
        with self.assertRaisesRegex(ValueError, 'hard link'):
            e.save(self.bundle, self.proposal, e.scenes.draft.sha(path.read_bytes()))

    def test_invalid_kind_review_and_occurrence_order(self):
        for mutate in (
            lambda r: r.update(kind='place'),
            lambda r: r['review'].update(confidence='certain'),
            lambda r: r['review'].update(status='accepted'),
            lambda r: r['occurrences'].reverse(),
            lambda r: r.update(occurrences=[]),
            lambda r: r.update(aiSummary='not part of this stage'),
        ):
            doc = self.document()
            mutate(doc['entities'][0])
            with self.assertRaises(ValueError):
                e.validate(self.bundle, doc)

    def test_exclusions_have_occurrences_and_do_not_partition_transcript(self):
        doc = self.document()
        doc['exclusions'] = [{'label': 'Routine gold', 'reason': 'Ordinary treasure.',
                              'occurrences': [{'source': e.scenes.source('u0005', 'u0005')}]}]
        self.assertEqual(e.validate(self.bundle, doc)['exclusions'], 1)
        self.assertIn('Excluded candidates', e.preview(self.bundle, doc))
        self.assertIn('Ordinary treasure.', e.preview(self.bundle, doc))
        missing_reason = copy.deepcopy(doc)
        del missing_reason['exclusions'][0]['reason']
        with self.assertRaisesRegex(ValueError, 'missing fields.*reason'):
            e.validate(self.bundle, missing_reason)
        doc['exclusions'][0]['occurrences'][0]['source'] = e.scenes.source('u0003', 'u0003')
        with self.assertRaisesRegex(ValueError, 'splits a polished turn'):
            e.validate(self.bundle, doc)

    def test_multiple_exclusion_occurrences_roundtrip_and_all_appear_in_preview(self):
        proposal = copy.deepcopy(self.proposal)
        proposal['exclusions'] = [{'label': 'Routine equipment', 'reason': 'Ordinary gear use.',
            'occurrences': [{'source': e.scenes.source('u0001', 'u0001')},
                            {'source': e.scenes.source('u0005', 'u0005')}]}]
        document = e.save(self.bundle, proposal)
        self.assertEqual(e.read_map(self.load())['exclusions'], proposal['exclusions'])
        preview = e.preview(self.bundle, document)
        exclusion_text = preview.split('## Excluded candidates', 1)[1]
        self.assertIn('u0001–u0001', exclusion_text)
        self.assertIn('u0005–u0005', exclusion_text)
        self.assertNotIn('source', document['exclusions'][0])

    def test_exclusion_occurrences_reject_empty_reversed_duplicate_and_old_shape(self):
        first = {'source': e.scenes.source('u0001', 'u0001')}
        last = {'source': e.scenes.source('u0005', 'u0005')}
        for refs in ([], None, [last, first], [first, first],
                     [{'source': e.scenes.source('u0002', 'u0004')},
                      {'source': e.scenes.source('u0004', 'u0005')}],
                     [{'source': e.scenes.source('u9999', 'u9999')}]):
            with self.subTest(occurrences=refs):
                doc = self.document()
                doc['exclusions'] = [{'label': 'Routine equipment', 'reason': 'Ordinary gear use.',
                                      'occurrences': refs}]
                with self.assertRaises(ValueError):
                    e.validate(self.bundle, doc)
        doc = self.document()
        doc['exclusions'] = [{'label': 'Routine equipment', 'reason': 'Ordinary gear use.',
                              'source': first['source']}]
        with self.assertRaisesRegex(ValueError, 'missing fields.*occurrences'):
            e.validate(self.bundle, doc)

    def test_preview_is_entity_first_with_evidence_only_on_request(self):
        doc = self.document()
        summary = e.preview(self.bundle, doc)
        self.assertIn('| e001 | Grash | npc |', summary)
        self.assertNotIn('DM: Grash greets', summary)
        detail = e.preview(self.bundle, doc, 'e001')
        self.assertIn('DM: Grash greets', detail)
        self.assertIn('u0001–u0001', detail)
        self.assertNotIn('Scene 1', detail)
        self.assertEqual(doc['entities'][0]['review']['status'], 'unreviewed')
        with self.assertRaisesRegex(ValueError, 'Unknown entity'):
            e.preview(self.bundle, doc, 'missing')

    def test_divine_identity_keeps_evidence_and_filters_separately(self):
        doc = self.document()
        divine = copy.deepcopy(doc['entities'][0])
        divine.update(id='e002', kind='divine', label='Spirit of the gate', note=None)
        doc['entities'].append(divine)
        e.validate(self.bundle, doc)
        gods = e.preview(self.bundle, doc, kind='divine')
        npcs = e.preview(self.bundle, doc, kind='npc')
        self.assertIn('| e002 | Spirit of the gate | divine |', gods)
        self.assertNotIn('| e001 | Grash |', gods)
        self.assertIn('| e001 | Grash | npc |', npcs)
        self.assertNotIn('| e002 |', npcs)
        self.assertIn('u0001–u0001', gods)
        self.assertNotIn('interaction', divine)
        self.assertEqual(divine['occurrences'], doc['entities'][0]['occurrences'])
        self.assertIn('Showing 0 item entities', e.preview(self.bundle, doc, kind='item'))
        with self.assertRaisesRegex(ValueError, 'Unknown entity kind filter'):
            e.preview(self.bundle, doc, kind='deity')


if __name__ == '__main__':
    unittest.main()
