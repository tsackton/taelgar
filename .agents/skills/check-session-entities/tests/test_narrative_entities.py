import copy
from pathlib import Path
import tempfile
import unittest

from test_entity_map import e


class NarrativeEntityTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        self.root = self.vault / '_sessions/demo/demo-001'
        self.cleaned = self.root / 'cleaned'
        self.cleaned.mkdir(parents=True)
        self.yaml = self.cleaned / 'demo-001-session.yaml'
        self.source = self.cleaned / 'demo-001-source-prepared.md'
        self.source.write_text('[u0001] A scout arrives.\n[u0002] The scout returns the vial.\n', encoding='utf-8')
        self.write_yaml('cleaned/demo-001-source-prepared.md')
        self.proposal = {'entities': [{
            'id': 'e001', 'kind': 'npc', 'label': 'Scout', 'importance': 'supporting',
            'occurrences': [{'source': {'kind': 'narrative', 'sourceId': 'preparedSourcePath',
                                       'startUid': 'u0001', 'endUid': 'u0002'}}],
            'review': {'confidence': 'high', 'status': 'unreviewed'}}]}

    def write_yaml(self, path):
        self.yaml.write_text('sourceType: narrative\ncampaign: Demo\nsessionNumber: 1\n'
                             f'preparedSourcePath: {path}\n', encoding='utf-8')

    def load(self):
        return e.load(self.yaml, self.vault)

    def test_guarded_roundtrip_and_source_preservation(self):
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        bundle = self.load()
        doc = e.save(bundle, self.proposal)
        self.assertEqual(e.read_map(self.load()), doc)
        self.assertIn('A scout arrives.', e.preview(bundle, doc, 'e001'))
        self.assertIn('prepared narrative', e.window(bundle, 'u0001', 'u0002'))
        for p, raw in before.items():
            self.assertEqual(p.read_bytes(), raw)
        self.assertEqual({p for p in self.root.rglob('*') if p.is_file()} - before.keys(),
                         {bundle['entityPath']})
        with self.assertRaisesRegex(ValueError, 'expect-sha256'):
            e.save(bundle, self.proposal)

    def test_source_and_yaml_changes_stale_map_and_guard(self):
        for path in (self.source, self.yaml):
            with self.subTest(path=path):
                original = path.read_bytes()
                bundle = self.load()
                doc = e.build(bundle, self.proposal)
                path.write_bytes(original + (b'[u0003] Changed.\n' if path == self.source else b'participants: []\n'))
                with self.assertRaisesRegex(ValueError, 'inputs changed'):
                    e.validate(self.load(), doc)
                with self.assertRaisesRegex(ValueError, 'Input changed'):
                    e.save(bundle, self.proposal)
                path.write_bytes(original)

    def test_wrong_source_unknown_reversed_and_duplicate_uids(self):
        for patch in ({'kind': 'transcript'}, {'sourceId': 'cleaned'},
                      {'startUid': 'u9999'}, {'startUid': 'u0002', 'endUid': 'u0001'}):
            proposal = copy.deepcopy(self.proposal)
            proposal['entities'][0]['occurrences'][0]['source'].update(patch)
            with self.assertRaises(ValueError):
                e.build(self.load(), proposal)
        self.source.write_text('[u0001] First.\n[u0001] Duplicate.\n', encoding='utf-8')
        with self.assertRaisesRegex(ValueError, 'Duplicate UID'):
            self.load()

    def test_legacy_relocation_is_exact_and_paths_are_safe(self):
        self.write_yaml('/old/vault/_sessions/demo/demo-001/cleaned/demo-001-source-prepared.md')
        self.assertEqual(self.load()['source'], self.source)
        for path in ('../escape.md', '/old/demo-002/cleaned/demo-001-source-prepared.md'):
            self.write_yaml(path)
            with self.assertRaises(ValueError):
                self.load()
        self.write_yaml('cleaned/demo-001-source-prepared.md')
        self.source.unlink()
        self.source.symlink_to(self.yaml)
        with self.assertRaises(ValueError):
            self.load()
