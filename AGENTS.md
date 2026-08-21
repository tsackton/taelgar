# AGENTS.md - Taelgar Obsidian Vault

This repository is an Obsidian vault for the homebrew D&D world of Taelgar. Its
lore, campaign records, and worldbuilding notes are the primary product. It also
contains scripts, plugins, assets, and session-processing data that may have more
specialized instructions.

These instructions apply throughout the repository unless a more specific
`AGENTS.md` or applicable task workflow says otherwise.

## 1. Scope and Approval

Agents may search, inspect, and summarize the vault without modifying it. Do not
create or edit files without user authorization.

A narrow, targeted instruction is itself approval. Examples include adding a
specified metadata value, expanding a specified stub, or replacing every instance
of one specified name with another. Before a broader or interpretive change—such
as open-ended cleanup, reorganizing a group of notes, or rewriting several notes
for style—show a compact preview of the files and intended changes and wait for
explicit approval.

Authorization covers only the described operation:

- Touch only the necessary files and sections.
- A request for ideas does not authorize writing them into the vault.
- Preserve pre-existing changes outside the task.
- If the necessary scope becomes materially larger, stop and ask.

## 2. Core Rules

1. **Search first.** Search relevant notes before answering lore questions or
   editing content. If the vault does not support a claim, say so.
2. **Do not invent canon.** Do not add unsupported lore, dates, names, events, or
   connective explanations. Requested speculation remains noncanonical until the
   user explicitly adopts it.
3. **Keep sparse notes sparse.** Match length and certainty to the evidence. One
   supported fact may justify only one sentence.
4. **Preserve meaning and uncertainty.** Do not silently strengthen tentative
   claims, resolve contradictions, or erase narrow exceptions.
5. **Make the smallest sufficient change.** Do not fix unrelated errors or
   formatting, even in an edited file.
6. **Mark agent-edited content notes.** Every content note modified outside
   `_sessions` must include `status/check/ai` in its YAML `tags`, except that an
   explicitly approved Taelgar note-linter run uses `status/check/lint` instead.
   The linter adds or retains `status/check/lint` only when a complete lint leaves
   an open error, warning, or suggestion. A complete clean lint writes no Lint
   block and may remove only `status/check/lint` together with any previous Lint
   block. The only status operations an agent may perform are adding
   `status/check/ai` during ordinary content work, adding `status/check/lint` for
   open lint work, or removing `status/check/lint` after an explicitly approved
   complete re-lint finds no open work. Never add, remove, or alter `status/stub`
   or any other status tag; status cleanup requires human review.
   [[Taelgar Note Linter]] is the authoritative lint specification.
   Support files such as `AGENTS.md`, scripts, and configuration are not content
   notes.
7. **Preserve special syntax.** Leave unfamiliar Obsidian constructs, generated
   blocks, callouts, code, and custom markers unchanged. Report concerns in chat
   rather than adding an unapproved annotation.

## 3. Source Authority and Uncertainty

| Source                         | Treatment                                                                                                                                                  |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Canonical reference notes      | Strongest lore authority when not marked for review, but still capable of rare uncaught errors.                                                            |
| `Primary Sources`              | Fundamental source artifacts. A source's claims may be incomplete, biased, or mistaken in-world, but the linter never declares the source note itself factually wrong. |
| Campaign and session records   | Fundamental records of play and of what characters experienced, observed, learned, or believed. They are not omniscient truth, but the linter never declares the record itself factually wrong. |
| `Worldbuilding`                | Development material, not canon unless separately adopted into a canonical note.                                                                           |
| `_DM_`                         | Local, unshared DM material. It may support a `dm_notes` attestation but must not be exposed in shared or player-facing prose.                              |
| `_dm_notes`                    | Git-shared, nonpublic DM or meta material that may be tentative or speculative. Do not expose it in player-facing prose without direction or canonical support. |
| `_MoC`                         | Authoritative for vault structure, metadata, and editorial conventions, not setting lore.                                                                  |
| `%%` comments                  | Meta, uncertain, or speculative; noncanonical by default.                                                                                                  |
| `status/check/*` material      | Lower-confidence material requiring human review.                                                                                                          |
| `status/gameupdate/*` material | The information in this note might have been superseded or impacted by game events that are not captured in the note.                                      |

These are defaults, not guarantees of correctness. When sources conflict:

- Do not choose one merely because it is easier to write.
- Preserve relevant uncertainty in the prose.
- During an approved edit, add a precise `%%` comment near the affected passage
  naming the conflict and sources.
- Report the inconsistency to the user for human review.

## 4. Standard Workflow

Before editing:

- Read the complete target note, including frontmatter and comments.
- Check for and preserve pre-existing changes to the target.
- Before changing metadata, review [[Note Categorization]] and
  [[Metadata Specification]].

### Search guidance

- Search filenames first, then `name`, `aliases`, spelling or diacritic variants,
  and both sides of aliased wikilinks. Search literal text before broadening
  case-insensitively, and collision-check proposed names.
