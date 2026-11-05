---
name: classify-transcript-segments
description: Classify a registered polished RPG transcript into contiguous gameplay, combat, meta discussion, table talk, and narrowly defined session framing. Produces segments.json with source UID boundaries, without scene extraction or narrative summaries.
---

# Classify transcript segments — experimental draft

Produce **source UID range → activity category** for the entire transcript. This is a small set of activity bins, not scene extraction. Read [the segment format](references/format.md) before authoring. Keep this uninstalled draft's outputs in the agreed directory under `_sessions/time-location-testing`; preserve previous trials unless their revision is requested. Do not install skills or register outputs in session YAML as part of extraction.

Resolve the session's existing YAML and its registered `transcriptProcessing.artifacts.polishedMarkdown`; fingerprint both. Preserve the original source-local UIDs. Session identity + transcript revision + UID identifies a passage. A recap, reduced transcript, or existing scene map cannot replace the polished source.

Read the complete transcript sequentially before calling classification complete, rereading any truncated output. Search can help check boundaries but cannot establish complete coverage. If the source is incomplete or part cannot be read, disclose the concrete limitation; do not fill the unread portion with guessed gameplay.

## Categories and boundaries

| Category | Use |
| --- | --- |
| `gameplay` | Default for active play: roleplay, exploration, NPC speech, character decisions, in-character planning, ordinary rules adjudication, and narrated events. Includes travel montages, visions, flashbacks, dream sequences, and other developments in play. |
| `combat` | The complete span from entering initiative until initiative ends. A fight without an initiative roll also qualifies when participants establish and repeat an ordered turn cycle; start with the first turn in that cycle. |
| `meta_discussion` | Substantial out-of-character discussion of plot, goals, possible plans, or what the group wants to do next. Brief clarifications or suggestions during active play do not automatically create a new segment. |
| `table_talk` | Sustained unrelated conversation, scheduling, technical troubleshooting, or other interruptions outside the game. A brief joke or isolated unrelated comment stays in its surrounding activity. Opening or closing housekeeping can be as short as one line. |
| `session_framing` | Recaps, introductions, and similar framing narration outside active play that does not itself advance session events. This is a narrow category, not a label for DM narration generally. |

**Combat takes precedence throughout its continuous span.** Do not interrupt it for table talk, tactical planning, rule explanations, visions, or narration. Reactions, lair actions, and the death of the first actor do not terminate the segment. End when initiative is dropped, the encounter resolves, or escape ends the ordered action. If the transcript ends mid-combat, retain that segment and note the unresolved ending rather than inventing a conclusion.

**Use session framing sparingly.** An opening recap or overview of the wider world may qualify. Once the opening moves into what the characters actually experience or do, it is gameplay. Narrator identity, speech length, lack of player interruption, and the cinematic quality of a passage are not reasons to use framing. A six-day journey advances play and is gameplay. A narrated vision or flashback is gameplay, or combat if initiative is active. Do not emit `cutscene` or `dm_narration`.

Distinguish plans spoken by characters from players stepping outside play to debate options. Use conversational context and explicit transitions, such as the DM asking to move a discussion into character. Do not change categories for every pronoun, rules term, joke, or shift between direct speech and describing a character's intentions. For an extended mixed discussion, choose its main function; explain a material boundary choice briefly if necessary.

Place boundaries at whole polished turns; keep turns sharing source UIDs together. Choose the primary activity of an inseparable mixed boundary turn. Cover all readable turns once, in source order, without overlap. Merge adjacent spans of the same category unless they are separately bounded combat encounters. Changing topic, location, in-world date, speaker, or narrative viewpoint alone is not a boundary. Do not subdivide gameplay into named scenes.

## Output and verification

Write `segments.json` with the envelope and fields in the format reference. A segment needs only its local ID, source range, and category. Optional notes explain material boundary ambiguity; omit routine descriptions, confidence scores, review statuses, scene titles, summaries, and reading logs.

Verify JSON parsing, unique IDs, allowed categories, whole-turn/shared-UID boundaries, source order, and complete one-time coverage of the polished turns. Check combat starts and ends in context. Recheck every `session_framing` choice against the non-advancing-play rule; a file with no framing segment is valid. Verify source hashes still match. Preserve human corrections and existing IDs when revising, and identify changed boundaries for dependent combat extraction rather than silently updating fingerprints.

The JSON is the product. Give a concise handoff; render a table only when useful or requested. When showing the actual table, include all segments and their notes, not a compressed selection presented as complete. This skill does not infer dates or places, extract entities or interactions, summarize combat, or write campaign notes. Classification does not authorize downstream extractors to skip gameplay, combat, or other bins: relevant evidence can occur anywhere.
