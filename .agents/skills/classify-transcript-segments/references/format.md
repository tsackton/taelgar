# Transcript segments — draft format 0.1

One `segments.json` partitions the polished transcript by activity. It does not partition the story into scenes.

## Envelope

Required fields:

- `schemaVersion`: `0.1-transcript-segments-draft`.
- `provenance`: `sessionId`, `sessionYaml`, `sessionYamlSha256`, `transcriptPath`, and `transcriptSha256`.
- `segments`: source-ordered array of records below.

Paths are vault-relative; SHA-256 values fingerprint the exact file bytes. Resolve the transcript through session YAML rather than guessing its filename. Source-local UIDs repeat between sessions; preserve them and use provenance to disambiguate.

Optional top-level `limitations` is a string identifying concrete missing or unread source material and its effect. It is not a review-status field. A partial file must identify its uncovered span and must not claim complete classification. Empty `segments` is valid only for an empty source or an explicitly disclosed inability to classify it.

## Segment record

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | Yes | Stable file-local reference, e.g. `s001`. Not a replacement source UID. |
| `source` | Yes | `{startUid, endUid}`: inclusive boundaries of the classified passage. |
| `category` | Yes | Exactly `gameplay`, `combat`, `meta_discussion`, `table_talk`, or `session_framing`. |
| `note` | No | A material boundary qualification, e.g. ordered combat without a roll, an inseparable mixed turn, or combat continuing beyond the transcript. |

Category semantics are defined in the skill. Do not add subcategories, scene names, summaries, actor inventories, confidence, review status, or mandatory boundary explanations. The source range supplies the evidence; copied transcript text is not required.

A completed file covers each polished turn exactly once, with no gaps or overlapping ranges. Check actual source order and turn membership, not consecutive UID integers: UIDs may skip numbers, one turn may span several UIDs, and several speakers may share a UID. Never split a shared-UID group between segments. Source order governs even during flashbacks or retrospective discussion. Adjacent same-category spans normally combine; two separately bounded combat encounters may remain separate so each can be referenced independently.

Illustrative record shape, not a claim about a real session:

```json
{
  "id": "s001",
  "source": {"startUid": "u0001", "endUid": "u0005"},
  "category": "session_framing"
}
```

Framing requires actual non-advancing introduction or recap content in those turns. The next segment begins where active play begins, even if the DM continues narrating uninterrupted.

## Gameplay backfill (0.2-transcript-segments-draft)

This revision is for explicitly selected existing bundles. The full-transcript procedure above describes 0.1. In a backfill, read the polished turns covered by each existing `gameplay` span. Split at sustained changes of activity, keeping whole turns and shared UIDs together. Use `exploration` for actively interacting with the environment, such as searching, inspecting objects or places, experimenting, navigating, and overcoming environmental obstacles. Use `social_interaction` for engaging with NPCs, through speech or other actions, and for played exchanges between characters. Use `planning` for weighing what to do next, in or out of character. Rules questions follow the activity they serve.

Use `session_framing` for recaps, introductions, and player-led character check-ins, including those that establish new details. A played conversation between the characters is social interaction. Clear out-of-character bookkeeping can be `meta_discussion`. Use `gameplay` for other actions, in-world developments, and mixed stretches when a more specific label would misdescribe what the table is doing. For example, stand-alone lore recall, narrated travel without active engagement with the environment, receiving unsolicited news, or routine healing can be gameplay. Keep ambiguous passages as `gameplay` rather than forcing a more specific label. Notes are optional for every category. Keep brief mixed moments with the surrounding activity. Preserve every span outside the original gameplay ranges, including its ID, exact boundaries, category, and note. Keep historical boundaries when necessary to preserve those records.

## Revisions and consumers

Preserve IDs for unchanged segments and human-adopted boundaries. When splitting or merging, retain an existing ID only for a clearly continuing segment and assign unused IDs to new segments; array order, not ID numbering, establishes sequence. Consumers bind to the exact file fingerprint. Changed boundaries or labels require reinspection of affected combat records, not blind fingerprint replacement.

The earlier three-session trial uses `schemaVersion: 0.1-trial`, a `transcript` provenance key, and the now-rejected broad `cutscene` category. It is historical evidence, not a current-format input. Reclassification must apply the narrow framing rule; renaming every old cutscene to session framing is incorrect. Do not rewrite trial files unless requested.

## Verification

Parse the JSON and verify required fields, enum values, ID uniqueness, existing UID endpoints, whole-turn boundaries, monotonic source order, and complete coverage unless a concrete partial-reading limitation is disclosed. Reinspect combat boundaries and framing semantics against source speech. Confirm YAML/transcript hashes match both the source and any bound downstream artifact. These structural checks do not prove semantic correctness.
