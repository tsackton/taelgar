# Sparse location markers — draft format 0.4

One `location-markers.json` contains a **place dictionary** and **source-ordered marker list**. A journey is a movement marker, not a separate collection. Places identify references; markers establish presence, movement, or relevant observation. This is not an exhaustive geography inventory or occupancy timeline. Existing A/B maps are not migrated by this specification.

## File envelope and source identity

Required fields:

- `schemaVersion`: `0.4-location-markers-draft`.
- `provenance`: `sessionId`, `sessionYaml`, `sessionYamlSha256`, `transcriptPath`, and `transcriptSha256`. Resolve the registered `transcriptProcessing.artifacts.polishedMarkdown`; do not guess the source filename. The lookup key and transcript processing status are not output fields. Session + source revision + UID identifies evidence.
- `places`: dictionary keyed by stable local IDs such as `p01`.
- `markers`: array defined below, ordered by `source.startUid` rather than reconstructed chronology.

Optional top-level `limitations` is a string describing concrete source or reading limitations that affect this extraction, such as an unread portion or missing source material. Identify the affected UID range when known and explain the impact. Omit generic disclaimers about source status, self-review, or lack of human approval. Reading the complete transcript remains an extraction requirement, not a `fullRead` field. Do not emit `review`, `readWindows`, or a review-status lifecycle.

Omit absent optional fields and empty optional collections. Null is permitted for an unknown movement endpoint; unknown is never zero or a guessed place. No separate visits, journeys, observations, planned movements, or spatial-graph collections.

Optional `provenance.timeMarkers` records `{path, sha256, schemaVersion}` only when linking a revised sparse time file. Check its session ID and transcript hash against this extraction. Optional marker `timeRefs` then contains IDs from that exact file. Do not link old time-B node IDs as if they were new markers. Location extraction remains independent when no time file exists; preserve directly stated journey durations locally. Changed source/YAML/time-file hashes require reinspection, not blind hash replacement.

## Place dictionary

Each entry requires `label` (session-era wording) and nonempty `evidence` (exact source references as defined below). Add only useful optional fields:

| Field | Meaning |
| --- | --- |
| `kind` | Concise category such as settlement, building, room, camp, region, or vessel. |
| `aliases` | Other transcript labels demonstrably referring to the same place, not speculative identity matches. |
| `vaultPath` | Verified vault identity; omit if unresolved. The match does not establish a visit or supply played geography. |
| `mobile` | `true` for a vessel or other moving place used as a location. |
| `relations` | Evidence-backed enduring physical relationships needed to interpret markers; see below. |
| `note` | Material identity uncertainty or limits not already expressed elsewhere; no generic extraction instructions. |

Reuse IDs for repeat visits and supported co-reference. Do not merge two unnamed camps, similar temples, or distinct rooms for convenience. Uncertain identities can remain separate with a note. Preserve existing human decisions and IDs during revision; IDs are session-local, not a global gazetteer.

Include only places needed to interpret markers, route references, or necessary physical context. Incidental hills, crossings, or landmarks can remain route text without dictionary entries. Do not require canonical notes for local places or catalog every room description. Place evidence may use a later naming passage to establish identity while markers preserve the earlier occurrence.

An enclosing site is necessary context when omitting it would leave only anonymous rooms or grounds. Retain supported named settings and regions in this dictionary and connect their local places with `within` evidence, without requiring extra markers for the parents. For example, a later identification of a family villa can identify the manor estate already containing the played grounds; it does not put the gardens inside the main house or establish a new arrival. Preserve a verified `vaultPath` for that site. The link resolves identity; it does not authorize importing modern whereabouts or containment from the note. Attribute useful vault-only orientation explicitly in `note`, including its source and temporal qualification, and keep it out of transcript-backed `relations`. Unknown parentage stays unknown.

## Marker core

Every marker requires:

| Field | Meaning |
| --- | --- |
| `id` | Stable local marker ID, e.g. `l01`. |
| `type` | `presence`, `movement`, or `observation`. |
| `source` | `{startUid, endUid}` for the passage stating/resolving the claim; inclusive whole polished-turn boundaries. This is a citation span, not exhaustive occupancy. |
| `actors` | Nonempty list of characters/groups to whom the claim applies; for observations these are the observers. Use `party` only when shared group presence/movement is supported. Retain an explicitly uncertain label when actor identity cannot be resolved. |
| `reading` | Concise interpretation distinct from literal evidence. |
| `evidence` | Nonempty array of `{startUid, endUid, quote}`. Exact contiguous excerpts from cited passages; preserve complete UID mappings for shared-UID turns and include context that establishes acceptance, correction, or actor scope. |

