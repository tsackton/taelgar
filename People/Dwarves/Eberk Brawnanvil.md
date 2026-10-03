---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
born: 1502
gender: male
name: Eberk Brawnanvil
affiliations: [Brawnanvils]
whereabouts:
  - {type: home, end: 1544, location: "Raven's Hold"}
  - {type: home, start: 1547-01-01, end: "", location: Tharn Todor}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Eberk Brawnanvil
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% some color notes from Riswynn's backstory to copy %%

An elder [[Dwarves|dwarf]], a respected member of the Brawnanvil clan and priest of the [[Bahrazel]]. He was born in the [[Sentinel Range]] before the [[Great War]] and grew up in the [[Dwarven Outpost (Raven's Hold)|dwarven outpost]] near [[Raven's Hold]], but fled south during the [[Great War]]. He now lives with many other Brawnanvils in [[Tharn Todor]]. 

%%^Campaign:dufr%%
Eberk is [[Riswynn]]'s great uncle, who helped her develop her divine magic, and passed along a map of the [[Dwarven Outpost (Raven's Hold)|dwarven outpost near Raven's Hold]] to aid her in the quest to recover the [[Shield of the Brawnanvil Clan]]. 
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Eberk Brawnanvil", "language": "unknown", "pronunciation": "EH-berk BRAWN-an-vil", "status": "proposed", "notes": "Eberk appears in the [[Dwarves]] naming list; the [[Languages]] guidance uses Tolkien Dwarvish. Proposal uses short e vowels, an audible r and hard final k, with tentative initial stress; the clan surname follows its trade-tongue rendering. Exact name-specific phonology is unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Eberk as an elder in Tharn Todor and Riswynn’s mentor, with selected Great War backstory; it does not establish his state throughout the intervening centuries.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Recorded supported campaign knowledge in `knownTo`, the article’s temporal viewpoint in `POV`, and its coverage limits in `povNotes`.
- Added a primary name entry with a proposed pronunciation; retained `language: unknown` because the complete name’s language is not expressly attested.
- Converted the campaign block’s exact registry alias `DuFr` to `dufr`, preserving its audience.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `EH-berk BRAWN-an-vil` for Eberk Brawnanvil. Eberk appears in the [[Dwarves]] naming list; the [[Languages]] guidance uses Tolkien Dwarvish. Proposal uses short e vowels, an audible r and hard final k, with tentative initial stress; the clan surname follows its trade-tongue rendering. Exact name-specific phonology is unrecorded. Accept or revise this proposal in `Metadata:names:v1`; on acceptance, change its status to `documented` and copy the accepted primary pronunciation to frontmatter.

- [ ] **Warning — correctness.cross_note_conflict:** The target and [[Session 7 (DuFr)]] call Eberk Riswynn’s great uncle, while [[Dunmar Frontier - Session 06]] calls him her great-great-uncle. Both session records agree that he supplied her map; they do not establish one consistent kinship degree. Confirm the intended degree before changing it. If the exact degree is to remain open, a copy-ready neutral opening is: “Eberk is an elder relative of [[Riswynn]], who helped her develop her divine magic”. Preserve the existing map and quest information after that clause.

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The current `color` attestation may refer to Riswynn’s backstory, remembered information, or another off-vault source. Retain it unless a human confirms that no useful private information remains.
%%^End%%
