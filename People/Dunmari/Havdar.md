---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/dufr, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, person: Delwath, date: 1748-12-27, type: scryed, format: "<met:U> by <person> in <current:fr!>, on <target>"}
born: 1724
gender: male
name: Havdar
affiliations:
  - {org: "Havdar's Warband", type: leader, title: Commander}
whereabouts:
  - {type: home, location: Karawa}
  - {type: home, location: Eastern Dunmar}
  - {type: away, location: "Havdar's Warband", wCurrent: ""}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Havdar
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Scryed by [[Delwath]] in [[Songara]], [[Dunmar]], on December 27th, 1748 %%^End%%

%% still need some work on people in organizations for whereabouts; needs updated image; updated campaign info; updated whereabouts and organization/affiliation info; 

needs updating to bring current; needs a bit of a rewrite to incorporate no-longer-secret secrets, mention curse and resolution
%%

![[havdar.jpg|right|350]]Havdar, a brash and confident warrior, made a name for himself as a war leader in [[Eastern Dunmar]], before joining with Nayan [[Sura]] in support of her claim to the leadership of the Dunmari people. 
## Overview

Havdar was born outside [[Karawa]], and grew up herding goats amongst the rough, rocky deserts and scrublands of [[Eastern Dunmar]]. Always passionate about the traditions of the Dunmari, he is dedicated to his homeland and [[Eastern Dunmar]], and the traditions of his people, and skeptical of the city folk to the west and especially the Samraat. Blessed with natural strength and dexterity, Havdar gathered a small group of dedicated warriors around him, and became known as something of a protector of [[Eastern Dunmar]]. He often speaks reverently about the [[Red Mesa]], the [[Gomat]] Oasis, and other landmarks of the eastern plains.

In the summer of DR 1748, he took on a pivotal role as the chief general to Nayan [[Sura]], standing steadfastly by her side as she asserts her claim to the Dunmari throne.
## Description

Havdar is tall, imposing, and rugged, shaped by the relentless sun and winds of the Dunmari plains. He has dark, tangled hair and a short, scrubby beard. He is usually wearing armor and carrying his spear.

## Relationships

