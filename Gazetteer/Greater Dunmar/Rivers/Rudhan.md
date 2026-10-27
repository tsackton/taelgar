---
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Rudhan
whereabouts:
  - {type: primary, location: Coastal Dunmar}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Rudhan is the principal river of [[Coastal Dunmar]], rising in the uplands of the [[Rudhan Heights]] and flowing southwest across the [[Darba Highlands]] to the [[Nevos Sea]]. Monsoon rains swell the river in summer, flooding riparian forests; in winter its flow slackens, exposing gravel bars and quiet eddies.

Near its mouth stands [[Darba]], a walled port city perched above the flooded swamps of the Rudhan’s estuary. The river’s deep natural harbor and strategic headlands made it attractive to Drankorian builders, and it has been continually occupied since. 

The Rudhan’s valley hosts a chain of small villages, often seasonally settled, along with waystations for travelers along the old [[Darba-Songara Road]]. Though no permanent bridges cross the river, it is easily forded in many places during the dry season. During the wet season, ferries provide crossings at many waystations, but the southern banks tend to flood and most travelers stay on the old Drankorian road, which crosses seasonal channels on stone causeways that seem to be able to withstand even the most intense floods.

%%^Metadata:names:v1%%
- {name: Rudhan, language: unknown, pronunciation: "RUDH-un", status: proposed, notes: "Preferred Hindi-informed reading from the Dunmari analogue guidance in [[Languages]]: first u short as in put, dh an aspirated/breathy d rather than English th, final a reduced to uh, and first-syllable stress. The name language and exact phonology are unestablished; a Persian-informed alternative would not preserve Hindi dh aspiration."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Rudhan Heights, map: world, locator: }
  - {role: outlet, feature: Nevos Sea, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography, seasonal flow, settlement, and crossings, with historical context for Darba's Drankorian harbor.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and added the explicit name.
- Corrected “in many place” to “in many places”.
- Added persistent name metadata with a proposed pronunciation.
- Added the required source/outlet map skeleton, naming the endpoints already established in the article and leaving their coordinates blank.
- Added `POV: modern` and broadly modern temporal guidance.

### Validated judgments
- The local source clusters and shared backlinks were reviewed. Plausible recoveries are reserved for the private handoff, and the human `dm_notes: none` attestation is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed `RUDH-un` pronunciation in the name block. The preferred Hindi-informed reading uses the Dunmari Hindi/Indo-Iranian guidance in [[Languages]]: u as in “put”, breathy/aspirated dh (not English th), reduced final a, and first-syllable stress. A Persian-informed reading could favor `roo-DAHN`, with different vowels, stress and no Hindi-style dh aspiration. The dh spelling favors the Hindi proposal, but neither exact phonology nor the name's language is established. Supply or accept the intended reading, then copy it to frontmatter and mark the entry documented.
- [ ] **Warning — metadata.map_location_missing:** The required map block now has separate `source` and `outlet` entries, but both `locator` values remain blank. The article establishes [[Rudhan Heights]] and [[Nevos Sea]] as the endpoints without establishing their world-map coordinates. Fill `source.locator` and `outlet.locator` with verified positions on `map: world`; retain the typed two-entry shape and do not infer coordinates from prose.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 46 - DM Notes]]
%%^End%%
