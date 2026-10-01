# Local Speaker Attribution

Use this workflow after Scribe transcription when real participant identities are needed or when a single Scribe speaker ID contains multiple people. Its primary task is reference-based voice classification of individual audio segments. Scribe-ID-to-person mappings are a later fallback for short cues.

## Outcome

The workflow has three distinct layers:

1. **Segmentation:** Scribe supplies text, word timestamps, and anonymous speaker
   IDs. `speaker_review.py` divides that output using ID changes, pauses, sentence
   endings, and duration limits. Scribe IDs influence boundaries, not physical
   identities.
2. **Voice classification:** A pretrained ECAPA encoder embeds the audio of each
   eligible segment (by default, at least 1.5 seconds and four words).
   `speaker_model.py` compares it with normalized mean embeddings from each
   person's reviewed reference clips. It assigns the closest participant profile,
   subject to any configured cosine/margin rejection thresholds and human
   overrides. Building these profiles does not train or fine-tune the encoder.
   Different segments sharing one Scribe ID can receive different identities.
   Verify these predictions with time-spread listening samples.
3. **Short-cue fallback:** After verification, measure participant agreement among
   the substantial model-classified segments within each Scribe ID. An ID with
   at least 80% agreement on one person can label its otherwise unassigned short
   cues. Model and manual assignments take precedence; unsupported cues remain
   `Unknown`.

Automatic Scribe speaker detection is the transcription default. Its ID count is
independent of the roster size and the classifier's participant profiles. Prefer
pure IDs for useful short-cue fallback; purity must still be checked, and neither
five IDs nor a larger count establishes correct attribution. The classifier
assigns one identity per segment. It does not independently detect speaker
changes or reliably split multiple voices that Scribe merged within one segment.

Acoustic microclusters help collect reference clips; their group labels are not
final classifier identities. Mixed groups describe different voices across group
members, not overlap within every member.

This is local processing. It does not upload audio, voiceprints, participant labels, or review decisions.

All paths written by this workflow must remain in the transcription workspace
beside the original recording, normally `<recording-directory>/transcription/scribe-v2/`.
Do not write reviews, embeddings, audits, reference banks, or identified VTTs under
the Taelgar vault `_sessions` tree. The scripts reject those output paths. A later
`prepare-session-source` run is responsible for archiving the finalized source.

## Inputs and dependencies

Supply corresponding `--audio` and `--transcript` arguments in the same order. Use the unchanged `*.scribe-v2.json`, not a VTT or an older diarization artifact. Multiple sequential recordings may be prepared in one review; do not include an alternate simultaneous capture unless it has been selected for this transcript.

The cluster review requires NumPy and `ffmpeg`. ECAPA embeddings additionally require Torch and SpeechBrain. Use an existing Python environment when possible. In Codex desktop, locate bundled dependencies when the system Python lacks them. If an existing `ffmpeg` is outside `PATH`, pass its absolute path with `--ffmpeg`. Do not install a package or download a speaker model without user authorization.

`speaker_embeddings.py` refuses a nonlocal model source unless `--allow-model-download` is present. Add that flag only after explicit authorization, and use a persistent `--model-cache` outside the skill. Its `.npz` caches contain source hashes and model settings, checkpoint periodically, resume compatible partial work, and print progress with an ETA.

## Choose the reference strategy

Match the workflow to microphone, room, speaker distance, and audio processing.
Being the same campaign is not sufficient evidence of compatible voice profiles.
Zoom-to-iPhone transfer and simultaneous phones at different table positions call
for clean local references and a blind comparison before accepting model labels.
Start with an independent profile scope for each recording; pool sequential chunks
only after testing that the profiles transfer. Keep concurrent captures separate.

Retain prior work as evidence: verified clips, reviewed identities, embedding
caches, older transcript labels, and provisional predictions. A prior bank may
suggest anchor candidates and independently check local predictions. Record
agreement and disagreement rather than averaging conflicting identities or
discarding the old work. Human corrections to the same recorded utterance remain
active decisions. Old anonymous Scribe IDs cannot supply physical identities.

An older **identified** transcript may support current-session seed selection
through conservative word-and-time alignment: preserve every raw timed item,
require strong text/timing agreement, check candidate voice coherence and prior
bank compatibility when available, and exclude a seed from its own prediction.
Those remain candidate identities until local listening verification. Do not
import labels on timestamp overlap alone or assume the older text is correct.

