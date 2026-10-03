---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
gender: male
died: 1748-03-14
name: Brottor
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, end: 1748-03-14, location: Goldpeak Mines}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: modern
---
# Brottor
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Brottor was a dwarven adventurer based in Chardon, and companion of [[Alton]] and [[Cassia]]. He died in the  [[Goldpeak Mines]] after falling under the aberrant influence of the beholder [[Vilaxes]]. 

%% Game Update
Part of another Great Library treasure-seeking party, with Alton and Cassia. 
He was the dwarf-looking creature at the abandoned camp that dissolved into gibbering mouthers during the Beholder arc of the Great Library campaign. 
%%

%%^Metadata:names:v1%%
- {"name": "Brottor", "language": "unknown", "pronunciation": "BROT-tor", "notes": "Proposed from the dwarven name list in [[Playing a Dwarf]] and the Tolkien Dwarvish analogue in [[Languages]]: rounded o vowels, an audible doubled t, and tapped r; first-syllable stress is a practical proposal, not established in-world phonology.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective account of Brottor’s adventuring companions and fate in the Goldpeak Mines in spring DR 1748; it does not describe a living present-day state.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo from recorded campaign interactions, a minimal name block, and temporal metadata.
- Normalized frontmatter while preserving its values.

### Validated judgments
- The concise role, companions, and fate perform this minor reference note’s role. The source chronology dates the aberrant encounter after the recorded death; it does not establish that Brottor was still alive then, so no death-date correction is inferred.

### Open findings

- [ ] **Suggestion — editorial.public_material_candidate:** The shared `Game Update` comment preserves a developed expedition association and transformation account beyond the visible summary of Brottor’s death. Consider adding: “Brottor’s expedition sought treasure for the [[Great Library]]. After his corruption, a dwarf-shaped creature identified as Brottor dissolved into a pair of gibbering mouthers at the abandoned camp outside the [[Goldpeak Mines]].” The transformation is established by [[Great Library Session Notes - Arc 4#Session 58]]; the Great Library association remains a human adoption decision from the comment. The addition would clarify his expedition’s purpose and the form his corruption took. If adopted, retire only the corresponding duplicated comment text.

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `BROT-tor` in `Metadata:names:v1`. Proposed from the dwarven name list in [[Playing a Dwarf]] and the Tolkien Dwarvish analogue in [[Languages]]: rounded o vowels, an audible doubled t, and tapped r; first-syllable stress is a practical proposal, not established in-world phonology. If accepted, copy it to frontmatter `pronunciation` and mark the entry `documented`; otherwise revise the proposal. The name’s source language remains `unknown`.
%%^End%%
