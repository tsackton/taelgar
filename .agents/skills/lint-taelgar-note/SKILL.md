---
name: lint-taelgar-note
description: Lint, re-lint, or batch-lint eligible Taelgar vault notes with deterministic validation and source-grounded editorial judgment, then write or clear versioned lint state. Use when the user asks to lint, re-lint, batch-review, validate the completeness or currency of, or apply Taelgar lint metadata to one or more notes. Never lint notes under Worldbuilding or any dot or underscore directory; do not use for ordinary lore editing without a lint request.
---

# Lint Taelgar Note

Combine the vault validator with a source-grounded editorial review. Report actual deficiencies relative to the note's expected scope, not mere opportunities for invention.

## Applicability boundary

- A lint target is ineligible when any directory segment in its path is `Worldbuilding` or begins with `.` or `_`. This includes nested paths such as `Campaigns/_generated/**` and `Campaigns/.chatgpt/**`, not only top-level directories.
- Every other Markdown note is an eligible target; tag, note type, and other directory names do not create exclusions. If the user explicitly names an ineligible note, report that it is outside scope and do not lint it. In a collection, omit ineligible notes; in a random sample, replace them rather than counting them.
- Target eligibility never limits evidence discovery. Search all relevant vault Markdown notes, including notes under Worldbuilding and dot or underscore directories, while preserving each source's authority and privacy. Worldbuilding remains provisional evidence; ineligible location never makes a source canonical.

## Choose the mode

- Obey the closest `AGENTS.md` and the user's stated scope.
- Treat a request to lint or re-lint a named note as approval for lint-owned changes: safe frontmatter normalization, supported persistent metadata, approved meta-comment placement, high-confidence light mechanical edits, and lint state.
- Use check-only mode when the user asks for a report in chat, says not to edit, or asks only whether the note is clean. Do not change the note or advance `lintedAt` in this mode.
- Preview and obtain approval before broader prose rewriting, speculative lore development, or multi-note cleanup.
- Preserve unrelated worktree changes and never expose private DM content.

## Load the governing references

Read the complete target note before acting. Load only the references relevant to its profile:

- Before changing metadata, read `../../../_MoC/Metadata Specification.md` and `../../../_MoC/Note Categorization.md`.
- Before interpreting any existing `status/*` tag or proposing any status-related outcome, read `../../../_MoC/Note Status.md`; it governs status meanings and lifecycle semantics.
- For names or pronunciation, read `../../../_MoC/Name Metadata.md` and the relevant language material under `../../../Background/Languages.md`.
- For campaign values, read `../../../_MoC/Campaign Registry.md`; `../../../_scripts/session_note_campaigns.json` is the authoritative registry.
- For article temporality, read `../../../_MoC/Temporal POV Metadata.md`.
- Read `../../../_MoC/Taelgar Note Linter.md`, the authoritative lint specification, and capture its `linterVersion`.

## Run the deterministic pass

From the vault root, run:

```sh
ruby _scripts/validate_taelgar_note.rb --format json "PATH/TO/NOTE.md"
```

On a re-lint, also pass the previous timestamp:

```sh
ruby _scripts/validate_taelgar_note.rb --format json --linted-at "PREVIOUS_TIMESTAMP" "PATH/TO/NOTE.md"
```

Keep link and relationship checks enabled for the final pass. Capture `validatorVersion` from the JSON output and require it to match the specification's `linterVersion`. Use `--fix-frontmatter` only after reading the complete note, then inspect the diff and confirm that parsed values and comments were preserved.

## Batch multiple notes efficiently

For two or more notes, use `_scripts/lint_taelgar_notes.rb` so the batch shares the vault index, scans `_DM_` once, and reuses Git evidence for notes with the same baseline. For each prior lint, it prefers the first Git commit containing that note's recorded `lintedAt` and `lintVersion`; later human clearing of its tag/report does not change that verification boundary. While the completion pair is still uncommitted, the batch falls back to the last commit at or before `lintedAt`. Because local-only `_DM_` files are outside Git, newer matching private evidence is identified by file modification time and reported separately. The batch tooling changes execution cost, not lint rules or the requirement to read and judge every included note completely; a skipped `dm_notes` evidence review is a rule-defined not-applicable result, not an incomplete lint.

