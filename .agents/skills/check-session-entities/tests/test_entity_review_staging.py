import copy
import json
import unittest
from unittest.mock import patch
import test_entity_review as fixtures

api = fixtures.api


class StagingNoteTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.EntityReviewTests()
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        self.call = self.f.call
        self.vault = self.f.f.fixture.vault
        manifest = self.f.f.fixture.yaml
        data = api.scenes.draft.yaml.safe_load(manifest.read_bytes())
        data.update(campaign='Dunmari Frontier', sessionNumber=1)
        manifest.write_bytes(api.scenes.draft.yaml.safe_dump(data).encode('utf8'))
        bundle = self.f.f.load()
        challenge = self.call()
        self.call('confirmSourceChanges', token=challenge['token'])
        api.maps.save(bundle, self.f.f.proposal, api.store.sha(bundle['entityPath'].read_bytes()))
        self.f.f.bundle = bundle
        self.f.source_before = {path: path.read_bytes() for path in self.f.source_before}
        result = self.call()
        self.result = self.call('entityUpdate', token=result['token'], entity='e001', changes={'note': None})

    def create(self, name='New Ally', **fields):
        return self.call('createStagingNote', token=self.result['token'], entity='e001', name=name, **fields)

    def test_empty_note_is_linked_without_approval_and_sources_are_preserved(self):
        result = self.create(changes={'label': 'New session label', 'importance': 'star'})
        row = result['document']['entities'][0]
        note = self.vault / row['note']
        self.assertEqual(note.read_bytes(), b'')
        self.assertTrue(row['note'].startswith('Worldbuilding/Staging/'))
        self.assertTrue(row['note'].endswith('/New Ally.md'))
        self.assertEqual(row['label'], 'New session label')
        self.assertEqual(row['importance'], 'star')
        self.assertEqual(row['review']['status'], 'unreviewed')
        self.assertEqual(result['review']['history'][-1]['action'], 'createStagingNote')
        self.assertEqual(self.call()['token'], result['token'])
        for path, before in self.f.source_before.items():
            self.assertEqual(path.read_bytes(), before)

    def test_short_campaign_folder_is_reused_through_registry_aliases(self):
        folder = self.vault / 'Worldbuilding/Staging/Dunmar'
        folder.mkdir(parents=True)
        scripts = self.vault / '_scripts'
        scripts.mkdir()
        registry = {'campaigns': {'dunmar-frontier': {'name': 'Dunmar Frontier',
                    'aliases': [self.f.f.bundle['data']['campaign']], 'sessionRoot': 'dunmar-frontier'}}}
        (scripts / 'session_note_campaigns.json').write_text(json.dumps(registry), encoding='utf8')
        self.assertEqual(self.call()['session']['stagingFolder'], 'Worldbuilding/Staging/Dunmar')
        result = self.create('New Ally.md')
        self.assertEqual(result['document']['entities'][0]['note'], 'Worldbuilding/Staging/Dunmar/New Ally.md')
        self.assertEqual((folder / 'New Ally.md').read_bytes(), b'')

    def test_chasm_folder_matches_a_campaign_word(self):
        folder = self.vault / 'Worldbuilding/Staging/Chasm'
        folder.mkdir(parents=True)
        bundle = dict(self.f.f.bundle, data={'campaign': 'Into the Chasm'})
        self.assertEqual(api.staging.folder(bundle, api.scenes), 'Worldbuilding/Staging/Chasm')

    def test_cached_note_identities_avoid_reopening_vault_notes(self):
        note_index = [{'path': 'People/Grash.md', 'names': ['Grash', 'The guide']}]
        with patch.object(api.staging.os, 'walk', side_effect=AssertionError('Unexpected full vault scan')):
            with patch.object(type(self.vault), 'open',
                              side_effect=AssertionError('Unexpected cached note read')):
                self.assertEqual(api.staging.collisions(self.vault, 'New Ally', api.scenes, note_index), [])
        with self.assertRaisesRegex(ValueError, 'already exists'):
            self.create('the GUIDE', noteIndex=note_index)
        result = self.create(noteIndex=note_index)
        self.assertEqual((self.vault / result['document']['entities'][0]['note']).read_bytes(), b'')

    def test_uncached_note_frontmatter_is_still_checked(self):
        note = self.vault / 'People/Other.md'
        note.write_bytes(b'---\nname: Known Person\naliases: [New Ally]\n---\n')
        index = [{'path': 'People/Grash.md', 'names': ['Grash']}, {'path': 'People/Other.md'}]
        for name in ['OTHER', 'known person', 'new ally']:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'already exists'):
                self.create(name, noteIndex=index)
        self.assertFalse((self.vault / 'Worldbuilding').exists())

    def test_unsafe_names_and_invalid_edits_do_not_create_files(self):
        before = self.f.f.bundle['entityPath'].read_bytes()
        for name in ['', '../Escape', 'one/two', r'one\two', '.hidden', '_private', 'CON', 'LPT1', 'Bad:name', 'Bad.']:
            with self.subTest(name=name), self.assertRaises(ValueError):
                self.create(name)
        with self.assertRaises(ValueError):
            self.create('New Ally', changes={'kind': 'invalid'})
        with self.assertRaises(ValueError):
            self.create('New Ally', changes={'status': 'humanReviewed'})
        self.assertFalse((self.vault / 'Worldbuilding').exists())
        self.assertEqual(self.f.f.bundle['entityPath'].read_bytes(), before)

    def test_existing_filename_and_alias_collisions_never_overwrite(self):
        other = self.vault / 'People/Existing.md'
        other.write_text('---\nname: Known Person\naliases: [New Ally]\n---\nExisting text.\n', encoding='utf8')
        original = other.read_bytes()
        for name in ['existing', 'Known Person', 'new ally']:
            with self.subTest(name=name), self.assertRaisesRegex(ValueError, 'already exists'):
                self.create(name)
        self.assertEqual(other.read_bytes(), original)
        self.assertFalse((self.vault / 'Worldbuilding').exists())

    def test_stale_tokens_and_already_linked_entities_cannot_create_notes(self):
        changed = self.call('entityUpdate', token=self.result['token'], entity='e001', changes={'importance': 'cameo'})
        with self.assertRaisesRegex(ValueError, 'Stale review'):
            self.create()
        inspected = self.call(notes=['People/Grash.md'])
        linked = self.call('entityUpdate', token=inspected['token'], entity='e001', changes={'note': 'People/Grash.md'})
        self.result = linked
        with self.assertRaisesRegex(ValueError, 'already has a linked'):
            self.create()
        self.assertFalse((self.vault / 'Worldbuilding').exists())

    def test_interrupted_link_save_retains_empty_note_and_recovers_the_link(self):
        original = api.scenes.atomic
        failed = False
        def interrupt(root, relative, data):
            nonlocal failed
            if str(relative).endswith('-entity-map.json') and not failed:
                failed = True
                raise OSError('Interrupted link save')
            return original(root, relative, data)
        with patch.object(api.scenes, 'atomic', interrupt):
            with self.assertRaisesRegex(ValueError, 'Created empty note'):
                self.create()
        created = list((self.vault / 'Worldbuilding/Staging').rglob('New Ally.md'))
        self.assertEqual(len(created), 1)
        self.assertEqual(created[0].read_bytes(), b'')
        recovered = self.call()
        self.assertEqual(recovered['document']['entities'][0]['note'], created[0].relative_to(self.vault).as_posix())
        self.assertEqual(recovered['review']['history'][-1]['action'], 'createStagingNote')
