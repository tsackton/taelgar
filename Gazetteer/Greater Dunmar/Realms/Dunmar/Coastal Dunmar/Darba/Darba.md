---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/check/lint]
typeOf: settlement
typeOfAlias: city
mapLocation: { x: 4516, y: 7064.5, hex: 15.08.C.17/0541, importance: local, symbol: square }
name: Darba
whereabouts: Coastal Dunmar
dm_owner: tim
dm_notes: important
POV: modern
---
# Darba
>[!info]+ Information
> A city in [[Western Dunmar]], [[Dunmar]], the [[Greater Dunmar]]

%%needs some basic cleanup, plus collating various notes in Obsidian and OneNote%%

Darba is a walled city set on the rocky coast, perched above the flooded swamps of the [[Rudhan]] river. From a distance, the white walls of the old Drankorian fort that guards the harbor gleam in the sun, its six towers commanding a wide view across the bustling city. The old trade road follows the height of land north of the river, avoiding the flooded swamps of the delta in monsoon, approaching the old gates of the city, the ancient Drankorian wrought iron motifs of confronted lions framing the gate and visible even from a distance.

To the south of the walls, across the estuary, a shanty town of wooden dwellings and flooded, muddy streets stretches inland for some distance. Now, in the monsoon flood, small boats ply their trade back and forth along the river, many distinctive high-prowed Illorian poled boats. In the sheltered estuary, the masts of tall sailing ships can just be seen dancing on the waves at dock. Three and four masted, square rigged Chardonian trading caravels, small and fast Illorian lateen-rigged ships, and the occasional junk-rigged sailing ship with unusual stiff sails from farther afield. The Dunmari are not known as shipbuilders, but the occasional single-masted Dunmari longship patrols the waters.

To the north, the waves lap against the sea wall, a thin beach of sand and rock exposed at low tide. A few distant ships ride at anchor here, and small fishing boats heading out to sea are a common sight.

A steady flow of traffic - dwarves with iron wares to trade, merchant caravans loaded with exotic goods heading south to [[Nayahar]], halfling traders taking goods overland to [[Songara]], lumber and food moving in and out of the city.

The land along the river is marshy and not much settled, but the floodplains are fertile farmland and you pass many communal pastures and fields, and the occasional small village, although even here the population is restless and many dwellings are not permanent.

The north bank is less marshy than the south, and there are several weirs and water mills that dot the landscape just inland of Darba, helping fuel the industry of the city.

## History

