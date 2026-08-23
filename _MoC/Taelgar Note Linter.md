---
linterVersion: "3.5"
dmNotesReviewVersion: "3.4"
nameReviewVersion: "3.4"
povReviewVersion: "3.4"
name: Taelgar Note Linter
---
# Taelgar Note Linter

> [!info] Adopted specification
> This note defines version **3.5** of the Taelgar note linter. The operational skill is `.agents/skills/lint-taelgar-note/SKILL.md`; deterministic validation is implemented by `_scripts/validate_taelgar_note.rb`.

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

An otherwise in-scope note is lintable when its authored body makes a substantive statement about its subject or source. The statement may be visible or inside an authored ordinary comment, `SECRET`, `Campaign:*`, or `Date:*` block. It need not be grammatically complete when the note title supplies the subject or an implied copula. Definitional phrases, elliptical reference prose, factual list entries, tables, callouts, and quotations qualify when they communicate a complete subject-matter assertion. This is a semantic judgment, not a word-count, punctuation, or regular-expression test.

Frontmatter, headings, images or embeds, isolated names, labels, dates, tags, wikilinks, TODOs, editorial reminders, and linter-owned `Metadata:*`, `povNotes`, and `Lint` blocks do not satisfy the minimum. One or a few words in a comment also do not qualify when they communicate no substantive fact. Evaluate the authored body before any lint-owned edit; existing lint output cannot make a textless note eligible. The deterministic validator rejects objectively empty, heading-only, embed-only, and linter-output-only bodies. Text that survives that mechanical screen is an authored-content candidate for contextual confirmation, not evidence that a grammatical sentence exists. After that screen, uncertainty favors inclusion; declare the note ineligible only when the remaining material is clearly placeholder or nonassertive content.

Tag, note type, and other directory names do not create additional exclusions. An explicitly named ineligible note is reported and left unchanged. Collections omit it; samples replace it rather than counting it. Target eligibility does not filter evidence. All relevant vault Markdown notes—including notes under Worldbuilding and dot or underscore directories—remain searchable and citable while linting an eligible target. Their ordinary authority, privacy, and uncertainty still apply; Worldbuilding remains provisional rather than canonical merely because it is evidence.

## Versioning

The current adopted linter version is stored in this note's `linterVersion` field. The deterministic validator exposes the same value as `validatorVersion`.

Every completed write-mode lint records:

```yaml
lintedAt: "2026-08-19T11:40:58-04:00"
lintVersion: "3.5"
```

The linter must take `lintVersion` from the validator output for that run. It must not infer the version from the target note, copy an older value, or maintain a separate hard-coded skill version. If `linterVersion` and `validatorVersion` disagree, the lint fails and writes no new timestamp.

Increase the linter version when a change can alter applicability, severity, findings, safe-fix behavior, persistent lint state, or report interpretation. Editorial clarification that cannot change an outcome does not require a bump. Schema versions such as `Metadata:names:v1` and the validator's output `schemaVersion` are independent of the linter version.

`dmNotesReviewVersion` is an independent minimum prior linter version for the contextual `dm_notes` evidence review. A note whose valid `lintVersion` is at least this value treats its recorded `lintedAt` as the last DM-attestation validation unless a matching `_DM_` source has since been modified. Unrelated future linter-version increases do not re-trigger DM review. When the adopted DM-review rules change, set `dmNotesReviewVersion` to the new linter version so older attestations are reviewed once under the new rules. Compare dotted versions numerically rather than lexically.

`nameReviewVersion` is the independent minimum prior linter version for contextual name-block applicability and pronunciation review. A note with a valid `lintedAt` whose numeric `lintVersion` is at least this value skips that contextual review during later lints. Existing name blocks still receive deterministic schema validation, and entries marked `proposed`, `disputed`, or `unresolved` still produce deterministic human-review tasks without being recalculated. When name-review rules change, raise `nameReviewVersion`; a human who changes the primary subject of a note can force review by removing its lint completion version.

`povReviewVersion` is the independent minimum prior linter version for contextual `POV` selection and, where applicable, `povNotes` review. A present `povNotes` block bypasses this gate and is always rechecked together with `POV`; the linter must retain the block because removing one is always a human-only decision. Only when `povNotes` is absent does the gate compare the prior lint: a note with a valid `lintedAt` whose numeric `lintVersion` is at least this value preserves its valid existing `POV` without recomputing it and preserves the absence of `povNotes`. Deterministic validation still reports a missing or malformed `POV`, a forbidden or malformed present `povNotes` block, and other structural defects. When POV-review rules change, raise `povReviewVersion`; a human can force contextual POV review by removing the lint completion version.

The deterministic report exposes the three contextual boundaries under `reviewGates.names`, `reviewGates.dmNotes`, and `reviewGates.pov`. For POV, `required` is always true when `povNotes` is present; when it is absent, `required` reflects the version comparison. The POV record also exposes `povNotesApplicable`, so the same decision is available in single-note output and each batch manifest packet rather than being recomputed by the reviewing agent.

