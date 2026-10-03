---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: lizardfolk
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Kenzo, date: 1748-09-30, type: met}
  - {campaign: dufr, person: Kenzo, date: 1748-11-04, type: last seen}
born: null
activeYear: 1745
gender: female
name: Arrosa
whereabouts: Bedez
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Arrosa
>[!info]+ Biographical Info  
> A [[Lizardfolk|lizardfolk]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Kenzo]] on September 30th, 1748 in [[Bedez]], [[Orekatu]], the South Region %%^End%%  
>> %%^Campaign:dufr%% Last seen by [[Kenzo]] on November 4th, 1748 in [[Bedez]], [[Orekatu]], the South Region %%^End%%

A lizardfolk elder, the matriarch of the village of [[Bedez]], in the Kingdom of [[Orekatu]]. 

%%^Metadata:names:v1%%
- {name: "Arrosa", language: "unknown", pronunciation: "ah-RROH-sah", notes: "Proposal using the Basque analogue for Lizardling in [[Languages]]: open a vowels, pure o, trilled rr, and a voiceless s; penultimate stress is a provisional reading because no precise in-world stress rule or accepted pronunciation is recorded.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s portrait of Arrosa as the elder and matriarch of Bedez, anchored by the DR 1748 visit; the beginning and end of her tenure are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]`, consistent with the existing campaign interactions.
- Added a proposed name entry and late-1740s temporal metadata; normalized frontmatter formatting.

### Validated judgments
- [[Session 57 (DuFr)]] corroborates the village leadership role; a record of the conversation that revealed that role is unnecessary in this bounded reference note.
- The confirmed local subject evidence supports `dm_notes: color`; generic name lists were excluded.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed `ah-RROH-sah` in `Metadata:names:v1`. The Basque analogue for Lizardling in [[Languages]] motivates open a vowels, pure o, trilled rr, and voiceless s. Penultimate stress is provisional because no exact in-world stress rule is recorded; the specific name language remains unestablished. Accept it by setting `pronunciation: ah-RROH-sah` in frontmatter and changing the entry to `status: documented`, or supply the intended reading.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Prequel - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Session 1 - Kenzo]]
%%^End%%