- (DR:: 377): A Drankorian fort, to provide naval defenses for the western frontier of the Empire, is constructed at the mouth of the [[Rudhan]] river, in the location that will eventually grow to become the city of Darba. 
- (DR:: 1552): An Illorian captain, Chirce, claims sovereignty over Darba and the surrounding coastal plain
- (DR:: 1559): The Samraat Nayan Kundar drives the Illorian from Darba and reclaims the city 
- (DR:: 1644): A massive new public market is constructed in Darba by dwarven craftsfolk, commissioned by the Samraat to reflect the growing importance of Darba as a center of trade

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```

%%SECRET[v2:35f6a8ac46d40b8f5f2bc91bee1dcce2]%%

%%^Metadata:names:v1%%
- {name: Darba, language: unknown, pronunciation: DAR-bah, notes: "Cautious two-syllable spelling-based proposal: d and r as written, with ah vowels and first-syllable stress; the name's source language and an accepted pronunciation are not established in the reviewed sources.", status: proposed}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern city portrait during the summer monsoon, with selected older history; the DR 1749 political settlement is not incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and list formatting while preserving its values and `headerVersion`.
- Corrected “lanteen” to “lateen,” “not know” to “not known,” “fuel in the industry” to “fuel the industry,” “sovreignity” to “sovereignty,” and “surrouding” to “surrounding.”
- Added a primary name entry with unknown source language and a proposed pronunciation; added the typed settlement map skeleton.
- Recorded a broadly modern, monsoon-season article POV and the present account's temporal limitation.

### Validated judgments
- The positive `dm_notes: important` attestation has confirmed local evidence; it and `dm_owner` are preserved.
- The SECRET block was reviewed for recovery; its contents remain private and unchanged.
- `status/cleanup/text` is **not assessable**: the retained comment records a broader source-collation and editorial intention; the tag is preserved.
- Routine visits, purchases, and departures in [[Session 45 (DuFr)]] and [[Session 46 (DuFr)]] do not require a campaign log in this city reference.

### Editorial assessment
**Underdeveloped**: Darba's substantial geography and older history omit the central change in its political and civic position after the DR 1749 war. The smallest useful addition is a short account of the naval defeat and free-port settlement, establishing the relationship with Chardon and the surviving local Dunmari administration after a human chooses whether to update the article or retain an earlier snapshot. This is an established coverage gap, not a request to invent a general city history.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The visible history stops in DR 1644 and the header still places Darba in Dunmar. [[Session 117 (DuFr)]] records news of a Chardonian naval victory and entry into the city; [[Session 129 (DuFr)]] records the DR 1749-07-25 free-port settlement. [[Chardon-Dunmar War#Settlement and Ramifications]] additionally establishes Chardonian suzerainty and continuing Darban temple authority over Dunmari civic affairs. These are durable changes central to the city's reference account. Candidate addition: “After a Chardonian naval victory outside Darba in May DR 1749, the peace treaty of DR 1749-07-25 established the city as a free port under the suzerainty of the [[Chardonian Empire]]. The Darban temple administration retained authority over local Dunmari civic affairs.” Choose to update the article and its POV interpretation, defer with an appropriate human-assigned game-update tag, or explicitly preserve the earlier city portrait. For a layered update, the settlement passage could be placed in `%%^Date:1749-07-25%%` / `%%^End%%`; this visibility change remains a proposal.
- [ ] **Warning — correctness.internal_conflict:** The information callout says “A city in [[Western Dunmar]]” while frontmatter locates Darba in Coastal Dunmar. [[Dunmar#Regions]], [[Coastal Dunmar]], and [[Western Dunmar]] distinguish the Darba/Rudhan coastal region from the Nayan Floodplains region. Candidate header correction: “A city in [[Coastal Dunmar]], [[Greater Dunmar]].” Resolve the regional label together with the chosen political snapshot; the existing location metadata has been preserved.
- [ ] **Warning — metadata.names_unresolved_status:** The new primary name entry remains `status: proposed`. The reviewed sources do not establish the name's source language or an accepted pronunciation, so the language remains `unknown`. `DAR-bah` is a cautious spelling-based proposal: two syllables, d and r as written, ah vowels, and first-syllable stress. The Dunmari analogue guidance in [[Languages]] was consulted, but the city's location alone does not establish the name as Dunmari or justify assigning that language. Accept or correct the pronunciation; after acceptance, copy it to frontmatter and mark the entry documented.
- [ ] **Warning — metadata.map_location_missing:** The required settlement map entry now exists with `map: world`, but its `locator` is blank. Supply the verified world-map hex in that entry; the reviewed textual sources establish the city's position at the Rudhan estuary but do not provide an adopted world-map coordinate.

### DM evidence
- [[_DM_/Brainstorming/Campaigns Overview]]
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Staging/Darba (OneNote - v2)]]
- [[_DM_/Staging/NPC Ideas - Unused]]
- [[_DM_/Timelines/Apollyon Endgame Timeline]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Nayan Sura]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Hralgar (Session 62- )/Session 62/Session 62 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Emerald Song (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/General Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Copper Hills (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Darba Hinterlands (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Old Trade Road]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Road to Darba]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 45]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 46 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 47]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Character Developments/Scrying]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Events in Tokra]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Servius Scroll Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Secrets of Karawa]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Dunmari Magic - Old Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 112 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 113 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 114 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 121 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics - ChatGPT Summary]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 128 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Peninsula NPC Notes]]
%%^End%%
