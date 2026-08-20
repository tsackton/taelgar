---
tags: [meta, status/check/ai]
linterVersion: "3.0"
dmNotesReviewVersion: "3.0"
nameReviewVersion: "3.0"
name: Taelgar Note Linter
---
# Taelgar Note Linter

> [!info] Adopted specification
> This note defines version **3.0** of the Taelgar note linter. The operational skill is `.agents/skills/lint-taelgar-note/SKILL.md`; deterministic validation is implemented by `_scripts/validate_taelgar_note.rb`.

## Purpose

The Taelgar note linter is a context-aware, repeatable review of an individual note. It combines deterministic validation with source-grounded agentic judgment and answers a broader question than whether the note parses: what established information, metadata, editorial work, or human disposition is still missing from this note?

The linter does not compress that answer into a few frontmatter fields. It records durable verification state and, only when work remains, a shared nonpublic narrative report that a human can review and clear.

## Authority

This specification defines lint behavior and state. It operates alongside:

- [[Metadata Specification]] and [[Note Categorization]] for general note metadata;
- [[Campaign Registry]] and `_scripts/session_note_campaigns.json` for campaign identities and codes;
- [[Name Metadata]] for human-curated name blocks;
- [[Temporal POV Metadata]] for the searchable article viewpoint and `povNotes` interpretation;
- [[Note Status]] for the meanings and lifecycle semantics of `status/*` tags;
- `AGENTS.md` for editing authorization, source authority, and status-tag permissions;
- `.agents/skills/lint-taelgar-note/SKILL.md` for the executable agent workflow; and
- `_scripts/validate_taelgar_note.rb` for deterministic rules and safe frontmatter formatting.

When these disagree, do not silently choose one. Stop the write-mode lint, report the mismatch, and correct the specification, governance, skill, implementation, and tests together.

## Applicability

Any note whose path contains a directory segment named `Worldbuilding` or beginning with `.` or `_` is categorically outside the linter's target scope. This applies at every nesting depth, including `Campaigns/_generated/**` and `Campaigns/.chatgpt/**`. Do not write `lintedAt`, `lintVersion`, `status/check/lint`, or persistent lint metadata to these notes, and do not count them in lint samples.

Every other Markdown note is an eligible target; tag, note type, and other directory names do not create exclusions. Target eligibility does not filter evidence. All relevant vault Markdown notes—including notes under Worldbuilding and dot or underscore directories—remain searchable and citable while linting an eligible target. Their ordinary authority, privacy, and uncertainty still apply; Worldbuilding remains provisional rather than canonical merely because it is evidence.

## Versioning

The current adopted linter version is stored in this note's `linterVersion` field. The deterministic validator exposes the same value as `validatorVersion`.

Every completed write-mode lint records:

```yaml
lintedAt: "2026-08-19T11:40:58-04:00"
lintVersion: "3.0"
```

The linter must take `lintVersion` from the validator output for that run. It must not infer the version from the target note, copy an older value, or maintain a separate hard-coded skill version. If `linterVersion` and `validatorVersion` disagree, the lint fails and writes no new timestamp.

Increase the linter version when a change can alter applicability, severity, findings, safe-fix behavior, persistent lint state, or report interpretation. Editorial clarification that cannot change an outcome does not require a bump. Schema versions such as `Metadata:names:v1` and the validator's output `schemaVersion` are independent of the linter version.

`dmNotesReviewVersion` is an independent minimum prior linter version for the contextual `dm_notes` evidence review. A note whose valid `lintVersion` is at least this value treats its recorded `lintedAt` as the last DM-attestation validation unless a matching `_DM_` source has since been modified. Unrelated future linter-version increases do not re-trigger DM review. When the adopted DM-review rules change, set `dmNotesReviewVersion` to the new linter version so older attestations are reviewed once under the new rules. Compare dotted versions numerically rather than lexically.