## Recover recording-local calibration

When a transfer is poor or recording conditions change, use the reusable recovery
script instead of recreating a recording-specific helper:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_recalibrate.py \
  "/absolute/path/to/current-model-assisted.speaker-review.json" \
  --attributions "/absolute/path/to/current-model-assisted.speaker-attributions.json" \
  --embeddings "/absolute/path/to/current.ecapa-embeddings.npz" \
  --output-dir "/absolute/path/to/speaker-review" \
  --review-id-prefix "session-local"
```

It creates one `session-local-<recordingId>-local-calibration` review and decision
pair per recording, a provenance report, and optionally corresponding subset
embedding caches. It refuses existing output names. Every utterance retains its
ID, text, timing, order, and group membership. Explicit human corrections and
existing human group decisions carry forward; participant confirmations reset
for the new review scope. Automated labels are retained under
`priorSpeakerEvidence.predictions`, not propagated as active identities.
Source paths and hashes, original verification, model metadata, and earlier
evidence remain available. The original review and decisions are unchanged.

Cache reuse requires a complete, provenanced cache and exact recording IDs,
utterance IDs, text, and timing. The new caches retain the unchanged vectors and
record the parent cache hash. Omit `--embeddings` when no compatible cache exists,
then run `speaker_embeddings.py review` on each new review.

Serve each local review and begin with **Calibration**. Identify group
representatives, listen to additional representatives when unclear, and refine
mixed groups. Explicit human per-cue assignments with eligible cached vectors can
also supply reference clips, including speakers absent from clear group labels;
they override a conflicting group representative label. Automated predictions
and qualified short-cue fallback labels cannot become reference anchors.
Build local profiles from clean accepted clips; do not review every
short exception. If only one voice lacks references, use prior predictions to
choose promising candidates and refine only the relevant mixed group with
`speaker_review.py refine --group <groupId>` (repeatable). Other mixed groups and
all accepted decisions remain preserved. It is not necessary to label every
microcluster once enough independent clean references support all voices and
the blind audit can hold out each reference group. Then use the blind audit below to assess predictions under the
new conditions and choose an acceptance policy. Margin and cosine are similarity
measures, not calibrated probabilities. Keep weak or unsupported matches Unknown.

For materialization, `speaker_model.py apply` accepts
`--minimum-model-margin` and `--minimum-model-cosine`. Both are required for the
recovered local-calibration reviews; choose them from the local audit rather than
reusing thresholds merely because they worked on Zoom. Low-confidence rejection
writes an explicit Unknown override, so an acoustic group cannot silently restore
the rejected identity.

To use prior work as an independent comparison, add the existing
`--reference-bank` and `--reference-embeddings` arguments plus
`--compare-reference`. The accepted local profiles still determine assignments.
The output records prior-bank identity, margin, cosine, agreement with the local
prediction, and `usedForAssignment: false`. Prior disagreements are useful
listening targets; agreement alone is not measured accuracy. Recovered local
reviews refuse a prior bank as their sole identity source.

Continue with ten time-spread verification samples per person within each
recording, then the qualified Scribe-ID short-cue fallback and rendering described
below. Export verified local reference banks for later comparable recordings.
Cross-capture timing alignment may later link the same spoken passage across
phones as additional evidence; it does not authorize merging the transcripts.

## Collect a few individual references

When refinement still produces many mixed groups, assess reference coverage
rather than refining everything again. Each participant needs clean eligible
clips from more than one current group so the blind audit can hold out a group
without removing that voice's entire profile. A Mixed group describes impure
membership; an individual member can still be a useful clean reference.

Use tentative local predictions and retained bank comparisons to select a small
set of eligible cached cues outside the participant's existing reference group.
Keep those suggestions out of the listening page and record candidate paths,
hashes, scores, selection rationale, and group IDs beside the recording. Agreement
between models only selects a listening target; it does not assign an identity.
Freeze a new local review/attribution layer and rebind its compatible cache with
`speaker_recalibrate.py`, then offer only the selected cues:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_review.py serve \
  "/absolute/path/to/local-reference-collection.speaker-review.json" \
  --port 8765 \
  --reference-utterance "r01-u00123" \
  --reference-utterance "r01-u00456"
```