Optional `context` is `flashback`, `reported`, `vision`, or `planned`; omit for current play. Context qualifies every route/stop/arrival claim in the marker. A reported or imagined visit never establishes current physical presence. A marker for a current scrying action uses observation mode rather than turning the observer's embodied location into a vision. A later statement confirming an earlier current-play action need not be labeled historical merely because it uses past tense.

Use `reading` to state the interpretation and quantity `basis` to explain support for a value. Optional `note` preserves a material uncertainty or qualification not already expressed elsewhere; do not repeat explanations or include generic extraction instructions. The same restraint applies to place and relationship notes, without dropping meaningful location detail or evidence.

Optional `relations` is an array of `{type, target, note?}` linking to other markers: `during`, `overlaps`, `revises`, or `returns_to`. `during` asserts temporal containment; `overlaps` leaves containment uncertain; `revises` supersedes a prior claim; `returns_to` resumes the target's narrative context after a flashback/vision, without asserting identical time or place. Evidence must support each relation. Use one direction, not reciprocal duplicates; do not infer concurrency from different actors or source order alone. Immediate corrections normally consolidate into one marker with both quotations. Unresolved contradictions remain explicit, not silently marked as revisions.

## Presence, movement, and observation

### Presence

Require `place` referencing the dictionary. Use for opening presence, a meaningful spatial or actor/context change, or a distinct stop not sufficiently represented by movement. Later confirmation or description of the same ongoing location can support the existing record; it does not automatically require another marker. Presence is attested at this passage, not necessarily for every intervening line until another marker appears.

### Movement, including journeys

Require `from` and `to` (place IDs or null), and `completion`:

- `arrived`: the marker’s `evidence` must quote narration or an accepted compressed transition that places its actors at `to`. A later passage placing them there can supply that quote. If the evidence ends on the approach, use `underway`.
- `underway`: movement begun, destination not yet reached in the available evidence.
- `planned`: proposed/intended movement, not established as begun.
- `interrupted`: started but interrupted; destination arrival not established.
- `canceled`: proposal explicitly abandoned; retain only when useful to prevent a material misreading.
- `uncertain`: completion unresolved.

`to` is the reached or intended endpoint according to `completion`; it never independently proves arrival. An arrived movement needs a non-null destination, which can be a local unnamed place. An interrupted movement may name the intended destination and describe the actual stopping place in its route or a presence marker. Actor-specific arrival does not move companions. Planned/canceled markers use `context: "planned"` unless another narrative context, such as a flashback, needs that field; completion still prevents physical-presence inference.

Optional fields:

- `mode`: stated travel mode, e.g. walk, sail, fly, teleport.
- `vehicle`: dictionary ID for a vehicle relevant to the movement; not a permanent geographic parent.
- `route`: ordered route details, each `{reading, place?}`. Reading states whether a feature was crossed, passed, bypassed, approached, or briefly used as a stop. A place reference alone does not establish entry or a visit.
- `distance`: quantity object with supported unit such as mile, foot, or kilometer.
- `duration`: quantity object with unit minute, hour, or day.

Quantities require `precision` (`exact`, `approximate`, or `vague`) and `basis` explaining narrated, inferred, or estimated meaning. Use either `value`, supported `min`/`max` bounds (with inclusive booleans for supplied bounds), or vague `text` without invented numbers. Preserve the transcript's units. Forecast distance/duration does not become measured elapsed travel just because arrival is later established. This quantity convention matches the [time format](../../extract-time-markers/references/format.md); read that reference only if linking time markers or further temporal detail is needed. Do not reconstruct clocks or calendar dates as a prerequisite for location extraction.

**Granularity:** One five-line narration of 200 miles of travel can be one movement. Do not generate a marker or daily position for each geographical mention, implied camp, or travel day. Split for independently useful activity, party splits, changed destinations, or distinct movements, not distance or transcript length. A short scouting excursion can use the same origin/destination with the visited site in `route`. Record an independently useful stop as presence, optionally `during` the larger journey, without automatically replacing that journey with inferred daily legs. Avoid duplicating the same distance/duration across aggregate and component movements; where both are necessary, label containment explicitly.

