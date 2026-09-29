---
name: review-linked-notes
description: Collate and review Taelgar context pages linked from one or more target notes, with an approved scope list, missing-note creation, existing-linter handoff, and optional images or status tables. For sessions, accept campaign/session identifiers and use recap entities when the final note is missing or the user opts in. Use for reviewing the surrounding context pages, not for reviewing or generating the target note itself.
---

# Review Linked Notes

Use target notes as collection roots and source evidence. Review the resulting context pages through the existing vault workflows. Follow the vault `AGENTS.md`; this skill does not authorize changes to the collection roots, session recaps, or session-processing artifacts.

## 1. Resolve sources and collect candidates

Accept one or more note paths, note names, or campaign/session identifiers. Resolve ambiguous identities before proceeding. Read each selected source completely, including frontmatter and comments.

### Ordinary note sources

- Collect direct internal note links, including Markdown links, note embeds, and links in metadata. Resolve aliases displayed in links and heading/block fragments to the underlying file; ignore same-note fragments. Distinguish actual links from code examples.
- Deduplicate by resolved vault path while retaining every originating target and the passage or field that supplied the reference. Detect filename collisions; frontmatter aliases help identify subjects but do not determine how a bare wikilink resolves.
- Identify substantive context pages separately from navigation, assets, production artifacts, and references found only in generated lint output. Present exclusions explicitly. Keep comment-only or private references marked with their source authority and visibility.
- Also identify noteworthy unlinked subjects as candidates. Search before proposing a new note. Incidental rooms, generic enemies, mundane possessions, and hypothetical objects do not automatically warrant standalone pages.
- Default to one link depth. Further searches may supply evidence or resolve identity, but do not expand the work collection without approval. Exclude the collection roots themselves from review, including when roots link to one another, unless the user explicitly includes them.

### Session sources and recap mode

Resolve campaign names, codes, aliases, and expected final-note locations using `../../../_scripts/session_note_campaigns.json`. Verify the actual files and session identity rather than assuming a constructed filename exists. Preserve fractional or otherwise distinctive session identifiers.

Choose the collection source separately for each session:

- **Final session note exists:** use its links by default. Offer recap entity collection as an opt-in choice unless the user already specified it. Do not silently supplement the collection from its recap.
- **Final session note is missing:** use the matching session recap as the collection source and say so in the scope preview. Do not create a final session note as a prerequisite.
- **User explicitly selects a recap:** use it even if a final session note exists. When supplementing a final note, take the deduplicated union and label each entry's provenance. Honor an explicit recap-only request.

Locate the current recap in the campaign's session bundle, normally `cleaned/<bundle-stem>-session-recap.md`, and verify its campaign/session header against the manifest when needed. Prefer the accepted or human-edited recap over old drafts, generated component copies, or stale context JSON. If the correct recap is absent or ambiguous, ask for the source; do not regenerate it or substitute transcripts automatically.

Parse **NPCs, locations, groups/organizations, and objects/items** from the recap's cast and world sections, including encountered and mentioned-only entries. Read relevant recap/timeline fields and prose to understand each entity and recover candidates when human edits changed or removed the standard sections. Names need not already be wikilinks. Retain encountered versus mentioned status and dated context where available. Exclude `none`, empty fields, and editorial placeholders. Do not classify PCs as missing NPCs or turn every sublocation or incidental item into a proposed note.

Resolve each entity against vault filenames, `name`, `aliases`, spelling/diacritic variants, existing links, and surrounding context. Record an exact match, an identity question, or a proposed missing subject; never silently merge ambiguous matches. Treat recap assertions as records of play with the vault's usual authority and uncertainty boundaries.

Human-edited recaps are read-only sources. Do not validate them against the generated recap schema, restore removed structure, normalize them, or rebuild pipeline outputs. Consult [session-summary](../session-summary/SKILL.md) only when source-format guidance is needed; do not run its drafting workflow.

## 2. Present and approve the scope of work

Discovery and source matching are read-only. **Before creating notes, changing metadata, performing contextual lint reviews, or generating images, present the complete proposed scope list and wait for user approval.** A general request to run this skill does not bypass this checkpoint. If the user already approved the same exact list and operations in the conversation, show a readback and continue without asking again.

Show the selected roots and source modes, then one row per distinct subject:

| Subject / note | Source targets and reference | Resolved or proposed path | Planned action | Blocker / decision |
| --- | --- | --- | --- | --- |

Use concrete actions such as lint, re-lint, create then lint, create in staging then pause, resolve identity, or exclude. Include existing tags and recorded lint completion when they affect the decision. Account separately for filtered navigation/assets and other exclusions; do not silently drop subject pages because they are ineligible.

For missing notes, include the proposed destination, supported frontmatter fields, and a brief factual bullet outline in the preview. For unresolved candidates, show the alternatives and why the identity or need for a note is uncertain. Preserve source privacy in both the preview and any persisted artifact.

State the proposed lint mode and whether previously completed notes are included. The default preserves every valid previous `lintedAt`/`lintVersion` pair; offer re-linting and obtain explicit authorization before including those pages. Do not infer re-lint permission from stale versions or recent session evidence.

Include any requested image work and the exact status-table destination/section. If those options remain undecided, retain them as pending closeout choices in section 6; omission from the initial scope is not a decline. Scope approval can cover both the displayed note creations and the subsequent lint; do not request duplicate approval for those same operations. Material additions or changes require an updated preview and approval for the changed scope.

## 3. Create approved missing notes