`nameReviewVersion` is the independent minimum prior linter version for contextual name-block applicability and pronunciation review. A note with a valid `lintedAt` whose numeric `lintVersion` is at least this value skips that contextual review during later lints. Existing name blocks still receive deterministic schema validation, and entries marked `proposed`, `disputed`, or `unresolved` still produce deterministic human-review tasks without being recalculated. When name-review rules change, raise `nameReviewVersion`; a human who changes the primary subject of a note can force review by removing its lint completion version.

An older `lintVersion` remains an accurate record of the earlier check, but it makes the note a candidate for re-linting under the current rules.

### Re-linting stale versions

A stale version is any present `lintVersion` that differs from `validatorVersion`, including a legacy numeric value such as `2`. Staleness means that the previous result used an older rule set; it does not itself prove that the note has a substantive defect.

Before changing the note, preserve the previous `lintedAt`, `lintVersion`, `status/check/lint` state, and Lint block as historical input. If the old `lintedAt` is a valid timestamp, use it as the Git freshness baseline even when the version is stale. Then run every currently applicable deterministic and contextual rule from the current version. The contextual `dm_notes` and name reviews remain not applicable when their independent gates are satisfied. Do not perform a version-only migration or assume that an earlier clean result satisfies a newly applicable rule.

The prior Lint block and status are evidence, not findings to copy forward. Re-evaluate each old item against the current note and current sources, validate persistent metadata under current schemas, and build the final report only from findings that remain open under the current version. The initial `lint.version_outdated` finding is resolved by successful completion and does not by itself justify a new Lint block.

If the old timestamp is absent or invalid, there is no trusted freshness baseline. Perform the full current lint and search all relevant source history without claiming that the search is bounded to changes since a verified lint.

Complete the source review and validate all content other than completion state first, treating `lint.version_outdated` as the expected transitional finding. Then apply the new timestamp, current `validatorVersion`, replacement report, and tag state as one final scoped edit and validate the resulting note. If the re-lint is interrupted before that edit, leave the old state untouched. If final validation fails afterward, restore the old completion state and report the failure; never leave a new version or timestamp on an incomplete lint. Open current work gets a replacement report and `status/check/lint`; a clean result gets neither.

## Modes and authorization

The linter has two note-level modes:

- **Check-only:** inspect and report in chat without editing the note or advancing `lintedAt`.
- **Write lint:** perform the complete review, apply only authorized lint-owned changes, and record final lint state.

A request to lint or re-lint a named note authorizes lint-owned changes: deterministic frontmatter normalization, supported persistent metadata, unambiguous meta-comment placement, approved high-confidence light editorial fixes, and lint state. Broader prose rewriting, speculative lore development, or multi-note cleanup still requires its own scope and approval.

The deterministic formatter may be run in safe-fix mode only when it can preserve parsed values, comments, meaningful quoting, unknown fields, and special syntax. Editorial fixes are opt-in and limited to high-confidence typos, punctuation, duplicated words, and very light clarity problems. They never decide names, dates, classifications, lore, uncertainty, private material, or conflicts.

## Core principles

1. **Expectations come before judgment.** Apply explicit, reviewable expectations rather than inventing a new standard for each note.
2. **Expectations are contextual.** Entity type, temporal point of view, structural role, and importance affect what completeness means.
3. **Deterministic and agentic findings remain distinguishable.** A malformed field is different from an evidence-backed coverage gap or editorial suggestion.
4. **Correctness, coverage, and invention are different.** Missing established information is not the same as an opportunity to invent more.
5. **Non-check status tags require disposition.** A completed lint assesses every existing `status/*` tag outside `status/check/*`; human-review check tags are preserved without semantic assessment.
6. **Privacy concepts remain separate.** Campaign knowledge, player audience, page publication, private material, DM ownership, and off-vault information are not interchangeable.
7. **The report exists only for open work.** Persistent temporal metadata survives; the replaceable Lint block does not survive a clean lint.
8. **Freshness is external.** Clean-preserving edits to the target do not invalidate a lint; later invention elsewhere in the vault can.
9. **Automation preserves meaning and visibility.** Apply a change only when one lint-owned correction preserves meaning, uncertainty, attribution, temporal framing, and audience visibility; otherwise propose it.

