---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
displayDefaults: {boxInfo: "<subspecies> (<species:s>), <pronouns>"}
tags: [person, testcase, status/gameupdate/dufr, status/check/lint]
species: undead
subspecies: lich
campaignInfo: []
born: null
gender: male
title: Emperor
name: Apollyon
aliases: [Emperor Apollyon]
pronunciation: ah-pol-LEE-on
whereabouts:
  - {type: home, end: 1059, location: Drankor}
  - {type: away, start: 1053}
  - {type: away, start: 1060}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: modern
---
# Emperor Apollyon
*(ah-pol-LEE-on)*
>[!info]+ Biographical Info  
> lich ([[Undead|undead]]), he/him  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The last emperor of Drankor, who is said to have wanted to become a god. Creator of the [[Scepter of Command]], and perhaps other artifacts of power. Was a very successful general and commander. 

Originally allied with [[Cha'mutte]], although towards the end of his reign this relationship turned to conflict and when he died, he was imprisoned and prevented from resurrection by [[Cha'mutte]]. 

%%^Metadata:names:v1%%
- {name: Apollyon, language: unknown, pronunciation: ah-pol-LEE-on, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern retrospective reference prose about Apollyon's imperial identity and original imprisonment; his later activity and defeat in DR 1749 are not yet represented.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting without changing existing values.
- Added `knownTo: [dufr]`, supported by the direct confrontation in [[Session 116 (DuFr)]] and [[Session 117 (DuFr)]].
- Added a minimal name block preserving the accepted pronunciation; the name's language remains unknown.
- Added `POV: modern` and a temporal-coverage note for the existing retrospective article.

### Validated judgments
- Confirmed local source matches support the existing positive `dm_notes` attestation; private contents have not been copied into this report.
- `status/gameupdate/dufr`: **not assessable** until the human chooses whether to update the article or preserve its earlier coverage. The later defeat is established; the tag remains unchanged.

### Editorial assessment
**Underdeveloped**. The visible note identifies the last emperor but lacks a central account of his imperial faction and persecution, the distinction between his lich transformation and imprisonment, and his modern campaign role and final defeat. The smallest useful scope is a short historical paragraph, a corrected imprisonment paragraph, and a dated campaign paragraph about his later plot and defeat. These gaps are established in shared reference and campaign sources; no new lore is needed to address them.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The opening reduces Apollyon's reign to military success and a reported ambition. [[History of the Drankorian Empire]] dates his rule to DR 1011–1059 and describes the empire's final push toward his godhood; [[Drankorian Empire]] identifies his strong association with [[Omnis Pura]]. [[Arheste#Arheste's Story]] records his theft of the [[Cloak of Rainbows]], destruction of Rostaurë, and persecution of the peronar. These define his historical role. Add a bounded historical account, keeping campaign testimony within a `Campaign:dufr` section. Copy-ready general opening: “Apollyon ruled the [[Drankorian Empire]] from DR 1011 to DR 1059 and was strongly associated with the Hkaran supremacist [[Omnis Pura]]. In the empire's final years, he turned its power toward his attempted ascent to godhood.” Copy-ready campaign addition: “According to [[Arheste]], Apollyon stole the [[Cloak of Rainbows]] from the orcs and used it to suppress [[Aldanor]]'s protection during his destruction of [[Rostaure|Rostaurë]]. In Drankor, he used the [[Scepter of Command]] to compel loyal legions and oversaw the persecution and slaughter of the peronar.”
- [ ] **Warning — correctness.cross_note_conflict:** Reconcile “when he died, he was imprisoned and prevented from resurrection” with [[Arheste#Arheste's Story]], which explicitly says he did not die that day, and [[Vision of Rai and Apollyon]], which distinguishes his hidden life force from the restraints on his magic, body, and tomb. [[Apollyon's Phylactery]] establishes the seven-soul dagger anchoring his undeath. The current wording collapses lichhood, imprisonment, and resurrection into one event. Copy-ready replacement for the final paragraph: “Originally allied with [[Cha'mutte]], Apollyon later became his enemy. He survived the fall of Drankor as a lich, his undeath anchored in [[Apollyon's Phylactery|an adamantine dagger]] forged through the sacrifice of seven souls, while Cha'mutte imprisoned him in [[Apollyon's Temple]].” Retain attribution or campaign scope for any further details taken from Arheste's testimony or the vision.
- [ ] **Warning — coverage.later_material_change:** The article ends with the original imprisonment and omits Apollyon's later attempt to return to power and his final defeat. [[Chardon-Dunmar War]] and [[Fausto]] establish his modern plot through Fausto and [[The Cleansed]]; [[Session 115 (DuFr)]] records the phylactery's destruction, and [[Session 117 (DuFr)]] records his death on DR 1749-05-24 and the prison's collapse on DR 1749-05-30. Choose whether to update the account and temporal framing, defer while retaining `status/gameupdate/dufr`, or intentionally retain the earlier account and have a human remove that tag. For an update, keep the later account campaign-scoped and make the final defeat visible on or after a DR 1749-05-24 date boundary; `died: 1749-05-24` is also supported but remains a proposal alongside that decision. Copy-ready addition: “In the DR 1740s, Apollyon worked through [[Fausto]] and [[The Cleansed]] to regain power, with their manipulation of Chardon and Dunmar serving his attempt to escape imprisonment. On DR 1749-05-24, the [[Dunmar Fellowship]] destroyed [[Apollyon's Phylactery|his phylactery]] in the [[Land of the Dead]], then killed him in the sanctum beneath [[Apollyon's Temple]]. His prison finally collapsed six days later.”

### DM evidence
- [[_DM_/Timelines/Apollyon Endgame Timeline]]
- [[_DM_/Timelines/Cloak of Rainbows Timeline]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/_Dunmari Frontier/Brainstorming - DM]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Agata Dustmother (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Apollyon (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Grash (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Hralgar (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Karmana (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Vola Forena (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Power Structures]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan Palace/Palace]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan History]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Monastery of Bhishma/Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Orc Stronghold/Orc Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 23 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival of Rebirth (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Individual Scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Session 16]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Tower Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Lair (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Seeker Solo Arc/Session 2 - Seeker]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Arc overview/Arc overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/History of Blasted Plains]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Leveling Up]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Major Players]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Arcs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Summary]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Old Notes 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Player Questions]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/The Relics of Apollyon]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Delwath (OneNote)]]
- [[_DM_/_Dunmari Frontier/Final Arc Planning - DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/DM Version - Bhishma Monastery]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Seeker Solo]]
- [[_DM_/_Dunmari Frontier/Session 0.75 Planning Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Apollyon Dopplegangers]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Arc Outline - The Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 0]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 1]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Adventure Part 3]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Circular Island Overview - DM notes v2]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Dragonet Info]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Ra'ghemdros Lair]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/FINAL/Ruins Secrets and Clues]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/Final Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/NOTES/Friday Morning]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/NOTES/Friday Night]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/NOTES/Thursday Night]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/Apollyon Tower Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/Circular Island Overview - DM notes v1]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/Circular Island Rewritten]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/Sessions Overview]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Circular Island/OLD/adventure_overview]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Outline v2]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 104 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 105 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Arc Outline]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Destroying the Phylactery]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Drankor Overview]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Fausto - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 112 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 113 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 114 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 115 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 116 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 117 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Seven Souls - Book of Martyrs]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Seven Souls]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Temple of Apollyon]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Timeline for the End of Drankor]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 118 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Politics]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 125 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Isingue Arc Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Limbo/Nantucket Planning]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Limbo/Rai Encounter - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Notes - Session 129]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Plaguelands Adventure]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Planning Update - Plaguelands]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 132 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 133 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 134 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/The Story of Apollyon and Cha'mutte]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Rescuing Hralgar]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 64 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Stormcaller Tower - DM Version]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 66 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Brainstorming - Scepter Arc]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Edge of Echoes - Map Key]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Prep Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 78 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 81 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 82 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 83 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 96 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 98-102 (Merfolk)/Session 98 - DM Notes]]
%%^End%%
