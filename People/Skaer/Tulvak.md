---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Skaer
campaignInfo:
  - {campaign: dufr, date: 1748-12-21, type: met}
born: 1719
gender: male
name: Tulvak
whereabouts:
  - {type: home, location: Pyhlla}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Tulvak
>[!info]+ Biographical Info  
> A [[Skaer]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on December 21st, 1748 in [[Pyhlla]], [[Skaerhem]] %%^End%%

![[tulvak.png|right|400]]Tulvak is a skilled sailor hailing from the island of [[Pyhlla]] in [[Skaerhem]], in the Western [[Green Sea]]. He has for many years served as the ferry captain guiding pilgrims to [[Vetta]], and knows the coast of [[Vetta]] like the back of his hand. 

%%^Date:1748%%
Tulvak was on [[Vetta]] when [[Urgall the Black]] attacked in DR 1748. He was the only survivor of that assault, and still questions whether it was fate, or luck, that he was outside pissing when the fireballs began to fly. He fled watching the longhouse burn with all the pilgrims inside, and still carries the trauma of that night. 
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Tulvak", "language": "unknown", "pronunciation": "TOOL-vahk", "status": "proposed", "notes": "Proposed from the Finnish option within the Skaegish Finnish-or-Norwegian analogue: initial stress, u as oo, a as ah, and hard final k. Norwegian-influenced u could differ; the actual name language and vowel values remain unconfirmed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Tulvak's established ferry service and coastal knowledge; the existing DR 1748 date block records the attack and its aftermath.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` and normalized the existing campaign codes in metadata and the block.
- Corrected the ordinal `21th` to `21st`.
- Added a proposed pronunciation and a 1740s viewpoint while preserving the existing dated passage; normalized frontmatter.

### Validated judgments
- [[Session 81 (DuFr)]] supports Tulvak’s ferry role, local knowledge, and escape; the existing date block preserves the attack’s later layer.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `TOOL-vahk`. [[Languages]] gives Skaegish Finnish or Norwegian analogues with Swedish influence. This proposal prefers the Finnish reading: first-syllable stress, `u` as oo, `a` as ah, and hard final k; a Norwegian-influenced u could be more central and rounded. The name’s actual source language is unconfirmed. If accepted, copy the proposal to frontmatter `pronunciation` and mark the entry documented.

### DM evidence
- [[_DM_/_Dunmari Frontier/NPCs/Ankka]]
%%^End%%
