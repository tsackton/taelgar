# Taelgar Skills

Last reviewed: **2026-10-30**

This guide covers the 28 skills maintained in this repository under `.agents/skills/`. It does not list personal or installed plugin skills, which can vary between machines.

Describe the task in ordinary language, or name a skill explicitly with `$skill-name`. Include the relevant note, session, source, or folder and what you want done. The linked skill instructions define the actual workflow and approvals; this guide is a way to choose the right starting point.

## Session preparation

For a recorded session, the core sequence is **transcribe-session → prepare-session-source → process-transcript**. Use **correct-transcript** for later targeted fixes. **session-note-prep** runs process-transcript when needed before its recap stages. Start at the step that matches the material you already have. Each step has its own scope and approvals; requesting one does not automatically request the rest.

Bundle creation belongs solely to **prepare-session-source**, which stops at a ready bundle. For transcript products, use **process-transcript** with that existing prepared bundle. If none exists, it asks whether to use prepare-session-source first. It initializes cleaned working text, makes reasonable contextual repairs to the cleaned UID text, and produces readable full-session Markdown with source mapping. Unrecoverable incidental speech can become `[garbled]` or `[cross-talk]` in the polished version only. Human review contains exact-span proposals and complete-exchange context for consequential choices. The review Markdown carries its own pending decisions and can be resumed alongside the retained references without the original processing state. Session-local state supports resuming work and processing different sessions concurrently. Finalization after review keeps the original, prepared UID, cleaned UID, polished Markdown, and session metadata, and removes temporary processing/review files. Corrected speakers, including multiple speakers within one UID, are retained in polished Markdown rather than duplicated in session YAML; cleaned speaker headers remain unchanged. Spoken factual mistakes and contradictions are preserved. Transcription, fact-checking, recaps, and highlight extraction remain separate workflows.

| Skill                                                                    | What it does                                                                                                                                                                                                                                                                                                    | Example use case                                                                                   |
| ------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| [transcribe-session](.agents/skills/transcribe-session/SKILL.md)         | Turns a local recording into a first-pass transcript and helps identify speakers. It can also inventory sequential recording chunks and alternate captures. Loads the API key from the environment or `~/RPGs/taelgar-utils/.env`, asking for another env file when needed. Uploading audio requires approval; this stage works beside the recordings, outside the vault. | “Transcribe this session recording and identify the participants.”                                 |
| [prepare-session-source](.agents/skills/prepare-session-source/SKILL.md) | Sole owner of new bundle creation: verifies session metadata and speaker mappings, then builds the prepared bundle. Stops there; processing and session-note preparation are separate requests.                                                                                                                                                                   | “Prepare this identified transcript for Dunmari Frontier Session 21.”                              |
| [process-transcript](.agents/skills/process-transcript/SKILL.md) | Starts from an existing prepared bundle and owns cleanup, polishing, quality review, chat review, and finalization. Offers prepare-session-source when the bundle is missing; never creates it implicitly. Its optional audio-review mode builds one listening page for selected passages across sessions without running processing; answers are saved in review Markdown and applied through the normal review. | “Process Dunmar session 53,” “Apply these review answers,” or “Generate an audio review page for these passages from sessions 64, 87, and 93.” |
| [correct-transcript](.agents/skills/correct-transcript/SKILL.md) | Handles targeted later wording and speaker edits, including several speakers within one UID and garbled/cross-talk display labels. Its shared helper keeps cleaned and polished text, source spans, and completion records aligned, and flags existing derivatives, including excerpts and highlights, for inspection. Ongoing human review stays in process-transcript. | “Replace this misheard name,” or “That turn was Yezali, not Oskar.” |
| [session-note-prep](.agents/skills/session-note-prep/SKILL.md)           | Runs or resumes a prepared bundle through cleanup, beats, chronology review, scene grouping, and a structured session recap. Its default interactive mode includes review of material uncertainty, date questions, and the scene proposal. It stops at the recap rather than rendering the final campaign note. | “Run session-note-prep on this prepared bundle,” or “Resume this bundle from its completed beats.” |
| [cleenseau-note](.agents/skills/cleenseau-note/SKILL.md)                 | Builds or revises Cleenseau session notes from Dreamwidth accounts and vault sources, preserving the source and using the recap/component/template pipeline for the final note. It also handles reviewed email-based sessions through the companion email workflow.                                             | “Build the Cleenseau session note from this Dreamwidth recap.”                                     |

### Individual session stages

These stages work from YAML-registered polished transcripts. Scene and entity
mapping run independently; a reduction draft is optional for scene reading.

| Skill | What it does | Example use case |
| --- | --- | --- |
| [prepare-interaction-transcript](.agents/skills/prepare-interaction-transcript/SKILL.md) | Makes a conservative smaller reading view, preserving speech/lore and all UID spans while replacing routine mechanics/chatter with restorable snips. Writes only the derivative draft. | “Prepare an interactions draft from Dunmar 10's polished transcript.” |
| [map-transcript-scenes](.agents/skills/map-transcript-scenes/SKILL.md) | Maps continuous stays at meaningful sites and travel routes, with separate start/end dates and narrative times. Uses the shared confidence/status review structure; an optional issues block surfaces AI concerns for review only. | “Map Dunmar 49's places and times, treating each tower visit and continuous route as one span.” |
| [check-session-entities](.agents/skills/check-session-entities/SKILL.md) | Checks NPCs, divine beings, significant items, and organizations directly from polished speech. Links vault identities and flags later identifications while preserving session labels. Its v3 map uses occurrence arrays for inclusions and exclusions; entity rationales are omitted. | “Check this session's entities without a scene map.” |