## Expectation profile

For eligible notes, the linter derives a profile from the note's tags, classification, content, structure, and role. Folder placement alone is insufficient except for the categorical target exclusions for Worldbuilding and dot or underscore directories at any depth.

### Subject or document type

Applicable profiles include people, places and more specific place types, groups, organizations, powers, creatures, objects, events, ancestries, backgrounds, primary sources, session notes, campaign documents, and meta material. People use `species`; non-people use documented `typeOf` values where classification is required.

### Temporal point of view

Every completed contextual lint identifies the article's speaking position, then judges whether the prose is suitable for that point of view. Temporal review is not a generic requirement to date every fact. It distinguishes lifecycle dates, dated relationships, date blocks, current reference prose, historical snapshots, bounded event accounts, campaign-relative language, and layered primary-source viewpoints.

The completed lint records the searchable scalar viewpoint in frontmatter `POV` and the practical interpretation as plain text in the persistent `%%^povNotes:v1%%` block, following [[Temporal POV Metadata]]. `POV` is the article's best single temporal reading position, not its validity interval or the span between its oldest and newest facts. Test the ordinary values in order: use `modern` when the current DR 1700s campaign era is precise enough; otherwise use a decade when a rough campaign era or life stage is precise enough; otherwise use a year for a narrower supported snapshot. Use `undated` only when all three tests fail because the note and its sources support no temporal reading position. `undated` records missing temporal support, not timeless truth or stability, and does not excuse incompatible undated states. Century values, named eras, and `timeless` are legacy choices to reconsider contextually on re-lint.

Choose `POV` from the undated visible frame. Historical backstory does not widen the viewpoint, and an isolated dated paragraph does not narrow it. `povNotes` begins with `Temporal coverage:` and concisely records the article's actual shape: broad or approximately bounded coverage, a narrow snapshot, one-sided uncertainty, or discontinuous periods with gaps. Name event boundaries when established, distinguish unknown periods from contradicted states, and never invent an exact cutoff or infer continuity between separated facts. Before choosing a narrow POV, propose the smallest useful `Date:*` blocks for supported later facts or state changes; do not apply a new block without approval because it can change filtered visibility.

Later truth does not by itself make an explicitly earlier-POV note incorrect, but a later fact that would materially change the article still requires the human coverage, POV, and game-update disposition below. A defect exists when the note silently mixes incompatible viewpoints, uses unanchored changing language, exposes later knowledge in an earlier view, or applies campaign/date blocks inconsistently.

### Structural role and importance

A bounded glossary entry, connector, overview, hub, minor subject, and major campaign subject do not have the same coverage expectations. Importance informs contextual judgment but never becomes a generic word-count or heading requirement.

## Source authority and correctness

Search likely canonical sources first, then campaign and session records, Primary Sources, Worldbuilding, shared DM material, local `_DM_` material, and other relevant vault notes as applicable. Target-ineligible paths remain evidence paths. Read the surrounding passage and preserve uncertainty and source distinctions.

Session notes and Primary Sources are fundamental source records. The linter may flag malformed metadata, damaged syntax, attribution problems, internal ambiguity, or usability issues, but it never declares the source note itself factually wrong because another note disagrees. Downstream reference notes must represent or reconcile what the source establishes.

Worldbuilding notes are explicitly provisional evidence and are never lint targets. When they inform a lint elsewhere, a proposal's non-adoption or divergence from later canon is not itself evidence that the eligible target is wrong.

Distinguish:

- **internal conflict:** passages or metadata inside the target disagree; and
- **cross-note conflict:** the target disagrees with an external source after authority, date, and context are evaluated.

An editorial comment questioning visible prose is not independent evidence of a cross-note conflict.

## Freshness and later invention

