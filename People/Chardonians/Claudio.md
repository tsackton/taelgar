---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T09:29:24-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, type: mentioned to, date: 1749-01-08, wParty: "<met:U> <person> on <target>"}
born: 1719
gender: male
name: Claudio
whereabouts:
  - {type: home, start: "", end: "", location: Luminatia}
  - {type: away, start: 1748-03-11, end: "", location: ""}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1749
---
# Claudio
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Mentioned to the [[Dunmar Fellowship]] on January 8th, 1749 %%^End%%

%% another "know about by rumor only" person to tag somehow %%

Claudio is a Chardonian man, from the village of [[Luminatia]] near [[Lake Valandros]]. He is [[Lucius]]'s father, but does not currently live with his family.

%%^Metadata:names:v1%%
- {name: Claudio, language: Chardonian, pronunciation: KLOW-dee-oh, notes: "Proposed from the ordinary Italian form under the Chardonian analogue, with an initial cl cluster and au diphthong; exact in-world phonology is not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 snapshot after Claudio left Luminatia; his destination and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [dufr]` and canonicalized the Dunmar Frontier campaign code in `campaignInfo` and the campaign block.
- Added persistent Chardonian name metadata with the proposed pronunciation `KLOW-dee-oh`.
- Added `POV: 1749` and a persistent temporal-coverage note.
- Corrected `Claudio in a Chardonian man` to `Claudio is a Chardonian man`.

### Validated judgments
- The two local-only name matches are not evidence about this Claudio: one is a generic name list, and the other campaign transcript explicitly identifies its servant Claudio as a different person.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed` because no accepted pronunciation is recorded. Review the ordinary Italian-form proposal `KLOW-dee-oh` under the Chardonian analogue; if accepted, mark the entry `documented` and copy the pronunciation to frontmatter, or revise it and record the chosen basis.
%%^End%%
