---
name: lint-taelgar-note
description: Lint, re-lint, or batch-lint eligible Taelgar vault notes with deterministic validation and source-grounded editorial judgment, then write or clear versioned lint state. Use when the user asks to lint, re-lint, batch-review, validate the completeness or currency of, or apply Taelgar lint metadata to one or more notes. Never lint notes under Worldbuilding or any dot or underscore directory; do not use for ordinary lore editing without a lint request.
---

# Lint Taelgar Note

Combine deterministic validation with one source-grounded contextual review. The adopted rules live in `../../../_MoC/Taelgar Note Linter.md`; do not reproduce or improvise a competing rule set.

## Isolate live guidance from lint history

- For ordinary lint, re-lint, batch, and check-only work, do not search, read, cite, or rely on Codex memories, rollout summaries, or prior-run guidance. The live skill, adopted specification, current validator, current governance files, and current vault evidence are the only procedural authorities.
- Consult historical linter material only when the user explicitly asks for history, rationale, maintenance, or regression analysis. Version-specific historical results never establish the current workflow or rule set.
- `linterVersion` is a human-controlled parameter. Never change it unless a human explicitly directs that version change. Do not infer authorization from implementation, specification, test, outcome, or maintenance changes.
- A task that changes `linterVersion` includes a mandatory read-only memory audit before handoff. Check whether active memory presents the superseded version as current or routes ordinary lint work to version-specific historical guidance. If correction is needed, tell the user and request the direct authorization required to submit a memory-update note; do not declare the version-update lifecycle complete without surfacing that step. Generated memory files are never edited directly.

## Gate the target and mode first

Apply the adopted specification's **Applicability** and **Modes and authorization** sections. Operationally:

- Reject every target with a `Worldbuilding`, dot-prefixed, or underscore-prefixed directory segment; those paths remain searchable evidence.
- Use the validator's objective authored-body screen, then have the editorial worker semantically confirm each surviving candidate under the specification. Uncertainty after the mechanical screen favors inclusion; collections omit confirmed ineligible notes and samples replace them.
- Check-only writes nothing and does not advance `lintedAt`.
- A lint request authorizes only lint-owned changes. Preserve unrelated work and keep local `_DM_` and `SECRET` contents out of Git-tracked output.
- Unless the user explicitly requests a re-lint, exclude every note with a valid `lintedAt`/`lintVersion` pair. Staleness, open findings, or newer evidence do not broaden that authorization.

## Load once and reuse

Read every target completely. Read the adopted specification once per reviewing context and capture its `linterVersion`. For a single-note lint, load each additional reference only when its rule family applies and only once for that review. For a batch, each fresh worker loads every additional authority applicable to its shard once and reuses it across all assigned notes; do not reload an authority separately for each note. The coordinator loads only authorities needed for its own orchestration, and its read never substitutes for a worker's read:

- metadata or classification meaning and usage: `../../../_MoC/Metadata Specification.md` and `../../../_MoC/Note Categorization.md`;
- place `typeOf` vocabulary validation: `../../../_MoC/Data Categorization/Place Categories.md`; its `canonical` and `linterAliases` fields define the exact accepted values and aliases, while `Note Categorization.md` explains their semantic meaning and appropriate use;
- non-check statuses: `../../../_MoC/Note Status.md`;
- names or pronunciation: `../../../_MoC/Name Metadata.md` and the relevant entries supplied from `../../../_scripts/language_pronunciation_analogues.json`;
- campaign identities: `../../../_MoC/Campaign Registry.md` and `../../../_scripts/session_note_campaigns.json`;
- article temporality: `../../../_MoC/Temporal POV Metadata.md`.

For a batch, the manifest is the reusable result of link, relationship, `_DM_`, Git-freshness, and deterministic checks. Do not rerun those searches per note unless the packet reports ambiguity, a tool failure, or a contextual question it cannot answer.

`../../../Background/Languages.md` remains the ordinary prose authority for language analogues. `../../../_scripts/generate_language_pronunciation_analogues.rb` records every level-five language heading, direct language and family analogue statements, family membership, explicit parent-language inheritance, lookup terms, and exact provenance in the generated JSON. It preserves each analogue statement's complete wording and mapping status; qualified or undefined mappings can still carry useful naming guidance and must not be reduced to their most conspicuous real-world language. Normal lint preparation reads the existing sidecar and performs only a filesystem freshness check. Run the generator with `--write` only when `Languages.md` is newer than the sidecar; `--check` tests that inexpensive boundary, and `--audit` reports name-block language values not covered by any entry or lookup term without inventing guidance for them. Workers use the packet's matched language and family entries, including inherited fallbacks, and do not parse the prose note repeatedly. The sidecar supplies guidance and provenance, not pronunciation rules; the worker still makes the contextual pronunciation judgment. If it is missing, stale, or insufficient for a name, regenerate it or read the authoritative language note rather than guessing.

