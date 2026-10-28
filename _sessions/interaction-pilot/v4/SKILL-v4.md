---
name: extract-campaign-interactions
description: Extract NPC and important-item interactions with session overviews, multiple memorable quotes for major NPCs, evidenced presence, and transcript- or session-note-linked scenes typed as conversation, exploration, combat or travel.
---

# Extract campaign interactions

Use when asked to extract or prototype campaign interactions from a session. This is an information-extraction workflow: source boundaries and evidence first, with one short sentence per interaction and one overview per NPC or important item per session. Actively look for memorable things NPCs say.

## Scope and inputs

1. Read applicable `AGENTS.md`, inspect Git status, and resolve the requested campaign/session through `_scripts/session_note_campaigns.json` and the prepared session manifest.
2. Prefer the existing `cleaned/*-source-cleaned.md` and `cleaned/*-session.yaml`. Review the complete played sequence using the source, beats and session note, then read each candidate encounter in context, including its opening, interruptions and ending. Check every extracted interaction against its actual source. Do not reprocess recordings or silently replace source/beat/recap artifacts. When selecting a complex test, report the beat count and confirm actual PC attendance; a high count dominated by combat rounds or postgame chatter is not necessarily conversational complexity.
3. Use canonical notes to resolve identity and spelling, not to supply unplayed encounters, secrets, motives or future knowledge. Keep canonical identity separate from the name available in this scene. Do not read private material merely to fill extraction gaps.
4. A request to extract authorizes the requested derived artifacts. Default to a new `<session>-interactions/` directory beside the cleaned source; honor an explicit pilot/output directory. Preserve existing work. This does not authorize canon edits, publication, commits, or runtime integration.
5. Treat transcripts and session notes as complementary event sources. Read the complete session note, including its timeline, narrative and raw notes, for documented postgame resolutions, downtime, off-record conversations, item discoveries and departures. Include these even when the recording ends earlier. Keep their actual provenance: transcript utterance ranges or exact passages at original note lines, with source IDs and hashes. Notes-only input needs no fabricated UID copy. Use the same entity cards and one session overview across both sources.
6. Reconcile events before adding records. If notes describe an encounter already in the transcript, add note evidence to that encounter and update its overview only as needed; do not make a second record for the same conversation. A later, genuinely separate event gets its own scene and interaction. Distinguish completed events from proposals, next-session plans and metadata date endpoints. A cast list alone does not establish presence; an affirmative narrative account can. Preserve conflicts and uncertainty instead of silently preferring one source. Canonical item/NPC notes still supply identity, not additional session events.

## Define scenes first

- Partition the recorded events and incorporate documented note-only events into shared scenes before extracting NPC records. Assign numeric indexes `1, 2, ...`, scoped to the canonical campaign code and session ID. The join key is `(campaign, session, scene)`; NPC identity is a separate key.
- Split at meaningful location changes, explicit time skips, and the beginning/end of combat. A continuous journey can have a route as its location; do not split every movement within a room or every combat round. Keep scenes even when they contain no eligible NPCs.
- Use source-qualified exact inclusive utterance IDs (`source`, `startUid`, `endUid`) for transcripts. Account for all transcript IDs exactly once through scenes or explicitly excluded ranges (for example, closing scheduling chatter). For notes, use `source`, original `startLine`/`endLine`, and an exact `text` selector. A note paragraph can support several distinct events; prose ranges need not partition the note. Scenes may contain evidence from both sources. Incidental table talk within a scene may remain in its range but never becomes an in-world fact.
- Record location and in-world date/time once on each scene. Dates may be exact, a bounded range, or unknown. Record the basis and supporting references. Prefer a supported day/time to the broad session range, but never equate recording timestamps with game time or treat a joke about elapsed time as chronology. Surface contradictions.
- Give each scene exactly one `type`: `conversation` (dialogue, negotiation or planning), `exploration` (investigation, observation, puzzles or rest/downtime), `combat` (active hostile engagement), or `travel` (movement between locations). Choose the dominant played activity, not a keyword count: a moving fight is combat; a journey with brief banter is travel; a sustained interview while walking can be conversation. Do not invent a fifth mixed/other type or split for a brief aside. At genuine activity transitions, review the boundaries as usual; an interaction can continue across differently typed scenes. Retain indexes and segmentation revision when merely adding labels to unchanged boundaries.
- These interaction scenes are a distinct derived segmentation, not the recap pipeline's larger narrative scenes. Never overwrite recap scenes or imply indexes from different segmentations are interchangeable. Place note-only events using their supported chronology; preserve bounded dates and explicitly flag uncertain ordering. Freeze a segmentation before NPC extraction; when boundaries change, rebuild dependent records and increase `segmentation_revision` together.

