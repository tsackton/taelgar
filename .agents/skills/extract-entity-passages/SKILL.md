---
name: extract-entity-passages
description: Build interactions.json from a mapped session's polished transcript. Extract coherent exchanges with original text and marked cuts, per-exchange entity roles and actions, source provenance, and review confidence. Use for selected interaction trials or an explicitly requested session scope; scene maps are optional.
---

# Extract Entity Passages

Build exchange-based `interactions.json`, showing what entities said, did, or were
described as. Each record holds one coherent exchange or continuous account, its
extracted Markdown lines, one or more focal entities, and five original text lines
on either side for boundary review. Select, bound, and cut;
do not write replacement narrative. Read [the format](references/format.md) and
[calibration](references/calibration.md) before the first extraction in a conversation.

## Inputs and scope

Resolve the selected session YAML and its registered
`transcriptProcessing.artifacts.polishedMarkdown`. Reuse YAML participant roles
and source registration. The source reader in
`../prepare-interaction-transcript/scripts/interaction_draft.py`,
`load(session_yaml, for_draft=False, allow_unknown_dates=True)`, checks source integrity and reads turns
without writing. It requires Python 3.9+ and PyYAML; the interaction validator
also uses jsonschema, listed in [requirements.txt](requirements.txt).
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
(normally one to three entities) and expand only after feedback. For an explicitly
requested whole-session extraction, select coherent exchanges across that scope
without requiring an entity-by-entity shortlist. Every serialized entity ID must
resolve in the bound map. PCs may speak and act in the text through YAML-owned
roles without entries in the entities array. A requested focal target absent from
the map needs a separately authorized mapping/model decision; do not invent an ID
or change the map to make the extraction fit.

Declare focal entities as interaction-local `role: star`. Other mapped entities
represented in retained text may be `supporting` or `cameo`; these entries do not
authorize expanding the extraction. For a selected-entity trial, additional stars
must also be selected, not added to justify background. A short `title` provides
navigation; it is not extraction reasoning or a replacement summary.

A request to build or save interactions authorizes the scoped derivative at
`cleaned/<stem>-interactions.json`. A request only to discuss, propose, or preview
stays in chat. Read an existing output completely and inspect its local changes;
preserve unrelated exchanges, stable IDs, and human edits. Existing Markdown
trials remain untouched unless their conversion or replacement is requested.
Sources, YAML, maps, vault notes, and `session.json` remain unchanged. Do not
commit, publish, or register output in YAML automatically.

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
result in the handoff as selected-scene or occurrence-led extraction, not exhaustive.
Respect an explicitly limited scene scope, expanding boundaries only as needed to
finish the exchange. Maps should reduce reading work, not silently truncate conversations.

## Select complete moments where the entity is the focus

