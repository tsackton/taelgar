---
name: lint-cleanup
description: Find Taelgar pages whose existing lint findings concern only names, language, or pronunciation, then guide human-approved cleanup in batches of at most ten. Use for resolving existing name-only lint work without re-linting, not general linting or note rewriting.
---

# Name-only lint cleanup

Resolve existing name findings with the user. This is a bounded cleanup of a recorded report, not a new lint or a claim that the page passes current lint rules. Never invoke the full lint workflow, validator, batch finalizer, or lint agents. Regenerate the header using the stub review's helper after naming approval. Do not update `lintedAt`, `lintVersion`, or `headerVersion`.

## Authority and strict write boundary

Follow vault `AGENTS.md`, except for these user-adopted workflow exceptions: after the user approves resolution of every name-only finding and explicitly chooses deletion after viewing the entire Lint block, remove the existing Lint block and `status/check/lint` without re-linting; regenerate the header; do not add `status/check/ai` for either the name cleanup or any changes made by the header regeneration flow; add Mike/Tim review tags only with direct human confirmation. Preserve any existing `status/check/ai` and every other status tag, including `status/check/name` and `status/stub`.

The complete allowlist for live page edits is:

1. Remove the entire `%%^Lint%%` through its matching `%%^End%%`, only when the original report has no findings other than name issues, all those issues have an approved resolution, and the user explicitly chooses deletion after viewing the entire block.
2. Remove `status/check/lint` under that same condition.
3. Add `status/check/mike` and/or `status/check/tim` only for the reviewer(s) directly confirmed by the user for that page or by an applicable standing instruction.
4. Add an accepted frontmatter `pronunciation` where absent.
5. Create or modify the persistent `Metadata:names:v1` block exactly as approved by the user, including language, pronunciation, status, and any approved subject-specific explanation.
6. Add the hidden reviewer context specified below when adding a confirmed Mike/Tim tag.
7. Replace the generated header using the stub review's live header regeneration helper, as described below.

Do not modify frontmatter `name` or `aliases`, replace/remove an existing frontmatter pronunciation, rename or move files, edit article prose or manually rewrite headers, fix links outside the generated header, normalize unrelated formatting, remove competing review tags, or alter other metadata/comments. If a proposed resolution needs any of those operations, explain the boundary and handle it as a separately authorized task; this skill cannot perform it. A request to rename a form within the names block does not authorize changing the display name or filename.

Read live `../../../_MoC/Name Metadata.md`, the name/pronunciation and report-lifecycle sections of `../../../_MoC/Taelgar Note Linter.md`, `../../../_MoC/Metadata Specification.md`, and `../../../_MoC/Note Categorization.md`. Load relevant `../../../Background/Languages.md` guidance once per language. Consult live authorities and evidence, not historical lint runs or memories. These references supply schemas and name guidance; they do not authorize a full lint or broaden this allowlist.

## Fetch before page work

Use the fetch/push procedure in `../review-stub-staging/SKILL.md`, specifically **Check remote before starting** and **Commit the approved page and offer remote update**, and its **Generate the Obsidian header** procedure. Read those sections; do not inherit its stub completion, prose, filing, review-tag replacement, or optional-lint procedures.

Before candidate research, inspect branch, worktree, index, upstream, and any merge/rebase in progress. Fetch the configured upstream remote and compare fresh upstream with HEAD using `git rev-list --left-right --count HEAD...@{upstream}` (quote the expression in PowerShell). If upstream is missing/ambiguous or fetch fails, report the incomplete check and ask how to proceed. If incoming commits exist, identify branch/upstream and count, and ask before rebasing or beginning page work; existing explicit rebase authorization satisfies this gate. Never silently switch branches, discard changes, stash, resolve conflicts, or force-push. Account for unrelated work before any rebase. If the user declines rebase, obtain direction to proceed locally.

## Select efficiently, then prove eligibility

Choose the requested number, capped at **ten per review batch**. Default to ten; interpret “a few” as three, “a small set” as five, or honor a smaller explicit number. For a request exceeding ten, retain its total and work through successive approved batches of at most ten. With no total, finish one batch and offer another. Return fewer when insufficient eligible pages exist; never pad with mixed findings or broaden the requested scope.

Start with a single cheap filename discovery over existing reports, for example from the vault root:

```powershell
rg -l --glob '*.md' --glob '!.*/*' --glob '!_*/*' --glob '!Worldbuilding/**' --glob '!AGENTS.md' '^%%\^Lint%%\s*$' .
```

Apply any narrower user path/category restrictions. Exclude Worldbuilding and dot/underscore directories, consistent with ordinary lint eligibility. Do not scan all lore or run validators to build the candidate list. Use the resulting report paths as a queue; inspect report sections first, reject mixed reports cheaply, and read each surviving full page only until the requested batch is filled. Honor explicit ordering; otherwise use stable path order. Track rejected, skipped, and completed paths across batches so declined pages do not recur in the same run.

For each candidate:

- Identify exactly one complete, unambiguous Lint block; do not use a regex that consumes another custom block. Skip malformed, duplicate, or ambiguous reports rather than repairing them.
- Read the entire report, including continuations, nested items, editorial assessment, and any legacy structure. Require at least one genuinely open finding. Every error, warning, suggestion, unchecked task, and unresolved action must concern only the subject's names block, name-language attribution, name derivation, or pronunciation. A name word in a link, privacy, coverage, classification, status, or prose finding does not make it a name finding. Underdeveloped assessments or other unresolved work disqualify the page. Applied changes, validated judgments, and informational source links are not open findings, but inspect them for hidden unresolved work.
- Use stable rule IDs as hints, not proof: `metadata.names_*` commonly qualifies, but evaluate its substance and the entire report. Unknown IDs and legacy prose require semantic inspection; ambiguity disqualifies. Do not select a mixed report by ignoring the other findings.
- Read the complete surviving page, its name entries, existing pronunciation, comments, and local diff. Confirm every finding can be resolved within the allowlist. Exclude a page with a conflicting existing frontmatter pronunciation or another required out-of-scope fix; explain why if explicitly selected.

The selection limit applies to eligible pages, not the first ten report matches. Report insufficient results with the search scope and the principal exclusion reasons. Finding discovery authorizes reading only; no page is edited during selection or proposal preparation.

## Propose and obtain decisions

Reuse each report's proposal and the page's existing name metadata rather than recalculating unresolved proposals automatically. Search bounded explicit name/pronunciation evidence and relevant language rules as needed. Preserve documented facts and naming context. Do not infer language from ancestry, residence, spelling, or folder alone; propose `language: unknown` where unsupported. Human confirmation can establish a language without establishing a meaning or etymology.

For missing pronunciation, prefer recorded pronunciation, adopted language rules, documented real-world analogues/naming patterns, then a cautious spelling reading. Explain concrete sounds/stress and uncertainty briefly. Preserve an accepted pronunciation. Do not invent etymology or use pronunciation placeholders. Ordinary obvious names may omit pronunciation under the live name rules; do not impose the stub workflow's mandatory pronunciation.

Select the requested batch, but review one page at a time. Present its numbered review item and wait for its decision before advancing. Include a clickable page link, current finding(s), the page's existing `species` and `ancestry` when known (say unknown/not recorded when absent; do not infer them), proposed complete pronunciation where needed, and name language with evidence/uncertainty. Repeat the complete `Metadata:names:v1` block for that page, including every entry and the full verbatim `notes` values; never replace these notes with a high-level summary, truncate them, or refer the user back to the page. Show the exact proposed block with approved-resolution changes such as `status: documented` visibly represented. Preserve the existing notes verbatim unless proposing an explicit notes edit, in which case show both the full current notes and their full proposed replacements. Clearly label the block as a proposal pending acceptance, not already accepted metadata. Show any new frontmatter pronunciation separately. A queue summary may supplement this individual preview but cannot replace it. State that naming acceptance authorizes name changes and header regeneration while report deletion remains a separate decision; preserve lint completion metadata and any existing AI tag. This is the concrete review preview; do not rewrite the whole page for review.

Ask the user to **accept, change, or skip** this person. Skip leaves the page entirely unchanged and advances the queue. Change returns to a revised exact proposal for acceptance; do not advance while that decision is pending. Acceptance settles only naming and proceeds to report disposition below. If the user explicitly accepts multiple already-previewed pages together, still show each complete report and obtain its separate disposition. Before writing, also ask: **“Should this page get `status/check/mike` or `status/check/tim` for name and pronunciation confirmation, or neither?”** Bundle the reviewer choice with report disposition when convenient. Wait for explicit answers to naming, report disposition, and reviewer choice. Do not infer a reviewer from language, campaign, authorship, acceptance, or silence; do not repeat choices already supplied. Either or both reviewers may be selected.

For each newly added confirmed reviewer tag, add the matching standalone hidden comment below the existing header and before persistent metadata:

```markdown
%% @check/mike : Please confirm name and pronunciation. %%
%% @check/tim : Please confirm name and pronunciation. %%
```

Use only confirmed reviewer lines; these follow the stub workflow's mention syntax. Preserve unrelated existing comments and tags. Avoid duplicating an identical comment. Do not send external notifications or messages. Reviewer confirmation can request a second opinion on accepted values; it does not resolve a still-unaccepted proposal. If the user leaves a name issue unresolved, skip writing that page and retain its report/tag.

When the user modifies a proposal, show the revised exact values/block for acceptance unless their instruction already unambiguously approves those exact edits. Synchronize accepted primary pronunciation with a newly added frontmatter pronunciation, and mark accepted entries `documented` only for facts the user actually established. Preserve other uncertainty and existing documented name context. All original name findings must be resolved before clearing the report; approving only some findings does not authorize clearing any lint state.

## Show the complete Lint block and choose its disposition

