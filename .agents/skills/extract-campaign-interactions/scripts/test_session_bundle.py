"""Bundle provenance, polished UID ranges, exclusions and YAML handoff."""
import copy
import json
import tempfile
import unittest
from pathlib import Path

import yaml
from jsonschema import ValidationError
from process import review_request
from batch import audit_chain, build
from session_bundle import BundleCatalog, BundleError, CLEANED, POLISHED, fingerprint, load_bundle
from session_model import critical_queue, digest, render, validate
from session_processing import apply_processing_review, complete, new_processing, processing_digest, validate_processing


class BundleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        self.root = self.vault / '_sessions/test/session-1'
        self.folder = self.root / 'cleaned'
        self.folder.mkdir(parents=True)
        self.raw = self.folder / 'test-source-cleaned.md'
        self.raw.write_text('[u0001 | 00:00 | PC] Hello\n[u0002 | 00:01 | DM] my friend.\n[u0003 | 00:02 | DM] Table chatter.\n')
        self.polished = self.folder / 'test-transcript.md'
        self.polished.write_text('# Transcript\n\n## Transcript\n\n%% u0001:0-5, u0002:0-10 %%\nDM: Hello, my friend!\n\n%% u0003:0-14 %%\nDM: Table chatter.\n')
        self.manifest = self.folder / 'test-session.yaml'
        self.metadata = {'schemaVersion': '1.0', 'sourceType': 'transcript', 'campaign': 'Test',
                         'sessionNumber': 1.5, 'realWorldDate': '2026-10-29',
                         'drStart': '1748-01-01', 'drEnd': '1748-01-05', 'participants': [],
                         'transcriptProcessing': {'artifacts': {
                             'cleaned': {'path': 'cleaned/test-source-cleaned.md', 'sha256': digest(self.raw)},
                             'polishedMarkdown': {'path': 'cleaned/test-transcript.md', 'sha256': digest(self.polished)}},
                             'speakerCorrections': [{'uid': 'u0001', 'start': 0, 'end': 5, 'speaker': 'DM'}]}}
        self.save_yaml()
        self.loc = {'kind': 'transcript', 'sourceId': POLISHED, 'startUid': 'u0001', 'endUid': 'u0002'}
        self.data = {'schemaVersion': 6, 'sessionYaml': str(self.manifest.relative_to(self.vault)),
                     'scenes': [{'index': 1, 'source': copy.deepcopy(self.loc), 'dateStart': '1748-01-02', 'dateEnd': '1748-01-02'}],
                     'entities': [{'id': 'guide', 'kind': 'npc', 'label': 'Guide'}],
                     'interactions': [{'id': 'meeting', 'entity': 'guide', 'scenes': [1], 'interaction': 'interacted',
                                       'quotes': [{'id': 'greeting', 'type': 'color', 'text': 'Hello, my friend!', 'source': copy.deepcopy(self.loc)}]}]}
        self.catalog = BundleCatalog(self.data, self.vault)
        self.processing = new_processing(self.data, self.catalog)
        self.processing['fullTranscriptRead'] = True
        self.processing['excludedBlocks'] = [{'source': {**self.loc, 'startUid': 'u0003', 'endUid': 'u0003'},
                                               'reason': 'Out-of-character table chatter after play.'}]

    def save_yaml(self):
        self.manifest.write_text('# Keep this comment.\n' + yaml.safe_dump(self.metadata, sort_keys=False))

    def report(self, data=None, processing=None, confidence='high'):
        data, processing = data or self.data, processing or self.processing
        return {'inputDigest': fingerprint(data), 'processingDigest': processing_digest(processing),
                'reviewer': 'test semantic review fixture', 'attempt': len(processing['reviews']),
                'decisions': [{'target': t, 'confidence': confidence, 'reason': 'Fixture evidence reviewed.', 'evidence': [self.loc]}
                              for t in ['session', 'scenes', 'entity:guide']]}

    def reviewed(self):
        return apply_processing_review(self.data, self.processing, self.report(), self.vault)

    def test_polished_ranges_preserve_ids_and_quote_new_punctuation(self):
        result = validate(self.data, self.vault, processing=self.processing)
        self.assertEqual(result['catalog'].bundle['sourceId'], POLISHED)
        self.assertEqual(result['excludedUtterances'], 1)
        self.assertEqual(result['unexplainedUtterances'], 0)
        self.assertIn('Hello, my friend!', self.catalog.passage(self.loc))
        self.assertIn('?plain=1#L5-L7', self.catalog.link(self.loc, self.root / 'review.md'))
        narrow = {**self.loc, 'endUid': 'u0001'}
        self.assertNotIn('Hello, my friend!', self.catalog.passage(narrow))

    def test_metadata_is_not_duplicated_and_fractional_session_supported(self):
        for field, value in [('campaign', 'Test'), ('session', 1.5), ('realWorldDate', '2026-10-29'),
                             ('pcs', []), ('sources', []), ('dateStart', '1748-01-01'), ('dateEnd', '1748-01-05')]:
            with self.subTest(field=field), self.assertRaises(ValidationError):
                validate({**self.data, field: value}, self.vault)
        self.assertEqual(self.catalog.display_metadata()['session'], 1.5)

    def test_yaml_extending_or_clarifying_dates_is_accepted(self):
        data, processing = self.reviewed()
        validate_processing(data, processing, self.vault, complete=True)
        self.assertEqual(processing['metadataFindings'], [])

    def test_clear_date_conflict_is_critical_and_visible(self):
        finding = {'id': 'date', 'kind': 'dateConflict', 'severity': 'critical', 'status': 'open',
                   'reason': 'An explicit transcript date contradicts the YAML start.',
                   'evidence': [self.loc, {'yamlField': 'drStart'}]}
        self.processing['metadataFindings'].append(finding)
        data, processing = apply_processing_review(self.data, self.processing, self.report(confidence='low'), self.vault)
        self.assertTrue(any(q['target'] == 'metadata:date' for q in critical_queue(data, processing)))
        output = render(data, self.vault, self.root / 'review.md', processing=processing)
        self.assertIn(finding['reason'], output)
        finding['severity'] = 'info'
        with self.assertRaisesRegex(ValueError, 'must be critical'):
            validate(self.data, self.vault, processing=self.processing)

    def test_conflict_requires_actual_transcript_and_yaml_evidence(self):
        self.processing['metadataFindings'] = [{'id': 'd', 'kind': 'dateConflict', 'severity': 'critical', 'status': 'open',
                                               'reason': 'Bad evidence', 'evidence': [{'yamlField': 'drEnd'}]}]
        with self.assertRaisesRegex(ValueError, 'both transcript and YAML'):
            validate(self.data, self.vault, processing=self.processing)

    def test_review_receives_exclusions_and_unexplained_ranges(self):
        request = review_request(self.data, self.vault, self.processing)
        self.assertEqual(request['excludedBlocks'], self.processing['excludedBlocks'])
        self.assertEqual(request['unexplainedRanges'], [])
        self.processing['excludedBlocks'] = []
        request = review_request(self.data, self.vault, self.processing)
        self.assertEqual(request['unexplainedRanges'][0]['startUid'], 'u0003')

    def test_excluded_blocks_need_reasons_and_cannot_hide_scenes(self):
        block = self.processing['excludedBlocks'][0]
        block['reason'] = ''
        with self.assertRaises(ValidationError):
            validate(self.data, self.vault, processing=self.processing)
        block['reason'] = 'Chatter'
        block['source']['startUid'] = 'u0002'
        with self.assertRaisesRegex(ValueError, 'overlaps a scene'):
            validate(self.data, self.vault, processing=self.processing)

    def test_changed_yaml_stales_review_even_when_json_is_unchanged(self):
        report = self.report()
        self.metadata['drEnd'] = '1748-01-06'
        self.save_yaml()
        with self.assertRaisesRegex(ValueError, 'changed since preparation'):
            apply_processing_review(self.data, self.processing, report, self.vault)

    def test_changed_exclusion_reason_stales_report(self):
        report = self.report()
        self.processing['excludedBlocks'][0]['reason'] = 'Changed interpretation'
        with self.assertRaisesRegex(ValueError, 'processing evidence changed'):
            apply_processing_review(self.data, self.processing, report, self.vault)

    def test_changed_candidate_cannot_render_as_currently_ready(self):
        data, processing = self.reviewed()
        data['entities'][0]['label'] = 'Changed after review'
        result = validate(data, self.vault, processing=processing)
        self.assertFalse(result['metadataReady'])
        self.assertIn('Review is stale', render(data, self.vault, self.root / 'review.md', processing=processing))
        self.assertTrue(any(q['target'] == 'session' for q in critical_queue(data, processing)))

    def test_changed_source_is_rejected(self):
        self.polished.write_text(self.polished.read_text().replace('Hello', 'Goodbye'))
        with self.assertRaisesRegex(ValueError, 'hash changed'):
            validate(self.data, self.vault, processing=self.processing)

    def test_bad_source_path_proposes_yaml_fix_without_using_fallback(self):
        self.metadata['transcriptProcessing']['artifacts']['polishedMarkdown']['path'] = 'elsewhere/test-transcript.md'
        self.save_yaml()
        with self.assertRaises(BundleError) as caught:
            load_bundle(self.vault, self.data['sessionYaml'])
        self.assertEqual(caught.exception.proposals[0]['proposed'], 'cleaned/test-transcript.md')
        self.assertIn('elsewhere/test-transcript.md', self.manifest.read_text())

    def test_unregistered_cleaned_file_is_only_a_proposal(self):
        del self.metadata['transcriptProcessing']
        self.save_yaml()
        with self.assertRaises(BundleError) as caught:
            load_bundle(self.vault, self.data['sessionYaml'])
        self.assertEqual(caught.exception.proposals[0]['field'], 'cleanedSourcePath')
        self.assertEqual(caught.exception.proposals[0]['proposed'], 'test-source-cleaned.md')

    def test_cleaned_fallback_applies_partial_speaker_overrides(self):
        del self.metadata['transcriptProcessing']['artifacts']['polishedMarkdown']
        self.metadata['transcriptProcessing']['speakerCorrections'][0]['end'] = 2
        self.save_yaml()
        catalog = BundleCatalog(self.data, self.vault)
        self.assertEqual(catalog.bundle['sourceId'], CLEANED)
        self.assertIn('DM: He', catalog.compact())
        self.assertIn('PC: llo', catalog.compact())

    def test_polished_mapping_must_cover_cleaned_source(self):
        self.polished.write_text(self.polished.read_text().replace('u0001:0-5, ', ''))
        self.metadata['transcriptProcessing']['artifacts']['polishedMarkdown']['sha256'] = digest(self.polished)
        self.save_yaml()
        with self.assertRaisesRegex(ValueError, 'source coverage'):
            BundleCatalog(self.data, self.vault)

    def test_split_uid_and_multiline_polished_turns_keep_source_mapping(self):
        self.metadata['transcriptProcessing']['speakerCorrections'][0]['end'] = 2
        self.polished.write_text('# Transcript\n\n## Transcript\n\n%% u0001:0-2 %%\nDM: He\n\n'
                                 '%% u0001:2-5 %%\nPC: llo\n\n%% u0002:0-10 %%\nDM: my\n\nfriend.\n\n'
                                 '%% u0003:0-14 %%\nDM: Table chatter.\n')
        self.metadata['transcriptProcessing']['artifacts']['polishedMarkdown']['sha256'] = digest(self.polished)
        self.save_yaml()
        catalog = BundleCatalog(self.data, self.vault)
        self.assertEqual(len(catalog.turns), 4)
        self.assertIn('my\n\nfriend.', catalog.passage(self.loc))
        self.assertIn('?plain=1#L5-L15', catalog.link(self.loc, self.root / 'review.md'))

    def test_cleaned_text_without_ids_cannot_be_silently_excluded(self):
        self.raw.write_text(self.raw.read_text() + 'Unmapped meaningful text\n')
        self.metadata['transcriptProcessing']['artifacts']['cleaned']['sha256'] = digest(self.raw)
        self.save_yaml()
        with self.assertRaisesRegex(ValueError, 'Unmapped cleaned'):
            BundleCatalog(self.data, self.vault)

    def test_completion_writes_relative_pointers_and_preserves_yaml(self):
        data, processing = self.reviewed()
        before = self.manifest.read_bytes()
        output = self.root / 'interactions'
        pointers = complete(data, processing, self.vault, output)
        self.assertEqual(pointers['sessionJson'], '../interactions/session.json')
        self.assertTrue(self.manifest.read_bytes().startswith(before.rstrip()))
        saved = json.loads((output / 'session-processing-data.json').read_text())
        self.assertEqual(saved['stage'], 'completed')
        validate(data, self.vault, processing=saved)
        self.assertIn('Out-of-character table chatter', (output / 'review.md').read_text())
        self.assertEqual(complete(data, processing, self.vault, output), pointers)

    def test_completion_protects_existing_outputs_and_requires_coverage_review(self):
        data, processing = self.reviewed()
        output = self.root / 'interactions'
        output.mkdir()
        (output / 'review.md').write_text('Human edits')
        before = self.manifest.read_bytes()
        with self.assertRaisesRegex(ValueError, 'overwrite'):
            complete(data, processing, self.vault, output)
        self.assertEqual(self.manifest.read_bytes(), before)
        self.processing['excludedBlocks'] = []
        data, processing = self.reviewed()
        with self.assertRaisesRegex(ValueError, 'Unexplained transcript'):
            complete(data, processing, self.vault, self.root / 'other')

    def test_no_validation_only_completion_or_repeated_review_attempt(self):
        with self.assertRaisesRegex(ValueError, 'semantic review'):
            complete(self.data, self.processing, self.vault, self.root / 'interactions')
        data, processing = self.reviewed()
        report = self.report(data, processing)
        report['attempt'] = 0
        with self.assertRaisesRegex(ValueError, 'repeated'):
            apply_processing_review(data, processing, report, self.vault)

    def test_saved_chain_is_replayed_and_correction_cannot_reset_human_review(self):
        data, processing = apply_processing_review(self.data, self.processing, self.report(), self.vault, 'humanReviewed')
        candidate = copy.deepcopy(data)
        candidate['entities'][0]['label'] = 'Different person'
        candidate['entities'][0]['review'] = {'confidence': 'low', 'status': 'unreviewed'}
        report = self.report(candidate, processing)
        with self.assertRaisesRegex(ValueError, 'human-reviewed record'):
            apply_processing_review(candidate, processing, report, self.vault)

    def test_batch_audit_reuses_processing_history(self):
        data, processing = self.reviewed()
        output = self.root / 'interactions'
        complete(data, processing, self.vault, output)
        saved, _ = audit_chain(output, self.vault)
        self.assertEqual(saved, data)
        data['entities'][0]['label'] = 'Post-review change'
        (output / 'session.json').write_text(json.dumps(data))
        with self.assertRaisesRegex(ValueError, 'changed after semantic review'):
            audit_chain(output, self.vault)

    def test_batch_directory_follows_yaml_pointer_without_copying_canonical_json(self):
        data, processing = self.reviewed()
        output = self.root / 'interactions'
        complete(data, processing, self.vault, output)
        row = {'id': 'session-1', 'manifest': data['sessionYaml'], 'inputs': processing['inputs'],
               'sha256': self.catalog.hashes[POLISHED]}
        sample = {'seed': 1, 'selected': [row], 'population': [row]}
        directory = self.vault / 'trial'
        directory.mkdir()
        result = build(self.vault, sample, directory, directory / 'README.md')
        self.assertTrue(result['complete'])
        self.assertIn('session-1/interactions/review.md#entity-list', (directory / 'README.md').read_text())
        self.assertFalse((directory / 'session-1/session.json').exists())
        (output / 'review.md').write_text('Human review notes')
        result = build(self.vault, sample, directory, directory / 'README.md')
        self.assertFalse(result['complete'])
        self.assertEqual((output / 'review.md').read_text(), 'Human review notes')


if __name__ == '__main__':
    unittest.main()
