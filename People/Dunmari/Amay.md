---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, type: met, date: 1748-07-02}
born: null
gender: male
name: Amay
whereabouts:
  - {type: away, start: 1748-06-03, end: 1748-12-14, linkText: camped near, location: Tokra, format: "<name:q>"}
knownTo: [dufr]
dm_owner: none
dm_notes: important
POV: 1748
---
# Amay
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on July 2nd, 1748 in [[Tokra]], [[Dunmar]] %%^End%%

A captain in the Dunmari army, in service of [[Illyan]] and ultimately the Samraat [[Nayan Karnas]]. 

%%^Date:1748%%
## Chronology
- (DR:: 1748-06-03): Arrives in Tokra with the first wave of [[Nayan Karnas]]'s army, under the command of [[Illyan]]. 
- (DR:: 1748-07-02): Briefly encounters [[Dunmar Fellowship]] in Tokra while escorting them to [[Illyan]]'s camp. 

%%^End%%

%%SECRET[v2:fec1d7f066508f696dd103e553b12647]%%

%%^Metadata:names:v1%%
- {name: Amay, language: unknown, pronunciation: uh-MAY, notes: "Proposed using the Hindi option in the Dunmari analogue in [[Languages]]: reduced initial a, ordinary m, and a final ay glide; the stress and vowel approximation remain uncertain, and the name language is not separately established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Amay as a captain serving Illyan; the chronology describes June–July 1748 and does not establish a later role.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]` from the recorded campaign encounter.
- Added persistent name metadata with a proposed pronunciation and a DR 1748 temporal viewpoint.

### Validated judgments
- The brief captain-and-command reference is proportionate to Amay’s role in [[Session 36 (DuFr)]].
- Confirmed local-only matches support the existing positive `dm_notes` attestation. The SECRET block was reviewed and retained.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `uh-MAY` for Amay. The proposal uses the Hindi option in the Dunmari analogue in [[Languages]]: reduced initial a, ordinary m, and a final ay glide. Stress and vowel approximation remain uncertain; no source separately establishes the name’s language. Accept by adding `pronunciation: uh-MAY` to frontmatter and changing the name entry to `status: documented`, or replace the proposal with the intended pronunciation.

### DM evidence
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
%%^End%%
