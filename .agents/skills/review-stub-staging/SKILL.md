---
name: review-stub-staging
description: Collaboratively fill in a Taelgar person stub or Staging page from vault evidence and human corrections, establish required identity metadata and pronunciation, present the complete page for approval, choose review tags, retire stub status, and file approved Staging pages. Use for initial base-page completion, not automatic linting or broad note cleanup.
---

# Review Stub or Staging Page

Work one page at a time with the user. Produce a concise, correct reference page with enough visible information for a meaningful contextual lint. A short identifying paragraph may be sufficient; do not pad sparse evidence into a campaign recap.

## Scope and authorities

Follow the vault's `AGENTS.md`, source hierarchy, Git procedure, and preservation rules. This workflow carries the user's explicitly adopted exceptions for completed pages: remove `status/stub`, apply the selected review disposition, and move a page out of Staging. Do not apply those exceptions before approval or outside the selected page.

Read `../../../_MoC/Note Categorization.md` and `../../../_MoC/Metadata Specification.md` before changing metadata. For name work, read `../../../_MoC/Name Metadata.md`, the names-and-pronunciation section of `../../../_MoC/Taelgar Note Linter.md`, and relevant guidance in `../../../Background/Languages.md`. Use `../lint-taelgar-note/SKILL.md` only for the applicable name rules or a separately authorized full lint. Consult live authorities, not historical lint guidance or Codex memories.

This workflow does not itself run a full lint, write lint completion state, or require lint's batch agents. The name review below is a bounded application of its name-resolution rules, including for Staging evidence; it is not a full lint of a Worldbuilding page.

## Check remote before starting

Before researching or editing a page, inspect the branch, working tree, index, and configured upstream. Check for an in-progress merge or rebase. Fetch the upstream remote and compare local HEAD with the freshly fetched upstream (`git rev-list --left-right --count HEAD...@{upstream}`, quoting the upstream expression appropriately for the shell). Do not treat stale tracking refs as proof that the remote is unchanged. If fetch fails or the upstream is missing or ambiguous, report that the remote check is incomplete and ask how to proceed; never select a remote or branch silently.

If the upstream has commits absent locally, warn the user and ask whether rebasing onto the named upstream is okay **before starting page work**. Show the branch/upstream and incoming commit count. Wait for approval; a standing explicit rebase authorization satisfies this gate. If the user declines, ask whether to proceed locally without updating, and explain that an eventual push will require rebasing. If approved, rebase onto the fetched upstream, then inspect the updated page and restart evidence gathering from that state.

Before rebasing, account for all local changes and staged work. Never discard, reset, or silently stash unrelated work. If a dirty checkout prevents rebase, explain the affected paths and request a preservation plan; any stash must be explicitly authorized and restored with its outcome checked. On conflicts or other Git failures, stop dependent work, preserve the recoverable state, report the affected paths and error, and ask how to proceed. Do not automatically choose conflict sides, skip commits, abort a user's operation, or force-push.

## Select, research, and draft

