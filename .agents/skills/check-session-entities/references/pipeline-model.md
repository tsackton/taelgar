# Session interaction pipeline and v7 model

This contract describes the implemented stages and the candidate final model.
Interaction generation, guarded review application, Obsidian integration, and
publication are not implemented. Helpers validate structure and protect writes;
they do not decide identities or establish semantic review.

## Implemented stages and ownership

```text
session YAML + registered polished transcript
    ├─ optional interaction draft: conservative reading view
    ├─ scene map: place/time partition + optional AI concerns
    └─ entity map: identity, selection, and vault-link decisions
current scene map + entity map
    → read-only v7 candidate projection
    → interaction generation, review, publication [not implemented]
```

Scene and entity mapping can run in either order. Scene mapping can read a
validated reduction draft; entity mapping reads polished speech directly.
Neither requires beats or generated recaps. YAML owns campaign/session metadata,
dates, PC roles, and transcript registration; do not create another manifest,
source registry, or participant list.

Each format has one maintained definition:

| Artifact | Contract | Ownership |
| --- | --- | --- |
| `cleaned/<stem>-interactions-draft.md` | [Draft format](../../prepare-interaction-transcript/references/format.md) | Optional reversible view; source text remains authoritative. |
| `cleaned/<stem>-scene-map.json` | [Scene map v2](../../map-transcript-scenes/references/format.md) | Complete source partition, locations/times, shared map review, optional AI issues. |
| `cleaned/<stem>-entity-map.json` | [Entity map v3](format.md) | Identity decisions, representative UID evidence, confidence/review, meaningful exclusions. |
| Candidate `session.json` | [v7 schema](session.schema.json), detailed below | Projection to stdout; no final generation, registration, or publication. |

Entity decisions bind to YAML/source and consulted-note fingerprints, not scene
maps. Scene/context indexes are revision-dependent: downstream consumers using
them must bind to the originating scene-map hash. Changed inputs require evidence
rechecking, not replacement of stored hashes. Hashes detect changes in inspected
files; they prove neither search completeness nor semantic correctness.

Use the [entity review workflow](review-workflow.md) for saved reviews and manual
feedback application. Helpers accept caller-authored review statuses and do not
enforce human-decision preservation, review history, or selective reset. Agents
must preserve stable IDs and accepted decisions and recheck changed records.
An automated or human review must be an actual review, not a validation result.

## Source references

The only implemented source kind is a YAML-registered polished transcript:

```json
{
  "kind": "transcript",
  "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
  "startUid": "u0013",
  "endUid": "u0137"
}
```

`sourceId` is the dotted YAML artifact key. Artifact paths are bundle-relative.
Ranges are inclusive and contiguous in transcript order and respect both whole
polished turns and whole UIDs. A turn combining UIDs cannot be split; turns
sharing one UID remain together. Original character offsets do not authorize
invented sub-turn locators. Recording timestamps are not in-world times.
Other source kinds would need explicit locators and readers before use.

Scene membership does not classify every passage as played action: one site/time
span can contain chatter, recaps, or hypotheticals. Context blocks and reduction
snips are not blanket extraction exclusions. Inspect individual passages before
inferring visits, presence, events, or dialogue.

## Final session.json v7

[session.schema.json](session.schema.json) is the normative structural definition.
[session_model.py](../scripts/session_model.py) adds source-aware checks against
the registered transcript. Version **7** is independent of scene-map v2,
entity-map v3, and draft v4. There is no automatic version migration.

| Root field | Required? | Purpose |
| --- | --- | --- |
| `schemaVersion` | Yes | Exactly `7`. |
| `sessionYaml` | Yes | Vault-relative canonical manifest reference. |
| `locations` | No | Deduplicated visited vault place paths, independently reviewed. |
| `scenes` | No | Scene records using the scene-map scene fields/indexes. |
| `contextBlocks` | No | Indexed contextual passages retaining recap/lore/chatter framing. |
| `entities` | No | Entity records defined below. |
| `interactions` | No | Entity/party interactions with scene/context anchors. |
| `review` | No | Aggregate consistency with YAML metadata and reviewed visited locations. |
| `sceneReview` | No | Overall scene division and source accounting review. |

Do not copy campaign names, session numbers/dates, PCs, source registries, or an
aggregate date span from YAML. Unknown properties are rejected. Optional arrays
may be absent/empty; optional note/place/date/time values may be absent/null,
not empty strings. Minimal validity does not mean readiness: a document containing
only `schemaVersion: 7` and a valid `sessionYaml` passes partial validation.

### Scene and contextual anchors

Scenes retain the scene-map scene fields, including independent optional
`timeStart` and `timeEnd` text endpoints beside `dateStart` and `dateEnd`.
Relative/approximate wording is allowed; unknown endpoints stay absent/null.
The single `time` field is retired. Map-level `review` projects to final
`sceneReview`; optional AI `issues` and fingerprints stay in the scene map.
Issues serve only to surface concerns to a reviewer; their presence does not
change validation results, confidence, or review status.
Final context blocks require
`index`, `kind`, and `source`, with optional `aiSummary` of at most 25 words.
Kinds are `recap | loreDiscussion | tableChatter`. Scene and context indexes are
positive, ordered, and unique in **separate namespaces**. Projection assigns
context indexes in source order.

Ranges cannot overlap within or across those collections. Complete accounting
means every UID belongs to one scene or context block; it does not require an
interaction for every block. Partial candidates can leave UIDs unaccounted.

### Entities and review

Required entity fields: `id`, `kind`, `label`. Kinds are
`npc | divine | item | organization`. Optional fields:

- `note`: verified vault-relative `.md` path or null.
- `aiSummary`: one entity/session overview, at most two sentences.
- `aiSuggestedFeaturedQuotes`: IDs of that entity's existing quotes.
- `review`: whole-record confidence and status.

Intermediate `occurrences`, `names`, `candidates`, and `identifiedLater`
remain map/review evidence. They are not extra final entity fields. Later stage
interaction authoring must preserve session knowledge, using `knownAs` where
helpful; projection alone does not generate those interactions.

Review objects contain `confidence: high | medium | low` and
`status: unreviewed | automatedReviewed | humanReviewed`. Confidence covers the
whole decision rather than separate field scores. Automated review is a distinct
semantic pass; human review requires an actual decision on that record. Projection
can carry entity review values and scene-map review without establishing overall
final-output review. Legacy scene maps lacking review do not acquire `sceneReview`
through projection.

### Interactions

Required: `id`, `entity` (an existing entity ID), `interaction`, and at least one
nonempty anchor array: `scenes` or `contexts`. Anchor arrays contain existing,
ordered, unique indexes. Interaction types:

| Value | Meaning |
| --- | --- |
| `interacted` | Meaningful direct exchange/action. |
| `observed` | The party observes the entity without a direct exchange. |
| `present` | The entity is known to be around but does not otherwise act. |
| `mentioned` | Discussion without establishing current participation. |

Any nonempty `contexts` array requires `mentioned`, even with scene anchors.
Separate a played exchange from related postgame commentary; context-only
mentions need no invented scene. In-scene recollections and hypotheticals also
use `mentioned`. Scene anchors alone do not prove presence.

The same vocabulary applies to divine entities. Prayer, invocation, belief, and
attributed intervention alone are mentions. An explicitly played manifestation
can be observed/present; a supported direct exchange can be interacted. Divine
kind allows separate religious views without another interaction taxonomy.

Optional interaction fields: `importance: star | supporting | cameo`, `knownAs`
(source-specific name), `aiSummary` (at most one sentence), `passages`, `quotes`,
and `review`. Importance belongs to that interaction, not the permanent entity.
Preserve a whole conversation through brief interruptions, even across scenes.
There is no separate `fought` type.

### Passages and quotations

A passage requires `source`; optional fields are
`relevance: primary | supporting` and `aiSummary` (at most one sentence). Usually
one primary passage suffices, with additional passages for meaningful discontinuous
portions. Do not copy whole scenes or add a `purpose` field.

A quote requires `id`, `type`, `text`, and `source`. Types:

- `introduction`: wording introducing the entity, spoken by a PC or DM.
- `color`: a memorable line spoken by the entity.
- `whole`: the entire meaningful exchange is a short quotable passage, spoken by a PC or DM.

Quote IDs are session-unique. Featured-quote IDs must belong to that entity.
Quotes must be verbatim polished-source text, never reduction labels or fragments
joined across snips. There is no separate attribution field. Significant entities
may have several quotes.

Passages/quotes must fit inside the union of their interaction's scene/context
anchors without unlinked gaps. Passages are ordered and non-overlapping. A quote
can select part of a turn's text, but its locator still respects whole turns/UIDs.
Speaker/type interpretation and sentence limits require semantic review; the
mechanical validator does not establish them.

## Validation and projection

Install [requirements](../requirements.txt), then run from the vault root:

```bash
python3 -B .agents/skills/check-session-entities/scripts/session_model.py project --session-yaml PATH
python3 -B .agents/skills/check-session-entities/scripts/session_model.py validate PATH_TO_SESSION_JSON --require-coverage
```

Both commands are **read-only**, printing JSON to stdout. `project` requires
current scene and entity maps, preserves scene indexes and entity identities,
adds indexed contextual blocks, and checks full coverage. It does not fabricate
interactions, summaries, quotes, aggregate visited locations, or aggregate final review.
Explicit redirection can save a candidate but does not register it in YAML.
Legacy scene maps containing single `time` descriptions remain readable, but
projection stops until their endpoints are assigned from source evidence. It does
not silently drop the description or invent a start/end conversion.

Without `--require-coverage`, validation accepts partial candidates and reports
unaccounted UIDs. With the flag it requires complete scene/context coverage.
Neither mode certifies accuracy or completion. The returned
`publicationReady: false` is a validator result, not a stored final-session field.

Entity-map v2 upgrades remove the retired entity `reason` field and wrap each
exclusion's single source in an `occurrences` array. Verify inputs and preserve
all other decisions in a guarded v3 save. Version 1 additionally needs
source and identity rechecking because it depended on scene maps. Adapting
v6 final outputs requires reviewing divine classification and contextual ranges,
preserving compatible IDs/decisions, and validating v7; changing only the version
number is insufficient. No historical branch or extractor is a runtime dependency.

## Remaining integration

Final generation must consume map decisions rather than rematch everything,
produce evidence-grounded interactions, and bind the result to input/map revisions.
Visited-location review is independent of scene links. Safe selective review must
handle approval, corrections, inclusion/exclusion, candidate matching, merge/split,
deferred questions, and reruns without discarding accepted work. Approval of every
clear record is not intended.

Keep fingerprints, review evidence/history, excluded-source annotations, metadata
concerns, and progress outside final enrichment records. There is no implemented
processing-companion format or review-history store in these helpers. Entity-map
exclusions describe omitted candidates; source exclusions would explain why a
passage yielded no interaction, not form a third coverage bucket.

Only after review/application and completion checks are implemented should final
outputs be registered in YAML. Current stages never append `interactionExtraction`
output pointers or change existing note pipelines. Use existing beats/facts/recaps
only as optional review hints, not source registries or prerequisites.