`../../../_scripts/generate_worldbuilding_discussion_index.rb` maintains the complete non-Staging Worldbuilding discussion sidecar at `../../../_scripts/worldbuilding_discussion_index.json`. Keep it outside ordinary evidence packets and do not load or use it to decide editorial sufficiency. Only after a note is independently judged **Underdeveloped** may a single-note lint query it. In a batch, workers do nothing with it: the finalizer loads it lazily only when an Underdeveloped result exists and inserts the compact research route mechanically. The route is informational note-local output, not a finding or chat handoff.

## Select samples and collections mechanically

For a random sample, capped alphabetical collection, directory-wide collection, or lint-state-based collection, run the read-only selector from the vault root instead of hand-building the target list:

```sh
# Five random unlinted People notes
ruby _scripts/select_taelgar_lint_notes.rb --random --cap 5 People

# First ten alphabetical unlinted Chardonians notes
ruby _scripts/select_taelgar_lint_notes.rb --cap 10 People/Chardonians

# Every unlinted note under one directory (no cap means all matches)
ruby _scripts/select_taelgar_lint_notes.rb People/Chardonians

# Ten random stale completed notes from the vault
ruby _scripts/select_taelgar_lint_notes.rb --re-lint --state stale --random --cap 10 .
```

The default state is `unlinted`, meaning no valid `lintedAt`/`lintVersion` pair. `linted` means any valid pair, `stale` means a valid pair whose version differs from the live validator version, `current` means a valid pair at that exact version, and `all` ignores completion state. The completed-note states require `--re-lint`; use that flag only when the user explicitly authorized re-linting. With `--re-lint` and no explicit state, the selector uses `all`. Alphabetical order is the default. `--random` records its effective seed in the JSON, and an explicit `--seed` reproduces a sample. Omit `--cap`/`--limit` to select the entire matching scope. Multiple file or directory scopes form one deduplicated collection.

The selector recursively discovers Markdown files, applies the batch linter's path exclusions and objective authored-body screen, filters completion state, orders the survivors, and applies the cap last. Its default JSON reports counts, state breakdown, exclusions, random seed, and exact selected paths; `--format paths` emits only those paths. It never edits notes and does not replace the editorial worker's semantic eligibility judgment. Run it once per requested collection, show the user the exact paths before review when they requested that gate, and reuse the same list for preparation rather than drawing another random sample.

## Keep semantic judgment on Sol xhigh

Use `gpt-5.6-sol` with `xhigh` reasoning for every semantic eligibility, source-authority, privacy, coverage, editorial sufficiency, finding-selection, and report-writing decision. If the current agent is not running that model and effort, delegate the complete judgment-bearing review of each note to a fresh Sol xhigh worker rather than splitting one note's decisions across models. Deterministic scripts remain authoritative for selection, manifests, shard construction, schemas, checksums, finalization, and rollback. `gpt-5.6-terra` at `high` may help execute those mechanical operations but must not reinterpret an editorial result.

## Single-note workflow

Run from the vault root:

```sh
ruby _scripts/validate_taelgar_note.rb --format json "PATH/TO/NOTE.md"
```

For an authorized re-lint with a valid previous timestamp, add `--linted-at "PREVIOUS_TIMESTAMP"`. Require `validatorVersion` to equal the adopted `linterVersion`. Read and judge the complete note and perform the integrated review below. Check-only stops after reporting that review and leaves the target unchanged. In write mode, apply only safe lint-owned changes; use `--fix-frontmatter` only after the eligibility and preservation checks. After assigning an Underdeveloped verdict, and never before, query `ruby _scripts/generate_worldbuilding_discussion_index.rb --query "PATH/TO/NOTE.md"` from the vault root. When the returned record has `significant: true`, add the specification's one informational discussion-research line to `### Editorial assessment`; do not include its source list in the Lint report or chat handoff.