An older `lintVersion` remains an accurate record of the earlier check, but it makes the note a candidate for re-linting under the current rules.

### Re-linting stale versions

A stale version is any present `lintVersion` that differs from `validatorVersion`, including a legacy numeric value such as `2`. Staleness means that the previous result used an older rule set; it does not itself prove that the note has a substantive defect.

Before changing the note, preserve the previous `lintedAt`, `lintVersion`, `status/check/lint` state, and Lint block as historical input. If the old `lintedAt` is a valid timestamp, use it as the Git freshness baseline even when the version is stale. Then run every currently applicable deterministic and contextual rule from the current version. The contextual `dm_notes`, name, and POV reviews remain not applicable when their independent gates are satisfied. Do not perform a version-only migration or assume that an earlier clean result satisfies a newly applicable rule.

The prior Lint block and status are evidence, not findings to copy forward. Re-evaluate each old item against the current note and current sources, validate persistent metadata under current schemas, and build the final report only from findings that remain open under the current version. The initial `lint.version_outdated` finding is resolved by successful completion and does not by itself justify a new Lint block.

If the old timestamp is absent or invalid, there is no trusted freshness baseline. Perform the full current lint and search all relevant source history without claiming that the search is bounded to changes since a verified lint.

Complete the source review and validate all content other than completion state first, treating `lint.version_outdated` as the expected transitional finding. Then apply the new timestamp, current `validatorVersion`, replacement report, and tag state as one final scoped edit and validate the resulting note. If the re-lint is interrupted before that edit, leave the old state untouched. If final validation fails afterward, restore the old completion state and report the failure; never leave a new version or timestamp on an incomplete lint. Open current work gets a replacement report and `status/check/lint`; a clean result gets neither.

## Modes and authorization

The linter has two note-level modes:

- **Check-only:** inspect and report in chat without editing the note or advancing `lintedAt`.
- **Write lint:** perform the complete review, apply only authorized lint-owned changes, and record final lint state.

A request to lint or re-lint a named note authorizes lint-owned changes: deterministic frontmatter normalization, supported persistent metadata, unambiguous meta-comment placement, approved high-confidence light editorial fixes, and lint state. Broader prose rewriting, speculative lore development, or multi-note cleanup still requires its own scope and approval.

The deterministic formatter may be run in safe-fix mode only when it can preserve parsed values, comments, meaningful quoting, unknown fields, and special syntax. Editorial fixes are opt-in and limited to objective typos, punctuation, duplicated words, and other defects whose correction is unambiguous without changing voice, cadence, uncertainty, or meaning. Unusual, awkward, archaic, or stylistically marked phrasing is not itself defective. When phrasing materially impairs comprehension but correction requires judgment, preserve it and report `editorial.prose_clarity` with the exact passage, an explanation, and a copy-ready candidate. Mere stylistic preference is not a finding. Editorial fixes never decide names, dates, classifications, lore, uncertainty, private material, or conflicts.

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

When POV review is required, the contextual lint identifies the article's speaking position, then judges whether the prose is suitable for that point of view. A present `povNotes` always requires that review. When `povNotes` is absent and the version gate does not require review, preserve a valid existing `POV` without recomputing it and do not recreate the block; temporal coverage and later-material-change review remain separate. Temporal review is not a generic requirement to date every fact. It distinguishes lifecycle dates, dated relationships, date blocks, current reference prose, historical snapshots, bounded event accounts, campaign-relative language, and layered primary-source viewpoints.

Every completed lint records the searchable scalar viewpoint in frontmatter `POV`. Most notes also record the practical interpretation as plain text in the persistent `%%^povNotes:v1%%` block, following [[Temporal POV Metadata]]. The exception is a note under `Campaigns/**` tagged `session-note`, `meta`, or `source`: it records `POV` but must not contain `povNotes`. `POV` is the article's best single temporal reading position, not its validity interval or the span between its oldest and newest facts. When contextual POV review applies, test the ordinary values in order: use `modern` when the current DR 1700s campaign era is precise enough; otherwise use a decade when a rough campaign era or life stage is precise enough; otherwise use a year for a narrower supported snapshot. Use `undated` only when all three tests fail because the note and its sources support no temporal reading position. `undated` records missing temporal support, not timeless truth or stability, and does not excuse incompatible undated states. Century values, named eras, and `timeless` are legacy choices to reconsider only when contextual POV review applies.

When contextual POV review applies, do not use `modern` merely because `povNotes` can state a narrower limitation. When the undated article centrally describes a specific living person's current leadership, office, whereabouts, age or life stage, or active relationship, that state normally makes the modern era too broad; use a supported decade or year unless the evidence establishes that the state is broadly stable across the era.

