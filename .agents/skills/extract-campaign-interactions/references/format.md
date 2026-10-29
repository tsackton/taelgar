# Session enrichment format v6

[session.schema.json](session.schema.json) defines the extracted data. [session-processing-data.schema.json](session-processing-data.schema.json) defines the required execution companion; [processing.md](processing.md) explains it. Historical v5 files use [session-v5.schema.json](session-v5.schema.json) and are not silently migrated.

`session.yaml` owns campaign/session identity, real-world date, accepted in-world date span, participant/PC metadata, and source artifacts. `session.json` is its companion enrichment, not another session manifest. It contains no copied campaign, session number, real-world date, PC list, source registry or aggregate date endpoints. The independently reviewed aggregate `locations` remains an extraction result, alongside scenes/entities/interactions.

| Object | Required | Optional |
| --- | --- | --- |
| Session enrichment | schemaVersion (6), sessionYaml | locations, scenes, entities, interactions, review, sceneReview |
| Scene | index, source | type, location, locationDetail, dateStart, dateEnd, time, aiSummary |
| Entity | id, kind (npc/item/organization), label | note, aiSummary, aiSuggestedFeaturedQuotes, review |
| Interaction | id, entity, scenes (nonempty), interaction | importance, knownAs, aiSummary, passages, quotes, review |
| Passage | source | relevance, aiSummary |
| Quote | id, type, text, source | — |
| Review (when present) | confidence, status | — |

`sessionYaml` is vault-relative. Entity `note`, scene `location` and aggregate `locations` reference existing vault pages. Optional note/location/date/time fields may be omitted or null; optional collections can be empty. Session numbers, including fractional sessions, are read from the YAML without imposing a second numbering rule.

## Source ownership and ranges

A source reference remains a discriminated union, currently supporting transcripts:

```json
{"kind":"transcript","sourceId":"transcriptProcessing.artifacts.polishedMarkdown","startUid":"u0001","endUid":"u0020"}
```

`sourceId` identifies the existing dotted YAML artifact key, not a registry inside the JSON. Prefer `transcriptProcessing.artifacts.polishedMarkdown`, using `transcriptProcessing.artifacts.cleaned` to interpret its retained source mapping. Those artifact paths are bundle-relative, as defined by transcript processing. If no polished artifact is registered, use the registered cleaned artifact. For older bundles, an explicit `cleanedSourcePath` relative to the YAML directory is supported; it must be added to YAML before use. Never silently substitute a guessed sibling file. Report missing, machine-specific or incorrect paths as proposed YAML fixes. Ancillary stale paths do not block a valid retained transcript, but their proposals remain visible.

Polished Markdown embeds `%% u0001:0-25, u0002:0-40 %%` comments. These contain original utterance IDs and original-text character offsets, not new paragraph IDs. Inclusive `startUid`/`endUid` ranges remain valid. A UID can appear in multiple polished turns and a turn can combine UIDs; the reader validates complete ordered offset coverage and maps ranges to the corresponding Markdown lines. Quotes must exactly match the selected representation and their ranges must contain the complete provenance of the quoted polished turns. Choose boundaries around whole turns/UIDs. Partial-UID ranges are not implemented; retain minor chatter inside a scene when it shares a UID with play.

Saved YAML speaker corrections apply when reading cleaned text and must agree with polished attribution. Polished and cleaned source hashes are checked. Preparation/review fingerprints also bind the YAML metadata, so changes cannot silently inherit previous review confidence.

Scenes have one contiguous range; passages and quotes must lie within their interaction's joined scenes. Other source kinds may later define different locators and YAML descriptors; extracting authored narratives/emails is not implemented.

## Content and review

Scene type: conversation/exploration/combat/travel. Interaction: interacted/observed/present/mentioned. Importance: star/supporting/cameo. Passage relevance: primary/supporting. Keep whole conversations despite topic changes and short interruptions.

Optional AI summaries are orientation aids: scene at most 25 words, entity at most two sentences, interaction/passage at most one sentence. They are not evidence or narrative replacements. Quotes use introduction/color/whole; introduction and whole are PC/DM wording, color is the entity speaking. Featured suggestions reference this entity's quotes without duplicating text.

Review confidence is high/medium/low; status is unreviewed/automatedReviewed/humanReviewed. Root `review` covers consistency with the authoritative YAML and the extracted aggregate location list. Root `sceneReview` covers the complete division and excluded coverage. Entities and interactions retain individual review; scenes do not. Critical records require high confidence after semantic review, with current processing fingerprints, for normal use.

The YAML may describe dates before/after the recording or clarify dates never spoken aloud. That is legitimate additional context, not an error or a reason to truncate its dates to scene endpoints. Clear conflicting transcript evidence creates a critical `dateConflict` finding with source and YAML-field evidence in processing data. Propose a correction; do not change the YAML dates. Participant speaker mappings are not automatically proof of actual PC attendance. Report conflicting/missing participation facts there too rather than creating a rival PC list.

Completion saves `session.json`, `session-processing-data.json` and the entity-first `review.md`, then appends relative pointers to the YAML:

```yaml
interactionExtraction:
  sessionJson: ../interactions/session.json
  processingData: ../interactions/session-processing-data.json
```

Paths here are relative to the YAML directory. Other YAML fields and formatting are preserved. Completion records that processing/review finished; low-confidence critical claims remain visibly provisional. Beats, beat facts, recaps and subsequent artifacts are noncanonical optional review hints, never extraction inputs or completion prerequisites.