This focused page edits only selected per-cue decisions; group labels,
verification, unrelated cues, and the frozen review remain unchanged. The original
group ID remains attached for holdout scoring. Overlap becomes an explicit
Unknown identity with the listening decision retained and cannot seed a profile.
Reassess reference coverage after listening, then prepare the blind audit. The
reference collection is calibration evidence, not an accuracy test.

## Fast path with a verified reference bank

Use this path for a later recording with comparable conditions after one session has produced clean, verified reference clips. The bank is matched to the new roster by participant `name`, not the order-dependent `p01` identifiers. Role changes are recorded but do not silently change physical identity. A poor transfer returns to recording-local calibration above; it is not repaired by asking the user to confirm many obviously wrong suggestions.

First prepare the ordinary speaker-review JSON and blank attribution layer as described below. Then create the reference-bank embedding cache once:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_embeddings.py reference-bank \
  "/absolute/path/to/session-reference-bank/reference-bank.json" \
  --output "/absolute/path/to/session-reference-bank/reference-bank.ecapa.npz" \
  --model-source "/absolute/path/to/local/speechbrain-ecapa-model"
```

Create a resumable cache for the new recording. The defaults embed only cues lasting at least 1.5 seconds and containing at least four words:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_embeddings.py review \
  "/absolute/path/to/new-session.speaker-review.json" \
  --output "/absolute/path/to/new-session.ecapa-embeddings.npz" \
  --model-source "/absolute/path/to/local/speechbrain-ecapa-model"
```

Apply the bank as a new, reversible attribution layer:

This is a provisional nearest-profile transfer. Supply audited margin/cosine
thresholds when available; without them the legacy fast path does not reject weak
matches. It must still pass listening verification before becoming a source.

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_model.py apply \
  "/absolute/path/to/new-session.speaker-review.json" \
  --attributions "/absolute/path/to/new-session.speaker-attributions.json" \
  --embeddings "/absolute/path/to/new-session.ecapa-embeddings.npz" \
  --reference-bank "/absolute/path/to/session-reference-bank/reference-bank.json" \
  --reference-embeddings "/absolute/path/to/session-reference-bank/reference-bank.ecapa.npz" \
  --output-dir "/absolute/path/to/speaker-review" \
  --review-id "new-session-model-assisted" \
  --allow-unresolved-verification
```

Serve that model-assisted review and go directly to **Verification**. Confirm ten time-spread samples for each person. A correction invalidates only the old and new participants' confirmations; it does not erase unrelated completed blocks.

After verification, derive a reversible short-cue layer from Scribe IDs:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_model.py apply-scribe-fallback \
  "/absolute/path/to/new-session-model-assisted.speaker-review.json" \
  --attributions "/absolute/path/to/new-session-model-assisted.speaker-attributions.json" \
  --output-dir "/absolute/path/to/speaker-review" \
  --review-id "new-session-scribe-fallback" \
  --minimum-accuracy 0.8
```

For each Scribe ID, this measures the majority participant among its durable model-assigned cues by cue count. An agreement rate of 80% or higher is sufficient to assign that ID's short cues. The threshold is inclusive, and the audit records the supporting cue count so a small but passing sample remains visible. Per-cue model or manual assignments always win. Acoustic group labels are discarded from this derived layer: they are review aids, not identity evidence. A mixed group means that different group members contain different voices; it must not be rendered as overlapping speech. Short cues whose Scribe ID does not meet the threshold remain `Unknown`.

The existing `--minimum-accuracy` option and saved `accuracy` fields name this
within-ID agreement rate. They do not measure classifier accuracy against an
independent human test set. Keep those names for artifact compatibility, but
describe the result as agreement and report its supporting cue count.

If the time-spread samples are clean, apply the Scribe-ID fallback and render. If errors concentrate on one or two people, recalibrate only those participants from clean clips in the current recording. Do not automatically rerun a 50-clip blind audit for every session; repeat it when the embedding model, reference profiles, or recording conditions change materially, or when verification indicates poor transfer.

## Prepare the review

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_review.py prepare \
  --audio "/absolute/path/to/Session-Chunk-01.m4a" \
  --transcript "/absolute/path/to/Session-Chunk-01.scribe-v2.json" \
  --audio "/absolute/path/to/Session-Chunk-02.m4a" \
  --transcript "/absolute/path/to/Session-Chunk-02.scribe-v2.json" \
  --participants "/absolute/path/to/campaign-participants.yaml" \
  --output-dir "/absolute/path/to/speaker-review" \
  --review-id "session-135"
