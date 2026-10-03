---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
gender: male
player: Isaac Sackton
campaignInfo:
  - {campaign: dufr, person: Riswynn, type: met, date: 1748-05-09}
name: Agnor
affiliations:
  - {org: "Oskar's Companions", title: One}
whereabouts:
  - {type: home, location: Tharn Todor}
knownTo: [dufr]
dm_owner: player
dm_notes: none
POV: 1740s
---
# Agnor
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Riswynn]] on May 9th, 1748 in [[Tharn Todor]], [[Nardith]], the [[Yuvanti Mountains]] %%^End%%

Agnor is a dwarven warlock from [[Tharn Todor]], who has occasionally adventured with [[Oskar]] and [[Riswynn]]. His magic is tied to mysterious ancient powers, and he is often accompanied by his familiar, Ravi.

%%  Great Old One warlock%%

%%^Metadata:names:v1%%
- {"name":"Agnor","language":"unknown","pronunciation":"AG-nor","status":"proposed","notes":"Proposed from the Dwarvish Tolkien Dwarvish analogue in Languages: short a, separately sounded g and n, rounded o, and first-syllable stress. Name-language and exact in-world phonology remain unestablished."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Agnor’s Tharn Todor base, adventuring relationships, and familiar in the DR 1740s, anchored by the DR 1748 encounter; no later changes are established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo: [dufr] from existing campaignInfo.
- Normalized campaignInfo and Campaign block code to dufr without changing scope.
- Added persistent name metadata with a proposed pronunciation.
- Recorded POV: 1740s and its DR 1748 anchor; normalized frontmatter.

### Validated judgments
- The hidden subclass label is DM mechanics and remains separate from the public description.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm proposed `AG-nor`. [[Languages]] gives Dwarvish the Tolkien Dwarvish analogue: short a, separately sounded g and n, rounded o, and initial stress for this two-syllable reading. This is a cultural analogue, not established in-world phonology or proof of the name’s language. Accept or correct it before marking the entry documented and copying the primary pronunciation to frontmatter.
%%^End%%
