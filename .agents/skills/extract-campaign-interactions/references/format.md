# Canonical session format v5

The authoritative shape is [session.schema.json](session.schema.json). The [shareable overview](../../../../_sessions/interaction-pilot/MODEL_OVERVIEW.md) explains its purpose. The new version number avoids collision with historical v3 and v4 pilot formats.

| Object | Required | Optional |
| --- | --- | --- |
| Session | schemaVersion (5), campaign, session (number), realWorldDate, pcs, sources (nonempty) | dateStart, dateEnd, locations, scenes, entities, interactions, review, sceneReview |
| Source | id, kind (transcript), path | sha256 |
| Scene | index, source | type, location, locationDetail, dateStart, dateEnd, time, aiSummary |
| Entity | id, kind (npc/item/organization), label | note, aiSummary, aiSuggestedFeaturedQuotes, review |
| Interaction | id, entity, scenes (nonempty), interaction | importance, knownAs, aiSummary, passages, quotes, review |
| Passage | source | relevance, aiSummary |
| Quote | id, type, text, source | — |
| Review (when present) | confidence, status | — |

A source reference is a discriminated union, currently with one supported case:

```json
{"kind":"transcript","sourceId":"transcript-1","startUid":"u0001","endUid":"u0020"}
```

Bounds are inclusive. All IDs resolve within the session. Scenes have one contiguous range; passages and quotes must lie inside their interaction's joined scenes. Sequential source ranges may share the same UID strings across different sources. A future union kind can define a different locator without pretending authored prose is a transcript. Non-transcript extraction is not implemented.

Paths are vault-relative. `pcs`, `locations`, entity `note` and scene `location` refer to existing vault pages when supplied. Optional locations, note links and date/time fields may be absent or null. Other optional fields may be omitted; optional collections may be empty. Absence does not mean reviewed or proven absent.

Scene type: conversation/exploration/combat/travel. Interaction: interacted/observed/present/mentioned. Importance: star/supporting/cameo. Passage relevance: primary/supporting; without relevance a sole passage is the default and multiple passages retain source order. Keep whole conversational units despite topic changes and short interruptions.

All AI summaries are optional, non-evidentiary orientation aids: scene at most 25 words, entity at most two sentences, interaction/passage at most one sentence. The validator enforces the scene word ceiling; sentence boundaries and semantic support require review, avoiding unreliable punctuation-based rejection of proper names and fragments.

Quotes use introduction/color/whole, with exact text and source bounds. Introduction and whole are PC/DM wording; color is spoken by the entity. There is no attribution field. Attribution still needs contextual review. Featured suggestions reference only this entity's quotes, in display order.

Review confidence: high/medium/low. Review status: unreviewed/automatedReviewed/humanReviewed. Session `review` covers critical aggregate metadata; `sceneReview` covers the complete scene division. Individual entities and interactions use their own `review`; scenes do not. Critical records are usable only with high confidence after automated/human review. Mechanical validation never changes review state.

Aggregate dates and locations are reviewed independently from individual scene assignments. Coverage exclusions, review rationale and candidate matches are execution evidence outside the canonical field set. The producer checks coverage, but minimal model instances need not contain scenes or partition a source. Git tracks revisions; there is no segmentation_revision field.