Git history is the freshness boundary; no separate corpus snapshot is required. Starting from the previous `lintedAt`, the deterministic pass nominates newer external sources that link or otherwise resolve to the target. Prioritize session and campaign notes, finalized `beat-facts.json`, `_DM_`, and `_dm_notes`, while retaining authority labels for ordinary reference and Worldbuilding sources.

A newer mention is only a candidate. The contextual pass decides whether it changes, supplements, contradicts, or does not affect the target. Plain-text resolution must be conservative for short or common names. Generated derivatives and binary assets are not invention-bearing sources.

Editing the target note does not itself invalidate a clean lint. The relevant question is whether invention elsewhere in the vault has overtaken what the article represents.

## Coverage and suggestions

For every potentially missing fact or event, first determine whether an appropriate vault source establishes it. Unestablished information is a development opportunity rather than an incorrectness or coverage finding. Provisional material may motivate future invention but does not establish a missing fact.

Established information is a `coverage.established_fact_missing` warning when omitting it would materially mislead the reader about the subject, its state, a major relationship, or the article's central account, or would leave the article materially outdated. Materiality is not inferred from note length, backlink count, or the mere existence of additional detail. Established information that is not materially required may support a suggestion under the threshold below; otherwise its omission is not a finding.

An established fact or event that would materially change the article must be reported as `coverage.later_material_change` even when it occurs after the recorded `POV`. The linter records a human decision rather than silently treating the information as outside scope: update the article and `POV`; defer the update and add or retain the appropriate `status/gameupdate/*` tag; or intentionally preserve the earlier article and `POV`, in which case the applicable game-update tag can be removed. The linter does not choose among these outcomes or alter game-update tags.

An editorial suggestion must be grounded in a named source, exact passage, metadata problem, or other specific evidence; name the affected note or notes; propose a concrete addition, correction, or bounded human choice; explain the practical improvement; and be important enough to justify retaining `status/check/lint`. Evidence and resolution may cross note boundaries. Concise evidence-backed additions to stubs are valid suggestions when they improve usefulness; brevity alone is not a defect. Vague prompts to expand, add detail, or improve context are not findings. A lesser observation may be reported informationally when useful, but it does not retain a Lint block or lint status.

## Status disposition

`status/check/*` tags record human-review state and are never semantically assessed by the linter. Preserve them without a supported, questioned, or not-assessable disposition and never recreate a check tag that a human removed. `status/check/lint` remains mechanically governed by the Lint report lifecycle and deterministic report/tag consistency, but it is not evidence about the note and receives no semantic assessment.

For every existing `status/*` tag outside `status/check/*`, record one disposition without altering the tag:

- **supported:** the note and appropriate vault evidence support the documented status; no open finding is required;
- **questioned:** concrete evidence suggests the tag no longer describes the note; report `status.questioned` as a warning with a bounded human choice; or
- **not assessable:** the tag depends on human intent, provenance, unfinished plans, or unavailable evidence; preserve it without creating an open finding solely for that uncertainty.

Judge `status/stub` by whether the note still lacks useful detail, not by word count. Judge `status/gameupdate/*` against established intervening game events and the article's recorded temporal framing. When the coverage rule leaves a human choice between updating, deferring, or preserving an earlier `POV`, the game-update tag is not assessable until that choice is made. Apply the same rubric to other non-check statuses using [[Note Status]]. Never add, remove, replace, or normalize any status tag except `status/check/lint` through its authorized lifecycle.

## Safe fixes and proposals

When no more specific rule controls the action, apply a change automatically only if exactly one correction satisfies the adopted rules, the operation is lint-owned, and it preserves lore meaning, uncertainty, attribution, temporal framing, and player/DM visibility. Supported descriptive metadata may be applied when it records one unambiguous interpretation of the existing note rather than changing that interpretation. If multiple reasonable corrections exist, a human decision remains, or meaning or visibility could change, provide a copy-ready proposal instead.