Prepare a read-only manifest for named notes:

```sh
ruby _scripts/lint_taelgar_notes.rb prepare --output /tmp/taelgar-lint-manifest.json "PATH/ONE.md" "PATH/TWO.md"
```

This default command skips every target with a valid prior `lintedAt`/`lintVersion` pair. Resolve scope in this order:

1. Use the user's named files, folders, collection, or sample as the maximum scope; no selector may broaden it.
2. Remove ineligible targets using the path rule above.
3. Unless the user explicitly says `re-lint`, `lint again`, `refresh the lint`, or equivalent, skip notes with valid prior lint completion state. Stale versions, open findings, or newer evidence do not silently authorize re-linting.
4. Apply explicit re-lint authorization only to the target it modifies. Split mixed lint and re-lint scopes into separate manifests when necessary.

For an explicitly requested re-lint, pass `--re-lint`:

```sh
ruby _scripts/lint_taelgar_notes.rb prepare --re-lint --output /tmp/taelgar-lint-manifest.json "PATH/ONE.md" "PATH/TWO.md"
```

For explicitly requested maintenance across previously linted notes, select them and omit current notes with no newer invention candidate:

```sh
ruby _scripts/lint_taelgar_notes.rb prepare --re-lint --all-linted --only-needs-review --output /tmp/taelgar-lint-manifest.json
```

Use `--re-lint --stale` instead of `--re-lint --all-linted` to select only notes whose stored version differs from the current validator. The batch command rejects `--all-linted` or `--stale` without `--re-lint`. The manifest contains a separate deterministic report, prior completion state, freshness baseline, candidate sources, checksum, and routing reason for every included note. `current_with_no_newer_invention_candidate` is eligible for a no-op only inside an explicitly authorized re-lint scope. An explicit user request to re-lint a named note still requires complete review even if its routing result is no-op eligible.

Read each included note in full and perform the ordinary expectation, source, and agentic review below. Apply supported persistent metadata or lint-owned edits first, but do not yet change `lintedAt`, `lintVersion`, `status/check/lint`, or the old Lint block. After those edits, snapshot all reviewed files:

```sh
ruby _scripts/lint_taelgar_notes.rb snapshot --manifest /tmp/taelgar-lint-manifest.json --output /tmp/taelgar-lint-decisions.json
```

Fill every decision with `outcome: clean` and no report, or `outcome: open` and one complete replacement `%%^Lint%%` block. Then dry-run finalization before writing:

```sh
ruby _scripts/lint_taelgar_notes.rb finalize --manifest /tmp/taelgar-lint-manifest.json --decisions /tmp/taelgar-lint-decisions.json
```

If preflight succeeds, repeat with `--write`. The finalizer refuses a different manifest, unresolved decisions, changed reviewed checksums, changed old completion state, unsafe frontmatter, invalid open reports, or any deterministic error in the proposed final notes. It validates every result before writing any, uses one completion timestamp and validator version, stages same-directory replacements, and rolls back ordinary write failures. Do not bypass a failed finalizer by manually advancing lint state.

## Re-lint a stale version

Treat any existing `lintVersion` that differs from `validatorVersion`—including a legacy numeric value such as `2`—as stale historical state.

Before editing, preserve the prior `lintedAt`, version, `status/check/lint` state, and Lint block. If `lintedAt` is valid, pass it to `--linted-at` as the freshness baseline even though the version is stale. If it is missing or invalid, run the full current lint without claiming a bounded freshness search and examine all relevant sources.

