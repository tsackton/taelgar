---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
displayDefaults: {boxInfo: "<subspecies> (<species:s>), <pronouns>"}
tags: [status/cleanup/metadata, person, status/check/lint]
species: fey
subspecies: hag
campaignInfo:
  - {campaign: dufr, date: 1748-11-15, type: imprisoned}
born: null
gender: female
name: Agata Dustmother
aliases: [Old Woman of the Dusts, Dasoclese, Agata Dustmother]
whereabouts:
  - {type: home}
  - {type: home, end: 1, location: Amberglow}
  - {type: home, start: "", end: 1748-05-29, location: Garamjala Desert}
  - {type: away, start: 1748-05-29, end: 1748-11-15, location: Ring of the Warded Mind}
  - {type: away, start: 1748-11-15, end: 9999, location: Heartwood Grove}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Agata Dustmother
>[!info]+ Biographical Info
> hag ([[Fey|fey]]), she/her
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:DuFr%% Imprisoned by the [[Dunmar Fellowship]] on November 15th, 1748 in the [[Heartwood Grove]], [[Amberglow]], the [[Feywild]] %%^End%%

%% Original whereabouts annotation for {type: home, end: 1, location: Amberglow}:
# amberglow not origin, just past home
%%

![[agata-v2.png|right|300]]Agata Dustmother, often referred to as the "Old Woman of the Dusts," is an ancient and cunning fey hag, based for many years on the edge of the [[Garamjala Desert]], near [[Eastern Dunmar]]. 
## Overview

Agata Dustmother, known as the Old Woman of the Dusts, is an ancient fey [[Story about Hags|hag]] renowned for her plotting and deal-making skills, who always seems to emerge victorious in her bargains. She has dwelt at the edge of the [[Garamjala Desert]], in [[Eastern Dunmar]], for as long as anyone can remember, luring the desperate and unwary into bargains. She is fascinated by strange and especially gruesome magic, and is a collector of magic items, from the common to the extraordinary. 

In DR 1748, she was imprisoned in the [[Heartwood Grove]] in the [[Feywild]] realm of [[Amberglow]] by [[Dunmar Fellowship]]. 
## Description

![[agata-v1.png|left|300]]
Agata takes the appearance of a withered old woman, with dry, dusty skin, wearing white robes. Her lair is a magical and seemingly un-scryable hut hidden on the edge of the desert, surrounded by brambles and rocks, and only approachable if one follows the correct path.
## Events

