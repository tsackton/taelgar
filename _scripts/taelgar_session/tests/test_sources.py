"""Behavioral source-library tests using only synthetic bundles and code copies."""
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from taelgar_session import sources, transcript, passages, storage

REPOSITORY = Path(__file__).resolve().parents[3]


class SharedSourceTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        self.root = self.vault / '_sessions/demo'
        self.cleaned = self.root / 'cleaned'
        self.cleaned.mkdir(parents=True)
        self.manifest = self.cleaned / 'demo-session.yaml'
        self.source = self.cleaned / 'demo-transcript.md'
        self.source.write_text('# Demo\n\n'
            '%% u0001:0-5, u0002:0-5 %%\nDM: Élan greets you.\n\n'
            '%% u0003:0-2 %%\nPC: I ask.\n\n'
            '%% u0003:2-5 %%\nDM: He answers.\n\n', encoding='utf-8', newline='\n')
        self.manifest.write_text('sourceType: transcript\nrealWorldDate: 2020-10-02\n'
            'drStart: 1748-04-12\ndrEnd: 1748-04-12\ntranscriptProcessing:\n  artifacts:\n'
            '    polishedMarkdown:\n      path: cleaned/demo-transcript.md\n',
            encoding='utf-8', newline='\n')
        self.originals = {p: p.read_bytes() for p in (self.manifest, self.source)}

    def test_load_and_windows_preserve_source_bytes_without_writes(self):
        bundle = sources.load(self.manifest, self.vault)
        self.assertEqual(bundle['coverage'], [('u0001', 0, 5), ('u0002', 0, 5), ('u0003', 0, 5)])
        self.assertEqual(bundle['sessionYaml'], '_sessions/demo/cleaned/demo-session.yaml')
        self.assertEqual(set(bundle['fingerprints']), {'cleaned/demo-session.yaml', 'cleaned/demo-transcript.md'})
        first = sources.window(bundle, 'u0002', 'u0002')
        self.assertIn('[u0001–u0002]', first)
        self.assertIn('Élan greets', first)
        self.assertNotIn('He answers', first)
        shared = sources.window(bundle, 'u0003', 'u0003')
        self.assertIn('I ask.', shared)
        self.assertIn('He answers.', shared)
        self.assertEqual(shared.count('[u0003–u0003]'), 1)
        self.assertEqual({p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}, self.originals)

    def test_evidence_cannot_split_combined_uid_turns(self):
        bundle = sources.load(self.manifest, self.vault)
        with self.assertRaisesRegex(sources.MapError, 'splits a polished turn'):
            sources.source_bounds(bundle, sources.source('u0002', 'u0003'), 'evidence')
        self.assertEqual(sources.source_bounds(bundle, sources.source('u0001', 'u0003'), 'evidence'), (0, 2))

    def test_missing_dates_need_explicit_policy_and_invalid_dates_still_fail(self):
        text = self.manifest.read_text(encoding='utf-8').replace('drStart: 1748-04-12', 'drStart: null')
        self.manifest.write_text(text, encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(transcript.SourceError, 'drStart'):
            sources.load(self.manifest, self.vault)
        self.assertIsNone(sources.load(self.manifest, self.vault, allow_unknown_dates=True)['data']['drStart'])
        self.manifest.write_text(text.replace('drStart: null', 'drStart: "1748-02-31"'), encoding='utf-8', newline='\n')
        with self.assertRaisesRegex(transcript.SourceError, 'drStart'):
            sources.load(self.manifest, self.vault, allow_unknown_dates=True)

    def test_changed_registered_hash_requires_inspection_opt_in(self):
        self.manifest.write_text(self.manifest.read_text(encoding='utf-8') + '      sha256: stale\n',
                                 encoding='utf-8', newline='\n')
        before = self.manifest.read_bytes()
        with self.assertRaisesRegex(transcript.SourceError, 'fingerprint'):
            sources.load(self.manifest, self.vault)
        bundle = sources.load(self.manifest, self.vault, allow_source_changes=True)
        self.assertEqual(bundle['sourceSha256'], storage.sha(self.source.read_bytes()))
        self.assertEqual(self.manifest.read_bytes(), before)

    def test_cleaned_coverage_is_verified_without_rewriting(self):
        cleaned = self.cleaned / 'demo-source-cleaned.md'
        cleaned.write_text('[u0001 | 0-1 | DM] abcde\n[u0002 | 1-2 | DM] fghij\n'
                           '[u0003 | 2-3 | PC] klmno\n', encoding='utf-8', newline='\n')
        self.manifest.write_text(self.manifest.read_text(encoding='utf-8')
            + '    cleaned:\n      path: cleaned/demo-source-cleaned.md\n', encoding='utf-8', newline='\n')
        sources.load(self.manifest, self.vault)
        cleaned.write_bytes(cleaned.read_bytes().replace(b'klmno', b'klmnop'))
        before = cleaned.read_bytes()
        with self.assertRaisesRegex(transcript.SourceError, 'completely cover'):
            sources.load(self.manifest, self.vault)
        self.assertEqual(cleaned.read_bytes(), before)

    def test_gap_or_overlap_in_shared_uid_is_rejected(self):
        for end in ('1', '3'):
            with self.subTest(end=end):
                self.source.write_bytes(self.originals[self.source].replace(b'u0003:0-2', f'u0003:0-{end}'.encode()))
                with self.assertRaisesRegex(transcript.SourceError, 'Gap or overlap'):
                    sources.load(self.manifest, self.vault)

    def test_read_guards_detect_changes_after_inspection(self):
        bundle = sources.load(self.manifest, self.vault)
        self.source.write_bytes(self.source.read_bytes() + b'\n')
        with self.assertRaisesRegex(sources.MapError, 'Input changed'):
            sources.check_inputs(bundle)

    def test_literal_parentheses_are_valid_source_speech(self):
        self.source.write_bytes(self.source.read_bytes().replace(b'greets', b'((the guide)) greets'))
        bundle = sources.load(self.manifest, self.vault)
        self.assertIn('((the guide))', sources.window(bundle, 'u0001', 'u0002'))
        self.assertNotIn('draft', bundle)

    def test_inline_omission_requires_exact_retained_text(self):
        turn = {'body': 'DM: Élan greets you, rolls dice, and answers.\n\n'}
        body = 'DM: Élan greets you, ((dice mechanics)) and answers.\n\n'
        self.assertTrue(passages.match_inline(turn, body))
        with self.assertRaisesRegex(transcript.SourceError, 'Unmarked change'):
            passages.match_inline(turn, body.replace('greets', 'attacks'))

    def test_entity_cli_needs_no_scene_or_processing_skill(self):
        code_root = self.vault / 'standalone-code'
        skill = code_root / '.agents/skills/check-session-entities/scripts'
        skill.mkdir(parents=True)
        for name in ('entity_map.py', 'entity_review_store.py'):
            shutil.copy2(REPOSITORY / '.agents/skills/check-session-entities/scripts' / name, skill / name)
        shutil.copytree(REPOSITORY / '_scripts/taelgar_session', code_root / '_scripts/taelgar_session',
                        ignore=shutil.ignore_patterns('tests', '__pycache__'))
        bundle = code_root / '_sessions/demo/cleaned'
        bundle.mkdir(parents=True)
        for path in (self.manifest, self.source):
            shutil.copy2(path, bundle / path.name)
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', PYTHONUTF8='0')
        env.pop('PYTHONPATH', None)
        result = subprocess.run([sys.executable, '-B', str(skill / 'entity_map.py'),
                                 '--session-yaml', str(bundle / self.manifest.name), 'inspect'],
                                cwd=self.vault, env=env, capture_output=True, text=True, encoding='utf-8')
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)['sessionYaml'], '_sessions/demo/cleaned/demo-session.yaml')
        self.assertFalse((code_root / '.agents/skills/map-transcript-scenes').exists())
        self.assertFalse((code_root / '.agents/skills/process-transcript').exists())

    def test_shared_lock_excludes_an_independent_source_reader_process(self):
        code = ("from pathlib import Path; from taelgar_session.storage import lock; "
                "import sys\nwith lock(Path(sys.argv[1])): print('acquired')")
        env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1',
                   PYTHONPATH=str(REPOSITORY / '_scripts'))
        with storage.lock(self.root):
            result = subprocess.run([sys.executable, '-B', '-c', code, str(self.root)],
                                    env=env, capture_output=True, text=True)
        self.assertNotEqual(result.returncode, 0)
        self.assertIn('Another writer', result.stderr)
        with storage.lock(self.root):
            pass


if __name__ == '__main__':
    unittest.main()
