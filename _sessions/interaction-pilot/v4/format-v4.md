# Interaction extraction v4

`extraction.json` is a derived sidecar, not canonical entity metadata. Version 4 adds source-qualified evidence and documented events beyond the recording. Preserve earlier outputs; the helper can also read historical v3 transcript extractions without rewriting them.

```json
{
  "schema_version": 4,
  "campaign": "mawar",
  "session": "mawar-adventures-002",
  "segmentation_revision": 2,
  "sources": [
    {"id": "transcript", "kind": "transcript", "path": "relative/transcript.md", "sha256": "64 hex characters"},
    {"id": "session-note", "kind": "session_notes", "path": "relative/note.md", "sha256": "64 hex characters"}
  ],
  "supporting_sources": [{"path": "relative/session.yaml", "sha256": "64 hex characters"}],
  "scenes": [{
    "index": 1, "type": "exploration",
    "evidence": [{"source": "session-note", "startLine": 12, "endLine": 12, "text": "Wazir identifies the recovered brass bowl."}],
    "boundary": "Identification the day after recovery.", "location": "Unspecified",
    "date": {"start": "1747-08-06", "end": "1747-08-06", "time": null, "basis": "Explicit date in session notes.", "evidence": ["relative/note.md:12"]}
  }],
  "excluded_ranges": [],
  "entities": [{
    "id": "airion-bowl", "kind": "item", "label": "Brass bowl",
    "canonical_name": null, "note": null, "eligibility": "distinctive",
    "basis": "Recovered magical object explicitly investigated.",
    "session_overview": "Wazir identifies the recovered brass bowl.",
    "overview_records": ["bowl-identification"], "quote_review": "not_applicable",
    "featured_quote_ids": []
  }],
  "interactions": [{
    "id": "bowl-identification", "entity": "airion-bowl", "scenes": [1],
    "interaction": "interacted", "importance": "supporting",
    "overview": "Wazir identifies the recovered brass bowl.",
    "evidence": [{"source": "session-note", "startLine": 12, "endLine": 12, "text": "Wazir identifies the recovered brass bowl."}]
  }],
  "review_notes": ["Illustrative shape only; real selectors must match frozen source files."]
}
```

The example is illustrative, not a complete extraction. All paths are relative to `--vault`. Sources have unique IDs, unique paths, `kind` (`transcript` or `session_notes`), and SHA-256 hashes. Supporting manifests, beats and identity references also retain path/hash. Notes may be the only source. Do not fabricate transcript UIDs for note prose.

## Evidence selectors

Every scene has an `evidence` list; every interaction has an `evidence` list instead of v3's `transcript`. Optional excerpts, quotes, introductions and transcript exclusions also name their source.

- Transcript: `{"source":"transcript","startUid":"u0003","endUid":"u0019"}`. Bounds are inclusive and retain the whole encounter, including minor interjections. All UIDs in each transcript must belong to exactly one scene or excluded range with a reason. Ranges remain ordered within each source; different sources may reuse UID strings.
- Notes: `{"source":"session-note","startLine":12,"endLine":12,"text":"Exact original text."}`. Lines are inclusive, one-based, in the original note. `text` is required and must match exactly once within those lines. It can select a sentence inside a long paragraph; preserve wikilinks and punctuation. The frozen hash detects edits that would invalidate navigation. Separate events may cite the same paragraph, so notes do not have transcript-style partition coverage.

Each interaction's evidence must fall within its referenced scenes' evidence; highlights and quotes must fall within interaction evidence. An introduction can use the joined scene evidence. Multiple ranges or scenes require `continuity`, including when notes and transcript complement the same encounter. Full transcript ranges remain navigable links rather than long passages on cards. Notes are labeled “Documented interaction,” never “Complete transcript.” The evidence review expands selected note text alongside transcript highlights.

## Reconcile events, then segment

Read the entire session note, including timelines, narrative and raw notes. Include documented resolutions, downtime, discoveries and departures after or outside the recording. Merge overlapping accounts into the same interaction; add a separate scene/record for a genuinely different event. A single ongoing conversation stays one interaction even when the note adds its final topics. Do not import later events from canonical entity notes, count repeated recaps as independent evidence, or mistake plans for completed actions. A cast listing alone is not proof of presence; an explicit narrative account can establish participation. Preserve contradictory accounts and source-specific limits in review notes and supported wording.

Scene indexes are sequential integers scoped to `(campaign, session, segmentation_revision)`. Split meaningful location changes, time skips and combat transitions. Keep scenes without eligible entities. Insert note-only scenes using supported chronology; when ordering is uncertain, retain bounded dates and explain it. Changed scene boundaries or insertion/reindexing require a new segmentation revision and rebuilt joins. Adding corroborating evidence to an unchanged event does not itself require a new scene.

Locations, dates and types belong to scenes, not records. Both date bounds null means unknown; different dates mean a bounded interval. Explain inherited dates and inferences in `basis` and `evidence`. Do not infer an exact day from a broad session range, recording timestamps, or an endpoint alone. A memory is dated when witnessed, with historical time described separately. If a documented postgame event has no stated setting, say so instead of carrying forward the last recorded room.

