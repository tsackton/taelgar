---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
displayDefaults: {endStatus: killed by spiders}
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, type: His body was found, date: 1719-10-22}
born: 1651
gender: male
died: 1719-10-14
name: Nicholas the Beggar
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: away, start: 1719-10-14, end: 1719-10-30, location: Cleenseau Wood}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: modern
---
# Nicholas the Beggar
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:clee%% His body was found by the [[Heroes of Cleenseau]] on October 22nd, 1719 in the [[Cleenseau Wood]], the [[Barony of Aveil]], [[Sembara]] %%^End%%

An old man with a thick grey beard, a beggar who lived in the ramshackle [[Beggar's Way]] outside of [[Cleenseau]]. His body was found in the [[Cleansing of the Ettercap Lair]] by [[Viepuck|Najeer]], [[Izgil Moonseeker|Izgil]], [[Robin of Abenfyrd|Robin]], and [[Celyn]]. He was believed to have been killed by spiders on or around October 14th.

%%^Metadata:names:v1%%
- {"name": "Nicholas the Beggar", "language": "Sembaran", "status": "inferred"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a retrospective account of Nicholas and his death in October 1719; the recovery date remains a source discrepancy.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; added supported name and temporal review blocks, `POV`, and `knownTo`.
- Corrected “killed by spider's” to “killed by spiders”.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — temporal.recovery_date_conflict:** The campaignInfo and generated header say Nicholas’s body was found on October 22, 1719. [[Cleenseau - Session 02]] places the lair expedition on October 21 and the return with recovered dead on October 22. Confirm whether the current date describes discovery or return before changing it. If discovery was on the expedition date, the candidate field is `date: 1719-10-21`; otherwise preserve October 22 and clarify what it records. The approximate October 14 death remains separate.
%%^End%%
