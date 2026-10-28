import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from process import build_index, inventory, sample, prepare
from batch import audit_chain
from session_model import apply_review, digest
import test_session_model as fixtures


class PreparationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.vault = Path(self.temp.name)
        (self.vault / '_scripts').mkdir()
        registry = {'campaigns':{'a':{'code':'a','sessionRoot':'a'},'b':{'code':'b','sessionRoot':'b'}}}
        (self.vault / '_scripts/session_note_campaigns.json').write_text(json.dumps(registry))
        for campaign in ['a','b']:
            for number in [1,2]:
                folder = self.vault / f'_sessions/{campaign}/{campaign}-{number}/cleaned'
                folder.mkdir(parents=True)
                (folder / f'{campaign}-{number}-session.yaml').write_text(f'sourceType: transcript\nsessionNumber: {number}\nrealWorldDate: 2026-10-28\ndrStart: unknown\nparticipants: []\n')
                (folder / f'{campaign}-{number}-source-cleaned.md').write_text('[u0001 | 00:00 | DM] A complete utterance.\n')
    def test_sample_is_reproducible_and_spans_campaigns(self):
        a = sample(self.vault,3,123); b = sample(self.vault,3,123)
        self.assertEqual(a,b)
        self.assertEqual({r['campaign'] for r in a['selected']},{'a','b'})
        self.assertEqual(len({r['id'] for r in a['selected']}),3)
    def test_narrative_excluded(self):
        p = self.vault / '_sessions/a/a-1/cleaned/a-1-session.yaml'
        p.write_text(p.read_text().replace('transcript','narrative'))
        rows, excluded = inventory(self.vault)
        self.assertEqual(len(rows),3); self.assertEqual(len(excluded),1)
    def test_unknown_date_omitted_and_resume_preserves_agent_work(self):
        selection = sample(self.vault,1,1)['selected'][0]
        folder = self.vault / 'work'
        prepare(self.vault,selection,{'entries':[]},folder)
        d = json.loads((folder/'draft.json').read_text())
        self.assertNotIn('dateStart',d)
        self.assertTrue(json.loads((folder/'execution.json').read_text())['dateIssues'])
        (folder/'draft.json').write_text('Agent work preserved verbatim')
        self.assertEqual(prepare(self.vault,selection,{'entries':[]},folder,resume=True),'preserved')
        self.assertEqual((folder/'draft.json').read_text(),'Agent work preserved verbatim')
    def test_changed_sample_source_rejected(self):
        selection = sample(self.vault,1,1)['selected'][0]
        (self.vault/selection['source']).write_text('[u0001 | DM] Changed.\n')
        with self.assertRaisesRegex(ValueError,'changed since sampling'):
            prepare(self.vault,selection,{'entries':[]},self.vault/'work')
    def test_index_handles_nulls_and_excludes_private_and_generated(self):
        for name in ['Public.md','_dm_notes/Private.md','Campaigns/_generated/Generated.md']:
            p = self.vault/name; p.parent.mkdir(parents=True,exist_ok=True)
            p.write_text('---\nname: Name\naliases: null\ntags: null\n---\nBody\n')
        (self.vault/'LooksPublic.md').symlink_to(self.vault/'_dm_notes/Private.md')
        self.assertEqual([e['path'] for e in build_index(self.vault)['entries']],['Public.md'])