Exactly one `type`: `conversation`, `exploration`, `combat`, or `travel`. Choose the dominant activity. Exploration includes investigation, divination and rest/downtime; conversation includes negotiation and settlements; travel includes departures. A moving fight is combat; incidental banter does not split travel. Preserve whole encounters across genuine scene changes. These four labels do not authorize inventing activity, dialogue or travel arrivals.

## Entity cards and interaction kinds

Each entity has `id`, `kind` (`npc` or `item`), `label`, `canonical_name`, `note`, `eligibility`, `basis`, one `session_overview`, `overview_records`, `quote_review`, and `featured_quote_ids`. IDs share a unique namespace. Source-safe labels and optional interaction `known_as` distinguish canonical identity from knowledge available in the scene.

NPC eligibility is `named` or `individual`; include distinctive unnamed people, not generic combatants, crowds or hypothetical creatures. Exclude this campaign's PCs. Item eligibility is `named` or `distinctive`; include consequential objects, clues, tools, gifts, payments and transfers, not routine inventory. An artificial character remains an NPC. Keep books distinct from authors, containers from contents, and distinguish copies or parts when supported. Collections can share a card when the source treats them as one subject.

One factual sentence per interaction (normally at most 30 words, validator ceiling 35) and per entity/session (normally at most 45, ceiling 55). `overview_records` references all and only that entity's records, including note-only events. Do not generate extra descriptive prose. Preserve the distinction between discussing an object and acquiring it.

Interaction kinds remain `interacted`, `observed`, `present`, `mentioned`; importance remains `star`, `supporting`, `cameo` relative to the encounter. `interacted` covers direct exchanges/actions with NPCs and examination, use, handling, acquisition, transfer or destruction of items. `observed` covers seeing/hearing without directly engaging. `present` requires affirmative `presence_basis`, not assumptions about companions or inventory. `mentioned` covers discussion without established participation. Use the strongest supported relationship within the whole unit.

For a documented event without party action or an established PC witness, an `observed` record can explicitly set `perspective: "session_record"` and `observation_basis`. Such records require note-only evidence and display “Documented event; party witnessing is not established.” For example, notes may confirm Azar leaves with Benat without recording a farewell or who watched him leave. Do not manufacture an eyewitness encounter. This is a provenance qualifier, not a fifth interaction kind.

Do not duplicate an encounter across sources or split it for every topic, interruption or quote. The validator rejects overlapping transcript encounters for the same entity and exact duplicate note records; semantic deduplication of differently worded note passages still requires review.

## Quotes

Optional `quotes` contain session-unique `id`, `kind`, `quote`, `speaker`, `attribution`, and a source-qualified evidence selector. Quote text must be a contiguous substring of the selected passage (transcript utterance texts joined with single spaces). Preserve ASR wording; never stitch or improve dialogue.

For NPCs, `kind` is `dialogue` or `written`, and `speaker` must be that NPC's ID. DM narration, jokes and hypothetical speech are not NPC quotes. For items, `kind` may also be `description`; dialogue identifies its actual speaker, never the item. Use null for unattributed narration/inscription and explain the origin. The same written passage may appear on author and book cards with different quote IDs.

A note paraphrase is not direct speech. Only use note-sourced dialogue when the note explicitly quotes attributable speech; require `verification: "reported_in_notes"` and show that it is not transcript-verified. This also applies to dialogue introductions. Note descriptions must be labeled as note text, not spoken narration. Prefer the actual recording for a quote that appears in both sources. Structural validation checks exact text and required labels; attribution and whether it is direct speech require human/agent source review.

`featured_quote_ids` orders quotes beneath the session overview. Major NPCs with substantive star encounters should have several complementary lines when supported, typically two to four; several can come from one interaction. Minor NPCs usually have zero or one. These are targets, not quotas. Additional quotes appear with their interaction.

`quote_review`: `selected`, `no_suitable_dialogue`, `no_suitable_excerpt` (items), `uncertain_attribution`, or `not_applicable`. Entities with quotes require a nonempty featured list; those without quotes use an empty list. Optional `introduction` is a separate verbatim appearance/introduction passage at most once per entity, with `kind` (`description` or `dialogue`), `quote`, and its source selector.

## Navigation and migration

Local file/line links are review aids, not working website URLs. A viewer should resolve source IDs to their path/hash and use transcript UIDs or note line/text selectors. Scene co-membership alone does not prove co-presence: check relationship, event perspective and evidence. Mentioned and remotely observed entities need not be physically present.

To migrate v3 transcript extractions, preserve the old artifacts, set version 4, move root `source` into `sources` with an ID, replace each scene's bare bounds with `evidence`, rename interaction `transcript` to `evidence`, and qualify all ranges with the source ID. Register the original session note, review it in full, reconcile overlapping accounts and add genuinely new events. Preserve accepted transcript bounds and quotes unless a reviewed correction is required. Legacy UID-marked notes must be regenerated against their original note lines, not silently relabeled.
