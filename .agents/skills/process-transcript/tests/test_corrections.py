"""Bounded correction regressions on isolated session bundles only."""
import json
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import patch

import yaml
import transcript_core as core
import transcript_corrections as corrections
import transcript_finalize as final
import transcript_review as review
import test_review as fixtures


class CorrectionTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.ReviewTests()
        self.f.setUp()
        self.root = self.f.root

    def tearDown(self): self.f.tearDown()

    def completed(self):
        self.f.f.init()
        self.a = self.f.f.complete()['artifacts']
        self.f.f.finalize()

    def plan(self, **kwargs):
        return dict(version=1, inputDigest=corrections.inspect(self.root)['inputDigest'], **kwargs)

    def edit(self, after='much darker'):
        return dict(uid='u0001', start=19, end=25, before='denser', after=after)

    def turn(self, **kwargs):
        return dict(index=0, before='Well, well, it got denser.', **kwargs)

    def text(self, key): return (self.root/self.a[key]).read_text()

    def turns(self):
        return review.parse_markdown(self.text('polishedMarkdown'), core.parse_units(self.text('cleaned')))[0]

    def test_word_replacement_preview_readonly_and_preserves_references(self):
        self.completed()
        manifest = self.root/self.a['sessionMetadata']
        manifest.write_text(manifest.read_text()+'# Human metadata\nextra: unchanged\n')
        before = self.f.snapshot()
        plan = self.plan(edits=[self.edit()])
        preview = corrections.build(self.root, plan)['preview']
        self.assertEqual(before, self.f.snapshot())
        self.assertEqual(set(preview['changedFiles']), {self.a[k] for k in ('cleaned','polishedMarkdown','sessionMetadata')})
        result = corrections.apply(self.root, plan)
        self.assertTrue(result['status']['outputsCurrent'])
        self.assertEqual(self.turns()[0]['text'], 'Well, well, it got much darker.')
        self.assertEqual(self.turns()[0]['sources'][0]['end'], 31)
        for key in ('original','prepared'):
            self.assertEqual(before[self.a[key]], (self.root/self.a[key]).read_bytes())
        self.assertIn('# Human metadata\nextra: unchanged', manifest.read_text())
        self.assertFalse((self.root/core.WORK).exists())
        self.assertNotIn('speakerCorrections', yaml.safe_load(manifest.read_text())[final.KEY])

    def test_speaker_only_preserves_cleaned_and_all_speech(self):
        self.completed()
        before = self.text('cleaned')
        turns = self.turns()
        corrections.apply(self.root, self.plan(turns=[self.turn(speaker='Finnan')]))
        turns[0]['speaker'] = 'Finnan'
        self.assertEqual(turns, self.turns())
        self.assertEqual(before, self.text('cleaned'))

    def test_split_speakers_then_replace_preserves_boundaries(self):
        self.completed()
        parts = [dict(speaker='DM', text='Well, well,', sources=[dict(uid='u0001',start=0,end=12)]),
                 dict(speaker='Finnan', text='it got denser.', sources=[dict(uid='u0001',start=12,end=26)])]
        corrections.apply(self.root, self.plan(turns=[self.turn(parts=parts)]))
        corrections.apply(self.root, self.plan(edits=[self.edit()]))
        turns = self.turns()
        self.assertEqual(turns[1]['speaker'], 'Finnan')
        self.assertEqual(turns[1]['sources'], [dict(uid='u0001',start=12,end=31)])
        self.assertEqual(core.parse_units(self.text('cleaned'))[0]['speaker'], 'DM')
        before = self.f.snapshot()
        with self.assertRaisesRegex(core.PipelineError, 'boundary'):
            corrections.apply(self.root, self.plan(edits=[dict(uid='u0001',start=0,end=31,before='Well, well, it got much darker.',after='Much darker.')]))
        self.assertEqual(before, self.f.snapshot())

    def test_invalid_split_or_polished_only_words_cannot_write(self):
        self.completed()
        before = self.f.snapshot()
        invalid = [self.turn(parts=[dict(speaker='DM',text='Well',sources=[dict(uid='u0001',start=0,end=4)])]),
                   self.turn(after='Well, well, it got darker.')]
        for turn in invalid:
            with self.assertRaises(core.PipelineError): corrections.apply(self.root, self.plan(turns=[turn]))
            self.assertEqual(before, self.f.snapshot())

    def test_display_label_relabel_and_restore(self):
        self.completed()
        source = self.text('cleaned')
        substitution = dict(uid='u0001',start=19,end=25,kind='garbled',reason='User heard unintelligible speech.')
        corrections.apply(self.root, self.plan(turns=[self.turn(after='Well, well, it got [garbled].',substitutions=[substitution])]))
        self.assertEqual(source, self.text('cleaned'))
        corrections.apply(self.root, self.plan(turns=[dict(index=0,before='Well, well, it got [garbled].',speaker='Finnan')]))
        corrections.apply(self.root, self.plan(edits=[self.edit()],turns=[dict(index=0,before='Well, well, it got [garbled].',after='Well, well, it got much darker.')]))
        self.assertEqual(self.turns()[0]['speaker'], 'Finnan')
        self.assertEqual(self.turns()[0]['text'], 'Well, well, it got much darker.')

    def test_stale_inputs_reject_before_writing(self):
        self.completed()
        plan = self.plan(edits=[self.edit()])
        corrections.apply(self.root, self.plan(turns=[self.turn(speaker='Finnan')]))
        before = self.f.snapshot()
        with self.assertRaisesRegex(core.PipelineError, 'Stale'):
            corrections.apply(self.root, plan)
        self.assertEqual(before, self.f.snapshot())

    def test_repeated_words_need_explicit_polished_update_and_shift_review(self):
        raw = 'WEBVTT\n\n0 --> 1\nDM: Bob and Bob arrived.\n'
        def issues(us):
            first = self.f.issue(us[0],'Bob','Robert')
            second = self.f.issue(us[0],'Bob','Roberta')
            second['target'] = dict(start=8,end=11,before='Bob')
            return [first, second]
        self.a = self.f.export(issues, raw)
        self.f.handoff(self.a)
        initial = corrections.inspect(self.root, ['u0001'])
        plan = self.plan(edits=[dict(uid='u0001',start=0,end=3,before='Bob',after='Robert')],
                         decisions=[dict(id=initial['issues'][0]['id'],resolution='corrected')])
        before = self.f.snapshot()
        with self.assertRaisesRegex(core.PipelineError, 'ambiguous'):
            corrections.apply(self.root, plan)
        self.assertEqual(before, self.f.snapshot())
        plan['turns'] = [dict(index=0,before='Bob and Bob arrived.',after='Robert and Bob arrived.')]
        corrections.apply(self.root, plan)
        remaining = review.read(self.root)[2]
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0]['target']['start'],11)
        self.assertEqual(remaining[0]['proposal'],'Robert and Roberta arrived.')
        result = corrections.apply(self.root,self.plan(decisions=[dict(id=remaining[0]['id'],resolution='retain')]))
        self.assertTrue(result['status']['finalized'])
        self.assertEqual(result['status']['status'],'complete_with_uncertainty')
        self.assertFalse(review.report_path(self.root))

    def test_open_review_requires_actual_decisions_and_finalizes_after_correction(self):
        self.a = self.f.export()
        initial = corrections.inspect(self.root,['u0001'])
        before = self.f.snapshot()
        with self.assertRaisesRegex(core.PipelineError, 'unresolved issue'):
            corrections.apply(self.root,self.plan(edits=[self.edit()]))
        self.assertEqual(before,self.f.snapshot())
        result = corrections.apply(self.root,self.plan(edits=[self.edit()],decisions=[dict(id=initial['issues'][0]['id'],resolution='corrected')]))
        self.assertTrue(result['status']['outputsCurrent'])
        self.assertFalse((self.root/core.WORK).exists())
        self.assertFalse(review.report_path(self.root))

    def test_preexisting_markdown_decisions_are_preserved(self):
        self.a = self.f.export()
        self.f.decide(['retain'])
        before = self.f.snapshot()
        with self.assertRaisesRegex(core.PipelineError,'already recorded'):
            corrections.inspect(self.root)
        self.assertEqual(before,self.f.snapshot())

    def test_speaker_review_can_close_without_source_word_edit(self):
        self.a = self.f.export(lambda us:[dict(self.f.issue(us[0],'denser',None),kind='speaker')])
        issue = corrections.inspect(self.root)['issues'][0]
        source = self.text('cleaned')
        result = corrections.apply(self.root,self.plan(turns=[self.turn(speaker='Finnan')],
                                                      decisions=[dict(id=issue['id'],resolution='corrected')]))
        self.assertTrue(result['status']['finalized'])
        self.assertEqual(source,self.text('cleaned'))
        self.assertEqual(self.turns()[0]['speaker'],'Finnan')

    def test_interrupted_last_decision_finalization_recovers(self):
        self.a = self.f.export()
        issue = corrections.inspect(self.root)['issues'][0]
        with patch.object(final,'finish',side_effect=OSError('interrupted retirement')):
            with self.assertRaises(OSError):
                corrections.apply(self.root,self.plan(decisions=[dict(id=issue['id'],resolution='retain')]))
        result = corrections.recover(self.root)
        self.assertTrue(result['status']['outputsCurrent'])
        self.assertFalse(review.report_path(self.root))
        self.assertFalse((self.root/core.WORK).exists())

    def test_interrupted_transaction_recovers_consistent_finalized_references(self):
        self.completed()
        atomic = core.atomic
        def interrupt(root,path,data):
            if path == self.a['polishedMarkdown']: raise OSError('interrupted')
            return atomic(root,path,data)
        with patch.object(core,'atomic',side_effect=interrupt):
            with self.assertRaises(OSError): corrections.apply(self.root,self.plan(edits=[self.edit()]))
        corrections.recover(self.root)
        data = corrections.inspect(self.root,['u0001'])
        self.assertTrue(data['finalized'])
        self.assertEqual(data['turns'][0]['text'],'Well, well, it got much darker.')
        self.assertFalse((self.root/core.WORK).exists())

    def test_source_restoration_and_display_substitution_in_one_plan(self):
        self.completed()
        corrections.apply(self.root,self.plan(edits=[self.edit('blur')],turns=[self.turn(
            after='Well, well, it got [cross-talk].',
            substitutions=[dict(uid='u0001',start=19,end=23,kind='cross-talk',reason='User confirmed overlapping speech.')])]))
        self.assertIn('it got blur.',self.text('cleaned'))
        self.assertEqual(self.turns()[0]['text'],'Well, well, it got [cross-talk].')

    def test_multiple_uids_merged_turn_and_unrelated_derivatives(self):
        raw = 'WEBVTT\n\n0 --> 1\nDM: Hé saw Bob.\n\n1 --> 2\nDM: Then called him.\n'
        def merged(job):
            return [dict(speaker='DM',text='Hé saw Bob. Then called him.',sources=[s for t in job['draftTurns'] for s in t['sources']])]
        self.a = self.f.export(lambda us:[],raw,merged)
        self.f.finalize()
        derivative = self.root/'cleaned/session-001-session-recap.md'
        derivative.write_text('Human recap: unchanged.')
        result = corrections.apply(self.root,self.plan(edits=[dict(uid='u0001',start=7,end=10,before='Bob',after='Beryl')]))
        self.assertEqual(self.turns()[0]['sources'],[dict(uid='u0001',start=0,end=13),dict(uid='u0002',start=0,end=16)])
        self.assertEqual(self.turns()[0]['text'],'Hé saw Beryl. Then called him.')
        self.assertEqual(derivative.read_text(),'Human recap: unchanged.')
        self.assertIn(str(derivative.relative_to(self.root)),result['downstreamToInspect'])

    def test_confirmed_marker_removal_closes_review_without_retained_issue(self):
        raw = 'WEBVTT\n\n0 --> 1\nDM: Here is {{Beryl}}.\n'
        self.a = self.f.export(lambda us:[self.f.issue(us[0],'{{Beryl}}','Beryl')],raw)
        issue = corrections.inspect(self.root)['issues'][0]
        result = corrections.apply(self.root,self.plan(edits=[dict(uid='u0001',start=8,end=17,before='{{Beryl}}',after='Beryl')],
                                                      decisions=[dict(id=issue['id'],resolution='confirmed')]))
        self.assertEqual(result['status']['issues'],0)
        self.assertEqual(self.turns()[0]['text'],'Here is Beryl.')

    def test_cli_stdin_preview_and_inspection(self):
        self.completed()
        helper = Path(corrections.__file__)
        prefix = [sys.executable,'-B',str(helper),'--bundle',str(self.root)]
        result = subprocess.run(prefix+['inspect','--uid','u0001'],capture_output=True,text=True,check=True)
        self.assertEqual(json.loads(result.stdout)['turns'][0]['index'],0)
        before = self.f.snapshot()
        result = subprocess.run(prefix+['preview','--plan','-'],input=json.dumps(self.plan(edits=[self.edit()])),capture_output=True,text=True,check=True)
        self.assertIn('much darker',json.loads(result.stdout)['diff'])
        self.assertEqual(before,self.f.snapshot())


if __name__ == '__main__': unittest.main()
