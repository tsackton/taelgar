import copy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
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

    def test_scene_time_endpoints_are_optional_and_legacy_time_is_rejected(self):
        scene = self.doc['scenes'][0]
        for fields in ({'timeStart': 'After breakfast'}, {'timeEnd': 'After sunset'},
                       {'timeStart': None, 'timeEnd': None}):
            scene.pop('timeStart', None)
            scene.pop('timeEnd', None)
            scene.update(fields)
            self.check()
        scene['timeStart'] = ''
        with self.assertRaises(m.jsonschema.ValidationError):
            self.check()
        scene['timeStart'] = None
        scene['time'] = 'Afternoon to evening'
        with self.assertRaises(m.jsonschema.ValidationError):
            self.check()

    def test_quote_outside_anchors_and_broken_entity_rejected(self):
        self.doc['interactions'][0]['entity'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'Broken entity'):
            self.check()
        self.doc['interactions'][0]['entity'] = 'e1'
        self.doc['interactions'][0]['quotes'] = [{'id': 'q1', 'type': 'whole', 'text': 'We reach the mountain shrine.',
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
            'identifiedLater': True,
            'occurrences': [{'source': m.scenes.source('u0006', 'u0006')}],
            'review': {'confidence': 'high', 'status': 'unreviewed'}}]})
        # Entities can be completed first; projection separately requires scenes.
        with self.assertRaises(FileNotFoundError):
            m.project(self.f.yaml, self.f.vault)
        self.f.proposal['scenes'][0].update(timeStart='After breakfast', timeEnd='Before noon')
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
        self.assertEqual(doc['sceneReview'], self.f.proposal['review'])
        self.assertEqual(doc['scenes'][0]['timeStart'], 'After breakfast')
        self.assertEqual(doc['scenes'][0]['timeEnd'], 'Before noon')
        self.assertNotIn('time', doc['scenes'][0])
        self.assertEqual(len(doc['contextBlocks']), 2)
        self.assertEqual(before, {p: p.read_bytes() for p in self.f.root.rglob('*') if p.is_file()})
        scene_path = self.f.bundle['mapPath']
        scene_doc = json.loads(scene_path.read_text(encoding='utf-8'))
        scene_doc['schemaVersion'] = 1
        del scene_doc['review']
        scene_doc['scenes'][0].pop('timeStart')
        scene_doc['scenes'][0].pop('timeEnd')
        scene_path.write_text(json.dumps(scene_doc), encoding='utf-8')
        legacy_projection = m.project(self.f.yaml, self.f.vault)
        self.assertNotIn('sceneReview', legacy_projection)
        scene_doc['scenes'][0]['time'] = 'After breakfast through noon'
        scene_path.write_text(json.dumps(scene_doc), encoding='utf-8')
        before_legacy = scene_path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'Legacy scene.time needs evidence-based'):
            m.project(self.f.yaml, self.f.vault)
        self.assertEqual(scene_path.read_bytes(), before_legacy)
        scene_doc['inputs']['sessionYamlDigest'] = 'stale'
        scene_path.write_text(json.dumps(scene_doc), encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Map inputs changed'):
            m.project(self.f.yaml, self.f.vault)
        self.assertEqual(m.entities.read_map(b)['entities'][0]['id'], 'e1')

    def test_cli_json_round_trip_uses_utf8_under_a_non_utf8_locale(self):
        label = 'Gräsh Δ'
        proposal = {'entities': [{'id': 'e1', 'kind': 'npc', 'label': label,
                     'occurrences': [{'source': m.scenes.source('u0002', 'u0004')}],
                     'review': {'confidence': 'high', 'status': 'unreviewed'}}]}
        proposal_path = self.f.root / 'proposal.json'
        proposal_path.write_text(json.dumps(proposal, ensure_ascii=False), encoding='utf-8')
        scripts = BASE / 'check-session-entities/scripts'
        env = dict(os.environ, PYTHONUTF8='0', PYTHONCOERCECLOCALE='0',
                   LC_ALL='C', PYTHONIOENCODING='utf-8')
        # Select the synthetic vault while exercising real CLI file IO in a new process.
        save_cli = '''import sys
from pathlib import Path
sys.path.insert(0, sys.argv.pop(1))
import entity_map
vault = Path(sys.argv.pop(1))
load = entity_map.load
entity_map.load = lambda session_yaml, notes=(): load(session_yaml, vault, notes)
entity_map.main()
'''
        digest = m.entities.load(self.f.yaml, self.f.vault)['entityInputDigest']
        result = subprocess.run([sys.executable, '-B', '-c', save_cli, str(scripts), str(self.f.vault),
            '--session-yaml', str(self.f.yaml), 'save', '--proposal', str(proposal_path),
            '--expect-input-digest', digest], env=env, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode('utf-8'))
        saved = m.entities.read_map(m.entities.load(self.f.yaml, self.f.vault))
        self.assertEqual(saved['entities'][0]['label'], label)
        candidate = self.f.root / 'candidate.json'
        candidate.write_text(json.dumps({'schemaVersion': 7, 'sessionYaml': self.f.bundle['sessionYaml'],
                             'entities': [{'id': 'e1', 'kind': 'npc', 'label': label}]},
                             ensure_ascii=False), encoding='utf-8')
        check_cli = '''import sys
from pathlib import Path
sys.path.insert(0, sys.argv.pop(1))
import session_model
vault = Path(sys.argv.pop(1))
validate = session_model.validate
session_model.validate = lambda doc, require_coverage=False: validate(doc, vault, require_coverage)
session_model.main()
'''
        result = subprocess.run([sys.executable, '-B', '-c', check_cli, str(scripts), str(self.f.vault),
                                 'validate', str(candidate)], env=env, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode('utf-8'))
        self.assertEqual(json.loads(result.stdout)['entities'], 1)


if __name__ == '__main__':
    unittest.main()
