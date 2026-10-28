"""Opt-in regression on temporary copies; the configured vault is read-only."""
import sys
sys.dont_write_bytecode=True
import argparse
import os
from pathlib import Path
import shutil
import tempfile
import unittest
import transcript_core as core
import transcript_pipeline as pipeline

CASES=['dunmar-frontier/dunmari-frontier-053','dunmar-frontier/dunmari-frontier-139','dragonets/dragonets-002','feywild/lost-in-the-feywild-004','into-the-chasm/into-the-chasm-001','lablost/labyrinths-of-the-lost-001','mawar/mawar-adventures-002']

def snapshot(root):
    return {str(p.relative_to(root)):core.sha(p.read_bytes()) for p in root.rglob('*') if p.is_file()}

@unittest.skipUnless(os.environ.get('TRANSCRIPT_TEST_VAULT'),'Set TRANSCRIPT_TEST_VAULT to test temporary copies of real bundles')
class ExistingBundles(unittest.TestCase):
    def test_campaign_resolution_is_read_only(self):
        vault=Path(os.environ['TRANSCRIPT_TEST_VAULT']).resolve()
        result=pipeline.resolve(vault,'dunmar','53')
        self.assertEqual(Path(result['bundle']),vault/'_sessions/dunmar-frontier/dunmari-frontier-053')

    def test_copy_normalization_preserves_work_and_live_sources(self):
        vault=Path(os.environ['TRANSCRIPT_TEST_VAULT']).resolve()
        for case in CASES:
            with self.subTest(bundle=case), tempfile.TemporaryDirectory() as tmp:
                live=vault/'_sessions'/case;before=snapshot(live)
                root=Path(tmp).resolve()/live.name;shutil.copytree(live,root)
                args=argparse.Namespace(source=None,metadata=None,manifest=None,prepared=None,cleaned=None,chunk_words=1800)
                with core.lock(root):result=pipeline.initialize(root,args)
                state,units=pipeline.load(root)
                self.assertGreater(len(units),500)
                self.assertEqual(result['status'],'needs_work')
                for kind in ['original','prepared','cleaned']:
                    relative=state['artifacts'][kind]
                    expected=(live/relative).read_bytes()
                    if kind!='original':expected=core.render_units(core.parse_units(expected.decode('utf-8-sig'))).encode()
                    self.assertEqual((root/relative).read_bytes(),expected)
                managed={state['artifacts'][k] for k in ['original','prepared','cleaned']}
                for relative,digest in before.items():
                    if relative not in managed:self.assertEqual(core.sha((root/relative).read_bytes()),digest)
                with core.lock(root):job=core.read_json(pipeline.make_work(root,'clean')['job'])
                if case in CASES[1:4]:self.assertTrue(job['legacyCandidates'])
                resumed=(root/core.STATE).read_bytes()
                with core.lock(root):pipeline.initialize(root,args)
                self.assertEqual(resumed,(root/core.STATE).read_bytes())
                self.assertEqual(snapshot(live),before)
                print(f'Copied-bundle check: {case}: {len(units)} UIDs, live source unchanged')

if __name__=='__main__':unittest.main()
