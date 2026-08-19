---
name: lint-taelgar-note
description: Lint or re-lint a Taelgar vault note with deterministic validation and source-grounded editorial judgment, then write or clear versioned lint state. Use when the user asks to lint, re-lint, validate the completeness or currency of, or apply Taelgar lint metadata to a note. Do not use for ordinary lore editing without a lint request.
---

# Lint Taelgar Note

Combine the vault validator with a source-grounded editorial review. Report actual deficiencies relative to the note's expected scope, not mere opportunities for invention.

## Choose the mode

- Obey the closest `AGENTS.md` and the user's stated scope.
- Treat a request to lint or re-lint a named note as approval for lint-owned changes: safe frontmatter normalization, supported persistent metadata, approved meta-comment placement, high-confidence light mechanical edits, and lint state.
- Use check-only mode when the user asks for a report in chat, says not to edit, or asks only whether the note is clean. Do not change the note or advance `lintedAt` in this mode.
- Preview and obtain approval before broader prose rewriting, speculative lore development, or multi-note cleanup.
- Preserve unrelated worktree changes and never expose private DM content.

## Load the governing references

Read the complete target note before acting. Load only the references relevant to its profile:

- Before changing metadata, read `../../../_MoC/Metadata Specification.md` and `../../../_MoC/Note Categorization.md`.
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

## Re-lint a stale version

Treat any existing `lintVersion` that differs from `validatorVersion`—including a legacy numeric value such as `2`—as stale historical state.

Before editing, preserve the prior `lintedAt`, version, `status/check/lint` state, and Lint block. If `lintedAt` is valid, pass it to `--linted-at` as the freshness baseline even though the version is stale. If it is missing or invalid, run the full current lint without claiming a bounded freshness search and examine all relevant sources.

Run every current deterministic and contextual rule. Never do a version-only migration or assume the old clean result satisfies newly applicable rules. Treat the old report and tag as evidence to re-evaluate, not findings to carry forward; validate existing persistent metadata under current schemas. The initial `lint.version_outdated` finding is resolved by successful re-linting and does not alone require a final report.

Complete the source review and validate all non-state content first, treating `lint.version_outdated` as the expected transitional finding. Then update the timestamp, version, report, and tag together as the final scoped edit and validate the resulting note. If interrupted before that edit, leave the old state untouched. If final validation fails afterward, restore the old completion state and report the failure; never leave a new version or timestamp on an incomplete lint. The replacement report contains only currently open findings and follows the ordinary open-or-clean lifecycle below.

## Build the expectation profile

Infer the profile from the note's tags, classifications, structure, content, and role; folder location alone is insufficient. Check all applicable expectations:

- identity, classification, aliases, strict pronunciation disposition, and human-curated name metadata;
- `knownTo` for people and objects, and map metadata for waterways, roads, and settlements;
- canonical long campaign names in `campaign` frontmatter and lowercase short codes in `knownTo`, `campaignInfo`, and `Campaign:*` blocks;
- searchable frontmatter `POV`, article mode, and a note-specific `povNotes` explanation; every completed write-mode lint records the broadest honest POV value supported by the note;
- internal inconsistency separately from cross-note conflict;
- completeness against already established facts separately from opportunities to invent more;
- editorial clarity, spelling, metadata organization, special syntax, and every existing `status/*` tag.

Session notes and Primary Sources are authoritative source records: do not call them factually wrong. Their accounts can still be incomplete, internally inconsistent, biased, unclear, or poorly structured. Worldbuilding notes are explicitly provisional: describe internal inconsistency, divergence, or development status, but never issue an incorrectness finding merely because canon differs.

## Search for later invention

Search filenames, `name`, aliases, spelling variants, links, backlinks, and relevant surrounding passages. Use `name` and aliases for discovery and metadata matching, but remember that Obsidian bare wikilinks resolve filenames only. Follow vault source authority, beginning with likely canonical sources and broadening deliberately to campaign and session records, Primary Sources, Worldbuilding, and DM material.

Use Git history as the freshness boundary. Starting from the previous `lintedAt`, prioritize newer external sources—especially session notes, campaign notes, finalized `beat-facts.json`, `_DM_`, and `_dm_notes`—that mention or resolve to the subject. A clean-preserving edit to the target itself does not make it stale; invention elsewhere can.

When `dm_owner` is `tim`, `joint`, or `none`, search `_DM_` for notes that link or could link to the subject. Report found Markdown notes as wikilinks and describe relevance without quoting or exposing private content. Treat `dm_notes: color` and `dm_notes: important` alike: local evidence supports either positive value and is not a reason to change between them. If positive `dm_notes` has no local evidence, suggest human review but never remove it automatically because it can represent off-vault or remembered information. A `%%SECRET[v2:01d09d28f3c9b99beed3e3ecc2487a5f]%%` block—even one containing only links to hidden material—communicates that the page has a secret and can support `dm_notes: none` when it accounts for the found material and no additional unlinked DM source remains. Question `dm_notes: none` only when additional unlinked local evidence makes it suspect.

## Apply safe lint-owned changes

- Canonicalize frontmatter deterministically: deprecated fields first; then `headerVersion`, `lintedAt`, `lintVersion`, `displayDefaults`; classification; other fields; naming; relationships; visibility/DM fields; and finally `POV` immediately after `dm_notes`. Keep string lists and dictionaries on one line, and expand lists of dictionaries one entry per line. Never change `headerVersion`.
- Put meta comments about note quality or POV immediately below the complete header block. Leave other private comments in place unless a clearer arrangement is obvious; suggest uncertain moves rather than performing them.
- Put persistent `Metadata:names:v1`, `Metadata:map:v1`, and `Metadata:article:v1` blocks at the end of the note after prose and comments. The article block records `mode` and note-specific `povNotes`; `POV` itself belongs in frontmatter. Migrate legacy inline `(POV:: ...)` fields and legacy article-block `pov` keys when linting. Keep the Lint block, when required, after persistent metadata.
- Treat name metadata as human-curated. When proposing pronunciation, explain the language and derivation in the report. When proposing deprecated-field replacement or useful POV metadata/comments, provide copy-ready candidate text.
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