Run every currently applicable deterministic and contextual rule. Never do a version-only migration or assume the old clean result satisfies newly applicable rules. Treat the old report and tag as evidence to re-evaluate, not findings to carry forward; validate existing persistent metadata under current schemas. The initial `lint.version_outdated` finding is resolved by successful re-linting and does not alone require a final report. The contextual `dm_notes` and name reviews have their own gates below, so an unrelated linter-version change does not make either review applicable again.

Complete the source review and validate all non-state content first, treating `lint.version_outdated` as the expected transitional finding. Then update the timestamp, version, report, and tag together as the final scoped edit and validate the resulting note. If interrupted before that edit, leave the old state untouched. If final validation fails afterward, restore the old completion state and report the failure; never leave a new version or timestamp on an incomplete lint. The replacement report contains only currently open findings and follows the ordinary open-or-clean lifecycle below.

## Build the expectation profile

Infer the profile from the note's tags, classifications, structure, content, and role; folder location alone is insufficient. Check all applicable expectations:

- identity, classification, aliases, required persistent name metadata for notes about named in-world subjects or works, and strict actual-pronunciation disposition;
- `knownTo` for people and objects, and map metadata for waterways, roads, and settlements;
- canonical long campaign names in `campaign` frontmatter and lowercase short codes in `knownTo`, `campaignInfo`, and `Campaign:*` blocks;
- searchable frontmatter `POV` and a concise note-specific `povNotes` temporal-coverage explanation; every completed write-mode lint records the least precise useful reading position supported by the undated visible article frame, or `undated` only when no reading position is supported;
- internal inconsistency separately from cross-note conflict;
- completeness against already established facts separately from opportunities to invent more;
- substantial Git-shared nonpublic material for public-safe facts or concrete adoption candidates that are absent from the visible article;
- editorial clarity, spelling, metadata organization, special syntax, and every existing non-`check` `status/*` tag; preserve `status/check/*` as unassessed human-review state.

Session notes and Primary Sources are authoritative source records: do not call them factually wrong. Their accounts can still be incomplete, internally inconsistent, biased, unclear, or poorly structured. All Markdown notes remain discoverable evidence even when their paths make them ineligible lint targets; apply the ordinary authority and privacy distinctions to their claims. Worldbuilding remains provisional evidence.

## Search for later invention

Search filenames, `name`, aliases, spelling variants, links, backlinks, and relevant surrounding passages. Use `name` and aliases for discovery and metadata matching, but remember that Obsidian bare wikilinks resolve filenames only. Markdown inside dot-prefixed directories remains evidence but is not an Obsidian link or relationship target, so ignore it when deciding whether a filename, name, or alias is ambiguous. When searching from the shell, include hidden and ignored Markdown notes while excluding repository internals, for example with `rg --hidden --no-ignore --glob '*.md' --glob '!.git/**'`; never reuse the target-eligibility filter as an evidence filter. Follow vault source authority, beginning with likely canonical sources and broadening deliberately to campaign and session records, Primary Sources, Worldbuilding, and DM material.

Use Git history as the freshness boundary. Starting from the previous `lintedAt`, prioritize newer external sources—especially session notes, campaign notes, finalized `beat-facts.json`, `_DM_`, and `_dm_notes`—that mention or resolve to the subject. A clean-preserving edit to the target itself does not make it stale; invention elsewhere can.

For `dm_owner: tim`, `joint`, or `none`, apply the independent `dmNotesReviewVersion` recorded in [[Taelgar Note Linter]]. Perform the contextual `dm_notes` evidence review when the note has no valid `lintedAt`/`lintVersion` pair, its prior `lintVersion` is lower than `dmNotesReviewVersion`, or an `_DM_` Markdown note that links or could link to the subject has a filesystem modification time later than `lintedAt`. Compare dotted versions numerically. If none of those triggers applies, do not reconsider `dm_notes` during that lint; still validate that any authored `dm_owner` and `dm_notes` values use the allowed vocabulary. A future unrelated linter-version increase does not re-trigger this review. To adopt changed DM-review rules, raise `dmNotesReviewVersion` to the linter version that introduces them.