When contextual POV review applies, choose `POV` from the undated visible frame. Historical backstory does not widen the viewpoint, and an isolated dated paragraph does not narrow it. When `povNotes` is applicable, it begins with `Temporal coverage:` and concisely records the article's actual shape: broad or approximately bounded coverage, a narrow snapshot, one-sided uncertainty, or discontinuous periods with gaps. If no temporal information or material temporal constraint is established, a generic statement that coverage is broadly modern is sufficient. Name event boundaries when established, distinguish unknown periods from contradicted states, and never invent an exact cutoff or infer continuity between separated facts. Before choosing a narrow POV, propose the smallest useful `Date:*` blocks for supported later facts or state changes; do not apply a new block without approval because it can change filtered visibility.

Later truth does not by itself make an explicitly earlier-POV note incorrect, but a later fact that would materially change the article still requires the human coverage, POV, and game-update disposition below. A defect exists when the note silently mixes incompatible viewpoints, uses unanchored changing language, exposes later knowledge in an earlier view, or applies campaign/date blocks inconsistently.

### Structural role and importance

A bounded glossary entry, connector, overview, hub, minor subject, and major campaign subject do not have the same coverage expectations. Importance informs contextual judgment but never becomes a generic word-count or heading requirement.

### Editorial sufficiency

Every completed lint assigns exactly one editorial verdict to the note as a reference artifact:

- **Sufficient:** the note performs its present role and provides setting-specific substance proportional to its demonstrated importance.
- **Sufficient, worth expanding:** the note is already adequate, but one bounded addition would materially improve its usefulness.
- **Underdeveloped:** the note does not currently perform its reference role because it lacks a central setting-specific account, role, state, consequence, or other core dimension required by its demonstrated importance.

Use this controlling question: **Does the visible note currently perform its reference role without a central gap?** If not, the verdict is **Underdeveloped**. If it does and one bounded addition would materially improve it, the verdict is **Sufficient, worth expanding**. Otherwise the verdict is **Sufficient**.

The following rules control that judgment:

- Underdevelopment requires an identifiable central missing dimension. The fact that more could be written is not enough.
- Existing vault evidence is not required for every underdevelopment verdict. A subject whose central importance is clear may be underdeveloped because important lore still needs to be invented.
- Independently inventory central gaps whose content is established elsewhere and central dimensions that remain uninvented. When an appropriate source establishes the missing or outdated information, use `coverage.established_fact_missing` or `coverage.later_material_change`. When a separate central dimension has not yet been invented, use `editorial.note_underdeveloped`. A note may contain findings from both categories when they describe different gaps; never duplicate the same gap under both.
- Reserve invention-based underdevelopment for subjects whose importance or centrality is clear from their setting or campaign role, important relationships or consequences, structural function, or broad pattern of use and backlinks. A backlink pattern is one signal among others, never a numerical score or threshold.
- A bounded or minor note can be sufficient with very little prose when it performs its reference role. When importance is unclear or the missing material is optional rather than central, use **Sufficient** or **Sufficient, worth expanding**, not **Underdeveloped**.
- Visible incomplete structure matters when the author has established a central section and left it with placeholders, fragments, or hidden planning instead of an account. Several such central sections strongly support **Underdeveloped**; polished volume elsewhere does not compensate for them. One peripheral unfinished section ordinarily supports at most **Sufficient, worth expanding**.
- Do not require conventional template headings, generic genre material, a word count, or a universal entity checklist.

For a person, a defining relationship, role, and fate can be enough for a minor connector. An important person may require central consequences and current state when those are material to the reference account. Apply the same proportional principle to places, events, objects, organizations, and other subjects.

Do not stop the gap inventory after identifying established missing facts. When a person's visible account gives only an origin or childhood while established evidence shows a materially different later identity or role, separately ask whether the transition is established. If how or why the important later role developed remains unknown and that transition is central to the person's reference account, report it as `editorial.note_underdeveloped`; the established endpoints do not supply the missing transition.

**Sufficient, worth expanding** is a handoff-only verdict. By itself, it cannot create a Lint block, `status/check/lint`, or an editorial finding. Other findings are evaluated independently, and the note is open whenever any remain. Record one structured bounded addition with the exact proposed content, its practical benefit, and named source notes, evidence, and certainty. Preserve distinctions such as established, reported, assumed, provisional, and uninvented. Never use worth-expanding to hide an open conflict or shared-public-material finding.

An **Underdeveloped** verdict must identify the exact central missing dimensions and the smallest useful development scope without inventing canon or merely saying to expand the note. Its Lint report includes an `### Editorial assessment` between validated judgments and open findings that explicitly states **Underdeveloped** and names every central gap. Do not report the same gap under both an editorial and a coverage rule. `editorial.note_underdeveloped` has default severity **suggestion** and is appropriate only for the balanced, central-importance case above.

### Reference voice and stylistic judgment

