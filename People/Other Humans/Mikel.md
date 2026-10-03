---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
gender: male
born: 1733
name: Mikel
whereabouts:
  - {type: home, location: Suwi}
  - {type: away, start: 1748-08-23, location: Lake Suwi}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1748
---
# Mikel
>[!info]+ Biographical Info  
> A [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Mikel, the brother of [[Clara|Clara of Suwi]], was kidnapped by the [[Havoc Host]] during the [[Great Library Session Notes - Arc 4|Havoc Host raids in Suwi]]. Though the [[Silver Tempests]] destroyed the [[Aboleths|aboleth]] behind the Havoc Host attacks, Mikel's later fate is not recorded.

%%^Metadata:names:v1%%
- {"name": "Mikel", "language": "unknown", "pronunciation": "MEE-kel", "notes": "Cautious spelling-based proposal: initial m, first-syllable ee, hard k, unstressed el, and initial stress; no name-specific language or accepted pronunciation is recorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account of the kidnapping and its aftermath; later fate and whereabouts remain unknown.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the persistent name entry and temporal viewpoint metadata.
- Added knownTo: [grli] from the recorded investigation in Great Library Arc 4.

### Validated judgments
- The bounded account preserves the lack of a recorded later fate; it does not imply that killing the aboleth rescued Mikel.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed pronunciation `MEE-kel` in the name block. No name-specific language or accepted pronunciation was found; the cautious spelling reading uses initial stress, ee, hard k, and an unstressed final el. Accept or replace the proposal before copying it to frontmatter.
- [ ] **Warning — metadata.whereabouts_uncertain:** The open-ended Lake Suwi `away` entry begins on 1748-08-23, but [[Great Library Session Notes - Arc 4]] says on that day that the kidnapping happened a few days earlier, and records no later location for Mikel. The current header can therefore imply an ongoing location unsupported by the record. Confirm the intended dates and current-location display; a supported replacement description is: "His last reported location was a logging camp near [[Lake Suwi]], from which he was taken shortly before DR 1748-08-23; his subsequent whereabouts are unknown." Do not invent exact whereabouts bounds.
%%^End%%