When review is triggered, report matching `_DM_` Markdown notes as wikilinks without quoting or exposing their content, then use this decision table:

- `dm_notes: none` with no matches: no finding.
- `dm_notes: none` with matches: list them informationally with “Did you check these notes?” Do not suggest changing the field merely because candidates exist.
- `dm_notes: color` or `important` with no matches: suggest “No `_DM_` notes found; verify `dm_notes`.” Never remove or change the attestation automatically because it can represent off-vault or remembered information.
- `dm_notes: color` or `important` with matches: list them informationally for reference; do not adjudicate between the two positive values.

The presence or contents of `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%`, ordinary comments, and `Campaign:none` blocks inside the target never trigger, suppress, or otherwise affect this `dm_notes` review. They are separate privacy mechanisms.

## Review shared nonpublic material

During every full lint, independently review substantial ordinary `%% ... %%` comments and `Campaign:none` blocks in the target for useful material absent from the visible article. This review is always applicable and is not gated by `dmNotesReviewVersion`. Do not create a finding merely because a comment or block is long. Separate:

- public-safe description, history, geography, culture, or other reader-facing information;
- DM-only encounters, mechanics, treasure, secrets, and unpublished twists; and
- brainstorming, source notes, and editorial reminders.

If an appropriate source establishes public-safe information and omitting it materially weakens or misleads the visible article, apply the ordinary coverage rule below. If useful material appears only in the noncanonical shared comment or block but is a specific, coherent candidate for human adoption, report `editorial.public_material_candidate` as a suggestion rather than treating it as established canon. The suggestion must identify the exact private passage, explain why the visible note would improve, and include copy-ready public prose. When public candidates are intermingled with usable DM material, also propose a bounded organization for the remaining private guidance. The candidate must be important enough to justify retaining `status/check/lint`; omit minor possibilities.

Never promote or reorganize private material automatically. Copy or paraphrase only the public-safe subset into the Git-shared Lint proposal; do not expose DM mechanics, treasure, secrets, or unresolved brainstorming. Never copy or paraphrase material from `%%SECRET[v2:2813636d58fe60b6f07f9b3fae26e409]%%` blocks or local `_DM_` notes into the Git-shared Lint report.

## Review names and pronunciation

Apply the independent `nameReviewVersion` recorded in [[Taelgar Note Linter]]. Perform contextual name review when the note has no valid `lintedAt`/`lintVersion` pair or its prior `lintVersion` is numerically lower than `nameReviewVersion`. When a valid prior version is at least the threshold, do not reconsider whether a missing name block is appropriate and do not search for or derive a pronunciation. To force re-review after a human changes the note's subject, remove its lint completion version before linting. When the adopted name-review rules change, raise `nameReviewVersion` to the new linter version.

The gate never suppresses deterministic validation of an existing `Metadata:names:v1` block. Always validate its YAML shape, required fields, statuses, pronunciations, and provenance rule. An entry with `status: proposed`, `disputed`, or `unresolved` remains open deterministically even when contextual review is skipped; preserve it without recalculating or replacing it and carry the validator's human-review task into the Lint report.

When contextual review is required, use this decision sequence:

1. Decide whether the note's primary subject is a named in-world thing or in-world work. If yes, give it a name block. If it merely mentions in-world subjects while organizing, analyzing, or summarizing them, do not add a block. Apply this semantically rather than from tag, folder, or title.
2. Create or validate the minimal primary entry with the exact subject name and its established language, or `language: unknown`. Add other name forms only when they are genuinely documented; do not invent etymology or manufacture entries for every alias. Preserve established name-specific meaning, derivation, naming agent, and historical circumstance or timing in the appropriate fields or `notes`; “minimal” means omitting unsupported or redundant fields, not discarding documented naming context.
3. Disposition pronunciation. When creating a missing entry, if frontmatter already contains an actual pronunciation, treat this note as its source and record the matching block pronunciation as `status: documented`; no source note is required. Otherwise search for an explicit recorded pronunciation. Store one found elsewhere as `status: documented` and identify its source in `notes`. If the complete reader-facing name is a genuinely obvious ordinary name or plain-English title, omit pronunciation. Otherwise derive the strongest supported proposal, store it with `status: proposed`, explain its source or derivation in `notes`, and keep the deterministic unresolved-name task open until human acceptance. The rule above for preserving an existing unresolved entry takes precedence over this creation rule.

