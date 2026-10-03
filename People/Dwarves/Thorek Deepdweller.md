---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
born: 1515
gender: male
campaignInfo:
  - {campaign: grli, person: Mabist, type: met, date: 1748-10-02}
name: Thorek Deepdweller
affiliations:
  - {org: Deepdwellers, type: primary}
whereabouts:
  - {type: home, location: Castrella, alias: outside Castrella, format: "<name:x>"}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Thorek Deepdweller
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of the [[Deepdwellers]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by [[Mabist]] on October 2nd, 1748 [[Castrella|outside Castrella]], in [[Cedrano]], the [[Chardonian Empire]] %%^End%%

Thorek Deepdweller is an elderly dwarven hermit living outside [[Castrella]], devoted to the memory of lost [[Enderra]]. Gruff and sorrowful, he preserves old dwarven lore of the [[War of the Dark Rift]] and the old customs and tales of [[Enderra]].

%%^Metadata:names:v1%%
- {"name": "Thorek Deepdweller", "language": "unknown", "pronunciation": "THOR-ek DEEP-dwel-er", "notes": "Using the Tolkien Dwarvish analogue in Languages as broad guidance: voiceless th, sounded r, an open o and short e, with initial stress; the translated clan name uses ordinary English. Exact in-world phonology is unconfirmed.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Thorek as an elderly hermit outside Castrella in the late 1740s, anchored by the DR 1748 meeting; the beginning and end of his residence are unknown.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported `knownTo`, a subject-name block, and article `POV`/`povNotes`; normalized frontmatter.
- Normalized the equivalent campaign alias `GL` to `grli` in `campaignInfo` and the existing header block.

### Validated judgments
- [[Great Library Session Notes - Arc 5]] corroborates the elderly hermit and his Enderra lore; the compact reference account is sufficient.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciation `THOR-ek DEEP-dwel-er` in `Metadata:names:v1`. Using the Tolkien Dwarvish analogue in [[Languages]] as broad guidance, the proposal uses voiceless th, a sounded r, open o, short e and initial stress; the translated clan name uses ordinary English. This is an analogue-informed proposal, not an adopted in-world rule. If accepted, copy `pronunciation: THOR-ek DEEP-dwel-er` to frontmatter and change the entry to `status: documented`; otherwise amend the proposal.
%%^End%%
