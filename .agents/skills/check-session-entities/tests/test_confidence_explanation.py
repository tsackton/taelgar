import copy
import unittest
import test_entity_review as fixtures

api = fixtures.api


class ConfidenceExplanationTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.EntityReviewTests()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        self.call = self.f.call

    def save(self, proposal):
        bundle = self.f.f.load()
        return api.maps.save(bundle, proposal, api.store.sha(bundle['entityPath'].read_bytes()))

    def test_new_medium_and_low_agent_decisions_require_a_short_explanation(self):
        path = self.f.f.bundle['entityPath']
        for rating in ['medium', 'low']:
            proposal = copy.deepcopy(self.f.f.proposal)
            proposal['entities'][0]['review']['confidence'] = rating
            before = path.read_bytes()
            with self.assertRaisesRegex(ValueError, 'require confidenceExplanation'):
                self.save(proposal)
            self.assertEqual(path.read_bytes(), before)
            proposal['entities'][0]['confidenceExplanation'] = 'The identity fits, but the source does not distinguish another plausible guide.'
            result = self.save(proposal)
            self.assertEqual(result['entities'][0]['confidenceExplanation'], proposal['entities'][0]['confidenceExplanation'])
            self.assertIn(proposal['entities'][0]['confidenceExplanation'], api.maps.preview(self.f.f.load(), result))

    def test_legacy_maps_remain_readable_but_revised_uncertain_decisions_need_an_explanation(self):
        proposal = copy.deepcopy(self.f.f.proposal)
        proposal['entities'][0]['review']['confidence'] = 'medium'
        document = api.maps.build(self.f.f.load(), proposal)
        bundle = self.f.f.bundle
        api.scenes.atomic(bundle['root'], bundle['entityPath'].relative_to(bundle['root']), api.scenes.encoded(document))
        self.assertNotIn('confidenceExplanation', self.call()['document']['entities'][0])
        self.save(proposal)
        proposal['entities'][0]['importance'] = 'star'
        with self.assertRaisesRegex(ValueError, 'require confidenceExplanation'):
            self.save(proposal)

    def test_invalid_explanations_are_rejected_without_changing_the_map(self):
        path = self.f.f.bundle['entityPath']
        before = path.read_bytes()
        for explanation in ['', None, 'Two\nlines', 'word ' * 41]:
            proposal = copy.deepcopy(self.f.f.proposal)
            proposal['entities'][0]['confidenceExplanation'] = explanation
            with self.subTest(explanation=explanation), self.assertRaises(ValueError):
                self.save(proposal)
            self.assertEqual(path.read_bytes(), before)

    def test_protected_human_legacy_record_survives_note_edits_without_inventing_rationale(self):
        proposal = copy.deepcopy(self.f.f.proposal)
        proposal['entities'][0]['review']['confidence'] = 'medium'
        bundle = self.f.f.bundle
        api.scenes.atomic(bundle['root'], bundle['entityPath'].relative_to(bundle['root']), api.scenes.encoded(api.maps.build(self.f.f.load(), proposal)))
        result = self.call()
        result = self.call('entityUpdate', token=result['token'], entity='e001', changes={'status': 'humanReviewed'})
        proposal['entities'][0]['review']['status'] = 'humanReviewed'
        self.save(proposal)
        changed = copy.deepcopy(proposal)
        changed['entities'][0]['confidenceExplanation'] = 'An explanation was not recorded at the time.'
        with self.assertRaisesRegex(ValueError, 'Preserve human-reviewed'):
            self.save(changed)
        self.f.f.note.write_text('# Changed note evidence\n', encoding='utf8')
        self.save(proposal)
        preserved = self.call()['document']['entities'][0]
        self.assertEqual(preserved['review']['status'], 'humanReviewed')
        self.assertNotIn('confidenceExplanation', preserved)

    def test_queue_exclusion_preserves_edits_explanation_and_all_occurrences(self):
        proposal = copy.deepcopy(self.f.f.proposal)
        explanation = 'The repeated name and unique vault match support this identity.'
        proposal['entities'][0]['confidenceExplanation'] = explanation
        self.save(proposal)
        other = self.f.f.note.with_name('Other.md')
        other.write_text('# Other\n', encoding='utf8')
        inspected = self.call(notes=['People/Other.md'])
        excluded = self.call('entityUpdate', token=inspected['token'], entity='e001', action='exclude',
                             reason='Only a passing mention.', changes={'label': 'Other guide', 'note': 'People/Other.md', 'importance': 'cameo'})
        record = excluded['review']['excludedRecords'][0]['record']
        self.assertEqual(record['label'], 'Other guide')
        self.assertEqual(record['note'], 'People/Other.md')
        self.assertEqual(record['confidenceExplanation'], explanation)
        self.assertEqual(record['occurrences'], proposal['entities'][0]['occurrences'])
        self.assertEqual(excluded['document']['exclusions'][0]['label'], 'Other guide')
        restored = self.call(notes=excluded['exclusionDetails'][0]['restoreNotes'])
        restored = self.call('exclusionInclude', token=restored['token'], exclusionIndex=0)
        self.assertEqual(restored['document']['entities'][0], record)

    def test_exclusion_rejects_uninspected_edited_links_before_moving_anything(self):
        before = self.f.f.bundle['entityPath'].read_bytes()
        initial = self.call()
        with self.assertRaisesRegex(ValueError, 'Inspect new vault targets'):
            self.call('entityUpdate', token=initial['token'], entity='e001', action='exclude',
                      reason='Passing mention.', changes={'note': 'People/Uninspected.md'})
        self.assertEqual(self.f.f.bundle['entityPath'].read_bytes(), before)
