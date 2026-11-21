from pathlib import Path
import unittest

from analyze import format_for_session, session_key, session_level, session_order


class PointSessionTest(unittest.TestCase):
    def test_point_sessions_use_distinct_metadata_keys(self):
        first, tenth = session_key('012.1'), session_key('012.10')
        levels = {'initial': 2, 'session_overrides': {'12.1': {'level': 3}, '12.10': {'level': 5}}}
        self.assertEqual(session_level(levels, first), 3)
        self.assertEqual(session_level(levels, tenth), 5)

        metadata = {'play_formats': {'demo': {
            'source': 'gathering notes', 'in_person': [{'sessions': ['12.1'], 'gathering': 'Demo'}],
            'overrides': {'12.10': {'format': 'Zoom', 'evidence': 'recording'}},
        }}}
        manifest = Path('demo-session.yaml')
        self.assertEqual(format_for_session('demo', first, manifest, {}, metadata)[0], 'in person')
        self.assertEqual(format_for_session('demo', tenth, manifest, {}, metadata)[0], 'Zoom')

    def test_milestones_and_sorting_treat_the_suffix_as_a_part_number(self):
        config = {'initial': 2, 'milestones': [{'session': '12.10', 'level': 3, 'boundary': 'end'}]}
        self.assertEqual(session_level(config, '12.2', at_end=True), 2)
        self.assertEqual(session_level(config, '12.10'), 2)
        self.assertEqual(session_level(config, '12.10', at_end=True), 3)
        self.assertEqual(session_level(config, 13), 3)
        self.assertEqual(sorted(['12.10', 13, '12.2', 12, '12.1'], key=session_order),
                         [12, '12.1', '12.2', '12.10', 13])
