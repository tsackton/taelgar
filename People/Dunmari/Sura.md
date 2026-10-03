---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [status/gameupdate/dufr, testcase, person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, date: 1748-12-26, type: scryed}
born: 1720
gender: female
name: Nayan Sura
aliases: [Nayan Sura]
affiliations:
  - {org: Nayan Dynasty, type: primary}
  - {org: Eastern Dunmar, type: leader, start: 1748-07-22, title: Samraat}
whereabouts:
  - {type: home, end: 1740, location: Darba}
  - {type: home, start: 1735, end: 1737, location: Lakan Monastery}
  - {type: away, start: 1740, end: 1748-06-08, location: Mirror of Soul Trapping}
  - {type: away, start: 1748-06-08, end: 1748-07-22, location: Karawa}
  - {type: away, start: 1748-07-22, end: 1748-12-14, location: Central Dunmar}
  - {type: away, start: 1748-12-14, end: 1748-12-22, location: Tokra}
  - {type: away, start: 1748-12-22, end: 1748-12-26, location: plains south of Tokra}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Nayan Sura
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her), of the [[Nayan Dynasty|Nayan dynasty]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Scryed by the [[Dunmar Fellowship]] on December 26th, 1748 on the [[Sukal Plains|plains south of Tokra]], [[Dunmar]] %%^End%%

Nayan Sura is the younger sister of Samraat [[Nayan Karnas]]. Once seen as a future Samraat and a unifier of [[Eastern Dunmar|eastern]] and [[Western Dunmar]], she vanished eight years ago, trapped by [[Agata]] Dustmother in the [[Mirror of Soul Trapping]]. In her absence, her brother, [[Nayan Karnas]], claimed the throne of [[Dunmar]]. In DR 1748, Nayan Sura was freed from [[Agata]]'s imprisonment, and now seeks to reclaim her destiny. 
## Overview

Sura was born in [[Darba]], but traveled widely in her youth, including spending several years at the [[Lakan Monastery]] in [[Tokra]]. From a young age, she was seen as god-touched, and perceived as a potential heir to the Dunmari throne, one who could unite the eastern and western factions of the divided country. Her future was cut short in DR 1740, when she was just 20 years old: she was trapped by [[Agata]] Dustmother in the [[Mirror of Soul Trapping]], and vanished. In DR 1748, she was freed by [[Dunmar Fellowship]], and began to contemplate reclaiming the throne, especially in light of her perception that Karnas had neglected the east, most notably in his decision to leave the eastern nomads to their fate during the [[Summer Gnoll Raids of 1748]]. In December of DR 1748, she defeated a small force of Karnas' warriors and their Chardonian allies in the [[Battle of Tokra]], laying claim to central and [[Eastern Dunmar]]. 
## Description

![[sura.png|400]]

Sura is a tall, striking Dunmari woman, with high cheekbones, light brown skin, medium length dark hair, and a regal bearing. 
## Events

- Spent two years learning under the guidance of the [[Lakan Mystai]] at the monastery outside [[Tokra]], from DR 1735 - DR 1737. 
- Traversed across [[Eastern Dunmar]] in DR 1740 with the then Samraat, Nayan Marathu, as part of a great census of all [[Dunmar]], the first census to travel east in many years. Between [[Bas Udda]] and [[Askandi]], she was kidnapped by [[Agata]]'s servants - lured out of her tent by a magically disguised [[Orcs|orc]] and then knocked unconscious and brought to [[Agata's Lair]] by [[Samerki]], where she was imprisoned in the [[Mirror of Soul Trapping]]. 
- Freed from the [[Mirror of Soul Trapping]] by [[Dunmar Fellowship]] in the summer of DR 1748. Seeing what seemed to be continued neglect of the needs of the east by her brother, she prepared to press her claim to rule, hopefully avoiding war and relying on the gods to give a clear sign of her favor. 
- Led her troops to victory against the Chardonian battle mages and a small group of Dunmari warriors loyal to Karnas during the [[Battle of Tokra]] on December 14th, 1748. 

%%SECRET[v2:59a26f873569533c2579be691dfe68fa]%%

## Timeline
```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {   yearStart: 1,   yearEnd: 2000,   pageFilter: "\"People/Dunmari/Sura\"",  includeAll : true })
 ```

```dataview
LIST WITHOUT ID events.text from #timeline or #event-source  flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```

