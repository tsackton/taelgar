---
name: extract-entity-passages
description: Extract focused, complete interactions for selected entities from an entity map with assessed session importance. Cut progressively tighter for supporting entities and cameos. Keep original speech and actions, minimal setup, and marked cuts; never rewrite or summarize. A scene map is optional.
---

# Extract Entity Passages

Use for readable source passages showing what an entity said, did, or was described
as. The agent selects, bounds, and cuts; it does not write replacement narrative.
Read [calibration](references/calibration.md) before the first extraction in a
conversation.

## Inputs and scope

Resolve the selected session YAML and its registered
`transcriptProcessing.artifacts.polishedMarkdown`. Reuse YAML participant roles
and source registration. The source reader in
`../prepare-interaction-transcript/scripts/interaction_draft.py`,
`load(session_yaml, for_draft=False)`, checks source integrity and reads turns
without writing. This retained implementation requires Python 3.9+ and PyYAML;
its former draft-authoring skill is retired.
Do not initialize a reduction draft to extract passages. Recaps, beat narratives,
vault biographies, and reduction labels are not substitutes for source speech.

Require a current, validated v4 entity map with session importance assessed for
every entity. Read the [importance calibration](../check-session-entities/references/importance.md).
Readable legacy v3 maps have no importance assessment; complete that mapping
review before new extraction. If absent or stale, complete the separate
`../check-session-entities/SKILL.md` workflow first within the authorized scope;
do not silently substitute an ad hoc inventory or fabricate source registration.
Preserve unnamed labels, session-era identities, and ambiguity.

A user-requested correction to cuts in an existing trial can restore source text
without first reclassifying the whole session. Validate its recorded source/map
provenance, keep importance explicitly unassessed, and limit the revision to that
feedback; this exception does not authorize a new extraction batch.

Before extracting, identify the selected **focal entities** by session-local entity ID and
label. Use explicit user selections; otherwise present a compact map-based shortlist
for selection. A request for maps first stops at that shortlist. Do not default to
extracting every mapped entity. During calibration, use a small selected batch
(normally one to three entities) and expand only after feedback. An explicitly
requested target outside the map inventory, such as a PC, must be named as an
exception; the session still requires its entity map.

Declare the focal entity or entities for each passage. Other entities may speak or act
as supporting participants without becoming additional focal entities. Co-focal entities must be
explicitly selected, not added just to justify retaining more background. State a
short editorial focus outside the excerpt, such as “the ocean challenges the
intruders”; this is a selection description, not replacement narration.

Default to chat excerpts. A request to save, or an established output destination,
authorizes a saved derivative; otherwise do not persist a report. Default saved
destination: `cleaned/<stem>-entity-passages.md`. Follow repository Git instructions
before writing. Read any existing output completely and preserve unrelated
entities and human edits. Sources, YAML, maps, vault notes, and `session.json`
remain unchanged. Do not commit or publish automatically.

## Locate candidate scenes

Read the contracts for maps actually used:
`../check-session-entities/references/format.md` and
`../map-transcript-scenes/references/format.md`. Validate maps with their read-only
helpers. If the entity map is absent or stale, return to the mapping stage. If an
optional scene map is absent or stale, use entity occurrences and original-source
reading; do not replace fingerprints to make a map appear current.
Reuse accepted identity decisions without rematching them.

1. With known entity-to-scene links supplied by the user or an existing artifact,
   read those scenes and boundary context first. Verify indexes against the
   current map revision.
2. With entity occurrences and a scene map, intersect occurrence ranges with
   scenes/context blocks and read the containing windows.
3. With occurrences alone, expand backward and forward to understand the complete
   encounter or discussion, including unnamed speech and pronouns. Reading that
   context does not mean retaining it. Searches orient reading but cannot replace
   it: DM dialogue and unnamed appearances often lack the name.

Current entity-map occurrences are representative identity evidence, not a
complete scene-membership list. Do not add scene fields to that map. Geographic
scene membership proves neither attendance nor centrality. Recaps and lore
discussions remain eligible; preserve their framing.

For mapped scopes, scan outside candidate windows for other names/variants and
follow newly found discussions. For comprehensive session coverage without known
complete membership, read the remaining source in order. Otherwise label the
result as selected-scene or occurrence-led extraction, not exhaustive. Respect an
explicitly limited scene scope, expanding boundaries only as needed to finish the
exchange. Maps should reduce reading work, not silently truncate conversations.

## Select complete moments where the entity is the focus

The entity is central as a principal participant, the object of a meaningful
action, or the substantive subject of discussion/description. This is a local
selection rule, not a requirement for an existing `importance: star` rating. A
minor session entity can be the focus of one sentence; an absent entity can be the
focus of a discussion. Presence, a name drop, or a name embedded in a place label
alone is insufficient.

- Start with the core exchange: what the focal entity says, does, reveals, undergoes, or
  is substantively described as, plus the other participants' relevant responses.
  Add only the setup needed to understand who is involved and what prompts it.