Canonical frontmatter ordering and formatting, versioned lint-state replacement, unambiguous one-to-one legacy-syntax conversion, and exact movement of an unambiguously misplaced header comment are ordinary automatic cases. Prose or lore changes, competing classifications or metadata interpretations, new or moved `Date:*`, `Campaign:*`, or secret blocks that can change filtered visibility, ambiguous comment moves or map conversions, and all changes to human attestations or non-lint status tags are proposal-only.

## Adopted metadata and structural checks

### Frontmatter

Version 3.0 uses this canonical ordering:

1. deprecated or obsolete fields, retained conspicuously for human migration;
2. `headerVersion`, `lintedAt`, `lintVersion`, `displayDefaults`;
3. `tags`, `typeOf`, `typeOfAlias` or person equivalents, and `ancestry`;
4. unclassified fields in stable original order;
5. `name`, `aliases`, `pronunciation`;
6. `affiliations`, `whereabouts`; and
7. `knownTo`, `excludePublish`, `audience`, `dm_owner`, `dm_notes`; and
8. `POV`, immediately after `dm_notes` and therefore last in frontmatter.

String-only lists and dictionaries use one line. Lists of dictionaries are expanded with one single-line dictionary per list item. The formatter never changes `headerVersion`, silently deletes a deprecated field, or rewrites unsafe YAML. Every deprecated-field finding proposes a plausible replacement or a bounded human choice.

### Naming and pronunciation

Perform contextual name review when the note has no valid `lintedAt`/`lintVersion` pair or its prior version is numerically lower than `nameReviewVersion`. A valid prior version at or above the threshold suppresses both missing-block applicability review and pronunciation search or derivation. The gate never suppresses deterministic validation of an existing block. A `proposed`, `disputed`, or `unresolved` entry remains an open deterministic human-review task; preserve it without recalculating the entry.

When review applies, first decide semantically whether the note's primary subject is a named in-world thing or in-world work. Notes about people, places, objects, groups, events, powers, creatures, ancestries or cultures, religions, primary-source works, and other named in-world subjects use `Metadata:names:v1` as documented in [[Name Metadata]]. A meta or background page that merely organizes, analyzes, or summarizes in-world material does not. Tag, folder, and title do not decide applicability.

For an applicable note, write a minimal primary entry with the exact subject name and its established language, or `language: unknown`; add other forms only when documented and never invent etymology. When creating a missing entry, if frontmatter has an actual pronunciation, treat the note itself as the source and record the matching entry as `status: documented` without requiring a source note. Otherwise use an explicit recorded pronunciation when found, mark it `documented`, and cite its source in `notes`. If the complete name is a genuinely obvious ordinary name or plain-English title, omit pronunciation. Otherwise derive the strongest supported proposal and store it with `status: proposed`, with its source or derivation in `notes`, until human acceptance. Preserve an existing unresolved entry rather than recalculating it; that rule takes precedence over the creation rule.

Use adopted language rules before cultural patterns or a real-world analogue in [[Languages]], and a cautious spelling-based reading only when no stronger basis exists. Missing exact in-world phonology leaves an analogue-derived result proposed. Every pronunciation must be pronounceable; exemptions use absence rather than sentinel text. Whenever a name-block entry has a pronunciation and frontmatter either has no pronunciation or has a different one, its `notes` must record the block value's source or derivation. A matching frontmatter pronunciation needs no source note. Never overwrite accepted frontmatter or recalculate an unresolved block entry automatically.

### Campaign knowledge and identity

`knownTo` is required for people and objects; `[]` explicitly records that no campaign knowledge is known. It is optional for other subjects. `campaignInfo` on a person or object normally implies the matching `knownTo` code.

`campaign` frontmatter applies only to session notes, campaign-specific meta notes, and campaign source material. It uses the registry's canonical long name. `knownTo`, `campaignInfo`, and `Campaign:*` blocks use lowercase short codes. Campaign directory placement does not make `campaign` appropriate for an in-world entity.

Positive campaign lists in `audience` are not yet a universal requirement. A session backlink proves that the subject appeared, not that every character knows every fact in the note.

### Privacy and DM metadata

The linter distinguishes three private in-note forms:

- `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%` is local-only material excluded from GitHub;
- ordinary `%% ... %%` comments are Git-shared, nonpublic DM or editorial material; and
- `Campaign:none` blocks are structured Git-shared DM material excluded from Taelgarverse.

`dm_notes` is a human attestation that relevant information exists outside Git-tracked material or in someone's head. Shared comments or blocks do not imply it. Basic vocabulary validation always applies, but the contextual evidence review has an independent validation boundary. For `dm_owner: tim`, `joint`, or `none`, perform that review when any of the following is true:

- the note has no valid `lintedAt`/`lintVersion` pair;
- its prior `lintVersion` is numerically lower than `dmNotesReviewVersion`; or
- an `_DM_` Markdown note that directly links or uniquely matches the subject has a filesystem modification time later than `lintedAt`.

If none applies, do not re-check or report on the `dm_notes` attestation during that lint. If a newer matching source triggers review, evaluate the complete current match set, not only the new source. A newer nonmatching `_DM_` file does not trigger review.

When review applies, use these four outcomes:

- `dm_notes: none` with no matches is valid and produces no finding.
- `dm_notes: none` with matches produces an informational “Did you check these notes?” list. Candidate presence alone is not a suggestion to change the human attestation.
- `dm_notes: color` or `important` with no matches produces the suggestion “No `_DM_` notes found; verify `dm_notes`.” The field may represent information in someone's head or another off-vault source and must never be removed automatically.
- `dm_notes: color` or `important` with matches produces an informational reference list. The linter does not adjudicate between the two positive values.

Report matching Markdown notes as Obsidian wikilinks without exposing content. The presence or contents of `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%`, ordinary comments, and `Campaign:none` blocks in the target never trigger, suppress, support, or otherwise affect the candidate-based `dm_notes` review; they are separate privacy mechanisms. In-note secret material remains compatible with `dm_notes: none` under [[Note Status]].

### Links and relationship metadata

Obsidian resolves a bare wikilink target from filenames, not from frontmatter `name` or `aliases`. Link validation therefore treats `[[Drankor]]` as a link to a file named `Drankor.md`; an alias on another file does not make that link ambiguous. Explicit paths disambiguate genuine duplicate filenames. Markdown notes inside dot-prefixed directories are not link or relationship targets and do not create filename, name, or alias collisions, although they remain searchable and citable evidence.

Metadata relationship resolution is a separate system and may use the vault's name and alias conventions. `whereabouts.location` also permits descriptive free text such as `traveling east to Tokra`. A value that does not resolve to a note is not by itself malformed and does not produce an unresolved-relationship finding. The contextual pass may still report a demonstrated typo, contradiction, or misleading location, but it must not replace an existing supported entry with an identical duplicate.

### Map metadata

`Metadata:map:v1` is required for waterways, roads, and settlements and optional for other places. The supported model has only single-hex locations and two-ended features. Every location entry has `map` and `locator`; it may also have `role` or `feature`. `geometry`, `hex`, `sourceHex`, and `outletHex` are not part of the model. On re-lint, redundant `geometry` is removed and legacy position keys are converted to equivalent `locator` entries when that can be done without guessing.

When positions are unknown, the linter writes the appropriate location entries and leaves their `locator` values blank; it never writes `status: missing` with `locations: []`. A blank locator remains an open `metadata.map_location_missing` finding until a human supplies it. A blank optional `feature` is not a finding. Existing empty placeholders are replaced with the typed form on re-lint. A coordinate in `13.07.F16` form always uses `map: world`. Coordinates remain strings.

Waterways have two directionally meaningful entries:

```yaml
locations:
  - {role: source, feature: , map: world, locator: }
  - {role: outlet, feature: , map: world, locator: }
```

Roads have two unordered endpoints. They do not use `start` and `end` roles because either direction would be arbitrary; `feature` can optionally name a city or other feature at each endpoint:

```yaml
locations:
  - {feature: , map: world, locator: }
  - {feature: , map: world, locator: }
```