In write mode, write completion state as the final scoped edit. Run the validator again with link checks enabled; if it fails, restore the prior completion state. Never perform a version-only migration or carry an old report forward without re-evaluating it.

## Batch workflow

Use the batch wrapper for two or more notes. `prepare` replaces individual initial validator runs and performs only the objective authored-body screen; fresh editorial workers decide semantic eligibility inside bounded shards.

```sh
ruby _scripts/lint_taelgar_notes.rb prepare --output /tmp/taelgar-lint-manifest.json "PATH/ONE.md" "PATH/TWO.md"
ruby _scripts/lint_taelgar_notes.rb workspace --manifest /tmp/taelgar-lint-manifest.json --review-dir /tmp/taelgar-lint-review
```

Authorization remains exact: `--re-lint`, `--all-linted`, and `--stale` require explicit re-lint permission; `--only-needs-review` may narrow that scope. Inspect `selectionSummary`, including `skippedNoReviewableProse`. Use `--force-dm-review` only with `--re-lint` and explicitly named targets when the user requests repair of a completed `dm_notes` evidence review; it reopens only that contextual gate.

The workspace uses largest-estimate-first balanced bins under a 40,000 estimated input-token cap, including packet size and complexity allowances. Oversized notes receive singleton shards; path locality is only a tie-breaker. Sharding balances the user-selected run and never broadens its scope.

The coordinator and every judgment-bearing worker use `gpt-5.6-sol` with `xhigh` reasoning. Start one fresh-context worker per available shard slot without inherited conversation turns. Give it only the skill, adopted specification, assigned packet, staged candidates, and result path; it loads applicable additional authorities once for its shard. The staged candidate directory and exact result path are its write allowlist, although it may search the full vault. An optional `gpt-5.6-terra` `high` helper may perform preparation, sharding, schema and hash checks, completion tracking, and finalization, but no semantic or report-language decisions.

Each worker reads every assigned note completely, performs one integrated evidence pass, edits only its staged copy, and preserves the prior completion state until finalization. For each note its result supplies:

- `eligibility` and `eligibilityReason`; an ineligible note has no staged change, verdict, outcome, report, handoff, or review payload;
- for an eligible note, exactly one `editorialVerdict`, a clean or open `outcome`, conforming `lintReport`, declared objective `bodyEdits`, `editorialAssessment` when Underdeveloped, and `expansionCandidate` when worth expanding;
- complete `dmNotesReview`, `secretReview`, and `sharedNonpublicReview` dispositions. Review each unique dossier cluster once. For confirmed material, distinguish no useful remainder from plausible public or private recovery and provide the structured summary and bounded copy-ready candidate when useful;
- a completed `selfReview`, including `privacySanity` and candidate validation; and
- `candidateSha256` computed only after the staged candidate and result are final.

Private recoveries and expansion candidates stay in those structured fields. Never copy or paraphrase `_DM_` or `SECRET` contents into `lintReport`; privacy review is semantic, not raw overlap screening. The finalizer renders the handoff and mechanically routes exact reportable `_DM_` source links: into an open report, or into the handoff for a clean note. Nonrecoverable `dm_notes: none` matches remain dossier evidence only. Do not use a separate review agent: the same worker self-reviews while context is loaded. Reshard unfinished notes more narrowly; never write a partial batch.

After every shard is complete, finalize once from the review workspace. Omit `--write` for check-only; include it only for an authorized write lint:

```sh
# Check-only
ruby _scripts/lint_taelgar_notes.rb finalize --manifest /tmp/taelgar-lint-manifest.json --review-dir /tmp/taelgar-lint-review

# Authorized write lint
ruby _scripts/lint_taelgar_notes.rb finalize --write --manifest /tmp/taelgar-lint-manifest.json --review-dir /tmp/taelgar-lint-review
```

The finalizer is fail-closed and all-or-nothing. It requires every manifest path exactly once with completed self-review and matching `candidateSha256`; rejects schema/version/assignment errors, changed live targets or prior state, changed ineligible candidates, invalid verdict/outcome/report combinations, and new whitespace errors; and validates every candidate before writing any. It lazily adds the discussion route only to an already-Underdeveloped result. A write uses one timestamp and validator version, same-directory atomic replacements, verified hashes, and rollback on ordinary failure. Its generated `handoff` renders structured recoveries and expansion candidates; `reviewSummary` separates `mechanicalOnlyPaths` from `targetedReviewPaths` and classifies the changed risks for verification. Keep every manifest, workspace, result, and finalization JSON owner-only. `snapshot` is compatibility-only. Never bypass the finalizer.