- Start with likely canonical sources, then broaden deliberately to campaign and
  session records, `Primary Sources`, `Worldbuilding`, and DM material.
- For metadata, search anchored frontmatter fields rather than ordinary prose.
- Do not count repeated session artifacts as independent evidence; use the
  applicable workflow's finalized source of truth.
- Read the full note and surrounding passage before relying on a match. Before
  reporting that nothing was found, check filenames, metadata names and aliases,
  variants, backlinks, and likely session sources, then report the search scope.
- For vault-wide corrections, search filenames and every relevant format,
  including transcripts, JSON, and YAML; exclude `.git` and use path-safe
  operations.

While editing:

- Change only the approved files and sections.
- Preserve user-authored text outside the requested scope.
- Do not move files or change link targets unless required by the task. 
- Never rename files. If the user requests to rename a note, change the metadata `name` field but not the filename. 
- For an exact field or section change, make only that change plus the applicable
  status operation described in rule 6.

After editing:

- Re-read every changed file in full.
- Confirm frontmatter occurs once at the top and parses as YAML.
- Check edited tags, classification fields, special syntax, and wikilink targets.
- Exception: after an authorized `lint-taelgar-note` batch finalizer succeeds and
  verifies the written hashes, follow that skill's risk-based post-finalization
  verification instead of independently repeating the full-file, YAML, tag,
  special-syntax, and link checks above. This exception does not waive complete
  scoped-diff review or scoped `git diff --check`; any mismatch, tool-reported
  anomaly, or later manual edit restores the ordinary requirements.
- Review the complete diff and run a scoped `git diff --check`.
- Do not broaden the task to fix unrelated or pre-existing findings. Ignore
  harmless end-of-file-only whitespace differences.

For an exact vault-wide replacement, inspect the match set first, use path-safe
operations, and verify both the replacements and any remaining matches afterward.

## 5. Common Tasks

### 5.1 Expand a stub

- Search the vault for evidence about the subject.
- Add to existing text rather than replacing it unless rewriting was requested.
- Match the note's length to the evidence; do not pad it with atmosphere,
  repeated context, or a campaign recap.
- Follow the appropriate existing note or template.
- Mention campaign events only when they identify or explain the subject. Keep
  the mention brief and link the relevant session note with a useful alias.
- Flag contradictions rather than resolving them.
- If evidence is minimal, write a minimal factual note and add a concise `%%`
  comment explaining the source limitation.

### 5.2 Reformat or clean up a note

- Rewrite only the approved scope for clarity and concision while preserving
  meaning, uncertainty, and factual boundaries.
- Add detail only from vault sources.
- Preserve existing structures unless changing them is part of the task.
- Do not copy all replaced prose into comments by default; Git history preserves
  it. Retain particular wording in `%%` comments only when it contains ambiguity
  or nuance that the rewrite cannot safely carry forward.

If the user explicitly asks to preserve the existing text for review, preserve
**all** pre-edit note body text in `%%` comments, excluding YAML frontmatter. This
exception supports large rewrites where old and new prose must be visible together.

### 5.3 Clean up a blank or staging note

- Aim for a quick reference, not a campaign recap.
- When evidence is sparse, answer "What is this?" in one or two factual sentences.
- If the subject appears only in a session, identify it and give only useful
  context.
- Put uncertainty, proposed names, filing questions, and source limitations in
  `%%` comments.
- Do not promote staging material into canon or move it without explicit
  instruction.

## 6. Content and Obsidian Conventions

### 6.1 Voice

Canonical lore and reference notes use a professional, player-facing, in-world
encyclopedia style. Write directly. Avoid "it is said that" unless attributing a
claim to a particular in-world source; express genuine uncertainty precisely.

Campaign records, Worldbuilding notes, `_DM_`, `_dm_notes`, `_MoC`, and repository
documentation follow their own established purpose and style.

### 6.2 Comments and speculation

Use `%%` comments for uncertainty, editorial context, source limitations, and
human-review notes. Do not place established canonical prose inside comments.

Comments belong below the note's header block, never between frontmatter and the
title or above an immediately following information/header callout. A linter may
move an unambiguously misplaced comment below that header only if it preserves the
comment text exactly. Other comments stay in place unless an obvious rearrangement
is proposed for human review. Persistent `Metadata:*` and `povNotes:v1` blocks
belong at the end of the note, after article text and comments and immediately
before a replaceable `Lint` block when one is present.

For substantial DM or meta material, use:

```markdown
%%^Campaign:none%%

(content)

%%^End%%
```

Brainstorming stays in chat unless the user asks to write it. Put visible
speculation in a Worldbuilding or other explicitly noncanonical context unless
directed otherwise, with this marker immediately before it:

```markdown
%% Speculative ideas generated by AI at user request; not canon. %%
```

### 6.3 Links and sources

