# Transcript artifact and response contract

## New inputs

Create the explicitly selected session directory. Write a small JSON metadata file
under `cleaned/transcript-work/input.json` with verified `campaign`, `sessionNumber`, and optional `realWorldDate`,
`drStart`, `drEnd`, and `participants`. Participant entries contain `gameRole`, an
optional real `name`, and `transcriptIdentifiers`. Do not infer unknown dates.

```bash
python3 -B HELPER init --bundle BUNDLE --source RAW_TRANSCRIPT --metadata BUNDLE/cleaned/transcript-work/input.json
```

Supported inputs are VTT (including voice tags), SRT, existing UID lines, and
`[start-end] Speaker: text` lines. Unsupported formats need an explicit faithful
adapter; do not invent timestamps or silently omit malformed units. An external
raw transcript is read-only and copied into `sources/` without changing its bytes.

For ambiguous existing artifacts, `init` accepts bundle-relative `--manifest`,
`--prepared`, and `--cleaned` overrides. `--source` explicitly selects the incoming
original. Existing headers must match between prepared and cleaned inputs.
Source/header conflicts require an inspected migration, not automatic renumbering.

## Files and identity

The helper registers existing prepared/cleaned filenames rather than renaming
them. The existing session-manifest stem supplies new output names. New bundles
use the directory name. Managed artifact paths are bundle-relative; copied legacy
absolute paths are resolved against the copy's local directories, never followed
back into the live vault for writes.

Artifacts produced under `cleaned/` during processing:

- `<stem>-source-prepared.md`: stable UID baseline.
- `<stem>-source-cleaned.md`: current error-corrected text, preserving baseline headers.
- `<stem>-transcript.md`: readable transcript, with hidden source-span comments.
- `<stem>-transcript.json`: ordered turns, exact source spans, source fingerprint,
  attribution corrections, and unresolved issues; suitable for a website renderer.
- `<stem>-transcript.html`: escaped standalone rendering for display and QA.
- `<stem>-transcript-entities.json`: agent-reviewed people, groups, places, time
  expressions and items with exact quoted mentions and source UIDs. This is not
  canonical lore, exhaustive fact annotation, or inferred chronology.
- `<stem>-transcript-review.md`: pending substantive choices with original/proposed wording and recommendations; no incidental appendix.

## File lifecycle

These roles are independent of the current `cleaned/` directory layout:

| File | Purpose and retention |
| --- | --- |
| `sources/<original>` | Permanent evidence: exact incoming bytes, never overwritten. |
| `<stem>-source-prepared.md` | Permanent technical reference: normalized original wording and stable UID/time/speaker baseline for comparison and source links. |
| `<stem>-source-cleaned.md` | Permanent working reference: best supported transcription; primary input to later analysis. |
| `<stem>-transcript.md` | Permanent polished transcript: readable speech, corrected speaker turns, and hidden source-span comments. This is the retained reading/website source. |
| `<stem>-session.yaml` | Permanent session metadata, plus completion status, counts, and retained artifact paths/fingerprints. Corrected attribution lives in the polished Markdown, not a duplicate YAML list. |
| `<stem>-transcript.json` | Temporary structured export for inspection/integration during processing. Removed at finalization; no permanent duplicate of the Markdown is required. |
| `<stem>-transcript.html` | Temporary display/QA export. Removed at finalization; future display can render the retained Markdown. |
| `<stem>-transcript-entities.json` | Temporary exact-mention index supporting the cleanup pass. Removed at finalization; it is not a separate final product. |
| `<stem>-transcript-review.md` | Portable review state: exact targets, context, decisions, reference fingerprints, and affected readable-turn updates in Markdown. Works without the processing queue; removed at finalization. |
| `transcript-work/state.json` | Current turns, fingerprints, and progress for unfinished cleanup/polish/quality work. Not required for the Markdown review handoff. Removed at finalization. |
| `transcript-work/history/` | Submitted responses used during active processing. Removed at finalization; no permanent audit archive. |
| `transcript-work/transactions/` | Temporary snapshots that recover interrupted writes. Removed at finalization after recovery completes. |
| `transcript-work/jobs/`, `responses/`, and other work files | Processing packets and drafts. Removed with the work directory at finalization. Finish wanted work before finalizing. |
| `transcript-finalization.json` | Temporary retirement plan, present only during finalization or an interruption. `finalize`/`recover` resumes it and removes it on success. |