For ordinary canonical reference prose, the integrated editorial pass also asks whether the writing is specific, direct, informative, and proportionate to its evidence and reference role. Fluent prose can still fail this standard when it is materially generic, inflated, repetitive, formulaic, or built from unsupported connective claims. Examples include atmospheric description that could apply to almost any subject, repeated assertions of importance without additional information, canned symbolic conclusions, and elaborate transitions that imply unsupported causation or synthesis.

This is a judgment about the published prose, never an attribution of authorship or a claim that text was generated by AI. Do not flag merely polished writing, one conventional transition, harmless awkwardness, intentional poetic or in-world voice, quotations, Primary Sources, campaign narration, or evocative description that carries concrete setting-specific information. Ordinary source records retain their own purpose and voice. A distinctive human style is not a defect merely because it resembles a common model tendency.

When a material passage fails the reference-voice standard, report `editorial.reference_voice` as a **suggestion**. Identify the exact passage or bounded section, name the concrete stylistic problem, state which supported facts or nuances must be preserved, and direct the human to rewrite or remove it. Do not supply replacement prose for this rule: the required resolution is a human rewrite, so a copy-ready replacement is deliberately not applicable. Consolidate a pervasive problem into one note-level finding instead of creating a task for every paragraph. Do not apply an automatic body edit under this rule.

Keep this rule distinct from adjacent findings. Use `editorial.prose_clarity` when meaningful prose is materially difficult to understand; use a correctness or coverage rule for unsupported or missing facts; and use `editorial.note_underdeveloped` when generic volume leaves the note without a central substantive account. A note may have both `editorial.reference_voice` and `editorial.note_underdeveloped` only when they describe those distinct problems.

### Worldbuilding discussion routing

`_scripts/generate_worldbuilding_discussion_index.rb` generates `_scripts/worldbuilding_discussion_index.json` as a research sidecar. It scans every Markdown note under `Worldbuilding` except any path containing a `Staging` directory segment, matched case-insensitively. It resolves explicit links and embeds plus unique distinctive plain-text identities, including stable display forms recovered from resolved aliased links. For each canonical target it retains the complete matching source set without a count cap, with source path, match kind, mention lines, title, folder, conversation dates where encoded in the filename, and a deterministic thread cluster. The sidecar is provisional research routing only: a match never establishes canon, correctness, coverage, importance, or underdevelopment.

Determine the editorial sufficiency verdict without consulting the discussion index. Only after a note is independently judged **Underdeveloped** may the linter query its sidecar record. Two or more distinct non-Staging Worldbuilding source notes constitute significant discussion for this routing purpose. When significant discussion exists, add one informational line to the note's `### Editorial assessment` directing later research to the complete sidecar. Do not add a separate finding, severity, task, source list, excerpt, or chat-handoff section, and do not change the verdict or lint state because the sidecar exists. A note with either sufficient verdict does not query or report this information.

Batch workers never receive discussion records or read the indexed Worldbuilding sources for this rule. The finalizer loads the sidecar only when at least one completed worker result is already Underdeveloped, verifies the target identity and sidecar freshness, and mechanically inserts the compact route. A single-note lint follows the same order and uses the generator's `--query PATH` mode only after assigning the Underdeveloped verdict. The complete sidecar remains available for a later, separately requested research query.

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

For every potentially missing fact or event, first determine whether an appropriate vault source establishes it. Unestablished information is a development opportunity rather than an incorrectness or coverage finding, but a clearly central uninvented dimension may support `editorial.note_underdeveloped` under the editorial sufficiency rules. Provisional material may motivate future invention but does not establish a missing fact.

Established information is a `coverage.established_fact_missing` warning when omitting it would materially mislead the reader about the subject, its state, a major relationship, or the article's central account, or would leave the article materially outdated. Materiality is not determined mechanically from note length, backlink count, or the mere existence of additional detail. Established information that is not materially required may support a suggestion under the threshold below; otherwise its omission is not a finding.

Campaign and session records are evidence, but ordinary people, Gazetteer, and other reference notes are not campaign logs. A party visit, conversation, purchase, overnight stay, routine encounter, or other campaign appearance does not become reference-note coverage merely because it happened. Campaign-derived material belongs in reference prose only when it establishes a defining fact about the subject or caused a durable change or consequence significant from that subject's perspective—for example destruction or lasting damage, a change of ownership or function, a defining relationship or fate, or a durable change in public role or reputation. If play merely revealed a stable subject fact, state that fact in generic reference voice and omit the party's discovery unless the discovery itself was consequential. Include an event rather than only its consequence only when the event is independently central to the subject's account. These constraints do not apply to campaign and session records whose purpose is to document play.

Apply this as a filter over campaign evidence already gathered, not as another search pass. The absence of an incidental campaign event is neither a coverage gap nor an expansion candidate. A tavern does not need to record that the party visited; if their actions burned down its second story, the lasting damage or resulting change may be material, while the visit itself still is not.

