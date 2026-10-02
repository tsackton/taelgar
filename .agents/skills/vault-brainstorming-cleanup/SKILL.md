---
name: vault-brainstorming-cleanup
description: Find substantial noncanonical idea passages and related Taelgar brainstorming notes, then propose and carry out approved extraction, organization, consolidation, or retirement. Use for vault brainstorming cleanup, not ordinary note linting or canon development.
---

# Vault Brainstorming Cleanup

Organize Taelgar's reusable ideas without treating them as canon. Follow the vault `AGENTS.md` and the current `Worldbuilding/Purpose of Worldbuilding.md`. A request to find cleanup opportunities authorizes discovery, not a vault-wide rewrite or deletion. Work in reviewable batches.

## Discover and classify

Agree on a topic, folder, or bounded batch when the request does not specify one. For a vault-wide request, inventory broadly but propose a small coherent first batch before editing. Search filenames, names, aliases, backlinks, and relevant prose. Read each candidate note in full, including frontmatter and comments, plus likely related canonical notes, Brainstorming, Talk, Tentative, Old Documents, and source records. Check the Git branch and working tree before any edit and preserve existing changes.

Look for long passages of exploratory ideas, alternatives, rejected possibilities, or undeveloped proposals in ordinary prose, `%%` comments, and shared private blocks. Keep relatively short, focused speculation with its subject, even when it is in a comment or could fit on a brainstorming page. Passage length alone does not justify extraction; move material when it overwhelms the host note or addresses a different subject. An off-topic list may merit moving even when it is shorter. Classify each passage by meaning, not by markers or keywords alone:

- **Reusable brainstorming:** Possible future setting content with no established adoption. Route to an existing topical page under `Worldbuilding/Brainstorming`, or propose a new topical page there.
- **Uncertain subject:** A candidate entity whose existence or identity remains unsettled. Consider `Worldbuilding/Tentative` under its documented criteria, rather than making it a canonical page.
- **Decision history or open questions:** Reasoning about a topic, including rejected proposals worth remembering. Consider the relevant `Worldbuilding/Talk` page.
- **Obsolete or duplicate idea:** Propose retirement only when the exact content is already preserved, explicitly abandoned, or has no remaining value the user wishes to retain. Noncanonical status alone is not a reason to delete: all Brainstorming content is noncanonical.
- **Keep in place:** Short, targeted speculation; DM guidance; campaign or session records; primary sources; quotations; mechanical notes; source attribution; structured `Metadata:*` or `povNotes:v1` blocks; `Lint` blocks; and comments needed to interpret the host note. These are not automatically movable brainstorming, even when hidden or speculative.

Do not promote ideas to canonical prose. Distinguish a user's explicit adoption from repetition, polished wording, an AI summary, or appearance in a brainstorming page. Treat `_DM_` as local private material and `_dm_notes` or `%%^Campaign:none%%` as nonpublic; never copy their secrets into a shared brainstorming note or review artifact. Read source artifacts for evidence but do not edit or retire them through this workflow unless the user explicitly includes them and the applicable source workflow permits it.

## Preview the batch

Before an interpretive change, give the user a compact table with each source path and passage, the proposed destination or surviving page, the action (extract, merge, retain, or retire), the reason, and any uncertain canon, privacy, or link question. Name every file to be created, edited, moved, or deleted. Show the intended organization of a consolidation, identify repeated versus distinct ideas, and flag contradictions or variants for separate retention. Quote only enough material for a decision and keep private content out of shared artifacts. Obtain explicit approval for this concrete batch. Approval of one batch does not authorize new candidates or a materially larger edit.

If deletion is proposed, state exactly what text or file would be removed and where any unique useful content would remain. When an idea is merely noncanonical or its future value is uncertain, offer retention or a Talk record instead of presuming deletion. Never delete a source note, campaign record, or unique authored text simply because a later summary exists. Do not rename existing notes; if an existing page's title is poor, retain its filename and propose an allowed metadata `name` change separately.

## Apply an approved batch

Reread the approved files and verify that the branch, working tree, source passages, and destination content still match the preview. Read `Note Categorization`, `Metadata Specification`, and the relevant template before creating or changing note metadata. Use the smallest edits that complete the approved operations.

Move an approved passage by preserving its meaning, uncertainty, distinctions, and useful provenance in the destination, then removing only the approved source passage. Keep the destination visibly noncanonical in its Worldbuilding context. Do not silently turn a tentative statement into a fact or smooth over conflicting alternatives. Prefer one topical destination when ideas genuinely overlap; keep distinct topics or incompatible proposals separate. Avoid pasting the same passage into multiple notes. Preserve source links where useful, and check incoming wikilinks, embeds, heading links, and filename collisions before retiring a page. Update only links required by the approved change. A source note may need a short remaining pointer when removing the passage would otherwise obscure why a topic is mentioned, but include that in the preview.

Apply the vault's `status/check/ai` rule to created or edited content notes, including Worldbuilding notes, without changing any other status tag. Respect the no-tags exception for `Worldbuilding/Agentic Review`. Do not touch generated or special blocks outside the approved passage. If investigation reveals mixed private material, a canonical conflict, a new dependency, or a larger scope, pause that item and give an updated preview; continue independent approved items where safe.

## Verify and report

Read every changed note in full. Check YAML, edited metadata and tags, special syntax, destination paths, wikilinks and backlinks, and that all approved unique content survived with its uncertainty intact. Review the complete diff and run scoped `git diff --check`. Report the extracted and consolidated ideas, retained material, any retired text or pages, and unresolved decisions. Distinguish applied changes from proposals left for later review.
