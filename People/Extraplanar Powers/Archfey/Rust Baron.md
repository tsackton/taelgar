---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [power, status/check/lint]
typeOf: archfey
gender: male
name: Rust Baron
affiliations:
  - {org: "Fate's Ruin", type: leader, title: Master}
whereabouts: "Fate's Ruin"
dm_owner: tim
dm_notes: none
POV: modern
---
# Rust Baron
>[!info]+ Information  
> An archfey (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Rust Baron, often called just the Baron, is the mysterious ruler of [[Fate's Ruin]], said to be able to age anything to dust with a single touch. 

%%SECRET[v2:87dec89ac5de96c9d4ee14615913bbba]%%

%%^Metadata:names:v1%%
- {"name": "Rust Baron", "language": "unknown", "notes": "A plain-English title; its original in-world language is not recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference prose about the ruler of Fate’s Ruin; the sources do not date his accession or the transformation of the realm.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added explicit display-name, primary-name, and temporal POV metadata.

### Validated judgments
- The title is plain English and needs no pronunciation guide.
- Reviewed the SECRET block; no settled recoverable addition was identified.

### Open findings

- [ ] **Suggestion — metadata.profile_mismatch:** The power profile in [[Note Categorization]] does not accept whereabouts, but this note has `whereabouts: Fate's Ruin` as well as the supported ruler affiliation. Consider removing that whereabouts field and its `_scripts/view/get_Whereabouts` header line while retaining `affiliations: [{org: Fate's Ruin, type: leader, title: Master}]`. This leaves the realm relationship represented through the supported power metadata; the rendering change is reserved for human approval.
%%^End%%