- Completeness is relative to that focal interaction, not the entire encounter,
  journey, preparation, or battle. Preserve its question/answer, action/reaction,
  important qualification, and outcome when the source supplies them. Do not
  manufacture closure if the session ends mid-interaction.
- A complete scene here means an intelligible focal moment, not necessarily
  one geographic scene-map record. It can occupy part of one or cross several.
  Do not alter map boundaries to match the extracted passage.
- Use the shortest passage that preserves the substance and character of the
  interaction. One substantive sentence can suffice; a major negotiation may
  need many turns. Do not pad short moments or compress important exchanges to
  highlights merely to meet a word cap. A long source scene is not itself a reason
  for a long excerpt.
- Prefer whole exchanges over scattered highlights. Snip brief interruptions or
  unrelated digressions within one passage. Separate later encounters, recollections,
  and distinct discussions; do not stitch them into apparently continuous speech.
- Preserve continuous narration as a coherent passage. A character's account or
  an unfolding vision may introduce other people, places, and events that belong
  to its narrative. Do not remove those stretches merely because the focal entity
  is not the grammatical subject of every line. Cut table interruptions around
  the account; retain its development, transitions, and natural endpoint.
- Retain revealing gestures as well as major actions. Speech, action, and description
  do not need separate mandatory categories.
- For explicitly selected co-focal entities, one shared passage may serve both. Otherwise
  judge every retained stretch against the declared focal entity, not every entity present.
- If no meaningful central passage exists in the inspected scope, say so. Do not
  fill the gap with peripheral mentions or an AI overview.

## Use session importance to set extraction depth

Read the selected entity's `importance` from the map. Being selected as a passage's
focus does not promote it to `star` or `supporting` in the session. Stars can merit
several substantial interactions; supporting entities merit their meaningful
scene with tighter cuts; cameos need much tighter cuts, often just one sentence
or a short exchange with almost no background. Do not preserve a long approach,
search, rules discussion, or another entity's story around a cameo.

Use tiers to judge relevance, not as word limits. Keep necessary questions,
responses, qualifications, actions, outcomes, and continuous narration. Lower
importance does not justify fragmenting a selected coherent account. Prefer
tighter setup and fewer separate passages over cuts through that account.
If the mapped tier seems wrong,
return to entity assessment rather than silently changing it or inflating the
excerpt to justify a promotion. The session-99 calibration classifies Caloria,
Martino, and the Immovable Rod as cameos, and Dorian, Kazuro, and the Sentient
Ocean as supporting.

## Snip irrelevant material; never rewrite

### Items: brief use or acquisition, complete original lore

For items, default to a much tighter passage than for a character: the minimum
original wording needed to understand how the item was used or acquired, by whom,
and the relevant result or limitation. Apply the same economy to transfers,
discoveries, losses, and destruction. A higher importance tier does not by itself
justify keeping the surrounding encounter, equipment discussion, repeated rules,
or hypothetical uses. Preserve only mechanics needed to understand this action.

The exception is original in-world history or lore invented for the setting:
usually extract that account fully, with its continuous narration, transitions,
qualifications, and meaningful clarifications. This includes a custom history
for an otherwise standard rules item. A reading of standard item mechanics is
not this exception. Do not invent lore or assume that every magical property is
custom lore; when uncertain, retain the supported in-world account without
claiming external originality. Keep separate use/acquisition and lore moments
separate rather than attaching all surrounding item discussion to the lore.

When the item was specifically examined in the **Mirror of the Past** during this
session, display **Mirror of the Past: examined** alongside its passage heading
and carry `examinedInMirrorOfPast: true` in saved focal-item metadata. New runs
consume the entity map's flag and its occurrence evidence. A correction to a
legacy trial can flag a source-verified examination in that derivative without
silently migrating its map. Preserve the resulting history/vision as a coherent
lore passage, including events involving other participants in that history.
Flag the item being examined, not every item visible in the vision or the mirror
merely used to view it. Proposed examinations, recollections of earlier sessions,
unrelated visions, and the Mirror of Soul Trapping do not establish this flag.

### General cutting rules

Read the complete candidate exchange before cutting. Remove irrelevant material
as much as possible while preserving the target's meaningful interaction. Unlike
the session-wide reduction draft, this selection need not preserve unrelated
material about other entities.

For each retained stretch, ask: does this show the focal interaction, or is it
part of its coherent narration, or indispensable to understanding it? If none,
cut it. Preparation that merely
enables reaching the focal entity is usually dispensable. For each cut, ask: did this
remove the focal entity's speech, action, response, or a necessary counterpart? If so,
restore the original words. A passage dominated by setup while the focal entity's actual
interaction is missing or reduced to a cut label fails even if every word is exact.

