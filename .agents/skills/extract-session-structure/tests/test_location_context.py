from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import render_review as review


def within(target, **extra):
    return dict(relation='within', target=target,
                evidence=[dict(startUid='u0001', endUid='u0001', quote='Inside the manor estate.')], **extra)


class LocationContextTest(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.vault_patch = patch.object(review, 'VAULT', self.root)
        self.vault_patch.start()
        self.addCleanup(self.vault_patch.stop)
        self.places = {'room': dict(label='Hidden archive', kind='room')}
        self.markers = [dict(id='l01', type='presence', place='room', actors=['party'])]
        self.sources = {
            'time-markers': {'markers': []},
            'location-markers': dict(places=self.places, markers=self.markers),
            'entity-map': {'entities': []}, 'combat': {'combats': []},
        }
        self.edit = dict(flags=[], dates='', watches=[], locations=[
            dict(kind='presence', places=['room'], actors=['party'], markers=['l01'])],
            entities=[], combats=[])
        self.bundle = dict(data=dict(campaign='Context fixture', sessionNumber=2),
                           source=self.root / 'transcript.md')

    def render(self):
        review.check_rows(self.edit, self.sources, self.bundle)
        paths = {key: self.root / f'{key}.json' for key in review.VERSIONS}
        return review.render(self.bundle, paths, self.sources, self.edit, self.root,
                             dict(recording=None, notes=[]))

    def parent(self, linked=False):
        self.places['manor'] = dict(label='Perdoli Manor', kind='estate')
        self.places['room']['relations'] = [within('manor')]
        if linked:
            path = self.root / 'Gazetteer' / 'Perdoli Manor.md'
            path.parent.mkdir()
            path.write_text('# Test-owned manor identity\n')
            self.places['manor']['vaultPath'] = path.relative_to(self.root).as_posix()

    def test_missing_parent_is_not_guessed_from_room_names(self):
        self.assertIn('| Hidden archive | Party | l01 |', self.render())
        self.assertNotIn('Perdoli', self.render())

    def test_named_parent_link_and_supported_region_render_as_breadcrumb(self):
        self.parent(linked=True)
        self.places['region'] = dict(label='Western Cymea', kind='region')
        self.places['manor']['relations'] = [within('region')]
        result = self.render()
        self.assertIn('| Western Cymea › [Perdoli Manor](Gazetteer/Perdoli%20Manor.md) › Hidden archive | Party | l01 |', result)
        self.assertEqual(len(self.edit['locations']), 1)  # Parents are context, not invented arrivals.

    def test_only_explicit_containment_supplies_breadcrumbs(self):
        self.places['town'] = dict(label='Nearby town')
        for relation in ('near', 'adjacent_to', 'above', 'connected_to'):
            with self.subTest(relation=relation):
                self.places['room']['relations'] = [dict(relation=relation, target='town')]
                self.assertIn('| Hidden archive | Party | l01 |', self.render())
                self.assertNotIn('Nearby town ›', self.render())

    def test_qualification_and_vault_only_orientation_remain_visible_as_notes(self):
        self.parent()
        self.places['room']['relations'][0]['note'] = 'Extent of the estate boundary is uncertain.'
        self.places['manor']['note'] = 'Vault-only orientation: modern Gazetteer/Manor.md places it in Western Cymea; not established in play.'
        result = self.render()
        self.assertIn('Perdoli Manor › Hidden archive', result)
        self.assertIn('Extent of the estate boundary is uncertain.', result)
        self.assertIn('Vault-only orientation: modern Gazetteer/Manor.md', result)
        self.assertNotIn('Western Cymea ›', result)
        self.assertIn('| Context |', result)

    def test_two_supported_parents_are_not_silently_chosen_between(self):
        self.parent()
        self.places['district'] = dict(label='Ruined district')
        self.places['room']['relations'].append(within('district', note='Its relation to the manor boundary is unclear.'))
        result = self.render()
        self.assertIn('Perdoli Manor › Hidden archive / Ruined district › Hidden archive', result)
        self.assertIn('relation to the manor boundary is unclear', result)

    def test_missing_targets_cycles_and_unsupported_containment_are_rejected(self):
        self.places['room']['relations'] = [within('missing')]
        with self.assertRaisesRegex(ValueError, 'Unknown parent'):
            self.render()
        self.parent()
        self.places['manor']['relations'] = [within('room')]
        with self.assertRaisesRegex(ValueError, 'Containment cycle'):
            self.render()
        self.places['manor'].pop('relations')
        self.places['room']['relations'][0].pop('evidence')
        with self.assertRaisesRegex(ValueError, 'Containment needs extraction evidence'):
            self.render()

    def test_missing_or_outside_vault_links_are_rejected(self):
        for value in ('Gazetteer/Missing.md', '../outside.md', '/etc/hosts'):
            with self.subTest(value=value):
                self.places['room']['vaultPath'] = value
                with self.assertRaisesRegex(ValueError, 'inside the vault'):
                    self.render()

    def test_mobile_context_is_temporary_and_not_a_parent(self):
        self.places.update(ship=dict(label='Skyship', mobile=True), house=dict(label='House'))
        self.markers[0].update(place='ship', locationContext=[
            dict(subject='ship', relation='above', target='house', note='Temporary position.')])
        self.edit['locations'][0]['places'] = ['ship']
        result = self.render()
        self.assertIn('| Skyship | Party | l01 | Skyship — above House (l01): Temporary position. |', result)
        self.assertNotIn('House › Skyship', result)

    def test_observation_breadcrumb_does_not_become_a_physical_visit(self):
        self.parent(linked=True)
        self.places['camp'] = dict(label='Camp')
        self.markers[0].update(type='observation', observerPlace='camp', mode='remote')
        self.edit['locations'][0].update(kind='observation', **{'from': 'camp', 'via': 'vision'})
        result = self.render()
        self.assertIn('| Observed location | Observer | From | Markers |', result)
        self.assertIn('› Hidden archive | Party (vision) | Camp | l01 |', result)
        self.assertNotIn('| Location | Present |', result)


class IndividualEntityTest(unittest.TestCase):
    def setUp(self):
        self.sources = {'time-markers': {'markers': []}, 'location-markers': {'places': {}, 'markers': []},
                        'entity-map': {'entities': [
                            dict(id='e01', label='Silver locket', importance='supporting'),
                            dict(id='e02', label='Pirate documents', importance='supporting', aliases=['Pirate papers'])]},
                        'combat': {'combats': []}}
        self.edit = dict(watches=[], locations=[], entities=[], combats=[])

    def test_grouped_duplicate_empty_or_nonlist_ids_are_rejected(self):
        for ids in (['e01', 'e02'], ['e01', 'e01'], [], 'e01'):
            with self.subTest(ids=ids):
                self.edit['entities'] = [dict(ids=ids, summary='A shared description.')]
                with self.assertRaisesRegex(ValueError, 'exactly one entity ID'):
                    review.check_rows(self.edit, self.sources, {})

    def test_each_entity_retains_its_own_summary_and_aliases_stay_one_identity(self):
        self.edit.update(flags=[], dates='', entities=[
            dict(ids=['e01'], summary='Found inside the altar.'),
            dict(ids=['e02'], summary='Read for clues to the pirate hideout.')])
        review.check_rows(self.edit, self.sources, {})
        bundle = dict(data=dict(campaign='Entity fixture', sessionNumber=2), source=Path('/fixture/transcript.md'))
        paths = {key: Path('/fixture') / f'{key}.json' for key in review.VERSIONS}
        result = review.render(bundle, paths, self.sources, self.edit, Path('/fixture'), dict(recording=None, notes=[]))
        self.assertIn('| Silver locket | Found inside the altar. | e01 |', result)
        self.assertIn('| Pirate documents | Read for clues to the pirate hideout. | e02 |', result)
        self.assertEqual(result.count('| e02 |'), 1)

    def test_individual_rows_still_require_summaries_valid_ids_and_unique_entities(self):
        for row, message in [
            (dict(ids=['e01'], summary=' '), 'nonempty session-specific'),
            (dict(ids=['missing'], summary='A role.'), 'Invalid entity references')]:
            with self.subTest(row=row):
                self.edit['entities'] = [row]
                with self.assertRaisesRegex(ValueError, message):
                    review.check_rows(self.edit, self.sources, {})
        self.edit['entities'] = [dict(ids=['e01'], summary='A role.')] * 2
        with self.assertRaisesRegex(ValueError, 'Invalid entity references'):
            review.check_rows(self.edit, self.sources, {})


if __name__ == '__main__':
    unittest.main()
