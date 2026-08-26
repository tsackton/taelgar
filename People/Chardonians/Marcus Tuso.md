---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T23:14:40-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: human
ancestry: Chardonian
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: 1747-09-28}
name: Marcus Tuso
affiliations:
  - {org: Voltara Guard, title: Commander}
whereabouts:
  - {type: home, location: Voltara}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1747
---
# Marcus Tuso
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on September 28th, 1747 in [[Voltara]], [[Greater Voltara]], the [[Northern Provinces]] %%^End%%

Marcus Tuso is the local commander of the Voltara Guard. 

%%^Metadata:names:v1%%
- {name: Marcus Tuso, language: Chardonian, pronunciation: MAR-koos TOO-soh, notes: "Proposed from Chardon's more Latinate Chardonian analogue: Latin-style hard c and final us in Marcus, with a hard s in Tuso; Italian-influenced speech could voice the surname s toward TOO-zoh. Exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747 snapshot of Marcus during the defense of Voltara; his later service is not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added `knownTo: [grli]` and normalized the Great Library code in `campaignInfo` and the campaign header block.
- Added persistent `Metadata:names:v1` metadata with a Chardonian language assignment and an analogue-derived pronunciation proposal.
- Added `POV: 1747` and a `povNotes:v1` block identifying the article as a DR 1747 snapshot.

### Validated judgments
- `Voltara Guard` is valid descriptive affiliation text even though it does not resolve to a note.
- `status/gameupdate/gl` is not assessable from the established evidence reviewed and was preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new `Metadata:names:v1` entry proposes `MAR-koos TOO-soh` from Chardon's more Latinate Chardonian analogue: Latin-style hard *c* and final *us* in Marcus, with a hard *s* in Tuso. Italian-influenced speech could voice the surname *s* toward `TOO-zoh`, and exact in-world phonology is not established. If the proposal is accepted, add `pronunciation: MAR-koos TOO-soh` to frontmatter and change the entry to `status: documented`; otherwise revise the pronunciation and derivation note.
%%^End%%
