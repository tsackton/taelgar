---
name: lint-taelgar-note
description: Lint, re-lint, or batch-lint eligible Taelgar vault notes with deterministic validation and source-grounded editorial judgment, then write or clear versioned lint state. Use when the user asks to lint, re-lint, batch-review, validate the completeness or currency of, or apply Taelgar lint metadata to one or more notes. Never lint notes under Worldbuilding or any dot or underscore directory; do not use for ordinary lore editing without a lint request.
---

# Lint Taelgar Note

Combine deterministic validation with one source-grounded contextual review. The adopted rules live in `../../../_MoC/Taelgar Note Linter.md`; do not reproduce or improvise a competing rule set.

## Isolate live guidance from lint history

- For ordinary lint, re-lint, batch, and check-only work, do not search, read, cite, or rely on Codex memories, rollout summaries, or prior-run guidance. The live skill, adopted specification, current validator, current governance files, and current vault evidence are the only procedural authorities.
- Consult historical linter material only when the user explicitly asks for history, rationale, maintenance, or regression analysis. Version-specific historical results never establish the current workflow or rule set.
- A task that changes `linterVersion` includes a mandatory read-only memory audit before handoff. Check whether active memory presents the superseded version as current or routes ordinary lint work to version-specific historical guidance. If correction is needed, tell the user and request the direct authorization required to submit a memory-update note; do not declare the version-update lifecycle complete without surfacing that step. Generated memory files are never edited directly.

## Gate the target and mode first

- Exclude any note with a `Worldbuilding`, dot-prefixed, or underscore-prefixed directory segment. Ineligible paths remain searchable evidence.
- An otherwise in-scope note is lintable when its authored body makes a substantive statement about its subject or source. The statement need not be grammatically complete when the title supplies the subject or an implied copula; definitional phrases, elliptical reference prose, and factual list entries qualify when they communicate a complete subject-matter assertion. Visible prose and authored comments or `SECRET`, `Campaign:*`, and `Date:*` blocks can count. Frontmatter, headings, embeds, isolated names, links, dates or labels, TODOs, editorial reminders, and lint-owned blocks cannot. The validator first excludes objectively blank, heading-only, embed-only, and linter-output-only bodies. Semantically exclude a surviving candidate only when it is clearly placeholder or nonassertive content; uncertainty after the mechanical screen favors inclusion. Collections omit confirmed ineligible notes and samples replace them.
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

For an authorized re-lint with a valid previous timestamp, add `--linted-at "PREVIOUS_TIMESTAMP"`. Require `validatorVersion` to equal the adopted `linterVersion`. Read and judge the complete note, perform the integrated review below, then apply only safe lint-owned changes. Use `--fix-frontmatter` only after the eligibility and preservation checks.

Write completion state as the final scoped edit. Run the validator again with link checks enabled; if it fails, restore the prior completion state. Never perform a version-only migration or carry an old report forward without re-evaluating it.

## Batch workflow

Use the batch wrapper for two or more notes; its `prepare` step replaces individual initial validator runs. Do not semantically pre-screen a large collection in the coordinator's context: preparation performs only the objective blank-stub screen, and editorial workers confirm semantic eligibility inside bounded shards.

```sh
ruby _scripts/lint_taelgar_notes.rb prepare --output /tmp/taelgar-lint-manifest.json "PATH/ONE.md" "PATH/TWO.md"
ruby _scripts/lint_taelgar_notes.rb workspace --manifest /tmp/taelgar-lint-manifest.json --review-dir /tmp/taelgar-lint-review
```

Use `--re-lint` only when explicitly authorized. Broad `--all-linted` and `--stale` selectors also require `--re-lint`; `--only-needs-review` may narrow that authorized maintenance scope. Inspect `selectionSummary`, including `skippedNoReviewableProse`, and confirm every included note is authorized and passed the objective candidate screen. Editorial workers determine semantic eligibility.