- Use `[[Note Name]]` or `[[Note Name|alias]]`, normally without a path or `.md`.
- Check for filename collisions rather than creating an ambiguous link.
- Obsidian resolves a bare wikilink against filenames, not frontmatter `name` or
  `aliases`. Use those identity fields for search and metadata matching, but do
  not report a wikilink collision solely because another note has the same alias.
- Link sources naturally in the prose when useful to the reader.
- If relevant sources do not fit naturally, list only those additional links in
  a hidden block:

```markdown
%% Sources:
- [[Additional Source Note]]
- [[Another Source Note]]
%%
```

- Omit the block when all relevant sources are linked naturally.
- If the user requests a complete source list, include every source in the block,
  including notes already linked in the prose.
- Preserve existing headings, links, callouts, embeds, code blocks, and custom
  markers unless the task specifically changes them.

### 6.4 Frontmatter

[[Note Categorization]] and [[Metadata Specification]] are authoritative. Follow
these general rules:

- Frontmatter appears once, at the beginning of the file.
- Preserve an existing `headerVersion`; do not manually update it. Use the current
  appropriate template for a new note.
- Deprecated or obsolete fields are preserved but placed before `headerVersion`
  so they are conspicuous during review.
- Canonical field groups are ordered as follows: `headerVersion`, `lintedAt`,
  `lintVersion`, `displayDefaults`; then `tags`, `typeOf`, `typeOfAlias` or their
  person-note equivalents, and `ancestry`; then other fields in stable relative
  order; then `name`, `aliases`, `pronunciation`; then `affiliations` and
  `whereabouts`; then `knownTo`, `excludePublish`, `audience`, `dm_owner`,
  `dm_notes`, and finally `POV`.
- Format lists containing only strings on one line. Format dictionaries on one
  line with `{}`. Format lists containing dictionaries as expanded lists, with
  each dictionary on its own single line.
- Fields not named in these groups retain stable relative order in the “other
  fields” group; do not invent a second ordering rule for them.
- Use `species` as the primary classification field for a person and the
  documented `typeOf` for non-person subjects when classification is required.
  Do not introduce `subTypeOf` as a substitute.
- Add metadata only when supported by evidence or required by the template.
- `_scripts/session_note_campaigns.json` is the authoritative campaign registry.
  Use its canonical long `name` for `campaign` frontmatter and its lowercase
  `code` for `knownTo`, `campaignInfo`, and `Campaign:*` blocks. Aliases are
  accepted for resolution but are not canonical authored values. Positive
  `audience` semantics remain a separate, underdeveloped design question.
- Apply the status lifecycle in rule 6 to edited content notes outside
  `_sessions`. If another status tag appears wrong or obsolete, report it instead
  of changing it.

## 7. Specialized and High-Risk Work

- **Taelgar linter memory isolation:** When `lint-taelgar-note` applies, do not
  consult Codex memories, rollout summaries, or prior-run guidance for ordinary
  lint execution or calibration. The live skill, adopted specification,
  validator, governance files, and vault evidence are authoritative. Historical
  linter material is available only when the user explicitly requests history,
  rationale, maintenance, or regression analysis. Any task that changes
  `linterVersion` must perform the skill's read-only memory audit and surface any
  required memory reconciliation before handoff, so the user does not have to
  remember that lifecycle step.
- **`_sessions`:** These files are exempt from `status/check/ai` and
  `status/check/lint` and may have
  strict preservation or pipeline requirements. Follow the applicable session
  workflow and its stated source of truth. Do not normalize generated artifacts,
  line identifiers, speaker order, or structured data unless required.
- **Scripts and plugins:** Content-writing rules do not replace code-specific
  engineering instructions for `_scripts`, `.scripts`, or `.obsidian/plugins`.
  Authorization, narrow scope, preservation of unrelated changes, and validation
  still apply.
- **High-risk operations:** Bulk moves or renames, deletion, large-scale
  restructuring, multi-note stylistic rewrites, collection-scale note creation,
  and merging apparently similar entities require explicit scope. An exact
  mechanical replacement of specified text is targeted work, not an open-ended
  rewrite.

## 8. Minimal Note Example

This current person-note example is illustrative; use current templates and
source evidence rather than copying it blindly.

```markdown
---
headerVersion: 2023.11.25
tags: [person, status/check/ai]
name: Szoltár
species: hobgoblin
---
# Szoltár

Szoltár is a hobgoblin warrior of the [[Iron Fang]].

%% AI note: This minimal example uses [[Session 129 (DuFr)]] as its source. A real
edit requires a complete vault search. %%
```

The sentence is sourced; the comment records the evidence limitation without
suggesting that details were invented.

## 9. Final Checklist

- The exact scope was authorized or the broader preview approved.
- Relevant sources were searched; contradictions were preserved and reported.
- No unsupported canon or certainty was introduced.
- Unrelated prose and special syntax were preserved.
- The applicable status lifecycle in rule 6 was followed; no other status tag
  changed.
- Frontmatter, classifications, and edited links were validated.
- The final diff contains only intended changes.
