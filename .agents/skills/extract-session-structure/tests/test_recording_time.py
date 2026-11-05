import hashlib
from pathlib import Path
import sys
import tempfile
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import render_review as review


def segment(ident, category, start, end):
    return dict(id=ident, category=category, source=dict(startUid=start, endUid=end))


class RecordingTimeTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)

    def bundle(self, rows, artifact='cleaned'):
        # Real registered UID-header format, with test-owned timing/coverage.
        raw = ''.join(f'[{uid} | {timing} | DM] Speech.\n' for uid, timing in rows).encode()
        (self.root / 'timed.md').write_bytes(raw)
        return dict(manifest=self.root / 'fixture-001-session.yaml', root=self.root, source=self.root / 'polished.md',
                    data=dict(campaign='Timing fixture', sessionNumber=1,
                              transcriptProcessing=dict(artifacts={artifact: {'path': 'timed.md'}})),
                    fingerprints={'timed.md': hashlib.sha256(raw).hexdigest()},
                    positions={uid: index for index, (uid, _) in enumerate(rows)},
                    groups=[dict(startUid=uid, endUid=uid) for uid, _ in rows])

    def render(self, bundle, timing):
        paths = {key: self.root / f'{key}.json' for key in review.VERSIONS}
        sources = {'location-markers': {'places': {}}, 'entity-map': {'entities': []},
                   'combat': {'combats': []}}
        edit = dict(flags=[], dates='Unknown.', watches=[], locations=[], entities=[], combats=[])
        return review.render(bundle, paths, sources, edit, self.root, timing)

    def test_elapsed_counts_internal_silence_but_not_between_separate_blocks(self):
        # First two ranges mirror DF119's millisecond precision and shared endpoint.
        bundle = self.bundle([
            ('u0001', '00:00:08.710-00:00:10.210'),
            ('u0002', '00:00:10.210-00:00:13.859'),
            ('u0003', '00:01:00.000-00:01:02.000'),
            ('u0004', '00:01:12.000-00:01:13.000'),
            ('u0005', '00:01:20.000-00:01:21.000')])
        timing = review.recording_time(bundle, [
            segment('s1', 'combat', 'u0001', 'u0003'),
            segment('s2', 'meta_discussion', 'u0004', 'u0004'),
            segment('s3', 'combat', 'u0005', 'u0005')])
        self.assertEqual((timing['start'], timing['end'], timing['recording']), (8710, 81000, 72290))
        self.assertEqual(timing['elapsed']['combat'], 54290)
        self.assertEqual(timing['speaking']['combat'], 8149)
        self.assertEqual(sum(timing['elapsed'].values()), 55290)
        self.assertEqual(sum(timing['speaking'].values()), 9149)
        text = self.render(bundle, timing)
        self.assertIn('Recording length (transcript timestamp extent): **0:01:12**', text)
        self.assertIn('Outside segment spans: **0:00:17**', text)
        self.assertIn('| Combat | 0:00:54 | 98.2% | 0:00:08 | 89.1% |', text)
        self.assertIn('silence outside these timestamps', text)

    def test_latest_end_need_not_be_final_uid_end(self):
        bundle = self.bundle([('u0001', '00:00:00.000-00:00:20.000'),
                              ('u0002', '00:00:10.000-00:00:12.000')])
        timing = review.recording_time(bundle, [segment('s1', 'combat', 'u0001', 'u0002')])
        self.assertEqual(timing['recording'], 20000)
        self.assertEqual(timing['elapsed']['combat'], 20000)
        self.assertEqual(timing['speaking']['combat'], 20000)
        self.assertEqual(timing['overlap'], 2000)

    def test_cross_class_overlaps_count_once_and_totals_remain_additive(self):
        bundle = self.bundle([('u0001', '00:00:00.000-00:00:10.000'),
                              ('u0002', '00:00:08.000-00:00:12.000')])
        timing = review.recording_time(bundle, [segment('s1', 'combat', 'u0001', 'u0001'),
                                                segment('s2', 'gameplay', 'u0002', 'u0002')])
        for measure in ('elapsed', 'speaking'):
            self.assertEqual(timing[measure]['combat'], 10000)
            self.assertEqual(timing[measure]['gameplay'], 2000)
            self.assertEqual(sum(timing[measure].values()), timing['recording'])
        self.assertIn('Overlapping utterance timestamps: 2.000 cumulative seconds counted once.',
                      self.render(bundle, timing))

    def test_uid_order_not_integer_arithmetic_and_shared_groups_count_once(self):
        bundle = self.bundle([('u0001', '00:00:00.000-00:00:01.000'),
                              ('u0004', '00:00:02.000-00:00:03.000'),
                              ('u0010', '00:00:04.000-00:00:05.000')])
        bundle['groups'] = [dict(startUid='u0001', endUid='u0004'),
                            dict(startUid='u0010', endUid='u0010')]
        timing = review.recording_time(bundle, [segment('s1', 'combat', 'u0001', 'u0004'),
                                                segment('s2', 'gameplay', 'u0010', 'u0010')])
        self.assertEqual(sum(timing['speaking'].values()), 3000)
        with self.assertRaisesRegex(ValueError, 'Invalid classification or boundary'):
            review.recording_time(bundle, [segment('s1', 'combat', 'u0001', 'u0001')])

    def test_prepared_fallback_ignores_polished_character_offsets(self):
        bundle = self.bundle([('u0001', '01:42:49.310-01:42:51.299')], artifact='prepared')
        bundle['source'].write_text('%% u0001:0-999 %%\nDM: Speech.\n')
        timing = review.recording_time(bundle, [segment('s1', 'gameplay', 'u0001', 'u0001')])
        self.assertEqual((timing['start'], timing['end'], timing['recording']), (6169310, 6171299, 1989))

    def test_cleaned_source_takes_precedence_over_prepared(self):
        bundle = self.bundle([('u0001', '00:00:01.000-00:00:02.000')])
        bundle['data']['transcriptProcessing']['artifacts']['prepared'] = {'path': 'unused.md'}
        self.assertEqual(review.recording_time(bundle, [segment('s1', 'combat', 'u0001', 'u0001')])['recording'], 1000)

    def test_missing_timestamps_are_unavailable_not_zero(self):
        bundle = self.bundle([('u0001', '00:00:01.000-00:00:02.000')])
        bundle['data']['transcriptProcessing']['artifacts'] = {}
        timing = review.recording_time(bundle, [])
        self.assertIsNone(timing['recording'])
        self.assertIsNone(timing['elapsed'])
        text = self.render(bundle, timing)
        self.assertIn('No registered cleaned or prepared UID transcript', text)
        self.assertIn('No human action requested.', text)
        self.assertNotIn('**0:00:00**', text)

    def test_invalid_or_backwards_timestamps_are_distinguished(self):
        for rows, message in [
            ([('u0001', 'unknown')], 'Invalid or missing UID timestamps'),
            ([('u0001', '00:00:20-00:00:10')], 'Invalid or missing UID timestamps'),
            ([('u0001', '00:00:10-00:00:11'), ('u0002', '00:00:00-00:00:01')],
             'Timestamp starts run backwards')]:
            with self.subTest(rows=rows):
                timing = review.recording_time(self.bundle(rows), [
                    segment('s1', 'gameplay', rows[0][0], rows[-1][0])])
                self.assertIsNone(timing['recording'])
                self.assertIsNone(timing['speaking'])
                self.assertIn(message, timing['notes'][0])

    def test_fingerprints_uid_mappings_and_segment_coverage_still_guard_results(self):
        bundle = self.bundle([('u0001', '00:00:00-00:00:01')])
        with self.assertRaisesRegex(ValueError, 'Segments do not cover'):
            review.recording_time(bundle, [])
        bundle['positions'] = {'u0002': 0}
        with self.assertRaisesRegex(ValueError, 'Timed UID source differs'):
            review.recording_time(bundle, [])
        (self.root / 'timed.md').write_text('Changed.')
        with self.assertRaisesRegex(ValueError, 'Timed transcript changed'):
            review.recording_time(bundle, [])

    def test_zero_length_intervals_do_not_divide_by_zero(self):
        bundle = self.bundle([('u0001', '00:00:01.000-00:00:01.000')])
        timing = review.recording_time(bundle, [segment('s1', 'combat', 'u0001', 'u0001')])
        self.assertEqual(timing['recording'], 0)
        self.assertIn('| **Total** | 0:00:00 | — | 0:00:00 | — |', self.render(bundle, timing))


if __name__ == '__main__':
    unittest.main()