- Agata was known as Dasoclese in the [[Feywild]] realm of [[Amberglow]]
- Agata was rumored to have been an ally of [[Cha'mutte]] in the [[Great War]], focusing on the pain of war refugees and survivors. It was suggested by [[Hralgar]] and by [[Delios the Sage]] that she never forgave the Dunmari for their role in the [[Great War]], and her later actions were often driven by vengeance. 
- In the early 1740s, Agata imprisoned Nayan [[Sura]] in a magic mirror, triggering a chain of events that led to the ascension of [[Nayan Karnas]], [[Sura]]'s brother, to the Dunmari throne, for mysterious ends.
- Acquired the [[Scepter of Command]] from the [[Fraternity of the Empty Moon]] sometime in 1747 or early 1748, in exchange for assisting the Fraternity in their plan to draw the energy of [[Pandemonium]] closer to Taelgar, strengthening the curse of lycanthropy and causing madness to spread across [[Dunmar]]. 
- Thought to be killed by [[Dunmar Fellowship]] at [[Shakun’s Wellspring]] on [[Session 28 (DuFr)|May 29th, 1748]].
- Masqueraded for months as a fey named [[Typhina]] in the [[Ring of the Warded Mind]], recounting [[Typhina]]'s story to [[Seeker]].
- Was finally imprisoned in the [[Heartwood Grove]] in [[Amberglow]] in the [[Feywild]] in [[Session 67 (DuFr)|November 1748]].

%%SECRET[v2:b38bce9a4308879e747dd76fa9ab78d3]%%
## **Other Notes**

- Agata possessed a magical substance called living wood, that she used to turn her victims into wooden puppets and worse. [[Jumi]], [[Cintra]]'s daughter, was in the process of being turned into a wooden mannequin when she was rescued by [[Dunmar Fellowship]] in [[Session 29 (DuFr)| May 1748]]. Also freed were:
	- [[Garret Tealeaf]], who had been forced into Agata's service as a wooden scarecrow before being turned back by [[Dunmar Fellowship]] on [[Session 30 (DuFr)|June 2, 1748]]
	- [[Shandar]], an old man who had been trapped as a table for decades, freed by [[Dunmar Fellowship]] on [[Session 30 (DuFr)|June 4, 1748]]
	- [[Kaya]], a Dunmari woman who had been trapped as a chair for decades, freed by [[Dunmar Fellowship]] on [[Session 31 (DuFr)|June 8, 1748]]

%%^Metadata:names:v1%%
- {"name": "Agata Dustmother", "language": "unknown", "pronunciation": "AH-gah-tah DUST-muth-er", "notes": "Cautious spelling-based proposal: hard g, three ah vowels with first-syllable stress, and ordinary English Dustmother. No name-specific pronunciation or name-language identification was found; Sylvan naming guidance is not a fixed phonology.", "status": "proposed"}
- {"name": "Old Woman of the Dusts", "role": "sobriquet", "language": "unknown"}
- {"name": "Dasoclese", "role": "historical", "language": "unknown", "pronunciation": "dah-SOH-kleez", "notes": "Used in Amberglow, as recorded in Session 67 (DuFr). Proposed Greek-patterned reading informed by the qualified Fey naming guidance in Languages: c before l is k, the ending is read kleez, with stress on SOH. The guidance is not fixed Sylvan phonology; the written final e and stress remain unconfirmed.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account of Agata’s desert activity, apparent death in May, and imprisonment in Amberglow in November; the present-tense desert description retains an earlier layer that needs reconciliation with her imprisonment.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- With explicit user approval, moved the exact Amberglow whereabouts annotation from YAML into a hidden comment below the complete header, preserving its original-field context and all whereabouts values.
- Added `knownTo: [dufr]` from the recorded campaign interaction, and normalized its `campaignInfo` code to `dufr`.
- Added persistent name metadata and proposed pronunciations, leaving frontmatter pronunciation unset.
- Added `POV: 1748` and temporal coverage notes distinguishing the desert account from the November imprisonment.
- Added the missing article in “Her lair is a magical and seemingly un-scryable hut.”

### Validated judgments
- The positive `dm_notes` attestation is supported by matching local sources; their contents remain outside this report.
- Reviewed the existing SECRET block; any recovery proposal is confined to the private handoff.
- `status/cleanup/metadata` is not assessable as a completed human cleanup request: its original intended scope is unspecified. Preserved unchanged.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** Three precise dates disagree with the cited session timelines. This note and [[Garret Tealeaf]] give Garret’s rescue as June 2, while [[Session 30 (DuFr)]] places the lair visit and rescue on June 4. The Kaya bullet gives June 8, while [[Session 31 (DuFr)]] and [[Kaya]] place her living-wood release in Bas Udda on June 5. The imprisonment header and `campaignInfo`/`whereabouts` transition give November 15, while [[Session 67 (DuFr)]] places the imprisonment on November 14 and the return to the Material Plane on November 15. Resolve these as linked continuity decisions. If the session timelines are confirmed, use `[[Session 30 (DuFr)|June 4, 1748]]` for Garret, `[[Session 31 (DuFr)|June 5, 1748]]` for Kaya, and `1748-11-14` for the imprisonment record and transition, with “November 14th, 1748” in the header; otherwise retain the dates and record the agreed session interpretation.
- [ ] **Warning — coverage.later_material_change:** “For mysterious ends” in the Sura event leaves Agata’s defining political manipulation unresolved despite [[Session 83 (DuFr)]] attributing a deliberate effort to destroy Dunmar from within to [[Delios the Sage]], and [[Session 90 (DuFr)]] / [[Nayan Marathu's Letter Vision]] revealing her forged letter used to discredit Sura. Decide whether to incorporate these revelations, defer them with the appropriate human-managed game-update status, or intentionally retain an earlier viewpoint. A bounded replacement for the Sura event is: “Agata imprisoned Nayan [[Sura]] in the [[Mirror of Soul Trapping]], enabling [[Nayan Karnas]] to claim the throne. According to [[Delios the Sage]], she sought to destroy [[Dunmar]] from within by sowing discord. She also [[Nayan Marathu's Letter Vision|forged a letter in Marathu’s name]], later used to portray Sura as her willing apprentice.” For an account that should reveal the forgery only from its recorded discovery date, place that final sentence inside `%%^Date:1749-02-02%%` / `%%^End%%`; this visibility change requires human approval.
- [ ] **Warning — temporal.mixed_current_state:** The overview says she “has dwelt” in the desert “for as long as anyone can remember, luring” victims, and Description presents her lair in the present tense, while the same visible article and [[Session 67 (DuFr)]] establish her November imprisonment. Preserve the historical desert account while choosing a coherent speaking position. Smallest prose proposal: replace the overview sentence with “Before her defeat in DR 1748, she dwelt at the edge of the [[Garamjala Desert]], in [[Eastern Dunmar]], for as long as anyone could remember, luring the desperate and unwary into bargains,” and begin the lair sentence “Her desert lair was a magical and seemingly un-scryable hut…”. If retaining the pre-imprisonment portrait instead, gate the later imprisonment statements with agreed `Date:*` blocks; do not use a broader POV to imply she remained active in the desert.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm the two proposed pronunciations in `Metadata:names:v1`. `AH-gah-tah DUST-muth-er` is a cautious spelling-based primary proposal: hard g, ah vowels, first-syllable stress, and ordinary English Dustmother. `dah-SOH-kleez` uses the qualified Greek naming pattern discussed for Fey in [[Languages]], with c before l read as k and a kleez ending; stress and the written final e remain uncertain. No explicit pronunciation or established name-language evidence was found. The language guidance is deliberately nonprescriptive, so neither proposal is accepted phonology; accept or replace the forms and copy an accepted primary pronunciation to frontmatter. The plain-English sobriquet needs no pronunciation.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated header still uses `%%^Campaign:DuFr%%`. [[Campaign Registry]] requires the canonical short code: replace that opening marker with `%%^Campaign:dufr%%`, preserving its entire contents and closing marker.

### DM evidence
- [[_DM_/Brainstorming/Campaigns Overview]]
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
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Cintra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Oduk (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Vola Forena (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Power Structures]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 49]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Feywild (Session 61)/Session 61/Notes - Feywild and Agata Adventure]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Feywild (Session 61)/Session 61/Session 61]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Feywild (Session 61)/Session 61/Typhina (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Awakened Soul Monks]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 19/Into the Desert]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 20]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 21]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 22]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 23 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 24]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Session 25]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival Visitors and NPCs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Festival of Rebirth (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa (Sessions 4-6)/Individual Scenes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 17]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/The Situation in the South]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Map Raven’s Hold]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Raven's Hold Demon Roster]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Raven’s Hold Text]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 11]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 12]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Raven's Hold/Session 13]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Session 15]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Stormcaller Tower/Session 16]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Tower/Session 14]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Emerald Song (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/General Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 46 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Lair (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Magic Items]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Karawa/Centaur Camp]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Notes - Shakun Heart]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Red Mesa (One Note)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 26-1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 27]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 28/Session 28]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Session 30]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 31]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Session 32]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Shakun's Heart Overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Postscripts/Postscripts]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Seeker Solo Arc/Session 2 - Seeker]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Arc overview/Arc overview]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Arc overview/Feywild Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Character Developments/Scrying]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 37]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 40]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Arc Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/History of Blasted Plains]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Magic Items - Dunmar]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Major Players]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Campaign Arcs]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Faction Action]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Main boss enemy ideas]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Mystai of Shakun]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Old Notes 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Overview - Dunmar Arc 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Player Questions]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Secrets of Karawa]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Timeline - Dunmari Old]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Solo Quests]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/The Relics of Apollyon]]
- [[_DM_/_Dunmari Frontier/Equipment Info DM Notes]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Chardonian Treasure Hunters]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Gnoll Warbands]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Agata Feywild]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Seeker Solo]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Brainstorming - Cloudspinner]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 66 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 73 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%
