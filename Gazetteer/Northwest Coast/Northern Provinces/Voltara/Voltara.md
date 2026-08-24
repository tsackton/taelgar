---
headerVersion: 2023.11.25
lintedAt: "2026-08-24T09:25:51-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/text, status/gameupdate/gl, status/check/lint]
typeOf: settlement
typeOfAlias: city
campaignInfo: []
name: Voltara
whereabouts:
  - {type: primary, location: Greater Voltara}
  - {type: secondary, location: Northwest Coast}
dm_owner: tim
dm_notes: important
POV: 1747
---
# Voltara
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% copy remaining details from Great Library campaign %%

## Overview

Voltara, the northernmost substantial settlement in the Chardonian Empire, is a walled town of maybe 2000 people. It is situated on a grassy lowland steppe east of the [[Fiatara Mountains]], primarily supported by a large mining industry in the nearby hills, which are rich in chalyte. The grasslands are fertile land, and sheep farming and agriculture are common in the Voltara hinterlands.

%% NOTE
The plains around voltara are "pampas-like" I think -- key large mammals are deer and llamas, plus probably mountain goats/giant goats.
%%

Access to the walled town itself is heavily restricted. However, a decent-sized settlement has grown up outside the walls, oriented around the needs of the traveling merchant caravans that regularly depart carrying ore, precious metals, and more valuable goods extracted from the mines. Here, you can find taverns and inns aplenty, as well as a thriving bazaar.

Inside the walls, Voltara is a rich city, made wealthy on the chalyte trade. It is also a new city, largely constructed over the past two generations, on the site of a sleepy frontier fort after the discovery of chalyte in the hills to the north. Many buildings are constructed of white marble, the streets are wide and clean, and the entire town has an air of opulence about it.

## Precincts

![[voltara-outline.png]]

*Library (1):* At the northern edge of town is the academic precinct, which houses dormitories, a library, and various buildings associated with the archivists of the Great Library who come to study the inner workings of chalyte magic. The library complex is itself surrounded by walls, and overseen by Master Archivist Gaius. The wizard's gate leads north from this precinct. 

*Chalyte (2):* Southwest of the library precinct are a series of buildings and workshops involved in the sometimes-hazardous processing of chalyte ore, both for local use and for preparation to transport to Chardon. This area sometimes suffers from strange magical effects. 

*Baths  / Central  (3):* In the center of town is a large baths complex, and the main public market. The eastern part of this precinct, spilling into the temple precinct, is the wealthy part of town and dominated by manor houses and villas. 

*Temple (4):* East of the baths is a large temple dedicated to the Eight Divines. This is also a wealthy area with manor houses. The temple gate leads east from this precinct. 

*Artificer's Way (5):* South of the chalyte precinct, the street known as artificer's way runs south, giving this precinct its name, and terminating at the Waygate, one of the two primary gates to Voltara. While much of the chalyte mined here goes south to fuel industry in Chardon, Voltara has a small but extremely skilled community of artificers, largely centered in this precinct. The relatively minor Smallgate also exits west from this precinct.

*Fort Hill (6)*: The southernmost precinct sits on a small rise, on the site of the original border fort that once stood here. The proconsul, who administers the city in the name of the Magistros, is based here, as are the old fortifications and parade grounds pre-dating the city proper. The city gate exits south from this precinct. 

*Outer (7):* A large fraction of the population of Voltara lives in slums and settlements that have grown up along the south wall and extend along the main road leading south from Voltara to Lake Valandros and eventually Chardon. This area has no formal name, but many informal ones, and has a much more rough-and-tumble frontier feeling than the city proper.

## Inns 

[[The Purple Pig]]

A modest accommodation outside the city walls, run by Dravia. Modest accommodations, 1 gp per day. Destroyed by [[Grumella]].

The Sage and Spear

A comfortable inn just outside the town gates, in what passes for a small Dwarven district here. The innkeeper is a retired dwarven soldier named Orin Stonekeeper. It is a two-story stone building with two wings, and a large common room that tends to attract artisans and dwarves. Known for sausages.

[[The Wandering Toad]]

A small inn just inside the city gates, modest in size but welcoming and friendly. Considered comfortable accommodations, 2 gp for food, drink, lodging. Known for wild game, mushrooms, and ale. Run by a charming, friendly, and unusually large halfling man known as [[Finoc Small]].

The Ruby Flask

The premier lodging in Voltara. Can stay in private rooms with more modest food for 4 gp a day, or in a whole wing with servants and suites for 15 gp per day. Both prices include food, drink, rooms; the more expensive option includes servants as well. A three-story marble villa near the baths. Known for its wines and smoked meats. Run by a thin, prim and proper older human man, Decius Prixima.

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {name: Voltara, language: unknown, pronunciation: vol-TAH-rah, notes: cautious spelling-based reading; no language or name-specific pronunciation source was found, status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late DR 1747 portrait of the walled chalyte city after Grumella's attack; the DR 1752 political break and resulting city conditions are not represented.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Corrected objective typos, punctuation, and grammar in the overview, precinct, and inn descriptions.
- Added the required settlement map skeleton with its unsupported locator left blank.
- Added persistent name metadata with a cautious spelling-based pronunciation proposal.
- Recorded a DR 1747 POV and its temporal interpretation.

### Validated judgments
- The positive `dm_notes: important` attestation is supported by confirmed local `_DM_` sources; private contents were not copied into this report.
- `status/cleanup/text` remains supported by the still-rough inn entries and source-pointer comment; it was preserved unchanged.
- `status/gameupdate/gl` is not assessable until a human decides whether to update the article for the established DR 1752 change or preserve the DR 1747 snapshot; it was preserved unchanged.
- The shared comments were reviewed: one is a source pointer and the other preserves explicitly tentative ecological planning.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** As a settlement, Voltara requires a world-map locator, but neither the note nor the reviewed sources establish one. In `Metadata:map:v1`, replace the blank value with `locator: "<confirmed world-map locator>"` after the coordinate is supplied.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `vol-TAH-rah` only as a cautious spelling-based reading because the sources do not establish the name's language or pronunciation. Review the proposal; if accepted, add `pronunciation: vol-TAH-rah` to frontmatter and change the entry to `status: documented`, or replace it with the accepted form and derivation.
- [ ] **Warning — coverage.established_fact_missing:** [[Battle of Voltara]] and [[Grumella's War]] establish a defining DR 1747 siege and victory that the city article reduces to the unexplained destruction of one inn. Add after the overview: `In DR 1747, [[Grumella's Horde]] besieged Voltara. The city's defenders, aided by the [[Silver Tempests]] and their allies, broke the siege at the [[Battle of Voltara]], where [[Grumella]] was killed.`
- [ ] **Warning — coverage.later_material_change:** [[Great Library Session Notes - Arc 5]] records that by DR 1752 the [[Northern Provinces]] had split from the [[Chardonian Empire]] and Voltara was in political chaos, while the opening still presents Voltara as an imperial city. Choose one: update the article and `POV`; defer the change and retain `status/gameupdate/gl`; or intentionally preserve the DR 1747 snapshot and then review that status tag. If updating, revise the opening into a historical frame and add: `By DR 1752, the [[Northern Provinces]] had split from the [[Chardonian Empire]], and Voltara was in political chaos. The city's resulting government and physical condition are not yet established.`

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Chardon NPC Flowchart]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chalyte Oligarch]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics - ChatGPT Summary]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 126 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 126 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Mawar Confederacy/Ep 5 - Lost Legacy/Time Skip - Bullet Points]]
%%^End%%