An established fact or event that would materially change the article must be reported as `coverage.later_material_change` even when it occurs after the recorded `POV`. The linter records a human decision rather than silently treating the information as outside scope: update the article and `POV`; defer the update and add or retain the appropriate `status/gameupdate/*` tag; or intentionally preserve the earlier article and `POV`, in which case the applicable game-update tag can be removed. The linter does not choose among these outcomes or alter game-update tags.

An editorial suggestion must be grounded in a named source, exact passage, metadata problem, or other specific evidence; name the affected note or notes; propose a concrete addition, correction, or bounded human choice; explain the practical improvement; and be important enough to justify retaining `status/check/lint`. Evidence and resolution may cross note boundaries. Concise evidence-backed additions to stubs are valid suggestions when they improve usefulness; brevity alone is not a defect. Vague prompts to expand, add detail, or improve context are not findings. A lesser observation may be reported informationally when useful, but it does not retain a Lint block or lint status.

When a source passage already consulted for a finding or expansion candidate directly contradicts the target's visible prose or persistent metadata, handle that specific contradiction as an open conflict, coverage, or metadata finding. This is a local coherence check over the target and evidence already in hand, not a new search, note reread, or separate review pass.

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

For an applicable note, write a minimal primary entry with the exact subject name and its established language, or `language: unknown`; add other forms only when documented and never invent etymology. Preserve established name-specific meaning, derivation, naming agent, and historical circumstance or timing in the appropriate fields or `notes`; “minimal” means omitting unsupported or redundant fields, not discarding documented naming context. During ordinary lint, an existing entry with `status: documented` remains documented and every populated documented value remains unchanged. Supported missing fields may be added. If another note conflicts with a documented value, preserve the entry and report open `metadata.names_documented_conflict` for human resolution. When creating a missing entry, if frontmatter has an actual pronunciation, treat the note itself as the source and record the matching entry as `status: documented` without requiring a source note. Otherwise use an explicit recorded pronunciation when found, mark it `documented`, and cite its source in `notes`. If the complete name is a genuinely obvious ordinary name or plain-English title, omit pronunciation. Otherwise derive the strongest supported proposal and store it with `status: proposed`, with its source or derivation in `notes`, until human acceptance. Preserve an existing unresolved entry rather than recalculating it; that rule takes precedence over the creation rule.

Evaluate every displayed work-title form independently under [[Name Metadata]]. Infer `language: Common` only when the form consists entirely of ordinary modern-English words and no contrary title-language evidence exists; record an explicit translation as such. Non-English, constructed, or transliterated forms do not receive that presumption: use an unambiguous established language or `language: unknown`. The title-form language does not establish the language of the work's text, and ancestry, origin, or authorship is not sufficient evidence by itself.

Use adopted language rules before cultural patterns or a real-world analogue in [[Languages]], and a cautious spelling-based reading only when no stronger basis exists. [[Languages]] remains the ordinary prose authority. `_scripts/generate_language_pronunciation_analogues.rb` writes `_scripts/language_pronunciation_analogues.json` from every level-five language heading and the analogue lines under both language and language-family headings. The sidecar preserves each complete analogue statement and its provenance, attaches family guidance to member languages, and records explicit parent-language inheritance for dialects such as Free Orcish. A qualified or undefined mapping must remain qualified or undefined; its complete text can still contain useful naming guidance, as with Vargaldi. Batch preparation reads the sidecar and performs only a filesystem freshness check; regenerate it only when [[Languages]] is newer. Relevant language and family entries, including inherited fallbacks, are selected into each evidence packet so workers do not repeatedly parse the prose note. The generator's audit mode reports name-block language values that match neither an entry nor a lookup term; it does not invent guidance for uncovered values. The generated data records exact guidance text, mapping status, lookup terms, relationships, and provenance, not deterministic pronunciation rules; contextual pronunciation remains agentic judgment. Missing exact in-world phonology leaves an analogue-derived result proposed. Every pronunciation must be pronounceable; exemptions use absence rather than sentinel text. Whenever a name-block entry has a pronunciation and frontmatter either has no pronunciation or has a different one, its `notes` must record the block value's source or derivation. A matching frontmatter pronunciation needs no source note. Never overwrite accepted frontmatter or recalculate an unresolved block entry automatically.

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

When review applies, use these four attestation outcomes:

- `dm_notes: none` with no matches is valid and produces no finding.
- `dm_notes: none` with matches requires semantic disposition of the mechanically clustered candidates. Candidate presence alone is not a suggestion to change the human attestation. When a genuine cluster contains plausible public or private material absent from the target, surface that material in the private chat handoff as described below; otherwise produce no user-facing list.
- `dm_notes: color` or `important` with no matches produces the suggestion “No `_DM_` notes found; verify `dm_notes`.” The field may represent information in someone's head or another off-vault source and must never be removed automatically.
- `dm_notes: color` or `important` with matches supports the positive attestation. Confirmed source links are always reported: in the Lint block when the note is independently open, or in the private chat handoff when the note is clean. The linter does not adjudicate between the two positive values and does not screen those sources for recoverable public additions.