Mark every internal omission with `((short description))`. Inline and whole-turn
cuts are both useful. Material outside selected boundaries need not be described,
but mark omissions at the start/end of a partially retained source turn. Prefer
one coherent cut over many tiny ones when the entire intervening stretch is
irrelevant.

Usually snip dice arithmetic, initiative, interface issues, unrelated banter,
redundant planning, repeated explanations, other entities' unrelated business,
and verbal scaffolding that adds nothing. Keep mechanics that explain a meaningful
property, limitation, uncertainty, choice, action, or consequence. In combat retain
the entity's distinctive actions, threats, responses, attempted escape, defeat,
and aftermath; cut routine attacks and bookkeeping.

Cut labels are the only generated connective text inside an excerpt. They describe
omitted material briefly, e.g. `((Spell mechanics))`. An omitted action/outcome may
be described only when supported by the removed source. Do not invent motives,
resolve ambiguity, or replace the target's important dialogue/actions with a
miniature summary. If a label carries the reason the passage matters, restore
the relevant original words.

Retained wording, spelling, punctuation, capitalization, and speaker labels remain
exact. Do not fix grammar, complete unfinished sentences, normalize names, change
person/tense, combine speakers, or add quotation marks. Preserve retained
`{{...}}`, `[garbled]`, wikilinks, and other uncertainty. Do not cut inside words
or uncertainty markers. If original speech contains `((...))`, explicitly
distinguish it from editorial markers rather than silently treating it as a cut.

Preserve attribution, hedges, negation, alternatives, corrections, and disagreement.
Do not turn plans into events, attempts into successes, or claims into established
facts. Keep enough context to resolve pronouns and DM-spoken lines, including
switches between NPCs or narration. A brief separate attribution note is allowed;
silently relabeling DM speech is not. Later vault knowledge must not change what
the session said or knew.

## Output and provenance

Group passages by entity, in source order within each entity. Provide short
navigation labels, explicit focal IDs/labels, mapped session importance, editorial focus, source links,
and inclusive whole-turn UID ranges. Explain
`((...))` once. Put necessary framing (recap, speculation, reported claim, or NPC
attribution) outside the excerpt. Do not append AI summaries, trait lists,
biographies, or motive explanations. Discuss editorial choices outside the
extraction only when useful in exploration or requested.

For saved derivatives:

- Record vault-relative session YAML, the YAML source artifact key, and polished
  source SHA-256 in an opening provenance comment. Record paths and byte hashes
  of the required entity map and any scene map used. Record selected focal IDs and
  any explicit target exceptions; identify each passage's focal entities alongside its
  source range and mapped importance. Do not add passage-focus fields to the entity map or create another
  metadata/source registry.
- State reading scope: complete session, selected scenes, or occurrence-led.
- Give each passage a source range. Preserve original UID/offset comments on
  retained turns. Whole-turn snips retain the omitted turns' span entries in source
  order with their cut label. Offsets still refer to cleaned source, not display
  text or invented sub-turn alignment.
- Ranges respect whole polished turns and whole UIDs, including combined/shared
  UIDs. Displaying a cut-down turn does not authorize a partial-UID locator.
- Overlap across different entities is legitimate. A local reference to a shared
  passage may avoid duplication. Within one entity prefer a complete passage to
  redundant overlapping excerpts.

This derivative is neither final v7 enrichment nor a full-coverage reduction
draft. Do not put cut-bearing text into v7 verbatim `quotes`. The existing
full-draft validator does not validate a partial entity collection. Extraction
does not migrate maps, add a review-status store, or register final output;
complete any prerequisite map upgrade through the entity-mapping workflow.

## Verify and hand off

Make a distinct second pass over each selected original range and its neighbors:

1. Check the declared focal entities, mapped importance, and completeness: minimal necessary setup,
   substantial exchange, relevant responses, and the actual endpoint. Would a
   reader learn mostly about preparations or supporting entities? If so, refocus.
2. Inspect every cut and retained stretch. Restore lost qualifiers, attribution,
   corrections, needed replies, or meaningful actions; cut remaining irrelevant
   material. Verify descriptions of cuts against the omitted source.
3. Compare retained text with corresponding original turns in order, including
   speakers/punctuation. Check marked omissions and whole-turn source ranges.
   The draft reader's `match_inline` can check individual cut-bearing turns when
   their labels fit its syntax; it is not a collection or semantic validator.
4. Check identity, recap/played-event framing, and continuity across cuts. Prior
   map review does not review the new extraction.
5. Before saving, recheck inspected source/map hashes and prior output state.
   Re-read changed evidence rather than overwriting hashes. Review the saved
   derivative, scoped diff, and unchanged inputs.

Return excerpts or the saved file plus material uncertainty/scope limitations.
For calibration, present the selected batch alone rather than another full-session
collection. Retain earlier trials for comparison unless replacement was requested.
Do not require approval of every clear passage. Human-reviewed means the user
actually reviewed that selection and its cuts, not merely the skill or maps.
