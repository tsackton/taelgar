import copy
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch
import test_entity_review as fixtures

api = fixtures.api


class EntityInputTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.EntityReviewTests()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        self.call = self.f.call
        self.path = self.f.f.bundle['entityPath']

    def change_transcript(self):
        path = self.f.f.fixture.source
        path.write_bytes(path.read_bytes().replace(b'Grash greets you', b'Grash welcomes you'))

    def test_vault_content_changes_leave_digest_token_and_human_status_unchanged(self):
        self.assertEqual(self.f.f.load(notes=())['entityInputDigest'], self.f.f.load()['entityInputDigest'])
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        self.f.f.note.write_bytes(b'# Revised Grash information\n')
        self.assertEqual(self.call()['token'], result['token'])
        changed = self.call('entityFeedback', token=result['token'], comment='A note changed.')
        self.assertEqual(changed['document']['entities'][0]['review']['status'], 'humanReviewed')
        self.assertNotIn('vaultNotes', changed['document']['inputs'])

    def test_legacy_vault_hashes_are_ignored_then_removed_on_guarded_save(self):
        doc = json.loads(self.path.read_bytes())
        doc['inputs']['vaultNotes'] = {'People/Grash.md': 'obsolete-sha', 'People/No-longer-consulted.md': 'irrelevant'}
        self.path.write_bytes(api.scenes.encoded(doc))
        self.f.f.note.write_bytes(b'# Updated\n')
        before = self.path.read_bytes()
        result = self.call()
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse(result.get('confirmationRequired'))
        changed = self.call('entityUpdate', token=result['token'], entity='e001', changes={'importance': 'cameo'})
        self.assertNotIn('vaultNotes', changed['document']['inputs'])

    def test_transcript_change_requires_exact_confirmation_and_records_history(self):
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        decisions = copy.deepcopy(result['document']['entities'])
        self.change_transcript()
        before = self.path.read_bytes()
        review_path = api.store.review_path(self.f.f.bundle)
        review_before = review_path.read_bytes()
        challenge = self.call()
        self.assertTrue(challenge['confirmationRequired'])
        self.assertTrue(challenge['sourceChanges'])
        self.assertEqual(self.path.read_bytes(), before)
        self.assertEqual(review_path.read_bytes(), review_before)
        with self.assertRaisesRegex(ValueError, 'confirm before continuing'):
            self.call('entityUpdate', token=result['token'], entity='e001', changes={'importance': 'cameo'})
        with self.assertRaisesRegex(ValueError, 'human confirmation'):
            api.maps.save(self.f.f.load(), self.f.f.proposal, result['token']['mapSha256'])
        source_before = self.f.f.fixture.source.read_bytes()
        confirmed = self.call('confirmSourceChanges', token=challenge['token'])
        self.assertEqual(confirmed['document']['entities'], decisions)
        self.assertEqual(confirmed['document']['inputs'], self.f.f.load()['entityInputs'])
        event = confirmed['review']['history'][-1]
        self.assertEqual((event['actor'], event['action']), ('human', 'confirmSourceChanges'))
        self.assertNotEqual(event['before']['inputs'], event['after']['inputs'])
        self.assertFalse(self.call().get('confirmationRequired'))
        self.assertEqual(self.f.f.fixture.source.read_bytes(), source_before)
        with self.assertRaisesRegex(ValueError, 'No transcript/session input changes'):
            self.call('confirmSourceChanges', token=confirmed['token'])

    def test_confirmation_rejects_sources_or_map_changed_after_prompt(self):
        self.change_transcript()
        challenge = self.call()
        self.f.f.fixture.source.write_bytes(self.f.f.fixture.source.read_bytes() + b'\n')
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'changed since confirmation'):
            self.call('confirmSourceChanges', token=challenge['token'])
        self.assertEqual(self.path.read_bytes(), before)
        challenge = self.call()
        self.path.write_bytes(self.path.read_bytes() + b'\n')
        with self.assertRaisesRegex(ValueError, 'changed since confirmation'):
            self.call('confirmSourceChanges', token=challenge['token'])

    def test_confirmation_does_not_bypass_invalid_uid_evidence(self):
        doc = json.loads(self.path.read_bytes())
        doc['entities'][0]['occurrences'][0]['source']['startUid'] = 'u9999'
        self.path.write_bytes(api.scenes.encoded(doc))
        self.change_transcript()
        challenge = self.call()
        before = self.path.read_bytes()
        with self.assertRaisesRegex(ValueError, 'unknown startUid'):
            self.call('confirmSourceChanges', token=challenge['token'])
        self.assertEqual(self.path.read_bytes(), before)
        self.assertFalse(api.store.review_path(self.f.f.bundle).exists())

    def test_note_changes_during_a_guarded_write_are_allowed(self):
        result = self.call()
        check = api.scenes.check_inputs
        def update_note(bundle):
            self.f.f.note.write_bytes(b'# Live note edit\n')
            check(bundle)
        with patch.object(api.scenes, 'check_inputs', update_note):
            changed = self.call('entityUpdate', token=result['token'], entity='e001', changes={'importance': 'cameo'})
        self.assertEqual(changed['document']['entities'][0]['importance'], 'cameo')

    def test_entity_confirmation_handles_outdated_yaml_source_sha_without_relaxing_other_readers(self):
        data = api.scenes.draft.yaml.safe_load(self.f.f.fixture.yaml.read_bytes())
        data['transcriptProcessing']['artifacts']['polishedMarkdown']['sha256'] = 'outdated-sha'
        self.f.f.fixture.yaml.write_bytes(api.scenes.draft.yaml.safe_dump(data).encode('utf8'))
        self.change_transcript()
        challenge = self.call()
        confirmed = self.call('confirmSourceChanges', token=challenge['token'])
        self.assertFalse(confirmed.get('confirmationRequired'))
        self.assertFalse(self.call().get('confirmationRequired'))
        with self.assertRaisesRegex(ValueError, 'YAML fingerprint'):
            api.scenes.load(self.f.f.fixture.yaml, self.f.f.fixture.vault)

    def test_cli_inspection_and_confirmation_use_current_digest_and_expected_map_hash(self):
        self.change_transcript()
        scripts = Path(api.__file__).parent
        cli = """import sys
from pathlib import Path
sys.path.insert(0, sys.argv.pop(1))
import entity_map
vault = Path(sys.argv.pop(1))
load = entity_map.load
entity_map.load = lambda session_yaml, notes=(): load(session_yaml, vault, notes)
entity_map.main()
"""
        prefix = [sys.executable, '-X', 'utf8', '-B', '-c', cli, str(scripts),
                  str(self.f.f.fixture.vault), '--session-yaml', str(self.f.f.fixture.yaml)]
        result = subprocess.run(prefix + ['inspect'], capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr.decode())
        inspected = json.loads(result.stdout)
        self.assertTrue(inspected['sourceChanges'])
        self.assertIsInstance(inspected['notes'], list)
        before = self.path.read_bytes()
        bad = subprocess.run(prefix + ['confirm-sources', '--expect-input-digest', 'wrong',
                              '--expect-sha256', inspected['mapSha256']], capture_output=True)
        self.assertNotEqual(bad.returncode, 0)
        self.assertEqual(self.path.read_bytes(), before)
        good = subprocess.run(prefix + ['confirm-sources', '--expect-input-digest', inspected['inputDigest'],
                               '--expect-sha256', inspected['mapSha256']], capture_output=True)
        self.assertEqual(good.returncode, 0, good.stderr.decode())
        self.assertFalse(self.call().get('confirmationRequired'))


if __name__ == '__main__':
    unittest.main()