Keep the work directory while cleanup/polish/quality processing remains. A quality-complete
review Markdown is independently resumable with the retained references; no full
work state must accompany it. Use `finalize`
to retire the pipeline's temporary files after review, rather than deleting state
by hand. It is included in the workflow's authorized completion step. The bundle
directory itself supplies the writer lock, so no permanent lock file is needed.
All generated records and temporary files stay inside the selected bundle.
Existing recap prose, beat artifacts, highlights, and historical transcripts are
not rewritten by this workflow.

UIDs are session-local and stable. Character offsets below are zero-based Python
Unicode character indices into the **current cleaned unit text**, with exclusive
`end`. They are not bytes or word counts. A turn may span several UIDs; one UID
may span several turns, without duplicating or dropping source characters.

If speech continues across a work-chunk boundary, the first turn of the later
chunk may set `joinPrevious: true`. Export joins it to the preceding turn only
when the speakers match. Polish both sides' punctuation accordingly; use quality
review's neighboring turns to check the result. Work chunks must not impose an
artificial sentence or speaker boundary on the delivered transcript.

## Clean response

Write a response using the exact `sourceSha256` and chunk ID from the job:

```json
{
  "schemaVersion": 1,
  "stage": "clean",
  "chunkId": "chunk-001",
  "sourceSha256": "COPY_FROM_JOB",
  "checks": ["people", "groups", "places", "time_transitions", "items", "actions", "unmarked_errors", "second_pass"],
  "edits": [
    {"uid": "u0042", "before": "Exact current line text.", "after": "Supported corrected line text.", "kind": "asr", "reason": "Why this is a transcription error.", "evidence": ["u0041-u0044", "consulted vault-relative note path"]}
  ],
  "issues": [
    {"uid": "u0048", "target": {"start": 0, "end": 7, "before": "Oldtown"}, "replacement": "Old Town", "kind": "place", "importance": "material", "reason": "Two place names plausibly match the recognition.", "recommendation": "Prefer this reading because of its sound and the nearby exchange.", "question": "Use this name, choose the alternative, supply a correction, or leave unresolved?", "alternatives": ["Aldtown"], "contextRange": {"startUid": "u0043", "endUid": "u0052"}}
  ],
  "mentions": [
    {"uid": "u0043", "kind": "time", "text": "the next morning"}
  ]
}
```

`edits`, `issues`, and `mentions` may be empty when inspection supports that.
Do not fill the checklist without reading the complete range twice. Edit kinds:
`name`, `asr`, `punctuation`, `uncertainty`. Evidence is a nonempty list of specific
source pointers or actual human corrections; it is not invented corroboration.
Quote each edit's whole current line text, excluding its header. One edit per UID.

Issue kinds: `person`, `group`, `place`, `time`, `item`, `action`, `speaker`, `other`.
Only suspected word-recognition or speaker-attribution problems belong here.
`reason` must identify that suspicion; factual disagreement, uncertainty about
world geography/chronology, ordinary grammar, and spoken self-correction do not
qualify on their own. New issues must have `importance: material`; incidental
classifications from older runs are reassessed, not copied into new submissions.
Require an exact `target` (zero-based start, exclusive end, and `before` text),
a `replacement` string or `null`, and nonempty `recommendation` and `question`.
`alternatives`, when present, are replacement strings for that same target, never
whole passages. The helper constructs each full-UID proposal by replacing only the
target; it rejects free-form `proposal` input. Include marker braces in the target
when a correction should remove them. Do not move speech between UIDs or include
neighboring speech in replacement text. Empty replacement strings can remove an
ASR insertion, but the resulting UID must remain nonempty.

Use `replacement: null` when no credible correction can be recovered. The report
then recommends retaining uncertainty, without a misleading identical Proposed
field. Do not manufacture a negative alternative from the abstract possibility
that ASR omitted “not.” The human chooses credible substantive readings, rather
than certifying every uncertain word.

`contextRange` is optional and session-local. Select the complete exchange that
introduces the referent and gives the response. The default expands through nearby
speaker runs within a bounded word/caption window; it is a starting point, not proof
of sufficient context. Acceptance fingerprints cover the displayed range, including
explicitly selected context beyond adjacent captions.

