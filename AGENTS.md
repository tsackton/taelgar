# AGENTS.md — Taelgar Obsidian Vault

Taelgar is an Obsidian vault for a homebrew D&D world. Lore, campaign records, and worldbuilding notes are its primary product.

These instructions apply throughout the repository unless a more specific `AGENTS.md` or applicable task workflow says otherwise.

## 1. Authorization and Git

Read-only search, inspection, and summaries are allowed. Creating or editing files requires user authorization.

A narrow instruction is itself approval—for example, changing a specified field, expanding a specified stub, or replacing specified text. Before broader or interpretive work, show a compact preview of the files and intended changes and wait for explicit approval. This includes open-ended cleanup, multi-note stylistic rewrites, restructuring, collection-scale note creation, bulk moves, deletion, and merging entities.

Authorization covers only the described operation. Ideas do not authorize writing. Preserve unrelated work, touch only necessary files and sections, and stop for approval if the required scope becomes materially larger. An exact mechanical replacement is targeted work, not an open-ended rewrite.

Never rename files. For a requested note rename, change its metadata `name`, not its filename. Do not move files or change link targets unless required by the authorized task; Staging moves and promotion into canon require explicit instruction.

### Git procedure

Routine work normally happens on `main`; do not create a branch unless requested or included in the agreed plan.

- Before editing tracked files or creating files intended for Git, inspect the branch and working-tree state.
- On `main`, proceed within scope. On another branch, proceed only when the task clearly fits its established purpose. Otherwise, or with detached HEAD, confirm the branch before editing or committing tracked files. Do not silently switch branches.
- Recheck the branch immediately before staging or committing: the checkout is shared with the user, Obsidian, and other agents. Confirm the destination if it changed unexpectedly.
- Before an authorized branch switch, account for all local changes and preserve unrelated work. Stage and commit only approved task changes.

An explicit branch choice already supplied by the user satisfies the corresponding confirmation requirement.

## 2. Evidence and Canon

Search relevant vault sources before answering lore questions or editing content. Say when the evidence does not support a claim.

Do not invent canon, dates, names, events, or connective explanations. Requested speculation remains noncanonical until explicitly adopted. Preserve uncertainty, contradictions, and narrow exceptions.

| Source | Treatment |
| --- | --- |
| Canonical reference notes | Strongest lore authority when not marked for review, but still capable of errors. |
| `Primary Sources` | Fundamental source artifacts. Their in-world claims may be incomplete, biased, or mistaken; the linter never declares the source note itself factually wrong. |
| Campaign and session records | Fundamental records of play and what characters experienced, observed, learned, or believed. They are not omniscient truth; the linter never declares the record itself factually wrong. |
| `Worldbuilding` | Development material, not canon unless separately adopted into a canonical note. |
| `_DM_` | Local, unshared DM material. It may support a `dm_notes` attestation but must not be exposed in shared or player-facing prose. |
| `_dm_notes` | Git-shared, nonpublic DM or meta material, possibly tentative. Do not expose it in player-facing prose without direction or canonical support. |
| `_MoC` | Authority for vault structure, metadata, and editorial conventions, not setting lore. |
| `%%` comments | Meta, uncertain, or speculative; noncanonical by default. |
| `status/check/*` | Lower-confidence material requiring human review. |
| `status/gameupdate/*` | May have been superseded or affected by game events not recorded in the note. |

These are defaults, not guarantees. Do not choose between conflicting sources for convenience. Preserve the uncertainty, report the inconsistency, and during an approved edit add a precise nearby `%%` comment identifying the conflict and sources.

### Search practice

- Search filenames first, then `name`, `aliases`, spelling/diacritic variants, and both sides of aliased wikilinks. Start literally before broadening case-insensitively; collision-check proposed names.
- Start with likely canonical sources, then deliberately broaden to campaign/session records, `Primary Sources`, Worldbuilding, and DM material.
- For metadata, search anchored frontmatter fields.
- Read the full source note and surrounding passage before relying on a match. Repeated session artifacts are not independent evidence; follow the workflow’s finalized source of truth.
- Before reporting no evidence, check filenames, names/aliases, variants, backlinks, and likely session sources, then state the search scope.
- For vault-wide corrections, inspect the match set across filenames and all relevant formats, including transcripts, JSON, and YAML. Exclude `.git`, use path-safe operations, and verify replacements and remaining matches afterward.

## 3. Editing Content

Before editing, read the complete target, including frontmatter and comments, and inspect its existing local changes.

Make the smallest sufficient change. Preserve unrelated prose, formatting, headings, links, callouts, embeds, code, generated blocks, and custom markers. Leave unfamiliar special syntax unchanged and report concerns in chat. For an exact field or section request, change only that scope plus the applicable status operation.

Canonical reference prose uses a professional, player-facing, in-world encyclopedia voice. Write directly; use “it is said that” only to attribute an actual in-world claim. Other note types follow their established purpose and style.

### Sparse notes, stubs, and Staging

- Match length to evidence: one supported fact may warrant one sentence. Do not pad with atmosphere, repetition, or a campaign recap.
- Add to existing stub text unless rewriting was requested; follow the appropriate existing note or template.
- Identify what the subject is and its useful defining context. Mention campaign events only when they identify or explain the subject; keep the mention brief and link the session with a useful alias.
- If evidence is minimal, write a minimal factual note and a concise `%%` source-limitation comment.
- Keep uncertainty, proposed names, and filing questions in comments. Do not promote or move Staging material without explicit instruction.

### Rewriting and preservation

Rewrite only the approved scope, preserving meaning, factual boundaries, uncertainty, and existing structure unless its change was authorized. Add detail only from vault evidence.

