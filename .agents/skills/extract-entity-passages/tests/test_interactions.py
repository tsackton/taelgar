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


m = module('interactions', BASE / 'extract-entity-passages/scripts/interactions.py')
fixtures = module('entity_fixtures', BASE / 'check-session-entities/tests/test_entity_map.py')


class InteractionTests(unittest.TestCase):
    def setUp(self):
        fixture = fixtures.EntityMapTests()
        fixture.setUp()
        self.addCleanup(fixture.doCleanups)
        self.fixture = fixture
        bundle = fixture.bundle
        # Save only inside the isolated fixture vault, not the real session tree.
        m.entity_map.save(bundle, fixture.proposal)
        self.vault = fixture.fixture.vault
        text = ''.join(turn['raw'] for turn in bundle['turns'][1:4])
        text = text.replace('PC: I roll a 12.', '((Dice roll))')
        self.document = {
            'schemaVersion': 1, 'sessionYaml': bundle['sessionYaml'],
            'inputs': {
                'transcript': {'sourceId': m.scenes.draft.SOURCE_ID,
                               'sha256': bundle['sourceSha256']},
                'entityMap': {'path': bundle['entityPath'].relative_to(self.vault).as_posix(),
                              'sha256': m.scenes.draft.sha(bundle['entityPath'].read_bytes())}},
            'interactions': [{
                'id': 'i001', 'title': 'Grash welcomes the party',
                'entities': [{'id': 'e001', 'role': 'star', 'action': 'interacted'}],
                'source': {'startUid': 'u0002', 'endUid': 'u0004'},
                'lines': text.splitlines(),
                'reviewContext': {
                    'before': ['DM: Last time Grash escaped.'],
                    'after': ['PC: We reach the mountain shrine.',
                              'DM: Afterwards: the old king also used this hall.']},
                'review': {'confidence': 'high', 'status': 'unreviewed'}}]}

    def validate(self, document=None):
        return m.validate(self.document if document is None else document, self.vault)

    def test_valid_exchange_preserves_inputs_and_needs_no_scene_map(self):
        paths = [self.fixture.fixture.yaml, self.fixture.fixture.source,
                 self.fixture.bundle['entityPath']]
        before = {p: p.read_bytes() for p in paths}
        result = self.validate()
        self.assertEqual(result['interactions'], 1)
        self.assertIn('not established', result['semanticReview'])
        self.assertEqual(before, {p: p.read_bytes() for p in paths})
        self.assertFalse(self.fixture.bundle['mapPath'].exists())
        self.assertFalse(self.fixture.bundle['draft'].exists())
        # Local star status did not change the map's supporting session importance.
        self.assertEqual(json.loads(paths[-1].read_bytes())['entities'][0]['importance'], 'supporting')

    def test_conditional_review_reason(self):
        for confidence in ('low', 'medium'):
            self.document['interactions'][0]['review']['confidence'] = confidence
            for reason in (None, '', '   ', 'Two\nlines'):
                row = copy.deepcopy(self.document)
                if reason is not None:
                    row['interactions'][0]['review']['reason'] = reason
                with self.assertRaises(m.jsonschema.ValidationError):
                    self.validate(row)
            self.document['interactions'][0]['review']['reason'] = 'The speaker attribution is ambiguous.'
            self.validate()
            del self.document['interactions'][0]['review']['reason']
        self.document['interactions'][0]['review'] = {'confidence': 'high', 'status': 'unreviewed'}
        self.validate()
        self.document['interactions'][0]['review']['reason'] = 'Boundaries were checked against the source.'
        self.validate()
        del self.document['interactions'][0]['review']
        self.validate()

    def test_no_star_duplicate_or_unknown_entities(self):
        row = self.document['interactions'][0]
        for entries, error in (
            ([{'id': 'e001', 'role': 'supporting', 'action': 'present'}], m.jsonschema.ValidationError),
            (row['entities'] * 2, ValueError),
            ([{'id': 'e999', 'role': 'star', 'action': 'mentioned'}], ValueError)):
            document = copy.deepcopy(self.document)
            document['interactions'][0]['entities'] = entries
            with self.assertRaises(error):
                self.validate(document)

    def test_multiple_stars_can_share_one_exchange(self):
        bundle = self.fixture.bundle
        mapped = json.loads(bundle['entityPath'].read_bytes())
        second = copy.deepcopy(mapped['entities'][0])
        second.update(id='e002', label='Another guide')
        second.pop('note')
        mapped['entities'].append(second)
        bundle['entityPath'].write_text(json.dumps(mapped), encoding='utf-8')
        self.document['inputs']['entityMap']['sha256'] = m.scenes.draft.sha(bundle['entityPath'].read_bytes())
        self.document['interactions'][0]['entities'].append(
            {'id': 'e002', 'role': 'star', 'action': 'mentioned'})
        self.validate()

    def test_stale_provenance_and_cross_session_paths_fail(self):
        for target in ('transcript', 'entityMap'):
            document = copy.deepcopy(self.document)
            document['inputs'][target]['sha256'] = '0' * 64
            with self.assertRaisesRegex(ValueError, 'hash differs'):
                self.validate(document)
        self.document['inputs']['entityMap']['path'] = '../outside.json'
        with self.assertRaises(ValueError):
            self.validate()

    def test_whole_turn_uid_bounds_and_span_accounting(self):
        for source in (
            {'startUid': 'u0003', 'endUid': 'u0004'},
            {'startUid': 'u0002', 'endUid': 'u0002'},
            {'startUid': 'u0004', 'endUid': 'u0002'},
            {'startUid': 'u9999', 'endUid': 'u9999'}):
            document = copy.deepcopy(self.document)
            document['interactions'][0]['source'] = source
            with self.assertRaises(ValueError):
                self.validate(document)
        lines = self.document['interactions'][0]['lines']
        lines.remove('%% u0004:0-5 %%')
        with self.assertRaisesRegex(ValueError, 'source spans differ'):
            self.validate()

    def test_continuous_cut_preserves_all_spans_under_one_label(self):
        row = self.document['interactions'][0]
        blocks = self.fixture.bundle['turns'][1:4]
        comments = [turn['raw'].splitlines()[0] for turn in blocks]
        label = '((The battle))'
        row['lines'] = [comments[0], label, comments[1], label, comments[2], label]
        with self.assertRaisesRegex(ValueError, 'combine adjacent identical cut labels'):
            self.validate()
        spans = ', '.join(comment[3:-3] for comment in comments)
        row['lines'] = [f'%% {spans} %%', label]
        self.validate()
        row['lines'] = [comments[0], label, *blocks[1]['raw'].splitlines(), comments[2], label]
        self.validate()

    def test_duplicate_interactions_and_source_order(self):
        self.document['interactions'] *= 2
        with self.assertRaisesRegex(ValueError, 'Duplicate interaction'):
            self.validate()
        self.document['interactions'] = [copy.deepcopy(x) for x in self.document['interactions']]
        first = self.document['interactions'][0]
        first.update(id='i002', source={'startUid': 'u0005', 'endUid': 'u0005'},
                     lines=self.fixture.bundle['turns'][4]['raw'].splitlines(),
                     reviewContext=m.review_context(self.fixture.bundle, 4, 4))
        with self.assertRaisesRegex(ValueError, 'source order'):
            self.validate()

    def test_physical_lines_and_unknown_fields(self):
        for value in ('One\nTwo', 'One\rTwo'):
            document = copy.deepcopy(self.document)
            document['interactions'][0]['lines'].append(value)
            with self.assertRaises(m.jsonschema.ValidationError):
                self.validate(document)
        self.document['interactions'][0]['framing'] = 'Retired metadata'
        with self.assertRaises(m.jsonschema.ValidationError):
            self.validate()

    def test_empty_collection_is_valid_without_claiming_coverage(self):
        self.document['interactions'] = []
        result = self.validate()
        self.assertEqual(result['interactions'], 0)
        self.assertIn('completeness is not established', result['coverage'])

    def test_review_context_requires_exact_adjacent_lines(self):
        for change in (
            lambda context: context['before'].clear(),
            lambda context: context['after'].reverse(),
            lambda context: context['after'].__setitem__(0, 'PC: Invented wording.'),
            lambda context: context['before'].append('DM: Grash greets you at the gate.'),
        ):
            document = copy.deepcopy(self.document)
            change(document['interactions'][0]['reviewContext'])
            with self.assertRaisesRegex(ValueError, 'reviewContext differs'):
                self.validate(document)
        document = copy.deepcopy(self.document)
        del document['interactions'][0]['reviewContext']
        with self.assertRaises(m.jsonschema.ValidationError):
            self.validate(document)

    def test_context_limit_counts_nonblank_physical_lines(self):
        bundle = {'positions': {f'u{i:04}': i for i in range(13)}, 'turns': [
            {'spans': [(f'u{i:04}', 0, 10)],
             'body': f'DM: Line {i}a.\n\nContinuation {i}b.\n\n'} for i in range(13)]}
        context = m.review_context(bundle, 6, 6)
        self.assertEqual(context['before'], [
            'Continuation 3b.', 'DM: Line 4a.', 'Continuation 4b.',
            'DM: Line 5a.', 'Continuation 5b.'])
        self.assertEqual(context['after'], [
            'DM: Line 7a.', 'Continuation 7b.', 'DM: Line 8a.',
            'Continuation 8b.', 'DM: Line 9a.'])
        self.assertEqual(m.review_context(bundle, 0, 12), {'before': [], 'after': []})

    def test_review_context_cannot_store_blank_or_multiline_entries(self):
        for value in ('', '   ', 'First\nSecond'):
            document = copy.deepcopy(self.document)
            document['interactions'][0]['reviewContext']['before'] = [value]
            with self.assertRaises(m.jsonschema.ValidationError):
                self.validate(document)
        document = copy.deepcopy(self.document)
        document['interactions'][0]['reviewContext']['before'] = ['DM: Extra.'] * 6
        with self.assertRaises(m.jsonschema.ValidationError):
            self.validate(document)

    def test_schema_definition_and_cli(self):
        schema = json.loads(m.SCHEMA.read_text(encoding='utf-8'))
        m.jsonschema.Draft202012Validator.check_schema(schema)
        proposal = self.vault / 'trial.json'
        proposal.write_text(json.dumps(self.document), encoding='utf-8')
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1')
        command = [sys.executable, '-B', str(BASE / 'extract-entity-passages/scripts/interactions.py'),
                   'validate', str(proposal), '--vault-root', str(self.vault)]
        result = subprocess.run(command, capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['interactions'], 1)
        context_command = [sys.executable, '-B', str(BASE / 'extract-entity-passages/scripts/interactions.py'),
                           'context', '--session-yaml', self.document['sessionYaml'],
                           '--start-uid', 'u0002', '--end-uid', 'u0004',
                           '--vault-root', str(self.vault)]
        result = subprocess.run(context_command, capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout), self.document['interactions'][0]['reviewContext'])
        self.document['interactions'][0]['review']['confidence'] = 'medium'
        proposal.write_text(json.dumps(self.document), encoding='utf-8')
        result = subprocess.run(command, capture_output=True, text=True, env=env)
        self.assertEqual(result.returncode, 1)
        self.assertIn('reason', result.stderr)

    def test_source_or_yaml_changes_require_map_confirmation(self):
        for path in (self.fixture.fixture.source, self.fixture.fixture.yaml):
            original = path.read_bytes()
            # YAML is fingerprinted semantically by the shared map reader;
            # whitespace-only YAML edits intentionally do not stale a map.
            change = b'\ncampaign: Changed campaign\n' if path.suffix == '.yaml' else b'\n'
            path.write_bytes(original + change)
            try:
                with self.assertRaisesRegex(ValueError, 'inputs changed'):
                    self.validate()
            finally:
                path.write_bytes(original)


if __name__ == '__main__':
    unittest.main()
