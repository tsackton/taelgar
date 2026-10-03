---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, type: met}
born: 1694
gender: female
name: Marion
affiliations:
  - {org: Army Garrison of Cleenseau, title: Soldier}
whereabouts:
  - {type: home, location: Cleenseau}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720s
---
# Marion
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]], she/her
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A soldier of the Bridge Patrol.

%%^Date:1720%%
She was badly wounded during the events of the [[Cleenseau Spider Attacks]] and did not travel to [[Dunfry]] with the rest of the [[Army Garrison of Cleenseau]]. 
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Marion", "language": "Sembaran", "status": "inferred"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the Bridge Patrol identity belongs to the early Cleenseau campaign era; the existing date block records a wound sustained in October 1719 and the later missed deployment.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; added supported name and temporal review blocks, `POV`, and `knownTo`.
- Corrected the affiliation title typo “Solider” to “Soldier”.
- Corrected “A solider of the Bridge Patrol.” to “A soldier of the Bridge Patrol.”.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — temporal.date_block_scope:** The existing `Date:1720` block hides Marion’s wound until 1720, but [[Cleenseau - Session 02]] and its recap place the wounding on October 21, 1719; the missed Dunfry deployment occurred in November. Keep the later non-deployment clause separate if needed. Candidate for the injury alone: `%%^Date:1719-10-21%%` followed by “She was badly wounded during the Cleenseau Spider Attacks.” and the matching existing End marker. Changing filtered visibility needs human approval.
%%^End%%
