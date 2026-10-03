---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
campaignInfo:
  - {campaign: dufr, person: Riswynn, date: 1748-08-09, type: met}
gender: female
name: Finellen Silverstone
affiliations:
  - {type: primary, org: Silverstones}
whereabouts: Darba
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Finellen Silverstone
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (she/her), of Silverstones  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Riswynn]] on August 9th, 1748 in [[Darba]], [[Dunmar]] %%^End%%

A dwarven antiquities dealer in [[Darba]].

%%^Metadata:names:v1%%
- {name: Finellen Silverstone, language: unknown, pronunciation: fin-ELL-en SIL-ver-stohn, notes: 'Proposed from the Finellen naming example in [[Playing a Dwarf]] and the Tolkien Dwarvish analogue in [[Languages]]; short i, clear e vowels, sounded l and n, and a practical middle-syllable stress, with the ordinary English surname.', status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 occupational and residence snapshot, anchored by Riswynn’s August meeting in Darba; earlier and later activity are not established here.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added supported `knownTo: [dufr]`, a proposed pronunciation in a minimal name block, and temporal metadata.
- Normalized frontmatter while preserving its values.

### Validated judgments
- [[Session 46 (DuFr)]] corroborates her occupation and Darba setting. This one-sentence entry is sufficient for a minor professional contact.
- A genuine local source supports the existing positive `dm_notes` attestation; the attestation is unchanged.

### Open findings

- [ ] **Warning — relationship.unresolved:** The primary affiliation `Silverstones` has no resolving note or documented alternative in the searched clan and person records. Confirm that it is the intended clan. If so, create a minimal `Silverstones` reference identifying Finellen’s membership; otherwise replace the affiliation only with the confirmed existing clan name. Do not infer a different clan from a similar surname.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `fin-ELL-en SIL-ver-stohn` in `Metadata:names:v1`. [[Playing a Dwarf]] supplies Finellen as a dwarven name, and [[Languages]] gives Tolkien Dwarvish as broad analogue guidance: the proposal keeps short i, clear e vowels, and audible l and n; middle-syllable stress is a practical reading, not established in-world phonology. The surname uses ordinary English. If accepted, copy this pronunciation to frontmatter and mark the name entry `documented`; otherwise revise it. The name’s in-world source language remains unknown.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Darba/Darba (OneNote)]]
%%^End%%