Do not preserve all replaced prose in comments by default; retain wording only when it carries ambiguity or nuance the revision cannot safely preserve. Git retains history.

If the user explicitly requests preservation for review, put **all pre-edit body text**, excluding YAML frontmatter, in `%%` comments.

## 4. Metadata and Status

Before changing metadata, review [[Note Categorization]] and [[Metadata Specification]].

- Frontmatter occurs once, at the top. Preserve existing `headerVersion`; use the current appropriate template for new notes.
- Follow the exact field-group order and YAML list/dictionary formatting in [[Taelgar Note Linter#Frontmatter]]. This formatting reference does not authorize a lint or unrelated normalization.
- Use `species` as a person’s primary classification and the documented `typeOf` for non-person subjects when required. Do not substitute `subTypeOf`.
- Add metadata only when supported or required by the template.
- `_scripts/session_note_campaigns.json` owns campaign identities: use its canonical long `name` for `campaign`, and lowercase `code` for `knownTo`, `campaignInfo`, and `Campaign:*` blocks. Aliases are resolution inputs, not canonical authored values. Positive `audience` semantics remain an underdeveloped design question.

### Status lifecycle

These are the default rules; an applicable workflow may state a specific exception under the precedence rule above.

- Ordinary agent-edited content notes must include YAML tag `status/check/ai`.
- `_sessions` is exempt from both `status/check/ai` and `status/check/lint`.
- Files anywhere under `Worldbuilding/Agentic Review` must have no YAML `tags` field and no inline tags.
- An explicitly approved note-linter run uses the lint lifecycle instead: a complete lint with open errors, warnings, or suggestions adds or retains `status/check/lint` and a Lint block. A complete clean lint leaves neither and may remove the previous Lint block and `status/check/lint`.
- Outside applicable workflow exceptions, the only permitted status operations are adding `status/check/ai` for ordinary edits, adding `status/check/lint` for open lint work, and removing `status/check/lint` after an explicitly approved complete clean re-lint.
- Do not change status tags beyond the operations above unless explicitly authorized by the user or by an applicable workflow after its required approvals. For example, `review-stub-staging` removes `status/stub` and applies the selected review disposition after full-page approval. Report other apparently wrong or obsolete tags for human review.

[[Taelgar Note Linter]] owns lint semantics. Support files such as `AGENTS.md`, scripts, and configuration are not content notes.

## 5. Obsidian Comments and Links

Use `%%` comments for uncertainty, editorial context, source limitations, and human-review notes. Do not hide established canonical prose in comments.

Comments belong below the title and immediately following header/information callout. A linter may move an unambiguously misplaced header comment below that block only while preserving its text exactly. Other comments stay in place unless an obvious rearrangement is proposed for human review.

Persistent `Metadata:*` and `povNotes:v1` blocks belong after article text and comments, immediately before a replaceable Lint block when present.

Use this wrapper for substantial DM or meta material:

```markdown
%%^Campaign:none%%

(content)

%%^End%%
```

### Links and source attribution

Use `[[Note Name]]` or `[[Note Name|alias]]`, normally without paths or `.md`. Bare wikilinks resolve filenames, not frontmatter `name` or `aliases`. Check filename collisions; shared aliases alone do not make a link ambiguous.

Check collisions using complete filenames or the complete name or alias relevant to the operation. Shared words, first names, or displayed link labels are not collisions: `Jane of Tollen` and `Jane of Talfowen` are distinct. Warn only when the actual link or identity reference could resolve to multiple notes, and identify those candidates. Bare wikilinks resolve filenames; metadata relationships may use names and aliases.

Link sources naturally when useful. Put relevant sources not already linked in prose in a hidden block:

```markdown
%% Sources:
- [[Additional Source Note]]
%%
```

Omit the block when prose already links every relevant source. If the user requests a complete source list, include every source in the block, including those linked in prose.

## 6. Verification

Verify the result in proportion to the change:

- Review all changes made by the task, including added or deleted files, against the pre-edit state. Confirm that only authorized content changed and that pre-existing work was preserved.
- Read changed passages with enough surrounding context to judge meaning and continuity. Re-read the complete file for substantial rewrites, structural changes, or changes whose effects cannot be assessed locally.
- Check affected metadata, tags, special syntax, and links. When frontmatter is created or changed, confirm that it occurs once at the top and parses as YAML.
- Run scoped `git diff --check`. Do not fix unrelated or pre-existing findings; ignore harmless end-of-file-only whitespace differences.
- Reuse reliable checks already completed during the task; repeat them only when later edits or an anomaly invalidate their results.

**Specialized verification:** Follow any applicable workflow’s specific verification requirements. For finalized lint batches, use the lint skill’s **Verify and hand off** procedure and `reviewSummary`, including its rules for anomalies and subsequent edits. Do not repeat checks that finalization has already proved.

## 7. Specialized Workflows

**Linter memory isolation:** Ordinary lint execution and calibration use the live skill, adopted specification, validator, governance files, and vault evidence—not Codex memories, rollout summaries, or prior-run guidance. Historical material is available only when the user explicitly requests history, rationale, maintenance, or regression analysis. Any task changing `linterVersion` must perform the lint skill’s read-only memory audit and surface required memory reconciliation before handoff.

**Session artifacts:** Follow the applicable workflow and its source of truth. Do not normalize generated artifacts, line identifiers, speaker order, or structured data unless required.

**Scripts and plugins:** Follow applicable engineering instructions for `_scripts`, `.scripts`, and `.obsidian/plugins`. Content-writing rules do not replace them; authorization, narrow scope, preservation of unrelated changes, and validation still apply.