For a proposal, use an adopted language pronunciation or spelling rule first, then an established cultural naming pattern or real-world analogue in [[Languages]], then a cautious spelling-based reading only when nothing stronger exists. A real-world analogue without exact in-world phonology remains `status: proposed`; explain concrete sound and stress choices. If multiple analogues differ materially, preserve the preferred proposal and alternatives without claiming acceptance.

Whenever a name-block entry has a pronunciation and frontmatter either has no pronunciation or has a different one, require `notes` to record the block value's source or derivation. A matching frontmatter pronunciation needs no source note because the note itself is the source. Never overwrite frontmatter or accepted name data during contextual review; a mismatch or competing pronunciation is a human decision.

## Decide coverage and suggestions

For every potentially missing fact or event, apply this coverage rule:

1. Determine whether an appropriate vault source establishes it. If it is not established, treat it as a development opportunity, never as a correctness or coverage finding. Provisional material may motivate future invention but does not establish a missing fact.
2. Ask whether omitting the established information would materially mislead the reader about the subject, its state, a major relationship, or the article's central account, or would leave the article materially outdated. If yes, report `coverage.established_fact_missing` as a warning. Do not infer materiality from note length, backlink count, or the mere existence of additional detail.
3. If the established information is not materially required, create a suggestion only when it passes the rule below; otherwise make no finding.

An established fact or event that would materially change the article must be reported even when it occurs after the recorded `POV`; never silently classify it as outside scope. Report `coverage.later_material_change` as a warning and present the human choice without choosing among the outcomes: update the article and `POV`; defer the update and add or retain the appropriate `status/gameupdate/*` tag; or intentionally preserve the earlier article and `POV`, in which case the applicable game-update tag can be removed. Do not add, remove, or alter a game-update tag during linting.

Create an editorial suggestion only when it:

- is grounded in a named source, exact passage, metadata problem, or other specific evidence;
- names the affected note or notes and proposes a concrete addition, correction, or bounded human choice;
- explains the practical improvement; and
- is important enough to justify retaining `status/check/lint` until resolved.

The evidence and best resolution may cross note boundaries. For example, `[[History of the Skaer]]` establishing that the Skaer trace their ancestry to the ancient mariner culture can support a concrete suggestion to add that fact to a Skaer reference note. For a stub, check likely overview sources such as a watershed, regional, or history note for a concise evidence-backed sentence that would make the stub more useful, but never infer a defect from brevity alone. When practical, include copy-ready wording. Do not create vague suggestions such as “expand this history,” “add more detail,” or “improve the context.” If a proposed improvement does not meet this threshold, record it only as nonblocking information when useful or omit it; do not retain a Lint block or `status/check/lint` for it.

## Assess status tags

Never assess any `status/check/*` tag. These tags record human-review state and are not evidence that the tagged concern is supported, stale, or resolved. Preserve them without a supported, questioned, or not-assessable disposition and never recreate one that a human removed. `status/check/lint` is likewise not semantically assessed; add or remove it only through the Lint report lifecycle below, while continuing to enforce its deterministic report/tag consistency.

For every existing `status/*` tag outside `status/check/*`, assign one disposition without changing the tag:

- **supported:** the note and appropriate vault evidence support the tag under [[Note Status]]; no open finding is required;
- **questioned:** concrete evidence suggests that the tag no longer describes the note; report `status.questioned` as a warning with the evidence and a bounded human choice; or
- **not assessable:** the tag depends on human intent, provenance, unfinished plans, or unavailable evidence; preserve it and do not create an open finding solely because it cannot be assessed.