%%^Metadata:names:v1%%
- {name: Nayan Sura, language: Dunmari, pronunciation: "NUH-yun SOO-raa", notes: "Proposed reading of this Dunmari dynastic and personal name using the Hindi analogue in [[Languages]]; consonantal y, a tapped r, reduced vowels in Nayan, and open vowels in Sura. Vowel lengths and stress remain unconfirmed.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-DR 1748 portrait after the Battle of Tokra, with earlier life and captivity as backstory; the visible account does not incorporate the DR 1749 negotiations and division of Dunmar.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting, canonicalized the existing campaignInfo code to `dufr`, and added `knownTo: [dufr]` from the recorded campaign interaction.
- Added a persistent name entry with a proposed pronunciation, and recorded `POV: 1748` with the article’s temporal limits.
- Canonicalized the generated callout’s campaign marker from `DuFr` to `dufr`; its enclosed text and closing marker are unchanged.

### Validated judgments
- The visible biography is a late-DR 1748 account after the Battle of Tokra; its changing political claims and “eight years ago” wording require the year rather than a broad modern or decade viewpoint.
- Confirmed local source matches support the positive `dm_notes` attestation. The SECRET block was reviewed and preserved; any recovery remains in the private handoff.
- `status/gameupdate/dufr` is preserved and not assessable until the human chooses whether to update the article or retain its earlier viewpoint.

### Editorial assessment
**Underdeveloped** as an ongoing reference to a major ruler: the central missing dimension is the outcome of Sura’s contest with Karnas and the resulting division of Dunmar in DR 1749. Her origins, imprisonment, return, and initial military victory are already explained. The smallest useful update is a short account of the negotiations and settlement; the consulted public records establish that transition, so no separate invention-based gap is asserted.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The Overview and Events stop with the December 1748 victory, leaving Sura’s resulting rulership and relationship with Karnas unresolved. [[Session 90 (DuFr)]] records the exposure of forged evidence and the opening of negotiations in February 1749; [[Session 117 (DuFr)]] records her refusal to cede central or eastern territory during the Chardonian peace talks; [[Session 129 (DuFr)]] records the treaty on DR 1749-07-25 dividing Dunmar between the siblings. These are lasting political consequences. Choose whether to update the account and POV, defer the update and retain `status/gameupdate/dufr`, or intentionally retain the DR 1748 portrait and remove that tag by human decision. Copy-ready update candidate: “In February DR 1749, negotiations between Sura and [[Nayan Karnas]] began after evidence portraying her as [[Agata]]’s pawn was exposed as a forgery. During the later peace talks with [[Chardon]], Sura refused to cede territory in [[Central Dunmar]] or [[Eastern Dunmar]]. The treaty concluded on July 25th, DR 1749 divided [[Dunmar]] between Sura and Karnas, while [[Darba]] became a free port.” Cite [[Session 90 (DuFr)]], [[Session 117 (DuFr)]], and [[Session 129 (DuFr)]] with the adopted account; do not infer further treaty boundaries from this summary.
- [ ] **Warning — metadata.names_unresolved_status:** The new name entry proposes “NUH-yun SOO-raa” for Nayan Sura. This is a Hindi-leaning reading using [[Languages]]’ Dunmari guidance (“Hindi or other Indo-Iranian (Persian)”): consonantal y, tapped r, reduced vowels in Nayan, u as oo, an open final a, and light initial stress in each name. The spelling does not establish vowel length or exact stress, and the Persian alternative does not supply an adopted in-world rule. Confirm or replace the proposal; if accepted, copy `pronunciation: NUH-yun SOO-raa` into frontmatter and set the entry’s status to `documented`.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Timelines/Apollyon Endgame Timeline]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Agata Dustmother (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Nayan Sura]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Session 48]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Feywild (Session 61)/Session 61/Session 61]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 17]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/General Notes]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Agata Dustmother/Agata's Magic Items]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 31]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Session 32]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Character Developments/Scrying]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Events in Tokra]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Lakan Monastery (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 37]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/Campaign Outline]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Old Notes 1]]
- [[_DM_/_Dunmari Frontier/Fox and Hunter Intro]]
- [[_DM_/_Dunmari Frontier/Leveling]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Raw Notes - Agata Feywild]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Planning Update - Last Jade]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 104 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Arc Outline]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 111 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 112 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 113 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 114 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 115 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 111-117 (Drankor)/Session 116 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 120 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Chardon Timeline]]
- [[_DM_/_Dunmari Frontier/Session 124 - 128 (Chardon)/Session 124 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 129 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 130 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 66 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 70 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 71 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 69-73 (Grash Arc)/Session 72 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Prep Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 96 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 97 - DM Notes]]
%%^End%%
