# AGENTS.md – Taelgar Obsidian Vault

This document explains how automated agents should work with this vault’s Markdown files.  
Minimal code lives here; the content itself **is** the product.

---

## 1. What This Repo Is

- This repository is an Obsidian vault for homebrew D&D world of Taelgar, a D&D 5.5e setting.
- All content is stored as Markdown notes, typically with YAML frontmatter.
- Notes are a mix of canonical lore, campaign notes, DM notes, and brainstorming/worldbuilding. 

You are here to:
- Search and summarize existing notes.
- Clean up or lightly restructure existing content.
- Create or update notes **only** when explicitly instructed.

You are **not** here to:
- Invent new setting details that do not already exist in the vault, unless explicitly instructed. 

---

## 2a. Golden Rules for Agents

1. **Search first, then answer.**
   - When asked for information, search the vault for relevant notes.
   - Prefer quoting, summarizing, or reorganizing existing content.
   - If you cannot find it, say so clearly instead of guessing.

2. **Do not invent canon.**
   - Do not introduce new lore, dates, names, or events unless the user explicitly asks for speculative ideas.
   - When filling in gaps, keep speculation clearly marked as such (see `%%` comments below).

3. **Always mark AI edits.**
   - Any note you modify outside `_sessions` must be tagged with `status/check/ai` in its YAML frontmatter (see Section 5). Edits to notes in `_sessions` do not require this tag. However, you should *never* add other status tags to any notes you modify.

4. **Do not edit unrelated files.**
   - Do not revert or modify any pre-existing uncommitted changes; only touch files you have been instructed to work on. If you think something should be reverted, ask first.

---

## 2b. Common Task Defintions

You will often be asked to perform the following tasks:

(1) Expand a stub:

If asked to expand one or more "stub" notes into a full note, follow this procedure:
- Search the vault for information relevant to the target note
- Match the length of the note to the amount of information actually present in the vault. If there is only one fact, write one sentence. If there is extensive source material, a longer note is appropriate.
- Do not pad sparse notes with campaign recap, atmospheric prose, or repeated context. Short notes are acceptable and often preferred.
- Add text to the note, following section 2c. Canon and Style Guide. Be sure to properly use DM Notes sections and comments. 
- Use sensible markdown headers if needed; if given a template to follow, follow the style of the template exactly
- If there is minimal information about the target, write what is possible without invention and indicate with a comment (`%%` - see below) that minimal information was available. 
- Mention campaign events only when they are directly relevant to identifying or understanding the subject. Keep those mentions brief, and link to the session note with a useful alias, e.g. `[[Great Library Session Notes - Arc 4|the Suwi investigation]]`.
- Always highlight contradictions or inconsistencies in source material for review
- Always include links to source notes used. Links should be wiki-style `[[]]`, pointing to the file name without the `.md` extension or path. 

(2) Reformat a note:

If asked to reformat or clean up a note, follow this procedure:
- Take the existing text and rewrite it for clarity, conciseness, and detail, potentially changing headers
- Insert the old text in comments (`%%` tags) in relevant sections, so the human reviewer can see the source material
- Then, follow the "Expand a stub" procedure, but focus only on adding new information. Do not add redundant sections to an existing note.

(3) Clean up a blank or staging note:

Blank notes and notes in `Worldbuilding/Staging` are often placeholders. When cleaning them up, aim for a quick bio or place reference, not a campaign recap.
- If the vault contains only minimal information, write a minimal note: usually one or two sentences.
- If the staging note exists only because an entity was mentioned in a session, identify the entity and the useful context, then stop.
- Prefer visible text that answers "what is this?" over text that retells "what happened in the session?"
- Put uncertainty, proposed names, unresolved filing questions, and source limitations in `%%` comments, not in the canonical text.

---

## 2c. Canon and Style Guide

This repository contains speculation, DM notes, and canonical information about Taelgar. 
- Files in directories that start with an underscore (e.g., `_DM_`, `_dm_notes`) are DM information or meta information about the vault itself. DM information can be useful, but should be treated as speculative or brainstorming unless supported by information from elsewhere. 
- Files in the Worldbuilding directory are explicitly brainstorming and should be treated as useful source material, but not necessarily canonical
- Files in other directories are considered canon, unless they have a status tags that suggest errors or unreviewed AI text (e.g., status/check/errors, status/check/ai)
- Information in commnets (`%%`) is always meta or speculative, though it can inform useful context. 

Note are always written in the style of a player-facing, in-world encyclopedia. Stick to a professional tone with a complete in-world focus. 

Write clearly and directly. Avoid circumlocutions like "it is said that" or "are said to" unless you are specifically citing an in world source. Treat general world knowledge as plain fact.

Use comments (`%%`) to include meta information, such as context for information or other DM-facing notes. 
Notes can optionally have a DM notes or meta section at the end, formatted like so:

```
%%^Campaign:none%%

(content)

%%^End%%
```

Prefer `%%` comment blocks for brief asides; prefer %%^Campaign:none%% blocks for longer text, and especially for text that would benefit from headers. 

---

## 3. Markdown & Obsidian Conventions

