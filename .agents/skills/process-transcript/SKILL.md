---
name: process-transcript
description: Process or resume an existing session transcript into original and prepared UID references, corrected UID text, and readable full-session Markdown. Makes reasonable contextual ASR repairs, substitutes unrecoverable incidental speech only in the polished version, and presents concrete proposals for consequential human decisions. Supports review from Markdown without saved processing state and bounded revisions of finalized transcripts. Starts after transcription; excludes factual correction, recaps, and highlights.
---

# Process Transcript

Use this for requests such as “process the transcript from Dunmar session 53,”
“finish the readable transcript,” or “resume transcript processing.” An invocation
authorizes this workflow's transcript outputs and control files within the selected
session bundle. A preview request stays read-only. Never run live sessions while
developing/testing this skill unless the user separately requests that processing.

## Products and boundaries

Keep these transcript references permanently:

1. The original incoming transcript, preserved byte-for-byte under `sources/`.
   An identified/merged transcript received from an upstream workflow remains that
   workflow's product; do not describe it as untouched service output.
2. The prepared transcript: original wording with stable UIDs, timestamps, and
   speaker headers, so the user can check the original text by UUID.
3. A cleaned UID transcript suitable for finding people/NPCs, organizations/groups,
   places, time expressions/transitions, and things/items, with the context needed
   to understand the recorded speech about who acted, where, and when. Preserve
   uncertainty about the words actually spoken; do not adjudicate the claims.
4. A full-session readable Markdown transcript with source spans. Preserve
   recoverable speech and table talk; narrowly replace unrecoverable incidental
   spans with `[garbled]` or `[cross-talk]` in this version only.

Keep the session YAML metadata alongside them. JSON/HTML exports, the entity/time
mention index, review report, and processing state serve the active workflow and
are removed at finalization. The review report is for resolving transcription
questions; it is not a permanent reference. Auditability is not a retention goal.

An **ASR error** is a word or phrase the recognition system misheard, omitted, or
inserted. Speaker-attribution errors are a related, separately identified concern.
The transcript records what was said, including factual mistakes, contradictions,
misremembered names/dates, jokes, grammar errors, and self-corrections. None of those
is an ASR error merely because the statement is implausible or conflicts with lore.

Judge recoverability separately from importance. Recover incidental jokes and
ordinary wording as actively as names and actions. Use the best reading supported
by approximate sounds, syntax, and the full exchange; exact independent
corroboration is not required. Uncertainty about exact wording alone does not
justify human review when reasonable alternatives preserve the same clear meaning.
Prefer a repair close to the recognized wording and preserve genuine disfluency.
A merely conceivable missing “not” is not a competing reading: require support in the recognized sounds or exchange. Judge materiality
by what a different reading changes in the account; an unrecoverable roll total
with a clear outcome or incidental table chatter usually needs no human question.

Ask for review when credible alternatives change substantive information, such as
which person acted, an otherwise unknown occupation, or a materially different
action. Confident name corrections remain automatic. For each review item,
identify the recognition concern and present a proposed revision, recommendation,
and concrete choice. Do not ask whether a place, date, event, or claim is correct.
An awkward sentence or a contradiction alone is insufficient. For example, an ASR
rendering such as "Barry Chico" for a spoken setting name can warrant recovery;
"200 miles south" conflicting with a map cannot, without separate evidence that
the words were transcribed incorrectly. Preserve spoken self-corrections in full.

