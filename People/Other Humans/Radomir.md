---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T23:46:56-04:00"
lintVersion: "3.4"
tags: [person, status/cleanup/text, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Urskan
campaignInfo: []
born: 1710
gender: male
name: Radomir
whereabouts:
  - {type: home, location: Ursk}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Radomir
>[!info]+ Biographical Info  
> An [[Ursk|Urskan]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A man from a strange place to the east.

## Safri's Tale 

Maybe 10 or 15 years ago she met a strange man, maybe 25 at the time, from somewhere faraway to the east. Ursk, he said, and he spoke halting Common with a strange accent. He said his name was Radomir. He had run a long way, across the empty plains of the kenku and over the mountains, fleeing home, he claimed. He carried with him a [[Jade Piece of Rai's Hand]] that he said he found in the far north, in the ice. The full tale is his to tell, not mine. But he also asked about destroying artifacts, for this [[Jade Piece of Rai's Hand]] he carried haunted his dreams.

%%^Metadata:names:v1%%
- {name: Radomir, role: primary, language: Urksan, pronunciation: ruh-duh-MEER, notes: "Russian analogue: final stress and reduction of the two unstressed o vowels toward uh.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 secondhand account of Radomir's earlier flight from Ursk and encounter with Safri; his later return and current circumstances are not yet incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` and the persistent name and temporal metadata.

### Editorial assessment
**Underdeveloped**. The visible note gives only Safri’s older secondhand account. It lacks the established later state central to Radomir’s reference entry: his return to Ursk, poor health and isolation, monitored surrender to the Rodnya Voknaz, his relationship with Yelena, and the later disposition of the jade.

### Validated judgments
- `status/cleanup/text` and `status/cleanup/metadata` remain supported by the central coverage gap and unresolved metadata; both were preserved unchanged.
- Matching local-only sources support the existing positive `dm_notes: important` attestation; their paths will be recorded mechanically without exposing their contents.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** `Scrying Delwath Nov 15`, `Scrying Delwath Tollen Downtime`, `Jade Piece of Rai's Hand`, and the Dunmar Frontier session record establish Radomir’s later circumstances, which are absent from the article. Candidate: add “By DR 1749, Radomir had returned to Ursk and was living alone near a snowy forest village, in poor health and under the watch of the Rodnya Voknaz following his surrender. The group had taken the jade from him, while his sister Yelena sometimes brought medicine; the Dunmar Fellowship later recovered the jade after defeating Rhodar von Glauer.”
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `Radomir — ruh-duh-MEER` from the Urksan Russian analogue, using final stress and reducing the two unstressed o vowels toward `uh`. Candidate: review the derivation, then add `pronunciation: ruh-duh-MEER` to frontmatter and mark the entry documented, or correct the proposal.


### DM evidence
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
%%^End%%