Immediately after naming acceptance, repeat the **entire current Lint block verbatim** in a fenced Markdown block, from `%%^Lint%%` through its matching `%%^End%%`. Include its title, applied changes, validated judgments, every finding and continuation, and any DM evidence links or other sections. Never summarize, omit sections, replace it with a link, or show only the name task. Read and show the live report; if it differs materially from the reviewed report, recheck eligibility and approval before continuing.

Then ask: **“Delete this Lint block and remove `status/check/lint`, or preserve both?”** Naming acceptance is not permission to delete the report. Wait for an explicit disposition for this page; never infer deletion from acceptance, silence, reviewer selection, or resolution of its findings. An explicit standing disposition may apply, but still show every full report before deletion.

- **Delete:** after all original name-only findings are resolved and deletion is explicitly confirmed, remove only the displayed report and `status/check/lint`.
- **Preserve:** save the accepted name changes and regenerated header, but leave the complete report byte-for-byte unchanged and retain `status/check/lint`. Do not rewrite findings, check them off, or add a stale-report annotation. Explain in chat that the retained report reflects the prior lint and may still list the now-accepted proposal. Preservation does not cancel approved naming work.

Complete the reviewer choice, save/verify/commit this person's allowed changes, then present the next person. In an explicitly requested preview-only or skill-testing run, show the decisions but do not save or commit pages; continue the simulated flow only when the user supplies its relevant decisions. Approval of a skill edit never approves a person's name or report deletion.

## Regenerate the header

After the naming proposal, report disposition, and reviewer choice are settled, prepare a temporary candidate inside the vault with the intended filename unchanged and only the approved cleanup edits. Use the stub review's helper on that candidate; the default prints the regenerated complete candidate without writing:

```powershell
python -X utf8 .agents/skills/review-stub-staging/scripts/regenerate_header.py "PATH/TO/CANDIDATE.md"
```

This runs the live `OutputHandler.generateHeader(..., true)` with current vault metadata and campaign registry. Use existing `pageTargetDate` when present, otherwise the configured Taelgar Calendarium date, with `1750-01-01` as the helper's fallback. Do not substitute a real-world/session date, ask for a display date, or add date metadata. Preserve existing `headerVersion`; do not add or change it as part of this cleanup. Use `--date` only for an explicitly requested preview override.

Inspect the generated title, pronunciation line, information callout, and any generated dynamic views or campaign interactions. Show the resulting header in chat; naming approval includes this routine generated refresh, so no separate approval is needed unless it exposes a material unexpected change. Preserve article text, other comments, embeds, and persistent blocks. On an unfamiliar header, helper failure, ambiguous link, or changes beyond the generated header, stop that page's save and report the issue rather than broadening replacement boundaries or silently saving without regeneration. Save the verified regenerated candidate after the ordinary live-content check. Header regeneration adds no `status/check/ai`, and it never removes an existing AI tag.

## Apply, verify, commit, and offer push

Before every write, recheck the branch and compare the live page with the reviewed snapshot. If concurrent changes affect the report, eligibility, or proposed values, re-evaluate and obtain renewed approval for material changes. Never overwrite unrelated edits. Apply only the accepted allowlist changes to approved pages; pending or skipped pages remain untouched.

Read every changed page completely. Parse its top frontmatter and the names-block YAML without running a note linter. Check accepted values, allowed tag additions/removal, one correct names block, preserved lint timestamps/version, and the chosen report disposition: exact removal of only the eligible Lint block and lint tag, or byte-for-byte preservation of the complete block and retention of its lint tag. Verify the header matches the helper output and displays the accepted pronunciation. Compare before/after text and the full scoped diff to prove article, other comments/metadata, file path, and existing non-lint status tags are unchanged, except for the explicitly allowed reviewer additions/context. Header changes must be limited to the regeneration flow; preserve existing `status/check/ai` and prove none was added. Run scoped `git diff --check`; do not fix unrelated existing whitespace. Never describe this verification as re-linting or a newly clean lint.

As in the stub workflow, commit each approved and verified page locally without another commit confirmation. Recheck branch before staging/committing; isolate this workflow's hunks from pre-existing changes and staged work. Commit only that page's approved cleanup, not other notes, skills, or previous local edits. Use a message such as `Resolve name lint for <Name>`. If safe hunk isolation is unavailable, ask for a preservation plan rather than committing unrelated work. Inspect the resulting commit scope.

After the page commits (one remote offer may cover the approved batch), ask before pushing unless applicable standing authorization exists. Identify the remote URL/branch, cleanup commit(s), and **all other unpushed commits** that the push would publish. On approval, fetch again; if upstream has incoming commits, rebase onto it before pushing, never merge or force-push. Remote-update approval authorizes the necessary rebase subject to preserving local work. Reverify pages and commit scope after rebase; material changes require renewed proposal approval. Stop on conflicts/failure and report recoverable state. After a concurrent push rejection, fetch/rebase and retry once; stop after a second rejection.

Report approved page links, accepted name/language/pronunciation changes, regenerated headers, reviewer additions, lint report/tag deletion or preservation, commit hashes, and push outcome or pending decision. Explicitly say **no re-lint was run**. Continue an explicitly requested larger queue in the next batch; otherwise offer another batch.