Assess `status/stub` against whether the note still has no useful detail, not against a generic word count. Assess `status/gameupdate/*` against established intervening game events and the article's recorded temporal framing. If the coverage rule leaves a human choice between updating the article, deferring the update, or intentionally preserving an earlier `POV`, classify the game-update tag as not assessable until that choice is made rather than deciding it for the human. Apply the same rubric to other non-`check` statuses using their documented meanings. Never add, remove, replace, or normalize any status tag except `status/check/lint` through its authorized lifecycle.

## Apply safe lint-owned changes

Use this fallback whenever the rules below do not explicitly settle whether to apply a change. Apply it automatically only when exactly one correction satisfies the adopted rules, the operation is lint-owned, and it preserves lore meaning, uncertainty, attribution, temporal framing, and player/DM visibility. Supported descriptive metadata may be applied when it records one unambiguous interpretation of the existing note rather than changing that interpretation. If more than one reasonable correction exists, a human decision remains, or meaning or visibility could change, provide a copy-ready proposal instead of applying the change.

Ordinary automatic cases include canonical frontmatter ordering and formatting, replacing versioned lint state, an unambiguous one-to-one legacy-syntax conversion, and moving an unambiguously misplaced header comment without changing its text. Propose prose or lore changes, competing classifications or metadata interpretations, new or moved `Date:*`, `Campaign:*`, or secret blocks that can change filtered visibility, ambiguous comment moves or map conversions, and all changes to human attestations or non-lint status tags.

