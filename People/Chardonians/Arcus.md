---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T23:46:56-04:00"
lintVersion: "3.4"
displayDefaults: {endStatus: petrified}
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Chardonian
campaignInfo:
  - {campaign: dufr, date: 1748-03-25, type: discovered as a statue}
born: 1723
gender: male
died: 1748-03-15
name: Arcus
affiliations: [Society of the Open Scroll]
whereabouts:
  - {type: home, location: Chardon}
  - {type: away, start: 1747-12-23, end: 1748-02-02, prefix: traveling in, location: Yeraad River Basin}
  - {type: away, start: 1748-02-02, end: 1748-03-03, prefix: traveling in, location: Dunmar}
  - {type: away, start: 1748-03-03, end: 1748-03-05, location: Karawa}
  - {type: away, start: 1748-03-14, end: 9999, location: Dunmari Fort (Gomat)}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1748
---
# Arcus
>[!info]+ Biographical Info
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (he/him)
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Discovered as a statue with the [[Dunmar Fellowship]] on March 25th, 1748 in the [[Dunmari Fort (Gomat)]] %%^End%%

%% some canonical travel not captured in whereabouts yet %%

An adventurer and treasure hunter from the [[Society of the Open Scroll]], now petrified in the fort east of [[Gomat]]. 

%%^Campaign:dufr%%
Left [[Chardon]] with [[Servius]], [[Dee Wildcloak]], [[Dain Goldhammer]], and [[Alban]]. Argued constantly with [[Servius]], acording to [[Dee Wildcloak]]. Parted ways with other travelers in [[Songara]], presumably to press ahead. 

Passed through [[Karawa]] alone in late February or early March, according to [[Jasu]] and [[Ikram]].

## Chronology

```dataview
LIST WITHOUT ID events.text flatten file.lists as events where contains(events.text, this.file.name) and contains(events.text, "DR") sort events.DR
```
%%^End%%


%%SECRET[v2:68301e3aaee1fb07af463b7a11db1511]%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account of Arcus's final expedition and petrified state; his earlier life is not described beyond his departure from Chardon.
%%^End%%

%%^Metadata:names:v1%%
- {name: Arcus, language: Chardonian, pronunciation: AR-koos, notes: proposed from the documented Chardonian Latin analogue; c before u is hard and the first syllable is stressed, status: proposed}
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied automatically
- Added `knownTo: [dufr]` from the existing Dunmar Frontier interaction record.
- Added `POV: 1748` and a persistent temporal note describing the article as an account of Arcus's final expedition and petrified state.
- Added a persistent primary-name entry with a proposed Chardonian pronunciation.

### Validated judgments
- The visible article is sufficient for Arcus's role as a minor expedition and campaign connector: it identifies his profession, affiliation, companions, route, and fate.
- `status/cleanup/metadata` is supported by the existing editorial reminder and unresolved precision in the dated travel metadata; the tag is preserved for human review.
- `dm_notes: none` is retained. Matching local-only sources do not by themselves change the human attestation.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `AR-koos` uses the documented Chardonian Latin analogue: `c` before `u` is hard, and the first syllable is stressed. Confirm or replace it.
  - Copy-ready acceptance if correct: add `pronunciation: AR-koos` to frontmatter and change the Arcus name entry to `status: documented`.

### DM evidence
- [[_DM_/Staging/NPC Ideas - Unused]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Chardon (Session 48-49)/Finding Artifacts in Chardon/Hralgar's Eyes (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Clues in Karawa]]
%%^End%%
