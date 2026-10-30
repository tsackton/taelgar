import copy
import importlib.util
import json
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


m = module('session_model_v7', BASE / 'check-session-entities/scripts/session_model.py')
fixture = module('scene_fixture_v7', BASE / 'map-transcript-scenes/tests/test_scene_map.py')


class SessionModelTests(unittest.TestCase):
    def setUp(self):
        self.f = fixture.SceneMapTests()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        self.doc = {'schemaVersion': 7, 'sessionYaml': self.f.bundle['sessionYaml'],
                    'scenes': copy.deepcopy(self.f.proposal['scenes']),
                    'contextBlocks': [dict(index=i, **copy.deepcopy(row)) for i, row in
                                      enumerate(self.f.proposal['contextBlocks'], 1)],
                    'entities': [{'id': 'e1', 'kind': 'divine', 'label': 'The old king'}],
                    'interactions': [{'id': 'i1', 'entity': 'e1', 'contexts': [2], 'interaction': 'mentioned',
                                      'passages': [{'source': m.scenes.source('u0006', 'u0006')}]}]}

    def check(self, doc=None, complete=True):
        return m.validate(self.doc if doc is None else doc, self.f.vault, require_coverage=complete)

    def test_divine_context_only_mention_has_no_invented_scene(self):
        result = self.check()
        self.assertEqual(result['unaccountedUids'], 0)
        self.assertEqual(result['contextBlocks'], 2)
        self.assertFalse(result['publicationReady'])
        self.assertNotIn('scenes', self.doc['interactions'][0])

    def test_context_cannot_establish_presence_or_direct_exchange(self):
        for kind in ('interacted', 'observed', 'present'):
            doc = copy.deepcopy(self.doc)
            doc['interactions'][0]['interaction'] = kind
            with self.assertRaises((ValueError, m.jsonschema.ValidationError)):
                self.check(doc)
            doc['interactions'][0]['scenes'] = [1]
            with self.assertRaises((ValueError, m.jsonschema.ValidationError)):
                self.check(doc)

    def test_direct_divine_encounter_is_allowed_with_played_scene(self):
        self.doc['interactions'][0].update(scenes=[1], interaction='interacted')
        del self.doc['interactions'][0]['contexts']
        self.doc['interactions'][0]['passages'][0]['source'] = m.scenes.source('u0002', 'u0004')
        self.check()

    def test_requires_at_least_one_valid_anchor(self):
        for refs in ({}, {'scenes': []}, {'contexts': []}, {'scenes': [99]}, {'contexts': [99]}):
            doc = copy.deepcopy(self.doc)
            row = doc['interactions'][0]
            row.pop('contexts')
            row.update(refs)
            with self.assertRaises((ValueError, m.jsonschema.ValidationError)):
                self.check(doc)

    def test_duplicate_indexes_and_cross_collection_overlap_fail(self):
        for mutation in (
            lambda d: d['contextBlocks'][1].update(index=1),
            lambda d: d['scenes'].append(copy.deepcopy(d['scenes'][0])),
            lambda d: d['contextBlocks'][1].update(source=m.scenes.source('u0005', 'u0006')),
        ):
            doc = copy.deepcopy(self.doc)
            mutation(doc)
            with self.assertRaises(ValueError):
                self.check(doc)

    def test_passage_cannot_cross_unreferenced_scenes_or_split_turn(self):
        for ref in (m.scenes.source('u0002', 'u0004'), m.scenes.source('u0003', 'u0003')):
            doc = copy.deepcopy(self.doc)
            doc['interactions'][0]['passages'][0]['source'] = ref
            with self.assertRaises(ValueError):
                self.check(doc)

    def test_verbatim_quotes_and_featured_quote_ownership(self):
        row = self.doc['interactions'][0]
        row['quotes'] = [{'id': 'q1', 'type': 'whole', 'text': 'the old king also used this hall.',
                          'source': m.scenes.source('u0006', 'u0006')}]
        self.doc['entities'][0]['aiSuggestedFeaturedQuotes'] = ['q1']
        self.check()
        row['quotes'][0]['text'] = 'The old king personally greets you.'
        with self.assertRaisesRegex(ValueError, 'verbatim'):
            self.check()
        row['quotes'][0]['text'] = 'the old king also used this hall.'
        self.doc['entities'].append({'id': 'e2', 'kind': 'npc', 'label': 'Grash',
                                     'aiSuggestedFeaturedQuotes': ['q1']})
        with self.assertRaisesRegex(ValueError, 'does not belong'):
            self.check()

    def test_minimal_valid_candidate_does_not_claim_complete(self):
        doc = {'schemaVersion': 7, 'sessionYaml': self.f.bundle['sessionYaml']}
        self.assertEqual(self.check(doc, complete=False)['unaccountedUids'], 6)
        with self.assertRaisesRegex(ValueError, 'coverage incomplete'):
            self.check(doc)

    def test_old_version_and_duplicate_yaml_metadata_rejected(self):
        for fields in ({'schemaVersion': 6}, {'pcs': []}, {'campaign': 'Demo'}, {'sources': []}):
            doc = dict(self.doc, **fields)
            with self.assertRaises(m.jsonschema.ValidationError):
                self.check(doc)

    def test_schema_is_well_formed_and_unknown_paths_are_null_not_empty(self):
        m.jsonschema.Draft202012Validator.check_schema(json.loads(m.SCHEMA.read_text(encoding='utf-8')))
        self.doc['entities'][0]['note'] = None
        self.doc['scenes'][0]['location'] = None
        self.check()
        for row, field in ((self.doc['entities'][0], 'note'), (self.doc['scenes'][0], 'location')):
            row[field] = ''
            with self.assertRaises(m.jsonschema.ValidationError):
                self.check()
            row[field] = None

    def test_quote_outside_anchors_and_broken_entity_rejected(self):
        self.doc['interactions'][0]['entity'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Broken entity'):
            self.check()
        self.doc['interactions'][0]['entity'] = 'e1'
        self.doc['interactions'][0]['quotes'] = [{'id': 'q1', 'type': 'whole', 'text': 'We enter the hall.',
                                                'source': m.scenes.source('u0005', 'u0005')}]
        with self.assertRaisesRegex(ValueError, 'outside interaction'):
            self.check()

    def test_projection_preserves_divine_ids_and_context_without_writes(self):
        note = self.f.vault / 'Gods/Eran.md'
        note.parent.mkdir()
        note.write_text('# Eran\nThe old king was Eran.\n', encoding='utf-8')
        b = m.entities.load(self.f.yaml, self.f.vault, notes=['Gods/Eran.md'])
        m.entities.save(b, {'entities': [{
            'id': 'e1', 'kind': 'divine', 'label': 'The old king', 'note': 'Gods/Eran.md',
            'identifiedLater': True, 'reason': 'Later material identifies the old king as Eran.',
            'occurrences': [{'source': m.scenes.source('u0006', 'u0006')}],
            'review': {'confidence': 'high', 'status': 'unreviewed'}}]})
        # Entities can be completed first; projection separately requires scenes.
        with self.assertRaises(FileNotFoundError):
            m.project(self.f.yaml, self.f.vault)
        m.scenes.save(self.f.bundle, self.f.proposal)
        before = {p: p.read_bytes() for p in self.f.root.rglob('*') if p.is_file()}
        doc = m.project(self.f.yaml, self.f.vault)
        self.assertEqual(doc['entities'][0]['kind'], 'divine')
        self.assertEqual(doc['entities'][0]['id'], 'e1')
        self.assertEqual(doc['entities'][0]['label'], 'The old king')
        self.assertEqual(doc['entities'][0]['note'], 'Gods/Eran.md')
        self.assertNotIn('identifiedLater', doc['entities'][0])
        self.assertNotIn('occurrences', doc['entities'][0])
        self.assertNotIn('interactions', doc)
        self.assertNotIn('review', doc)
        self.assertEqual(len(doc['contextBlocks']), 2)
        self.assertEqual(before, {p: p.read_bytes() for p in self.f.root.rglob('*') if p.is_file()})
        scene_path = self.f.bundle['mapPath']
        scene_doc = json.loads(scene_path.read_text(encoding='utf-8'))
        scene_doc['inputs']['sessionYamlDigest'] = 'stale'
        scene_path.write_text(json.dumps(scene_doc), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Map inputs changed'):
            m.project(self.f.yaml, self.f.vault)
        self.assertEqual(m.entities.read_map(b)['entities'][0]['id'], 'e1')


if __name__ == '__main__':
    unittest.main()
