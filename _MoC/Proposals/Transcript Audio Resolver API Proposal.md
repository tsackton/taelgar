# Transcript Audio Resolver API Proposal

> [!info] Proposal
> Prepared November 2, 2026. High-priority API tooling candidate. Implementation has not started; this document records the proposed scope and first experiment.

## Objective and API value

Use audio-capable models to help resolve difficult passages in recorded sessions: unfamiliar names, overlapping speech, unclear words, and uncertain speaker attribution. Present candidate readings beside the original audio and surrounding exchange so a human can make the final decision.

Codex already handles transcript cleanup and review. The additional capability is direct inference over selected audio clips, including alternative transcription passes. API credits pay for those audio calls; a Codex skill can remain the interface for selecting passages and applying accepted corrections. A separate autonomous cleanup service is unnecessary.

## Existing foundation

The vault already has a transcription and transcript-processing workflow, a listening review page, and shared audio extraction:

- `.agents/skills/process-transcript/references/audio-review.md` describes the existing listening interface and review decisions.
- `.agents/skills/process-transcript/scripts/transcript_audio_review.py` prepares and serves review clips.
- `_scripts/audio_tools.py` handles verified source mappings and clip extraction.
- The transcript-processing and correction workflows own accepted changes and finalization.

Extend these components rather than building another clipper, review queue, or transcript editor. Review Markdown remains the source of truth for human decisions; generated clips and model results are supporting artifacts.

## First useful version

The user selects unresolved questions or specific transcript UIDs. For each selected passage:

1. Verify the source recording and timestamp mapping, including offsets and recording changes. Extract the exchange with enough surrounding audio to interpret it.
2. Show the selected clips and estimated API usage before the authorized upload batch. Existing workflow requirements for uploading audio still apply.
3. Request an independent transcription without supplying the proposed correction. Optionally make a second pass with relevant name spellings or a different audio model, recording which hints each pass received.
4. Show the existing wording, candidate readings, surrounding exchange, original playback, and any disagreement in the existing review interface.
5. Let the reviewer accept a reading, enter a correction, leave it unresolved, or defer. Apply decisions through the established transcript workflow.

Start with uncertain words and names. Treat speaker attribution as a separate capability to evaluate, especially where overlapping speech makes a confident assignment impossible. A model may abstain; an inaudible span should remain uncertain.

## Evidence and failure handling

Lore context can suggest a spelling but cannot establish what was spoken. Preserve spoken factual mistakes rather than correcting speech to match canon. Label contextual candidates separately from audio-supported readings. Agreement between models is not proof, and model-reported confidence is not a calibrated probability.

Store clip identity, recording fingerprint, verified time range, source UID range, model/version, hints, and raw response with each result. Invalidate candidates when the relevant inputs change. Reuse unchanged results on retries and bound the number of calls per passage. A failed API call must leave the existing review and transcripts intact.

Only selected, authorized clips go to the API. Keep original recordings unchanged and retain the existing distinction between disposable listening assets and persistent decisions. The implementation must establish how candidate provenance survives review finalization without creating a competing decision store.

## Pilot and acceptance

Use a small, deliberately mixed set of previously difficult clips: names, ordinary speech, cross-talk, and genuinely unintelligible audio. Include passages with known human-reviewed readings, withholding those readings from the initial model pass.

Measure correct useful candidates, misleading candidates, unresolved cases, listening time saved, and cost per reviewed passage. Compare against the current listening-only workflow. Advance only if the additional calls improve review enough to justify their cost and complexity.

Verify clip alignment, unchanged original recordings, preserved UID/source mappings, stale-result rejection, safe retries, and correct application through the existing correction process.

## Cost and implementation decisions

The main cost is selected audio duration multiplied by the number of passes, plus any text-based comparison. Record actual usage during the pilot; choose current model endpoints and prices at implementation time. Set a maximum batch cost, clip duration, and retry count. Full-session retranscription is outside the initial scope.

Before implementation, choose the first audio model, pilot passages, batch allowance, and result-storage contract. The first milestone is one selected clip producing reviewable candidates in the existing listening page.

Related proposals: [[Pronunciation Audio API Proposal]] and [[Private Discord Chatbot API Proposal]].