The [entity review workflow](.agents/skills/check-session-entities/references/review-workflow.md)
covers saved reviews and manual feedback. The [pipeline/model contract](.agents/skills/check-session-entities/references/pipeline-model.md)
defines the read-only v7 candidate projection. Final interaction generation,
automatic feedback application, and Obsidian review integration are unfinished.

The stages below are normally called by the session pipeline, except for the optional excerpt and highlights workflow after the recap. Use them directly when you want one stage, rather than the whole process.

| Skill | What it does | Example use case |
| --- | --- | --- |
| [transcript-splitter](.agents/skills/transcript-splitter/SKILL.md) | Divides a cleaned transcript or normalized written source into ordered story beats, preserving complete source coverage. Produces beat data and a readable preview. | “Split this cleaned source into beats.” |
| [beat-annotator](.agents/skills/beat-annotator/SKILL.md) | Records the supported facts for each beat, including people, places, items, organizations, and combat. Full-session work also reviews chronology against the session dates; a single-beat mode is available. | “Annotate these beats and check the session chronology.” |
| [session-summary](.agents/skills/session-summary/SKILL.md) | Builds the structured recap from finalized beats and facts, using the pipeline's scene grouping and chronology when applicable. Produces compact timeline entries and recap prose at three levels of detail. | “Draft the session recap from these finalized beats and facts.” |
| [transcript-excerpts](.agents/skills/beat-transcript-polisher/SKILL.md) | Copies recap excerpts from the finalized polished transcript, preserving corrected speakers and source spans, and helps select quotes/audio highlights. Reruns preserve existing recap selections; no second polishing pass. | “Add transcript excerpts and highlight candidates for this recap, keeping my existing selections.” |

## Reviewing and completing vault notes

| Skill | What it does | Example use case |
| --- | --- | --- |
| [review-stub-staging](.agents/skills/review-stub-staging/SKILL.md) | Works with you to complete a person or place page from evidence and your corrections, including identity information, pronunciation, and the generated header. After approval, it retires stub status and files Staging pages where appropriate. Full linting is a separate choice. | “Help me complete this person stub,” or “Review this place in Staging and prepare it for filing.” |
| [lint-taelgar-note](.agents/skills/lint-taelgar-note/SKILL.md) | Reviews eligible notes for metadata, structure, links, source support, and editorial completeness or currency. Records open findings or a completed clean review. Worldbuilding and dot/underscore directories are excluded. | “Lint these three reference notes,” or “Re-lint this previously reviewed page.” |
| [lint-cleanup](.agents/skills/lint-cleanup/SKILL.md) | Resolves existing findings that concern only names, language, or pronunciation in small reviewed batches. It does not perform a new full lint. | “Find a batch of name-only lint findings and work through them with me.” |
| [batch-lint-cleanup](.agents/skills/batch-lint-cleanup/SKILL.md) | Presents name-only lint proposals and full original reports in an open review document, with language guesses for adoption, batch approval, and selective row regeneration. It does not re-lint. | “Prepare ten name-only lint reviews; let me approve the batch or redo selected rows.” |
| [review-linked-notes](.agents/skills/review-linked-notes/SKILL.md) | Collects the context pages linked from selected notes or session recaps, presents the scope, and coordinates approved creation and linting. It reviews the surrounding pages rather than rewriting the source note. A named ready subset can proceed with approval while blocked pages remain pending. | “Review the people and places linked from this session.” |
| [vault-brainstorming-cleanup](.agents/skills/vault-brainstorming-cleanup/SKILL.md) | Finds substantial noncanonical idea passages and proposes their extraction, organization, consolidation, or retirement in reviewed batches. It preserves uncertainty and does not adopt ideas as canon. | “Find overlapping brainstorming about this region and propose a cleanup.” |
| [summarize-lore-changes](.agents/skills/summarize-lore-changes/SKILL.md) | Reviews vault history for meaningful lore and campaign-content changes, optionally by contributor. Quotes small changes, identifies substantial rewrites, and skips lint, metadata, and header maintenance unless it changes the lore. | “Summarize tsackton’s lore changes over the last four days.” |

## Design, illustrations, and assets

| Skill | What it does | Example use case |
| --- | --- | --- |
| [capture-brainstorming-idea](.agents/skills/capture-brainstorming-idea/SKILL.md) | Saves casual ideas verbatim in one monthly log, records their inspiration, and adds useful research, concrete color, and explained Taelgar connections. Research stays in the note; chat stays brief. | “I'm watching a documentary and will drop ideas—capture them with useful research and Taelgar connections.” |
| [adventure-design](.agents/skills/adventure-design/SKILL.md) | Develops an adventure's premise, goals, challenges, outcomes, and connected structure with you, using the vault's templates. It can develop an outline, Canvas structure, and initial scene cores; detailed encounters and session preparation are separate work. | “Help me turn this adventure premise into a connected outline.” |
| [illustrate-note](.agents/skills/illustrate-note/SKILL.md) | Selects illustration targets from a note or recap and develops evidence-based visual briefs with deliberate composition, materials, and lighting. Compares purposeful alternatives, critiques them at reading and full size, and makes targeted revisions with you. Only approved finals are exported; insertion requires separate authorization. | “Illustrate this history with portraits and scenes,” or “Refine this recap illustration so the action reads clearly and the materials feel distinct.” |
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
