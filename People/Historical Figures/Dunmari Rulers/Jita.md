---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
born: 1386
gender: female
title: Samraat
died: 1460
name: Dharajun Jita
aliases: [Samraat Jita]
affiliations:
  - {org: Dharajun Dynasty, type: primary}
  - {org: Dunmar, start: 1402, type: leader}
whereabouts:
  - {type: home, location: plains of Songara}
  - {type: home, location: Tokra}
knownTo: []
dm_owner: tim
dm_notes: color
POV: modern
---
# Samraat Dharajun Jita
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her), of the [[Dharajun Dynasty|Dharajun dynasty]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The founding ruler and Samraat of the Dharajun dynasty, associated with [[Chidya]] and often called the dynasty of the horse. 

Jita was born in the empty plains of northwestern Dunmar, near current-day [[Songara]]. In DR 1402, at just 16, she won several decisive victories against Thundering Axe Horde, driving them across the Mahar. Soon after she was proclaimed Samraat, founding a new dynasty under the protection of Chidya. 

Her primary court was based in Tokra, which grew dramatically during the 57 years of her rule.

%%^Metadata:names:v1%%
- {"name": "Dharajun Jita", "language": "unknown", "pronunciation": "dhuh-RAH-jun JEE-tah", "notes": "The Dunmari cultural context uses the Hindi or Persian analogue in [[Languages]]. This proposal favors Hindi: dh is a breathy voiced d, j is as in judge, i is read ee, and a is rendered ah or an unstressed uh. The preferred stress and vowel lengths are tentative; a Persian adaptation would normally lose the dh aspiration.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: modern retrospective account of Jita’s birth, victories, founding rule, and Tokra court in the DR 1400s; the accession date needs reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the primary name entry and the article’s POV and temporal-coverage note.
- Recorded supported campaign knowledge in `knownTo` (an empty list where no campaign knowledge is established).

### Validated judgments
- The positive `dm_notes: color` attestation has matching local sources; its value is retained.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The Dunmar leadership affiliation starts in DR 1402, whereas [[Dunmar#Dharajun Dynasty]] dates the dynasty’s foundation to DR 1403. The prose separates her DR 1402 victories from a proclamation soon afterward, and its 57-year reign ending in DR 1460 also fits DR 1403. Confirm the accession date; if the dynasty chronology is intended, use `{org: Dunmar, start: 1403, type: leader}` while retaining the DR 1402 victories.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `dhuh-RAH-jun JEE-tah`. The Dunmari cultural context uses the Hindi or Persian analogue in [[Languages]]. This proposal favors Hindi: dh is a breathy voiced d, j is as in judge, i is read ee, and a is rendered ah or an unstressed uh. The preferred stress and vowel lengths are tentative; a Persian adaptation would normally lose the dh aspiration. Confirm or revise the pronunciation, then mark the entry documented and copy the accepted primary pronunciation to frontmatter.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
%%^End%%
