# Session mapping pipeline

This contract describes the maintained source and mapping stages. The former
v7 `session.json` projection, schema, and validation helper are retired.

## Stages and ownership

```text
session YAML + registered polished transcript
    ├─ scene map: place/time partition and optional AI concerns
    └─ entity map: identity, selection, importance, and vault-link decisions
session YAML + registered prepared narrative
    └─ entity map
current entity map + selected focal entities + original polished speech
    → readable entity passages, with an optional scene map for navigation
```

Scene and entity mapping run independently. Neither requires beats or recaps.
YAML owns campaign/session metadata, dates, PC roles,
and source registration; do not create another manifest or participant list.

| Artifact | Contract | Ownership |
| --- | --- | --- |
| `cleaned/<stem>-scene-map.json` | [Scene map v2](../../map-transcript-scenes/references/format.md) | Complete transcript partition, places/times, map review, optional AI issues. |
| `cleaned/<stem>-entity-map.json` | [Entity map v4](format.md) | Identity, session importance, representative UID evidence, confidence/review, and meaningful exclusions. |
| `cleaned/<stem>-entities-review.json` | [Review workflow](review-workflow.md) | Durable human edits, feedback, exclusions, and guarded agent regeneration history. |
| `cleaned/<stem>-entity-passages.md` | [Passage workflow](../../extract-entity-passages/SKILL.md) | Selected original speech with marked cuts and source/map provenance. |

Existing recaps, excerpts, and highlight selections remain with their consumers.
Mapping does not regenerate them or register a final combined output in YAML.

## Fingerprints and review

Entity decisions bind to source/session fingerprints, not vault-note content
SHAs or scene maps. Vault-note edits do not block processing. Changed source
inputs require explicit human confirmation through the guarded entity helper;
acknowledgement preserves decisions/statuses without implying semantic rechecking.
See the [confirmation contract](review-workflow.md#confirm-changed-transcript-inputs).
Scene/context indexes are revision-dependent: consumers using them must bind to
the originating scene-map hash. Hashes prove neither completeness nor correctness.

The [review workflow](review-workflow.md) defines protected human decisions,
feedback, and guarded saves. Agents preserve stable IDs and accepted decisions
and recheck changed records. Validation alone never establishes semantic review.
Legacy entity maps are readable under their documented version rules; upgrading
requires explicit assessment and a guarded save, not a changed version number.

## Source references

Transcript references use the YAML artifact key and inclusive UID endpoints:

```json
{
  "kind": "transcript",
  "sourceId": "transcriptProcessing.artifacts.polishedMarkdown",
  "startUid": "u0013",
  "endUid": "u0137"
}
```

Ranges respect whole polished turns and whole UIDs. A turn combining UIDs cannot
be split; turns sharing one UID remain together. Original character offsets do
not authorize invented sub-turn locators. Recording timestamps are not in-world times.

Narrative entity maps use `kind: narrative`, `sourceId: preparedSourcePath`, and
whole prepared narrative units. Narrative support does not imply transcript
scene mapping or spoken passage extraction; see the [entity format](format.md).

Scene membership alone proves neither presence nor played action: a place/time
span can contain recaps, chatter, or hypotheticals. Inspect the original passages
and preserve their framing during entity review and passage selection.