Batch preparation constructs a mechanical evidence dossier before editorial review. It preserves every matching path, filesystem modification time, match kind, matched line, bounded source context, source-family grouping, and exact or near-duplicate context cluster. Clustering reduces repeated judgment but never discards a source or its provenance. Workers review each unique cluster once rather than screening every duplicate path separately. This dossier is owner-only temporary evidence and is not note content.

For each genuine `_DM_` cluster for a target with `dm_notes: none`, record whether it offers no recoverable material, a plausible public addition, or a plausible private addition. A plausible addition receives the exact handoff marker `Destination: public` or `Destination: private`, a content-level summary, and a bounded copy-ready candidate in the mechanically rendered private user-facing chat. This content may be quoted or paraphrased in chat but must not be intentionally copied or paraphrased into a Git-tracked note, Git-shared Lint report, or other shared artifact. Privacy validation is a quick semantic sanity check completed by the editorial worker, not an exhaustive raw-text or lexical-overlap proof. The recovery remains an optional human adoption choice and creates no finding or attestation change by itself.

When a note with a plausible `_DM_` recovery is already open for an independent finding, the finalizer records only the supporting note paths in the replacement Lint block under an informational heading, with each exact Obsidian wikilink on its own dash-bulleted Markdown list item. It uses the same destination for confirmed positive-attestation support. Any `_DM_` wikilink the linter records in a Lint block must use that one-link-per-list-item form; inline links and multiple links on one item are invalid. Do not include private contents there. Because those links are then available in the note, the mechanically rendered chat handoff says that sources are recorded in the Lint block rather than duplicating them. For a clean note, the handoff includes the exact source links as a Markdown list. Do not list merely matching `dm_notes: none` sources that add nothing recoverable.

The presence or contents of `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%`, ordinary comments, and `Campaign:none` blocks in the target never trigger, suppress, support, or otherwise affect the candidate-based `dm_notes` review; they are separate privacy mechanisms. In-note secret material remains compatible with `dm_notes: none` under [[Note Status]]. Every full lint nevertheless reviews each `SECRET` block for plausible public or private recovery. Useful content is explained with a bounded copy-ready candidate in the private chat handoff, without copying or paraphrasing it into Git-tracked output. A `SECRET` recovery remains informational and does not itself create a finding.

### Shared nonpublic content review

Every full lint independently reviews each substantive ordinary `%% ... %%` comment and `Campaign:none` block in the target. This review is always applicable and is not gated by `dmNotesReviewVersion`. Comment or block length alone never creates a finding. Record one disposition for every reviewed unit: `redundant_with_public`, `public_adoption_candidate`, `dm_only`, `speculative_or_unresolved`, `source_pointer`, or `no_useful_material`. The contextual review separates:

- public-safe description, history, geography, culture, or other reader-facing information;
- DM-only encounters, mechanics, treasure, secrets, and unpublished twists; and
- brainstorming, source notes, and editorial reminders.

When an appropriate source establishes public-safe information and its omission materially weakens or misleads the visible article, the ordinary coverage rule applies. When useful material appears only in the noncanonical shared comment or block but is a specific, coherent candidate for human adoption, report `editorial.public_material_candidate` as a suggestion rather than treating it as established canon. The finding identifies the exact private passage, explains the practical improvement, and includes copy-ready public prose. When shared hidden material substantially duplicates visible prose, report `editorial.shared_material_redundant`, identify the redundant passage, and propose removing it or retaining only distinct editorial guidance. If a unit is partly redundant and partly useful, propose a bounded split. Both dispositions remain open and retain `status/check/lint`; neither may be reduced to a worth-expanding handoff. When public candidates are intermingled with usable DM material, the report also proposes a bounded organization for the remaining private guidance.

The linter never promotes or reorganizes private material automatically. A Git-shared Lint proposal copies or paraphrases only the public-safe subset of Git-shared comments or `Campaign:none` blocks and does not expose DM mechanics, treasure, secrets, unpublished twists, or unresolved brainstorming. It never copies or paraphrases material from `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%` blocks or local `_DM_` notes into the Git-shared Lint report. The private chat handoff is the only lint output where those local sources may be summarized or quoted for the user.

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

`POV` and, where applicable, `povNotes` describe the article rather than the lint run and remain after review. Every completed lint requires frontmatter `POV`. A note under `Campaigns/**` tagged `session-note`, `meta`, or `source` must not be given a new `povNotes` block; a present block remains a finding for human review. For other notes, a temporal review creates or preserves one nonempty `povNotes:v1` text block; when an absent block is protected by the version gate, its absence is preserved instead. The linter never removes an existing `povNotes` block. `mode` has no adopted semantics and is not retained. The old inline `(POV:: ...)` annotation and `Metadata:article` block are deprecated.