- Nayan [[Sura]]: As her chief general and most trusted advisor, Havdar is unwavering in his loyalty to Nayan [[Sura]]. Their bond is strong, and he's fully committed to supporting her claim against her brother, even if it leads to civil war. Havdar first met her when she traveled in the east when he was young, and as a teenager was devastated by the news of her disappearance. He considers her rescue and reappearance a blessing from the gods. 
- [[Nayan Karnas]]: Havdar is disdainful of [[Nayan Karnas]], feeling him a weak ruler who has abandoned the traditions that made [[Dunmar]] great. Has often pushed for war, thinking Karnas will be unable to command the loyalty of enough warriors to fight back. 
- [[Havdar's Warband]]: Originally a close-knit group, they have grown under Havdar's leadership into a force that stands against threats from the [[Nashtkar]] and elsewhere. Havdar's troops now serve as elite warriors in [[Sura]]'s service. People in Havdar's band include [[Aram]] and [[Camana]] (deceased). 
- [[Dunmar Fellowship]]: Initially indifferent, perhaps even skeptical, of the [[Dunmar Fellowship]], grew to respect and greatly value them over the course of a month traveling in the eastern deserts together, during which [[Dunmar Fellowship]] [[Session 20 (DuFr)|helped defend his camp from orc attackers]]. 
## Events

- In March/April 1748, was heavily involved in defending [[Karawa]] from gnoll attacks. 
- In April/May 1748, scouted the eastern deserts with [[Dunmar Fellowship]]
- In August 1748, was petrified by a cursed sword taken from [[Agata's Lair]], gifted to him by [[Dunmar Fellowship]], who were unaware it was cursed.
- In September 1748, was restored, but became increasingly paranoid as the subtle curse of the sword still worked its evil magic. 
- In November 1748, the curse was broken by [[Riswynn]]'s prayers, and the cursed sword destroyed by the [[Bahrazel]], freeing Havdar of its evil influence. 
- In December 1748, led [[Sura]]'s army in the [[Battle of Tokra]]. 
## Rumors and Information

- Havdar was a major proponent of war with [[Nayan Karnas]], but whether this was the result of the curse of the sword, or his own opinion, is hard to know. 
- While cursed, became increasingly paranoid, seeing threats in everything.

%%SECRET[v2:2efb0c3bf03d749a162348cb77bc9589]%%

%%^Metadata:names:v1%%
- {name: Havdar, language: unknown, pronunciation: "hav-DAAR", notes: "Proposed from his Dunmari cultural context and the Hindi/Persian analogue in [[Languages]], favoring a Persian-style reading: short first a, long final a, v, a tapped r, and final prominence. The name's language, exact vowels, and stress are not explicitly recorded.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-DR 1748 portrait of Havdar as Sura's chief general, with selected earlier history and events through the Battle of Tokra; the relationship prose still contains a prewar perspective, and his later border command is not covered.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and list formatting; added `knownTo: [dufr]` from the recorded campaign interactions and canonicalized the existing `DuFr` metadata and block code to `dufr`.
- Corrected “became know” to “became known” and added the missing article in “a short, scrubby beard.”
- Added a proposed pronunciation in `Metadata:names:v1`, and recorded `POV: 1748` with the article's temporal limits.

### Validated judgments
- The biography establishes Havdar's identity, loyalty to Sura, command, and the curse's resolution. [[Session 69 (DuFr)]] corroborates the November 1748 cure; incidental travel, gifts, and individual encounters do not require further reference coverage.
- Confirmed local sources support the positive `dm_notes: important` attestation. The `SECRET` block was reviewed; its contents remain outside this report.
- The ordinary comment is an editorial reminder, not an unadopted public account. The undated home entries may encode origin and home; their multiplicity alone is not a defect.
- `status/gameupdate/dufr` is not assessable until the human decides whether to update this portrait or retain its earlier POV; the tag is preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new Havdar entry proposes `hav-DAAR`. [[Languages]] gives Dunmari a Hindi or other Indo-Iranian (Persian) analogue; this proposal favors a Persian-style reading with a short first a, long final a, v, tapped r, and final prominence. This is cultural guidance, not established in-world phonology, and the name's language remains `unknown`. Accept or revise the proposal; on acceptance, copy the agreed pronunciation to frontmatter and mark the entry `documented`.
- [ ] **Warning — correctness.cross_note_conflict:** `born: 1724` makes Havdar about fourteen around DR 1738. [[Wellby#Journey with Havdar|Wellby's account of the Session 32 journey]] instead remembers the royal visit about ten years before DR 1748, when Havdar was “in his late teens.” The target's Sura relationship also calls him a teenager when she disappeared in DR 1740. These approximate recollections do not establish one safe replacement birth year. Confirm the birth year and the intended age at the visit/disappearance together; preserve the source account and do not derive a new exact year solely from “about 10 years ago.”
- [ ] **Warning — temporal.mixed_viewpoints:** The Sura relationship says Havdar supports her claim “even if it leads to civil war,” but Events already records his participation in the December 1748 [[Battle of Tokra]], part of the [[Sibling War]]. Choose a coherent retrospective or explicitly earlier framing. For the late-1748 portrait, replace that sentence with: “Their bond is strong, and he supported her claim against her brother during the [[Sibling War]].”
- [ ] **Warning — coverage.later_material_change:** The article stops at the Battle of Tokra and omits Havdar's subsequent border command. [[Session 90 (DuFr)]] records Sura's February 1, 1749 report that he was fortifying Dunmar's northwestern border along the [[Myraeni Gap]]; [[Havdar's Warband]] also records his force's later role as Sura's elite guard based in Tokra. This gives his command a later setting and purpose beyond the eastern frontier and the contest for the throne. Decide whether to update the article and POV, defer with `status/gameupdate/dufr`, or intentionally retain the late-1748 portrait and remove that tag after human review. If updating, a bounded addition is: “By early DR 1749, Havdar was fortifying Dunmar's northwestern border along the [[Myraeni Gap]]. His [[Havdar's Warband|warband]] developed into Nayan [[Sura]]'s elite guard, based in [[Tokra]].”

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Candrosa (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Cintra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Grash (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Orc Stronghold/Orc Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Bas Udda (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Havdar's Band]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Into the Desert]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Session 19]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival of Rebirth (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Gnoll Attack]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Session 5 flowchart]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Session 5 scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Session 6 scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 17]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Situation in Karawa After Raven's Hold]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Distances and Travel Time]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Centaur Camp]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Mystai]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Situation in Karawa - Shakun Arc]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Red Mesa (One Note)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-0]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 27]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 31]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime Timeline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Session 32]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Old Notes 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Overview - Dunmar Arc 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Gnoll Warbands]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 115 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%
