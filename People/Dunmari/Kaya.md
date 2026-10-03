---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, date: 1748-06-05, type: "[[Session 31 (DuFr)|Freed]] from living wood", format: "<met:x> <person:q> on <target> <current:3Frq>"}
gender: female
name: Kaya
whereabouts:
  - {type: away, start: 1748-06-05, location: Bas Udda}
  - {type: away, start: 1748-06-08, end: 9999, location: Karawa}
knownTo: [dufr]
excludePublish: [clee]
dm_owner: tim
dm_notes: important
POV: "1748"
---
# Kaya
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% [[Session 31 (DuFr)|Freed]] from living wood by the [[Dunmar Fellowship]] on June 5th, 1748 in [[Bas Udda]], [[Eastern Dunmar]], [[Dunmar]] %%^End%%

A young Dunmari woman, trapped for many, many years as [[Agata]]'s chair. 

%%SECRET[v2:0c2fd28e5d08d2ef5948ea47a8237c92]%%

%%^Metadata:names:v1%%
- {name: Kaya, language: unknown, pronunciation: KAA-yaa, notes: "Proposed from the Hindi option in the Dunmari naming guidance in [[Languages]]: k as in kite, open ah vowels and consonantal y; the guide emphasizes the first syllable. The name language and in-world stress are unconfirmed.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Kaya at her release from living wood in June, after prolonged captivity; later recovery and life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added `knownTo: [dufr]`, a persistent name entry, `POV: 1748`, and temporal notes.
- Converted the `DuFr` campaign alias to `dufr` in the interaction metadata and matching header block, preserving the campaign scope.

### Validated judgments
- The dated release header agrees with [[Session 31 (DuFr)]]: the living-wood prisoners were freed at Bas Udda on June 5, 1748. That source distinguishes the June 8 mirror releases; the June 8 date in [[Agata]] does not warrant changing this note.
- Confirmed local sources support the positive `dm_notes` attestation; the in-note SECRET block was reviewed separately.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or replace the persistent proposal `KAA-yaa`. [[Languages]] gives Dunmari the analogue “Hindi or other Indo-Iranian (Persian)”; this proposal uses the Hindi option for a hard k, open ah vowels, and consonantal y. Initial emphasis is a reading aid, not an adopted stress rule. The name’s actual language and vowel lengths are unconfirmed. If accepted, copy `pronunciation: KAA-yaa` to frontmatter and mark the matching name entry `status: documented`.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 29]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 30/Agata's Lair, Revised]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%