The entity is central as a principal participant, the object of a meaningful
action, or the substantive subject of discussion/description. This is a local
selection rule, not a requirement for an existing `importance: star` rating. A
minor session entity can be the focus of one sentence; an absent entity can be the
focus of a discussion. Presence, a name drop, or a name embedded in a place label
alone is insufficient. Map inclusion does not require an extracted interaction.
Routine combat participation alone does not qualify as a substantive interaction;
apply the [combat rules](#combat-minimal-encounter-records-meaningful-exchanges).

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
  This does not require preserving a played battle's sequence of attacks.
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

## Assign interaction-local entity roles and actions

Use one `entities` array per exchange, with `{id, role, action}` for each mapped
entity represented in retained text. Require at least one `star`, the local focus.
`supporting` contributes meaningfully or is needed to understand the exchange;
`cameo` is a brief relevant appearance or mention. These local roles are independent
of entity-map session importance: a session cameo can star in its one short exchange.
Do not list an entity whose entire contribution was cut, or inventory every passing
name merely because it falls within the original source range.

Classify each entity's involvement relative to the party:

- `interacted`: meaningful direct exchange or action, including fighting, rescue,
  threats, help, or using an item.
- `observed`: perceived or examined without a direct exchange.
- `present`: established as there, without substantive selected action or observation.
- `mentioned`: discussed or described without establishing participation in the
  current encounter. An absent entity can be the star of a discussion.

These action labels classify retained material; they do not make routine fighting
eligible for its own interaction.

Use the most substantive supported involvement within the exchange, rather than
separate entries for seeing and then speaking to the same entity. Recaps, reported
history, speculation, prayer, and attributed divine intervention alone are mentions;
they do not establish a current direct encounter. A played manifestation or exchange
can support observation or interaction. Keep this framing intelligible in the source
text itself. `seen` is not a separate action value.

## Snip irrelevant material; never rewrite

### Combat: minimal encounter records, meaningful exchanges

For combat without substantive in-world conversation, retain a very short source
excerpt establishing the encounter and its outcome or lasting consequence. Default
to one brief record for the continuous encounter, with the intervening combat cut;
do not split it into records for attacks, abilities, or rounds. Retain only enough
original description to identify the encounter and understand the result. Do not
invent an outcome for an unfinished fight. This tighter depth applies at every
session importance tier, including a star or the main enemy in a climactic battle.

Remove all combat mechanics: rolls, damage, saves, AC, initiative, action economy,
movement measurements, resource accounting, rules explanations, and tactical
discussion. Cut the sequence of attacks and routine maneuvers, including narrated
hits, misses, and ability effects. A vivid description or unusual power does not
by itself warrant retention. Keep a meaningful fictional consequence in original
wording while cutting the mechanics that resolved it; a choice or consequence is
not a reason to restore those mechanics.

Preserve substantive conversation during combat, including demands, revelations,
negotiation, surrender, and relevant responses, with only the battle context needed
to understand it. Tactical table talk is not such a conversation, and a brief taunt
does not justify retaining the surrounding fight. Independently meaningful character
actions can also merit extraction without dialogue: a refusal, unexpected decision,
meaningful rescue, sacrifice, or consequential loss. Routine combat assistance does
not qualify merely because it helped the party win.

Do not create standalone interactions for companions merely attacking, moving,
following combat commands, or using their ordinary abilities. A mapped companion
may have no qualifying interaction in the session. Include one in a retained
encounter's entities only when its retained involvement warrants it; do not keep
extra combat text to ensure a companion is represented.

Preserve substantive lore discoveries and character responses in the aftermath at
their appropriate depth. Proximity to a fight does not make them combat bookkeeping.
Keep these distinct exchanges separate from the brief combat record. Use original
text and marked cuts throughout, not a generated battle summary or a cut label
standing in for the encounter's meaningful outcome.

### Items: brief use or acquisition, complete original lore

For items, default to a much tighter passage than for a character: the minimum
original wording needed to understand how the item was used or acquired, by whom,
and the relevant result or limitation. Apply the same economy to transfers,
discoveries, losses, and destruction. A higher importance tier does not by itself
justify keeping the surrounding encounter, equipment discussion, repeated rules,
or hypothetical uses. Outside combat, preserve only mechanics needed to understand
this action; combat uses follow the tighter rules above.

The exception is original in-world history or lore invented for the setting:
usually extract that account fully, with its continuous narration, transitions,
qualifications, and meaningful clarifications. This includes a custom history
for an otherwise standard rules item. A reading of standard item mechanics is
not this exception. Do not invent lore or assume that every magical property is
custom lore; when uncertain, retain the supported in-world account without
claiming external originality. Keep separate use/acquisition and lore moments
separate rather than attaching all surrounding item discussion to the lore.

When the item was specifically examined in the **Mirror of the Past** during this
session, consume the entity map's `examinedInMirrorOfPast` flag and its occurrence
evidence. Preserve the resulting history/vision as a coherent lore passage,
including events involving other participants in that history. The flag remains
owned by the entity map; do not copy it into the lean interaction records. A chat
preview may display **Mirror of the Past: examined** from the bound map. A targeted
correction to a legacy Markdown trial may retain its existing source-verified flag
without silently migrating the map.
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
remove substantive dialogue, an independently meaningful action or response, or a
necessary counterpart? If so, restore the original words. Do not restore routine
combat actions or mechanics merely because they belong to the focal entity.
A passage dominated by setup while the focal entity's actual
interaction is missing or reduced to a cut label fails even if every word is exact.

Mark every internal omission with `((short description))`. Inline and whole-turn
cuts are both useful. Material outside selected boundaries need not be described,
but mark omissions at the start/end of a partially retained source turn. Prefer
one coherent cut over many tiny ones when the entire intervening stretch is
irrelevant.

Usually snip dice arithmetic, initiative, interface issues, unrelated banter,
redundant planning, repeated explanations, other entities' unrelated business,
and verbal scaffolding that adds nothing. Outside combat, keep mechanics only when
needed to explain a meaningful property, limitation, uncertainty, choice, action,
or consequence. For combat, apply the tighter rules above.

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
switches between NPCs or narration. Preserve source attribution rather than
silently relabeling DM speech or inserting new narration. Later vault knowledge
must not change what the session said or knew.

## Output and provenance

Author the [interactions v1 format](references/format.md), enforced structurally by
[interactions.schema.json](references/interactions.schema.json). Store exchanges
in source order, not grouped into duplicate copies per entity. Reuse stable IDs on
revision; one shared record can serve multiple selected stars. Separate encounters
remain separate. Overlap is allowed when distinct exchanges need common context,
but avoid redundant overlapping extracts of the same exchange.

Store original Markdown as `lines`, one physical line per array entry, including
blank lines and original UID/offset comments. Whole-turn snips retain the omitted
turns' source spans in order beside their cut label. Join with `"\n"` for display;
do not embed newlines inside an entry or rewrap original retained prose. Outer
source ranges respect whole turns and shared UIDs; offsets still refer to cleaned
source. The title is the only content summary. There is no `framing`, separate
`focalEntities`, copied entity metadata, scene anchor, or v7 quote collection.

Bind the document to session YAML, the registered polished-source byte hash, and
the entity-map path and byte hash. A scene map may assist discovery, but the saved
artifact has no scene-index dependency. Do not create another participant/source
registry. Explain reading scope and material limitations in the handoff, rather
than adding undeclared schema fields. Empty interactions are permitted; say when
the inspected scope yielded no meaningful exchange.

Each interaction also requires `reviewContext: {before, after}`. Populate it with
the five nonblank original physical transcript text lines immediately outside the
complete source range, or fewer only where the transcript ends. Keep original
wording/speaker labels; exclude blank lines and UID/offset comments. Use the
helper's read-only `context` command documented in [the format](references/format.md)
instead of selecting favorable context. Do not add these lines to `lines`, widen
source bounds, or classify entities appearing only in review context. In HTML or
other readable reviews, show them by default above and below the interaction in
smaller, muted/grey text. Internal cut and summary disclosures show the raw omitted
or summarized source only, without their own before/after windows. The five-line
before/after context belongs only to the whole interaction.

`review` is optional in the format; new agent-authored exchanges should include
it. Confidence covers selection, boundaries, roles/actions, retained text, and
cuts. Put a concise, specific explanation in `review.reason` for `medium` or `low`
confidence; it is optional for `high`. A reason explains the uncertainty in this
extraction, not the entity's biography or a chain of reasoning. Start unreviewed;
use `automatedReviewed` only after the distinct second pass below. Use
`humanReviewed` only after the user actually reviews that exchange and its cuts.
Map approval and schema validation establish neither. Omitted review means no
attestation. Preserve human-reviewed records on reruns; if their evidence changes,
report the conflict rather than silently replacing them. Changed agent records
need a fresh review, not a carried-forward attestation.

This artifact replaces the Markdown collection as this skill's authored output;
it does not enrich v7 `session.json`, migrate maps, or register final output.
The existing full-draft validator does not validate this partial collection.

## Verify and hand off

Make a distinct second pass over each selected original range and its neighbors:

1. Check the declared focal entities, mapped importance, and completeness: minimal necessary setup,
   substantial exchange, relevant responses, and the actual endpoint. Would a
   reader learn mostly about preparations or supporting entities? If so, refocus.
   For combat, check that routine companion participation has not become a standalone
   interaction, mechanics and attack sequences are cut, and only a brief encounter
   record remains unless substantive conversation or character action warrants more.
2. Inspect every cut and retained stretch. Restore lost qualifiers, attribution,
   corrections, needed replies, or meaningful actions; cut remaining irrelevant
   material. Verify descriptions of cuts against the omitted source.
3. Compare retained text with corresponding original turns in order, including
   speakers/punctuation. Check marked omissions and whole-turn source ranges.
   The draft reader's `match_inline` can check individual cut-bearing turns when
   their labels fit its syntax; it is not a collection or semantic validator.
4. Check identity, local roles/actions, recap/played-event framing, and continuity
   across cuts. Prior map review does not review the new extraction. Check the
   review confidence and conditional reason after this pass.
5. Run the read-only helper with Python 3.9+, PyYAML, and jsonschema available:

   ```bash
   python -B .agents/skills/extract-entity-passages/scripts/interactions.py validate PATH_TO_INTERACTIONS_JSON
   ```

   It checks schema, conditional reasons, provenance, entity references, source
   order, UID boundaries, source-span accounting in `lines`, and the exact adjacent
   source text in `reviewContext`. It does not prove
   retained wording, appropriate cuts, classifications, or semantic review.
6. Before saving, recheck inspected source/map hashes and prior output state.
   Re-read changed evidence rather than overwriting hashes. Never update the root
   map hash while carrying forward uninspected exchanges: revalidate their entity
   references and review any relevant map-decision changes first. Review the saved
   derivative, scoped diff, and unchanged inputs. Validation must also pass on the
   saved bytes; rerun it only if those differ from the validated proposal.

Return the saved JSON or requested preview plus reading scope and material
uncertainty/limitations. A preview may render `lines` as Markdown and resolve
labels from the map; do not persist an extra Markdown report by default.
Show the persisted boundary context visibly when rendering a requested review.
For calibration, present the selected batch alone rather than another full-session
collection. Retain earlier trials for comparison unless replacement was requested.
Do not require approval of every clear passage. Human-reviewed means the user
actually reviewed that selection and its cuts, not merely the skill or maps.
