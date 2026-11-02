import copy
import json
import unittest
from unittest.mock import patch
from test_entity_map import module, BASE
import test_entity_map as fixtures

api = module('entity_review', BASE / 'check-session-entities/scripts/entity_review.py')


class EntityReviewTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.EntityMapTests()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        api.maps.save(self.f.bundle, self.f.proposal)
        self.yaml = self.f.bundle['sessionYaml']
        self.source_before = {p: p.read_bytes() for p in (self.f.fixture.yaml, self.f.fixture.source, self.f.note)}

    def call(self, command='inspect', **fields):
        return api.dispatch({'sessionYaml': self.yaml, 'command': command, **fields}, self.f.fixture.vault)

    def test_inspect_does_not_write_and_evidence_is_uid_bound(self):
        result = self.call()
        self.assertFalse(api.store.review_path(self.f.bundle).exists())
        self.assertEqual(result['document']['entities'][0]['review']['status'], 'unreviewed')
        evidence = self.call('evidence', entity='e001', mapSha256=result['token']['mapSha256'])
        self.assertEqual(len(evidence['passages']), 2)
        self.assertIn('Grash', evidence['passages'][0]['text'])
        self.assertGreaterEqual(result['evidence']['e001'][0]['line'], 0)

    def test_human_edit_reason_comment_resolution_and_stale_token(self):
        initial = self.call()
        changed = self.call('entityUpdate', token=initial['token'], entity='e001', changes={'status': 'humanReviewed', 'importance': 'cameo'}, reason='Only mentioned.')
        self.assertEqual(changed['review']['history'][0]['before']['importance'], 'supporting')
        self.assertEqual(changed['review']['history'][0]['after']['importance'], 'cameo')
        self.assertEqual(changed['review']['history'][0]['reason'], 'Only mentioned.')
        with self.assertRaisesRegex(ValueError, 'Stale review'):
            self.call('entityUpdate', token=initial['token'], entity='e001', changes={'status': 'unreviewed'})
        commented = self.call('entityFeedback', token=changed['token'], entity='e001', comment='Recalibrate importance.')
        resolved = self.call('resolveFeedback', token=commented['token'], feedbackId='f000001', resolution='Updated importance guidance.')
        self.assertEqual(resolved['review']['feedback'][0]['status'], 'resolved')
        self.assertEqual(resolved['review']['feedback'][0]['record']['review']['status'], 'humanReviewed')
        self.assertEqual(resolved['document']['entities'][0]['review']['status'], 'humanReviewed')
        for path, data in self.source_before.items():
            self.assertEqual(path.read_bytes(), data)

    def test_link_change_requires_inspection_and_records_old_target(self):
        other = self.f.note.with_name('Other.md')
        other.write_text('# Other\n', encoding='utf-8')
        initial = self.call()
        with self.assertRaisesRegex(ValueError, 'Inspect new vault'):
            self.call('entityUpdate', token=initial['token'], entity='e001', changes={'note': 'People/Other.md'})
        inspected = self.call(notes=['People/Other.md'])
        changed = self.call('entityUpdate', token=inspected['token'], entity='e001', changes={'note': 'People/Other.md'})
        self.assertEqual(changed['review']['history'][0]['before']['note'], 'People/Grash.md')
        self.assertEqual(changed['document']['inputs']['vaultNotes'].keys(), {'People/Other.md'})
        self.assertEqual(self.call()['token'], changed['token'])

    def test_remove_preserves_record_and_feedback(self):
        result = self.call()
        result = self.call('entityFeedback', token=result['token'], entity='e001', comment='Routine ability.')
        result = self.call('entityUpdate', token=result['token'], entity='e001', action='remove', reason='No ongoing identity.')
        self.assertEqual(result['document']['entities'], [])
        self.assertEqual(result['review']['history'][-1]['before']['id'], 'e001')
        self.assertEqual(result['review']['feedback'][0]['status'], 'open')

    def test_interrupted_write_is_recovered_once(self):
        result = self.call()
        original = api.scenes.atomic
        failed = False
        def interrupt(root, relative, data):
            nonlocal failed
            if str(relative).endswith('-entity-map.json') and not failed:
                failed = True
                raise OSError('Simulated interruption')
            return original(root, relative, data)
        with patch.object(api.scenes, 'atomic', interrupt):
            with self.assertRaisesRegex(OSError, 'interruption'):
                self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        recovered = self.call()
        self.assertEqual(recovered['document']['entities'][0]['review']['status'], 'humanReviewed')
        self.assertEqual(len(recovered['review']['history']), 1)
        self.assertNotIn('transaction', recovered['review'])

    def test_regeneration_preserves_review_history_and_human_records(self):
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        proposal = copy.deepcopy(self.f.proposal)
        with self.assertRaisesRegex(ValueError, 'Preserve human-reviewed'):
            api.maps.save(self.f.load(), proposal, result['token']['mapSha256'])
        proposal['entities'][0]['review']['status'] = 'humanReviewed'
        api.maps.save(self.f.load(), proposal, result['token']['mapSha256'])
        self.assertEqual(self.call()['review']['history'][-1]['actor'], 'agent')

    def test_stale_sources_and_external_feedback_edits_fail_without_map_changes(self):
        result = self.call()
        result = self.call('entityFeedback', token=result['token'], comment='Missing someone?')
        path = api.store.review_path(self.f.bundle)
        path.write_bytes(path.read_bytes() + b'\n')
        before = self.f.bundle['entityPath'].read_bytes()
        with self.assertRaisesRegex(ValueError, 'Stale review'):
            self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        self.assertEqual(self.f.bundle['entityPath'].read_bytes(), before)
        self.f.fixture.source.write_bytes(self.f.fixture.source.read_bytes() + b'\n')
        with self.assertRaises(ValueError):
            self.call()

    def test_changed_note_requires_demotion_without_rewriting_human_decision(self):
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        self.f.note.write_text('# Grash with revised evidence\n', encoding='utf-8')
        proposal = copy.deepcopy(self.f.proposal)
        proposal['entities'][0]['review']['status'] = 'humanReviewed'
        with self.assertRaisesRegex(ValueError, 'reset to unreviewed'):
            api.maps.save(self.f.load(), proposal, result['token']['mapSha256'])
        proposal['entities'][0]['review']['status'] = 'unreviewed'
        api.maps.save(self.f.load(), proposal, result['token']['mapSha256'])
        self.assertEqual(self.call()['document']['entities'][0]['review']['status'], 'unreviewed')

    def test_regeneration_cannot_restore_a_human_removed_id(self):
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', action='remove')
        with self.assertRaisesRegex(ValueError, 'human-removed'):
            api.maps.save(self.f.load(), self.f.proposal, result['token']['mapSha256'])