The workspace command sorts path-near notes together where practical and caps each shard at 10 notes or approximately 30,000 estimated input tokens, whichever comes first. A note above the token limit is a singleton shard. Change these operational defaults only when the actual packet sizes or task shape justify it.

The user-facing coordinator is the batch manager and should use `gpt-5.6-sol` with `xhigh` reasoning. Spawn one fresh-context `gpt-5.6-sol` `xhigh` editorial worker per available shard slot without inherited conversation turns. Give each worker the skill, adopted specification, assigned packet, staged candidates, and result path. Workers may search the full vault, but they edit only their staged copies and result file and return only completion plus that result path. Do not use a separate manager merely to page shards. An optional `gpt-5.6-terra` `high` helper may run preparation, sharding, schema and hash checks, completion tracking, and finalization, but it must not decide semantic eligibility, interpret evidence or privacy, assign an editorial verdict, select a finding, or write report language.

Each editorial worker reads every assigned note completely, uses its packet plus one integrated contextual evidence pass, and applies supported lint-owned changes only to the staged copy while preserving its old completion state, tag, and report. It sets semantic eligibility; for an eligible note it also sets exactly one editorial verdict, a clean or open outcome, a complete replacement `%%^Lint%%` block when open, structured shared-nonpublic dispositions, declared objective body edits, an explicit assessment when underdeveloped, and a structured expansion candidate when worth expanding. An ineligible result needs a concise reason and no staged change, verdict, outcome, report, handoff, or review payload. After the staged candidate and result are final, set `candidateSha256` in that result to the candidate's exact SHA-256; any later candidate mutation invalidates the result.

Route every semantic-ineligible result, every result containing `editorial.note_underdeveloped`, and every worker-flagged uncertainty to a second fresh `gpt-5.6-sol` `xhigh` review. Mark adjudication complete only after that review. If a worker cannot finish a shard, leave its results unresolved and reshard the unfinished notes more narrowly; do not write a partial batch.

After every shard is complete, finalize once from the review workspace:

```sh
ruby _scripts/lint_taelgar_notes.rb finalize --write --manifest /tmp/taelgar-lint-manifest.json --review-dir /tmp/taelgar-lint-review
```

The write command requires every manifest path exactly once, rejects duplicates, omissions, pending adjudication, mixed manifests or versions, changed live targets, staged candidates changed after their recorded SHA-256, altered prior completion state, changed ineligible candidates, invalid verdict/outcome/report combinations, and newly introduced whitespace errors. It validates every proposed note before writing any, uses one timestamp and validator version, writes same-directory replacements, verifies written hashes, and rolls back ordinary write or verification failures. Its `reviewSummary` classifies changed paths as `mechanicalOnlyPaths` or `targetedReviewPaths` and lists paths by change category: completion lifecycle, frontmatter formatting, other metadata, persistent metadata, body prose, private or visibility-sensitive content, non-lint statuses, and custom syntax. All file-based manifest, workspace, result, and finalization JSON is written with owner-only permissions because it can contain private evidence paths. A non-writing finalize remains available for check-only work and diagnosis. The legacy `snapshot` command remains compatibility-only; the adopted sharded workflow never edits live notes before finalization. Never bypass the finalizer.

## Perform one integrated contextual review

Use one evidence set to decide all applicable rule families rather than restarting the search for each:

