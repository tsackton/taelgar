# Experimental format contract — 0.1

This is a proposal, not an adopted session-artifact schema. All pilot writes remain under `_sessions/time-location-testing`. The two draft skills share this contract; neither changes the existing scene-map schema.

## Identity and provenance

Every map contains `schemaVersion`, `model`, `provenance`, `review`, `summary`, and `issues`.

`provenance` records session ID, YAML path/hash, registered polished artifact key, polished path/hash, processing status, and YAML date claims. The transcript is resolved through `transcriptProcessing.artifacts.polishedMarkdown`; it is not selected by filename guess or replaced with a recap. Four sampled sources retain transcription uncertainty.

A durable source identity is **session ID + polished artifact revision + UID**. Existing UIDs such as `u0002` repeat between sessions and are not global UUIDs. Preserve them; do not mint replacement UUIDs. Evidence uses inclusive `startUid` / `endUid` and an exact `quote`, aligned to whole polished turns. Shared UIDs belong together; retain multiple speakers when necessary. Recording timestamps are not in-world clocks. The full text remains in its existing source bundle.

A changed source or YAML hash requires reinspection, not updating the hash to make validation pass. B maps fingerprint their A ledger; location B also fingerprints time B. That lets downstream consumers detect stale derivations.

## Time A — `time-A.json`

`markers` is ordered by first evidence UID. A marker has:

- `id`: stable within this map revision; `kind`: date, clock, elapsed time, rest, overnight, framing, correction, etc.
- `frame`: `current`, `retrospective`, `flashback`, `vision`, `planned`, `reported`, `table`, `framing`, or `opening_boundary`.
- `actor`: party or named character/group.
- `reading`: concise interpreted meaning, separate from the literal evidence.
- `evidence`: nonempty exact source references.
- Optional structured readings: `clock`, `clockRange`, `month`, `day`, `yearBasis`, `duration`, `durationConvention`, `completion`, `supersededReading`, `acceptedReading`, `countGroup`.

`duration` carries a value or min/max, unit, and precision. Unknown is null/absent, not zero. “Few days” can stay a textual duration description; the schema does not decree numerical bounds. `countGroup` identifies a shared interval/activity, not an instruction to sum all members. A later rest confirmation and its earlier narration are one event.

`durationConvention` records the user's working assumptions of a one-hour short rest and eight-hour long rest. These are normalization conventions, not claims that the transcript states exact elapsed hours. Overnight may exceed eight hours; an eight-hour rest may occur in daylight. Interrupted, proposed, or retrospectively credited rests do not automatically add duration or a date boundary. Track any explicit exception from the transcript.

## Time B — `time-B.json`

`nodes` is in chronological order when supported. It is sparse and does not partition UIDs. Each node has an ID, label, supporting marker IDs, optional civil date, explicit date basis, and optional time-of-day description. Relative keys like `F`, `F+1` are useful when only a festival or another event anchors the sequence. Keep an unknown final date unknown even when YAML provides `drEnd`.

`constraints` connects nodes by relation, supporting markers, optional duration, optional date-boundary count, and count group. Relations can include `before`, `same_day`, `same_or_later_day`, `overnight`, `elapsed`, `parallel_activity`, and an explicitly excluded `prior_night` retcon. Concurrent actions can share endpoints or overlap an umbrella interval. No universal arithmetic solver is implemented in this pilot.

`nonAdvancingInSourceOrder` lists context markers that cannot naively move a running clock forward. This does not discard them: a played flashback can still contribute to reconstructed chronological coverage. A prior-night retcon outside a main-day span is explicitly excluded from that day's count. Define audit scope in the explanation; do not assume all YAML authors use identical flashback conventions.

`yamlAudit` contains the expected difference between `drStart` and `drEnd`, the supported count when determinable, narrower lower/partial counts when useful, and an explanation. Assessments in this sample:

| Value | Meaning |
| --- | --- |
| `supported` | Transcript dates and transitions substantiate the mapped span, with any inherited year noted. |
| `compatible_relative` | Observed transitions fit the YAML span length; absolute start is not independently established. |
| `underdetermined` | Missing/loose framing prevents a meaningful full-span confirmation. |