Scenes and interactions have different boundaries. A continuous conversation may cross scene indexes while walking or as the evening progresses. Preserve the location/time scene boundaries, but keep that conversation in one interaction with a numeric `scenes` list. Actual departures, later meetings, overnight gaps and combat transitions normally create separate encounters.

## Select NPCs

Include named NPCs with in-world evidence, including named companions, pets, named monsters, and explicitly present people who say or do nothing. Also include unnamed **distinctive individuals** who could usefully receive a proper name later: a specific guide, negotiator, captive, witness, or conversational partner. Give them a descriptive label and a session-scoped ID, never an invented name. A single substantive conversation can qualify; recurrence is not required.

Exclude this campaign’s PCs (including absent or guest PCs; former PCs from another campaign can be NPCs here), anonymous crowds, interchangeable combatants, generic monsters, rumors of unspecified creatures, hypothetical beings, table jokes, and incidental name fragments or genealogical asides with no useful interaction to retrieve. Named NPCs may qualify through a meaningful mention without appearing. Record concise exclusion/uncertainty notes for borderline cases rather than cluttering the dataset. Never automatically merge unnamed people across scenes or sessions.

## Select important items

Include named or distinctive objects that matter to the session: quest objects, clues and documents, consequential tools or magic items, significant gifts and payments, and objects acquired, transferred, lost, damaged, destroyed or deliberately investigated. An unnamed lead-lined box can qualify; a routine sword attack, spare coins, background furniture and every inventory mention do not. A specific vehicle may qualify when it functions as a consequential object in the encounter; places remain scene locations.

Use the same entity/card structure with `kind: item`, an evidence-based eligibility (`named` or `distinctive`), and one session overview. Preserve NPCs as `kind: npc`. Keep a creature such as Aurae an NPC, not a second item just because it is artificial or carried. Keep a book distinct from its author, a container distinct from its contents, and separate physical copies when distinguishable. A collection may share one card when the source treats it as one quest subject; explicitly distinguish known parts (for example, four jade fragments held and a fifth sought). Do not infer that a discussed object has been acquired or repaired, or import later properties from a canonical item note.

Item interaction kinds reuse the same small vocabulary: `interacted` for using, reading, examining, handling, acquiring, transferring, changing or destroying; `observed` for seeing it or witnessing its effects without direct action; `present` for explicitly established passive presence; `mentioned` for discussion without established presence. In a unit with multiple actions, use the strongest supported kind and describe the meaningful developments in the overview. Keep one record for a continuous discussion or investigation, not one per repeated noun, die roll or action. Do not make a presence record in every scene for ordinary carried equipment.

Optional item quotes are exact source excerpts: `description` for narration, `written` for quoted text/inscriptions, or `dialogue` for someone speaking about the object. Label the real speaker and attribution; an item is not the speaker. An uncertain quoted claim remains attributed, not an objective property. Omit excerpts that add little. No additional AI-written item description is required.

## Extract records

One record per eligible entity per **complete conversational encounter or other interaction unit**, using:

| Field | Rule |
| --- | --- |
| `entity` | NPC or item entity ID; canonical note path lives on the entity when securely resolved. |
| `scenes` | Ordered numeric shared indexes touched by this interaction. Do not duplicate location/date or add an `other_npcs` list. |
| `interaction` | `interacted`, `observed`, `present`, or `mentioned`. |
| `importance` | `star`, `supporting`, or `cameo`, relative to this encounter. |
| `overview` | One factual sentence, normally at most 30 words, describing this whole interaction. |
| `evidence` | Source-qualified ranges: complete transcript encounter bounds retaining interjections, exact note passages, or both. Multiple ranges may represent source discontinuities or complementary accounts of one encounter; explain in `continuity`. |
| `excerpts` | Optional focused ranges for quick verification; these never substitute for the complete conversation bounds. |
| `continuity` | Brief reason these ranges form one encounter, required for multi-scene or discontinuous records. |
| `quotes` | Optional list of exact quotes, each with a unique ID, source range, kind, actual speaker and attribution. NPC quotes are speech/writing by that NPC; item quotes are explicitly attributed excerpts about the item. |
| `introduction` | Optional verbatim introduction/appearance quote, with its exact source range and kind (`description` or `dialogue`). |
| `known_as` | Optional scene-specific label when the canonical name was not yet available to the party. |

**Whole conversations:** Topic changes, another PC's question, a brief NPC interjection, dice checks, rules talk, jokes and short asides do not split an ongoing conversation. Re-read before and after excerpt matches to find its real opening and ending. Consolidate duplicate fragments before writing overviews. If several NPCs participate, each may have a record referencing the same conversation bounds. Do not merge genuinely separate encounters simply because the NPC is the same. A guided tour with ongoing conversation can span several scenes; a new meeting after a rest is separate.

