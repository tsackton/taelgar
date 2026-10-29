# Session interaction model — proposal for vault users

This proposal makes it easier to find what happened with an NPC, item or organization in a campaign session, then jump to the relevant source passage. It could support entity histories, session browsing and memorable quote displays without requiring a new AI-written narrative.

The fields below reflect the agreed design and bulk-review workflow. The current enrichment format is `schemaVersion: 6`; the ten-session v5 trial and earlier files remain historical examples. The new model integrates with existing session bundles.

**How it fits together**

The existing `session.yaml` owns campaign/session identity, real-world date, session dates, participant/PC information and source documents. A companion `session.json` is canonical for extracted interaction data and references that YAML instead of copying those values. Completion adds relative pointers from the YAML to this JSON and `session-processing-data.json`. Three collections describe the session:

- **Scenes:** contiguous passages, optionally labeled with activity, place and in-world date/time.
- **Entities:** the NPCs, important items and organizations involved, with optional links to their vault pages.
- **Interactions:** an entity's involvement in an encounter, linked to one or more scenes. A continuous conversation can cross scenes while remaining one interaction.

For example, bargaining with Ghesh, walking with him and receiving his introduction to Megren can be one interaction across multiple scenes. An entity's session card collects its interactions and can suggest quotes to feature.

**Sources and navigation**

Sources are registered in the YAML. Extraction prefers its polished Markdown artifact, whose comments preserve the original cleaned transcript UIDs and character offsets; the registered cleaned source remains the mapping reference. Source/YAML fingerprints live in processing data. Missing or incorrect source paths produce proposed YAML fixes, not an independent JSON source registry. The model permits future source kinds, including authored narratives or emails, but **only `transcript` is defined and supported now**. Building an extractor for other sources is outside the current scope.

Scenes, passages and quotes use this source-reference structure:

```json
{
  "kind": "transcript",
  "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
  "startUid": "u1715",
  "endUid": "u1817"
}
```

These inclusive utterance IDs identify a contiguous range in the YAML-registered transcript. A polished turn can combine or split utterances; source links use its retained comments to locate the original IDs. Quotes must include the complete provenance of their polished turns. Partial-UID ranges are not implemented. Future source-reference kinds can define their own fields; they need not pretend prose documents have transcript utterances.

A scene has exactly one such range. An interaction already links to scenes and may optionally select more precise **passages**. Usually there is one primary passage covering the meaningful exchange, with minor interjections retained. Supporting passages are useful for gaps such as cuts between split parties. They are not a reason to fragment every topic into another interaction.

**Places, dates and participation**

A scene's `location` anchors it to a vault place; `locationDetail` describes a subplace, such as “inside Ovina's smithy.” Either may be omitted when unavailable. `dateStart` and `dateEnd` describe in-world dates, with equal dates for a single day. `time` can preserve wording such as “late afternoon.” Unknown values may remain absent or null. These are separate from YAML `realWorldDate`. YAML `drStart`/`drEnd` own the aggregate span; JSON `locations` retains the independently reviewed vault-linked place list. YAML can clarify unstated dates or extend beyond the recording. Only clear conflicting transcript evidence creates a critical date finding; it does not automatically rewrite YAML.

PC information belongs to the YAML; its participant speaker mappings must not automatically be treated as actual PC attendance. Missing/conflicting information is proposed for YAML review. Recurring versus guest status belongs on those pages, not in separate session lists. Entity cards cover NPCs, items and organizations.

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
| Session enrichment | `schemaVersion` (6), `sessionYaml` | `locations`, `scenes`, `entities`, `interactions`, `review`, `sceneReview` |
| Scene | `index`, `source` | `type`, `location`, `locationDetail`, `dateStart`, `dateEnd`, `time`, `aiSummary` |
| Entity | `id`, `kind`, `label` | `note`, `aiSummary`, `aiSuggestedFeaturedQuotes`, `review` |
| Interaction | `id`, `entity`, `scenes`, `interaction` | `importance`, `knownAs`, `aiSummary`, `passages`, `quotes`, `review` |
| Passage | `source` | `relevance`, `aiSummary` |
| Quote | `id`, `type`, `text`, `source` | — |

`sessionYaml` is a vault-relative reference to the manifest. Session numbering, dates, PC metadata and source identification are inherited from that manifest. No second copy is authored in enrichment JSON.

Scene `type`, when present, is `conversation`, `exploration`, `combat` or `travel`. Entity `kind` is `npc`, `item` or `organization`; `note` optionally resolves the entity to a vault page. Passage `relevance` is `primary` or `supporting`. When omitted, a sole passage is the default starting point; multiple passages retain source order without an implied ranking.

All source, scene, entity and quote references must resolve. Each interaction references one entity and at least one scene. Suggested featured quotes must belong to that entity's interactions. A transcript reference requires all four fields shown above. Optional collections may be omitted or empty; no collection can be omitted while another record depends on it.

</details>

**Confidence, review and bulk processing**

Draft and reviewed data live in the same session object. An optional `review` object contains `confidence` (`high`, `medium`, `low`) and `status` (`unreviewed`, `automatedReviewed`, `humanReviewed`). These are independent: review may confirm that uncertainty remains. Missing review metadata means unreviewed, never approved.

Review applies to four units:

- Session `review`: consistency with YAML dates/PC information, plus extracted vault-linked locations.
- Session `sceneReview`: the division into scenes as a whole, including sequence, coverage and reasoned exclusions. Individual scenes have no review flag.
- Entity `review`: the entire entity record's identification, inclusion and vault match.
- Interaction `review`: the individual interaction.

Critical session metadata and entity records are ready for normal vault use only at high confidence after automated or human review. Scene divisions and interactions may be used while unreviewed, with their status available to interfaces. A consumer must not silently treat draft critical claims as accepted canon. An interaction referencing an unresolved entity retains that entity's review state.

Bulk processing follows extraction, mechanical validation, a separate automated review of critical records, and at most one targeted correction attempt before unresolved critical issues enter a human queue. The rest of the batch continues. Small samples of unflagged output should also be checked for omissions.

Extraction uses cleaned transcripts, session metadata and a reusable vault name/alias index. Existing beats and beat-facts may inform automated review, but are optional and are not generated for this workflow. Any correction needs transcript evidence; beats may flag a discrepancy but do not supply additional events.

**Other review material**

A formal `session-processing-data.json` holds input fingerprints, full-read attestation, excluded transcript ranges with reasons, metadata findings/proposed YAML fixes, and replayable review history. Review requests and readable reviews expose the excluded blocks. Every UID must belong to a scene or a reasoned exclusion before completion. Critical uncertainty can remain visible after processing completes; completion is not automatic canon acceptance. There is no separate segmentation revision; Git history records changes. Stable scene links across reindexing may need future work.

**Feedback to request from other vault users**

1. Would these cards and source links help you find campaign information? What would be difficult to find?
2. Do scenes, entities and interactions feel like useful separate concepts, especially for organizations and items?
3. Are the quote types and short AI orientation aids useful and clearly distinguished from authored narrative?
4. Which mistakes would you most want a review interface to surface before accepting a session?

The [existing trial reviews](README.md#current-reviews) show the motivating examples, using the earlier schema. [Workflow discussion](WORKFLOW_DISCUSSION.md) records provisional next steps separately from this agreed model.