A production implementation should also support `conflict` with competing claims and evidence. This sample does not force an unconfirmed endpoint into that category. Distinguish nights explicitly narrated from calendar boundaries included in a journey montage. Dates May 3 → May 5 imply two boundaries, not three; sleeping twice in one day does not prove two nights. Never use `drEnd` to infer missing nights and then cite those inferred nights as validation of `drEnd`.

## Location A — `location-A.json`

`markers` is in source order. Each has an ID, kind, frame, actor list, concise reading, evidence, and a place or route endpoints. Optional fields include travel mode, vehicle, intermediate places, time-node references, concurrency group, confidence, and completion. Labels are denormalized for convenient display; IDs remain session-local.

Distinguish:

- `presence` or `arrival`: physical presence supported at the marker.
- `journey`: narrated physical transition, possibly only begun; unknown endpoint remains null.
- `observation`: local threshold/look-through observation without proof of entry.
- `remote_observation`: magical vision, scrying, remembered scene, or similar nonphysical view.
- `frame: planned`: intended movement, retained for review but excluded from accomplished routes.

Rooms may be separate places; ordinary movements inside combat do not need a full tactical trace. Record a meaningful return to a prior room. For long travel, use one route with approximate endpoints, optional waypoints/stops, and duration references; do not invent daily coordinates or campsite names.

## Location B — `location-B.json`

Collections:

| Collection | Purpose |
| --- | --- |
| `places` | Stable local identities, labels, kinds, optional parent and typed parent relation, evidence-marker IDs, optional verified vault path. |
| `visits` | Attested presence/arrival with actors and optional time anchors. Repeat visits are distinct. No exhaustive occupancy spans. |
| `journeys` | From/to, optional via nodes, actors, mode, vehicle, completion, evidence; `geometry: null` until independently supported. |
| `observations` | Remote or threshold views, kept outside visits. |
| `plannedMovements` | Intentions that do not establish arrival. |
| `spatialRelations` | Evidence-backed topology such as doorway, stairs, above/below, north-of, or bay approach. |

`parentRelation` is essential: `within` differs from `outside_adjacent_to`, `above_near`, `approach_to`, `part_of`, and `same_base_inferred`. A parent pointer is not automatically an occupancy inference. A regional grouping can contain a settlement and a nearby monastery without claiming the monastery is inside city walls.

A verified vault note is an identity aid, not proof of a visit and not permission to import modern geography or NPC histories into the session. `vaultCandidate` is explicitly unverified; leave `vaultPath` null. Do not confuse a similarly named temple, an upper mundane forge, or a lower magical forge. Unnamed rooms/camps can stay local. Mobile platforms have no permanent geographic parent; movements and time-specific harbor context establish their position.

A journey generates an arrival only when arrival is narrated. A route merely begun at departure produces no endpoint visit. A threshold observation does not generate an interior visit. Speaker membership in a passage does not prove in-world presence; player chatter, remote conversations, split parties, and narrated NPC reports need explicit handling. These pilot graphs primarily index the party and selected split actors, not an exhaustive NPC whereabouts inventory.

## Authoring, projection, and review

Each `authored.json` preserves manual decisions for the four projections. `author_*.py` reconstruct those annotations from the five pinned sources. `build_review.py` validates exact quotations, full-turn UID alignment, reference integrity, hierarchy cycles, known physical/prospective distinctions, source fingerprints, and date-boundary arithmetic; it renders JSON/Markdown/HTML. It cannot determine whether an omitted marker should have been found or whether an interpretation is correct.

The pilot's review label is `pilot-human-unreviewed`. A production lifecycle should distinguish unreviewed extraction, automated semantic review, and actual human decisions. Human corrections should be preserved by marker ID and source revision; changing evidence should stale dependent conclusions. Prior approval of a source transcript or skill is not approval of its new time or location map.

The recommended review surface is a compact table with date/time or place/path, claim, evidence quotation, UID, and visible uncertainty/framing. Exact quotations can be expandable. Keep an overview of elapsed date boundaries and material unresolved questions above the tables. Ask for human judgment only when uncertainty materially changes the chronology, identity, route, or intended scope; retain minor uncertainty without repeatedly interrupting.