1. Resolve the user's selected page or queue. When asked to pick, choose a person with `status/stub` in the requested folder or a person in `Worldbuilding/Staging`, respecting the user's order and already-completed exclusions. Prefer pages without a valid `lintedAt`/`lintVersion` pair. If a candidate is already linted, suggest skipping it and choosing an unlinted page; a completed lint usually indicates that this initial-base-page workflow is not the best next step. This is a recommendation, not an exclusion: if the user explicitly selects that page or wants to proceed, continue without automatically running or clearing a lint. Do not treat every note in a folder as authorized for writing.
2. Read the entire existing page, including YAML, comments, persistent metadata, and any Lint block. Inspect existing local changes. Search filenames, name and aliases, variants, backlinks, and the applicable finalized session sources. Read source passages in context; repeated generated artifacts are not independent evidence.
3. Draft a useful identity and defining role or relationships, with only brief relevant played events. Link the actual source or subject notes, checking filename collisions. Use `[[Heroes of Cleenseau]]` rather than an unexplained “the party” in Cleenseau reference prose. The user's corrections can establish facts; record a precise hidden comment when they resolve conflicting sources. Do not expose private DM material without direction.
4. Review existing `%%` comments as part of drafting. Remove obsolete reminders, superseded shorthand, and source excerpts or fact notes whose useful content is now captured by the approved article or linked source. Do not replace a removed comment with a new “superseded” comment merely to preserve history; Git retains it. Preserve comments containing still-relevant uncertainty, conflicts, source limitations, private context, characterization, or distinct facts absent from the article. If only part is redundant, retain the useful remainder without strengthening its meaning. Carry useful source attribution forward through natural links or the vault's hidden source conventions before removing a duplicated excerpt. Show these removals in the complete-note preview and briefly identify them in chat; full-note approval authorizes the scoped cleanup. When relevance is unclear, ask rather than deleting silently. Preserve unrelated prose, special syntax, generated structures, Campaign blocks, and persistent metadata; they are not disposable comments merely because they use `%%` delimiters. Preserve old Lint blocks and completion metadata unless the user explicitly requests removal or an authorized full re-lint replaces them; explain stale findings in chat rather than silently declaring them resolved.

## Discuss and approve the core prose first

Before generating pronunciation, identity metadata, or a header, present the proposed core sentences as readable prose in chat, using paragraphs or a blockquote rather than a full Markdown-file code block. Separately identify the actual sources with clickable links and briefly explain why each sentence belongs: what establishes the identity, defining relationship or role, and any selected event. Identify uncertainty, conflicting accounts, and the user's adopted corrections. Keep this evidence and editorial reasoning in the conversation, not in the page's article. Ordinary useful wikilinks and required hidden source/conflict comments remain governed by the vault conventions.

If the search finds no usable information to fill the page, say so plainly, describe the bounded search scope, and ask the user what the page should say. Do not manufacture an identifying paragraph from a filename or pad metadata into apparent lore. Human-supplied facts can support the draft.

Discuss the proposed prose with the user and ask for additional facts, corrections, or clarifications that matter to the page. Incorporate those answers while preserving factual boundaries. Once the wording is settled, present the **final core article text** as a clearly separated readable text block in chat and ask for explicit approval. Do not proceed to pronunciation proposals, metadata generation, or header generation until the core text is approved. Core-text approval does not authorize saving the note; complete-note approval and review-tag selection still follow.

After core approval, perform the identity, pronunciation, and header steps below, then present the complete note. Keep the approved article unchanged during technical preparation. If metadata research reveals a substantive prose issue, return to the readable prose discussion and approval before presenting the complete note. Preserve choices already settled for this page rather than asking the user to repeat them.

## Required person identity and pronunciation

The visible article must identify the person and provide at least one supported defining role, relationship, or fact beyond the generated header or portrait, so the linter has substantive authored prose to review. This is a readiness check, not a claim that a full lint will be clean. Before calling the page complete, establish:

- `species`;
- `ancestry` for a human, using the vault's supported cultural classification;
- supported gender/pronoun metadata, following the rule below;
- `name`;
- an actual accepted `pronunciation` in frontmatter;
- a matching primary `Metadata:names:v1` entry under the live name specification.

Also supply required category metadata such as supported `knownTo` values (use `[]` when no campaign knowledge is known). Do not infer ancestry or language solely from a folder, residence, or spelling. Ask for missing identity facts when sources cannot establish them. If the user explicitly says a fact is unknown, represent that uncertainty according to the metadata specification; never fabricate a value to satisfy the checklist.

The vault prefers `gender` with header-derived default pronouns; add `pronouns` only when the intended pronouns differ from those defaults or need an explicit override. Preserve existing explicit choices. Under this user-adopted workflow, infer `gender: female` from established she/her and `gender: male` from established he/him when the text gives pronouns but no explicit gender; briefly identify that inference in chat and include it in the complete-note preview for human correction. Explicit gender takes precedence over a pronoun-based inference. For other or mixed pronouns, preserve the established pronouns and ask the user for the intended gender value rather than treating them as proof of a particular gender. Do not infer gender or pronouns from a name, portrait, role, species, or other non-gender/non-pronoun clues. If the text establishes neither gender nor pronouns, ask the user. Verify the generated header displays the intended pronouns in the full-note preview; inferred `gender: female` normally generates `(she/her)` without a redundant `pronouns` field.

