---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T09:29:24-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-07-02}
born: 1711
gender: female
name: Drusa
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1748-05-01, location: Tokra}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Drusa
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% add campaign info, reformat text to isolate campaign stuff, check and see if secrets still need to be secret%%

A Chardonian wizard on loan to the Dunmari army of [[Nayan Karnas]], commanded by [[Illyan]], in [[Tokra]]. 

Does not particularly like the party given their attempt to scry on [[Illyan]], which Drusa detected, and their refusal to agree to simple magic protocols. 

%%SECRET[v2:084aa9d4f8cdb1996fa86d69b5cf2e20]%%

%%^Metadata:names:v1%%
- {name: Drusa, role: primary, language: Chardonian, pronunciation: DROO-sah, status: proposed, notes: "Proposed from Chardon's more Latinate Chardonian analogue; classical Latin supports a hard s in DROO-sah, while Italian could voice it toward DROO-zah."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Drusa during her secondment to the Dunmari army in Tokra; her earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added a `dufr` campaign interaction for DR 1748-07-02 and `knownTo: [dufr]`.
- Added persistent Chardonian name metadata with the proposed pronunciation `DROO-sah`.
- Added `POV: 1748` and a temporal coverage note for Drusa's secondment in Tokra.

### Validated judgments
- Local-only evidence supports the existing `dm_notes: important` attestation.
- The SECRET block was reviewed for recovery and remains local-only.
- The existing `status/cleanup/metadata` remains supported while the primary name metadata awaits human resolution.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name entry remains `status: proposed`. Chardon's more Latinate Chardonian analogue favors classical Latin **DROO-sah**, with a hard s; an Italian reading could voice the intervocalic consonant toward **DROO-zah**. Accept one by copying it to frontmatter and changing the entry to `status: documented`, or replace the proposal with the preferred pronunciation.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
%%^End%%