Issue targets must exactly match the resulting text. Their bounds are validated
before proposals are generated. Every `{{...}}` span must be
reassessed: recover reasonable wording, or remove unnecessary/incidental braces
through an `uncertainty` edit that keeps the words, or retain a consequential
review choice. Flag removal is not ASR recovery. Unmarked material issues are allowed,
including speaker ambiguities whose wording is intact. Repeated issues may share a human-readable
`group` field. The helper assigns stable issue IDs; do not invent them.

Calibrated examples:

- `please they created...` → `Pleased, they created...`: automatic contextual repair.
- `not to kill you or to not not to you` → `not to kill you or to not not kill you`:
  automatic recovery of a joke, preserving its double negative.
- `At least short messages back and since Johar arrives` → `At least short
  messages back and forth once Johar arrives`: automatic when the surrounding
  exchange establishes communication after his arrival. Uncertainty about these
  exact connective words alone does not warrant review.
- An ambiguous name with two credible identities, or an otherwise unknown
  occupation, normally warrants a concrete human choice. A confident name repair
  does not need review simply because it is a name.

Mention kinds: `person` (including PCs/NPCs and other named beings), `group`,
`place`, `time`, `item`. Quote actual source wording. Additional `uncertain: true`
or a short `note` may explain ambiguity; a normalized label must not be used to
claim an identity absent from the source. Include distinctive unnamed referents
when useful. Group multiple mentions for display without erasing source UIDs.

### Speaker corrections

An optional `attributions` list replaces the correction overlays within this
chunk. Omit it to retain unchanged overlays. Use an empty list only when deliberately
removing prior overlays after review. Each entry is:

```json
{"uid":"u0036","start":0,"end":25,"speaker":"Delwath","reason":"The player continues his stated action while the DM describes the interlocutor.","evidence":["u0031-u0044"]}
```

Use actual source offsets. Correcting only part of a UID is allowed; turns must
respect each attribution boundary. If wording changes on a unit with an existing
overlay, explicitly recheck its offsets and resubmit the overlay. Never transfer
an old speaker mapping to changed text without review. The helper retains original
headers and uses the attribution overlay during processing. Downstream consumers
read corrected speakers and their source spans from the polished Markdown.

## Polish response

```json
{
  "schemaVersion": 1,
  "stage": "polish",
  "chunkId": "chunk-001",
  "sourceSha256": "COPY_FROM_JOB",
  "turns": [
    {"speaker":"DM","sources":[{"uid":"u0001","start":0,"end":24}],"text":"Exact words, punctuated."}
  ]
}
```

The illustrative offsets above are not reusable. Start with `draftTurns` or a
faithful legacy candidate, inspect it, and author natural turns. Adjacent spans
must cover the chunk completely in original order. Each span's speaker must match
the source or a recorded attribution overlay. Whitespace/punctuation/capitalization
may change, but lexical words, contractions, numeric punctuation, meaningful
symbols, annotations and remaining review markers must survive outside the
explicit display substitutions described below. A successful token
check is necessary, not sufficient: punctuation can still misrepresent a question,
quoted speech, or a self-correction and requires semantic review.

### Polished-only display substitutions

An optional `substitutions` list on a turn replaces confidently unrecoverable
incidental spans with `[garbled]` or, when overlap is established, `[cross-talk]`.
Source spans still cover every character exactly once. The cleaned UID text is
not changed by a display substitution. Each replacement belongs within one
source span and one UID, with exclusive `end`:

```json
{"speaker":"DM","sources":[{"uid":"u0001","start":0,"end":25}],"text":"Well, [garbled], anyways.","substitutions":[{"uid":"u0001","start":6,"end":15,"kind":"garbled","reason":"Unrecoverable incidental recognition debris; the words on either side remain intelligible."}]}
```

Offsets are illustrative; calculate them against current cleaned text. Use the
smallest damaged span. Bounds must fall between words, must not overlap, and must
not cover a review marker, existing annotation, or wikilink. The validator builds
the expected wording from the exact source spans with these substitutions, then
checks all other words, symbols, markers, and annotations unchanged. Unsupported
labels, missing replacements, and unrecorded omissions fail. Export preserves
substitutions when joining chunks. Their presence records retained uncertainty
but does not add human review work.