Settlements and other single-hex features have one entry:

```yaml
locations:
  - {map: world, locator: }
```

### POV metadata and comment placement

The searchable viewpoint lives at the end of frontmatter:

```yaml
POV: 1750
```

The persistent temporal interpretation lives at the end of the note after prose and comments:

```markdown
%%^povNotes:v1%%
Temporal coverage: approximately DR 1748–1752; the present-tense geography is continuous across that interval, while older history does not change the article's speaking point.
%%^End%%
```

`POV` and `povNotes` describe the article rather than the lint run and remain after review. A completed lint requires frontmatter `POV` and one nonempty `povNotes:v1` text block. `mode` has no adopted semantics and is not retained. The old inline `(POV:: ...)` annotation and `Metadata:article` block are deprecated. Every full re-lint independently reassesses both `POV` and `povNotes` against the current note and applicable evidence. The legacy block's `povNotes` value is evidence whose meaning must not be lost, not accepted final output: retain it unchanged only when the contextual review confirms that it remains accurate; otherwise rewrite it. Move any useful legacy `pov` meaning into frontmatter or the explanation, and discard `mode`, `profile`, and other obsolete article-block keys.

Comments belong below the complete header block: the title and any immediately following information/header callout. The linter moves only an unambiguously misplaced comment while preserving its text exactly; uncertain rearrangements become suggestions.

## Findings and rule model

Every rule has a stable identifier, applicability condition, rule class, default severity, deterministic or agentic method, evidence requirement, not-applicable path where relevant, and safe-fix status.

Rule classes are `required`, `conditional`, `recommended`, and `judgment`. Open severities are:

- **error:** invalid structure, broken invariant, strong factual conflict, or clear privacy/publication failure;
- **warning:** likely missing information, unresolved continuity, questionable status, or an unmet conditional expectation; and
- **suggestion:** a non-required improvement in presentation, metadata, or development.

Development opportunity is distinct from a defect. A coverage gap means relevant established information belongs in the note; a development opportunity means the information has not yet been invented. The latter is never an incorrectness finding.

## Persistent lint state and report lifecycle

`lintedAt` records completion of the full write-mode lint. `lintVersion` records the exact validator version used. Together with `status/check/lint`, they distinguish unlinted, outdated-version, clean, and unresolved notes.

If any error, warning, or suggestion remains open:

- write exactly one `%%^Lint%%` block after all persistent metadata;
- add or retain `status/check/lint`;
- include at least one unchecked Markdown task with severity, stable rule ID, evidence, and a copy-ready candidate where applicable;
- distinguish automatic changes, informational observations, validated judgments, status dispositions, and open work; and
- replace the previous report rather than accumulating reports.

If no error, warning, or suggestion remains open:

- write no Lint block;
- remove any previous Lint block and remove only `status/check/lint`;
- retain the new `lintedAt`, `lintVersion`, and supported persistent metadata; and
- do not retain checked tasks, an empty “no findings” report, or a tag justified only by informational observations.

A check-only lint changes nothing and records no new timestamp. If evidence gathering or validation is incomplete, the lint fails and records no completion state.

## Workflow

1. Read the complete target and preserve unrelated worktree changes.
2. Read the applicable governance and metadata references.
3. Run deterministic validation and capture `validatorVersion`.
4. Derive the contextual expectation profile.
5. Resolve names, aliases, links, backlinks, relationships, campaigns, and relevant dates.
6. Gather sources according to authority, including newer invention after the prior lint.
7. Perform agentic review for correctness, coverage, editorial quality, status disposition, and development opportunity.
8. Apply only authorized lint-owned changes and write supported persistent metadata.
9. Re-run deterministic validation with links enabled and confirm the specification and validator versions agree.
10. Write `lintedAt`, the captured `lintVersion`, and either the open report/tag or the clean state.
11. Re-read the complete note, validate YAML and structured blocks, inspect the full diff, and report the result in chat.

### Batch execution

