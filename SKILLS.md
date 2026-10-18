# Taelgar Skills

Last reviewed: **2026-10-18**

This guide covers the 21 skills maintained in this repository under `.agents/skills/`. It does not list personal or installed plugin skills, which can vary between machines.

Describe the task in ordinary language, or name a skill explicitly with `$skill-name`. Include the relevant note, session, source, or folder and what you want done. The linked skill instructions define the actual workflow and approvals; this guide is a way to choose the right starting point.

## Session preparation

For a recorded session, the usual sequence is **transcribe-session → prepare-session-source → session-note-prep**. Start at the step that matches the material you already have. Each step has its own scope and approvals; requesting one does not automatically request the rest.

| Skill | What it does | Example use case |
| --- | --- | --- |
| [transcribe-session](.agents/skills/transcribe-session/SKILL.md) | Turns a local recording into a first-pass transcript and helps identify speakers. It can also inventory sequential recording chunks and alternate captures. Uploading audio requires approval; this stage works beside the recordings, outside the vault. | “Transcribe this session recording and identify the participants.” |
| [prepare-session-source](.agents/skills/prepare-session-source/SKILL.md) | Sets up the campaign/session information and transcript speaker mapping, then builds the vault source bundle after those inputs are reviewed. | “Prepare this identified transcript for Dunmari Frontier Session 21.” |
| [session-note-prep](.agents/skills/session-note-prep/SKILL.md) | Runs or resumes a prepared bundle through cleanup, beats, chronology review, scene grouping, and a structured session recap. Its default interactive mode includes review of material uncertainty, date questions, and the scene proposal. It stops at the recap rather than rendering the final campaign note. | “Run session-note-prep on this prepared bundle,” or “Resume this bundle from its completed beats.” |
| [cleenseau-note](.agents/skills/cleenseau-note/SKILL.md) | Builds or revises Cleenseau session notes from Dreamwidth accounts and vault sources, preserving the source and using the recap/component/template pipeline for the final note. It also handles reviewed email-based sessions through the companion email workflow. | “Build the Cleenseau session note from this Dreamwidth recap.” |

### Individual session stages

These are normally called by the session pipeline, except for the optional transcript polisher after the recap. Use them directly when you want one stage, rather than the whole process.

| Skill | What it does | Example use case |
| --- | --- | --- |
| [transcript-cleaner](.agents/skills/transcript-cleaner/SKILL.md) | Corrects transcription errors while preserving line IDs, speakers, timestamps, and order. Collects meaningful unresolved uncertainty for review; it does not turn the transcript into polished narrative. | “Clean this prepared transcript, but stop before splitting it into beats.” |
| [transcript-splitter](.agents/skills/transcript-splitter/SKILL.md) | Divides a cleaned transcript or normalized written source into ordered story beats, preserving complete source coverage. Produces beat data and a readable preview. | “Split this cleaned source into beats.” |
| [beat-annotator](.agents/skills/beat-annotator/SKILL.md) | Records the supported facts for each beat, including people, places, items, organizations, and combat. Full-session work also reviews chronology against the session dates; a single-beat mode is available. | “Annotate these beats and check the session chronology.” |
| [session-summary](.agents/skills/session-summary/SKILL.md) | Builds the structured recap from finalized beats and facts, using the pipeline's scene grouping and chronology when applicable. Produces compact timeline entries and recap prose at three levels of detail. | “Draft the session recap from these finalized beats and facts.” |
| [beat-transcript-polisher](.agents/skills/beat-transcript-polisher/SKILL.md) | Produces readable transcript excerpts organized around recap scenes and links them from the recap. Use after the recap exists, when the transcript itself is wanted as a more detailed view. | “Add polished transcript excerpts for this completed recap.” |

## Reviewing and completing vault notes