**Interaction meanings:** `interacted` means a direct exchange or action between party and NPC (conversation, aid, bargaining, attacks, physical handling). There is no separate `fought` type; describe combat in the overview. `observed` means the party sees/hears the NPC doing something without directly engaging them. `present` means the NPC is affirmatively established as around but has no meaningful action or exchange. `mentioned` means the NPC is discussed without their participation being established. Use the strongest evidenced relationship for the unit: interacted, then observed, then present; a mention alone is not presence. An idle person being discussed while visibly present is `present`, not `mentioned`. For a note-documented event with no direct party action and no established PC witness (such as an NPC departure), `observed` may use `perspective: session_record` and an `observation_basis` explaining the limit; phrase the overview as a documented event, not a party-witnessed encounter. State `presence_basis` for present records, with source evidence; do not infer presence from cast lists, normal party membership, canonical whereabouts, or mere mention. Continuity can carry presence through one unbroken encounter when no departure occurs, but not across arbitrary scene changes or overnight gaps.

**Importance:** `star` drives the scene's central interaction or objective; `supporting` makes a substantive contribution; `cameo` is brief/background. Do not derive importance from word count, combat statistics, or future lore.

Use at most one introduction quote per NPC per session by default. Quote exact cleaned-source wording, even when awkward; a contiguous substring of an utterance is acceptable. Across utterances, join their text with one space. Do not stitch noncontiguous fragments into a quotation. Do not invent an introduction when none is recorded. The first introduction in this source is not necessarily the party's first-ever meeting.

**Note quotations:** Narrative notes are evidence, not reconstructed dialogue. Only select NPC speech from a note when it explicitly records attributable direct speech; require `verification: reported_in_notes` and display that it is not transcript-verified. A paraphrase cannot become a pull quote. Item descriptions may quote the note verbatim with the note’s authorship identified, without implying anyone spoke those words. Prefer transcript evidence when the same quotation is recorded there.

**Pull quotes:** Review each speaking NPC for revealing lines: demands, promises, warnings, confessions, unusual beliefs, distinctive turns of phrase or consequential answers. For major NPCs with substantive `star` encounters, actively select several complementary lines when supported, typically two to four across the session. Several can come from the same uninterrupted conversation: never fragment an interaction to accommodate quotes. Prefer lines that reveal different things, not repeated paraphrases. Minor NPCs usually need zero or one. Quotes are normally 5–60 words each; these are targets, not quotas. This is separate from an introduction quote. Verify that the NPC actually says it: a `DM` label can be the NPC's voice or narration, and diarization can be wrong. An attributable written passage may be selected with `kind: written`; never label it spoken dialogue. Record contextual attribution; omit uncertain speech rather than attributing a PC/table joke to the NPC. Retain wording and ASR uncertainty exactly; never rewrite dialogue to make it punchier. Record `quote_review` on each entity as `selected`, `no_suitable_dialogue`, `no_suitable_excerpt` (items), `uncertain_attribution`, or `not_applicable`.

**Session overview:** Each NPC or item entity has exactly one `session_overview`, a factual sentence normally at most 45 words synthesizing its role across this session's records. Ground it with `overview_records` containing the entity's interaction IDs. Include changed relationships or consequential developments; do not concatenate all per-scene summaries. Present-only entities get a brief presence statement, and mentioned-only entities stay explicitly reported rather than encountered or obtained. `featured_quote_ids` selects an ordered list of this entity's quotes for the card, allowing several for major NPCs. The review groups by entity and labels NPC/item, showing the overview and selected quotes first, then complete interactions with shared scene/source links.

## Output and verification

Read [the archived format](format-v4.md). Produce `extraction.json` and a compact, human-readable `review.md` using the helper:

```sh
python .agents/skills/extract-campaign-interactions/scripts/validate.py \
  --vault /path/to/taelgar --input /path/to/extraction.json \
  --preview /path/to/review.md --excerpts /path/to/evidence.md
```

The helper checks hashes, source IDs, coverage, scene joins, enums, excerpts, quotes and canonical note paths. The compact review links to complete interactions and optional focused excerpts; the optional `--excerpts` output expands those passages for verification. Both use local file/line references and do not rewrite the source. Semantic review is still required: confirm all played passages and the complete session note were reviewed, reconcile note-only events and overlapping accounts, entity eligibility, speaker/identity attribution, boundaries, date evidence, and overview support. Read the rendered preview and investigate warnings. Do not present a passing structural check as proof of factual correctness.

Report counts, useful examples, borderline exclusions and unresolved chronology/identity questions. Link the skill and review artifacts. Explain that web deep links require a transcript viewer consuming the stored source-qualified UID or note-line/text selectors; do not invent working site URLs or change the current Taelgarverse recap-based interaction runtime as part of extraction.
