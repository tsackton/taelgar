import copy
from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import render_review as review


def presence(place, markers, actors=None):
    return dict(kind='presence', places=[place], markers=markers, actors=actors or ['party'])


class ReviewRowsTest(unittest.TestCase):
    def setUp(self):
        # Frozen, reduced DF119 regression scenario; never read the live bundle.
        self.sources = {
            'time-markers': {'markers': []},
            'location-markers': {
                'places': {ident: {'label': label} for ident, label in [
                    ('p01', 'Ship'), ('p02', 'Desert oak'), ('p03', 'Portal hill'),
                    ('p04', 'Riverbank'), ('p05', 'Barge'), ('p09', 'Cottage'),
                    ('p10', 'Kitchen')]},
                'markers': [
                    dict(id='l01', type='presence', place='p01', actors=['party']),
                    self.movement('l02', 'p01', 'p02'),
                    self.movement('l03', 'p02', 'p03'),
                    self.movement('l05', None, 'p04'),
                    self.movement('l07', 'p04', None, completion='underway'),
                    dict(id='l06', type='observation', place='p05',
                         observerPlace='p04', actors=['party']),
                    self.movement('l11', 'p04', 'p09'),
                    self.movement('l13', 'p09', 'p09', actors=['Wellby', 'Kenzo'],
                                  route=[dict(place='p10', reading='Collect tea in the kitchen.')]),
                    self.movement('l14', 'p09', 'p03', completion='planned', context='planned'),
                ]},
            'entity-map': {'entities': []},
            'interactions': {'interactions': []},
            'combat': {'combats': []},
        }
        self.edit = dict(watches=[], locations=[], entities=[], combats=[], flags=[], dates='Unknown.')
        self.bundle = {'data': {'campaign': 'Regression', 'sessionNumber': 119},
                       'source': Path('/fixture/transcript.md')}

    @staticmethod
    def movement(ident, origin, destination, **extra):
        return dict(id=ident, type='movement', **{'from': origin}, to=destination,
                    **(dict(completion='arrived', actors=['party']) | extra))

    def render(self):
        review.check_rows(self.edit, self.sources, self.bundle)
        paths = {key: Path('/fixture') / f'{key}.json' for key in review.VERSIONS}
        return review.render(self.bundle, paths, self.sources, self.edit, Path('/fixture'), None, 0)

    def test_df119_unexamined_itinerary_is_rejected(self):
        self.edit['locations'] = [dict(kind='presence', actors=['party'],
            places=['p01', 'p02', 'p03', 'p04', 'p09'],
            markers=['l01', 'l02', 'l03', 'l05', 'l07', 'l11'])]
        with self.assertRaisesRegex(ValueError, 'Arrow routes need routeBasis'):
            self.render()
        for basis in (None, '', '  ', 1):
            with self.subTest(basis=basis):
                self.edit['locations'][0]['routeBasis'] = basis
                with self.assertRaisesRegex(ValueError, 'Arrow routes need routeBasis'):
                    self.render()

    def test_df119_settings_use_arrivals_without_new_presence_markers(self):
        self.edit['locations'] = [
            presence('p01', ['l01']), presence('p02', ['l02']),
            presence('p03', ['l03']), presence('p04', ['l05', 'l07']),
            presence('p09', ['l11']),
            presence('p10', ['l13'], ['Wellby', 'Kenzo']),
            dict(kind='observation', places=['p05'], actors=['party'],
                 markers=['l06'], **{'from': 'p04'}),
        ]
        result = self.render()
        for label in ('Ship', 'Desert oak', 'Portal hill', 'Riverbank', 'Cottage'):
            self.assertIn(f'| {label} | Party |', result)
        self.assertIn('| Kitchen | Wellby and Kenzo | l13 |', result)
        self.assertIn('| Barge | Party | Riverbank | l06 |', result)
        self.assertNotIn(' → ', result)

    def test_actual_compressed_route_remains_an_arrow_chain(self):
        self.sources['location-markers']['markers'] = [self.movement(
            'l01', 'p01', 'p09', route=[dict(place='p04', reading='Cross the river.')],
            reading='Ride from the ship through a river crossing to the cottage.',
            evidence=[dict(startUid='u0010', endUid='u0010',
                           quote='You ride across the river and reach the cottage.')])]
        rationale = 'l01 narrates one ride with a transient crossing and no independent played stop.'
        self.edit['locations'] = [dict(kind='presence', actors=['party'],
            places=['p01', 'p04', 'p09'], markers=['l01'], routeBasis=rationale)]
        result = self.render()
        self.assertIn('| Ship → Riverbank → Cottage | Party | l01 |', result)
        self.assertNotIn(rationale, result)

    def test_continuous_travel_can_span_multiple_movement_markers(self):
        self.sources['location-markers']['markers'] = [
            self.movement('l01', 'p01', 'p04'), self.movement('l02', 'p04', 'p09')]
        self.edit['locations'] = [dict(kind='presence', actors=['party'],
            places=['p01', 'p04', 'p09'], markers=['l01', 'l02'],
            routeBasis='l01–l02 continue the ride; the river is only a crossing.')]
        self.assertIn('| Ship → Riverbank → Cottage | Party | l01–l02 |', self.render())

    def test_route_rationale_does_not_establish_a_planned_visit(self):
        self.edit['locations'] = [dict(kind='presence', actors=['party'],
            places=['p09', 'p03'], markers=['l14'], routeBasis='A proposed route.')]
        with self.assertRaisesRegex(ValueError, 'Physical locations need matching'):
            self.render()

    def test_feywild_rest_counts_elapsed_time_with_unchanged_afternoon(self):
        self.sources['time-markers']['markers'] = [
            dict(id='t01', reading='Golden afternoon, called evening later; light is unchanged.'),
            dict(id='t02', reading='Short-rest benefits awarded.', duration=dict(
                value=1, unit='hour', precision='exact', basis='short-rest convention')),
            dict(id='t03', reading='Long-rest benefits awarded; afternoon before and after.', duration=dict(
                value=8, unit='hour', precision='exact', basis='long-rest convention')),
            dict(id='t04', reading='Narrated dusk followed by morning; relationship unexplained.'),
        ]
        self.edit['watches'] = [
            dict(day='Feywild local appearance', clock='local', startWatch=None, endWatch=None,
                 basis='open', summary='Golden afternoon and evening light remain unchanged.', markers=['t01']),
            dict(day='Unplaced Feywild interval', startWatch=None, endWatch=None, basis='open',
                 summary='Short rest: one hour passed.', markers=['t02']),
            dict(day='Feywild long rest', startWatch=None, endWatch=None, basis='open',
                 summary='Long rest: eight hours passed; it is still afternoon.', markers=['t03']),
            dict(day='Unresolved Feywild time', clock='local', startWatch='dusk', endWatch='morning',
                 basis='stated', summary='Dusk then morning are narrated; their relationship remains unexplained.', markers=['t04']),
        ]
        before = copy.deepcopy(self.edit['watches'])
        result = self.render()
        self.assertEqual(self.edit['watches'], before)
        self.assertIn('| Feywild local appearance | Open (local) |', result)
        self.assertIn('| Unplaced Feywild interval | Open |', result)
        self.assertIn('Short rest: one hour passed.', result)
        self.assertIn('Long rest: eight hours passed; it is still afternoon.', result)
        self.assertIn('| Unresolved Feywild time | Dusk → morning (local) |', result)
        self.assertNotIn('startDate', self.edit['watches'][1])


if __name__ == '__main__':
    unittest.main()
