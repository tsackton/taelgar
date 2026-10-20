---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
name: Songara
whereabouts: Central Dunmar
dm_owner: tim
dm_notes: color
POV: modern
---
# Songara
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Songara is the westernmost city in [[Dunmar]], on the [[Stoneway]] near the [[Myraeni Gap]] and the traditional western boundary of the realm of [[Dunmar]].

Songara is located in the productive [[Songara Plains]] on the western edge of the [[Hara Basin]], on the fertile plains on the north bank of the [[Sone]]. It is a major center of animal husbandry and horse rearing in Dunmar, and historically grew around the ancient horse markets. Relatively untouched by the upheavals after the [[Great War]], Songara is among the oldest extant Dunmari cities. It was a major power center of the [[Dharajun Dynasty]], strongly associated with [[Jita]], the founder of that dynasty. 

Songara's economy is based on trade, but it has seen its wealth and power diminish with the growth of the [[Darba]]-[[Chardon]] oceanic trade. The decline in cross-Dunmar traffic, and the concomitant decline in [[Dunmari Economy#Land Ownership|tithes paid by travelers]] for the favor of the [[Dunmari Religion|Dunmari gods]], has also had a significant impact on Songara's economy. However, Songara remains the center of the breeding, rearing, and trade of the famous Dunmari horses, with thriving horse markets.

%%^Metadata:names:v1%%
- {"name": "Songara", "language": "unknown", "pronunciation": "sohn-GAH-rah", "notes": "Proposal from the Dunmari cultural context and the Hindi or Persian analogue in [[Languages]], favoring a Hindi-informed reading: o is oh, ng is the voiced cluster in finger, g is hard, and the two a vowels are rendered ah. Stress and vowel lengths are tentative; a Persian-informed adaptation could stress the final syllable. The name's own language is not explicitly attested.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and economic role, with historical background; the DR 1749 war and division of Dunmar are not incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter ordering and list formatting while preserving existing values and `headerVersion`.
- Corrected “the tradition western boundary” to “the traditional western boundary”.
- Added the primary name entry with a proposed pronunciation, the required settlement map skeleton, and the article’s broadly modern POV and temporal-coverage note.

### Validated judgments
- The regional references support Songara’s horse-market role, location on the western side of the Hara Basin, and association with Jita.
- Matching local sources support the positive `dm_notes: color` attestation; its value is retained.

### Editorial assessment
**Underdeveloped**: the article omits Songara’s established DR 1749 military outcome and its place in Sura’s central and eastern kingdom after Dunmar’s division. A short recent-history/current-allegiance paragraph and an agreed temporal viewpoint are the smallest useful addition. The existing geography and horse-trade account provides a useful foundation; no separate uninvented central dimension is asserted.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The required settlement map block is now present, but its `locator` is blank. Supply the supported world-map position in `- {map: world, locator: <coordinate>}`; no coordinate was established by the consulted textual sources.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `sohn-GAH-rah`. No name-specific pronunciation or language attestation was found in the target, regional references, or the place-name draft. The Dunmari cultural context supplies the Hindi or Persian analogue in [[Languages]]; this proposal favors Hindi: `o` is read oh, `ng` is the voiced cluster in “finger”, `g` is hard, and the two `a` vowels are rendered ah. Stress and vowel lengths remain tentative; a Persian-informed adaptation could stress the final syllable. Confirm or revise the complete pronunciation, then mark the entry documented and copy the accepted primary pronunciation to frontmatter. Keep `language: unknown` unless the name’s language is established.

- [ ] **Warning — coverage.later_material_change:** [[Session 117 (DuFr)]] records the Chardonian withdrawal from Songara in May DR 1749; [[Session 124 (DuFr)]] corroborates the withdrawal and reports the subsequent dispersal of deserters. The [[_sessions/dunmar-frontier/dunmari-frontier-139/cleaned/dunmar-frontier-139-session-recap#recap-003 | session 139 epilogue]], supported by finalized `beat-007`, places Songara in Sura’s central and eastern kingdom after Dunmar’s division. These changes materially affect the city’s recent history and political context, which the article omits. Choose whether to update the article and POV, defer that update with the appropriate human-selected game-update status, or intentionally preserve an earlier article and POV. Copy-ready addition if updating: “In May DR 1749, the Chardonian army withdrew from Songara. After Dunmar’s division, Songara remained part of the central and eastern kingdom ruled by [[Sura]].” Reconsider the unqualified opening “westernmost city in Dunmar” against the chosen realm and temporal frame; a bounded, frame-neutral replacement is “a city in northwestern [[Central Dunmar]]”. If retaining a broadly modern article with a dated withdrawal layer, the smallest supported proposal is `%%^Date:1749-05-25%%` around the withdrawal sentence, closed by `%%^End%%`; confirm a cutoff before placing the division/allegiance sentence in a new date block. Do not infer an exact division date from the epilogue’s mixed timeframes.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Staging/Darba (OneNote - v2)]]
- [[_DM_/Timelines/Apollyon Endgame Timeline]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chalice of the Runepriest (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Copper Hills (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Old Trade Road]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Road to Darba]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Riswynn Solo Arc]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Seeker (OneNote)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
%%^End%%