- Canonicalize frontmatter deterministically: deprecated fields first; then `headerVersion`, `lintedAt`, `lintVersion`, `displayDefaults`; classification; other fields; naming; relationships; visibility/DM fields; and finally `POV` immediately after `dm_notes`. Keep string lists and dictionaries on one line, and expand lists of dictionaries one entry per line. Never change `headerVersion`.
- Put meta comments about note quality or POV immediately below the complete header block. Leave other private comments in place unless a clearer arrangement is obvious; suggest uncertain moves rather than performing them.
- Put persistent `Metadata:names:v1`, `Metadata:map:v1`, and `povNotes:v1` blocks at the end of the note after prose and comments. `POV` belongs in frontmatter; `%%^povNotes:v1%%` contains only the plain-text temporal-coverage explanation. On every full re-lint, independently reassess both `POV` and `povNotes` against the current note and applicable evidence. Treat a legacy `Metadata:article` block's `povNotes` text as evidence whose meaning must not be lost, not as accepted final output: retain it unchanged only when the contextual review confirms that it remains accurate; otherwise rewrite it. Replace the legacy block with the reassessed text, discard `mode`, `profile`, and other obsolete keys, and migrate any useful legacy `pov` or inline `(POV:: ...)` meaning into frontmatter `POV` or the text explanation as appropriate. Keep the Lint block, when required, after persistent metadata.
- Choose `POV` from the undated visible article frame, not from the span between its oldest and newest facts. Test the ordinary values in order: use `modern` if the current DR 1700s campaign era is precise enough; otherwise use a decade if a rough campaign era or life stage is precise enough; otherwise use a year if the article is a narrower supported snapshot. Use `undated` only after all three tests fail because the note and its sources support no temporal reading position. `undated` records missing temporal support, not timeless truth or stability, and never excuses incompatible undated states. Historical backstory does not widen `POV`; an isolated dated event does not narrow it. Reconsider legacy `timeless`, named-era, and century values contextually on re-lint rather than replacing them mechanically.
- Do not use `modern` merely because `povNotes` can describe a narrower limitation. A central undated claim about a specific living person's current leadership, office, whereabouts, age or life stage, or active relationship normally requires a supported decade or year unless the evidence establishes that state across the modern era. `povNotes` explains the chosen viewpoint's limits; it does not rescue an overbroad viewpoint.
- Write `povNotes` beginning with `Temporal coverage:` and keep it concise, normally one sentence and at most two when needed. Describe the coverage as broad or approximately bounded, narrow, one-sided uncertain, discontinuous, or unsupported; for `POV: undated`, state that the available evidence does not support `modern`, a decade, or a year. Name established before/after events when useful, distinguish unknown periods from contradicted states, and never invent an exact cutoff or infer continuity between separated facts. Do not restate every lifecycle date, dated metadata value, or `Date:*` block unless it changes how the article should be read.
- Isolate narrower dated state before finalizing `POV`. If one supported event or change is narrower than the rest of the article, propose wrapping the smallest affected passage in a copy-ready `Date:*` block and keep the broader whole-note POV; do not apply a new block without approval because it can change filtered visibility. Do not call a decade- or modern-generic article a single-year snapshot merely because it contains one dated paragraph.
- For required map metadata with unknown positions, insert the validator's typed skeleton instead of `status: missing` and `locations: []`. Every location entry uses `map` and `locator`; `role` and `feature` are optional annotations. Waterways use two entries distinguished by `role: source` and `role: outlet`. Roads use two unordered endpoint entries with no directional role; include blank `feature` fields so a human can optionally name the endpoint cities or other features. Settlements use one entry. Do not write `geometry`, `hex`, `sourceHex`, or `outletHex`. During re-lint, remove redundant `geometry` and convert legacy position keys to equivalent `locator` entries when the mapping is unambiguous; otherwise provide a copy-ready candidate for human review. Preserve blank `locator` values until a human supplies the positions, and keep `metadata.map_location_missing` open. A blank optional `feature` is not a finding. Replace legacy empty placeholders with the typed skeleton during re-linting.
- Treat name metadata as human-curated and follow the independent contextual-review gate above. Never leave the only copy of a proposed pronunciation in the replaceable Lint block or promote it to frontmatter before human acceptance.
- Every `pronunciation` value in frontmatter or a name entry must be an actual pronunciation. For an obvious ordinary name, plain-English title, meta label, or unresolved inherited component, omit the field or entry key; never write `title`, `obvious`, `meta`, or `inherited from ...` as pronunciation data.
- When proposing deprecated-field replacement or useful POV metadata/comments, provide copy-ready candidate text.
- List every automatic or editorial change in the open report. If the final result is clean and therefore has no report, summarize those changes in chat; Git preserves the diff.
- Never silently rewrite lore, dates, names, classifications, uncertainty, or private material. Never remove a status tag other than `status/check/lint` under the clean-lint rule below.

## Write the final lint state

Write the validator's exact version as quoted `lintVersion` and an offset-bearing `lintedAt` only after the full write-mode lint and final validation complete. Never copy the target's previous version or maintain a separate hard-coded version in this skill. If the specification and validator versions disagree, stop without writing completion state and report the mismatch.

If any error, warning, or suggestion remains open:

- write exactly one `%%^Lint%%` block at the end, replacing any prior report;
- add or retain `status/check/lint`;
- include at least one unchecked Markdown task, with stable rule ID, severity, evidence, and a copy-ready candidate where applicable;
- distinguish applied changes, informational observations, validated judgments, and status disposition from open work.

If no error, warning, or suggestion remains open:

- write no Lint block;
- remove any previous Lint block and remove only `status/check/lint`;
- retain the new timestamp, version, and supported persistent metadata;
- do not preserve checked tasks or an empty “no findings” report;
- do not create a report or tag solely for informational observations or validated judgments.

A check-only clean lint makes no changes and records no new verification timestamp.

## Verify and hand off

Re-read every changed note in full. Run the deterministic validator again without `--no-links`, parse the YAML, check special blocks and resolved links, inspect the complete diff, and run a scoped `git diff --check -- "PATH/TO/NOTE.md"`.

In the handoff, state which files changed, whether open findings remain, whether the note is now clean or tagged for review, and what validation passed. If lint tooling or this skill changed, also run its focused test or structural validator.
