---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T18:19:15-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
gender: female
name: Primrose Merriweather
pronunciation: PRIM-rohz MERR-ee-weh-ther
affiliations:
  - {org: Merriweathers, type: primary}
whereabouts: Veltor
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Primrose Merriweather
*(PRIM-rohz MERR-ee-weh-ther)*
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Merriweathers]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[primrose-merriweather.png|left|200]]

Primrose Merriweather is a halfling of the [[Merriweathers]] who, with her brother [[Corrin Merriweather]], owned a long-established tailor shop in [[Veltor]].

%%^Campaign:clee%%
The siblings helped the [[Heroes of Cleenseau]] shelter [[Sabine de Brune]] after her escape from [[Veltor Keep]].

Shortly before the [[Cleenseau - Session 28|trial of the Heroes of Cleenseau]], Primrose and Corrin left Veltor in a mysterious overnight departure, abandoning the shop their family had maintained for two centuries.
%%^End%%

%%^Metadata:names:v1%%
- {name: Primrose Merriweather, language: unknown, pronunciation: PRIM-rohz MERR-ee-weh-ther, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720 account describes the Veltor tailor business and the siblings’ departure in March 1720; their whereabouts after leaving are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter collection formatting without changing its values.
- Added `POV: 1720` and temporal coverage metadata for the Cleenseau-era account.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — correctness.internal_conflict:** `whereabouts: Veltor` is an undated current home, but the article says Primrose and Corrin abandoned their shop and left Veltor. [[Cleenseau - Session 27]] places their last meeting on March 19, 1720 and reports their overnight disappearance the next morning; the preserved [[Cleenseau - Session 27 - Original]] records the same sequence. Decide whether the metadata should retain an explicitly earlier home snapshot or end the Veltor residence. A bounded candidate for the latter is `whereabouts: [{type: home, location: Veltor, end: 1720-03-19}]`, using the last documented day in town; confirm that boundary before applying it. Do not supply a later location without evidence.
%%^End%%
