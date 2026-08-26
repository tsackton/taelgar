---
headerVersion: 2023.11.25
lintedAt: "2026-08-25T09:29:24-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-04-15, type: grave discovered}
born: 1719
gender: male
died: 1748-03-18
name: Alban
affiliations: [Society of the Open Scroll]
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1747-12-23, end: 1748-02-02, prefix: traveling in, location: Yeraad River Basin}
  - {type: away, start: 1748-02-02, end: 1748-03-13, prefix: traveling in, location: Dunmar}
  - {type: away, start: 1748-03-13, end: 9999, location: Stormcaller Tower}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1748
---
# Alban
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Grave discovered by the [[Dunmar Fellowship]] on April 15th, 1748 in [[Stormcaller Tower]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%

%% some minor canonical locations in late 1747 - mid 1748 not captured completely in whereabouts %%

An adventurer associated with the [[Society of the Open Scroll]]. 

%%^Campaign:dufr%%
Traveled with [[Dee Wildcloak]] and [[Dain Goldhammer]] to [[Stormcaller Tower]], where he was killed. 
## Chronology

```dataview
LIST WITHOUT ID events.text flatten file.lists as events where contains(events.text, this.file.name) and contains(events.text, "DR") sort events.DR
```
%%^End%%

%%SECRET[v2:01384ab01f6465be611f42aaa0639469]%%

%%^Metadata:names:v1%%
- {name: Alban, language: Chardonian, pronunciation: AHL-bahn, notes: "Proposed from Chardon's Latinate naming analogue: an open first vowel, broad second vowel, and first-syllable stress.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1747–1748 expedition account ending with Alban's death at Stormcaller Tower; his earlier life is not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the supported knownTo value for dufr and temporal-POV metadata.
- Added a proposed Chardonian pronunciation in persistent name metadata.

### Validated judgments
- Confirmed that current local DM evidence supports the positive dm_notes attestation.
- Reviewed the SECRET block; any useful recovery remains confined to the private handoff.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation AHL-bahn follows Chardon's Latinate analogue, with an open first vowel, broad second vowel, and first-syllable stress. Accept it by moving it to frontmatter and marking the entry documented, or replace it with the intended pronunciation.

### DM evidence
- [[_DM_/Timelines/Uncategorized Events]]
%%^End%%
