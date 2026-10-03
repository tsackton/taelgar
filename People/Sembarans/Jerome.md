---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: executed for his crimes}
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, type: captured, date: 1719-11-03}
gender: male
born: 1681
died: 1719-11-09
name: Jerome
whereabouts:
  - {type: away, location: Cleenseau, linkText: at, alias: bandit lair upriver of Cleenseau, start: 1719-10-01, end: 1719-11-03}
  - {type: away, location: Cleenseau, start: 1719-11-04, end: 1719-11-09}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: modern
---
# Jerome
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Captured by the [[Heroes of Cleenseau]] on November 3rd, 1719 at the [[Cleenseau|bandit lair upriver of Cleenseau]], in the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

A professional outlaw and bandit involved in the [[Attempted Poisoning of Cleenseau]]. He was caught by the [[Heroes of Cleenseau]] and executed under sentence from [[Nicholas Wysson]].

%%^Metadata:names:v1%%
- {"name": "Jerome", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective account of the bandit's fate in DR 1719; the exact execution date conflicts between this note and the campaign record.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required knownTo, minimal name metadata, and supported POV/povNotes.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The `died` field and final whereabouts end on `1719-11-09`, but [[Cleenseau Campaign - Timeline]] records the execution on November 6, and the [[Cleenseau - Session 04]] recap agrees. Reconcile the date before changing either source. If the campaign date is retained, use `died: 1719-11-06` and end the final Cleenseau stay on `1719-11-06`. The conflicting values are preserved for review.
%%^End%%