```

The default creates three microclusters per roster participant per recording and offers up to three representative utterances for each group. The user can normally decide after one clip and play the other representatives only when the voice is unclear. More groups reduce the risk that a group contains multiple people but require more decisions. Do not silently lower the group count merely to make review appear faster.

Outputs:

```text
session-135.speaker-review.json
session-135.speaker-attributions.json
```

The review JSON records source paths and hashes, participant identities, independently segmented utterances, cluster membership, representative utterances, and unclustered exceptions. The attribution JSON is the human decision layer. Preserve both.

## Refine mixed groups

Do not ask the user to label every member of a large mixed group. Create a new refinement layer that carries forward accepted assignments and replaces only mixed or unknown groups with smaller child groups:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_review.py refine \
  "/absolute/path/to/session-135.speaker-review.json" \
  --attributions "/absolute/path/to/session-135.speaker-attributions.json" \
  --output-dir "/absolute/path/to/speaker-review" \
  --review-id "session-135-r2"
```

The default creates eight child groups per mixed or unknown parent. The source review and decisions remain unchanged; the new review records their paths and hashes, carries accepted group labels and utterance overrides forward, and resets participant verification. Refinement can be repeated if a child group remains mixed. Use a new review ID for every layer.

## Run the review page

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_review.py serve \
  "/absolute/path/to/session-135.speaker-review.json"
```

Open the printed localhost URL. The page saves every decision directly to the adjacent attribution JSON.

- Keys `1` through the roster size assign the displayed person and game role.
- `M` marks a group as containing mixed voices.
- `U` marks it unknown.
- The arrow keys move between groups.
- The calibration view is the required pass. The exception view is a fallback for mixed, unknown, or too-short material; it is not an instruction to review every utterance.
- When blocking exceptions remain, the exception view defaults to **Blocking only**. Turn that filter off only to inspect optional short, unclustered material.
- The verification view becomes available after blocking calibration work is resolved. It selects ten time-spread samples per attributed participant by default. Reassign any wrong sample, then confirm each participant's block; a changed assignment clears confirmations only for the old and new participants.

Acoustic clustering is only a review accelerator. Never infer a participant identity from the cluster itself. Play multiple representatives when they disagree, and mark the group mixed rather than forcing a person. Mixed means the cluster is impure across its member cues; it does not establish simultaneous speech within each cue. After model verification, use qualified Scribe-ID fallback for short cues instead of propagating acoustic group labels.

## Blindly audit a speaker-embedding model

Before allowing a new embedding model to replace reviewed assignments, create a small blind audit from a cached `ids` plus `embeddings` NumPy archive. The audit scores each eligible utterance against participant profiles built from reviewed group representatives, while excluding all representatives from that utterance's current acoustic group. This avoids testing a clip against a profile directly derived from its own reviewed group.

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_audit.py prepare \
  "/absolute/path/to/session.speaker-review.json" \
  --attributions "/absolute/path/to/session.speaker-attributions.json" \
  --embeddings "/absolute/path/to/session.speaker-embeddings.npz" \
  --output-dir "/absolute/path/to/speaker-review" \
  --audit-id "session-embedding-audit"
```

The default selects 35 model-versus-review disagreements and 15 agreement controls. Disagreements are allocated across current-to-model speaker pairs, controls across participants, and samples within each stratum are spread over session time and model margin. The audit JSON retains the hidden comparison data; the localhost review API omits it.

Scale a warranted audit to the recording and available candidate population with
`--sample-count` and `--disagreement-count`; the defaults are not a required quota.
For a short setup chunk, a smaller check can cover the observed disagreement
pairs while retaining comparison clips across every voice. Inspect the generated
`selection` counts and hidden strata, and record why the chosen sample is useful.
For example, 30 total clips with 20 disagreements leaves ten controls; confirm
that the actual allocation covers the intended voices and disagreements. Sparse
evidence or remaining uncertainty may require targeted follow-up after listening.

Serve the resulting audit:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_audit.py serve \
  "/absolute/path/to/session-embedding-audit.speaker-audit.json"
