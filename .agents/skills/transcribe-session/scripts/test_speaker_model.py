#!/usr/bin/env python3

from __future__ import annotations

import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("speaker_model.py")
sys.path.insert(0, str(SCRIPT_PATH.parent))
SPEC = importlib.util.spec_from_file_location("speaker_model", SCRIPT_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


class SpeakerModelTests(unittest.TestCase):
    def test_explicit_clean_cues_can_anchor_a_missing_voice_and_override_group_identity(self):
        np = MODULE.load_numpy()
        review, attrs = self.fixtures()
        by_id = {u['id']:u for u in review['utterances']}
        embeddings = {uid:np.array([1.,0.]) for uid in by_id}
        attrs['utteranceOverrides']['p1-g1'] = {'status':'unknown', 'participantId':None}
        refs = MODULE.build_profile_references({g['id']:g for g in review['groups']}, attrs['groupLabels'], by_id, embeddings, attrs['utteranceOverrides'])
        labels = {r['utteranceId']:r['participantId'] for r in refs}
        self.assertNotIn('p1-g1', labels)
        self.assertEqual(labels['manual'], 'p1')
        self.assertEqual(sum(r['utteranceId']=='manual' for r in refs), 1)
        refs = MODULE.build_profile_references({}, {}, by_id, embeddings, attrs['utteranceOverrides'])
        self.assertEqual([(r['utteranceId'],r['participantId']) for r in refs], [('manual','p1')])

    def test_automated_labels_do_not_seed_local_reference_profiles(self):
        np = MODULE.load_numpy()
        review, _ = self.fixtures()
        by_id = {u['id']:u for u in review['utterances']}
        refs = MODULE.build_profile_references({}, {}, by_id, {'target':np.array([1.,0.])},
            {'target':{'status':'assigned', 'participantId':'p1', 'modelMargin':.8}})
        self.assertEqual(refs, [])

    def materialize(self, *, prior=False, compare=False, thresholds=False, weak=False, low_cosine=False, policy=None):
        np = MODULE.load_numpy()
        review, attrs = self.fixtures()
        if policy:
            review['calibrationPolicy'] = policy
        embeddings = {'p1-g1': np.array([1., 0.]), 'p1-g2': np.array([.9, .1]),
                      'p2-g1': np.array([0., 1.]), 'p2-g2': np.array([.1, .9]),
                      'target': np.array([1., 1.]) / np.sqrt(2) if weak else np.array([.05, .95]),
                      'manual': np.array([1., 0.]), 'excluded': np.array([.05, .95])}
        if low_cosine:
            embeddings['target'] = np.array([-1., 0.])
        external = [{'participantId': 'p1', 'groupId': 'prior1', 'embedding': np.array([0., 1.])},
                    {'participantId': 'p2', 'groupId': 'prior2', 'embedding': np.array([1., 0.])}] if prior else None
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw)
            rp, ap, ep = root / 'r.json', root / 'a.json', root / 'e.npz'
            rp.write_text(json.dumps(review)); ap.write_text(json.dumps(attrs)); ep.write_bytes(b'fixture')
            return MODULE.materialize_model_layer(np=np, review=review, attributions=attrs, review_id='new',
                review_path=rp, attributions_path=ap, embeddings_path=ep, embedding_dimension=2,
                embedding_by_id=embeddings, model_name='test', minimum_duration_seconds=1.5, minimum_word_count=4,
                excluded_ids=set(), allow_unresolved_verification=True, external_references=external,
                compare_reference=compare, minimum_model_margin=.2 if thresholds else None,
                minimum_model_cosine=.8 if thresholds else None, profile_metadata={'source': 'prior'} if prior else None)

    def test_prior_bank_comparison_cannot_replace_local_prediction(self):
        review, attrs, summary = self.materialize(prior=True, compare=True)
        self.assertEqual(attrs['utteranceOverrides']['target']['participantId'], 'p2')
        prior = review['modelAttribution']['priorComparison']['target']
        self.assertEqual(prior['participantId'], 'p1')
        self.assertFalse(prior['agreesWithLocal'])
        self.assertFalse(prior['usedForAssignment'])
        self.assertNotIn('profileReference', attrs['modelAttribution'])
        self.assertGreater(summary['priorDisagreementCount'], 0)
        self.assertEqual(attrs['utteranceOverrides']['manual'], {'status': 'assigned', 'participantId': 'p1'})

    def test_low_margin_becomes_unknown_even_with_assigned_acoustic_group(self):
        review, attrs, summary = self.materialize(prior=True, thresholds=True, weak=True)
        self.assertEqual(attrs['utteranceOverrides']['target']['status'], 'unknown')
        self.assertNotIn('target', review['modelAttribution']['modelOverrideUtteranceIds'])
        self.assertIn('target', review['modelAttribution']['rejectedModelUtteranceIds'])
        self.assertGreater(summary['lowConfidenceUnknownCount'], 0)
        self.assertEqual(attrs['utteranceOverrides']['manual']['participantId'], 'p1')

    def test_phone_policy_requires_local_profiles_and_explicit_acceptance_thresholds(self):
        policy = {'externalReferenceRole': 'comparison', 'requiresConfidencePolicy': True}
        with self.assertRaises(MODULE.SpeakerReviewError):
            self.materialize(prior=True, policy=policy, thresholds=True)
        with self.assertRaises(MODULE.SpeakerReviewError):
            self.materialize(policy=policy)
        self.materialize(prior=True, compare=True, policy=policy, thresholds=True)

    def test_high_margin_does_not_override_low_cosine_rejection(self):
        _, attrs, _ = self.materialize(prior=True, thresholds=True, low_cosine=True)
        target = attrs['utteranceOverrides']['target']
        self.assertGreater(target['modelMargin'], .2)
        self.assertLess(target['modelCosine'], .8)
        self.assertEqual(target['status'], 'unknown')

    def test_confidence_policy_rejects_nonfinite_values(self):
        for margin, cosine in [(float('nan'), None), (None, float('inf')), (-.1, None), (None, 1.1)]:
            with self.assertRaises(MODULE.SpeakerReviewError):
                MODULE.validate_confidence_policy(margin, cosine)

    def transfer_fixture(self, root):
        np = MODULE.load_numpy()
        review, attrs = self.fixtures()
        rp, ap, auditp, dp = [root / name for name in ('source.json', 'source-attrs.json', 'audit.json', 'decisions.json')]
        rp.write_text(json.dumps(review)); ap.write_text(json.dumps(attrs))
        by_id = {u['id']: u for u in review['utterances']}
        audit = {'schemaVersion': 1, 'auditId': 'transfer', 'participants': review['participants'],
                 'recordings': review['recordings'],
                 'sourceReview': {'path': str(rp), 'sha256': MODULE.sha256_file(rp)},
                 'sourceAttributions': {'path': str(ap), 'sha256': MODULE.sha256_file(ap)}, 'items': []}
        labels = {'p1-g1': 'p1', 'p2-g1': 'p2', 'excluded': None}
        for uid, pid in labels.items():
            u = by_id[uid]
            audit['items'].append({'id': uid, 'utteranceId': uid,
                                  **{k: u[k] for k in ('recordingId', 'start', 'end', 'text')},
                                  'hidden': {'currentParticipantId': 'p1', 'predictedParticipantId': 'p2'}})
        auditp.write_text(json.dumps(audit))
        decisions = {'schemaVersion': 1, 'auditId': 'transfer', 'sourceAuditSha256': MODULE.sha256_file(auditp),
                     'decisions': {uid: {'status': 'assigned' if pid else 'overlap', 'participantId': pid,
                                        'transcriptRevealed': False} for uid, pid in labels.items()}}
        dp.write_text(json.dumps(decisions))
        review['humanAuditEvidence'] = {'auditPath': str(auditp), 'auditSha256': MODULE.sha256_file(auditp),
                                        'decisionsPath': str(dp), 'decisionsSha256': MODULE.sha256_file(dp)}
        for uid, decision in decisions['decisions'].items():
            attrs['utteranceOverrides'][uid] = {'status': 'unknown' if decision['status'] == 'overlap' else decision['status'],
                                               'participantId': decision['participantId'], 'humanVerified': True,
                                               'auditDecision': decision}
        refs = [{'participantId': 'p1', 'groupId': 'bank1', 'embedding': np.array([1., 0.])},
                {'participantId': 'p2', 'groupId': 'bank2', 'embedding': np.array([0., 1.])}]
        return {'np': np, 'review': review, 'attributions': attrs,
                'embedding_by_id': {'p1-g1': np.array([1., 0.]), 'p2-g1': np.array([0., 1.]), 'excluded': np.array([1., 0.])},
                'references': refs, 'profile_metadata': {'source': 'bank'}, 'audit_path': auditp, 'decisions_path': dp,
                'minimum_margin': .2, 'minimum_cosine': .8}

    def test_checked_transfer_uses_human_decisions_and_preserves_overlap(self):
        with tempfile.TemporaryDirectory() as raw:
            args = self.transfer_fixture(Path(raw))
            before = json.dumps(args['attributions'], sort_keys=True)
            evidence = MODULE.validate_reference_transfer(**args)
            self.assertEqual(evidence['bankMatchesIdentified'], 2)
            self.assertEqual(evidence['passingIdentifiedCount'], 2)
            self.assertEqual(evidence['passingIdentityErrors'], 0)
            self.assertEqual(evidence['passingParticipantIds'], ['p1', 'p2'])
            self.assertEqual(evidence['scoreRows'][0]['participantId'], 'p1')
            self.assertEqual(evidence['scoreRows'][2]['humanDecision']['status'], 'overlap')
            self.assertEqual(json.dumps(args['attributions'], sort_keys=True), before)

    def test_checked_transfer_rejects_stale_incomplete_or_changed_listening(self):
        for change in ('stale-source', 'incomplete', 'changed-text', 'changed-human', 'changed-decision-file'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as raw:
                args = self.transfer_fixture(Path(raw))
                if change == 'stale-source':
                    (Path(raw) / 'source.json').write_text('{}')
                elif change == 'incomplete':
                    data = json.loads(args['decisions_path'].read_text()); data['decisions'].pop('p1-g1')
                    args['decisions_path'].write_text(json.dumps(data))
                    args['review']['humanAuditEvidence']['decisionsSha256'] = MODULE.sha256_file(args['decisions_path'])
                elif change == 'changed-text':
                    args['review']['utterances'][0]['text'] = 'changed'
                elif change == 'changed-human':
                    args['attributions']['utteranceOverrides']['p1-g1']['status'] = 'unknown'
                else:
                    args['decisions_path'].write_text(args['decisions_path'].read_text() + '\n')
                with self.assertRaises(MODULE.SpeakerReviewError):
                    MODULE.validate_reference_transfer(**args)

    def test_checked_transfer_rejects_errors_or_missing_voice_evidence(self):
        for change in ('wrong-bank', 'weak-voice', 'missing-threshold', 'missing-vector'):
            with self.subTest(change=change), tempfile.TemporaryDirectory() as raw:
                args = self.transfer_fixture(Path(raw))
                if change == 'wrong-bank':
                    args['references'][0]['embedding'], args['references'][1]['embedding'] = args['references'][1]['embedding'], args['references'][0]['embedding']
                elif change == 'weak-voice':
                    args['embedding_by_id']['p2-g1'] = args['np'].array([.7, .71])
                elif change == 'missing-threshold':
                    args['minimum_margin'] = None
                else:
                    args['embedding_by_id'].pop('p1-g1')
                with self.assertRaises(MODULE.SpeakerReviewError):
                    MODULE.validate_reference_transfer(**args)

    def test_checked_transfer_materialization_preserves_humans_and_resets_verification(self):
        with tempfile.TemporaryDirectory() as raw:
            root = Path(raw); args = self.transfer_fixture(root)
            proof = MODULE.validate_reference_transfer(**args)
            review, attrs = args['review'], args['attributions']
            review['calibrationPolicy'] = {'externalReferenceRole': 'comparison', 'requiresConfidencePolicy': True}
            attrs['verification'] = {'p1': {'status': 'confirmed', 'sampleUtteranceIds': ['p1-g1']}}
            rp, ap, ep = root/'current.json', root/'current-attrs.json', root/'cache.npz'
            rp.write_text(json.dumps(review)); ap.write_text(json.dumps(attrs)); ep.write_bytes(b'fixture')
            vectors = {u['id']: args['np'].array([0., 1.]) for u in review['utterances']}
            vectors.update(args['embedding_by_id'])
            parameters = dict(np=args['np'], review=review, attributions=attrs, review_id='new', review_path=rp,
                              attributions_path=ap, embeddings_path=ep, embedding_dimension=2, embedding_by_id=vectors,
                              model_name='test', minimum_duration_seconds=1.5, minimum_word_count=4, excluded_ids=set(),
                              allow_unresolved_verification=True, external_references=args['references'],
                              profile_metadata=args['profile_metadata'], minimum_model_margin=.2, minimum_model_cosine=.8,
                              validated_reference_transfer=proof)
            result, decisions, summary = MODULE.materialize_model_layer(**parameters)
            self.assertEqual(decisions['utteranceOverrides']['target']['participantId'], 'p2')
            self.assertEqual(decisions['utteranceOverrides']['excluded']['status'], 'unknown')
            for uid, label in attrs['utteranceOverrides'].items():
                self.assertEqual(decisions['utteranceOverrides'][uid], label)
            self.assertEqual(decisions['verification'], {})
            self.assertEqual(result['modelAttribution']['validatedReferenceTransfer'], proof)
            parameters['minimum_model_margin'] = .3
            with self.assertRaises(MODULE.SpeakerReviewError):
                MODULE.materialize_model_layer(**parameters)

    def test_short_cue_guard_rejects_sparse_or_conflicting_listening(self):
        for support, human, confirmations, accepted in (
            (1, "p1", True, True), (6, "p1", True, False),
            (1, "p2", False, False), (1, None, False, False),
        ):
            with self.subTest(support=support, human=human, confirmed=confirmations), tempfile.TemporaryDirectory() as raw:
                root=Path(raw); rp=root/"review.json"; ap=root/"attrs.json"
                rp.write_text("{}"); ap.write_text("{}")
                review={"participants":[{"id":"p1","gameRole":"One"},{"id":"p2","gameRole":"Two"}],
                        "groups":[], "recordings":[], "utterances":[],
                        "modelAttribution":{"manualOverrideUtteranceIds":["human"] if human else []}}
                attrs={"groupLabels":{}, "utteranceOverrides":{}, "verification":{},
                       "modelAttribution":{"modelOverrideUtteranceIds":[]}}
                for i in range(5):
                    uid=f"model-{i}"
                    review["utterances"].append({"id":uid,"start":i,"end":i+2,"durationSeconds":2,"wordCount":5,"scribeSpeakerIds":["s"]})
                    attrs["utteranceOverrides"][uid]={"status":"assigned","participantId":"p1"}
                    attrs["modelAttribution"]["modelOverrideUtteranceIds"].append(uid)
                review["utterances"].append({"id":"short","start":20,"end":20.5,"durationSeconds":.5,"wordCount":1,"scribeSpeakerIds":["s"]})
                if human:
                    review["utterances"].append({"id":"human","start":21,"end":23,"durationSeconds":2,"wordCount":5,"scribeSpeakerIds":["s"]})
                    attrs["utteranceOverrides"]["human"]={"status":"assigned","participantId":human}
                if confirmations:
                    attrs["verification"]={"p1":{"status":"confirmed","sampleUtteranceIds":["model-0"]}}
                original=json.dumps(attrs,sort_keys=True)
                _,result,summary=MODULE.materialize_scribe_fallback_layer(review=review,attributions=attrs,review_id="guarded",review_path=rp,attributions_path=ap,minimum_accuracy=.8,minimum_support_cues=support,check_human_agreement=True)
                self.assertEqual(summary["acceptedScribeIdCount"],int(accepted))
                self.assertEqual(result["utteranceOverrides"].get("short",{}).get("participantId"),"p1" if accepted else None)
                self.assertEqual(json.dumps(attrs,sort_keys=True),original)
                if human:self.assertEqual(result["utteranceOverrides"]["human"],attrs["utteranceOverrides"]["human"])

    def test_short_cue_guard_cli_and_invalid_support(self):
        args=MODULE.build_parser().parse_args(["apply-scribe-fallback","r.json","--attributions","a.json","--output-dir","out","--review-id","checked","--minimum-support-cues","5","--check-human-agreement"])
        self.assertEqual(args.minimum_support_cues,5)
        self.assertTrue(args.check_human_agreement)
        with self.assertRaises(MODULE.SpeakerReviewError):
            MODULE.materialize_scribe_fallback_layer(review={},attributions={},review_id="x",review_path=Path("r"),attributions_path=Path("a"),minimum_accuracy=.8,minimum_support_cues=0)

    def test_scribe_fallback_uses_inclusive_eighty_percent_threshold(self) -> None:
        participants = [
            {"id": "p1", "name": "One", "gameRole": "One"},
            {"id": "p2", "name": "Two", "gameRole": "Two"},
        ]
        utterances = []
        overrides = {}
        model_ids = []
        assignments = [
            ("speaker_0", "p1"),
            ("speaker_0", "p1"),
            ("speaker_0", "p1"),
            ("speaker_0", "p1"),
            ("speaker_0", "p2"),
            ("speaker_1", "p1"),
            ("speaker_1", "p1"),
            ("speaker_1", "p1"),
            ("speaker_1", "p2"),
            ("speaker_1", "p2"),
        ]
        for index, (scribe_id, participant_id) in enumerate(assignments, start=1):
            utterance_id = f"model-{index}"
            model_ids.append(utterance_id)
            utterances.append(
                {
                    "id": utterance_id,
                    "recordingId": "r1",
                    "groupId": "mixed",
                    "start": float(index),
                    "end": float(index + 2),
                    "durationSeconds": 2.0,
                    "wordCount": 5,
                    "text": utterance_id,
                    "scribeSpeakerIds": [scribe_id],
                }
            )
            overrides[utterance_id] = {
                "status": "assigned",
                "participantId": participant_id,
            }
        utterances.extend(
            [
                {
                    "id": "short-accepted",
                    "recordingId": "r1",
                    "groupId": "mixed",
                    "start": 20.0,
                    "end": 20.5,
                    "durationSeconds": 0.5,
                    "wordCount": 1,
                    "text": "yes",
                    "scribeSpeakerIds": ["speaker_0"],
                },
                {
                    "id": "short-rejected",
                    "recordingId": "r1",
                    "groupId": "mixed",
                    "start": 21.0,
                    "end": 21.5,
                    "durationSeconds": 0.5,
                    "wordCount": 1,
                    "text": "no",
                    "scribeSpeakerIds": ["speaker_1"],
                },
            ]
        )
        review = {
            "schemaVersion": 1,
            "reviewId": "model-assisted",
            "participants": participants,
            "groups": [
                {
                    "id": "mixed",
                    "recordingId": "r1",
                    "memberUtteranceIds": [item["id"] for item in utterances],
                    "representativeUtteranceIds": [],
                }
            ],
            "utterances": utterances,
            "recordings": [],
            "verification": {"samplesPerParticipant": 1},
            "modelAttribution": {
                "minimumDurationSeconds": 1.5,
                "minimumWordCount": 4,
            },
        }
        attributions = {
            "schemaVersion": 1,
            "reviewId": "model-assisted",
            "groupLabels": {"mixed": {"status": "mixed", "participantId": None}},
            "utteranceOverrides": overrides,
            "verification": {
                "p1": {"status": "confirmed", "sampleUtteranceIds": ["model-1"]},
                "p2": {"status": "confirmed", "sampleUtteranceIds": ["model-5"]},
            },
            "modelAttribution": {"modelOverrideUtteranceIds": model_ids},
        }
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "review.json"
            attributions_path = root / "attributions.json"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            attributions_path.write_text(json.dumps(attributions), encoding="utf-8")
            output_review, output_attributions, summary = (
                MODULE.materialize_scribe_fallback_layer(
                    review=review,
                    attributions=attributions,
                    review_id="scribe-fallback",
                    review_path=review_path,
                    attributions_path=attributions_path,
                    minimum_accuracy=0.8,
                )
            )
        self.assertEqual(output_review["reviewId"], "scribe-fallback")
        self.assertEqual(output_attributions["groupLabels"], {})
        self.assertEqual(
            output_attributions["utteranceOverrides"]["short-accepted"][
                "participantId"
            ],
            "p1",
        )
        self.assertNotIn(
            "short-rejected", output_attributions["utteranceOverrides"]
        )
        self.assertEqual(summary["acceptedScribeIdCount"], 1)
        self.assertEqual(summary["shortCueFallbackCount"], 1)
        self.assertEqual(summary["unresolvedCueCount"], 1)
        self.assertEqual(
            output_attributions["verification"], attributions["verification"]
        )

    def test_materialize_preserves_manual_and_short_cues(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        review, attributions = self.fixtures()
        embeddings = {
            "p1-g1": np.array([1.0, 0.0]),
            "p1-g2": np.array([0.9, 0.1]),
            "p2-g1": np.array([0.0, 1.0]),
            "p2-g2": np.array([0.1, 0.9]),
            "target": np.array([0.05, 0.95]),
            "manual": np.array([1.0, 0.0]),
            "excluded": np.array([0.05, 0.95]),
        }
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            review_path = root / "review.json"
            attribution_path = root / "attributions.json"
            embedding_path = root / "embeddings.npz"
            review_path.write_text(json.dumps(review), encoding="utf-8")
            attribution_path.write_text(json.dumps(attributions), encoding="utf-8")
            np.savez(
                embedding_path,
                ids=np.array(list(embeddings)),
                embeddings=np.vstack(list(embeddings.values())),
            )
            output_review, output_attributions, summary = MODULE.materialize_model_layer(
                np=np,
                review=review,
                attributions=attributions,
                review_id="derived",
                review_path=review_path,
                attributions_path=attribution_path,
                embeddings_path=embedding_path,
                embedding_dimension=2,
                embedding_by_id=embeddings,
                model_name="test-model",
                minimum_duration_seconds=1.5,
                minimum_word_count=4,
                excluded_ids={"excluded"},
                allow_unresolved_verification=True,
            )
        self.assertEqual(
            output_attributions["utteranceOverrides"]["target"]["participantId"],
            "p2",
        )
        self.assertEqual(
            output_attributions["utteranceOverrides"]["manual"]["participantId"],
            "p1",
        )
        self.assertNotIn("short", output_attributions["utteranceOverrides"])
        self.assertNotIn("excluded", output_attributions["utteranceOverrides"])
        self.assertTrue(output_review["verification"]["allowUnresolved"])
        self.assertEqual(summary["modelOverrideCount"], 5)
        self.assertEqual(summary["manualOverrideCountPreserved"], 1)
        self.assertEqual(summary["shortCueCountPreserved"], 1)
        self.assertEqual(summary["explicitExclusionCountPreserved"], 1)

    def test_reference_selection_uses_only_current_confirmed_assignments(self) -> None:
        review, attributions = self.fixtures()
        attributions["verification"] = {
            "p1": {
                "status": "confirmed",
                "sampleUtteranceIds": ["p1-g1", "p1-g2", "manual"],
            },
            "p2": {
                "status": "confirmed",
                "sampleUtteranceIds": ["p2-g1", "p2-g2", "target"],
            },
        }
        attributions["utteranceOverrides"]["target"] = {
            "status": "assigned",
            "participantId": "p2",
        }
        selected = MODULE.select_verified_reference_samples(review, attributions, 2)
        by_participant: dict[str, list[str]] = {}
        for item in selected:
            by_participant.setdefault(item["participant"]["id"], []).append(
                item["utterance"]["id"]
            )
        self.assertEqual(len(by_participant["p1"]), 2)
        self.assertEqual(len(by_participant["p2"]), 2)

    def test_reference_bank_matches_current_participants_by_name_not_old_id(self) -> None:
        try:
            np = MODULE.load_numpy()
        except MODULE.SpeakerReviewError as exc:
            self.skipTest(str(exc))
        review, _attributions = self.fixtures()
        manifest = {
            "schemaVersion": 1,
            "clips": [
                {
                    "participantId": "old-p99",
                    "name": "One",
                    "gameRole": "One",
                    "utteranceId": "old-one",
                    "clipSha256": "hash-one",
                },
                {
                    "participantId": "old-p01",
                    "name": "Two",
                    "gameRole": "Old Role",
                    "utteranceId": "old-two",
                    "clipSha256": "hash-two",
                },
            ],
        }
        with tempfile.TemporaryDirectory() as raw_dir:
            root = Path(raw_dir)
            manifest_path = root / "reference-bank.json"
            embeddings_path = root / "reference.npz"
            manifest_path.write_text(json.dumps(manifest), encoding="utf-8")
            embeddings_path.write_bytes(b"embedding-cache")
            references, metadata = MODULE.build_reference_bank_references(
                review=review,
                manifest=manifest,
                embedding_by_id={
                    "hash-one": np.array([1.0, 0.0]),
                    "hash-two": np.array([0.0, 1.0]),
                },
                manifest_path=manifest_path,
                embeddings_path=embeddings_path,
            )
        by_utterance = {item["utteranceId"]: item["participantId"] for item in references}
        self.assertEqual(by_utterance, {"old-one": "p1", "old-two": "p2"})
        self.assertEqual(metadata["roleMismatches"][0]["name"], "Two")

    @staticmethod
    def fixtures() -> tuple[dict, dict]:
        participants = [
            {"id": "p1", "name": "One", "gameRole": "One", "display": "One / One"},
            {"id": "p2", "name": "Two", "gameRole": "Two", "display": "Two / Two"},
        ]
        utterances = []
        groups = []
        group_rows = [
            ("g1", "p1-g1", 0.0),
            ("g2", "p1-g2", 10.0),
            ("h1", "p2-g1", 20.0),
            ("h2", "p2-g2", 30.0),
            ("t1", "target", 40.0),
            ("m1", "manual", 50.0),
            ("e1", "excluded", 60.0),
        ]
        for group_id, utterance_id, start in group_rows:
            groups.append(
                {
                    "id": group_id,
                    "recordingId": "r1",
                    "memberUtteranceIds": [utterance_id],
                    "representativeUtteranceIds": [utterance_id],
                }
            )
            utterances.append(
                {
                    "id": utterance_id,
                    "recordingId": "r1",
                    "groupId": group_id,
                    "start": start,
                    "end": start + 2.0,
                    "durationSeconds": 2.0,
                    "wordCount": 5,
                    "text": utterance_id,
                    "scribeSpeakerIds": ["speaker_0"],
                }
            )
        utterances.append(
            {
                "id": "short",
                "recordingId": "r1",
                "groupId": "t1",
                "start": 70.0,
                "end": 70.5,
                "durationSeconds": 0.5,
                "wordCount": 1,
                "text": "short",
                "scribeSpeakerIds": ["speaker_0"],
            }
        )
        next(item for item in groups if item["id"] == "t1")[
            "memberUtteranceIds"
        ].append("short")
        review = {
            "schemaVersion": 1,
            "reviewId": "source",
            "participants": participants,
            "recordings": [{"id": "r1", "audioPath": "/tmp/audio.m4a"}],
            "groups": groups,
            "utterances": utterances,
            "exceptions": {"unclusteredUtteranceIds": []},
            "verification": {"samplesPerParticipant": 10},
        }
        attributions = {
            "schemaVersion": 1,
            "reviewId": "source",
            "updatedAt": None,
            "groupLabels": {
                "g1": {"status": "assigned", "participantId": "p1"},
                "g2": {"status": "assigned", "participantId": "p1"},
                "h1": {"status": "assigned", "participantId": "p2"},
                "h2": {"status": "assigned", "participantId": "p2"},
                "t1": {"status": "assigned", "participantId": "p1"},
                "m1": {"status": "assigned", "participantId": "p2"},
                "e1": {"status": "assigned", "participantId": "p1"},
            },
            "utteranceOverrides": {
                "manual": {"status": "assigned", "participantId": "p1"}
            },
            "verification": {},
        }
        return review, attributions


if __name__ == "__main__":
    unittest.main()
