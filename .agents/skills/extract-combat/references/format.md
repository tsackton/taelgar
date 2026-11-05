# Combat extraction — draft format 0.1

One `combat.json` records resolved combat actions grouped into rounds. Source spans identify the evidence; round grouping does not assert precise round reconstruction.

## Envelope and dependency

Required fields:

- `schemaVersion`: `0.1-combat-draft`.
- `provenance`: `sessionId`, `sessionYaml`, `sessionYamlSha256`, `transcriptPath`, `transcriptSha256`, and `segments: {path, sha256, schemaVersion}`.
- `combats`: array in classification/source order. Use an empty array when the complete classification has no combat segments.

Paths are vault-relative; hashes are SHA-256 of exact file bytes. `provenance.segments.schemaVersion` must be `0.1-transcript-segments-draft`. Check the bound classification's session ID and both YAML/transcript hashes against this file. Referenced artifacts must remain current; changing hashes without reinspection does not refresh an extraction.

Optional `limitations` is a string describing concrete missing source, incomplete reading, or a requested subset of combat segments. Identify affected ranges or segment IDs. Do not use it for generic confidence or round-placement caveats. Omit absent optional fields and empty optional collections.

## Combat record

| Field | Required | Meaning |
| --- | --- | --- |
| `id` | Yes | Stable file-local combat ID, e.g. `c001`. |
| `segmentId` | Yes | ID of exactly one `combat` segment in the bound classification. |
| `encounter` | Yes | Short source-grounded label for finding the fight; no invented encounter name. |
| `rounds` | Yes | Ordered array of `{round, entries}`; numbers are consecutive positive integers beginning at 1. |
| `ending` | Yes | `{summary, evidence}` describing the result or unresolved state when the available source ends. |
| `openingActions` | No | Ordered action entries resolved before the regular initiative cycle, when the source warrants this distinction. |
| `note` | No | Material encounter qualification, e.g. an initial partial cycle or why a no-roll fight uses ordered turns. Not a round-confidence narrative. |

Each included segment has exactly one combat record. A complete whole-session output includes all combat segments; a selected subset must be disclosed in `limitations`. Source boundaries belong to the classification and are not duplicated on the combat record. Initiative setup and rules discussion remain part of that source span even when they yield no action entry. `rounds` can be empty only when the available segment contains setup but no resolved regular turns; explain that concrete situation in the ending.

A `round` labels the recorded initiative cycle, not six seconds of independently established world time. Do not multiply round counts into the time extraction or infer missing source rounds. Each round has a nonempty `entries` array.

## Action entry

Required fields:

- `actor`: consistent session-era character, creature, group, or environmental label. Use a descriptive unknown label when identification is unavailable; do not create entity-map IDs.
- `kind`: one of `turn`, `reaction`, `lair_action`, `legendary_action`, `villain_action`, or `event`.
- `summary`: concise but complete resolved actions and results for that entry.
- `evidence`: nonempty array of `{startUid, endUid}`.

Optional `note` holds material uncertainty about an actor, target, action, or result that the summary does not already express. No confidence, round accuracy, review status, mandatory initiative scores, complete stat blocks, or HP/resource tracking collections.

Use `turn` for regular turns, including explicit inability to act. Use named extra-action kinds only when the source establishes them; an unusual monster ability is not automatically legendary. `event` covers meaningful developments outside an ordinary turn, such as a new creature appearing or a freed spirit intervening. It is not a second entry for an outcome already fully represented in the same actor's turn. Summoning effects belong to the summoner's action; the summoned creature gets a separate entry when it acts.

An entry can condense several attacks or a spell and bonus action within one turn. It must preserve their distinct results rather than reducing them to “attacks the enemy.” Separate reactions from ordinary turns. Keep entries in the resolved sequence, normally following source order; a reaction may follow the triggering turn's condensed entry and explain where it occurred within that turn. Apply later corrections at the turn they correct, with citations to both passages. A retrospectively inserted movement and its opportunity attack belong at that earlier turn, not after intervening actors merely because they were narrated later. Do not count the corrective statement as a second action. Unresolved ordering remains a local qualification rather than a fabricated sequence.

### Detail to preserve during the dedicated combat pass

Check these against the complete labeled source segment, including enemy and summoned-creature actions:

- Preserve explicitly resolved advantage/disadvantage, critical hits and their modifications, saving-throw abilities and success/failure, and resulting damage or conditions. A successful save with damage is not equivalent to an omitted save; an unsuccessful attack is not an omitted action.
- Preserve stated damage types, resistance/immunity/vulnerability, healing, concentration changes, and effect durations or ending conditions when they explain the resolved action or its continuing effect. Retain the table's outcome when its rules application is unusual; do not supply missing details from rules knowledge.
- Preserve concrete benefits granted during combat or its resolution: recipients, effects or items, number of uses, and duration or location restrictions when stated. Do not reduce a one-use reroll and an item award to “blessings,” or extend the segment into subsequent looting.
- Preserve distinct actors' turns and off-turn actions, including meaningful movement and explicit inability to act. Condensing one actor's turn must not hide another actor's reaction or obscure when movement resumes after an intervening action.

These details belong in the existing `summary`, evidence, and optional local `note`; no new fields or roll/HP/resource ledger are required. Details can appear in other extraction products as well, but those products do not replace a complete combat summary.

Evidence ranges are inclusive, aligned to complete polished turns/shared-UID groups, and contained within the referenced combat segment. Use source order, not numerical UID arithmetic, to establish membership. Ranges may overlap when several actions occur in one turn of speech or a reaction interrupts another actor. Multiple ranges can support a single entry. Exact quotes are not required in this condensed product; the cited transcript remains the evidence.

Illustrative record shape, not an extraction from a real session:

```json
{
  "id": "c001",
  "segmentId": "s003",
  "encounter": "Bridge ambush",
  "rounds": [
    {
      "round": 1,
      "entries": [
        {
          "actor": "Jane",
          "kind": "turn",
          "summary": "Moves beside the guard and attacks twice: the first misses; the second hits for 8 damage.",
          "evidence": [{"startUid": "u0040", "endUid": "u0046"}]
        }
      ]
    }
  ],
  "ending": {
    "summary": "The transcript ends during the fight; the guard is still standing.",
    "evidence": [{"startUid": "u0046", "endUid": "u0046"}]
  }
}
```

The ending must state whether the encounter actually resolved in the available source, without a separate status taxonomy. A real completed fight would include all supported turns, not merely the one shown in this shape example.

## Verification and revisions

Validate required fields/enums, ID uniqueness, consecutive round numbering, all `segmentId` references, one record per included combat segment, and complete whole-session combat coverage unless a subset or limitation is declared. Check every evidence range against whole polished turns and the containing segment. Verify all source and dependency hashes.

Complete the combat skill's mandatory dedicated second source pass after classification/shared reading, using the detail checklist above. Compare source to entries for missing actions and resolution details, and entries to source for unsupported claims. Confirm corrections applied once, proposals not promoted into fact, reactions correctly positioned beside their triggers, summons distinguished from summoning, and a supported ending. Record concrete unread-source limitations, not a pass-status field. Reuse unchanged IDs and human decisions on revision. Changes in classification boundaries require checking affected entries and endings before refreshing the bound hash.

The historical `0.1-trial` outputs have different provenance fields and bind the earlier classification. They are not current-format inputs and are not migrated by this specification. This draft defines checks but does not include a general-purpose schema validator or automated semantic extractor; trial-specific checks do not validate arbitrary new outputs.
