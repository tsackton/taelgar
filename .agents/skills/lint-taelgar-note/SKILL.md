---
name: lint-taelgar-note
description: Lint, re-lint, or batch-lint eligible Taelgar vault notes with deterministic validation and source-grounded editorial judgment, then write or clear versioned lint state. Use when the user asks to lint, re-lint, batch-review, validate the completeness or currency of, or apply Taelgar lint metadata to one or more notes. Never lint notes under Worldbuilding or any dot or underscore directory; do not use for ordinary lore editing without a lint request.
---

# Lint Taelgar Note

Combine deterministic validation with one source-grounded contextual review. The adopted rules live in `../../../_MoC/Taelgar Note Linter.md`; do not reproduce or improvise a competing rule set.

## Gate the target and mode first

- Exclude any note with a `Worldbuilding`, dot-prefixed, or underscore-prefixed directory segment. Ineligible paths remain searchable evidence.
- An otherwise in-scope note is lintable only when its authored body contains a complete natural-language sentence about its subject or source. Visible prose and authored comments or `SECRET`, `Campaign:*`, and `Date:*` blocks can count. Frontmatter, headings, embeds, isolated labels or links, fragments such as `%% dragonet on circular island %%`, editorial reminders, and lint-owned blocks cannot. Screen this semantically before any edit; when uncertain, skip it. Collections omit ineligible notes and samples replace them.
- Use check-only mode when the user asks only for a report or says not to edit. A check-only run writes nothing and does not advance `lintedAt`.
- A lint request authorizes only lint-owned changes. Broader prose rewriting, lore development, or multi-note cleanup still needs approval. Preserve unrelated changes and never expose private DM content.
- Unless the user explicitly requests a re-lint, exclude every note with a valid `lintedAt`/`lintVersion` pair. Staleness, open findings, or newer evidence do not create authorization. Apply re-lint permission only to the scope it modifies.

## Load once and reuse

Read every target completely. Read the adopted specification once per task or batch and capture its `linterVersion`. Load each additional reference only when its rule family applies, and only once per batch:

- metadata or classification: `../../../_MoC/Metadata Specification.md` and `../../../_MoC/Note Categorization.md`;
- non-check statuses: `../../../_MoC/Note Status.md`;
- names or pronunciation: `../../../_MoC/Name Metadata.md` and relevant material under `../../../Background/Languages.md`;
- campaign identities: `../../../_MoC/Campaign Registry.md` and `../../../_scripts/session_note_campaigns.json`;
- article temporality: `../../../_MoC/Temporal POV Metadata.md`.

For a batch, the manifest is the reusable result of link, relationship, `_DM_`, Git-freshness, and deterministic checks. Do not rerun those searches per note unless the packet reports ambiguity, a tool failure, or a contextual question it cannot answer.

## Single-note workflow

Run from the vault root:

```sh
ruby _scripts/validate_taelgar_note.rb --format json "PATH/TO/NOTE.md"
```

For an authorized re-lint with a valid previous timestamp, add `--linted-at "PREVIOUS_TIMESTAMP"`. Require `validatorVersion` to equal the adopted `linterVersion`. Read and judge the complete note, perform the integrated review below, then apply only safe lint-owned changes. Use `--fix-frontmatter` only after the eligibility and preservation checks.

Write completion state as the final scoped edit. Run the validator again with link checks enabled; if it fails, restore the prior completion state. Never perform a version-only migration or carry an old report forward without re-evaluating it.

## Batch workflow

Use the batch wrapper for two or more notes; its `prepare` step replaces individual initial validator runs. Before preparing, confirm the sentence requirement for every candidate and replace rejected sample candidates until the requested count is reached.

```sh
ruby _scripts/lint_taelgar_notes.rb prepare --output /tmp/taelgar-lint-manifest.json "PATH/ONE.md" "PATH/TWO.md"
```

Use `--re-lint` only when explicitly authorized. Broad `--all-linted` and `--stale` selectors also require `--re-lint`; `--only-needs-review` may narrow that authorized maintenance scope. Inspect `selectionSummary`, including `skippedNoReviewableProse`, and confirm every included note is both authorized and semantically lintable.

Read each included note completely. Use its manifest packet plus one integrated contextual evidence pass; do not repeat the packet's mechanical work. Apply supported persistent metadata and other lint-owned edits without changing the old completion state, tag, or report. Then snapshot once:

```sh
ruby _scripts/lint_taelgar_notes.rb snapshot --manifest /tmp/taelgar-lint-manifest.json --output /tmp/taelgar-lint-decisions.json
```

Set every decision to `clean` with no report, or `open` with one complete replacement `%%^Lint%%` block. Finalize once:

```sh
ruby _scripts/lint_taelgar_notes.rb finalize --write --manifest /tmp/taelgar-lint-manifest.json --decisions /tmp/taelgar-lint-decisions.json
```

The write command preflights every candidate before writing any, uses one timestamp and validator version, verifies reviewed checksums and prior state, validates the proposed notes, writes same-directory replacements, verifies the written hashes, and rolls back ordinary write or verification failures. A non-writing finalize remains available for diagnosis but is not a required duplicate pass. Never bypass the finalizer.

## Perform one integrated contextual review

Use one evidence set to decide all applicable rule families rather than restarting the search for each:

1. **Deterministic findings:** resolve or carry forward every actual error, warning, and suggestion. Do not turn informational output into open work.
2. **Evidence and coverage:** search filenames, identity metadata, variants, links, backlinks, and relevant passages not already resolved by the packet. Follow vault source authority. Session notes and Primary Sources are records, not omniscient truth, and are not declared factually wrong. Worldbuilding is provisional. Distinguish internal conflict, external conflict, established missing information, and unestablished development opportunity. Report omitted established information only when its absence materially misleads or leaves the central account outdated; suggestions require specific evidence, a concrete improvement, and enough importance to retain lint status.
3. **Editorial sufficiency:** assign exactly one verdict: **Sufficient**, **Sufficient, worth expanding**, or **Underdeveloped**. Judge the note's reference role, demonstrated importance, setting-specific substance, central established role or state, and visible completeness. Do not infer insufficiency from brevity, backlinks, status tags, `dm_notes`, generic genre expectations, or extra facts elsewhere. A short minor connector can be sufficient; an important subject represented only by a generic definition can be underdeveloped. Several central headings containing only placeholders or hidden planning can make a long note underdeveloped, but one peripheral unfinished section usually does not. For a person, a defining relationship, role, and fate can suffice for a minor connector; an important person needs any established central consequences and current state. **Sufficient, worth expanding** is handoff-only and never creates or retains a Lint block, `status/check/lint`, or an editorial comment. For **Underdeveloped**, use the applicable coverage rule when established information is missing or outdated; otherwise report `editorial.note_underdeveloped` only with concrete evidence, the exact central missing dimensions, and the smallest useful development scope. Never duplicate the same gap under both rule families or use a vague prompt to expand.
4. **Freshness and temporal framing:** use Git and manifest evidence from the prior `lintedAt`. Later material change requires a human choice among updating the article and `POV`, deferring with the applicable game-update status, or preserving the earlier article. Never change a game-update tag during linting. Obey `deterministic.reviewGates.pov`: an existing `povNotes` block always makes review required, regardless of prior lint version, and the linter must retain that block. Removing an existing `povNotes` block is always a human-only decision. Only when `povNotes` is absent does the version gate apply; if `required` is then false, preserve both the valid existing `POV` and the absence of `povNotes`. Deterministic missing or malformed `POV` still requires resolution. When review is required, choose `POV` from the undated visible article frame under the adopted temporal rules and do not let a narrow dated event redefine the whole article. If no temporal information or material temporal constraint is established, a retained block may simply describe the note as broadly modern. Notes under `Campaigns/**` tagged `session-note`, `meta`, or `source` require `POV` and must not be given a new `povNotes` block; if such a note already has one, retain it and report the categorical mismatch for human review.
5. **Privacy:** independently review substantial shared comments and `Campaign:none` blocks for important public-safe omissions or concrete adoption candidates, without promoting them automatically. Never copy or paraphrase `SECRET` or local `_DM_` content into a shared report. Use validator or manifest `_DM_` matches for the gated `dm_notes` review: matches do not invalidate `dm_notes: none`, and no match does not authorize clearing a positive human attestation.
6. **Names and metadata:** obey the independent name-review gate; do not redo a skipped pronunciation search. Preserve existing unresolved name entries and keep proposals out of frontmatter until accepted. Follow deterministic candidates and the adopted references for classification, campaigns, maps, persistent-block placement, and actual pronunciation values.
7. **Statuses:** do not assess `status/check/*`. Disposition every other existing `status/*` as supported, questioned with evidence, or not assessable, without changing it. Only the report lifecycle may add or remove `status/check/lint`.

## Apply changes and completion state

Apply a change automatically only when exactly one lint-owned correction satisfies the adopted rules and preserves lore meaning, uncertainty, attribution, temporal framing, and player/DM visibility. Safe cases include deterministic frontmatter normalization, versioned lint state, and an unambiguous mechanical conversion. Propose rather than apply prose or lore changes, competing interpretations, visibility-changing blocks, ambiguous conversions, human attestations, and non-lint status changes. Never change `headerVersion`.

Write the validator's exact quoted version and an offset-bearing timestamp only after the full review. Completion state is atomic:

- **Open:** one final `%%^Lint%%` block, `status/check/lint`, and at least one unchecked task with severity, stable rule ID, evidence, and a copy-ready candidate where applicable.
- **Clean:** no Lint block and no `status/check/lint`; retain the new completion pair and supported persistent metadata.

Reports contain only current open work. Preserve unresolved human decisions; do not keep checked tasks, empty reports, or tags justified only by information. Record applied changes in an open report or, for a clean lint, in the handoff.

## Verify and hand off

For a single note, re-read the complete result, inspect the complete diff, and run scoped `git diff --check`; the final validator is the deterministic proof.

For a batch, successful all-or-nothing finalization plus verified written hashes is the deterministic proof of YAML, links, tags, completion state, structured blocks, and file integrity. Do not rerun the validator, recheck clean/open invariants, or compare the files with the finalized manifest unless there is a mismatch, tool-reported anomaly, or later manual edit. Inspect the complete scoped diff once and run scoped `git diff --check`. Re-read an individual finalized note in full only if the change affects body prose, private or visibility-sensitive content, or unusual or custom syntax; if the diff lacks enough context to judge the result; or if an anomaly appears. Otherwise, do not perform a second full-note read.

State each note's editorial sufficiency verdict in the chat handoff, along with which files changed, whether each result is clean or open, what human work remains, and what validation passed. Do not write a sufficiency verdict into the note. If the skill or tooling changed, run its focused tests and the skill structural validator.
