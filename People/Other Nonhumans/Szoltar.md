---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: hobgoblin
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1749-08-06, type: met}
born: null
gender: male
name: Szoltár
aliases: [Szoltár]
pronunciation: SOHL-tahr
whereabouts:
  - {type: away, end: 1749-08-06, location: Plaguelands}
  - {type: away, start: 1749-08-07, end: 9999, location: Mirror of Soul Trapping}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1749
---
# Szoltár
*(SOHL-tahr)*
>[!info]+ Biographical Info  
> A [[Hobgoblins|hobgoblin]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on August 6th, 1749 in the [[Plaguelands]] %%^End%%

![[szoltar.png|right|400]]A captured soldier in the army of the [[Empress of Chaos]].

%%^Metadata:names:v1%%
- {"name": "Szoltár", "language": "unknown", "pronunciation": "SOHL-tahr", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 snapshot of his capture and confinement; his earlier life and later fate are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the objective typo `solider` to `soldier`.
- Normalized equivalent `DuFr` campaign values to `dufr`, added `knownTo: [dufr]`, and normalized frontmatter.
- Recorded the accepted pronunciation in a documented name entry and added temporal metadata.

### Validated judgments
- The minimal captive-soldier description and existing confinement metadata perform this minor character’s reference role.
- Confirmed local DM sources support the positive attestation; their contents remain private.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The meeting metadata and generated meeting line say DR 1749-08-06, and the Plaguelands whereabouts ends that day. [[Session 129 (DuFr)]] explicitly dates his capture and interrogation to DR 1749-08-07; [[Session 130 (DuFr)]] continues the interrogation that day. Confirm the chronology before changing it. If the session timeline is adopted, use `{campaign: dufr, date: 1749-08-07, type: met}`, change the generated meeting date to `August 7th, 1749`, and review the first whereabouts bound as `{type: away, end: 1749-08-07, location: Plaguelands}` while retaining the recorded mirror confinement from August 7. The conflicting dates have been preserved for that decision.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Notes - Session 129]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Session 130 - DM Notes]]
%%^End%%
