---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, date: 1719-11-07, type: met}
born: 1677-05-18
gender: male
name: Vincent de Arban
affiliations:
  - {org: Garay Family, type: primary}
whereabouts:
  - {type: home, location: Embry}
  - {type: away, start: 1719-11-07, end: 1719-11-22, location: Cleenseau}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1719
---
# Vincent de Arban
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[Garay Family]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Met by the [[Heroes of Cleenseau]] on November 7th, 1719 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

Vincent de Arban is an agent of [[Susanne Garay]]. He visited [[Cleenseau]] to investigate [[Viepuck]] (when he was masquerading as [[Viepuck|Najeer Garay]]).  He was extremely interested in Viepuck's spider silk scheme, and may return to see how it is faring.

%%^Metadata:names:v1%%
- {"name": "Vincent de Arban", "language": "Sembaran", "pronunciation": "van-SAHN duh ar-BAHN", "status": "proposed", "notes": "The French strand of the Sembaran analogue in [[Languages]] gives Vincent nasal vowels with silent final t, de a reduced duh, and Arban a nasal final an; the written n in the respelling marks nasalization rather than a fully released n. Final-syllable phrase stress is used. This is proposed; English VIN-sent duh AR-ban is also plausible."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-DR 1719 account centered on Vincent’s November visit and possible return; the whereabouts end date conflicts with the campaign timeline.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter formatting; added supported name and temporal review blocks, `POV`, and `knownTo`.
- Normalized the campaignInfo code to `clee`.
- Normalized the existing campaign-block code from `%%^Campaign:Clee%%` to `%%^Campaign:clee%%` without adding or moving content.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — temporal.whereabouts_date_conflict:** The Cleenseau whereabouts entry ends on November 22, 1719, whereas [[Cleenseau Campaign - Timeline]] records Vincent’s departure on November 8. Confirm the actual departure; if the timeline is correct, use `{type: away, start: 1719-11-07, end: 1719-11-08, location: Cleenseau}`. The linter preserves both dates pending that decision.

- [ ] **Warning — metadata.names_unresolved_status:** The name-block pronunciation `van-SAHN duh ar-BAHN` is proposed. The French strand of the Sembaran analogue in [[Languages]] gives Vincent nasal vowels with silent final t, de a reduced duh, and Arban a nasal final an; the written n in the respelling marks nasalization rather than a fully released n. Final-syllable phrase stress is used. This is proposed; English VIN-sent duh AR-ban is also plausible. Confirm it or supply the accepted full pronunciation before copying it to frontmatter and marking the entry documented.
%%^End%%