- **File format**
  - All notes are `.md`.
  - Obsidian-style links: `[[Note Name]]` or `[[Note Name|alias]]`.
- **Headings**
  - Use `#`, `##`, `###` etc. Maintain existing heading hierarchy.
- **Internal links**
  - Do not change link targets unless explicitly asked.
  - Do not rename files, as this may risk breaking links.
- **Special syntax**
  - Keep any callouts, code blocks, or custom inline markers as-is unless the user specifically requests changes.

If you’re unsure what a construct does, leave it alone and annotate with a `%%` comment rather than altering it.

---

## 4. YAML Frontmatter Conventions

Most notes start with YAML frontmatter, for example:

```yaml
---
headerVersion: 2023.11.25
tags: [person]
species: human
born: 1728
gender: female
ancestry: Chardonian
whereabouts: Chardon
dm_notes: none
dm_owner: none
---
```

**Frontmatter fields**

Frontmatter conventions are defined in these notes, stored in `_MoC`
- Note Categorization
- Metadata Specification

Please review these notes before updating frontmatter and conform to conventions. 


**Frontmatter style**
- prefer compact one-line format for YAML lists; EXCEPTION: use multi-line lists for lists of dictionaries. 
- always format dictionaries as single-line entries with {}
- prefer to place commonly edited entries, such as whereabouts, dm_notes, dm_info, campaignInfo at the bottom of the yaml frontmatter
- headerVersion and tags should always be the first two yaml entries

---

## 5. AI Edit Tagging: status/check/ai

Any time an automated agent modifies a note outside `_sessions`:

- Ensure the note has YAML frontmatter.
- Ensure it includes the tag status/check/ai.

Notes under `_sessions` are exempt from this requirement and do not need the `status/check/ai` tag added solely because an automated agent edited them.

Examples:

Existing tags, inline:

`tags: [place, status/stub]`

becomes:

`tags: [place, status/stub, status/check/ai]`


No tags present:

```
---
headerVersion: 2023.11.25
---
```

becomes:

```
---
headerVersion: 2023.11.25
tags: [status/check/ai]
---
```

Never remove status/check/ai yourself; that is reserved for human review.

---

## 6. %% ... %% Comment Conventions

`%%` marks Obsidian comments that are visible in the editor but not in preview.
Agents use these for meta-notes, uncertainties, and minimal extractions.

### 6.1 General Rules

Use `%%` for:
- Uncertain information.
- Meta commentary about how the note was created/edited.
- TODOs or follow-up work for the human author.

Do not put new canonical lore inside %%; anything in %% is non-canonical by default.

### 6.2 When Extracting Minimal Information

When you only have a tiny amount of information (e.g., from a transcript or partial reference):

Create a very small, factual stub:

A name.

A one-line description strictly based on what’s in the source.

Add a `%%` block at the top or near the relevant section explaining the limitation.

Example stub note:

```markdown
---
tags: [person, status/check/ai]
type: person
---

# Szoltár

Szoltár is a hobgoblin warrior who fought in the army of the [[Empress of Chaos]]. 

%% Minimal details invented; based on session transcript only %%
```

For uncertainty in an existing note:

%% AI note: The following summary is based only on currently available notes.
   If more detailed lore exists elsewhere, this section should be reviewed and expanded by a human. %%

### 6.3 Marking Speculation

If the user explicitly asks for speculative content or ideas:

Clearly mark it:

%% Speculative ideas generated by AI at user request. %%

Do not mix speculative text and established lore without such a marker.

---

## 7. Typical Tasks for Agents (Markdown Only)

When working in this repo, you are generally allowed to:

- Summarize existing notes into shorter reference sections.
- Normalize formatting (headings, bullet lists, spacing) while preserving content.
- Add missing frontmatter fields or tags, especially status/check/ai for notes outside `_sessions`.

Create stub notes for entities that appear in other notes but lack their own pages, using:
- Only facts present in the vault.
- `%%` comments to flag that the stub is incomplete.

Treat these as patterns, not hard rules; when in doubt, prefer less change and add a `%%` note.

---

## 8. Operations to Avoid (Without Explicit Instruction)

Do not perform the following unless the user explicitly tells you to, and even then, proceed carefully:

- Bulk renaming or moving notes.
- Large-scale restructuring of headings across many files.
- Deleting any notes or sections.
- Rewriting long passages of lore “for style” without a clear request.
- Collapsing or merging distinct entities because they “seem similar.”

If you think such a change is needed, add a `%%` comment suggesting it rather than doing it.

---

## 9. Quick Checklist for Any Edit

Before you finish editing a file:

- Did you search the vault for relevant existing content?
- Did you avoid inventing new canon, except where explicitly requested?
- If you added speculative or incomplete material, did you wrap it in `%%` with a clear explanation?
- If the edited note is outside `_sessions`, does its YAML frontmatter include status/check/ai?
- Did you keep the change as small and reversible as possible?
- When checking `git diff`, ignore minor end-of-file-only whitespace differences, such as an extra or missing final newline or extra or missing whitespace at the very end of the file. Do not make follow-up edits solely to normalize those EOF differences.

If all answers are “yes,” your edit is likely acceptable.