| Skill | What it does | Example use case |
| --- | --- | --- |
| [review-stub-staging](.agents/skills/review-stub-staging/SKILL.md) | Works with you to complete a person or place page from evidence and your corrections, including identity information, pronunciation, and the generated header. After approval, it retires stub status and files Staging pages where appropriate. Full linting is a separate choice. | “Help me complete this person stub,” or “Review this place in Staging and prepare it for filing.” |
| [lint-taelgar-note](.agents/skills/lint-taelgar-note/SKILL.md) | Reviews eligible notes for metadata, structure, links, source support, and editorial completeness or currency. Records open findings or a completed clean review. Worldbuilding and dot/underscore directories are excluded. | “Lint these three reference notes,” or “Re-lint this previously reviewed page.” |
| [lint-cleanup](.agents/skills/lint-cleanup/SKILL.md) | Resolves existing findings that concern only names, language, or pronunciation in small reviewed batches. It does not perform a new full lint. | “Find a batch of name-only lint findings and work through them with me.” |
| [review-linked-notes](.agents/skills/review-linked-notes/SKILL.md) | Collects the context pages linked from selected notes or session recaps, presents the scope, and coordinates approved creation and linting. It reviews the surrounding pages rather than rewriting the source note. A named ready subset can proceed with approval while blocked pages remain pending. | “Review the people and places linked from this session.” |
| [vault-brainstorming-cleanup](.agents/skills/vault-brainstorming-cleanup/SKILL.md) | Finds substantial noncanonical idea passages and proposes their extraction, organization, consolidation, or retirement in reviewed batches. It preserves uncertainty and does not adopt ideas as canon. | “Find overlapping brainstorming about this region and propose a cleanup.” |

## Design, illustrations, and assets

| Skill | What it does | Example use case |
| --- | --- | --- |
| [adventure-design](.agents/skills/adventure-design/SKILL.md) | Develops an adventure's premise, goals, challenges, outcomes, and connected structure with you, using the vault's templates. It can develop an outline, Canvas structure, and initial scene cores; detailed encounters and session preparation are separate work. | “Help me turn this adventure premise into a connected outline.” |
| [illustrate-note](.agents/skills/illustrate-note/SKILL.md) | Selects illustration targets from a note or recap, gathers visual evidence, generates alternatives, and refines them with you. Only approved finals are exported; inserting them into notes is a separate authorized step. | “Illustrate this history with portraits and scenes,” or “Create images for these recap scenes.” |
| [taelgar-asset-review](.agents/skills/taelgar-asset-review/SKILL.md) | Either reviews image/audio placement and applies approved directory moves, or checks and repairs frontmatter image references. A property check does not require a full asset-organization scan. Renaming, replacing asset files, conversion, maps, and generated audio need separate handling. | “Find misplaced campaign images,” or “Check the image properties on these notes.” |

## Importing and organizing source material

| Skill | What it does | Example use case |
| --- | --- | --- |
| [gdrive-doc-source](.agents/skills/gdrive-doc-source/SKILL.md) | Preserves a Google Doc as a readable Markdown source, including open and resolved comment threads. It preserves the source rather than rewriting it into canon. | “Import this old worldbuilding Google Doc, including its comments.” |
| [taelgar-email-import](.agents/skills/taelgar-email-import/SKILL.md) | Finds Taelgar worldbuilding correspondence in connected Gmail and preserves it as readable source notes. Supports new imports, completeness checks, and reformatting existing imports. | “Find and import our worldbuilding correspondence about this topic.” |
| [discord-chat-export](.agents/skills/discord-chat-export/SKILL.md) | Imports approved Discord conversations as reviewed, dated source notes. Supports catch-up runs and deliberate re-exports as well as new imports. | “Catch up this channel's source notes through yesterday.” |
| [cleenseau-email-review](.agents/skills/cleenseau-email-review/SKILL.md) | Reviews existing Cleenseau Raw Emails and routes their useful content to played exchanges, in-world writings, authorial narratives, or accepted facts. Raw files are retired only after their content, attachments, and links are accounted for. | “Review the next batch of Cleenseau Raw Emails and propose where each belongs.” |

## Keeping this guide current

Review this catalog when skills are added, removed, or materially change purpose. Check the use cases against the linked instructions and update the last-reviewed date after that review. Detailed procedures and approval rules belong in the individual skills.
