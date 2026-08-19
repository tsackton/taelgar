---
linterVersion: "2.3"
name: Taelgar Note Linter
---
# Taelgar Note Linter

> [!info] Adopted specification
> This note defines version **2.3** of the Taelgar note linter. The operational skill is `.agents/skills/lint-taelgar-note/SKILL.md`; deterministic validation is implemented by `_scripts/validate_taelgar_note.rb`.

## Purpose

The Taelgar note linter is a context-aware, repeatable review of an individual note. It combines deterministic validation with source-grounded agentic judgment and answers a broader question than whether the note parses: what established information, metadata, editorial work, or human disposition is still missing from this note?

The linter does not compress that answer into a few frontmatter fields. It records durable verification state and, only when work remains, a shared nonpublic narrative report that a human can review and clear.

## Authority

This specification defines lint behavior and state. It operates alongside:

- [[Metadata Specification]] and [[Note Categorization]] for general note metadata;
- [[Campaign Registry]] and `_scripts/session_note_campaigns.json` for campaign identities and codes;
- [[Name Metadata]] for human-curated name blocks;
- [[Temporal POV Metadata]] for the searchable article viewpoint and `povNotes` interpretation;
- `AGENTS.md` for editing authorization, source authority, and status-tag permissions;
- `.agents/skills/lint-taelgar-note/SKILL.md` for the executable agent workflow; and
- `_scripts/validate_taelgar_note.rb` for deterministic rules and safe frontmatter formatting.

When these disagree, do not silently choose one. Stop the write-mode lint, report the mismatch, and correct the specification, governance, skill, implementation, and tests together.

## Versioning

The current adopted linter version is stored in this note's `linterVersion` field. The deterministic validator exposes the same value as `validatorVersion`.

Every completed write-mode lint records:

```yaml
lintedAt: "2026-08-19T11:40:58-04:00"
lintVersion: "2.3"
```

The linter must take `lintVersion` from the validator output for that run. It must not infer the version from the target note, copy an older value, or maintain a separate hard-coded skill version. If `linterVersion` and `validatorVersion` disagree, the lint fails and writes no new timestamp.

Increase the linter version when a change can alter applicability, severity, findings, safe-fix behavior, persistent lint state, or report interpretation. Editorial clarification that cannot change an outcome does not require a bump. Schema versions such as `Metadata:names:v1` and the validator's output `schemaVersion` are independent of the linter version.

An older `lintVersion` remains an accurate record of the earlier check, but it makes the note a candidate for re-linting under the current rules.

### Re-linting stale versions

A stale version is any present `lintVersion` that differs from `validatorVersion`, including a legacy numeric value such as `2`. Staleness means that the previous result used an older rule set; it does not itself prove that the note has a substantive defect.

Before changing the note, preserve the previous `lintedAt`, `lintVersion`, `status/check/lint` state, and Lint block as historical input. If the old `lintedAt` is a valid timestamp, use it as the Git freshness baseline even when the version is stale. Then run every deterministic and contextual rule from the current version. Do not perform a version-only migration or assume that an earlier clean result satisfies a newly applicable rule.

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
2. **Expectations are contextual.** Entity type, article mode, temporal point of view, structural role, and importance affect what completeness means.
3. **Deterministic and agentic findings remain distinguishable.** A malformed field is different from an evidence-backed coverage gap or editorial suggestion.
4. **Correctness, coverage, and invention are different.** Missing established information is not the same as an opportunity to invent more.
5. **Status tags require disposition.** A completed lint validates or questions every existing `status/*` tag.
6. **Privacy concepts remain separate.** Campaign knowledge, player audience, page publication, private material, DM ownership, and off-vault information are not interchangeable.
7. **The report exists only for open work.** Persistent article metadata survives; the replaceable Lint block does not survive a clean lint.
8. **Freshness is external.** Clean-preserving edits to the target do not invalidate a lint; later invention elsewhere in the vault can.
9. **Automation preserves meaning.** Safe normalization must not strengthen certainty, resolve ambiguity, or damage special syntax.

## Expectation profile

The linter derives a profile from the note's tags, classification, content, structure, and role. Folder placement alone is insufficient.

### Subject or document type

Applicable profiles include people, places and more specific place types, groups, organizations, powers, creatures, objects, events, ancestries, backgrounds, primary sources, session notes, campaign documents, and meta material. People use `species`; non-people use documented `typeOf` values where classification is required.