## Quality response

Review the actual turns against the source and neighboring turns, in a separate
pass after polishing. Submit:

```json
{"schemaVersion":1,"stage":"quality","chunkId":"chunk-001","sourceSha256":"COPY_FROM_JOB","verdict":"pass","findings":[],"checks":["wording","punctuation","speaker_turns","uncertainty","boundary_continuity"],"note":"Brief concrete assessment of fidelity and readability for this range."}
```

For rework, record findings in the local response, repair the cited turns/source,
and generate a new quality job. `submit` refuses a rework response as completion.
Neighboring polish changes invalidate boundary review. Do not use a boilerplate
pass record as a substitute for reading the output.

## Completion and recovery

`needs_work` identifies unfinished or stale range work. Once all range work passes,
`ready_to_export` (or `ready_to_export_with_review`) still requires export.
Exported status is `needs_quality_review`, `needs_manual_review`,
`complete_with_uncertainty`, or `complete`. Completion requires current hashes
for active exports as well as reviewed source/turn coverage. Missing HTML is allowed; a missing review sheet is allowed
only after required review is resolved. Existing edited exports are still detected.
Status also reports material occurrence/group counts and `displaySubstitutions`;
the report contains pending decisions only, without incidental or completed-item
appendices. Within an active processing queue, source corrections use a new clean
response; `accept` means the human explicitly chose to retain uncertainty. The
Markdown handoff below provides independent review after export. Uncertainty can remain explicit;
material uncertainty requires a human decision before final completion.

After quality-complete export, the review Markdown alone carries review control
data and decisions. With the retained references, `review --apply` updates the
cleaned and readable text and remaps offsets without the original processing state.
`review --finalize` refreshes completion metadata and retires the report. See
[Markdown review](review.md) for its fields and recovery behavior.

After current export and review, `finalize` retires disposable outputs and working
state. Its five retained files are the original, prepared UID, cleaned UID, polished
Markdown, and session YAML. The `transcriptProcessing` metadata field contains the
completion status, counts, and four transcript paths/fingerprints. It does not
write `speakerCorrections`: corrected speakers and within-UID boundaries are
already retained in the polished Markdown's labelled turns and source spans.
Prepared and cleaned headers remain unchanged. Finalization does not retain
attribution reasons, evidence, submitted responses, or a parallel polished JSON edition.

After finalization, `status`/`init` read that record without recreating work. Status
adds `finalized: true`; later missing/edited references produce
`changed_after_finalization`, never a fresh claim of reviewed completion. Repeating
`finalize` is harmless when references match. Work is resumable until finalization;
afterward the job history is intentionally gone. Further substantive revision needs
a bounded `review --prepare UID [UID ...]` against current retained references,
not an automatic replay of earlier processing.

An interrupted retirement reports `needs_finalization`. Rerun `finalize` or
`recover`; the temporary plan checks permanent references and remaining deletion
targets before continuing. Changed files stop recovery for reconciliation. This
plan is removed on success, including when the work directory was already removed.

Changing source text invalidates affected range/context work. Unaffected ranges
remain reusable. An editorial-policy revision also invalidates earlier stage
signatures and exports while preserving their work for reassessment; it does not
reinitialize the source or recreate finalized bundles. Human acceptance is tied to the issue wording and its displayed context range; a change there requires reassessment. A transaction interrupted between files resumes its recorded
writes; a conflicting later edit stops recovery without replacing it. Processing
history stays within the bundle only until finalization. `status` does not mutate files. A stale response is
rejected before source edits. Regenerate its job and reconcile the current content.

Speaker-attribution storage order is not meaningful. Stage fingerprints sort
overlays by UID and character span, so resubmitting unchanged corrections cannot
alternately invalidate neighboring chunks. Changes to an overlay's contents still
invalidate affected work. Older order-sensitive fingerprints may become stale
after this fix; inspect affected work and submit fresh jobs rather than rewriting
stored hashes or treating stale review as current. Finalized reference checks
remain based on the retained artifact fingerprints.

The CLI does not call an LLM. The skill's agent performs the semantic work and
submits evidence-backed responses. Deterministic draft generation alone cannot
establish cleaned or polished quality.