class ChainTests(unittest.TestCase):
    def setUp(self):
        # Reuse realistic source/record fixtures, without rerunning the model tests.
        self.fixture = fixtures.ModelTests(); self.fixture.setUp(); self.addCleanup(self.fixture.doCleanups)
        self.vault = self.fixture.vault
        self.folder = self.vault/'run'; self.folder.mkdir()
        self.data = self.fixture.data
        self.report = self.fixture.report()
        self.report['decisions'].append({**self.report['decisions'][0], 'target':'session'})
        self.reviewed = apply_review(self.data,self.report,self.vault)
        self.save('extraction.json',self.data)
        self.save('review-decisions-0.json',self.report)
        self.save('session.json',self.reviewed)
        self.save('execution.json',{'fullTranscriptRead':True,'correctionAttempts':0})
    def save(self,name,data):
        (self.folder/name).write_text(json.dumps(data))
    def test_replay_preserves_reviewed_result(self):
        result,_ = audit_chain(self.folder,self.vault)
        self.assertEqual(result,self.reviewed)
    def test_post_review_claim_mutation_rejected(self):
        altered = copy.deepcopy(self.reviewed); altered['entities'][0]['label']='Different person'
        self.save('session.json',altered)
        with self.assertRaisesRegex(ValueError,'differs from'):
            audit_chain(self.folder,self.vault)
    def test_structural_only_completion_rejected(self):
        self.save('session.json',self.data)
        (self.folder/'review-decisions-0.json').unlink()
        with self.assertRaisesRegex(ValueError,'Expected initial review'):
            audit_chain(self.folder,self.vault)
    def correction(self, candidate, targets, removals=None):
        report = {'attempt':1, 'reviewer':'second pass',
                  'inputDigest':hashlib.sha256(json.dumps(candidate,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
                  'decisions':[{'target':t,'confidence':'high','reason':'Rechecked source context','evidence':[self.fixture.loc]} for t in targets]}
        if removals is not None:report['removals']=removals
        self.save('correction-candidate.json',candidate)
        self.save('review-decisions-1.json',report)
        self.save('session.json',apply_review(candidate,report,self.vault))
        self.save('execution.json',{'fullTranscriptRead':True,'correctionAttempts':1})
    def test_forged_root_human_approval_rejected(self):
        candidate=copy.deepcopy(self.reviewed)
        candidate['review']={'confidence':'high','status':'humanReviewed'}
        self.correction(candidate,['entity:guide'])
        with self.assertRaisesRegex(ValueError,'change review states'):
            audit_chain(self.folder,self.vault)
    def test_resetting_human_review_cannot_allow_automatic_overwrite(self):
        # A pre-existing human-reviewed entity is not targeted by the initial automated pass.
        self.data['entities'][0]['review']={'confidence':'high','status':'humanReviewed'}
        self.report=self.fixture.report(target='session')
        self.reviewed=apply_review(self.data,self.report,self.vault)
        self.save('extraction.json',self.data);self.save('review-decisions-0.json',self.report)
        candidate=copy.deepcopy(self.reviewed)
        candidate['entities'][0]['label']='Different person'
        candidate['entities'][0]['review']={'confidence':'low','status':'unreviewed'}
        self.correction(candidate,['entity:guide'])
        with self.assertRaisesRegex(ValueError,'human-reviewed record'):
            audit_chain(self.folder,self.vault)
    def test_unsupported_removal_rejected(self):
        candidate=copy.deepcopy(self.reviewed);candidate['entities']=[];candidate['interactions']=[]
        self.correction(candidate,['session'])
        with self.assertRaisesRegex(ValueError,'removal decisions'):
            audit_chain(self.folder,self.vault)
    def test_evidenced_removal_retained(self):
        candidate=copy.deepcopy(self.reviewed);candidate['entities']=[];candidate['interactions']=[]
        removals=[{'target':t,'reason':'No supported inclusion after contextual recheck','evidence':[self.fixture.loc]} for t in ['entity:guide','interaction:meet']]
        self.correction(candidate,['session'],removals)
        result,_=audit_chain(self.folder,self.vault)
        self.assertEqual(result['entities'],[])
    def test_sample_identity_and_source_are_bound(self):
        selection={'campaign':'test','session':1,'source':'source.md','sha256':digest(self.vault/'source.md')}
        audit_chain(self.folder,self.vault,selection)
        for field,bad in [('campaign','wrong'),('session',2),('source','Guide.md'),('sha256','0'*64)]:
            wrong={**selection,field:bad}
            with self.subTest(field=field),self.assertRaises(ValueError):
                audit_chain(self.folder,self.vault,wrong)


if __name__=='__main__':unittest.main()
