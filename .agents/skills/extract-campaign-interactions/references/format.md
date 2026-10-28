# Interaction extraction v3 — transcript-only baseline

`extraction.json` is a derived sidecar, not canonical NPC or item metadata. The active format is v3: typed entity cards, typed scenes, multiple quotes and one frozen transcript. The v4 mixed-source experiment is superseded; do not generate note-backed events or use its evidence registry, note selectors or session-record perspective.

```json
{
  "schema_version": 3,
  "campaign": "dufr",
  "session": "dunmari-frontier-108",
  "segmentation_revision": 1,
  "source": {"kind": "transcript", "path": "relative/source.md", "sha256": "64 hex characters"},
  "supporting_sources": [{"path": "relative/session.yaml", "sha256": "64 hex characters"}],
  "scenes": [{
    "index": 1, "type": "conversation", "startUid": "u0001", "endUid": "u0020",
    "boundary": "Opening conversation; departure follows.", "location": "Gate",
    "date": {"start": null, "end": null, "time": null, "basis": "No supported date.", "evidence": ["source.md"]}
  }],
  "excluded_ranges": [],
  "entities": [{
    "id": "session108-sealed-box", "kind": "item", "label": "Sealed box",
    "canonical_name": null, "note": null, "eligibility": "distinctive",
    "basis": "Specific box entrusted to the party during this negotiation.",
    "session_overview": "The party accepts a sealed box for delivery.",
    "overview_records": ["box-delivery"], "quote_review": "selected",
    "featured_quote_ids": ["box-warning"]
  }],
  "interactions": [{
    "id": "box-delivery", "entity": "session108-sealed-box", "scenes": [1],
    "interaction": "interacted", "importance": "supporting",
    "overview": "The guide hands over the sealed box and warns the party to keep it closed.",
    "transcript": [{"startUid": "u0003", "endUid": "u0019"}],
    "excerpts": [{"startUid": "u0011", "endUid": "u0013"}],
    "quotes": [{"id": "box-warning", "kind": "dialogue", "quote": "Illustrative verbatim warning.", "startUid": "u0012", "endUid": "u0012", "speaker": "Unnamed guide", "attribution": "The guide warns the party about the box; this is a reported claim."}]
  }],
  "review_notes": ["Concise exclusions, chronology conflicts or identity limits."]
}
```

The example is illustrative, not valid against a real transcript. All paths are relative to `--vault`. Freeze the transcript and supporting references by SHA-256. `source.kind` must be `transcript`; there is no notes-only fallback or fabricated UID copy of prose notes.

## Source scope

The transcript exclusively supplies events, participation, presence, outcomes, dialogue and quotations. Supporting manifests and reference notes may resolve dates, identities, spelling and location names for transcript passages. They cannot add missing actions or turn a mentioned NPC into a participant. Beats are navigation aids; verify every extracted claim against its transcript context. Session overviews synthesize only transcript-supported records.

Exclude events documented only in session notes, including postgame resolutions, later item identification, departures and confirmed rests beyond the recording. Do not fill a recording gap with recap prose or turn a planned action into a completed event. Report relevant uncertainty or conflicting accounts briefly without importing alternative events. Lack of a transcript means missing input, not permission for notes-only extraction.

## Scenes and dates

Scene indexes are sequential integers scoped to `(campaign, session, segmentation_revision)`. All transcript UIDs must belong to exactly one scene or excluded range with a reason. Bounds are inclusive and follow source order. Split meaningful location changes, explicit time skips and combat transitions; retain scenes with no eligible entities. Preserve whole conversations across genuine scene changes using an interaction's `scenes` list. Changed boundaries require a revised segmentation and rebuilt joins; adding type labels alone does not.

Locations, dates, boundaries and scene types belong to scenes, not records. Both date bounds null means unknown; different dates mean a bounded interval. Explain inherited dates and inferences in `basis` and `evidence`; do not manufacture hours or equate recording time with game time. A session endpoint alone does not establish another encounter. A memory is dated when witnessed, with its historical time described separately.

Exactly one `type`: `conversation`, `exploration`, `combat`, or `travel`. Choose the dominant activity: dialogue, negotiation and planning are conversation; investigation, observation, puzzles, divination and recorded rest are exploration; hostile engagement is combat; movement between locations is travel. A moving fight is combat; incidental banter need not split travel. These labels do not authorize invented activity.

## Entity cards