1. **Deterministic findings:** resolve or carry forward every actual error, warning, and suggestion. Do not turn informational output into open work.
2. **Evidence and coverage:** search filenames, identity metadata, variants, links, backlinks, and relevant passages not already resolved by the packet. Follow vault source authority. Session notes and Primary Sources are records, not omniscient truth, and are not declared factually wrong. Worldbuilding is provisional. Distinguish internal conflict, external conflict, established missing information, and unestablished development opportunity. Report omitted established information only when its absence materially misleads or leaves the central account outdated; suggestions require specific evidence, a concrete improvement, and enough importance to retain lint status. When evidence already consulted for a finding or expansion candidate directly contradicts the target's visible prose or persistent metadata, convert that specific issue into an appropriate open finding; do not start another search or general review.
3. **Editorial sufficiency:** ask: **Does the visible note currently perform its reference role without a central gap?** If no, assign **Underdeveloped**. If yes and one bounded addition would materially improve it, assign **Sufficient, worth expanding**. Otherwise assign **Sufficient**. Underdevelopment requires a specific central missing dimension; “more could be written” is not enough. Independently inventory central gaps whose content is established elsewhere and central dimensions that remain uninvented. Use a coverage rule for the former and `editorial.note_underdeveloped` for the latter. A note may contain both when they describe different gaps; never duplicate the same gap under both. Do not stop the inventory after finding established missing facts. When a person's visible account gives only an origin or childhood while established evidence shows a materially different later identity or role, separately ask whether the transition is established. If how or why the important later role developed remains unknown and that transition is central to the person's reference account, report it as `editorial.note_underdeveloped`; do not treat the later endpoints as if they supply the missing transition. Reserve invention-based underdevelopment for subjects whose centrality is clear from setting or campaign role, important relationships or consequences, structural function, or a broad pattern of use and backlinks. Backlinks are one signal, never a score. A bounded minor note can be sufficient with little prose; when importance or centrality is unclear, do not issue invention-based underdevelopment. Several central placeholder sections strongly support **Underdeveloped**, while a peripheral unfinished section usually does not. Do not impose template headings or generic genre expectations. Every Underdeveloped report includes an explicit `### Editorial assessment` naming all central missing dimensions. **Sufficient, worth expanding** requires one structured, bounded addition with its practical benefit and named sources, evidence, and certainty. By itself, that verdict cannot create a Lint block, `status/check/lint`, or an editorial finding. Other findings are evaluated independently, and the note is open whenever any remain. Never use worth-expanding to hide an open conflict or shared-public-material finding.
4. **Freshness and temporal framing:** use Git and manifest evidence from the prior `lintedAt`. Later material change requires a human choice among updating the article and `POV`, deferring with the applicable game-update status, or preserving the earlier article. Never change a game-update tag during linting. Obey `deterministic.reviewGates.pov`: an existing `povNotes` block always makes review required, regardless of prior lint version, and the linter must retain that block. Removing an existing `povNotes` block is always a human-only decision. Only when `povNotes` is absent does the version gate apply; if `required` is then false, preserve both the valid existing `POV` and the absence of `povNotes`. Deterministic missing or malformed `POV` still requires resolution. When review is required, choose `POV` from the undated visible article frame under the adopted temporal rules and do not let a narrow dated event redefine the whole article. If no temporal information or material temporal constraint is established, a retained block may simply describe the note as broadly modern. Notes under `Campaigns/**` tagged `session-note`, `meta`, or `source` require `POV` and must not be given a new `povNotes` block; if such a note already has one, retain it and report the categorical mismatch for human review.
5. **Privacy:** disposition every substantive ordinary comment and `Campaign:none` block as `redundant_with_public`, `public_adoption_candidate`, `dm_only`, `speculative_or_unresolved`, `source_pointer`, or `no_useful_material`. A public adoption candidate requires open `editorial.public_material_candidate`; material redundant with visible prose requires open `editorial.shared_material_redundant`. Neither disposition can be clean or merely worth-expanding. Preserve the hidden text and propose human action; never promote or remove it automatically. Never copy or paraphrase `SECRET` or local `_DM_` content into a shared report. Use validator or manifest `_DM_` matches for the gated `dm_notes` review: matches do not invalidate `dm_notes: none`, and no match does not authorize clearing a positive human attestation.
6. **Names and metadata:** obey the independent name-review gate; do not redo a skipped pronunciation search. Preserve existing unresolved name entries and keep proposals out of frontmatter until accepted. An existing `status: documented` name entry remains documented and every populated documented value remains unchanged; supported missing fields may be added. If another note conflicts with a documented value, preserve it and open `metadata.names_documented_conflict` for human resolution. Follow deterministic candidates and the adopted references for classification, campaigns, maps, persistent-block placement, and actual pronunciation values.
7. **Statuses:** do not assess `status/check/*`. Disposition every other existing `status/*` as supported, questioned with evidence, or not assessable, without changing it. Only the report lifecycle may add or remove `status/check/lint`.