### Article mode and temporal point of view

Every completed contextual lint identifies the article's mode and speaking position, then judges whether the prose is suitable for that point of view. Temporal review is not a generic requirement to date every fact. It distinguishes lifecycle dates, dated relationships, date blocks, current reference prose, historical snapshots, bounded event accounts, campaign-relative language, and layered primary-source viewpoints.

The completed lint records the searchable scalar viewpoint in frontmatter `POV` and the practical interpretation in the persistent article block's `povNotes`, following [[Temporal POV Metadata]]. Use the broadest honest value: a year, decade, century, named era, or `timeless`. A year is approximate rather than an exact validity boundary. `povNotes` may record an approximate, asymmetric, or minimal accuracy range and should distinguish unknown periods from established later developments.

Later truth does not make an explicitly earlier-POV note incorrect. A defect exists when the note silently mixes incompatible viewpoints, uses unanchored changing language, exposes later knowledge in an earlier view, or applies campaign/date blocks inconsistently.

### Structural role and importance

A bounded glossary entry, connector, overview, hub, minor subject, and major campaign subject do not have the same coverage expectations. Importance informs contextual judgment but never becomes a generic word-count or heading requirement.

## Source authority and correctness

Search likely canonical sources first, then campaign and session records, Primary Sources, Worldbuilding, shared DM material, and local `_DM_` material as applicable. Read the surrounding passage and preserve uncertainty and source distinctions.

Session notes and Primary Sources are fundamental source records. The linter may flag malformed metadata, damaged syntax, attribution problems, internal ambiguity, or usability issues, but it never declares the source note itself factually wrong because another note disagrees. Downstream reference notes must represent or reconcile what the source establishes.

Worldbuilding notes are explicitly provisional. The linter may report internal inconsistency, divergence from current canon, or unclear development status, but it never issues an incorrectness finding merely because a proposal was not adopted or later canon differs.

Distinguish:

- **internal conflict:** passages or metadata inside the target disagree; and
- **cross-note conflict:** the target disagrees with an external source after authority, date, and context are evaluated.

An editorial comment questioning visible prose is not independent evidence of a cross-note conflict.

## Freshness and later invention

Git history is the freshness boundary; no separate corpus snapshot is required. Starting from the previous `lintedAt`, the deterministic pass nominates newer external sources that link or otherwise resolve to the target. Prioritize session and campaign notes, finalized `beat-facts.json`, `_DM_`, and `_dm_notes`, while retaining authority labels for ordinary reference and Worldbuilding sources.

A newer mention is only a candidate. The contextual pass decides whether it changes, supplements, contradicts, or does not affect the target. Plain-text resolution must be conservative for short or common names. Generated derivatives and binary assets are not invention-bearing sources.

Editing the target note does not itself invalidate a clean lint. The relevant question is whether invention elsewhere in the vault has overtaken what the article represents.

## Adopted metadata and structural checks

### Frontmatter

Version 2.3 uses this canonical ordering:

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

Pronunciation is required for named in-world subjects unless contextual judgment records a plain-English title, meta note, genuinely obvious ordinary name, or inherited compound-name exception. A proposal must explain its language, derivation, and uncertainty and remains noncanonical until accepted. When [[Languages]] documents a real-world analogue, the linter must use that analogue to generate and explain a natural pronunciation or adaptation of the spelling. Missing exact in-world phonology makes the result proposed rather than documented; it does not justify an English-default reading.

Human-curated subject-specific naming data uses `Metadata:names:v1` as documented in [[Name Metadata]]. The linter validates but does not overwrite accepted name data or invent etymology to fill a block. `unknown` is a valid language value when no stronger evidence exists.

### Campaign knowledge and identity

`knownTo` is required for people and objects; `[]` explicitly records that no campaign knowledge is known. It is optional for other subjects. `campaignInfo` on a person or object normally implies the matching `knownTo` code.

`campaign` frontmatter applies only to session notes, campaign-specific meta notes, and campaign source material. It uses the registry's canonical long name. `knownTo`, `campaignInfo`, and `Campaign:*` blocks use lowercase short codes. Campaign directory placement does not make `campaign` appropriate for an in-world entity.

