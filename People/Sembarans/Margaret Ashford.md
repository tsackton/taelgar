---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, date: 1720-01-04, type: met}
born: 1676
gender: female
name: Margaret Ashford
whereabouts:
  - {type: home, location: Cleenseau}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720s
---
# Margaret Ashford
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:Clee%% Met by the [[Heroes of Cleenseau]] on January 4th, 1720 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

A midwife, who was tending to [[Beatrix Thorne|Béatrix Thorne]] when the [[Undead Attacks in Sembara]] broke out.

%%^Metadata:names:v1%%
- {"name": "Margaret Ashford", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s portrait of the Cleenseau midwife, illustrated by the January 1720 undead outbreak; no later change in her profession is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required knownTo, minimal name metadata, and supported POV/povNotes.
- Normalized the campaignInfo code Clee to clee using the campaign registry.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated interaction line uses `%%^Campaign:Clee%%`; use `%%^Campaign:clee%%` under the canonical campaign registry, keeping the same header content and end marker.
%%^End%%
