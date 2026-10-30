"""Behavioral tests: no live bundles or external services are mutated."""
import sys
sys.dont_write_bytecode = True
import argparse
import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import transcript_core as core
import transcript_pipeline as pipeline
import transcript_finalize as finalization
import yaml


class PipelineTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.parent = Path(self.temp.name).resolve()
        self.root = self.parent / 'session-001'
        self.root.mkdir()
        self.original = self.parent / 'raw.vtt'
        self.original.write_text('WEBVTT\n\n00:00:00.000 --> 00:00:03.000\nDM: Well, well, it got denser.\n\n00:00:03.000 --> 00:00:06.000\nPlayer: Anyways, I—I mean, are we going?\n')
        self.metadata = self.root / 'metadata.json'
        self.metadata.write_text(json.dumps({'campaign': 'Example', 'sessionNumber': 1, 'participants': [{'gameRole': 'DM'}, {'gameRole': 'Player'}]}))

    def tearDown(self):
        self.temp.cleanup()

    def init(self, **kwargs):
        args = argparse.Namespace(source=str(self.original), metadata=str(self.metadata), manifest=None, prepared=None, cleaned=None, chunk_words=1800)
        for k, v in kwargs.items(): setattr(args, k, v)
        with core.lock(self.root):
            return pipeline.initialize(self.root, args)

    def work(self, stage, chunk=None):
        with core.lock(self.root):
            path = pipeline.make_work(self.root, stage, chunk)['job']
        return core.read_json(path)

    def response(self, job, **kwargs):
        value = {'schemaVersion': 1, 'stage': job['stage'], 'chunkId': job['chunk']['id'], 'sourceSha256': job['sourceSha256'], **kwargs}
        p = self.root / job['responsePath']
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(value))
        with core.lock(self.root):
            return pipeline.submit(self.root, job['responsePath'])

    def review_issue(self, uid='u0001', **kwargs):
        return dict(uid=uid, target=dict(start=19, end=25, before='denser'), replacement='darker', kind='place', importance='material',
                    reason='A potentially misrecognized place description.',
                    recommendation='Consider darker as the candidate reading.',
                    question='Use darker, correct the wording, or leave unresolved?', **kwargs)

    def clean(self, **kwargs):
        return self.response(self.work('clean'), checks=sorted(core.CHECKS), edits=[], issues=[], mentions=[], **kwargs)

    def complete(self):
        self.clean()
        job = self.work('polish')
        self.response(job, turns=job['draftTurns'])
        self.response(self.work('quality'), verdict='pass', findings=[], checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'], note='Both turns retain repeated words, the false start, and the original question.')
        with core.lock(self.root): return pipeline.export(self.root)

    def finalize(self):
        with core.lock(self.root): return pipeline.finalize(self.root)

    def test_finalization_keeps_four_transcripts_and_metadata_only(self):
        self.init(); result = self.complete(); a = result['artifacts']
        self.metadata.unlink()  # Caller-supplied input is outside helper ownership.
        manifest = self.root / a['sessionMetadata']
        original_metadata = manifest.read_bytes() + b'# preserve this note\nextraField: untouched\n...\n'
        manifest.write_bytes(original_metadata)
        unrelated = self.root / 'cleaned/session-recap.md'
        unrelated.write_text('Unrelated recap.')
        retained = {a[k]: (self.root/a[k]).read_bytes() for k in finalization.RETAINED}
        result = self.finalize()
        self.assertTrue(result['finalized']); self.assertEqual(result['status'], 'complete')
        self.assertEqual({p.relative_to(self.root).as_posix() for p in self.root.rglob('*') if p.is_file()},
                         set(retained) | {a['sessionMetadata'], 'cleaned/session-recap.md'})
        for path, data in retained.items(): self.assertEqual((self.root/path).read_bytes(), data)
        self.assertEqual(unrelated.read_text(), 'Unrelated recap.')
        new_metadata = yaml.safe_load(manifest.read_bytes())
        del new_metadata[finalization.KEY]
        self.assertEqual(new_metadata, yaml.safe_load(original_metadata))
        self.assertIn(b'# preserve this note\nextraField: untouched', manifest.read_bytes())
        before = {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()}
        self.assertEqual(self.finalize(), result)
        self.assertEqual(self.init(), result)
        self.assertEqual(pipeline.status(self.root), result)
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob('*') if p.is_file()})

    def test_finalization_refuses_unfinished_work_stale_exports_and_manual_edits(self):
        self.init()
        with self.assertRaisesRegex(core.PipelineError, 'before finalization'): self.finalize()
        result = self.complete(); state, units = pipeline.load(self.root)
        units[0]['text'] += ' Yes.'
        source = self.root / state['artifacts']['cleaned']; old_source = source.read_bytes()
        source.write_text(core.render_units(units))
        with self.assertRaises(core.PipelineError): self.finalize()
        source.write_bytes(old_source)
        edited = self.root / result['artifacts']['polishedMarkdown']; edited.write_text('Human revision')
        with self.assertRaises(core.PipelineError): self.finalize()
        self.assertEqual(edited.read_text(), 'Human revision')
        self.assertTrue((self.root/core.STATE).is_file())
        self.assertFalse((self.root/finalization.PLAN).exists())

    def test_finalize_resumes_after_work_removal_without_releasing_lock(self):
        self.init(); result = self.complete(); a = result['artifacts']
        atomic = finalization.atomic
        def interrupt(root, relative, data):
            if relative == a['sessionMetadata']:
                self.assertFalse((self.root/core.WORK).exists())
                with self.assertRaises(core.PipelineError):
                    with core.lock(self.root): pass
                raise OSError('simulated interruption after retiring work')
            return atomic(root, relative, data)
        with patch.object(finalization, 'atomic', side_effect=interrupt):
            with self.assertRaises(OSError): self.finalize()
        self.assertEqual(pipeline.status(self.root)['status'], 'needs_finalization')
        self.assertTrue(self.finalize()['finalized'])
        self.assertFalse((self.root/finalization.PLAN).exists())

    def test_interrupted_finalization_refuses_a_later_source_change(self):
        self.init(); result = self.complete()
        with patch.object(finalization, 'finish', side_effect=OSError('interrupted before retirement')):
            with self.assertRaises(OSError): self.finalize()
        source = self.root/result['artifacts']['cleaned']
        source.write_text(source.read_text() + '\nHuman edit\n')
        with self.assertRaisesRegex(core.PipelineError, 'Permanent transcript changed'): self.finalize()
        self.assertTrue((self.root/core.STATE).is_file())
        self.assertIn('Human edit', source.read_text())

    def test_finalization_rejects_symlinks_and_protected_paths_in_work(self):
        self.init(); self.complete()
        linked = self.root/core.WORK/'external'; linked.symlink_to(self.original)
        original = self.original.read_bytes()
        with self.assertRaisesRegex(core.PipelineError, 'symlink|escapes'): self.finalize()
        self.assertEqual(self.original.read_bytes(), original)
        linked.unlink()
        state, units = pipeline.load(self.root)
        path = core.WORK + '/prepared.md'
        (self.root/path).write_bytes((self.root/state['artifacts']['prepared']).read_bytes())
        state['artifacts']['prepared'] = path
        (self.root/core.STATE).write_bytes(core.encoded(state))
        with self.assertRaisesRegex(core.PipelineError, 'permanent reference'): self.finalize()
        self.assertTrue((self.root/path).is_file())

    def test_finalized_status_detects_later_source_changes_without_recreating_work(self):
        self.init(); self.complete(); result = self.finalize()
        source = self.root/result['artifacts']['prepared']; source.write_text('Changed baseline')
        result = pipeline.status(self.root)
        self.assertEqual(result['status'], 'changed_after_finalization')
        self.assertFalse(result['outputsCurrent'])
        self.assertFalse((self.root/core.WORK).exists())
        self.assertEqual(self.init()['status'], 'changed_after_finalization')

    def test_new_source_end_to_end_and_idempotent_resume(self):
        raw = self.original.read_bytes()
        self.init()
        result = self.complete()
        self.assertEqual(result['status'], 'complete')
        self.assertTrue(result['outputsCurrent'])
        state = (self.root / core.STATE).read_bytes()
        self.init()
        self.assertEqual(state, (self.root / core.STATE).read_bytes())
        self.assertEqual(raw, self.original.read_bytes())
        payload = core.read_json(self.root / result['artifacts']['polishedJson'])
        self.assertEqual(payload['turns'][0]['text'], 'Well, well, it got denser.')
        self.assertTrue((self.root / result['artifacts']['polishedHtml']).exists())

    def test_completed_review_and_html_are_disposable_but_references_are_required(self):
        self.init();result=self.complete();a=result['artifacts']
        (self.root/a['review']).unlink();(self.root/a['polishedHtml']).unlink()
        self.assertEqual(pipeline.status(self.root)['status'],'complete')
        self.assertTrue(pipeline.status(self.root)['outputsCurrent'])
        # Re-export can restore these views from retained state without new editorial work.
        with core.lock(self.root):pipeline.export(self.root)
        self.assertTrue((self.root/a['review']).is_file())
        (self.root/a['polishedJson']).unlink()
        self.assertFalse(pipeline.status(self.root)['outputsCurrent'])

    def test_pending_review_sheet_is_not_disposable(self):
        self.init();job=self.work('clean');u=job['source'][0]
        issue=self.review_issue(u['uid'])
        self.response(job,checks=sorted(core.CHECKS),edits=[],issues=[issue],mentions=[])
        job=self.work('polish');self.response(job,turns=job['draftTurns'])
        self.response(self.work('quality'),verdict='pass',findings=[],checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'],note='Words and turns are intact.')
        with core.lock(self.root):result=pipeline.export(self.root)
        (self.root/result['artifacts']['review']).unlink()
        result=pipeline.status(self.root)
        self.assertFalse(result['outputsCurrent']);self.assertEqual(result['pendingMaterialIssues'],1)

    def test_drafts_cannot_count_as_complete(self):
        self.init()
        s = pipeline.status(self.root)
        self.assertEqual(s['pending']['clean'], ['chunk-001'])
        with self.assertRaises(core.PipelineError): self.work('polish')
        with self.assertRaises(core.PipelineError): pipeline.export(self.root)

    def test_smoothing_and_removed_repetition_are_rejected(self):
        self.init(); self.clean(); job = self.work('polish')
        for text in ['Well, it got denser.', 'Well, well, it grew denser.', 'Well, well, it got denser and darker.']:
            turns = copy.deepcopy(job['draftTurns']); turns[0]['text'] = text
            with self.assertRaisesRegex(core.PipelineError, 'changed words'): self.response(job, turns=turns)
        turns = copy.deepcopy(job['draftTurns']); turns[1]['text'] = 'Anyway, I mean, are we going?'
        with self.assertRaises(core.PipelineError): self.response(job, turns=turns)

    def test_punctuation_case_and_curly_quotes_are_allowed(self):
        units = core.parse_units("[u0001 | 0-1 | DM] we're going anyways\n")
        turns = core.draft_turns(units, []); turns[0]['text'] = 'We’re going, anyways.'
        core.validate_turns(turns, units, [])

    def test_markers_annotations_numbers_and_symbols_survive(self):
        units = core.parse_units('[u0001 | 0-1 | DM] {{Zara}} [laughs] [[Tollen]] + 1,000\n')
        for replacement in ['Zara [laughs] [[Tollen]] + 1,000', '{{Zara}} laughs [[Tollen]] + 1,000', '{{Zara}} [laughs] [[Tollen]] 1,000', '{{Zara}} [laughs] [[Tollen]] + 1.000']:
            turns = core.draft_turns(units, []); turns[0]['text'] = replacement
            with self.assertRaises(core.PipelineError): core.validate_turns(turns, units, [])

    def test_no_missing_duplicate_reordered_source(self):
        self.init(); self.clean(); job = self.work('polish')
        for turns in [job['draftTurns'][:1], job['draftTurns']*2, list(reversed(job['draftTurns']))]:
            with self.assertRaises(core.PipelineError): self.response(job, turns=turns)

    def test_speaker_correction_and_within_uid_split(self):
        self.init(); job = self.work('clean'); u = job['source'][0]
        split = u['text'].index('it')
        attribution = {'uid': u['uid'], 'start': split, 'end': len(u['text']), 'speaker': 'Player', 'reason': 'Explicit correction supplied by the test user', 'evidence': ['human correction']}
        self.response(job, checks=sorted(core.CHECKS), edits=[], issues=[], mentions=[], attributions=[attribution])
        job = self.work('polish')
        self.assertEqual([t['speaker'] for t in job['draftTurns']], ['DM','Player','Player'])
        self.response(job, turns=job['draftTurns'])
        source = (self.root / pipeline.status(self.root)['artifacts']['cleaned']).read_text()
        self.assertIn('| DM]', source)
        with self.assertRaises(core.PipelineError):
            bad = copy.deepcopy(job['draftTurns']); bad[0]['speaker'] = 'Player'; core.validate_turns(bad, job['source'], job['attributions'])
        self.response(self.work('quality'), verdict='pass', findings=[], checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'], note='The recorded speaker correction is retained in the split turn.')
        with core.lock(self.root): pipeline.export(self.root)
        result = self.finalize()
        metadata = yaml.safe_load((self.root/result['artifacts']['sessionMetadata']).read_text())
        self.assertEqual(metadata[finalization.KEY]['speakerCorrections'],
                         [{k: attribution[k] for k in ('uid', 'start', 'end', 'speaker')}])

    def test_unassessed_markers_block_and_material_acceptance_persists(self):
        self.init(); job=self.work('clean');u=job['source'][0]
        edit={'uid':u['uid'],'before':u['text'],'after':'Well, well, it got {{denser}}.','kind':'uncertainty','reason':'Meaning uncertain','evidence':[u['uid']]}
        with self.assertRaisesRegex(core.PipelineError,'Unassessed'):
            self.response(job,checks=sorted(core.CHECKS),edits=[edit],issues=[],mentions=[])
        issue=self.review_issue(u['uid'])
        issue['target']=dict(start=19,end=29,before='{{denser}}')
        self.response(job,checks=sorted(core.CHECKS),edits=[edit],issues=[issue],mentions=[])
        job=self.work('polish');self.response(job,turns=job['draftTurns'])
        self.response(self.work('quality'), verdict='pass',findings=[],checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'],note='Uncertainty is explicitly retained.')
        with core.lock(self.root): result=pipeline.export(self.root)
        self.assertEqual(result['status'],'needs_manual_review')
        with self.assertRaises(core.PipelineError): self.finalize()
        state,units=pipeline.load(self.root);issue_id=pipeline.all_issues(state,units)[0]['id']
        with core.lock(self.root): pipeline.accept(self.root,issue_id,'User explicitly accepted this uncertainty');result=pipeline.export(self.root)
        self.assertEqual(result['status'],'complete_with_uncertainty')
        self.assertEqual(pipeline.all_issues(*pipeline.load(self.root))[0]['disposition'],'accepted')
        finalized = self.finalize()
        self.assertEqual(finalized['status'], 'complete_with_uncertainty')
        self.assertIn('{{denser}}', (self.root/finalized['artifacts']['cleaned']).read_text())
        self.assertIn('{{denser}}', (self.root/finalized['artifacts']['polishedMarkdown']).read_text())

    def test_stale_response_and_output_detection(self):
        self.init();job=self.work('clean')
        state,units=pipeline.load(self.root);units[0]['text'] += ' Oh.'
        (self.root / state['artifacts']['cleaned']).write_bytes(core.render_units(units).encode('utf-8'))
        with self.assertRaisesRegex(core.PipelineError,'Stale'): self.response(job,checks=sorted(core.CHECKS),edits=[],issues=[],mentions=[])
        self.complete()
        state,units=pipeline.load(self.root)
        (self.root / state['artifacts']['polishedMarkdown']).write_text('human edit')
        self.assertFalse(pipeline.status(self.root)['outputsCurrent'])
        with self.assertRaisesRegex(core.PipelineError,'manual changes'): pipeline.export(self.root)
        self.assertEqual((self.root / state['artifacts']['polishedMarkdown']).read_text(),'human edit')

    def test_writes_cannot_escape_bundle(self):
        self.init()
        for path in ['../outside.txt', str(self.parent / 'absolute.txt')]:
            with self.assertRaises(core.PipelineError): core.commit(self.root,{path:b'bad'},'escape test')
        (self.root / 'linked').symlink_to(self.parent, target_is_directory=True)
        with self.assertRaises(core.PipelineError): core.commit(self.root,{'linked/escape.txt':b'bad'},'escape test')
        self.assertFalse((self.parent / 'outside.txt').exists())

    def test_interrupted_transaction_recovers_without_losing_work(self):
        self.init()
        atomic=core.atomic
        def fail(root,path,data):
            if path.endswith('second.json'): raise OSError('simulated interruption')
            return atomic(root,path,data)
        with core.lock(self.root):
            with patch.object(core,'atomic',side_effect=fail):
                with self.assertRaises(OSError):core.commit(self.root,{'cleaned/first.json':b'first','cleaned/second.json':b'second'},'test recovery')
            self.assertEqual((self.root/'cleaned/first.json').read_bytes(),b'first')
            self.assertEqual(len(core.recover(self.root)),1)
        self.assertEqual((self.root/'cleaned/second.json').read_bytes(),b'second')

    def test_recovery_refuses_conflicting_edits(self):
        self.init();atomic=core.atomic
        def fail(root,path,data):
            if path.endswith('second.json'):raise OSError('stop')
            return atomic(root,path,data)
        with core.lock(self.root):
            with patch.object(core,'atomic',side_effect=fail):
                with self.assertRaises(OSError):core.commit(self.root,{'cleaned/first.json':b'first','cleaned/second.json':b'second'},'test')
            (self.root/'cleaned/first.json').write_text('human changed')
            with self.assertRaises(core.PipelineError):core.recover(self.root)

    def test_old_absolute_paths_are_rebased_inside_copy(self):
        self.init();state,_=pipeline.load(self.root)
        p=pipeline.local_reference(self.root,'/some/other/live/session/sources/raw.vtt','sources')
        self.assertEqual(p,self.root/state['artifacts']['original'])
        for reference in (r'C:\some\other\session\sources\raw.vtt', r'\\server\share\session\sources\raw.vtt'):
            self.assertEqual(pipeline.local_reference(self.root,reference,'sources'),p)

    def test_independent_bundles_have_independent_locks(self):
        self.init();other=self.parent/'session-002';other.mkdir()
        with core.lock(self.root):
            with core.lock(other): pass
            with self.assertRaises(core.PipelineError):
                with core.lock(self.root): pass


    def test_acceptance_expires_when_relevant_context_changes(self):
        self.init(); job=self.work('clean'); u=job['source'][0]
        issue=self.review_issue(u['uid'])
        self.response(job,checks=sorted(core.CHECKS),edits=[],issues=[issue],mentions=[])
        state,units=pipeline.load(self.root); issue_id=pipeline.all_issues(state,units)[0]['id']
        with core.lock(self.root): pipeline.accept(self.root,issue_id,'Actual test user decision')
        job=self.work('clean','chunk-001');v=job['source'][1]
        edit=dict(uid=v['uid'],before=v['text'],after=v['text']+' No.',kind='asr',reason='User supplied the missing answer',evidence=['test user correction'])
        self.response(job,checks=sorted(core.CHECKS),edits=[edit],issues=[issue],mentions=[])
        current=pipeline.all_issues(*pipeline.load(self.root))[0]
        self.assertNotEqual(issue_id,current['id']); self.assertEqual(current['disposition'],'pending')

    def test_changing_neighbor_polish_invalidates_quality(self):
        self.init(chunk_words=1)
        while pipeline.status(self.root)['pending']['clean']:
            self.clean()
        for chunk in ['chunk-001','chunk-002']:
            job=self.work('polish',chunk);self.response(job,turns=job['draftTurns'])
        q=self.work('quality','chunk-001')
        self.response(q,verdict='pass',findings=[],checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'],note='Both turns and the boundary are intact.')
        job=self.work('polish','chunk-002');turns=job['draftTurns'];turns[0]['text']=turns[0]['text'].replace('—','...')
        self.response(job,turns=turns)
        self.assertIn('chunk-001',pipeline.status(self.root)['pending']['quality'])

    def test_chunk_join_preserves_continuation_and_all_source_spans(self):
        self.original.write_text('WEBVTT\n\n0 --> 1\nDM: He says,\n\n1 --> 2\nDM: maybe.\n')
        self.init(chunk_words=1)
        state,units=pipeline.load(self.root)
        # Explicitly exercise an older chunk boundary in the middle of a sentence.
        state['chunks']=[dict(id='chunk-001',startUid='u0001',endUid='u0001'),dict(id='chunk-002',startUid='u0002',endUid='u0002')]
        (self.root/core.STATE).write_bytes(core.encoded(state))
        while pipeline.status(self.root)['pending']['clean']:self.clean()
        for chunk in state['chunks']:
            job=self.work('polish',chunk['id']);turns=job['draftTurns']
            if chunk['id']=='chunk-002':turns[0]['joinPrevious']=True
            self.response(job,turns=turns)
        with core.lock(self.root):result=pipeline.export(self.root)
        data=core.read_json(self.root/result['artifacts']['polishedJson'])
        self.assertEqual(len(data['turns']),1);self.assertEqual(data['turns'][0]['text'],'He says, maybe.')
        self.assertEqual(len(data['turns'][0]['sources']),2)

    def test_recovery_checks_unmodified_inputs(self):
        self.init();atomic=core.atomic
        def stop(root,path,data):
            if path.endswith('second.json'):raise OSError('simulated interruption')
            return atomic(root,path,data)
        source='cleaned/source-dependency.txt';(self.root/source).write_text('reviewed input')
        with core.lock(self.root):
            with patch.object(core,'atomic',side_effect=stop):
                with self.assertRaises(OSError):core.commit(self.root,{'cleaned/first.json':b'1','cleaned/second.json':b'2'},'dependent operation',{source:core.sha('reviewed input')})
            (self.root/source).write_text('changed after crash')
            with self.assertRaisesRegex(core.PipelineError,'input changed'):core.recover(self.root)
        self.assertFalse((self.root/'cleaned/second.json').exists())

    def test_caption_formats_and_unsupported_text_fail_loudly(self):
        for text in ['WEBVTT\n\n00:00:00.000 --> 00:00:01.000\n<v Speaker A>Hello!</v>\n', '1\n00:00:00,000 --> 00:00:01,000\nSpeaker A: Hello!\n', '[0-1] Speaker A: Hello!\n']:
            units=pipeline.parse_raw(text,[dict(gameRole='DM',transcriptIdentifiers=['Speaker A'])])
            self.assertEqual(units[0]['speaker'],'DM');self.assertEqual(units[0]['text'],'Hello!')
        for text in ['WEBVTT\nUnparsed speech\n\n0 --> 1\nDM: Hi\n', 'WEBVTT\n\n0 --> 1\n<v DM>Hello</v><v Player>Hi</v>\n', 'Untimed speech must not disappear']:
            with self.assertRaises(core.PipelineError):pipeline.parse_raw(text,[])

    def test_percentage_and_annotation_characters_cannot_disappear(self):
        units=core.parse_units('[u0001 | 0-1 | DM] A 50% chance, +2, -2, 1/2, [laughs].\n')
        for removed in ['%', '-']:
            turns=core.draft_turns(units,[]);turns[0]['text']=turns[0]['text'].replace(removed,'')
            with self.assertRaises(core.PipelineError):core.validate_turns(turns,units,[])

    def test_changed_attribution_text_needs_rechecked_spans(self):
        self.init();job=self.work('clean');u=job['source'][0]
        attribution=dict(uid=u['uid'],start=0,end=len(u['text']),speaker='Player',reason='Explicit identification',evidence=['test user correction'])
        self.response(job,checks=sorted(core.CHECKS),edits=[],issues=[],mentions=[],attributions=[attribution])
        job=self.work('clean','chunk-001');u=job['source'][0]
        edit=dict(uid=u['uid'],before=u['text'],after=u['text']+' Yes.',kind='asr',reason='Explicit wording correction',evidence=['test user correction'])
        with self.assertRaisesRegex(core.PipelineError,'recheck'):
            self.response(job,checks=sorted(core.CHECKS),edits=[edit],issues=[],mentions=[])

    def test_unchanged_attributions_do_not_alternate_stale_neighbor_chunks(self):
        self.init(chunk_words=1)
        for chunk, speaker in [('chunk-001', 'Player'), ('chunk-002', 'DM')]:
            job = self.work('clean', chunk)
            unit = job['source'][0]
            attribution = dict(uid=unit['uid'], start=0, end=len(unit['text']),
                               speaker=speaker, reason='Explicit speaker correction',
                               evidence=['test user correction'])
            self.response(job, checks=sorted(core.CHECKS), edits=[], issues=[],
                          mentions=[], attributions=[attribution])
        # The second correction genuinely changes the first chunk's context.
        self.assertEqual(pipeline.status(self.root)['pending']['clean'], ['chunk-001'])
        # Re-submission moves a chunk's unchanged overlays to the end of storage.
        # That storage order must not repeatedly invalidate its neighbor.
        for chunk in ['chunk-001', 'chunk-002', 'chunk-001', 'chunk-002']:
            self.response(self.work('clean', chunk), checks=sorted(core.CHECKS),
                          edits=[], issues=[], mentions=[])
            self.assertEqual(pipeline.status(self.root)['pending']['clean'], [])
        self.assertEqual(self.work('polish')['stage'], 'polish')

    def test_attribution_signatures_ignore_order_but_preserve_content_changes(self):
        self.init()
        state, units = pipeline.load(self.root)
        state['attributions'] = [
            dict(uid=unit['uid'], start=0, end=len(unit['text']), speaker='Other',
                 reason='Explicit speaker correction', evidence=['test user correction'],
                 textSha256=core.sha(unit['text'])) for unit in units
        ]
        reordered = copy.deepcopy(state)
        reordered['attributions'].reverse()
        for stage in ['clean', 'polish', 'quality']:
            with self.subTest(stage=stage):
                chunk = state['chunks'][0]
                expected = pipeline.signature(state, units, chunk, stage)
                self.assertEqual(expected, pipeline.signature(reordered, units, chunk, stage))
                for field, value in [('speaker', 'Someone else'), ('start', 1),
                                     ('end', len(units[0]['text']) - 1),
                                     ('reason', 'Revised identification'),
                                     ('evidence', ['another user correction'])]:
                    changed = copy.deepcopy(state)
                    changed['attributions'][0][field] = value
                    self.assertNotEqual(expected, pipeline.signature(changed, units, chunk, stage))

    def test_real_runtime_writes_are_confined_to_bundle(self):
        import os, subprocess
        # An audit hook in a child process observes all Python file writes, not only helper calls.
        script=r'''
import os, sys
from pathlib import Path
sys.dont_write_bytecode=True
import test_pipeline as t
root=Path(sys.argv[1]).resolve(); original=Path(sys.argv[2]); metadata=root/'metadata.json'
def audit(event,args):
    if event=='open' and isinstance(args[0],(str,bytes)):
        mode,flags=args[1],args[2]
        if (isinstance(mode,str) and any(c in mode for c in 'wax+')) or (isinstance(flags,int) and flags & (os.O_WRONLY|os.O_RDWR|os.O_CREAT|os.O_TRUNC)):
            path=Path(os.fsdecode(args[0])).resolve()
            if not path.is_relative_to(root):raise AssertionError('Out-of-bundle write: '+str(path))
    if event in {'os.mkdir','os.remove','os.rmdir','os.rename'}:
        for value in args[:2] if event=='os.rename' else args[:1]:
            if isinstance(value,(str,bytes)) and not Path(os.fsdecode(value)).resolve().is_relative_to(root):raise AssertionError('Out-of-bundle mutation: '+str(value))
sys.addaudithook(audit)
test=t.PipelineTests();test.root=root;test.original=original;test.metadata=metadata
test.init();test.complete();test.finalize()
import transcript_review as review
import test_review
with t.core.lock(root):review.prepare(root,['u0001'])
review_test=test_review.ReviewTests();review_test.root=root
review_test.decide(['correction'],{0:'Well, well, it got darker.'},'Well, well, it got darker.')
with t.core.lock(root):review.apply(root);review.finalize(root)
'''
        env=dict(os.environ,PYTHONPATH=os.pathsep.join([str(Path(__file__).parent),str(Path(core.__file__).parent)]),PYTHONDONTWRITEBYTECODE='1')
        result=subprocess.run([sys.executable,'-X','utf8','-B','-c',script,str(self.root),str(self.original)],env=env,capture_output=True,text=True)
        self.assertEqual(result.returncode,0,result.stderr)

    def test_polished_substitution_preserves_surrounding_words_and_source(self):
        units=core.parse_units('[u0001 | 0-1 | DM] Well, giant bald hammer, anyways.\n')
        turn=core.draft_turns(units,[])[0]
        start=units[0]['text'].index('giant');end=start+len('giant bald hammer')
        turn['substitutions']=[dict(uid='u0001',start=start,end=end,kind='garbled',reason='Unrecoverable incidental recognition debris.')]
        turn['text']='Well, [garbled], anyways.'
        core.validate_turns([turn],units,[])
        self.assertIn('giant bald hammer', units[0]['text'])
        for bad in ['[garbled], anyways.', 'Well, [garbled], anyway.', 'Well, [cross-talk], anyways.']:
            with self.subTest(text=bad), self.assertRaises(core.PipelineError):
                core.validate_turns([dict(turn,text=bad)],units,[])
        with self.assertRaises(core.PipelineError):
            core.validate_turns([dict(turn,substitutions=[])],units,[])

    def test_substitution_rejects_invalid_spans_labels_and_hidden_review(self):
        units=core.parse_units('[u0001 | 0-1 | DM] Ah, scrambled nonsense, {{Zara}} [laughs].\n')
        base=core.draft_turns(units,[])[0]
        r=dict(uid='u0001',start=4,end=22,kind='garbled',reason='Recognition debris.')
        base.update(text='Ah, [garbled], {{Zara}} [laughs].',substitutions=[r])
        core.validate_turns([base],units,[])
        for bad in [dict(r,uid='u0002'),dict(r,start=5),dict(r,end=200),dict(r,kind='omitted'),dict(r,reason=''),
                    dict(r,end=31),dict(r,start=32,end=40)]:
            with self.subTest(replacement=bad),self.assertRaises(core.PipelineError):
                core.validate_turns([dict(base,substitutions=[bad])],units,[])
        with self.assertRaisesRegex(core.PipelineError,'Overlapping'):
            core.validate_turns([dict(base,substitutions=[r,r])],units,[])

    def test_review_requires_concrete_decisions_and_excludes_incidental_appendix(self):
        self.init();job=self.work('clean');issue=self.review_issue()
        for key in ['target','replacement','recommendation','question']:
            bad=dict(issue);del bad[key]
            with self.assertRaisesRegex(core.PipelineError,key):
                self.response(job,checks=sorted(core.CHECKS),edits=[],issues=[bad],mentions=[])
        with self.assertRaisesRegex(core.PipelineError,'incidental'):
            self.response(job,checks=sorted(core.CHECKS),edits=[],issues=[dict(issue,importance='incidental')],mentions=[])
        self.response(job,checks=sorted(core.CHECKS),edits=[],issues=[issue],mentions=[])
        job=self.work('polish');self.response(job,turns=job['draftTurns'])
        with core.lock(self.root):result=pipeline.export(self.root)
        report=(self.root/result['artifacts']['review']).read_text()
        self.assertIn('Well, well, it got darker.',report);self.assertIn(issue['question'],report)
        self.assertIn(job['source'][0]['text'],report)
        self.assertNotIn('Incidental speech',report)

    def test_substitution_survives_join_export_and_finalization_without_altering_cleaned(self):
        self.original.write_text('WEBVTT\n\n0 --> 1\nDM: Hello.\n\n1 --> 2\nDM: scrambled nonsense\n')
        self.init(chunk_words=1)
        while pipeline.status(self.root)['pending']['clean']:self.clean()
        state,units=pipeline.load(self.root)
        baseline={k:(self.root/state['artifacts'][k]).read_bytes() for k in ['original','prepared','cleaned']}
        for chunk in state['chunks']:
            job=self.work('polish',chunk['id']);turns=job['draftTurns']
            if chunk['id']=='chunk-002':
                turns[0].update(text='[cross-talk]',joinPrevious=True,substitutions=[dict(uid='u0002',start=0,end=len(units[1]['text']),kind='cross-talk',reason='Clearly overlapping unintelligible voices.')])
            self.response(job,turns=turns)
        for chunk in state['chunks']:
            self.response(self.work('quality',chunk['id']),verdict='pass',findings=[],checks=['wording','punctuation','speaker_turns','uncertainty','boundary_continuity'],note='Both sides of the joined passage inspected, including the substitution.')
        with core.lock(self.root):result=pipeline.export(self.root)
        data=core.read_json(self.root/result['artifacts']['polishedJson'])
        self.assertEqual(data['turns'][0]['text'],'Hello. [cross-talk]')
        self.assertEqual(len(data['turns'][0]['substitutions']),1)
        self.assertEqual(result['displaySubstitutions'],1)
        self.assertEqual(result['status'],'complete_with_uncertainty')
        final=self.finalize()
        self.assertIn('[cross-talk]',(self.root/final['artifacts']['polishedMarkdown']).read_text())
        for k,v in baseline.items():self.assertEqual((self.root/final['artifacts'][k]).read_bytes(),v)

    def test_editorial_policy_change_invalidates_existing_reviews_without_reinitializing(self):
        self.init();self.complete()
        with patch.object(pipeline,'EDITORIAL_POLICY',pipeline.EDITORIAL_POLICY+1):
            result=pipeline.status(self.root)
            self.assertEqual(result['status'],'needs_work')
            self.assertFalse(result['outputsCurrent'])
            self.assertTrue(all(result['pending'].values()))
            job=self.work('clean')
            self.assertIsNotNone(job['previousReview'])


if __name__ == '__main__': unittest.main()
