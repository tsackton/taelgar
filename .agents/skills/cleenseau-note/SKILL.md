---
name: cleenseau-note
description: Build or revise Cleenseau campaign session notes from Dreamwidth recaps and vault sources using the composable session-note pipeline. Use for source preservation, date reconstruction, reviewed recaps, generated components, NPC staging stubs, or final Cleenseau session-note cleanup; do not use for other campaigns.
---

# Cleenseau Note

Build a concise, source-grounded Cleenseau session record while preserving the player's colorful account in the long narrative.

## Establish The Sources

1. Follow the vault `AGENTS.md` and any more specific instructions.
2. Preserve the complete Dreamwidth post in the session's `sources` directory and record its original URL. Do not treat a link alone as archival preservation.
3. Treat the player recap as the primary record of what happened in play. Use adventure notes to identify people, roles, and behind-screen context without exposing unrelated DM material.
4. Search canonical vault notes for dates, terminology, and link targets. Do not invent missing facts or silently resolve source conflicts.
5. Derive the real session date as the Sunday on or immediately before the Dreamwidth publication date unless the user supplies a date. Record the in-world date only from supported vault evidence or user confirmation.

## Resolve Editorial Questions Before Drafting

Ask the user which candidate locations and items belong in the structured summary, whether every unnamed NPC has a name, and which candidate pull quotes to include. Present compact candidate lists rather than open-ended questions.

- Keep the one-sentence summary simple. Normally omit NPC names unless the NPC is central to understanding the session.
- In the cast, include every NPC with whom the party meaningfully interacts, plus every named NPC whom the party meets or hears of for the first time. Before treating a name as missing, search filenames, frontmatter `name` and `aliases`, likely spelling variants, and relevant place or family notes. If no note exists after that search, create a minimal linked stub in `Worldbuilding/Staging/Cleenseau` using only supported facts.
- Treat a place as a location only when it is named, map-worthy, or a meaningful building or landmark. Do not promote incidental rooms, clearings, ridges, temporary pocket spaces, or encounter terrain into locations merely because events occur there.
- Include an item only when it is unique or consequential and is acquired, discovered, materially changed, or central to the session. When reconstructing sessions backward, normally list an item in the session where it was acquired; do not repeat it in a later session merely because the party discusses or investigates it. Omit mundane objects and incidental use of pre-existing gear.
- Treat only concrete objects as items. Put blessings, bonds, permissions, vows, transformations, crafting benefits, and other nonphysical boons in the narrative or relevant character context instead of the item section.
- When no items are approved, render no item heading or section rather than leaving an empty `Treasure and Things` section.
- Omit empty optional sections such as Organizations and Combat instead of rendering bare headings.

Do not proceed past unresolved location, item, or unnamed-NPC questions unless the user has authorized a stated conservative assumption.

## Shape The Note

### Summary And Cast

- Keep the one-sentence summary factual and compact. Prefer the event and outcome over a roll call of NPC names; name an NPC only when that NPC is central to the summary.
- Keep the cast comprehensive under the rule above even when the one-sentence summary is deliberately sparse.
- Use canonical wikilinks where targets exist. Link newly created NPC stubs.
- Keep unnamed creatures descriptive and lowercase, such as `the duplicate` or `the doppelganger`; do not manufacture a proper name or stub.
- Treat Greymalkin and Es*tiasilos as implicit, normally present members of the party. Do not list them in the cast, companion frontmatter, or `Featuring` header. Retain them in narrative prose when their actions matter, and keep beat-level tracking when useful for source fidelity.

### Timeline

Use timeline entries to show meaningful passage of time, not every scene.

- A continuous sequence without a rest, break, travel interval, downtime, or time jump normally gets one timeline entry.
- Split the timeline only when the session spans meaningfully different periods.
- A single-entry timeline may closely resemble the one-sentence summary or session highlight.
- Recap beats may remain more granular than the timeline.

### Narrative

- Make `Long` narratives substantially preserve the player's wording, sequence, and distinctive descriptions.
- Remove fourth-wall material: player/GM deliberation, rules and roll discussion, table logistics, out-of-game asides, and external pop-culture comparisons.
- Replace table nicknames with supported character or descriptive names when needed for clarity.
- Keep `Short` and `Intermediate` narratives factual and progressively compressed.
- Preserve uncertainty. Attribute conclusions that were only inferred during play.

### Pull Quotes

Scan the complete source for memorable, clearly attributable player or player-character quotations. Present each candidate to the user with its exact wording and attributed speaker, and get explicit approval for each quote before adding it to the reviewed recap. Include only approved quotes, with exact wording, speaker, and source-line references. Do not guess at attribution. Quotes may preserve table voice even when equivalent fourth-wall material is removed from the narrative.

## Use The Session-Note Pipeline

Treat the reviewed `*-session-recap.md` as the durable, human-gated content source. Treat `_generated/session-notes/<sessionKey>/` as a rebuildable interchange layer and the campaign session note as rendered output. Do not keep a durable content or link correction only in `_generated` or the final note: `--overwrite` replaces generated slots, and Templater replaces the final note body.

1. Edit the reviewed session recap and cleaned session manifest. Keep the complete original source and its preparation manifest under the session's `sources` directory.
2. Keep `sourceUrl`, and when available `sourceTitle` and `sourceAuthor`, in both source and cleaned manifests. The builder exposes these as `session.source_url` and `session.source_header`.
3. Generate components with `_scripts/build_session_note_components.py --overwrite -c clee -n <session>`.
4. Review unresolved-link reports and every generated slot, especially summary, timeline, cast, locations, items, approved pull quotes, and narrative.
5. Ensure the final note frontmatter has the generated `sessionKey` and `session-template: cleenseau-template.md`. The Cleenseau campaign registry should use `cleenseau-template.md` as its default.
6. With the final note active in Obsidian, run `_templates/render-session-note.md`. This loads the three generated component files and renders `_templates/session-notes/cleenseau-template.md`.
7. Verify the rendered frontmatter and body against the reviewed recap. Make durable corrections upstream and regenerate instead of hand-maintaining rendered output.
8. Re-read all changed notes, validate frontmatter and wikilinks, review the complete scoped diff, and run `git diff --check`.

Session headers belong in the selected session-note template. Do not add Cleenseau session behavior to the generic `generate header` machinery or classify `session-note` as a general header page type merely to support this pipeline.

If the pipeline lacks a field needed by the approved format, fix the narrow pipeline gap rather than maintaining a hidden hand edit in generated output.