Each entity has `id`, `kind` (`npc` or `item`), `label`, `canonical_name`, `note`, `eligibility`, `basis`, `session_overview`, `overview_records`, `quote_review`, and `featured_quote_ids`. IDs share one unique namespace. Source-safe labels and optional interaction `known_as` distinguish canonical identity from what the party knows in the scene.

NPC eligibility is `named` or `individual`; include distinctive unnamed people, not generic combatants, crowds or hypothetical creatures. Exclude this campaign's PCs. Item eligibility is `named` or `distinctive`; include consequential objects, clues, tools, gifts, payments and transfers, not routine inventory. An artificial character remains an NPC. Keep books distinct from authors, containers from contents, and distinguish copies or parts when supported. Collections can share a card when the transcript treats them as one subject.

Exactly one factual sentence per interaction (normally at most 30 words, validator ceiling 35) and per entity/session (normally at most 45, ceiling 55). `overview_records` references all and only that entity's interactions. Do not generate an extra description or import later lore. Preserve the distinction between discussing an object and acquiring it.

## Interactions and evidence

`interactions.entity` references the entity ID. `scenes` is an ordered list of shared integer indexes. Kinds are `interacted`, `observed`, `present`, `mentioned`; importance is `star`, `supporting`, `cameo` relative to the encounter.

`interacted` covers direct exchanges/actions with NPCs and examination, use, handling, acquisition, transfer or destruction of items. `observed` covers seeing/hearing without directly engaging. `present` requires affirmative transcript evidence in `presence_basis`, not assumptions about companions or inventory. `mentioned` covers discussion without established participation. Use the strongest supported relationship within the whole unit. There is no separate fought type and no session-record observation qualifier.

`transcript` contains complete inclusive encounter ranges, retaining minor interjections and topic changes. One range is usual; multiple ranges may represent genuine source discontinuities, such as a cut to another simultaneous party. Explain multi-scene or multi-range continuity in `continuity`. `excerpts` are optional short highlights inside full ranges. Source bounds are links, not full transcripts displayed on cards. Do not split conversations to hold extra quotes or merge genuinely separate visits. The validator rejects overlapping duplicate interactions for the same entity; semantic fragmentation still needs review.

Interaction ranges must lie within their joined scenes. Highlights and quotes must lie within interaction ranges; an introduction can use the joined scene ranges. Scene co-membership does not itself prove physical co-presence: mentioned and remotely observed entities need not be there.

## Multiple quotes

Each optional `quotes` list contains objects with session-unique `id`, `kind`, `quote`, `startUid`, `endUid`, `speaker`, and `attribution`. Quote text must be a contiguous substring of transcript utterance texts joined with single spaces. Preserve ASR wording; never stitch separated fragments or rewrite dialogue.

For NPCs, `kind` is `dialogue` or `written`, and `speaker` must equal that NPC's entity ID. DM narration, PC jokes and hypothetical speech are not NPC quotes. Written passages must actually occur in the transcript; this kind does not permit importing text from a note. For items, `kind` may also be `description`; dialogue names its actual speaker, never the item. Use null for unattributed narration/inscription and explain its origin. An attributed written passage can appear on author and book cards with distinct quote IDs and the same transcript range.

`featured_quote_ids` orders quotes beneath the session overview. Major NPCs with substantive star encounters should have several complementary lines when supported, typically two to four; several can come from one interaction. Minor NPCs usually have zero or one. These are targets, not quotas. Additional selected quotes appear with their interaction.

`quote_review`: `selected`, `no_suitable_dialogue`, `no_suitable_excerpt` (items), `uncertain_attribution`, or `not_applicable`. Entities with quotes require a nonempty featured list; those without quotes use an empty list. Optional `introduction` is a separate verbatim appearance/introduction excerpt, at most once per entity, with `kind` (`description` or `dialogue`), `quote`, `startUid`, and `endUid`.

## Navigation and validation

Local file/line links are review aids, not working website URLs. A viewer should resolve `(campaign, session, segmentation_revision, scene)` and `(source.sha256, startUid, endUid)`. Changed source text or boundaries require reviewed regeneration.

The helper checks source hashes, transcript coverage, entity/scene joins, enums, range containment, exact quote text, attribution fields and overview references. Semantic review still checks complete conversations, eligibility, speaker identity, factual support and date uncertainty. Structural success is not proof of factual correctness.

The existing v3 trials are the current baseline. Preserve historical v4 mixed-source outputs separately; the active validator rejects them rather than silently dropping note-derived events.