## Perform one integrated contextual review

Use one evidence set rather than restarting discovery for each rule family. Apply the adopted specification and applicable additional authorities in this order:

1. Resolve every actual deterministic error, warning, and suggestion; informational output does not become open work.
2. Apply **Source authority and correctness**, **Freshness and later invention**, and **Coverage and suggestions** to the packet and any necessary bounded follow-up search.
3. Assign exactly one verdict under **Editorial sufficiency** and apply **Reference voice and stylistic judgment**. Do not consult the Worldbuilding discussion index before assigning the verdict.
4. Obey the packet's POV review gate and [[Temporal POV Metadata]]; visibility-changing `Date:*` changes remain proposal-only.
5. Apply **Privacy and DM metadata** and **Shared nonpublic content review**. Record private recoveries only in structured private fields, never in Git-shared report prose, and never change a human attestation automatically.
6. Apply the name, classification, campaign, map, persistent-metadata, and status rules. Preserve `status/check/name` as independent human-review state and never use it as evidence for name metadata; only the report lifecycle may change `status/check/lint`.

For a batch, populate every structured result field required by the workspace schema. The finalizer, not worker-authored handoff prose, converts those results into note changes and private user-facing output.

## Apply changes and completion state

Apply only changes allowed by the specification's **Safe fixes and proposals** section. Declare every automatic body edit and its objective basis, keep visibility-changing structures and human attestations proposal-only, and never change `headerVersion`.

Write the validator's exact quoted version and an offset-bearing timestamp only after the full review. Completion state is atomic: an open result has one complete replacement Lint report and `status/check/lint`; a clean result has neither and retains the supported completion and persistent metadata.

Every open `lintReport` must conform to the exact canonical structure in the specification's **Persistent lint state and report lifecycle** section. Before recording `candidateSha256`, verify the required title and headings, conditional sections, finding placement, and private-content boundary. For a clean result, leave `lintReport` empty and let the finalizer place any applied-change summary in the handoff.

## Verify and hand off

For a single note, re-read the complete result, inspect the complete diff, and run scoped `git diff --check`; the final validator is the deterministic proof.

For a batch, successful all-or-nothing finalization plus verified written hashes is the deterministic proof of YAML, links, tags, completion state, structured blocks, and file integrity. Do not rerun the validator, recheck clean/open invariants, compare the files with the finalized manifest, or repeat the workers' semantic review unless there is a mismatch or tool-reported anomaly. Use the finalizer's `reviewSummary` as the review router: verify that every `changedPath` is authorized; treat `mechanicalOnlyPaths` as mechanically proven without reading their routine timestamp, report-lifecycle, or frontmatter-formatting hunks; inspect the diff hunks only for `targetedReviewPaths`, prioritizing body prose, private or visibility-sensitive content, non-lint statuses, and custom syntax. Metadata and persistent-metadata changes need a bounded check of the changed values, not a second source review. Re-read an individual finalized note in full only when a targeted hunk lacks enough context, an anomaly appears, or the finalizer explicitly identifies body prose, private or visibility-sensitive content, or custom syntax whose safety cannot be judged from the hunk.

Run scoped `git diff --check` as a backstop; the finalizer should already have rejected newly introduced whitespace errors before writing. If a post-finalization correction is proven to remove only trailing horizontal whitespace and changes no non-whitespace bytes or line structure, it does not invalidate the finalized hashes' semantic or structural proof: do not refinalize, rerun note validators, or reread the note. Verify only that the correction is whitespace-only and that the scoped `git diff --check` now passes. Any other post-finalization edit restores the ordinary targeted verification appropriate to its `reviewSummary` category.

Use the finalizer's mechanically generated `handoff` as the basis of the chat handoff rather than rebuilding it from worker prose. Supplement it only with changed-path and validation facts from `reviewSummary`. It already renders open notes, bounded worth-expanding additions with sourced benefits and copy-paste-ready statements, every `_DM_` or `SECRET` recovery with destination and candidate, and exact `_DM_` links only when those links are not already in the finalized note. Omit nonrecoverable matches and leave DM-only contents from shared Git-tracked blocks under their ordinary rules unless the user separately requests them. Write an Underdeveloped assessment into its open Lint report; other sufficiency verdicts remain chat-only. If the skill or tooling changed, run its focused tests and the skill structural validator.