## Apply changes and completion state

Apply a change automatically only when exactly one lint-owned correction satisfies the adopted rules and preserves lore meaning, voice, cadence, uncertainty, attribution, temporal framing, and player/DM visibility. Safe cases include deterministic frontmatter normalization, versioned lint state, and an objective prose defect whose correction is unambiguous. Unusual, awkward, archaic, or stylistically marked phrasing is not itself defective. When phrasing materially impairs comprehension but correction requires judgment, preserve it and open `editorial.prose_clarity` with the exact passage, explanation, and a copy-ready candidate. Mere stylistic preference is not a finding. Declare every automatic body edit and its objective basis in the result. Propose rather than apply lore changes, competing interpretations, visibility-changing blocks, ambiguous conversions, human attestations, and non-lint status changes. Never change `headerVersion`.

Write the validator's exact quoted version and an offset-bearing timestamp only after the full review. Completion state is atomic:

- **Open:** one final `%%^Lint%%` block, `status/check/lint`, and at least one unchecked task with severity, stable rule ID, evidence, and a copy-ready candidate where applicable.
- **Clean:** no Lint block and no `status/check/lint`; retain the new completion pair and supported persistent metadata.

Reports contain only current open work. Preserve unresolved human decisions; do not keep checked tasks, empty reports, or tags justified only by information. Record applied changes in an open report or, for a clean lint, in the handoff.

## Verify and hand off

For a single note, re-read the complete result, inspect the complete diff, and run scoped `git diff --check`; the final validator is the deterministic proof.

For a batch, successful all-or-nothing finalization plus verified written hashes is the deterministic proof of YAML, links, tags, completion state, structured blocks, and file integrity. Do not rerun the validator, recheck clean/open invariants, compare the files with the finalized manifest, or repeat the workers' semantic review unless there is a mismatch or tool-reported anomaly. Use the finalizer's `reviewSummary` as the review router: verify that every `changedPath` is authorized; treat `mechanicalOnlyPaths` as mechanically proven without reading their routine timestamp, report-lifecycle, or frontmatter-formatting hunks; inspect the diff hunks only for `targetedReviewPaths`, prioritizing body prose, private or visibility-sensitive content, non-lint statuses, and custom syntax. Metadata and persistent-metadata changes need a bounded check of the changed values, not a second source review. Re-read an individual finalized note in full only when a targeted hunk lacks enough context, an anomaly appears, or the finalizer explicitly identifies body prose, private or visibility-sensitive content, or custom syntax whose safety cannot be judged from the hunk.

Run scoped `git diff --check` as a backstop; the finalizer should already have rejected newly introduced whitespace errors before writing. If a post-finalization correction is proven to remove only trailing horizontal whitespace and changes no non-whitespace bytes or line structure, it does not invalidate the finalized hashes' semantic or structural proof: do not refinalize, rerun note validators, or reread the note. Verify only that the correction is whitespace-only and that the scoped `git diff --check` now passes. Any other post-finalization edit restores the ordinary targeted verification appropriate to its `reviewSummary` category.

State each note's editorial sufficiency verdict in the chat handoff, along with which files changed, whether each result is clean or open, what human work remains, and what validation passed. For worth-expanding notes, render the structured addition concretely and name its source notes while preserving reported, assumed, provisional, or uninvented status. State shared-nonpublic dispositions without exposing DM-only content. Write an Underdeveloped assessment into its open Lint report; other sufficiency verdicts remain chat-only. If the skill or tooling changed, run its focused tests and the skill structural validator.
