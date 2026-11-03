---
name: extract-location-markers
description: Extract sparse actor-specific location markers, visits, and journeys from a registered polished session transcript, retaining room/site hierarchy, routes, and UID evidence. Distinguishes physical presence from plans, reports, and magical views; does not publish entity whereabouts.
---

# Extract location markers — experimental draft

This uninstalled prototype was developed from five Dunmari Frontier sessions. Read [the shared experimental contract](../../format.md) before authoring. During this experiment all generated files stay under `_sessions/time-location-testing`; no installation or live-bundle writes.

Resolve the YAML-registered polished transcript and fingerprint source/YAML before reading. A time map is optional. If linking one, bind to its revision and preserve unknown times; location extraction must not depend on a scene map or on assigning time to every line.

Read in source order for actual presence, entry/exit, relocation, routes, returns, and changes of viewpoint or actor group. Search aids do not replace semantic context. Record meaningful room-level detail when stated, while avoiding a full trace of combat squares or every step. A continuous narrated multi-day journey can remain one route; a distinct stop or return is independently useful. Report limited reading scope honestly.

Author a **location A transition ledger**: actors, place or endpoints, movement type, framing, concise interpretation, and exact whole-turn UID evidence. Distinguish intended movement, accepted/narrated movement, arrival, threshold observation, and remote observation. “Toward Tokra” is not proof of arriving in Tokra. A scrying view of a harbor is not a physical visit. A player speaking in a scene is not necessarily a character present there.

Track split groups independently and keep concurrent errands marked. Preserve embodied location separately from what is seen in a vision, historical mirror scene, or dream. A ship is a mobile platform; establish its harbor/route context at particular markers rather than nesting it permanently inside a city. Do not move the entire party when one character scouts or swims ashore.

Build **location B places, visits, and route graph**. Use local place IDs for unnamed rooms, camps, and unresolved sites. Reuse a place ID for a return visit, retaining distinct visit IDs. Distinguish containment, adjacency, approach, above/below, and inferred shared context. Record doorway/stair topology only with evidence. Keep unknown route endpoints or geometry null; pointing at an unavailable map does not establish coordinates.

For a vault identity, search filenames, names/aliases, and variants; read the candidate note and surrounding source passage. Preserve session-era wording. Similar names are not identity, and modern note context does not establish historical movement. Leave `vaultPath` null when unresolved; never create or rename canonical notes as part of extraction. Do not fill room details from private DM plans that were not played.

Recheck each transition and actor scope, especially returns, bypasses, magical transport, and planned departures. Check source hashes, exact quotations, UID boundaries, place references, and hierarchy cycles. Verify that remote observations and future journeys generate no physical visits, and that a begun route does not generate an endpoint arrival. The pilot builder validates and projects the five authored examples only; it does not perform general semantic extraction.

Deliver both JSON views and readable place/path, actors, evidence, and UID tables. Lead with material identity or spatial uncertainty. Preserve human corrections and stale dependent projections when evidence changes. Stop before NPC whereabouts publication, campaign-map coordinates, scene partitioning, canonical geography changes, or skill installation unless requested.