If `povNotes` is present, perform contextual POV selection regardless of the prior lint version, recheck the block, and retain it. If `povNotes` is absent, perform contextual POV selection only when the note has no valid `lintedAt`/`lintVersion` pair or its prior version is numerically lower than `povReviewVersion`; a valid prior version at or above the threshold suppresses recomputation of a valid existing `POV` and preserves the block's absence. Deterministic validation still reports malformed, duplicate, or categorically forbidden present metadata and a missing or malformed `POV`. When review applies, legacy `povNotes` text is evidence rather than accepted final output: retain it unchanged only when contextual review confirms that it remains accurate; otherwise rewrite it. For an exempt Campaigns record, do not create a block; if one is already present, retain it and report the mismatch for human disposition. Discard `mode`, `profile`, and other obsolete article-block keys only when doing so does not remove the existing `povNotes` block.

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
7. Perform agentic review for correctness, coverage, editorial quality, editorial sufficiency, status disposition, and development opportunity.
8. Apply only authorized lint-owned changes and write supported persistent metadata.
9. Re-run deterministic validation with links enabled and confirm the specification and validator versions agree.
10. Write `lintedAt`, the captured `lintVersion`, and either the open report/tag or the clean state.
11. Re-read the complete note, validate YAML and structured blocks, inspect the full diff, and report the result in chat.

### Batch execution

`_scripts/lint_taelgar_notes.rb` is the adopted batch wrapper around the same versioned rules. Its sharding and staging are operational mechanisms, not a different rule set; changing only their configurable size limits does not require a linter-version increase.

Automatic batch discovery excludes every note with any `Worldbuilding`, dot-prefixed, or underscore-prefixed directory segment. Preparation also omits objectively blank, heading-only, embed-only, and linter-output-only bodies and records them in `selectionSummary.skippedNoReviewableProse`. Surviving authored-content candidates receive semantic eligibility review inside their assigned shard. Explicit preparation rejects path-ineligible targets, and workspace creation and finalization reject any manifest note that becomes objectively blank, including a manifest created under an older rule set. These exclusions never filter the evidence index or source search.

Batch preparation builds the vault link/identity index once, scans `_DM_` once for all targets, loads the generated language-analogue sidecar once, and creates reusable per-note evidence packets. For each note, its preferred freshness baseline is the first Git commit containing the prior `lintedAt` and `lintVersion`. The tag and report are deliberately excluded from baseline identity because a human can clear them without changing the verification boundary. This prevents either that normal clear or a delayed commit of the completed lint from making the lint commit itself appear to be later invention. If the completion pair has not yet been committed, the fallback is the last commit at or before `lintedAt`. Freshness work is grouped by the resulting Git commit; within a shared baseline the batch reuses the changed-path list, per-source diff, line counts, and last-commit evidence. New untracked invention sources are included when their filesystem modification time is later than `lintedAt`. Because local-only `_DM_` files are outside Git, the shared DM scan records each matching file's modification time directly; this evidence both gates contextual DM review and routes a current note when a matching private source is newer than `lintedAt`. The preparer also extracts bounded contexts for every match and clusters exact or near duplicates without discarding their paths. Every note still receives its own deterministic report, prior completion state, freshness candidates, checksum, relevant language entries, complete DM dossier, and agentic review.

Batch selection resolves scope before routing:

1. The user's named files, folders, collection, or sample are the maximum scope; selection flags never broaden it.
2. Remove target-ineligible paths.
3. Remove objectively blank or generated-only stubs. Semantically review each surviving authored-content candidate; for a sample, replace only notes whose remaining material is clearly placeholder or nonassertive content.
4. A plain `lint` request excludes every note with a valid prior `lintedAt`/`lintVersion` pair. Stale versions, open findings, deterministic errors, or newer evidence do not override this default.
5. Only explicit language such as `re-lint`, `lint again`, or `refresh the lint` authorizes including previously linted notes, and only within the target that language modifies. Mixed scopes are prepared separately.

The batch CLI enforces this boundary: named targets are filtered by default, `--re-lint` includes valid prior lint state, and `--all-linted` or `--stale` require `--re-lint`. Within an explicitly authorized re-lint scope, routing follows the adopted invalidation model:

- an unlinted note requires review;
- a stale `lintVersion` requires a complete current-version review using the old timestamp as its freshness baseline when valid;
- a current note with a newer external source that mentions it requires judgment about whether invention elsewhere has overtaken the article; and
- a current note with no newer invention candidate is eligible for a no-op and is not edited merely to refresh its timestamp.

Routing is triage after selection, never authorization to re-lint. If the user specifically asks to re-lint a named note, review it completely even when routing would permit a no-op.

Batch execution has four phases:

1. **Prepare:** produce one read-only manifest and gather shared deterministic, DM, and Git evidence.
2. **Shard and stage:** create a private temporary review workspace. Use largest-estimate-first balanced bins with a default cap of approximately 40,000 estimated input tokens and no note-count floor or ceiling. The estimate includes note and serialized packet size plus evidence-complexity allowances; path locality is a soft tie-breaker. A note above the token limit receives a singleton shard. Each shard has its own staged candidate directory, which is the worker's file allowlist. These are configurable operational defaults.
3. **Parallel review:** assign each shard to a fresh-context editorial worker. The worker may search the full vault but reads only its packet and staged candidates by default, edits only those staged copies, and returns compact structured results. No worker writes a live note.
4. **Finalize:** require exactly one completed result per manifest note; verify assignment, manifest and validator versions, live and staged checksums, preserved old completion state, eligibility, editorial-verdict and clean/open consistency, and every proposed final note before writing anything.

The user-facing coordinator is also the batch manager and uses `gpt-5.6-sol` at `xhigh` reasoning. Every semantic eligibility, source, privacy, coverage, editorial sufficiency, and report-writing decision belongs to a fresh `gpt-5.6-sol` `xhigh` editorial worker. Spawn those workers without inherited conversational history and give each only the authoritative rules and its bounded shard. The same worker reviews its own completed evidence, verdict, candidate, privacy sanity, and result while that context remains loaded. Do not create separate managing, review, or adjudication agents. An optional `gpt-5.6-terra` `high` helper may run preparation, construct shards, track completion, validate schemas and hashes, and invoke finalization; it must not interpret note content or alter an editorial result. Deterministic scripts remain the authority for those mechanical operations.

Each temporary result records the path, the staged candidate's final SHA-256, semantic eligibility, a concise reason when ineligible, editorial verdict when eligible, clean/open outcome, replacement Lint report when open, optional concise supplemental handoff, declared objective body edits, structured dispositions for every `_DM_` evidence cluster, `SECRET` block, and shared-nonpublic unit, an explicit editorial assessment when underdeveloped, a structured expansion candidate when worth expanding, and completed worker self-review checks. A recoverable `_DM_` or `SECRET` item records its public or private destination, a content-level chat summary, and a bounded copy-ready candidate. An expansion candidate records the exact addition, practical benefit, and one or more source records containing path, evidence, and certainty. Record the SHA-256 only after the candidate and result are complete; later candidate mutation invalidates the result. Difficult, semantic-ineligible, and invention-based underdeveloped notes are not routed to another reviewer; the original worker completes the same explicit self-review fields. These owner-only temporary records may contain private content but are not note content or permanent calibration data.

The finalizer leaves semantically ineligible notes unchanged. For eligible notes it writes the current validator version and one offset-bearing completion timestamp, removes or replaces the old report, and clears or sets only `status/check/lint` according to independently open findings. **Sufficient** and **Sufficient, worth expanding** may each be clean or open; **Underdeveloped** must be open. It mechanically inserts the appropriate DM evidence links into open reports. Only when a completed result is already Underdeveloped does it load the Worldbuilding discussion sidecar; a significant match adds the compact research route to the editorial assessment without entering the chat handoff. It generates the complete private chat handoff from structured results, including all recoverable DM and SECRET additions and every worth-expanding candidate's sourced benefit and copy-paste-ready statement. The finalizer stages same-directory replacements so each file replacement is atomic and rolls back ordinary write failures after a complete preflight. It rejects newly introduced whitespace errors before writing and returns a `reviewSummary` that separates mechanically proven completion-lifecycle or frontmatter-formatting changes from targeted-review changes involving metadata, persistent metadata, body prose, private or visibility-sensitive content, non-lint statuses, or custom syntax. File-based manifests, workspaces, results, and finalization output use owner-only permissions because their evidence records can expose private paths and excerpts. A missing result, incomplete self-review, out-of-allowlist assignment, checksum or state mismatch, later staged-candidate mutation, whitespace error, or invalid verdict/outcome combination aborts the whole batch and must never be bypassed by manually advancing the affected notes.

After a successful batch write, the coordinator verifies that every changed path is authorized, accepts `mechanicalOnlyPaths` without rereading routine diff hunks, and inspects only the finalizer's `targetedReviewPaths`. A metadata-only target needs a bounded value check rather than a repeat source review. Body prose, private or visibility-sensitive content, non-lint statuses, and custom syntax receive closer hunk review and a full-note reread only when the hunk lacks enough context or an anomaly appears. Scoped `git diff --check` remains a backstop rather than the first whitespace gate. A post-finalization correction proven to remove only trailing horizontal whitespace changes neither semantic content nor structural lint proof and does not require refinalization, validator reruns, or a note reread; any other later edit receives the targeted verification appropriate to its change category.

## Deferred design areas

The following remain deliberately unsettled and are not universal lint requirements:

- positive campaign semantics for `audience`;
- a replacement for long historical `whereabouts` lists;
- a registry and location model for regional maps beyond the supported single-hex and two-end cases;
- whether significant shared DM material needs an authored frontmatter field;
- a queryable development-priority scale; and
- bounded relationship propagation beyond direct freshness links.

Changes in these areas require an explicit design decision and, when they alter lint outcomes, a linter version bump.
