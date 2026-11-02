import copy
import json
import unittest
from unittest.mock import patch
import test_entity_review as fixtures

api = fixtures.api


class EntityTableTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.EntityReviewTests()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        self.call = self.f.call

    def test_exclude_include_preserves_record_feedback_and_sources(self):
        proposal = copy.deepcopy(self.f.f.proposal)
        proposal['entities'][0].update(kind='item', identifiedLater=True, examinedInMirrorOfPast=True)
        api.maps.save(self.f.f.load(), proposal, self.call()['token']['mapSha256'])
        initial = self.call()
        original = copy.deepcopy(initial['document']['entities'][0])
        commented = self.call('entityFeedback', token=initial['token'], entity='e001', comment='Check inclusion.')
        excluded = self.call('entityUpdate', token=commented['token'], entity='e001', action='exclude', reason='Only a passing mention.')
        self.assertEqual(excluded['document']['entities'], [])
        self.assertEqual(excluded['document']['exclusions'][0]['occurrences'], original['occurrences'])
        self.assertTrue(excluded['exclusionDetails'][0]['restorable'])
        self.assertEqual(excluded['review']['history'][-1]['before'], original)
        passages = self.call('evidence', exclusionIndex=0, mapSha256=excluded['token']['mapSha256'])
        self.assertEqual(len(passages['passages']), len(original['occurrences']))
        inspected = self.call(notes=excluded['exclusionDetails'][0]['restoreNotes'])
        included = self.call('exclusionInclude', token=inspected['token'], exclusionIndex=0)
        self.assertEqual(included['document']['entities'][0], original)
        self.assertEqual(included['document']['exclusions'], [])
        self.assertEqual(included['review']['excludedRecords'], [])
        self.assertEqual(included['review']['feedback'][0]['entity'], 'e001')
        for path, content in self.f.source_before.items():
            self.assertEqual(path.read_bytes(), content)

    def test_restoring_a_reviewed_entity_requires_new_human_approval(self):
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        result = self.call('entityUpdate', token=result['token'], entity='e001', action='exclude', reason='Reconsider inclusion.')
        result = self.call(notes=result['exclusionDetails'][0]['restoreNotes'])
        result = self.call('exclusionInclude', token=result['token'], exclusionIndex=0)
        self.assertEqual(result['document']['entities'][0]['review']['status'], 'unreviewed')
        self.assertEqual(result['review']['history'][-1]['action'], 'include')

    def test_invalid_or_stale_moves_never_change_the_files(self):
        result = self.call()
        path = self.f.f.bundle['entityPath']
        before = path.read_bytes()
        for reason in ['', 'word ' * 41]:
            with self.assertRaises(ValueError):
                self.call('entityUpdate', token=result['token'], entity='e001', action='exclude', reason=reason)
            self.assertEqual(path.read_bytes(), before)
        moved = self.call('entityUpdate', token=result['token'], entity='e001', action='exclude', reason='Passing mention.')
        before = path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'Stale review'):
            self.call('exclusionInclude', token=result['token'], exclusionIndex=0)
        with self.assertRaisesRegex(ValueError, 'Unknown excluded'):
            self.call('exclusionInclude', token=moved['token'], exclusionIndex=-1)
        self.assertEqual(path.read_bytes(), before)

    def test_original_exclusion_requires_type_and_role_and_uses_a_fresh_id(self):
        original = self.call()['document']['entities'][0]
        proposal = copy.deepcopy(self.f.f.proposal)
        proposal['exclusions'] = [{'label': 'A sword', 'reason': 'Incidental.', 'occurrences': original['occurrences']}]
        api.maps.save(self.f.f.load(), proposal, self.call()['token']['mapSha256'])
        result = self.call()
        with self.assertRaisesRegex(ValueError, 'Choose an entity type and role'):
            self.call('exclusionInclude', token=result['token'], exclusionIndex=0)
        included = self.call('exclusionInclude', token=result['token'], exclusionIndex=0, kind='item', importance='cameo')
        row = included['document']['entities'][-1]
        self.assertEqual(row['id'], 'e002')
        self.assertEqual(row['kind'], 'item')
        self.assertEqual(row['importance'], 'cameo')
        self.assertEqual(row['review']['status'], 'unreviewed')
        self.assertEqual(row['occurrences'], original['occurrences'])

    def test_agent_regeneration_cannot_undo_a_human_exclusion(self):
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', action='exclude', reason='Not significant.')
        for proposal in [dict(entities=self.f.f.proposal['entities'], exclusions=result['document']['exclusions']),
                         dict(entities=[], exclusions=[])]:
            bundle = api.maps.load(self.f.f.fixture.yaml, self.f.f.fixture.vault, api.maps.note_refs(proposal))
            with self.assertRaisesRegex(ValueError, 'human-excluded'):
                api.maps.save(bundle, proposal, result['token']['mapSha256'])

    def test_exclusion_survives_interrupted_transaction(self):
        initial = self.call()
        original = api.scenes.atomic
        failed = False
        def interrupt(root, relative, data):
            nonlocal failed
            if str(relative).endswith('-entity-map.json') and not failed:
                failed = True
                raise OSError('Interrupted exclusion')
            return original(root, relative, data)
        with patch.object(api.scenes, 'atomic', interrupt):
            with self.assertRaises(OSError):
                self.call('entityUpdate', token=initial['token'], entity='e001', action='exclude', reason='Incidental mention.')
        recovered = self.call()
        self.assertEqual(recovered['document']['entities'], [])
        self.assertEqual(len(recovered['review']['excludedRecords']), 1)
        self.assertEqual(len(recovered['review']['history']), 1)
        self.assertTrue(recovered['exclusionDetails'][0]['restorable'])

    def test_session_header_links_use_existing_registered_paths_only(self):
        vault = self.f.f.fixture.vault
        scripts = vault / '_scripts'
        scripts.mkdir(exist_ok=True)
        registry = {'campaigns': {'demo': {'name': 'Demo', 'campaignRoot': 'Campaigns/Demo',
                                        'notePattern': 'Session {session_padded}.md'}}}
        (scripts / 'session_note_campaigns.json').write_text(json.dumps(registry), encoding='utf8')
        data = api.scenes.draft.yaml.safe_load(self.f.f.fixture.yaml.read_bytes())
        data.update(campaign='Demo', sessionNumber=1, realWorldDate='2026-05-14')
        self.f.f.fixture.yaml.write_text(api.scenes.draft.yaml.safe_dump(data), encoding='utf8')
        # Metadata changes require explicit confirmation before continuing.
        challenge = self.call()
        self.call('confirmSourceChanges', token=challenge['token'])
        bundle = self.f.f.load()
        api.maps.save(bundle, self.f.f.proposal, api.store.sha(self.f.f.bundle['entityPath'].read_bytes()))
        before = self.call()
        self.assertNotIn('sessionNotePath', before['session'])
        note = vault / 'Campaigns/Demo/Session 01.md'
        note.parent.mkdir(parents=True)
        note.write_text('# Session\n', encoding='utf8')
        metadata = self.call()['session']
        self.assertEqual(metadata['sessionNotePath'], 'Campaigns/Demo/Session 01.md')
        self.assertEqual(metadata['realWorldDate'], '2026-05-14')
        self.assertTrue((vault / metadata['transcriptPath']).is_file())

    def test_optional_bad_registry_cannot_turn_a_successful_save_into_an_error(self):
        scripts = self.f.f.fixture.vault / '_scripts'
        scripts.mkdir(exist_ok=True)
        (scripts / 'session_note_campaigns.json').write_text('not json', encoding='utf8')
        initial = self.call()
        self.assertIn('metadataWarning', initial['session'])
        changed = self.call('entityUpdate', token=initial['token'], entity='e001', changes={'status': 'humanReviewed'})
        self.assertEqual(changed['document']['entities'][0]['review']['status'], 'humanReviewed')
        self.assertEqual(self.call()['token'], changed['token'])

    def test_session_note_padding_matches_existing_vault_convention_and_aliases(self):
        vault = self.f.f.fixture.vault
        scripts = vault / '_scripts'
        scripts.mkdir(exist_ok=True)
        registry = {'campaigns': {'demo': {'name': 'Demo', 'aliases': ['Demo Campaign'],
                                         'campaignRoot': 'Campaigns/Demo',
                                         'notePattern': 'Session {session_padded}.md'}}}
        (scripts / 'session_note_campaigns.json').write_text(json.dumps(registry), encoding='utf8')
        for number, suffix in [(1, '01'), (12, '12'), (123, '123'), ('1.5', '01.5')]:
            with self.subTest(number=number):
                relative = f'Campaigns/Demo/Session {suffix}.md'
                note = vault / relative
                note.parent.mkdir(parents=True, exist_ok=True)
                note.write_text('# Session\n', encoding='utf8')
                bundle = dict(self.f.f.bundle, data={'campaign': 'Demo Campaign', 'sessionNumber': number})
                self.assertEqual(api.session_metadata(bundle)['sessionNotePath'], relative)