Positive campaign lists in `audience` are not yet a universal requirement. A session backlink proves that the subject appeared, not that every character knows every fact in the note.

### Privacy and DM metadata

The linter distinguishes three private in-note forms:

- `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%` is local-only material excluded from GitHub;
- ordinary `%% ... %%` comments are Git-shared, nonpublic DM or editorial material; and
- `Campaign:none` blocks are structured Git-shared DM material excluded from Taelgarverse.

`dm_notes` is a human attestation that relevant information exists outside Git-tracked material or in someone's head. Shared comments or blocks do not imply it. For `dm_owner: tim`, `joint`, or `none`, the linter searches `_DM_` for direct links or unique exact-name matches, reports matching Markdown notes as wikilinks without exposing content, and uses the result only to question or support human review of `dm_notes`. It never removes `dm_notes` automatically.

The linter does not adjudicate `color` versus `important`; both mean that the human attestation is present. When local hidden notes support an existing non-`none` value, they are supporting evidence rather than an open finding. Report found Markdown notes as Obsidian wikilinks, not raw filesystem-path lists.

`dm_notes: none` is compatible with a SECRET block. A SECRET block—including one that only links to hidden material—already communicates that the page has a secret. If it accounts for the hidden material found and no additional unlinked `_DM_` material remains, retain `dm_notes: none` without complaint. Additional unlinked hidden material may still justify a human-review warning. If `color` or `important` has no local file evidence, a suggestion to review the attestation is permitted, but the field may represent information in someone's head or another off-vault source and must never be removed automatically.

### Links and relationship metadata

Obsidian resolves a bare wikilink target from filenames, not from frontmatter `name` or `aliases`. Link validation therefore treats `[[Drankor]]` as a link to a file named `Drankor.md`; an alias on another file does not make that link ambiguous. Explicit paths disambiguate genuine duplicate filenames.

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

### Article metadata and comment placement

The searchable viewpoint lives at the end of frontmatter:

```yaml
POV: 1750
```

Persistent article interpretation lives at the end of the note after prose and comments:

```yaml
%%^Metadata:article:v1%%
mode: geographic reference
povNotes: "Accuracy range: approximately DR 1748–1752. Present-tense geographic description; historical background does not change the article's speaking point."
%%^End%%
```

`POV`, `mode`, and `povNotes` describe the article rather than the lint run and remain after review. The descriptive profile is already represented by the note tag and is not repeated. A completed lint requires `POV`, `mode`, and `povNotes`; the old inline `(POV:: ...)` annotation and article-block `pov` key are deprecated. On re-lint, migrate their meaning into the frontmatter value and `povNotes` rather than preserving duplicate temporal labels.

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

`_scripts/lint_taelgar_notes.rb` is the adopted batch wrapper around the same versioned rules. It is an operational optimization of linter 2.3, not a different rule set: it does not change applicability, severity, persistent state, or report interpretation and therefore does not itself require a linter-version increase.

Batch preparation builds the vault link/identity index once and scans `_DM_` once for all targets. For each note, its preferred freshness baseline is the first Git commit containing the prior `lintedAt` and `lintVersion`. The tag and report are deliberately excluded from baseline identity because a human can clear them without changing the verification boundary. This prevents either that normal clear or a delayed commit of the completed lint from making the lint commit itself appear to be later invention. If the completion pair has not yet been committed, the fallback is the last commit at or before `lintedAt`. Freshness work is grouped by the resulting Git commit; within a shared baseline the batch reuses the changed-path list, per-source diff, line counts, and last-commit evidence. New untracked invention sources are included when their filesystem modification time is later than `lintedAt`. Because local-only `_DM_` files are outside Git, matching private evidence also receives a separate modification-time freshness check. Every note still receives its own deterministic report, prior completion state, freshness candidates, checksum, and agentic review.

Routine routing follows the adopted invalidation model:

- an unlinted note requires review;
- a stale `lintVersion` requires a complete current-version review using the old timestamp as its freshness baseline when valid;
- a current note with a newer external source that mentions it requires judgment about whether invention elsewhere has overtaken the article; and
- a current note with no newer invention candidate is eligible for a no-op and is not edited merely to refresh its timestamp.

Routing is triage, not a substitute for an explicit request. If the user specifically asks to re-lint a named note, review it completely even when routine routing would permit a no-op.

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
