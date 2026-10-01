#!/usr/bin/env python3
"""Preservation and provenance checks for recording-local recalibration."""

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import speaker_recalibrate as module


class RecalibrateTests(unittest.TestCase):
    def fixture(self):
        utterances = [
            {'id': 'one', 'recordingId': 'r1', 'start': 0, 'end': 2, 'text': 'first recording', 'groupId': 'g1'},
            {'id': 'two', 'recordingId': 'r1', 'start': 3, 'end': 5, 'text': 'another person', 'groupId': 'g1'},
            {'id': 'three', 'recordingId': 'r2', 'start': 0, 'end': 2, 'text': 'other phone', 'groupId': 'g2'},
        ]
        review = {'schemaVersion': 1, 'reviewId': 'original', 'participants': [{'id': 'p1'}],
                  'recordings': [{'id': 'r1', 'audioSha256': 'a'}, {'id': 'r2', 'audioSha256': 'b'}],
                  'utterances': utterances, 'groups': [
                      {'id': 'g1', 'recordingId': 'r1', 'memberUtteranceIds': ['one', 'two'], 'representativeUtteranceIds': ['one']},
                      {'id': 'g2', 'recordingId': 'r2', 'memberUtteranceIds': ['three'], 'representativeUtteranceIds': ['three']}],
                  'exceptions': {'unclusteredUtteranceIds': []},
                  'modelAttribution': {'modelOverrideUtteranceIds': ['one', 'two', 'three']}}
        attrs = {'schemaVersion': 1, 'reviewId': 'original', 'groupLabels': {}, 'utteranceOverrides': {
            'one': {'status': 'unknown', 'participantId': None},
            'two': {'status': 'assigned', 'participantId': 'p1', 'modelMargin': 0.1},
            'three': {'status': 'assigned', 'participantId': 'p1'}},
            'verification': {'p1': {'status': 'confirmed', 'sampleUtteranceIds': ['three']}}}
        return review, attrs

    def test_partitions_exact_cues_and_preserves_corrections_as_prior_predictions(self):
        review, attrs = self.fixture()
        before = copy.deepcopy((review, attrs))
        outputs = [module.recording_layer(review, attrs, rec, rec + '-local', {}) for rec in ['r1', 'r2']]
        self.assertEqual([u for r, _ in outputs for u in r['utterances']], review['utterances'])
        self.assertEqual(outputs[0][1]['utteranceOverrides'], {'one': attrs['utteranceOverrides']['one']})
        self.assertEqual(outputs[0][0]['priorSpeakerEvidence']['predictions'], {'two': attrs['utteranceOverrides']['two']})
        self.assertEqual(outputs[1][1]['utteranceOverrides'], {'three': attrs['utteranceOverrides']['three']})
        self.assertTrue(all(not a['verification'] for _, a in outputs))
        self.assertEqual(outputs[0][0]['priorSpeakerEvidence']['verification'], attrs['verification'])
        self.assertEqual((review, attrs), before)

    def test_cache_reuse_is_exact_and_rejects_changed_timing_or_source(self):
        np = module.load_numpy()
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            review, _ = self.fixture()
            source = root / 'source.json'
            source.write_text(json.dumps(review))
            cache = root / 'cache.npz'
            meta = {'sourceType': 'speaker-review', 'sourcePath': str(source), 'sourceSha256': module.sha256_file(source),
                    'complete': True, 'plannedCount': 3, 'completedCount': 3}
            vectors = np.array([[1., 0.], [0., 1.], [1., 1.]])
            np.savez(cache, ids=np.array(['one', 'two', 'three']), embeddings=vectors, metadata_json=np.array(json.dumps(meta)))
            ids, reused, _ = module.provenanced_cache(np, cache, review)
            self.assertTrue(np.array_equal(reused, vectors))
            self.assertEqual(list(ids), ['one', 'two', 'three'])
            altered = copy.deepcopy(review)
            altered['recordings'][0]['audioSha256'] = 'different-phone'
            with self.assertRaises(module.SpeakerReviewError):
                module.provenanced_cache(np, cache, altered)
            altered = copy.deepcopy(review)
            altered['utterances'][0]['start'] = .01
            with self.assertRaises(module.SpeakerReviewError):
                module.provenanced_cache(np, cache, altered)
            source.write_text(json.dumps(altered))
            with self.assertRaises(module.SpeakerReviewError):
                module.provenanced_cache(np, cache, altered)

    def test_cli_writes_new_layers_and_refuses_to_overwrite(self):
        np = module.load_numpy()
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            review, attrs = self.fixture()
            rp, ap, cp = root / 'review.json', root / 'attrs.json', root / 'cache.npz'
            rp.write_text(json.dumps(review)); ap.write_text(json.dumps(attrs))
            before = (rp.read_bytes(), ap.read_bytes())
            meta = {'sourceType': 'speaker-review', 'sourcePath': str(rp), 'sourceSha256': module.sha256_file(rp),
                    'complete': True, 'plannedCount': 3, 'completedCount': 3}
            vectors = np.array([[1., 0.], [0., 1.], [1., 1.]])
            np.savez(cp, ids=np.array(['one', 'two', 'three']), embeddings=vectors, metadata_json=np.array(json.dumps(meta)))
            argv = [str(rp), '--attributions', str(ap), '--embeddings', str(cp), '--output-dir', str(root / 'out'), '--review-id-prefix', 'trial']
            self.assertEqual(module.main(argv), 0)
            report = json.loads((root / 'out/trial.local-calibration.json').read_text())
            self.assertEqual([x['reusedEmbeddingCount'] for x in report['layers']], [2, 1])
            for layer in report['layers']:
                with np.load(layer['embeddingPath'], allow_pickle=False) as z:
                    m = json.loads(str(z['metadata_json'].item()))
                    self.assertEqual(m['sourceSha256'], module.sha256_file(Path(layer['reviewPath'])))
                    self.assertTrue(np.array_equal(z['embeddings'], vectors[:2] if layer['recordingId'] == 'r1' else vectors[2:]))
            hashes = {p: module.sha256_file(p) for p in (root / 'out').iterdir()}
            self.assertEqual(module.main(argv), 2)
            self.assertEqual(hashes, {p: module.sha256_file(p) for p in (root / 'out').iterdir()})
            self.assertEqual((rp.read_bytes(), ap.read_bytes()), before)


if __name__ == '__main__':
    unittest.main()
