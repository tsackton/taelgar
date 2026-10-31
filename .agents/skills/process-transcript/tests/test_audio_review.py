"""Audio review is a view over portable Markdown, never a transcript writer."""
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch
from urllib.request import Request, urlopen
from urllib.error import HTTPError

import transcript_audio_review as page
import transcript_core as core
import transcript_review as review
import transcript_corrections as corrections
import test_review as fixtures


class AudioReviewTests(unittest.TestCase):
    def setUp(self):
        self.f=fixtures.ReviewTests();self.f.setUp();self.addCleanup(self.f.tearDown)
        self.root=self.f.root
        self.a=self.f.export();self.f.handoff(self.a)
        self.cache=self.f.f.parent/'audio-page'
        self.recording=self.f.f.parent/'recording.m4a';self.recording.write_bytes(b'audio')
        self.mapping=dict(startUid='u0001',endUid='u0002',audioPath=str(self.recording),offsetSeconds=10,verified=True)
        self.patchers=[patch.object(page.audio,'probe_duration',return_value=40),
                       patch.object(page.audio,'resolve_clip_backend',return_value=page.audio.MediaBackend('ffmpeg','ffmpeg')),
                       patch.object(page.audio,'extract_audio_clip',side_effect=self.extract)]
        for p in self.patchers:p.start();self.addCleanup(p.stop)

    def extract(self,source,target,**kwargs): Path(target).write_bytes(b'm4a clip')

    def prepare(self,**kwargs):
        spec=dict(bundle=str(self.root),recordings=[self.mapping],**kwargs)
        return page.prepare(dict(sessions=[spec]),self.cache)

    def items(self): return page.items_for(self.root,self.cache,durations={})

    def save(self,item,choice='answer',text='Darker, not denser.'):
        return page.save_answer(self.root,item['issueId'],item['version'],choice,text)

    def test_prepare_and_save_only_review_markdown_changes(self):
        before=self.f.snapshot();self.prepare()
        item=self.items()[0]
        self.assertEqual(item['targetStart'],0)  # padded context cannot precede mapped segment
        self.save(item,text='It says "darker".\nSpeaker: [[Finnan]].')
        for name,data in before.items():
            if name!=self.a['review']:self.assertEqual((self.root/name).read_bytes(),data)
        current=review.inputs(self.root)[2][0]
        self.assertEqual(current['audio']['text'],'It says "darker".\nSpeaker: [[Finnan]].')
        self.assertEqual(current['resolution'],'pending')
        self.assertFalse((self.root/core.WORK).exists())
        self.assertEqual({p.name for p in self.cache.iterdir()}-{page.CACHE_MARKER,'index.html'}, {item['clip']})

    def test_defer_is_not_retained_acceptance_and_survives_rebuild(self):
        self.prepare();self.save(self.items()[0],choice='defer',text='Listen again later.')
        self.prepare()
        self.assertEqual(self.items()[0]['answer'],dict(choice='defer',text='Listen again later.'))
        self.assertEqual(review.read(self.root)[1]['retainedIssues'],0)
        with core.lock(self.root):
            self.assertEqual(review.apply(self.root)['pendingMaterialIssues'],1)
            with self.assertRaises(core.PipelineError):review.finalize(self.root)

    def test_incomplete_quality_is_not_replaced_by_an_audio_review(self):
        path,meta,issues,_,units,_,turns,_=review.inputs(self.root)
        meta['qualityComplete']=False
        path.write_text(review.document(meta,issues,units,turns))
        before=path.read_bytes()
        with self.assertRaisesRegex(core.PipelineError,'quality work'):self.prepare(uids=['u0002'])
        self.assertEqual(before,path.read_bytes())

    def test_partial_application_preserves_other_audio_answers(self):
        self.prepare(uids=['u0001','u0002'])
        items=self.items()
        for i in items:self.save(i,text='Answer for '+i['uid'])
        plan=dict(version=1,inputDigest=corrections.inspect(self.root)['inputDigest'],
                  decisions=[dict(id=items[0]['issueId'],resolution='retain')])
        corrections.apply(self.root,plan)
        self.assertEqual(review.read(self.root)[2][0]['audio']['text'],'Answer for u0002')
        self.assertEqual(len(self.items()),1)

    def test_stale_text_or_concurrent_answer_refuses_overwrite(self):
        self.prepare();item=self.items()[0];self.save(item)
        before=review.report_path(self.root).read_bytes()
        with self.assertRaisesRegex(core.PipelineError,'changed'):self.save(item,text='stale overwrite')
        self.assertEqual(before,review.report_path(self.root).read_bytes())
        item=self.items()[0]
        source=self.root/self.a['cleaned'];source.write_text(source.read_text().replace('denser','darker'))
        with self.assertRaisesRegex(core.PipelineError,'Transcript changed'):self.save(item)

    def test_standalone_selection_opens_finalized_review_without_processing(self):
        self.f.decide(['retain']);self.f.apply();self.f.finalize()
        before={k:(self.root/self.a[k]).read_bytes() for k in ('original','prepared','cleaned','polishedMarkdown','sessionMetadata')}
        self.prepare(uids=['u0002'])
        self.assertEqual(self.items()[0]['uid'],'u0002')
        self.assertFalse((self.root/core.WORK).exists())
        for k,data in before.items():self.assertEqual((self.root/self.a[k]).read_bytes(),data)

    def test_multisession_uids_have_distinct_keys(self):
        other=fixtures.ReviewTests();other.setUp();self.addCleanup(other.tearDown)
        artifacts=other.export();other.handoff(artifacts)
        specs=[dict(bundle=str(root),recordings=[self.mapping]) for root in (self.root,other.root)]
        result=page.prepare(dict(sessions=specs),self.cache)
        items=self.items()+page.items_for(other.root,self.cache,durations={})
        self.assertEqual(result['items'],2)
        self.assertNotEqual(items[0]['key'],items[1]['key'])
        self.assertEqual(items[0]['clip'],items[1]['clip'])  # same recording and time safely reuse a clip

    def test_clock_mapping_is_explicit_and_rejects_resets(self):
        units=[dict(uid='u0001',timing='0-1'),dict(uid='u0002',timing='0-2')]
        for mapping in [dict(self.mapping,verified=False),dict(self.mapping,offsetSeconds=-20)]:
            with self.assertRaises(page.audio.MediaToolError):page.audio.map_audio_range(units,[mapping],'u0001')
        units[0]['timing']='10-11'
        with self.assertRaisesRegex(page.audio.MediaToolError,'reset'):
            page.audio.map_audio_range(units,[self.mapping],'u0002')

    def test_failed_extraction_has_no_valid_cache_entry(self):
        def fail(source,target,**kwargs):
            target.write_bytes(b'partial');raise page.audio.MediaToolError('failed')
        with patch.object(page.audio,'extract_audio_clip',side_effect=fail):
            with self.assertRaises(page.audio.MediaToolError):self.prepare()
        self.assertFalse(list(self.cache.glob('*.m4a')))
        self.prepare();self.assertEqual(len(self.items()),1)

    def test_local_server_records_answers_and_rejects_unknown_requests(self):
        self.prepare()
        server=page.make_server([self.root],self.cache)
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        self.addCleanup(server.server_close);self.addCleanup(server.shutdown)
        base=f'http://127.0.0.1:{server.server_port}'
        with urlopen(base) as r:html=r.read().decode()
        token=html.split("const token='")[1].split("';")[0]
        with urlopen(base+'/api/review') as r:item=json.load(r)['items'][0]
        body=json.dumps(dict(key=item['key'],version=item['version'],choice='retain',text='Still unclear.')).encode()
        with self.assertRaises(HTTPError):urlopen(Request(base+'/api/answer',data=body))
        with urlopen(Request(base+'/api/answer',data=body,headers={'X-Review-Token':token})) as r:
            self.assertEqual(json.load(r)['answer']['choice'],'retain')
        self.assertEqual(review.read(self.root)[2][0]['resolution'],'pending')
        with self.assertRaises(HTTPError):urlopen(base+'/clips/../../metadata.json')

    def test_cleanup_preserves_answers_and_refuses_unrelated_files(self):
        self.prepare();self.save(self.items()[0]);before=review.report_path(self.root).read_bytes()
        extra=self.cache/'my-notes.txt';extra.write_text('Keep')
        with self.assertRaises(core.PipelineError):page.clean_cache(self.cache)
        self.assertTrue(extra.exists());extra.unlink();page.clean_cache(self.cache)
        self.assertFalse(self.cache.exists())
        self.assertEqual(before,review.report_path(self.root).read_bytes())


if __name__=='__main__':unittest.main()
