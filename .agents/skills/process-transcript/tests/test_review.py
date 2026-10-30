"""Review handoffs survive loss of all original work state."""
import copy
import json
from pathlib import Path
import re
import shutil
import unittest
from unittest.mock import patch
import yaml
import transcript_core as core
import transcript_pipeline as pipeline
import transcript_review as review
import transcript_finalize as final
import test_pipeline as fixtures


class ReviewTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.PipelineTests()
        self.f.setUp()
        self.root = self.f.root

    def tearDown(self): self.f.tearDown()

    def issue(self, unit, before, after, **extra):
        start = unit['text'].index(before)
        return dict(uid=unit['uid'], target=dict(start=start,end=start+len(before),before=before),
                    replacement=after, kind='action', importance='material', reason='Recognition concern in the example.',
                    recommendation='Use the supported candidate or retain the uncertainty.', question='Which words were spoken?', **extra)

    def export(self, issue_factory=None, raw=None, turns_factory=None, quality=True):
        if raw: self.f.original.write_text(raw)
        self.f.init()
        job = self.f.work('clean')
        issues = issue_factory(job['source']) if issue_factory else [self.f.review_issue()]
        self.f.response(job, checks=sorted(core.CHECKS), edits=[], issues=issues, mentions=[])
        job = self.f.work('polish')
        self.f.response(job, turns=turns_factory(job) if turns_factory else job['draftTurns'])
        if quality:
            self.f.response(self.f.work('quality'), verdict='pass', findings=[], checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'], note='Inspected the fixture, context, and substitution boundaries.')
        with core.lock(self.root): result = pipeline.export(self.root)
        return result['artifacts']

    def handoff(self, artifacts):
        # Simulate a fresh checkout containing exactly the retained references and MD.
        shutil.rmtree(self.root/core.WORK)
        for key in ('polishedJson','polishedHtml','entities'):
            (self.root/artifacts[key]).unlink()
        self.f.metadata.unlink()
        self.assertFalse((self.root/core.STATE).exists())

    def decide(self, resolutions, polished=None, correction=None):
        path, _, issues, _ = review.read(self.root)
        text = path.read_text()
        for issue, choice in zip(issues, resolutions):
            token = '%% transcript-issue:v1 '+json.dumps({k:issue[k] for k in ('id','uid','target','contextRange')},ensure_ascii=False)+' %%'
            start = text.index(token)
            end = text.find('%% transcript-issue:v1 ',start+len(token))
            if end < 0: end=len(text)
            section=text[start:end].replace('**Resolution:** pending','**Resolution:** '+choice,1)
            if correction is not None:section=section.replace('**Correction:** ','**Correction:** '+correction,1)
            text=text[:start]+section+text[end:]
        if polished:
            def update(match):
                value=json.loads(match[1])
                if value['index'] in polished:
                    result=polished[value['index']]
                    value.update(result if isinstance(result,dict) else {'after':result})
                return '%% transcript-polish:v1 '+json.dumps(value,ensure_ascii=False)+' %%'
            text=review.POLISH.sub(update,text)
        path.write_text(text)

    def apply(self):
        with core.lock(self.root): return review.apply(self.root)

    def finalize(self):
        with core.lock(self.root): return review.finalize(self.root)

    def snapshot(self): return {str(p.relative_to(self.root)):p.read_bytes() for p in self.root.rglob('*') if p.is_file()}

    def test_markdown_only_handoff_applies_and_finalizes(self):
        a=self.export();self.handoff(a)
        baseline={k:(self.root/a[k]).read_bytes() for k in ('original','prepared')}
        self.assertEqual(pipeline.status(self.root)['pendingMaterialIssues'],1)
        self.decide(['proposed'],{0:'Well, well, it got darker.'})
        result=self.apply();self.assertEqual(result['pendingMaterialIssues'],0)
        self.assertFalse((self.root/core.WORK).exists())
        self.assertEqual(self.apply()['pendingMaterialIssues'],0)
        result=self.finalize();self.assertTrue(result['outputsCurrent'])
        self.assertEqual(result['status'],'complete')
        self.assertEqual(len(self.snapshot()),5)
        self.assertIn('it got darker',(self.root/a['polishedMarkdown']).read_text())
        self.assertIn('- Status: Complete\n',(self.root/a['polishedMarkdown']).read_text())
        for k,v in baseline.items():self.assertEqual((self.root/a[k]).read_bytes(),v)

    def test_retain_has_clear_disposition_and_needs_no_polished_rewrite(self):
        a=self.export(lambda us:[self.issue(us[0],'denser',None)])
        report=(self.root/a['review']).read_text()
        self.assertIn('Retain unresolved; no supported correction',report)
        self.assertNotIn('**Proposed:**',report)
        self.handoff(a);self.decide(['retain']);self.apply()
        self.assertEqual(self.finalize()['status'],'complete_with_uncertainty')

    def test_original_and_proposal_cannot_replace_neighboring_text(self):
        unit=core.parse_units("[u0001 | 0-1 | A] the old Tina, gonna come at once. Tell Ulgna I'll be back.\n")[0]
        issue=self.issue(unit,'the old Tina, gonna','All ten are gonna')
        normalized=pipeline.validate_issues([issue],[unit])[0]
        self.assertEqual(normalized['proposal'],"All ten are gonna come at once. Tell Ulgna I'll be back.")
        with self.assertRaisesRegex(core.PipelineError,'outside'):
            review.replacement(dict(normalized,original=unit['text']), 'All ten are gonna come at once.')
        with self.assertRaisesRegex(core.PipelineError,'target'):
            pipeline.validate_issues([dict(issue,target=dict(start=0,end=999,before=unit['text']))],[unit])
        with self.assertRaisesRegex(core.PipelineError,'free-form'):
            pipeline.validate_issues([dict(issue,proposal='Duplicate neighboring speech.')],[unit])

    def test_collapsed_building_boundary_is_not_duplicated(self):
        raw='WEBVTT\n\n0 --> 1\nWazir: Six people word children a collapse.\n\n1 --> 2\nWazir: Building bodies never found.\n'
        def merged(job):
            return [dict(speaker='Wazir',sources=[s for t in job['draftTurns'] for s in t['sources']],text='Six people word children a collapse building. Bodies never found.')]
        a=self.export(lambda us:[self.issue(us[0],'word children a collapse.','were killed in a collapsed')],raw,merged)
        self.handoff(a);second=core.parse_units((self.root/a['cleaned']).read_text())[1]
        self.decide(['proposed'],{0:'Six people were killed in a collapsed building. Bodies never found.'})
        self.apply()
        self.assertEqual(core.parse_units((self.root/a['cleaned']).read_text())[1],second)
        self.assertEqual((self.root/a['polishedMarkdown']).read_text().count('building.'),1)

    def test_long_fragmented_exchange_and_explicit_context(self):
        units=core.parse_units('\n'.join(f'[u{i:04d} | {i}-{i+1} | '+('A' if i<15 else 'B')+'] words in this tiny caption.' for i in range(1,31)))
        bounds=review.context_range(units,'u0015')
        self.assertLess(int(bounds['startUid'][1:]),13)
        explicit=dict(startUid='u0002',endUid='u0028')
        self.assertEqual(review.context_range(units,'u0015',explicit),explicit)
        old=pipeline.issue_context(units,'u0015',explicit)
        units[2]['text']='Changed distant but displayed context.'
        self.assertNotEqual(old,pipeline.issue_context(units,'u0015',explicit))

    def test_partial_decisions_shift_remaining_targets_safely(self):
        raw='WEBVTT\n\n0 --> 1\nDM: Bob and Bob arrived.\n'
        def issues(us):
            first=self.issue(us[0],'Bob','Robert')
            second=self.issue(us[0],'Bob','Roberta');second['target']=dict(start=8,end=11,before='Bob')
            return [first,second]
        a=self.export(issues,raw);self.handoff(a)
        self.decide(['proposed','pending'],{0:'Robert and Bob arrived.'});self.apply()
        remaining=review.read(self.root)[2][0]
        self.assertEqual(remaining['target']['start'],11)
        self.assertEqual(remaining['proposal'],'Robert and Roberta arrived.')
        with self.assertRaises(core.PipelineError):self.finalize()
        self.decide(['proposed'],{0:'Robert and Roberta arrived.'});self.apply();self.finalize()

    def test_missing_or_unfaithful_polish_blocks_before_any_writes(self):
        a=self.export();self.handoff(a);self.decide(['proposed'])
        before=self.snapshot()
        with self.assertRaisesRegex(core.PipelineError,'polished text'):self.apply()
        self.assertEqual(before,self.snapshot())
        self.decide([],{0:'Well, it got darker and colder.'});before=self.snapshot()
        with self.assertRaisesRegex(core.PipelineError,'changed words'):self.apply()
        self.assertEqual(before,self.snapshot())

    def test_changed_reference_and_incomplete_quality_block(self):
        a=self.export(quality=False)
        self.decide(['retain'])
        with self.assertRaisesRegex(core.PipelineError,'quality'):self.apply()
        source=self.root/a['cleaned'];source.write_text(source.read_text().replace('denser','darker'))
        with self.assertRaisesRegex(core.PipelineError,'input changed'):review.status(self.root)

    def test_completed_bundle_can_reopen_without_work_state(self):
        self.f.init();a=self.f.complete()['artifacts'];self.f.finalize()
        manifest=self.root/a['sessionMetadata'];manifest.write_text(manifest.read_text()+'# preserve trailing comment\nextra: unchanged\n')
        with core.lock(self.root):review.prepare(self.root,['u0001'])
        self.decide(['correction'],{0:'Well, well, it got darker.'},'Well, well, it got darker.')
        self.apply();self.finalize()
        self.assertIn('# preserve trailing comment\nextra: unchanged',manifest.read_text())
        self.assertEqual(yaml.safe_load(manifest.read_text())['extra'],'unchanged')
        self.assertFalse((self.root/core.WORK).exists())

    def test_split_speaker_bounds_are_preserved_and_crossing_patch_rejected(self):
        self.f.init();job=self.f.work('clean');unit=job['source'][0];split=unit['text'].index('it')
        overlay=dict(uid=unit['uid'],start=split,end=len(unit['text']),speaker='Player',reason='User identification',evidence=['user'])
        self.f.response(job,checks=sorted(core.CHECKS),edits=[],issues=[],mentions=[],attributions=[overlay])
        job=self.f.work('polish');self.f.response(job,turns=job['draftTurns'])
        self.f.response(self.f.work('quality'),verdict='pass',findings=[],checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'],note='Reviewed split speakers.')
        with core.lock(self.root):a=pipeline.export(self.root)['artifacts'];pipeline.finalize(self.root);review.prepare(self.root,['u0001'])
        self.decide(['correction'],correction='Well, well, it got much darker.')
        with self.assertRaisesRegex(core.PipelineError,'boundary'):self.apply()
        path,meta,issues,updates=review.read(self.root)
        issues[0].update(target=dict(start=19,end=25,before='denser'),correction='much darker',resolution='correction')
        units=core.parse_units((self.root/a['cleaned']).read_text());turns,_=review.parse_markdown((self.root/a['polishedMarkdown']).read_text(),units)
        path.write_text(review.document(meta,issues,units,turns))
        self.decide([],{1:'it got much darker.'});self.apply();self.finalize()
        record=yaml.safe_load((self.root/a['sessionMetadata']).read_text())[final.KEY]
        self.assertNotIn('speakerCorrections', record)
        units=core.parse_units((self.root/a['cleaned']).read_text())
        turns,_=review.parse_markdown((self.root/a['polishedMarkdown']).read_text(),units)
        self.assertEqual(turns[1]['speaker'],'Player')
        self.assertEqual(turns[1]['sources'],[dict(uid='u0001',start=split,end=len('Well, well, it got much darker.'))])
        self.assertEqual(units[0]['speaker'],'DM')
        with core.lock(self.root):review.prepare(self.root,['u0001'])
        reopened=review.inputs(self.root)[6]
        self.assertEqual(reopened,turns)
        self.decide(['retain']);self.apply();self.finalize()
        self.assertNotIn('speakerCorrections',yaml.safe_load((self.root/a['sessionMetadata']).read_text())[final.KEY])

    def test_recovery_after_interrupted_markdown_application(self):
        a=self.export();self.handoff(a);self.decide(['proposed'],{0:'Well, well, it got darker.'})
        atomic=core.atomic
        def fail(root,path,data):
            if path==a['polishedMarkdown']:raise OSError('interrupted')
            return atomic(root,path,data)
        with patch.object(core,'atomic',side_effect=fail):
            with self.assertRaises(OSError):self.apply()
        with core.lock(self.root):core.recover(self.root)
        self.assertEqual(review.status(self.root)['pendingMaterialIssues'],0)
        self.finalize();self.assertFalse((self.root/core.WORK).exists())

    def test_quality_job_exposes_garbled_source_for_recovery(self):
        raw='WEBVTT\n\n0 --> 1\nDM: Church.\n'
        self.f.original.write_text(raw);self.f.init();self.f.clean()
        job=self.f.work('polish');turn=job['draftTurns'][0]
        turn.update(text='[garbled]',substitutions=[dict(uid='u0001',start=0,end=7,kind='garbled',reason='Prior incidental classification')])
        self.f.response(job,turns=[turn])
        self.assertEqual(self.f.work('quality')['recoveryCandidates'][0]['recognized'],'Church.')

    def test_recover_one_garbled_passage_preserves_another_without_old_state(self):
        raw='WEBVTT\n\n0 --> 1\nDM: Church.\n\n1 --> 2\nPlayer: scrambled nonsense\n'
        def garbled(job):
            turns=job['draftTurns']
            for turn in turns:
                span=turn['sources'][0]
                turn.update(text='[garbled]',substitutions=[dict(span,kind='garbled',reason='Prior incidental recognition debris')])
            return turns
        a=self.export(lambda us:[],raw,garbled)
        with core.lock(self.root):pipeline.finalize(self.root);review.prepare(self.root,['u0001'])
        self.decide(['correction'],{0:dict(after='[garbled]',substitutions=[dict(uid='u0001',start=0,end=5,kind='garbled',reason='Should not hide accepted words')])},'Sure.')
        before=self.snapshot()
        with self.assertRaisesRegex(core.PipelineError,'hides the accepted'):self.apply()
        self.assertEqual(before,self.snapshot())
        self.decide([],{0:dict(after='Sure.',substitutions=[])})
        self.apply();self.finalize()
        result=(self.root/a['polishedMarkdown']).read_text()
        self.assertIn('DM: Sure.',result)
        self.assertIn('Player: [garbled]',result)
        self.assertEqual(result.count('[garbled]'),1)

    def test_review_rejects_escaping_reference_paths_without_writes(self):
        a=self.export();self.handoff(a)
        path,meta,_,_=review.read(self.root)
        old=meta['artifacts']['original'];bad='../raw.vtt'
        meta['artifacts']['original']=bad;meta['hashes'][bad]=meta['hashes'].pop(old)
        path.write_text(review.HEADER.sub(lambda m:'%% transcript-review:v1 '+json.dumps(meta)+' %%',path.read_text()))
        before=self.snapshot();outside=self.f.original.read_bytes()
        with self.assertRaisesRegex(core.PipelineError,'escapes'):self.apply()
        self.assertEqual(before,self.snapshot());self.assertEqual(outside,self.f.original.read_bytes())


if __name__=='__main__':unittest.main()