Existing markers are candidates for reassessment, not proof of recognition errors.
Remove braces around ordinary fragments, abandoned starts, incidental cross-talk,
and unrecoverable incidental noise; retain their underlying text in the cleaned
UID reference. Remove factual-doubt flags as well. These are `uncertainty` edits,
not recovered speech or human acceptance. Do not replace a
clearly spoken older/wrong name with the later canonical name. Lore can help rank
plausible recognition candidates; it cannot rewrite the recording. Do not discard
a good phonetic/contextual candidate just because lore helped identify it. Read
[the review calibration examples](references/review.md#editorial-calibration) when
judging residual nonsense, negation, or lore-assisted candidates.

This workflow does not transcribe/upload audio, classify voices, merge recordings,
create beats/recaps, extract highlights, or modify canonical notes. Read relevant
vault evidence when needed. Keep **every write inside the selected session bundle**,
including jobs, response plans, history, locks, snapshots, decisions, and temporary
files. Do not use a global queue, `/tmp` plan, shared correction dictionary, or an
older helper whose output path comes from archived configuration. In particular,
copied bundles may retain absolute paths pointing to the live vault.

Use Python 3.9+ with PyYAML. Run helpers with `python3 -B` to avoid writing import
caches beside the skill. Commands below use `HELPER` for this skill's absolute
`scripts/transcript_pipeline.py` path and `BUNDLE` for the resolved session directory.

## Resolve and normalize

1. Follow repository branch/worktree requirements before editing a live bundle.
   Resolve a campaign/session request read-only:

   ```bash
   python3 -B HELPER resolve --vault-root VAULT --campaign dunmar --session 53
   ```

   Use the single returned bundle, or an explicitly supplied bundle path. Do not
   create another copy during an ordinary processing run. Missing/ambiguous sources
   require a precise selection, not guessed session identity. For development,
   explicitly copy selected bundles to a temporary test directory first and pass
   only the copy to mutating commands.

2. Inspect existing artifacts and local changes. If a readable transcript and review
   Markdown already exist, use [the Markdown review workflow](references/review.md)
   directly. That Markdown is the complete review state; the original processing
   queue is not required and must not be reconstructed. For new/in-progress
   cleanup and polishing, run:

   ```bash
   python3 -B HELPER init --bundle BUNDLE
   python3 -B HELPER status --bundle BUNDLE
   ```

   `init` registers original/prepared/cleaned paths, normalizes working text to UTF-8
   and LF, preserves existing UID/header structure, and creates a durable work queue.
   It is idempotent. It does not move/rename files, normalize unrelated recap/beat
   artifacts, or overwrite archived originals. Temporary recovery snapshots protect
   interrupted writes. Existing cleaned text is the starting point, never discarded merely
   because an old report or acceptance file is missing.

   For a new bundle with only a raw transcript, read
   [the artifact and response contract](references/contract.md#new-inputs). Supply
   verified campaign/session metadata and participant mappings; preserve unknown
   dates. Never overwrite an existing baseline to resolve a structural mismatch.

3. Treat legacy polished excerpts as candidates. Jobs include overlapping excerpts
   and whether their words/speakers match the current cleaned source. Inspect
   differences for missed upstream corrections, obsolete content, or over-polish.
   Resolve supported corrections in the cleaned transcript; preserve ambiguity as
   an issue. Reuse faithful punctuation/turns where useful. Account for unlinked
   files and overlapping excerpts without duplicating speech. Do not change recaps,
   highlight files, or historical excerpts as a side effect.

## Clean and recover

Request the next job:

```bash
python3 -B HELPER work --bundle BUNDLE --stage clean
```

Read the returned job in full. Work only on its assigned source range; neighboring
lines are context. Existing cleaned text still needs an inspection for missed
errors, not a fresh rewrite. Use the response schema in
[contract.md](references/contract.md#clean-response).

- Inspect every line, then perform a second pass. Check people and possessives,
  groups, places, time expressions/transitions, things/items, actions and negation,
  as well as ordinary English that may disguise a name. Keep a session-local list
  of established corrections/evidence in the work directory when useful.
- Use conversation context, participants, repeated usage, and relevant vault
  sources. Canonical spelling can establish a likely name; it cannot prove that a
  speaker said it. Preserve spoken mistakes, competing readings, and novel names.
- Repair likely ASR errors, including ordinary English, jokes, and errors outside existing markers. Every
  change needs exact before/after text, a reason, and traceable evidence. Evidence
  can be nearby UIDs, an actual user correction, or consulted source paths. Do not
  copy private DM passages into shared output.
- Written source matching can support wording when a speaker is evidently reading
  that source, but retain spoken departures. Archived ASR is not independent
  corrective authority. Do not silently reconstruct missing dialogue from lore.
- Reserve `{{...}}` for unresolved consequential choices needing human review.
  Recover reasonable wording first; remove unnecessary and incidental flags.
  Preserve ordinary annotations, wikilinks, and underlying unrecoverable text in
  the cleaned reference. Do not insert `[garbled]` or `[cross-talk]` there.
- Every retained marker and important unmarked issue needs an exact replacement
  target (UID, character bounds, and current text). Supply only replacement words;
  the helper generates the full proposal while preserving the rest of the UID.
  Include a complete exchange in the review context, expanding the default range
  when the referent or response is missing. Each issue needs a concrete proposal,
  preferred reading with a brief reason, and a decision the user can make. Include
  genuine alternatives when useful. If no credible wording can be recovered,
  recommend leaving the consequential span unresolved and say what an audio check
  would resolve. Never invent a candidate just to populate the report. Group
  repeated issues while retaining their occurrence UIDs. See the calibrated
  examples and fields in [contract.md](references/contract.md#clean-response).
- Record entity/time mentions as exact source quotes with UIDs. Include unnamed
  but relevant referents (“the hunter,” “their village”), relative time language,
  and uncertain names when present. Avoid inventing identities or dates. A category
  may have no mentions; the inspection checklist records that it was considered.
- Record a speaker correction only when context or human evidence supports it.
  The helper stores an attribution overlay with source character spans; prepared
  and cleaned headers remain stable. Both polished output and its structured
  provenance use this overlay. It also supports multiple speakers within one UID.
  Preserve uncertain speakers as such and assess their materiality.

Write the response only to the returned bundle-local response path, then submit:

```bash
python3 -B HELPER submit --bundle BUNDLE --response cleaned/transcript-work/responses/clean-chunk-001.json
```

Continue until `status` shows no pending clean jobs. An edit can invalidate a nearby
review because its context changed; inspect that job again without undoing valid
work. Do not stop mid-session to ask about ASR. Complete independent work first.

## Polish without rewriting speech

Request `work --stage polish`. The job supplies source units, context, attribution
overlays, legacy candidates, and **unreviewed** draft turns. Read the entire range
and author the polished turns using [the polishing contract](references/contract.md#polish-response).

- Preserve every recoverable word, repetition, hedge, false start, awkward construction,
  grammatical mistake, tense shift, fragment, joke, rules discussion, and aside.
  “Anyways” stays “anyways”; “got denser” stays “got denser”; “long, long since”
  keeps both “long”s. Do not delete filler merely because it reads awkwardly.
- Change punctuation, capitalization, sentence boundaries and paragraph/turn
  grouping to make the existing speech legible. A fragment may remain a fragment.
  Do not add words to complete a sentence or convert dialogue into narrative.
- Merge adjacent same-speaker units into natural speech; divide long turns at
  rhetorical/topic boundaries. Use source character spans when splitting a UID.
  Cover every source character exactly once in order. Avoid arbitrary turns based
  on a fixed line count. Read across work-chunk boundaries; use `joinPrevious`
  when a sentence/turn continues into the next chunk.
- Preserve unresolved braces, annotations, symbols, and numbers. The validator
  rejects changed words, missing speech, and unrecorded speaker changes. Passing
  that check does not prove sensible punctuation or speaker attribution.
- When confident that an incidental span is unrecoverable recognition debris,
  replace only that span with `[garbled]`. Use `[cross-talk]` when overlapping
  speakers are confidently established; do not infer overlap solely from nonsense
  text. Keep intelligible words on either side, and retain source coverage via the
  turn's exact `substitutions` spans (see the polishing contract). The cleaned text
  stays intact. These labels do not create review items. Do not use them to hide
  awkward but intelligible speech or an unresolved consequential choice.
- If polishing reveals an ASR or speaker error, record it through a new clean job
  for that chunk, then refresh affected polish jobs. Never hide a substantive
  correction only in the polished output.

Submit all polish responses. Then run a separate quality pass with `work --stage
quality`. Review the actual polished wording against source, punctuation, speaker
turns, uncertainty, and neighboring boundaries. Check sentence starts and name
capitalization after merges, and inspect the final assembled passages across chunk
boundaries. Challenge every remaining flag: attempt a reasonable repair, remove
an unnecessary flag, or provide a useful decision. Inspect each display
substitution and the intelligible speech around it. Quality jobs enumerate these
spans as `recoveryCandidates`; revisit the recognized words with their exchange
before retaining a label. Also look for ordinary English masking names or short
responses (see the calibration examples). These checks require editorial judgment;
coverage and token tests cannot certify recovery quality. The quality reviewer may be the
same agent taking a distinct pass. Do not spawn agents unless separately authorized.
Return `pass` only after inspection; revise cited turns or upstream corrections
when needed and repeat the affected checks. A generated scaffold is not polished.

## Export, secondary review, and resume

```bash
python3 -B HELPER export --bundle BUNDLE
python3 -B HELPER status --bundle BUNDLE
```

Export requires complete source coverage and current clean/polish work. It can
produce explicitly provisional products while quality or human review is pending.
Final status also requires all quality jobs. Inspect the Markdown/HTML appearance
and report current output paths, remaining material issue groups, and any source
limitations. No routine approval is needed when no material uncertainty remains.

The exported review Markdown is a portable handoff containing pending questions,
exact targets, proposals, surrounding exchanges, and the information needed to
apply decisions to the retained references. **It is the review state.** No separate
review-state file, original job queue, or saved response history is required.
After quality review is complete, follow [the Markdown review workflow](references/review.md)
to record actual user choices, update affected readable turns, and apply them:

```bash
python3 -B HELPER review --bundle BUNDLE
python3 -B HELPER review --bundle BUNDLE --apply
python3 -B HELPER review --bundle BUNDLE --finalize
```

Present one session at a time with original wording, a proposed correction or an
explicit retain-unresolved recommendation, and enough context to decide. Resolve
only actual user decisions. Retaining uncertainty preserves the words; it does not
confirm a reading as fact. The agent maintains the Markdown's hidden control blocks
and readable-turn updates; the user can answer in ordinary chat.

The older `accept` command remains available inside an active processing queue;
it means accepting uncertainty, never applying a proposed correction. Do not require
that queue when continuing a review from its Markdown handoff.

On resume, `status` is read-only; it reports pending/stale jobs and whether exported
files still match. Continue the earliest affected stage. Mutating commands recover
interrupted recorded transactions under the session lock; `recover` can do so
explicitly. A conflicting later edit blocks recovery and remains untouched.
Manually changed exports are never silently overwritten: reconcile their changes
first, then use `export --replace-exports` within the user's authorized scope.

The helper serializes writers within one bundle and uses source fingerprints to
reject stale plans. Separate session bundles share no mutable state. Keep
`transcript-work/` while cleanup, polishing, or quality work remains; it supports
resumption of those stages. After a quality-complete export, review can move to
another checkout with only the review Markdown and retained references. The work
folder need not be transferred or preserved for that review.

## Finalize after review

Once all cleanup, polish, quality, and required manual review are complete, export
the current results and finalize as the last step of this workflow:

```bash
python3 -B HELPER finalize --bundle BUNDLE
python3 -B HELPER status --bundle BUNDLE
```

Finalization keeps the **original, prepared UID, cleaned UID, polished Markdown,
and session YAML**. The prepared transcript remains the permanent original-text
lookup by UUID. Existing session metadata and its comments are preserved; a compact
completion field records the retained paths, current fingerprints, completion
status, and any speaker corrections needed because UID headers remain unchanged.
These fingerprints detect later changes without keeping processing history.

Finalization removes the pipeline's JSON/HTML exports, entity index, completed
review report, and the entire `transcript-work/` folder, including jobs, responses,
history, and transaction snapshots. It does not remove unrelated session artifacts
or older workflows' files. This retirement is part of normal completed processing;
do not finalize a review-only request or fabricate a human decision to clear the gate.

The command refuses incomplete review, stale exports, and changed outputs. Accepted
uncertainty may remain explicit in the retained transcripts. If interrupted, rerun
`finalize` or `recover`; later conflicting edits stop retirement for reconciliation.
`status` remains read-only after completion, and repeated `init`/`finalize` does not
recreate processing files. For a later authorized correction, use
`review --prepare UID [UID ...]` to create a bounded Markdown review from current
finalized references. Preserve existing
speaker assignments; inspect and validate the revised turns. Do not silently
restart full processing or claim that old review covers the new words.
See the [file lifecycle](references/contract.md#file-lifecycle) for retention details.

## Maintenance checks

See [testing.md](references/testing.md) for isolated regression commands and the
initial cross-campaign pilot results. Keep integration tests on temporary copies.