When pronunciation is absent, perform only the linter's contextual name-review subpart:

1. Inspect existing frontmatter and name entries. Preserve accepted/documented values and existing unresolved proposals; do not automatically recalculate them. Surface conflicts for human resolution.
2. Search explicit recorded pronunciations and adopted language rules first, then documented naming patterns and real-world analogues in `Languages`. Use a cautious spelling-based reading only when stronger guidance is unavailable. Explain concrete sound and stress choices and uncertainty briefly.
3. Present a pronounceable proposal for the complete name and help the user accept or revise it. In the draft name block, retain an unaccepted proposal as `status: proposed` with its derivation in `notes`; do not silently put it in accepted frontmatter.
4. After human acceptance, put the accepted pronunciation in frontmatter and synchronize the name entry as `status: documented`. Preserve established meanings and derivations; use `language: unknown` when unsupported. Do not invent etymology.

Unlike ordinary lint's optional pronunciation exemption for obvious names, this completion workflow asks the user to establish an explicit pronunciation even for an ordinary name. Never use placeholders such as `obvious` or `inherited from` as a pronunciation. If the user declines or essential evidence is missing, explain the remaining gap and keep the page in review rather than claiming completion or removing stub status prematurely.

## Generate the Obsidian header

After settling identity metadata, generate the header before the complete-page preview. Use the Python entry point, which runs the live JavaScript `OutputHandler.generateHeader(..., true)` used by `_scripts/templater/regenerateHeader.js`, with the vault's current metadata and campaign registry:

```powershell
python -X utf8 .agents/skills/review-stub-staging/scripts/regenerate_header.py "PATH/TO/CANDIDATE.md" --date YYYY-MM-DD
```

The default prints the entire candidate without writing. Run it on a temporary draft inside the vault when the proposed metadata differs from the current page; do not save unapproved prose to the live target just to generate a preview. Pass the intended filename unchanged so name fallback is correct. Supply the agreed in-world display date, or omit `--date` only when `pageTargetDate` already supplies it. Never substitute the real-world date or guess a campaign date. The adapter excludes dot directories and refuses ambiguous filename links.

Include the generated title, pronunciation line, information callout, dynamic views, and campaign interactions in the full-page preview. Preserve an existing `headerVersion`; the helper deliberately regenerates only the header, rather than rewriting version metadata. For a page lacking `headerVersion`, supply the current template value in the draft. The helper preserves the remaining article, comments, embeds, and persistent blocks. Inspect an unfamiliar header manually rather than widening replacement boundaries.

After approval and tag selection, save the reviewed candidate. `--write` is available to regenerate a live header only within authorized scope; if regeneration materially changes the approved preview, obtain approval of the new complete text before saving it. Do not hand-author a substitute header or port only a subset of name/token/campaign rules.

## Full-page approval, tags, and filing

After the readable core text has been approved and identity metadata, pronunciation, and header generation are complete, show the **complete proposed Markdown file** to the user: YAML, title/header, approved article, embeds, comments, name block, and any retained Lint block. Use a fenced code block with enough backticks to preserve embedded fences. This is the second approval stage; do not substitute the earlier readable prose block, a summary, diff, or file link for the complete text.

For a Staging page, show the exact proposed destination alongside the preview. Select the appropriate existing canonical directory using species, human ancestry, similar notes, and directory instructions. Keep the filename unchanged. If classification or destination is ambiguous, settle it with the user before saving or moving. A page outside `Worldbuilding/Staging` stays at its current path.

