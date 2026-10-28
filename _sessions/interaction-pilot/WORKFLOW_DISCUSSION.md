# Review and preprocessing — discussion starter

**Status:** recommendations for discussion, not adopted workflow rules. The [model overview](MODEL_OVERVIEW.md) records the agreed data design. The extraction skill has not been changed to implement that design or these recommendations.

**What the current pipeline already provides**

The source preparation stage supplies session identity, real-world date, participant/game-role mappings and a transcript with stable utterance IDs. The cleaner preserves those IDs while resolving transcription problems and marking unresolved text. Existing beats and annotations may also contain date evidence, location candidates and lists of NPCs, items and organizations.

For example, the [Dunmari 108 manifest](../dunmar-frontier/dunmari-frontier-108/cleaned/dunmari-frontier-108-session.yaml) has participant/game-role mappings and session dates; its [beats](../dunmar-frontier/dunmari-frontier-108/cleaned/dunmari-frontier-108-beats.json) have source ranges and chronology evidence; its [beat facts](../dunmar-frontier/dunmari-frontier-108/cleaned/dunmari-frontier-108-beat-facts.json) have locations and candidate entities. Those facts do not automatically establish every interaction, and their recap-oriented boundaries are not the interaction scene model.

**Preprocessing recommendation**

Reuse a prepared, cleaned transcript and available session metadata. Do not require running the entire narrative-recap pipeline to extract interactions.

A lightweight first pass over the full transcript would be useful to assemble:

- Name variants and candidate vault matches, including identities revealed later in the session.
- Candidate locations and narrative subplaces.
- Date/time anchors, meaningful transitions and unresolved chronology.

This is a working index for extraction, not another source of events. Existing beat facts can seed it when available, but the transcript remains the evidence. Lexical matching alone cannot decide whether an NPC is present, whether a name refers to a PC or NPC, or whether two unnamed people are the same person. A failed vault match should leave a descriptive label or unresolved reference; it should not force a match or automatically create a note.

Construct provisional scenes from source boundaries and chronology, then entity cards and whole interaction units. Allow context discovered during extraction to revise provisional matches and boundaries before review. The preprocessing pass need not be a separate skill, a permanent artifact, or a mandatory human approval checkpoint. Whether it should be any of those is still open.

**Review recommendation**

Produce a complete candidate extraction before routine human review. Present it in small, navigable parts:

1. Session metadata and scene map: dates, locations and source boundaries.
2. Entity matches and cards: inclusion, whole interactions, source passages and quote choices.
3. Focused unresolved questions, with source links and proposed corrections.

Keep uncertain identities and dates visible in the review rather than filling them with guesses. Corrections to shared data should propagate to dependent records before acceptance. A scene-boundary change needs corresponding interaction/passage checks. Quote text and source links should remain inspectable alongside the proposed cards.

Check source references, joins, enum values and exact quotation text mechanically. Human review judges meanings, identities, chronology and useful scope. A passing validator does not make the draft accepted. Once accepted, changes should preserve human edits and make subsequent differences reviewable; regeneration should not silently overwrite the canonical `session.json`.

**Decisions still to make together**

- Should review begin with a complete draft, or should the scene map be approved before interactions are generated?
- What unit can be accepted or corrected: the session, a scene, an entity, or an individual interaction/quote?
- How should unresolved issues, review decisions and candidate matches be stored and presented? No storage format or interface is selected yet.
- Which ambiguities justify pausing extraction early, and which can remain unresolved in an otherwise useful draft?
- What should reprocessing do when the transcript or an accepted record has changed?

The first useful decision is the review checkpoint. A complete draft gives the reviewer the entity and interaction context needed to judge scene boundaries; reviewing scenes earlier could avoid rebuilding dependent records. My initial recommendation is complete-draft review, with an early question only when missing or ambiguous input would materially undermine the extraction.