`_scripts/lint_taelgar_notes.rb` is the adopted batch wrapper around the same versioned rules. It is an operational optimization of linter 3.0, not a different rule set: it does not change applicability, severity, persistent state, or report interpretation and therefore does not itself require a linter-version increase.

Automatic batch discovery excludes every note with any `Worldbuilding`, dot-prefixed, or underscore-prefixed directory segment. Explicit preparation rejects such targets, and snapshot/finalization reject any manifest that contains one, including a manifest created under an older rule set. These exclusions never filter the evidence index or source search.

Batch preparation builds the vault link/identity index once and scans `_DM_` once for all targets. For each note, its preferred freshness baseline is the first Git commit containing the prior `lintedAt` and `lintVersion`. The tag and report are deliberately excluded from baseline identity because a human can clear them without changing the verification boundary. This prevents either that normal clear or a delayed commit of the completed lint from making the lint commit itself appear to be later invention. If the completion pair has not yet been committed, the fallback is the last commit at or before `lintedAt`. Freshness work is grouped by the resulting Git commit; within a shared baseline the batch reuses the changed-path list, per-source diff, line counts, and last-commit evidence. New untracked invention sources are included when their filesystem modification time is later than `lintedAt`. Because local-only `_DM_` files are outside Git, the shared DM scan records each matching file's modification time directly; this evidence both gates contextual DM review and routes a current note when a matching private source is newer than `lintedAt`. Every note still receives its own deterministic report, prior completion state, freshness candidates, checksum, and agentic review.

Batch selection resolves scope before routing:

1. The user's named files, folders, collection, or sample are the maximum scope; selection flags never broaden it.
2. Remove target-ineligible paths.
3. A plain `lint` request excludes every note with a valid prior `lintedAt`/`lintVersion` pair. Stale versions, open findings, deterministic errors, or newer evidence do not override this default.
4. Only explicit language such as `re-lint`, `lint again`, or `refresh the lint` authorizes including previously linted notes, and only within the target that language modifies. Mixed scopes are prepared separately.

The batch CLI enforces this boundary: named targets are filtered by default, `--re-lint` includes valid prior lint state, and `--all-linted` or `--stale` require `--re-lint`. Within an explicitly authorized re-lint scope, routing follows the adopted invalidation model:

- an unlinted note requires review;
- a stale `lintVersion` requires a complete current-version review using the old timestamp as its freshness baseline when valid;
- a current note with a newer external source that mentions it requires judgment about whether invention elsewhere has overtaken the article; and
- a current note with no newer invention candidate is eligible for a no-op and is not edited merely to refresh its timestamp.

Routing is triage after selection, never authorization to re-lint. If the user specifically asks to re-lint a named note, review it completely even when routing would permit a no-op.

Batch writes have three phases:

1. **Prepare:** produce a read-only manifest and gather shared deterministic, DM, and Git evidence.
2. **Review and snapshot:** read and judge each included note, apply any supported persistent changes while preserving its old lint completion state, then snapshot the reviewed file checksum.
3. **Finalize:** require one clean or open decision per manifest note; verify the manifest, reviewed checksum, and preserved old completion state; construct every proposed final note; and deterministically validate all of them before writing any completion state.

The finalizer writes the current validator version and one offset-bearing completion timestamp, removes or replaces the old report, and clears or sets only `status/check/lint` according to the decision. It stages same-directory replacements so each file replacement is atomic and rolls back ordinary write failures after a complete preflight. A checksum or state mismatch aborts the whole batch; it must never be bypassed by manually advancing the affected notes.

## Deferred design areas

The following remain deliberately unsettled and are not universal lint requirements:

- positive campaign semantics for `audience`;
- a replacement for long historical `whereabouts` lists;
- a registry and location model for regional maps beyond the supported single-hex and two-end cases;
- whether significant shared DM material needs an authored frontmatter field;
- a queryable development-priority scale; and
- bounded relationship propagation beyond direct freshness links.

Changes in these areas require an explicit design decision and, when they alter lint outcomes, a linter version bump.
