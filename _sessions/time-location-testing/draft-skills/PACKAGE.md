# Structured transcript extraction package

Six complementary components, reviewed 2026-11-04. Four are uninstalled drafts in this directory; entities and interactions use the existing installed skills. This index groups the workflows; it does not install them, add a combined runner, or replace their format contracts.

| Component | Skill | Structured product | State |
| --- | --- | --- | --- |
| Location | [extract-location-markers](extract-location-markers/SKILL.md) | `location-markers.json`: place dictionary and sparse presence, movement, and observation markers; journeys at their narrated scale. | Draft |
| Time | [extract-time-markers](extract-time-markers/SKILL.md) | `time-markers.json`: source UID, inferred time/duration, exact evidence; supporting context/relationships and YAML date assessment. Separate temporal assertions remain separate markers. | Draft |
| Entities | [check-session-entities](../../../.agents/skills/check-session-entities/SKILL.md) | `<stem>-entity-map.json`: session entities, identities, inclusion decisions, importance, and evidence under the existing contract. | Installed |
| Interactions | [extract-entity-passages](../../../.agents/skills/extract-entity-passages/SKILL.md) | `<stem>-interactions.json`: coherent source exchanges, marked cuts, and entity roles/actions under the existing contract. | Installed |
| Combat | [extract-combat](extract-combat/SKILL.md) | `combat.json`: resolved turns and actions grouped into rounds, linked to combat segments and source evidence. | Draft |
| Segment classification | [classify-transcript-segments](classify-transcript-segments/SKILL.md) | `segments.json`: complete activity partition into gameplay, combat, meta discussion, table talk, and narrow session framing. | Draft |

## Dependencies and shared boundaries

All components resolve their source through session YAML and preserve existing source-local UIDs. A session ID, source revision, and UID together identify evidence. Each component retains its own format and provenance contract; membership in this package does not silently migrate existing artifacts or remove the established entity/interaction review model.

- Entities precede interactions; interactions bind to the relevant entity-map revision.
- Classification precedes combat; combat binds to the classification revision.
- Time and location remain independent. Location can optionally reference a fingerprinted time-marker file.
- None requires scene extraction. Classification is an activity partition, not a scene map or a filter authorizing other extractors to ignore parts of the transcript.

`session_framing` is limited to introductions, recaps, and similar narration outside active play. Narration that advances events—including travel, visions, flashbacks, and narrated outcomes—is gameplay, or remains combat during initiative. The historical three-session trial's broad `cutscene` labels are superseded; those outputs remain unchanged. An old cutscene cannot simply be renamed to session framing.

Draft outputs stay in agreed experiment directories under `_sessions/time-location-testing`. The installed entity and interaction skills retain their existing output locations and scope rules. Installing the drafts, migrating trials, building a package runner, or generating a combined session artifact are separate tasks.
