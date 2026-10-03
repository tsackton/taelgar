---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: stoneborn
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-12-29, type: met}
born: 1666
activeYear: 1732
gender: female
name: Umli the Exile
aliases: [Umli]
whereabouts:
  - {type: home, end: 1731, location: Svinjo Mountains, wOrigin: "Exiled from <origin> in <enddate>"}
  - {type: home, start: 1732, location: Tollen, wHome: "Based in <home:r> (for <age>)"}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1740s
---
# Umli the Exile
>[!info]+ Biographical Info  
> A [[Stoneborn|stoneborn]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on December 29th, 1748 in the [[Tollen|Free City of Tollen]] %%^End%%

![[umli-the-exile-portrait.png|right|320]]Umli is a tall, imposing stoneborn, with gray skin marked with intricate patterns reminiscent of intertwining metalwork and intense obsidian-like eyes. She is a master metalworker and smith, known for her unparalleled mastery of metallurgy and her knowledge of the elemental plane of fire.
%%^Date:1732%%
Born in the southern [[Svinjo Mountains]], she was exiled from her Stoneborn community for reasons she keeps private, and has lived in [[Tollen]] since DR 1732. 
%%^End%%
%%^Date:1738%%
Though loosely affiliated with the [[University of Tollen]], she does not teach open lectures. She only takes private students who are the most skilled and dedicated at working with rare metals. 
## Rumors and Information
- There are murmurs of Umli once attempting a creation using a metal sourced from a location she keeps secret. Whether this is related to her exile, none will speculate, for Umli is quick to anger if she learns anyone speculating about the reasons for her exile. 
- Umli is exceedingly private. She never takes visitors in her home/forge, and usually takes her meals alone.
- Once a week, on Tuesdays, she takes interviews for new students in a dwarven tavern near campus called [[The Fire and Stone]], and will also sometimes speak to clients desiring her skills in smithing then as well. 
- Once a week, on Fridays, she tests her student's work at her forge. No one is allowed in, but a crowd gathers outside and she takes each item presented to examine. 
%%^End%%

%%SECRET[v2:fb83a07c7b5633edf08597937b2be2e7]%%

%%^Metadata:names:v1%%
- {name: "Umli the Exile", language: "unknown", pronunciation: "oo-MM-lee the EG-zyle", notes: "Proposed from the Stoneborn cultural context and its Xhosan analogue in [[Languages]]: the stem is read with a syllabic m between oo and lee, lengthened on that penultimate beat. The English epithet is read ordinarily; the complete name’s source language and tones are not established.", status: "proposed"}
- {name: "Umli", role: "alias", language: "unknown", pronunciation: "oo-MM-lee", notes: "The existing alias and visible short form; same Stoneborn/Xhosan-informed proposed stem reading as the primary entry, with syllabic m.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Umli as an active smith and private teacher in Tollen; existing date blocks separately begin the exile/residence account in DR 1732 and the teaching account in DR 1738.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the missing article in “Umli is a tall, imposing stoneborn.”
- Corrected the origin’s transposed spelling to Svinjo Mountains, matching the visible article and linked place note.
- Added knownTo: [dufr], normalized the equivalent campaignInfo and existing header-marker codes to dufr, recorded a 1740s viewpoint and proposed name pronunciations, and normalized frontmatter.

### Validated judgments
- The local DM sources support the existing positive dm_notes attestation; their contents remain private.
- The SECRET block was reviewed; any useful recovery is confined to the private handoff.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `oo-MM-lee the EG-zyle` and the short form `oo-MM-lee`. The Stoneborn cultural context supplies the Xhosan analogue in [[Languages]]: u is read oo, i as ee, and m as a syllabic nasal before l, with length on that penultimate nasal beat; the epithet uses ordinary English pronunciation. The syllabic-nasal and penultimate-length treatment follows [Mncube’s Xhosa manual](https://emandulo.apc.uct.ac.za/collection/FHYA%20Depot/Mncube_F_S_M_Xhosa_Manual.pdf). Exact Stoneborn sound rules, tone and the complete name’s language are unestablished, so both entries remain proposed. Accept or replace them; on acceptance, mark them documented and copy the accepted primary pronunciation to frontmatter.

- [ ] **Warning — metadata.campaign_date_conflict:** The campaignInfo and displayed header record a meeting on December 29th, DR 1748. [[Session 81 (DuFr)]] places the first meeting on December 17th, and [[Session 82 (DuFr)]] places the return consultation on December 30th. No consulted session supports December 29th. If this entry is intended to record the first meeting, replace it with `{campaign: dufr, date: 1748-12-17, type: met}` and regenerate the corresponding header. If it denotes another meeting, identify its source before choosing a different date.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/In Game Notes]]
- [[_DM_/_Dunmari Frontier/Session 74-75 (Scepter)/Tollen DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Prep Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 77 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 78 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 79 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 80 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - DM Notes]]
%%^End%%