After the user approves the complete text, ask: **“Which review tag should this page have: ai, mike, tim, or none? Would you like a lint after completion?”** These are required workflow choices; wait for an answer before saving. Do not re-ask a choice the user has already explicitly supplied for this page or as a standing instruction. If the text changes materially, present the revised complete file for approval again.

Apply the chosen disposition:

- `ai` → `status/check/ai`;
- `mike` → `status/check/mike`;
- `tim` → `status/check/tim`;
- `none` → none of those three tags.

Treat the choice as replacement of the ai/mike/tim review disposition: remove competing tags from that set, preserving all other tags, including `status/check/lint`, `status/check/name`, and unrelated human review states. “None” does not clear independently managed lint or name state. Do not add `status/check/ai` when the user chooses mike, tim, or none. Always remove `status/stub` from the approved completed page, regardless of the chosen review tag or whether the user wants a lint. Do not change other non-check status tags.

After the answers, apply only the approved full text plus these agreed tag changes and, if applicable, the approved Staging move. Recheck the branch and target's live contents before writing; reconcile any concurrent edit instead of overwriting it. Check the resolved source and destination paths stay inside the vault and never overwrite an existing destination. Move using path-safe native operations, preserving the filename and checking affected path-qualified references. Ordinary bare wikilinks need no change. If required link updates expand beyond the reviewed scope, show those changes for approval first.

## Verification and optional lint

Read the final file completely, validate YAML and edited identity fields/name-block structure, check links and tags, and inspect the complete scoped diff (including the destination for a move). Run scoped `git diff --check`. Confirm no unrelated files changed.

If the user requested lint, hand the final canonical path to `lint-taelgar-note` and follow its full workflow. For a page with existing valid lint completion metadata, ask specifically about **re-lint** unless the user's choice already explicitly authorized re-linting. Staging must be filed before a full lint because Worldbuilding paths are ineligible. Full lint may independently add or clear `status/check/lint`; it must not override the selected ai/mike/tim disposition. Do not claim partial name review is a completed lint.

## Commit the approved page and offer remote update

After full-page approval, review-tag selection, saving, verification, and any requested lint, commit the completed page automatically as part of this workflow. No additional commit confirmation is needed. Recheck the branch immediately before staging and committing. Review both staged and unstaged diffs; preserve any pre-existing edits and staged work. Commit only the reviewed page's approved changes. For a Staging move, include both its source deletion and destination addition as one logical page, preserving the filename. Do not include other notes or skill files. If approved link repairs involve additional files, obtain an explicit exception to the single-page commit scope first.

Use a clear message such as `Complete Corrin Merriweather base page` or `Complete and file <Name> from Staging`. Check that the resulting commit contains exactly the intended paths and changes. If unrelated work is staged, isolate the approved paths with a scoped commit rather than including the whole index. If the page itself contains pre-existing changes outside the approval, separate those hunks or ask for scope clarification; never silently commit them.

After the local commit, ask whether the user wants to update the named remote branch. Identify the exact remote URL, branch, page commit, and any other unpushed commits that a push would publish so approval covers the actual destination and payload. Do not push without an explicit yes or applicable standing authorization. Declining the remote update leaves the local commit intact and permits moving to the next page.

When the user approves updating remote, fetch again immediately before pushing. If the fetched upstream contains commits absent locally, **always rebase onto it before pushing**, including when the branches have diverged; never merge remote changes or force-push as a substitute. Approval of the remote-update workflow authorizes this necessary rebase, subject to preserving local changes as above. Reverify the completed page and commit scope after rebase; material content changes require renewed full-page approval. If rebase or push fails, or conflicts or concurrent edits appear, stop the update, preserve the state, report the concrete issue, and ask how to proceed. If a concurrent remote update rejects the push, fetch and follow the same rebase procedure; stop after a second rejection rather than entering an unbounded retry loop.

Report the saved path, selected review disposition, stub removal, any move, lint outcome, commit hash, and remote update outcome or pending choice. Then continue the user's review queue by presenting the next candidate; do not save that candidate without its own approval.
