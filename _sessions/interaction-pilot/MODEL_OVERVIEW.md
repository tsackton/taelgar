# Session interaction model — proposal for vault users

This proposal makes it easier to find what happened with an NPC, item or organization in a campaign session, then jump to the relevant source passage. It could support entity histories, session browsing and memorable quote displays without requiring a new AI-written narrative.

The fields below reflect the agreed design and bulk-review workflow. The new format is `schemaVersion: 5`; earlier v3/v4 trial files remain historical examples. Implementation and ten sampled executions will follow this model checkpoint on the review branch.

**How it fits together**

A `session.json` would be the canonical record of the accepted structured session data. It identifies the campaign, session number, real-world date, participating PCs and source documents. Three collections describe the session:

- **Scenes:** contiguous passages, optionally labeled with activity, place and in-world date/time.
- **Entities:** the NPCs, important items and organizations involved, with optional links to their vault pages.
- **Interactions:** an entity's involvement in an encounter, linked to one or more scenes. A continuous conversation can cross scenes while remaining one interaction.

For example, bargaining with Ghesh, walking with him and receiving his introduction to Megren can be one interaction across multiple scenes. An entity's session card collects its interactions and can suggest quotes to feature.

**Sources and navigation**

Each session has at least one source, identified by a session-local `id`, `kind` and vault-relative `path`. An optional `sha256` fingerprint detects changes to that source. The model permits future source kinds, including authored narratives or emails, but **only `transcript` is defined and supported now**. Building an extractor for other sources is outside the current scope.

Scenes, passages and quotes use this source-reference structure:

```json
{
  "kind": "transcript",
  "sourceId": "transcript-1",
  "startUid": "u1715",
  "endUid": "u1817"
}
```

These inclusive utterance IDs identify a contiguous range in the named transcript. Future source-reference kinds can define their own fields; they need not pretend prose documents have transcript utterances.

A scene has exactly one such range. An interaction already links to scenes and may optionally select more precise **passages**. Usually there is one primary passage covering the meaningful exchange, with minor interjections retained. Supporting passages are useful for gaps such as cuts between split parties. They are not a reason to fragment every topic into another interaction.

**Places, dates and participation**

A scene's `location` anchors it to a vault place; `locationDetail` describes a subplace, such as “inside Ovina's smithy.” Either may be omitted when unavailable. `dateStart` and `dateEnd` describe in-world dates, with equal dates for a single day. `time` can preserve wording such as “late afternoon.” Unknown values may remain absent or null. These are separate from the session's required `realWorldDate`. Session-level `dateStart`, `dateEnd` and `locations` also record the aggregate in-world span and vault-linked place list; they are reviewed independently of the scene breakdown.

The session's `pcs` list references participating PC pages. Recurring versus guest status belongs on those pages, not in separate session lists. Entity cards cover NPCs, items and organizations.

**Interaction classifications**

| `interaction` | Meaning |
| --- | --- |
| `interacted` | Direct exchange or action involving the entity; includes conversation, aid, combat, examining or using an item. |
| `observed` | Seen or heard without direct engagement. |
| `present` | Explicitly around without meaningful action or exchange. |
| `mentioned` | Discussed without established participation. |

Optional `importance` is `star`, `supporting` or `cameo`, relative to that encounter. Optional `knownAs` preserves a scene-specific identity such as “the old man at the tower,” even after his canonical identity is resolved. An organization record concerns the group; it does not imply every member was present.

**AI summaries and quotes**

All `aiSummary` fields are optional orientation aids for humans and agents: review, exploration and navigation. They are not evidence or replacements for authored narrative. Fragments and summary-style wording are acceptable.

| Object | Summary guidance |
| --- | --- |
| Scene | At most 25 words. |
| Entity | At most two sentences about its involvement across the session. |
| Interaction | At most one sentence. |
| Passage | At most one sentence about that passage. |

Each interaction may include exact source quotations in one `quotes` array:

- `introduction`: PC or DM wording introducing or describing the entity.
- `color`: memorable words spoken by the entity, including an NPC voiced by the DM.
- `whole`: PC or DM wording capturing the entire meaningful interaction in a sentence or short quotable passage.

