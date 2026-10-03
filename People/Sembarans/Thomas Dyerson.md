---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
gender: male
name: Thomas Dyerson
affiliations:
  - {org: Barony of Aveil, title: Magistrate}
whereabouts:
  - {type: home, location: Veltor}
  - {type: away, location: Cranford, start: 1720-02-20, end: 1720-02-25}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720s
---
# Thomas Dyerson
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[thomas-dyerson.png|right|200]]One of three assistants to [[Victorine Rosseau]], Thomas is an important magistrate in the [[Barony of Aveil]] and often travels to investigate and adjudicate crimes on behalf of the Barony. He is dedicated to his job, if a bit uncreative, and willing to look beyond the obvious when pushed.

%%^Metadata:names:v1%%
- {"name": "Thomas Dyerson", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s portrait of the circuit magistrate; the dated Cranford stay has a start-date discrepancy requiring review.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required knownTo, minimal name metadata, and supported POV/povNotes.
- Recorded the existing filename identity explicitly as name.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The Cranford whereabouts entry begins `1720-02-20`, but [[Cleenseau - Session 17]] places Dyerson's arrival and investigation there on February 19. Preserve the existing entry pending reconciliation; if the session chronology controls, replace only its start with `start: 1720-02-19` and retain `end: 1720-02-25`.
%%^End%%
