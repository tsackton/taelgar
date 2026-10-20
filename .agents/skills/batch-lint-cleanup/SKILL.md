---
name: batch-lint-cleanup
description: Resolve existing name-only Taelgar lint through a visible batch review document, language guesses for human adoption, and selective row regeneration. Use for low-typing batch approval; lint-cleanup remains the sequential chat workflow. Does not re-lint.
---

# Batch name-only lint cleanup

Prepare ten eligible notes by default, present their proposals and complete original lint reports together, and accept one short batch decision. Keep the existing `lint-cleanup` skill unchanged. Do not invoke lint agents, validators, or finalizers: this resolves recorded findings, not a new lint.

## Authority and boundaries

Read live `../../../_MoC/Name Metadata.md`, the naming and report-lifecycle sections of `../../../_MoC/Taelgar Note Linter.md`, `../../../_MoC/Metadata Specification.md`, and `../../../_MoC/Note Categorization.md`. Use relevant `../../../Background/Languages.md` guidance and bounded vault evidence, not historical lint runs or Codex memories.

User-adopted workflow exceptions:

- Guess unknown languages in proposals, explicitly labeled for human adoption. This overrides the ordinary no-guessing rule only during proposal preparation; no guess is saved before acceptance.
- After showing every complete original Lint block, explicit batch acceptance authorizes deletion of approved, fully resolved name-only reports and `status/check/lint`, without a separate disposition question or re-lint.
- Add no `status/check/ai` for this cleanup or header regeneration. Preserve existing AI and other status tags except approved lint removal and requested reviewer additions.
- Commit an approved subset together instead of one note at a time.

Live-note changes are limited to: adding accepted frontmatter pronunciation where absent; approved names-block edits; eligible report/lint-tag removal; explicitly requested Mike/Tim review tags and context comments; and helper-generated headers. Preserve established naming context and unrelated entries. Never change frontmatter `name`, `aliases`, existing pronunciation, `lintedAt`, `lintVersion`, or `headerVersion`; rename/move files; edit article prose; normalize unrelated formatting; repair unrelated links; or remove other status tags. Required out-of-scope changes need separate authorization. Setting up this skill or preparing a review does not approve note changes.

## Start and select

Read and follow **Check remote before starting** in `../review-stub-staging/SKILL.md`: inspect branch, worktree, index, upstream, and merge/rebase state; fetch and compare fresh upstream before page research. Ask how to proceed if upstream/fetch is unavailable or incoming commits require rebase approval. Never silently switch branches, stash, discard changes, or resolve conflicts. Do not inherit that skill's prose, filing, or stub procedures.

Honor requested scope and smaller counts; split larger totals into successive batches of at most ten. With no total, finish one batch and offer another. Discover report paths cheaply, then inspect reports before full notes:

```sh
rg -l --glob '*.md' --glob '!.*/*' --glob '!_*/*' --glob '!Worldbuilding/**' --glob '!AGENTS.md' '^%%\^Lint%%\s*$' .
```

Use stable path order unless directed otherwise. Exclude Worldbuilding and dot/underscore directories. Track rejected, skipped, and completed paths across batches. Do not scan all lore or run validators for selection.

Require exactly one complete, unambiguous report and at least one genuinely open finding. Read its entire contents, including continuations, nested tasks, editorial assessments, and legacy sections. Every unresolved error, warning, suggestion, or action must concern the subject's names block, language, derivation, or pronunciation. Rule IDs are hints, not proof. Mixed findings, other underdeveloped work, ambiguous reports, and required edits outside the allowlist disqualify a note. Applied changes and informational sources alone do not. Read each surviving full note and local diff until the eligible batch is filled. Explain explicit-note exclusions and insufficient results without broadening scope.

Capture full-note and exact-report baselines. Assign stable row numbers: never renumber or reuse them after skips, regeneration, or partial application.

## Propose

Reuse existing proposals unless regeneration is requested or an unknown language needs a default. Preserve documented language, pronunciation, meaning, derivation, naming circumstances, and uncertainty. Show recorded species/ancestry for people; do not infer them.

For unknown language, consider explicit name context first, then culture, geography, spelling, and adopted language guidance together. Label a plausible default **guess**, with a brief concrete basis and uncertainty. Ancestry/residence alone is not proof. Use `unknown` where no useful basis exists. Acceptance can establish a language choice without establishing a meaning or etymology.

Pronunciation preference: recorded pronunciation, adopted language rules, documented analogue/naming patterns, then cautious spelling reading. Apply relevant analogues instead of silently falling back to English. Show complete pronounceable forms with stress and brief reasoning. Preserve existing frontmatter pronunciation. Obvious ordinary names may omit it; never use placeholders. A changed language must not silently change pronunciation.

Determine exact candidate edits internally without displaying replacement names blocks. Expose every substantive decision in the table or row details, including contextual-note edits, meanings, derivations, and status changes. Preserve existing notes verbatim unless a change is explicitly shown and approved. Mark only established or human-adopted facts documented; retain other inference/uncertainty. Generic acceptance cannot resolve an undisclosed substantive conflict.

## Review document

Create a unique Markdown file under `Worldbuilding/Agentic Review/Name Cleanup/`, such as `2026-10-20-batch-01.md`. Keep it for review/resumption; do not overwrite another run or commit it with cleanup notes. No YAML tags or applied inline tags; literal tag strings inside quoted evidence are review content.

Include:

1. Batch identity/revision and this prominent approval legend: **Accepting a row adopts the displayed naming decisions, deletes its appended Lint block and lint tag by default, adds no reviewer tags unless requested, regenerates the header, and includes it in a local batch commit. No re-lint is run.** Explain `preserve` and `redo` here.
2. A numbered table with state, clickable note link, identifying context (recorded species/ancestry for people), language, pronunciation, and concise basis/uncertainty. Display nondefault reviewer/report dispositions. Detail multiple name forms beneath the table when necessary; never hide extra decisions.
3. Only necessary row-specific details, including explicit proposed changes to existing contextual notes. No names-block dumps.
4. **Every full original Lint block**, under a heading matching its row number and linked note. Copy verbatim from `%%^Lint%%` through its matching `%%^End%%`, including all assessments, applied changes, findings, continuations, and source sections. Use Markdown fences longer than any fence within the report. Never summarize, truncate, or substitute a link.

Automatically open the review with `open_in_codex` and provide an absolute clickable file link. If opening is unavailable or fails, show the table and all full reports in chat before approval. A link alone is insufficient. Explicit approval after presentation suffices; do not ask for a separate reading acknowledgment. Keep private evidence local, not in a shared Page or external publication.

Update the same open document for revisions, increment its revision, and summarize changed rows. Preserve original displayed reports as audit evidence after application, clearly labeled original rather than current. On resumption, reread the document and live notes; do not infer past approval solely from a row label without reliable conversation evidence.

## Commands

Interpret natural language and these short forms:

| Reply | Effect |
| --- | --- |
| `all` | Approve all pending displayed rows with visible defaults. |
| `all except 3, 7` | Approve others; leave 3 and 7 pending and untouched. |
| `skip 3` | Leave untouched and exclude from this run. |
| `5 Dwarvish` | Adopt that exact language correction and approve row 5's other displayed decisions/defaults. |
| `7 mike`, `7 both`, `7 neither` | Set reviewers; alone does not approve naming/deletion. |
| `preserve 4` | Retain report/tag; alone does not approve naming. |
| `redo 3, 7` | Fresh proposals for just those rows; no application. |
| `redo language 4–6` | Reconsider only those language fields. |
| `redo pronunciation 2; more Elvish` | Reconsider only that pronunciation with the guidance. |
| `approve rest; redo 3, 7` | Apply other pending rows; regenerate 3 and 7 and leave pending. |
| `all except 3; 5 Elvish; 7 mike` | Approve others with the explicit correction and reviewer override. |

Parse the entire reply before acting. Exceptions, skips, regeneration, and explicit field overrides outrank broad approval. Do not guess ambiguous/nonexistent row references; continue unambiguously approved rows. A bare `redo` needs row selection. `all` never resurrects skipped/applied rows or overrides regeneration in the same reply.

Regenerate only requested rows/fields, preserve other decisions, and require acceptance after showing revised proposals. Field-limited regeneration must flag dependent inconsistencies and propose any coupled change explicitly. Never overwrite accepted frontmatter values or regenerate applied rows; corrections to applied rows are separate tasks. Exact user corrections need no redundant confirmation; newly derived dependent values do. Unaffected approvals remain valid.

## Apply and verify

Before each write, recheck branch and compare live content with the reviewed baseline. Reread and display any changed report and obtain renewed deletion approval; never delete an unseen replacement. Material proposal-input changes need renewed row approval. Preserve unrelated concurrent edits and continue unaffected rows.

Apply only when every original finding has an accepted resolution. Default deletion removes exactly the reviewed report and lint tag. `preserve` retains both byte-for-byte, even if they describe now-resolved proposals; explain that in chat. For requested reviewers, add only their tags and corresponding standalone comments below the header and before persistent metadata, without duplication:

```markdown
%% @check/mike : Please confirm name and pronunciation. %%
%% @check/tim : Please confirm name and pronunciation. %%
```

Create a temporary candidate in a dot directory inside the vault, retaining the intended filename. Regenerate using:

```sh
python -X utf8 .agents/skills/review-stub-staging/scripts/regenerate_header.py "PATH/TO/CANDIDATE.md"
```

The default prints the complete candidate; use that output. Preserve `headerVersion`, including absence. Use existing `pageTargetDate`, otherwise the helper's Calendarium date/fallback; add no date metadata and never substitute real-world/session dates. Inspect title, pronunciation, callout, dynamic views, and campaign interactions. Routine refresh is approved with the row; show material unexpected changes for approval. Hold a row on helper failure or ambiguous boundaries rather than saving without regeneration. Add no AI tag.

Read each changed note completely. Parse its single top frontmatter and names-block YAML without linting. Check approved values, primary pronunciation synchronization, one correct names block, report disposition, allowed tags/comments, unchanged lint completion/version metadata, and header equality to helper output. Compare full before/after changes to prove preservation outside scope. Run scoped `git diff --check`; preserve intentional hard breaks and ignore unrelated findings.

## Commit and hand off

Commit each approved, verified application subset together, e.g. `Resolve name-only lint for 8 notes`. Recheck branch immediately before staging/committing. Isolate task hunks from unrelated local/staged work; ask for a preservation plan if safe isolation is unavailable. Verify commit scope. Include no review artifacts, skill files, or unrelated notes. Record commit hashes on applied rows; keep pending/skipped states visible.

For optional push, read **Commit the approved page and offer remote update** in `../review-stub-staging/SKILL.md`, adapting page scope to this subset. Disclose remote URL/branch and all unpushed commits, obtain push authorization, fetch again, rebase only under its authorization/preservation rules, and reverify. Stop on conflicts or a second concurrent rejection; never merge or force-push as a shortcut.

Report the review link, applied/skipped/pending counts, accepted changes/reviewers, report deletion/preservation, commit hash, and push state. State **no re-lint was run**. Offer another batch or continue an already requested larger total. Do not repeat decisions covered by the batch reply.