Before writing, check the current branch and working tree under the vault Git procedure. Read the current [Note Categorization](../../../_MoC/Note%20Categorization.md), [Metadata Specification](../../../_MoC/Metadata%20Specification.md), and appropriate template. Search the wider vault for supported facts and possible existing identities before declaring a subject missing. Preserve source distinctions and flag conflicts instead of resolving them by inference.

- Add directly supported metadata and a small factual bullet outline, with source links or a hidden source block. Do not add narrative expansion or pad sparse evidence. Infer dates, affiliations, whereabouts, and campaign knowledge only when the evidence supports their documented meanings.
- Use the approved canonical location when identity and classification are settled. Use the approved staging destination when filing or interpretation remains open. Staging does not promote provisional content into canon.
- Apply `status/check/ai` where required. “Stub” describes minimal content here; never add or change `status/stub` or other human-owned status tags. Apply the no-tags exception for `Worldbuilding/Agentic Review` if that destination was explicitly selected.
- Do not rename or move existing files. If staging needs a backlink or the source uses the wrong link target, propose the source change separately. For generated session notes, any authorized correction must follow that session workflow's durable source rules; do not patch only rendered output.

Validate and read back created files under `AGENTS.md`. Do not treat approved destinations or metadata proposals as permission to modify unrelated notes.

## 4. Resolve lint blockers before review

Load [lint-taelgar-note](../lint-taelgar-note/SKILL.md) and use its live applicability rules for the approved collection. Its specification and tools own eligibility; do not maintain a competing test here.

Notes under `Worldbuilding` or dot/underscore directories are not lint targets. Factual bullets may qualify as substantive authored content; metadata-only notes, headings, and planning placeholders do not. A canonical file location alone does not make a note eligible.

If any included page is missing, ambiguous, staged, or otherwise ineligible, **warn the user and pause before linting the collection**. List the affected paths and the needed decisions. Wait for the user to update them, explicitly authorize a bounded remedy, or explicitly exclude them. Do not silently lint only the eligible subset or move a note to make it eligible.

After updates, reread affected sources and pages, resolve their current paths, and refresh the scope list. Continue on unchanged approval; obtain approval for material scope changes. Preserve exclusions and reasons in the final accounting. If the linter later discovers another ineligible subject, return to this checkpoint before finalization rather than silently accepting partial coverage.

## 5. Hand off the approved collection to the linter

Follow the live lint skill for single-note or batch execution, model/delegation requirements, authorization, privacy, verification, and finalization. Do not duplicate its findings, change its version, consult historical lint guidance, or implement a second editorial review pass.

Pass exact approved subject paths, lint/re-lint authorization, any user restriction on prose edits, and the originating source notes or recaps with relevant references. The sources are evidence, not additional lint targets. Supply this context without bypassing the linter's normal source search or treating repeated session artifacts as independent evidence.

Leave broader expansions or substantive changes surfaced by lint as proposals unless separately authorized. Record completed, skipped, excluded, blocked, and failed outcomes accurately; an old completed lint is not a review performed during this run. Retain completed work across pauses and do not re-lint it merely to resume the workflow.

After linting and verification, return to section 6 of this skill. The linter's handoff is input to the linked-note closeout, not the end of this workflow. The coordinating agent retains responsibility for the summary and any pending artifact choice, including when linting was delegated or all notes were previously completed.

## 6. Close out with a summary and optional artifacts

Always provide a substantive chat summary: identify the collection roots and source mode, distinguish newly reviewed notes from preserved prior reviews and exclusions, explain the important open findings in plain language, and separate applied changes from proposed additions. Use the linter's generated handoff and saved reports without performing a second editorial review. Include concise counts, links, and unresolved blockers, but do not substitute counts or rule identifiers for the findings summary.

### Summary page or status table

If this option is undecided, explicitly ask whether the user wants the summary saved with a status table for the full approved collection, including preserved prior reviews and exclusions. Propose a concrete destination and content outline; use a suitable existing review location or suggest `Worldbuilding/Agentic Review/<target> - Linked Notes Review.md`. A restriction on creating subject pages does not settle this separate choice, but never write a summary without authorization. Honor explicit summary-page declines and broader instructions such as chat-only or no further writes. If the destination and contents were already approved, write them without asking again.

The saved summary should include the collection source, snapshot date, substantive findings from this run, applied changes versus proposals, the complete status table, and exclusions or remaining decisions. Read final live completion fields, tags, and saved reports for the table without re-linting preserved notes. Useful columns are **Page**, **Referenced by**, **Tags**, **Lint state**, and **Outstanding work**; include image status only when relevant. Clearly distinguish newly completed clean/open results from preserved, skipped, excluded, blocked, or failed work. A completion pair with no report records prior state, not a new assurance of completeness; flag tag/report mismatches without repairing them or inferring findings from tags alone.

Keep private evidence out of shared summaries. Preserve unrelated destination content and apply its status/tag rules; under `Worldbuilding/Agentic Review`, use no YAML or inline tags, and display source-note tags as plain text. Preview any unapproved destination, section, or replacement before writing. Read back the saved artifact and verify its paths and values.

### Images

After the note work, offer [illustrate-note](../illustrate-note/SKILL.md) if image work was not already decided. Hand off the selected pages and relevant source context to that skill for image target selection, two initial alternatives, iterative feedback, and export of explicitly approved finals. Keep drafts outside the vault. Image approval does not itself authorize replacing existing assets or inserting images into notes; follow the companion skill's separate insertion step.

Closeout is complete when the chat summary has been delivered and each optional artifact is either delivered with a link, explicitly declined, or presented as a concrete pending choice. When awaiting a choice, end with the useful summary and that question; retain completed lint work while waiting. Do not end immediately after the linter's completion message or reopen an already settled image or summary decision.