```

The user hears one clip at a time and chooses a participant without seeing the current label, model label, confidence, or whether the clip is a disagreement or control. Transcript text is hidden by default and the decision layer records when it was revealed. Mark cross-talk as **Overlap** rather than forcing one speaker; overlap clips are reported separately and excluded from accuracy denominators. The audit never changes speaker attributions.

After review, generate the comparison:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_audit.py report \
  "/absolute/path/to/session-embedding-audit.speaker-audit.json" \
  --decisions "/absolute/path/to/session-embedding-audit.speaker-audit-decisions.json" \
  --output "/absolute/path/to/session-embedding-audit.speaker-audit-report.json"
```

Use the pair and margin breakdowns to set any later auto-accept policy. Treat the weighted population accuracy as exploratory because the audit deliberately spreads samples across time and confidence rather than taking a simple random sample. Do not apply model labels from the audit itself.

Carry the **human listening decisions** forward before model application. Run
`speaker_recalibrate.py` on the exact frozen review and attributions used by the
audit, adding `--audit <audit.json> --audit-decisions <decisions.json>` and a new
review prefix. The script requires a complete audit, checks its source paths and
hashes, preserves every timed utterance, and imports only human decisions. Hidden
model predictions are never imported. Reviewed overlap becomes an explicit
Unknown identity with the original overlap decision retained in provenance; it
cannot seed a voice profile or inherit a group identity. Other human corrections
remain active. Reuse the compatible embedding cache without recomputation.

Recheck leave-group-out scores after corrected anchors change the profiles and
record the provisional margin/cosine policy with its audit evidence. This recheck
is a diagnostic after using audit labels as references, not a new independent
accuracy estimate. Low-confidence human-identified clips keep their explicit
identities; the rejection policy applies to automatic predictions. New model
verification still follows, including material outside the original audit
population. Do not claim full-recording accuracy from a small selected audit.

## Apply an audited model

Once a blind audit supports using the embedding model, materialize its predictions as a new review layer. This preserves the reviewed source files, retains every explicit utterance override, and applies predictions only to substantial cues:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_model.py apply \
  "/absolute/path/to/session.speaker-review.json" \
  --attributions "/absolute/path/to/session.speaker-attributions.json" \
  --embeddings "/absolute/path/to/session.speaker-embeddings.npz" \
  --output-dir "/absolute/path/to/speaker-review" \
  --review-id "session-model-assisted"
```

Use repeatable `--exclude-utterance` arguments for known cross-talk or otherwise unsuitable clips that should retain their current labels. `--allow-unresolved-verification` permits the time-spread verification pass to proceed before short cues receive the Scribe-ID fallback. After verification, run `apply-scribe-fallback`; remaining below-threshold cues stay `Unknown`, and rendering still requires the explicit `--allow-unresolved` choice.

After verification, preserve a small per-session reference bank from the confirmed samples. It may seed another recording from the same campaign, but every transfer still receives its own time-spread verification because microphone and room conditions may differ:

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_model.py export-reference-bank \
  "/absolute/path/to/session-model-assisted.speaker-review.json" \
  --attributions "/absolute/path/to/session-model-assisted.speaker-attributions.json" \
  --output-dir "/absolute/path/to/session-reference-bank" \
  --samples-per-participant 5
```

The exporter refuses unverified participants and records each clip's participant, utterance, timing, transcript text, attribution provenance, and hashes in `reference-bank.json`.

## Render an identified VTT

```bash
python3 .agents/skills/transcribe-session/scripts/speaker_review.py render \
  "/absolute/path/to/session-135.speaker-review.json" \
  --attributions "/absolute/path/to/session-135.speaker-attributions.json" \
  --output "/absolute/path/to/session-135.identified.vtt"
```

The default labels physical participants by their roster `gameRole`, which produces `DM`, character names, and similar pipeline labels. Real-world `name` values remain in the participant roster used by `prepare-session-source`; do not rewrite the VTT to physical names merely to preserve them.

The renderer requires current verification for each participant with attributed material. A mixed acoustic group renders as `Unknown`, never `Overlap`; cross-talk may be reported as overlap only when it was explicitly reviewed, not inferred from cluster impurity. For the verified reference-bank fast path, render the Scribe-fallback layer with `--allow-unresolved` after confirming that the residuals are below-threshold or unsupported Scribe IDs, not a failed participant transfer. Report their count and speech-duration coverage. `--allow-unverified` always produces an incomplete draft and is not pipeline-ready.

Do not replace the raw Scribe VTT with the identified VTT. Report cluster decisions, exception counts, and unresolved coverage separately.
