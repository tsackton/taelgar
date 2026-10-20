---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {dPast: ""}
tags: [place, status/gameupdate/dufr, status/check/lint]
typeOf: settlement
typeOfAlias: city
ancestry: Dunmari
destroyed: 1545
name: Kharsan
whereabouts:
  - {type: home, end: 1544, location: Dunmar, wOrigin: "Originally part of <origin:1><(, )endstatus> <(in )enddate>"}
  - {type: home, start: 1545, location: Nashtkar, wPastHome: "Ruined <ancestry> <typeOf> <home:2qr>"}
dm_owner: tim
dm_notes: important
POV: modern
---
# Kharsan
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% clean up text; update based on post-Grash, post-Apollyon  changes %%

Once a major Dunmari city, now a ruin. At one point, was controlled by the undead warrior [[Grash]], until his defeat at the [[Battle for Uzgukhar]]. 

Set on the banks of the now-dry river [[Kharja]]. Much of the city, especially the northern sections, are in complete ruins. However, the palace square and the administration complex around it remain standing, as does the old stadium in the southern part of the city. 

Across the river from the city are cliffs on which stand two lines of massive monuments, north and south of the road. These are the Samraat Tombs, monuments to the rulers of the first dynasty of [[Dunmar]], the [[Aatmaji Dynasty]]. 

Although of varying sizes and designs, all share some common architectural features:
-   Five sided step pyramids / ziggurats, with steps/"arms" reaching out from the main base
-   A statue, temple, pyramid, something on top of the complex
-   A chapel/burial chamber underneath

%%SECRET[v2:b799f6c3183706c0e15393a7430efff1]%%




%%^Metadata:names:v1%%
- {name: Kharsan, language: unknown, pronunciation: KHUR-sun, status: proposed, notes: "No explicit name-specific pronunciation or source language was found. The Dunmari setting supplies the Hindi or other Indo-Iranian (Persian) analogue in [[Languages]]. Preferred Hindi-informed reading: kh is an aspirated k, both written a vowels are short uh, r/s/n are sounded, with tentative first-syllable stress. A Persian-informed alternative would use a throaty kh and could favor a final ah vowel and final stress. Exact in-world vowel values and stress remain unsettled."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern description of the surviving ruins, treating Grash's rule retrospectively after his DR 1749 defeat; the visible account does not yet incorporate the January 1749 change to the orc warren.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and dictionary formatting while preserving existing values and the header version.
- Added persistent name metadata with an unresolved, analogue-informed pronunciation proposal and unknown source language.
- Added the required typed settlement map block, leaving its unknown locator blank.
- Added `POV: modern` and a temporal-coverage note distinguishing the surviving ruins from the omitted January DR 1749 aftermath.

### Validated judgments
- Confirmed local sources support the existing positive `dm_notes` attestation; its value is unchanged.
- The SECRET block was reviewed. Its content and any recovery remain confined to local-only material and the private handoff.
- `status/gameupdate/dufr` is not assessable until the human chooses how to represent the established aftermath; the tag is preserved. The shared cleanup reminder records unfinished editorial work rather than additional canon.

### Editorial assessment
**Underdeveloped**: the visible entry describes the ruins and royal tombs but omits Kharsan's defining role as the Aatmaji administrative center, the plague devastation behind its ruined state, and the lasting January DR 1749 change to the orc warren. A short sourced history and one aftermath sentence can close these established gaps without inventing further city history.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The opening calls Kharsan only a former major city, and the tomb paragraph names the first dynasty without explaining why its rulers are associated with this city. [[Aatmaji Dynasty]] and [[Dunmar#Aatmaji Dynasty]] establish Kharsan as the dynasty's administrative center; [[Dunmar#Dharajun Dynasty]] establishes the later shift to Tokra. [[Cha'mutte's Plague]] establishes the destruction and lingering plague echoes at Kharsan. Add a bounded historical paragraph, for example: `Kharsan was the administrative center of [[Dunmar]] under the [[Aatmaji Dynasty]]. Under the [[Dharajun Dynasty]], the realm's administrative and religious center moved west to [[Tokra]]. [[Cha'mutte's Plague]] devastated Kharsan in DR 1545, leaving lingering hauntings among its ruins.` This supplies the central historical context without adopting the local-only historical draft.

- [ ] **Warning — coverage.later_material_change:** [[Session 89 (DuFr)]] records a durable change absent from this account: on January 26, DR 1749, the Fellowship burned the empty orc warren, and Kenzo and Riswynn cleansed spirits there, releasing trapped souls. Copy-ready addition: `On January 26, DR 1749, the [[Dunmar Fellowship]] burned the abandoned orc warren near Kharsan; [[Kenzo]] and [[Riswynn]] cleansed the site, freeing trapped souls.` This establishes the warren's fate, not a citywide end to the haunting. Choose whether to update the article and reassess its POV, defer while retaining `status/gameupdate/dufr`, or intentionally preserve the earlier account and dispose of that tag. A proposed `%%^Date:1749-01-26%%` / `%%^End%%` wrapper around only this new sentence would isolate its later visibility. No prose, date block, or game-update tag was changed automatically.

- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent proposal `KHUR-sun`. No accepted pronunciation or source language was found. The Dunmari context supports the Hindi or other Indo-Iranian (Persian) analogue in [[Languages]]: the preferred Hindi-informed reading uses an aspirated `kh`, short `uh` for both written `a` vowels, sounded `r`, `s`, and `n`, and tentative first-syllable stress. A Persian-informed alternative uses a throaty `kh` and could favor final `ah` and final stress. Exact in-world vowels and stress remain uncertain. Accept or revise the proposal; if accepted, set `pronunciation: KHUR-sun` in frontmatter and mark the entry `status: documented`.

- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now has `{map: world, locator: }`; no supported world-map locator was found in the reviewed evidence. Supply the verified coordinate in that existing locator field, for example `{map: world, locator: VERIFIED_COORDINATE}`, replacing the example token with the actual location rather than inventing one.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Agata Dustmother (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Apollyon (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Candrosa (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Grash (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Karmana (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan Palace/Palace]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan Approach]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan City Proper]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan History]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan Palace]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Mechanics]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Monastery of Bhishma/Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Orc Stronghold/Orc Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Orc Stronghold/Orc Stronghold Map]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Awakened Soul Monks]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Into the Desert]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Session 19]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Stone House]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 23 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Session 5 scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/The Situation in the South]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Distances and Travel Time]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-0]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 27]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 40]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Arc Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Archive Mysteries]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Servius Scroll Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/History of Blasted Plains]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Major Players]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Old Notes 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/The Relics of Apollyon]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Delwath (OneNote)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/DM Version - Bhishma Monastery]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Gnoll Warbands]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Isingue Arc Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Grash Arc Overview]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 82 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 85 - DM Notes]]
%%^End%%
