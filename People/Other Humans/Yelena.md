---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T16:58:26-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Urskan
gender: female
name: Yelena
affiliations: [Rodnya Voknaz]
whereabouts: Ursk
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1749
---
# Yelena
>[!info]+ Biographical Info  
> An [[Ursk|Urskan]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The sister of [[Radomir]]. 

%%SECRET[v2:9d6e654a90f7801b39d540bd2a95acea]%%

%%^Metadata:names:v1%%
- {"name":"Yelena","language":"Urksan","notes":"The Urskan context and Russian-form ordinary given name support this language attribution; the familiar name does not require a pronunciation guide."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 reference to Radomir’s sister and her Rodnya Voknaz membership; earlier and later affiliations are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added explicit identity, `knownTo: [dufr]`, a DR 1749 temporal frame, and a minimal name block; normalized frontmatter formatting.

### Validated judgments
- [[Interlude (Tollen Downtime)]] confirms the sibling relationship and Rodnya Voknaz membership. The ordinary given name does not require a pronunciation guide. The SECRET block was reviewed and remains private.

### Open findings

- [ ] **Suggestion — dm.notes_no_local_evidence:** No confirmed matching `_DM_` notes were found to support `dm_notes: color`; the mechanical first-name matches do not establish this person’s identity. Verify the human attestation: retain `color` if useful information remains off-vault or in memory, or set `dm_notes: none` if it is all captured. The linter has preserved the current value.
%%^End%%
