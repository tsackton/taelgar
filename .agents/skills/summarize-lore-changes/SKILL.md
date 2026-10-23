---
name: summarize-lore-changes
description: Summarize meaningful lore and campaign-content changes in the Taelgar vault over a date or revision range, optionally by contributor. Quote small changes and identify substantial page rewrites; exclude lint, metadata, and header maintenance unless they change the lore.
---

# Summarize Lore Changes

Produce a concise, evidence-backed account of what changed in the setting or campaign record. This is a read-only history review, not a lint, editorial review, or request to improve the notes. Follow the vault's `AGENTS.md`; return the summary in chat unless the user requests a saved artifact.

## Establish the history scope

- Resolve the vault checkout, requested period or revision range, and any contributor filter from the request and conversation. Ask only when an essential scope cannot be inferred.
- Interpret "last N days" as a rolling interval unless the user specifies calendar days. Use the user's timezone, compute an explicit start and end, and state the dates in the summary. Git commit dates are real-world dates; dates inside notes are in-world chronology.
- Inspect the checkout state and latest available history without changing branches or touching local edits. Use committed changes by default; include uncommitted work only when requested, labeled separately and without inferring its author.
- Resolve a contributor's account name to Git author names/emails using available evidence. Match authors, not merely committers or the repository owner. Include known author identities and avoid similarly named contributors. Disclose unresolved identity or missing-history limitations.
- Use local Git history first. If the requested history is unavailable, obtain it through available read-only sources or report the gap; do not imply remote freshness without checking it.

## Review changes efficiently

Start with a scoped commit list and file statistics, then inspect the actual patches. Commit titles are triage hints: a "cleanup" commit can change lore, and a lore-related title can contain only maintenance.

Useful Git operations, with placeholders replaced by the resolved scope:

```text
git log --since=<start> --until=<end> --format="%H %aI %an <%ae> %s"
git show --format=fuller --stat <commit>
git diff <commit>^ <commit> -- <note-path>
git show <commit>:<note-path>
```

Apply an author filter when requested. For merge commits, inspect the parents and avoid counting merged work twice or crediting every merged change to the merge author.

- Triage the full file list, including new/deleted notes and media, before spending time on large patches. Read bounded per-file patches so tool truncation does not silently omit changes.
- Inspect the actual before/after note and enough context to judge meaning. Read the complete note for substantial rewrites or when comments, chronology, or attribution affect interpretation.
- Consolidate repeated edits to a page into its net result. Exclude transient changes that were reverted. Distinguish new lore from existing lore moved, consolidated, or newly exposed in reference prose.
- When other authors' commits are interleaved, use the selected author's per-commit patches as attribution evidence. A single diff between the interval's endpoints also contains other contributors' changes. Note material later supersession when relevant.
- Do not generate a replacement vault-wide prose parser for an ordinary summary. Existing helpers may aid triage, but verify reported findings against raw note text and patches.

## Separate lore from maintenance

Include additions, removals, and corrections that alter facts, relationships, geography, history, beliefs, uncertainty, or campaign events. Also include meaningful descriptions of people, places, organizations, and items. Mention new illustrations or maps briefly when they materially illustrate the lore and fall within the requested scope.

Normally omit spelling, grammar, formatting, link repairs, generated headers/indexes, lint diagnostics, status tags, administrative metadata, tooling, and proposals for workflow changes.

Judge the effect rather than the storage format:

- A frontmatter change to an identity, birth/death date, affiliation, or location can change lore. An administrative timestamp usually does not.
- Restoring an accidentally removed passage is a repair, not newly invented lore. Report it only when its restoration matters to the requested account, and call it a restoration.
- Changes from "all" to "many," certainty to speculation, or prohibition to rarity can be meaningful even when only one word changes.
- Distinguish presentation/visibility changes from new facts. Date and campaign wrappers can change when or to whom lore appears without changing its text.
- A lint report's suggested or copy-ready passage is not an applied change. Do not present it as new lore unless it was actually incorporated into the note body.
- Preserve source authority: campaign records describe play and character knowledge; Worldbuilding and editorial comments remain development material unless adopted. Respect the audience restrictions on DM and private material.

Obsidian syntax needs care: `%%^Campaign:...%%`, `%%^Date:...%%`, and `%%^End%%` delimit conditional content, while ordinary `%% ... %%` comments and generated `Lint`, `Metadata:*`, and `povNotes:*` blocks have different roles. Broad comment-removal regexes can swallow real prose or expose diagnostics. Blockquotes can contain authored lore, prayers, and source passages; do not discard them as if every blockquote were a generated header.

## Write the summary

Lead with the period, contributor when filtered, and the main themes. Keep the account proportional to the meaningful changes, not the number of commits or changed lines.

- **Substantially rewritten pages:** give a linked page title and say it was substantially rewritten. Do not reproduce the rewrite or provide a long synopsis unless requested. Judge the authored content, excluding inflated lint/header churn.
- **Small changes:** briefly identify what changed, then quote the added or revised passage directly. Quote the smallest self-contained passage that preserves its meaning and qualifications. For deletions, identify the removed claim and quote it when useful.
- Link each finding to its note or an exact revision when the current note no longer supports the quoted text. Prefer absolute local file links in a local chat; use appropriate accessible links for an explicitly shared artifact.
- Preserve quoted wording, punctuation, spelling, and uncertainty. It is fine to render wikilinks as their displayed text; mention that normalization once. Use ellipses for real omissions and never silently improve the prose.
- Group related changes where useful, without repeating the same addition across a species page, religion page, and reference note. Keep distinct facts visible.
- Leave minor roleplaying/mechanics additions and illustrations as brief closing items when relevant. Do not pad the answer with commit-by-commit maintenance accounting.

Before delivering, verify that every claimed change is supported by the scoped patch, every quotation matches the relevant after-version, links resolve, and substantial rewrites are not merely large generated diffs. If no meaningful lore changed, say so directly.