import copy
import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from jsonschema import ValidationError
from session_model import validate, ready, critical_queue, apply_review, render

class ModelTests(unittest.TestCase):
    def setUp(self):
        self.temp=tempfile.TemporaryDirectory();self.addCleanup(self.temp.cleanup)
        self.vault=Path(self.temp.name)
        (self.vault/'source.md').write_text('[u0001 | DM] A guide waits.\n[u0002 | DM] Follow me.\n[u0003 | PC] We leave.\n')
        (self.vault/'Guide.md').write_text('A guide.\n')
        (self.vault/'PC.md').write_text('A PC.\n')
        self.loc={'kind':'transcript','sourceId':'t','startUid':'u0001','endUid':'u0003'}
        self.data={'schemaVersion':5,'campaign':'test','session':1,'realWorldDate':'2026-10-28','pcs':['PC.md'],
                   'sources':[{'id':'t','kind':'transcript','path':'source.md'}],
                   'scenes':[{'index':1,'source':copy.deepcopy(self.loc)}],
                   'entities':[{'id':'guide','kind':'npc','label':'Guide','note':'Guide.md'}],
                   'interactions':[{'id':'meet','entity':'guide','scenes':[1],'interaction':'interacted'}]}
    def report(self,target='entity:guide',confidence='high'):
        return {'inputDigest':hashlib.sha256(json.dumps(self.data,sort_keys=True,ensure_ascii=False).encode()).hexdigest(),
                'reviewer':'separate review pass','attempt':0,'decisions':[{'target':target,'confidence':confidence,
                'reason':'Guide is introduced and speaks in this passage.','evidence':[self.loc,{'vaultPath':'Guide.md'}]}]}
    def test_minimal_session(self):
        for k in ['scenes','entities','interactions']:del self.data[k]
        validate(self.data,self.vault)
        self.assertFalse(ready(self.data))
    def test_required_source(self):
        self.data['sources']=[]
        with self.assertRaises(ValidationError):validate(self.data,self.vault)
    def test_required_metadata(self):
        for k in ['pcs','realWorldDate']:
            d=copy.deepcopy(self.data);del d[k]
            with self.assertRaises(ValidationError):validate(d,self.vault)
    def test_minimal_records_and_missing_review(self):
        result=validate(self.data,self.vault)
        self.assertEqual(result['provisionalEntities'],1)
        self.assertEqual(len(critical_queue(self.data)),2)
    def test_individual_scene_review_rejected(self):
        self.data['scenes'][0]['review']={'confidence':'high','status':'unreviewed'}
        with self.assertRaises(ValidationError):validate(self.data,self.vault)
    def test_scene_collection_review(self):
        self.data['sceneReview']={'confidence':'medium','status':'automatedReviewed'}
        validate(self.data,self.vault)
    def test_changed_hash(self):
        self.data['sources'][0]['sha256']='0'*64
        with self.assertRaisesRegex(ValueError,'hash changed'):validate(self.data,self.vault)
    def test_broken_source_and_scene_joins(self):
        self.data['scenes'][0]['source']['sourceId']='missing'
        with self.assertRaisesRegex(ValueError,'Unknown source'):validate(self.data,self.vault)
        self.data['scenes'][0]['source']['sourceId']='t';self.data['interactions'][0]['scenes']=[2]
        with self.assertRaisesRegex(ValueError,'Broken scene'):validate(self.data,self.vault)
    def test_quote_and_featured_provenance(self):
        q={'id':'q','type':'color','text':'Follow me.','source':{**self.loc,'startUid':'u0002','endUid':'u0002'}}
        self.data['interactions'][0]['quotes']=[q]
        self.data['entities'][0]['aiSuggestedFeaturedQuotes']=['q']
        validate(self.data,self.vault)
        q['text']='Please follow me.'
        with self.assertRaisesRegex(ValueError,'not verbatim'):validate(self.data,self.vault)
    def test_passage_bounds(self):
        self.data['scenes'][0]['source']['endUid']='u0002'
        self.data['interactions'][0]['passages']=[{'source':self.loc}]
        with self.assertRaisesRegex(ValueError,'outside referenced'):validate(self.data,self.vault)
    def test_summary_limit(self):
        self.data['scenes'][0]['aiSummary']=' '.join(['word']*26)
        with self.assertRaisesRegex(ValueError,'25 words'):validate(self.data,self.vault)
    def test_organization_supported(self):
        self.data['entities'][0]['kind']='organization'
        validate(self.data,self.vault)
    def test_readiness_independent_of_validation(self):
        self.data['review']={'confidence':'high','status':'unreviewed'}
        validate(self.data,self.vault);self.assertFalse(ready(self.data))
        self.data['review']['status']='automatedReviewed';self.assertTrue(ready(self.data))
        self.data['review']={'confidence':'low','status':'humanReviewed'};self.assertFalse(ready(self.data))
    def test_stale_review_rejected(self):
        report=self.report();self.data['entities'][0]['label']='Changed'
        with self.assertRaisesRegex(ValueError,'Stale review'):apply_review(self.data,report,self.vault)
    def test_review_requires_evidence(self):
        report=self.report();report['decisions'][0]['evidence']=[]
        with self.assertRaisesRegex(ValueError,'evidence'):apply_review(self.data,report,self.vault)
    def test_review_promotes_only_target(self):
        reviewed=apply_review(self.data,self.report(),self.vault)
        self.assertTrue(ready(reviewed['entities'][0]));self.assertFalse(ready(reviewed))
        self.assertNotIn('review',self.data['entities'][0])
    def test_review_can_keep_medium_confidence(self):
        reviewed=apply_review(self.data,self.report(confidence='medium'),self.vault)
        self.assertFalse(ready(reviewed['entities'][0]))
    def test_human_review_protected(self):
        self.data['entities'][0]['review']={'confidence':'high','status':'humanReviewed'}
        with self.assertRaisesRegex(ValueError,'overwrite human'):apply_review(self.data,self.report(),self.vault)
    def test_retry_limit(self):
        report=self.report();report['attempt']=2
        with self.assertRaisesRegex(ValueError,'At most one'):apply_review(self.data,report,self.vault)
    def test_private_reference_rejected(self):
        self.data['entities'][0]['note']='../Guide.md'
        with self.assertRaisesRegex(ValueError,'escapes vault'):validate(self.data,self.vault)
    def test_private_symlink_rejected(self):
        private=self.vault/'_dm_notes';private.mkdir()
        (private/'secret.md').write_text('Private lore')
        (self.vault/'Public.md').symlink_to(private/'secret.md')
        self.data['entities'][0]['note']='Public.md'
        with self.assertRaisesRegex(ValueError,'Private source'):validate(self.data,self.vault)
    def test_render_marks_provisional_records(self):
        output=render(self.data,self.vault,self.vault/'review.md')
        self.assertIn('Provisional critical metadata',output)
        self.assertIn('Provisional entity',output)
        self.assertIn('?plain=1#L1',output)

if __name__=='__main__':unittest.main()
