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
        e.scenes.save(f.bundle, f.proposal)
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

    def test_reuses_source_and_derives_scene_vs_recap(self):
        doc = self.document()
        self.assertEqual(e.validate(self.bundle, doc)['entities'], 1)
        self.assertEqual(e.owner(self.bundle, doc['entities'][0]['occurrences'][0]['source']), 'recap u0001')
        self.assertEqual(e.owner(self.bundle, doc['entities'][0]['occurrences'][1]['source']), 'Scene 1')
        self.assertNotIn('pcs', doc)
        self.assertNotIn('scenes', doc)

    def test_cross_scene_and_partial_turn_ranges_rejected(self):
        for start, end in [('u0001', 'u0004'), ('u0003', 'u0004'), ('u0002', 'u0005'), ('u0009', 'u0009')]:
            doc = self.document()
            doc['entities'][0]['occurrences'] = [{'source': e.scenes.source(start, end)}]
            with self.assertRaises(ValueError):
                e.validate(self.bundle, doc)

    def test_unlinked_high_confidence_identity_is_allowed_with_reason(self):
        p = copy.deepcopy(self.proposal)
        row = p['entities'][0]
        del row['note']
        row['label'] = 'Unnamed camp spokesman'
        row['reason'] = 'Distinct individual; no suitable page in searched camp references.'
        doc = e.build(self.load(notes=()), p)
        self.assertEqual(e.validate(self.load(notes=()), doc)['matched'], 0)
        del row['reason']
        with self.assertRaisesRegex(ValueError, 'need a reason'):
            e.build(self.load(notes=()), p)

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
        row['reason'] = 'Similar name, but the role is ambiguous.'
        self.assertEqual(e.validate(self.bundle, e.build(self.bundle, p))['reviewPriority'], ['e001'])
        row['note'] = 'People/Grash.md'
        with self.assertRaisesRegex(ValueError, 'not both'):
            e.build(self.bundle, p)

    def test_source_and_scene_changes_invalidate_review(self):
        doc = self.document()
        scene_path = self.bundle['mapPath']
        scene_path.write_text(scene_path.read_text(encoding='utf-8') + '\n', encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(ValueError, 'inputs changed'):
            e.validate(self.load(), doc)
        with self.assertRaisesRegex(ValueError, 'Scene map changed'):
            e.save(self.bundle, self.proposal)

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

    def test_exclusions_have_source_and_do_not_partition_transcript(self):
        doc = self.document()
        doc['exclusions'] = [{'label': 'Routine gold', 'reason': 'Ordinary treasure.',
                              'source': e.scenes.source('u0005', 'u0005')}]
        self.assertEqual(e.validate(self.bundle, doc)['exclusions'], 1)
        self.assertIn('Excluded candidates', e.preview(self.bundle, doc))
        self.assertIn('Ordinary treasure.', e.preview(self.bundle, doc))

    def test_preview_is_entity_first_with_evidence_only_on_request(self):
        doc = self.document()
        summary = e.preview(self.bundle, doc)
        self.assertIn('| e001 | Grash | npc |', summary)
        self.assertNotIn('DM: Grash greets', summary)
        detail = e.preview(self.bundle, doc, 'e001')
        self.assertIn('DM: Grash greets', detail)
        self.assertIn('recap u0001', detail)
        self.assertEqual(doc['entities'][0]['review']['status'], 'unreviewed')
        with self.assertRaisesRegex(ValueError, 'Unknown entity'):
            e.preview(self.bundle, doc, 'missing')

    def test_divine_identity_keeps_evidence_and_filters_separately(self):
        doc = self.document()
        divine = copy.deepcopy(doc['entities'][0])
        divine.update(id='e002', kind='divine', label='Spirit of the gate', note=None,
                      reason='Named religious spirit; no individual vault page.')
        doc['entities'].append(divine)
        e.validate(self.bundle, doc)
        gods = e.preview(self.bundle, doc, kind='divine')
        npcs = e.preview(self.bundle, doc, kind='npc')
        self.assertIn('| e002 | Spirit of the gate | divine |', gods)
        self.assertNotIn('| e001 | Grash |', gods)
        self.assertIn('| e001 | Grash | npc |', npcs)
        self.assertNotIn('| e002 |', npcs)
        self.assertIn('recap u0001', gods)
        self.assertNotIn('interaction', divine)
        self.assertEqual(divine['occurrences'], doc['entities'][0]['occurrences'])
        self.assertIn('Showing 0 item entities', e.preview(self.bundle, doc, kind='item'))
        with self.assertRaisesRegex(ValueError, 'Unknown entity kind filter'):
            e.preview(self.bundle, doc, kind='deity')


if __name__ == '__main__':
    unittest.main()