Each quote has an ID, type, text and source reference. There is no separate attribution field; quote type specifies the attribution rule, and the source retains the original context. Uncertain attribution should not become an asserted quote. Multiple quotes can belong to one interaction. An entity's optional `aiSuggestedFeaturedQuotes` lists quote IDs in suggested display order; it does not duplicate the text or require an interface to feature them.

<details>
<summary>Field reference: required and optional fields</summary>

**Minimal records and optional enrichment**

| Object | Required fields | Optional fields |
| --- | --- | --- |
| Session | `schemaVersion`, `campaign`, `session`, `realWorldDate`, `pcs`, `sources` | `dateStart`, `dateEnd`, `locations`, `scenes`, `entities`, `interactions`, `review`, `sceneReview` |
| Source | `id`, `kind`, `path` | `sha256` |
| Scene | `index`, `source` | `type`, `location`, `locationDetail`, `dateStart`, `dateEnd`, `time`, `aiSummary` |
| Entity | `id`, `kind`, `label` | `note`, `aiSummary`, `aiSuggestedFeaturedQuotes`, `review` |
| Interaction | `id`, `entity`, `scenes`, `interaction` | `importance`, `knownAs`, `aiSummary`, `passages`, `quotes`, `review` |
| Passage | `source` | `relevance`, `aiSummary` |
| Quote | `id`, `type`, `text`, `source` | — |

`session` is a number within its campaign. `realWorldDate` uses `YYYY-MM-DD`; `pcs` holds vault references. `sources` must be nonempty. `schemaVersion` identifies the format; the new format uses version 5 to avoid collision with historical trial formats.

Scene `type`, when present, is `conversation`, `exploration`, `combat` or `travel`. Entity `kind` is `npc`, `item` or `organization`; `note` optionally resolves the entity to a vault page. Passage `relevance` is `primary` or `supporting`. When omitted, a sole passage is the default starting point; multiple passages retain source order without an implied ranking.

All source, scene, entity and quote references must resolve. Each interaction references one entity and at least one scene. Suggested featured quotes must belong to that entity's interactions. A transcript reference requires all four fields shown above. Optional collections may be omitted or empty; no collection can be omitted while another record depends on it.

</details>

**Confidence, review and bulk processing**

Draft and reviewed data live in the same session object. An optional `review` object contains `confidence` (`high`, `medium`, `low`) and `status` (`unreviewed`, `automatedReviewed`, `humanReviewed`). These are independent: review may confirm that uncertainty remains. Missing review metadata means unreviewed, never approved.

Review applies to four units:

- Session `review`: aggregate dates, PC attendance and vault-linked locations.
- Session `sceneReview`: the division into scenes as a whole, including sequence and coverage. Individual scenes have no review flag.
- Entity `review`: the entire entity record's identification, inclusion and vault match.
- Interaction `review`: the individual interaction.

Critical session metadata and entity records are ready for normal vault use only at high confidence after automated or human review. Scene divisions and interactions may be used while unreviewed, with their status available to interfaces. A consumer must not silently treat draft critical claims as accepted canon. An interaction referencing an unresolved entity retains that entity's review state.

Bulk processing follows extraction, mechanical validation, a separate automated review of critical records, and at most one targeted correction attempt before unresolved critical issues enter a human queue. The rest of the batch continues. Small samples of unflagged output should also be checked for omissions.

Extraction uses cleaned transcripts, session metadata and a reusable vault name/alias index. Existing beats and beat-facts may inform automated review, but are optional and are not generated for this workflow. Any correction needs transcript evidence; beats may flag a discrepancy but do not supply additional events.

**Other review material**

Source coverage exclusions, candidate matches and detailed review evidence need not clutter canonical records. Supporting tools may retain them as execution artifacts; they are not required session fields, and a general review interface remains to be designed. There is no separate segmentation revision; Git history records changes. Stable scene links across reindexing may need future work.

**Feedback to request from other vault users**

1. Would these cards and source links help you find campaign information? What would be difficult to find?
2. Do scenes, entities and interactions feel like useful separate concepts, especially for organizations and items?
3. Are the quote types and short AI orientation aids useful and clearly distinguished from authored narrative?
4. Which mistakes would you most want a review interface to surface before accepting a session?

The [existing trial reviews](README.md#current-reviews) show the motivating examples, using the earlier schema. [Workflow discussion](WORKFLOW_DISCUSSION.md) records provisional next steps separately from this agreed model.