Arrival is already established by an arrived movement; do not mechanically add a presence marker for the same evidence. Repeated descriptions of the same ongoing location can strengthen or clarify that record, including its role as a camp or stop. A place mention or substantial conversation there does not alone justify another marker. Meaningful returns, actor/context changes, and distinct stops not already represented retain their own markers and reuse place IDs.

### Observation

Require `place` (observed place) and `mode` (`local`, `remote`, or `vision`). Use only when useful for understanding movement, identity, or the distinction between seeing and entering. Optional `observerPlace` identifies the observer's separately evidenced physical location; omit if unknown. Optional `observedActors` records specifically witnessed subjects only when their identity matters to interpreting the location observation; keep them distinct from observers. Do not inventory everyone visible or extend this field into NPC whereabouts tracking. A remotely seen NPC is not a companion or a physical party visit.

Opening a door, looking through a wall, scrying, and historical mirror scenes do not establish entry. If entry later occurs, record its own supported movement/presence. Record narrative context changes and uncertainty about their scope; never move the embodied party to a viewed location.

## Where spatial relationships belong

- **Route facts:** On movement markers, e.g. north along the river, across the pass, bypassing a room through windows. Do not derive a permanent compass relation between endpoints merely from an initial travel direction.
- **Enduring place context:** Optional dictionary `relations`, each `{relation, target, evidence, note?}`. Use explicit meanings such as `within`, `near`, `adjacent_to`, `above`, `below`, `north_of`, or `connected_to`; retain doorway/stair detail in the note when useful. `target` is a place ID; `evidence` uses exact source references. No generic parent field. Near/adjacent is not containment. A shared regional context does not imply that one site is inside another.
- **Temporary placement:** Optional marker `locationContext`, an array of `{subject, relation, target, note?}` place references supported by that marker's evidence. For example, a presence marker can put actors aboard a ship (`place` = ship) while its location context places the ship `offshore_of` a port. The ship can later move. Do not attach that harbor as an enduring relation in the dictionary.

These relationships support interpreting the markers, not a separate mapping objective. Retain a room within a tower when needed for identity; do not reconstruct all floors, doors, or distances from every description. Mobile places may have enduring parts (a cabin within a ship), but no permanent geographic parent inferred from a temporary anchorage. Unknown geography stays unspecified; map gestures do not supply coordinates.

## Example: one narrated journey

Synthetic illustration only, assuming the dictionary defines `p01` and `p02`. The hills and river do not require their own IDs or visits.

```json
{
  "id": "l01",
  "type": "movement",
  "source": {"startUid": "u0100", "endUid": "u0100"},
  "actors": ["party"],
  "reading": "Ride from the monastery to the city over five days.",
  "from": "p01",
  "to": "p02",
  "completion": "arrived",
  "mode": "ride",
  "route": [
    {"reading": "Travel through the hills."},
    {"reading": "Cross the river."}
  ],
  "distance": {"value": 200, "unit": "mile", "precision": "approximate", "basis": "DM's narrated distance"},
  "duration": {"value": 5, "unit": "day", "precision": "exact", "basis": "narrated travel duration"},
  "evidence": [{"startUid": "u0100", "endUid": "u0100", "quote": "You leave the monastery and ride through the hills, cross the river, and reach the city five days later, having covered about two hundred miles."}]
}
```

## Verification and revisions

Check JSON parsing, required/type-specific fields, enums, quantities, unique IDs, existing place/marker/time references, whole-turn UID boundaries, exact quotation membership, source order, and unchanged hashes. Reject containment and revision cycles. Review substantive relationships and completions against evidence, including accepted hand-waves, canceled routes, split parties, returns, and observations. Verify that context/status prevents plans, historical reports, visions, and uncertain arrivals from becoming current visits. Confirm that repeated geographical mentions did not inflate a single journey into invented visits or positions.

Check optional time links against the bound file and shared source revision. Read the complete source before calling extraction complete; structural validity does not prove semantic completeness. Disclose concrete source or reading limitations in optional top-level `limitations`. Check that repeated descriptions of one ongoing location have not generated unnecessary markers and that notes contain material qualifications rather than repeated explanations or generic extraction rules. Preserve human decisions and stable IDs when revising, and recheck dependent relationships after source changes.

This draft has no general-purpose extractor or schema validator yet. Existing A/B builders do not validate it. Installation, migration of old outputs, publication of NPC whereabouts, map generation, and canonical changes remain separate work.
