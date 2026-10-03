---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T18:19:15-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
gender: male
name: Corrin Merriweather
pronunciation: KOR-in MERR-ee-weh-ther
affiliations:
  - {org: Merriweathers, type: primary}
whereabouts: Veltor
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Corrin Merriweather
*(KOR-in MERR-ee-weh-ther)*
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (he/him), of the [[Merriweathers]]  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[corrin-merriweather.png|left|200]]

Corrin Merriweather is a quiet halfling of the [[Merriweathers]] who, with his sister [[Primrose Merriweather]], owned a long-established tailor shop in [[Veltor]].

%%^Campaign:clee%%
The siblings helped the [[Heroes of Cleenseau]] shelter [[Sabine de Brune]] after her escape from [[Veltor Keep]].

Shortly before the [[Cleenseau - Session 28|trial of the Heroes of Cleenseau]], Corrin and Primrose left Veltor in a mysterious overnight departure, abandoning the shop their family had maintained for two centuries.
%%^End%%

%%^Metadata:names:v1%%
- {name: Corrin Merriweather, language: unknown, pronunciation: KOR-in MERR-ee-weh-ther, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 account of Corrin's Veltor shop and departure before the March trial; his later whereabouts are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `POV: 1720` and persistent temporal coverage notes.
- Normalized affiliation-list formatting without changing its values.

### Validated judgments
- The existing account includes the consequential departure; the later Merriweather caravan in [[The Merriweathers - Authored Turns]] names Quent, Tobin, and Tamsin and does not establish a destination for Corrin or Primrose.

### Open findings

- [ ] **Warning — correctness.internal_conflict:** The undated `whereabouts: Veltor` still presents Veltor as Corrin's current home, while the article records his departure and abandonment of the shop. [[Cleenseau - Session 27]] dates the first day to March 19, DR 1720; [[Cleenseau - Session 27 - Original]] reports that the siblings vanished during the following night. For a date-filtered correction, consider `whereabouts: [{type: home, location: Veltor, end: 1720-03-19}]`, using the last day before that overnight departure. Confirm that day-level boundary before applying it, since the narrative gives an overnight sequence rather than an explicit departure date. Do not add a new home or destination without evidence.
%%^End%%
