---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/gameupdate/gl, status/check/lint]
species: elf
gender: male
ka: 37
born: 1645
name: Aelar
affiliations:
  - {org: Silver Tempests, end: 1748-05-01}
whereabouts:
  - {type: home, end: 1747-01-01, location: Chardon}
  - {type: home, start: 1747-04-08, end: 1747-10-06, location: Voltara}
  - {type: home, start: 1747-10-06, end: 1748-05-01, location: Tempest Towers}
knownTo: [grli]
dm_owner: tim
dm_notes: none
POV: 1748
---
# Aelar
>[!info]+ Biographical Info  
> An [[Elves|elf]] (he/him), ([[Elven Cycle of Generations|ka]] 37)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Aelar is an elf and a monk, from the first generation of elves born after the [[Great War]]. Always something of a loner, he spent much of his early life on the streets of [[Chardon]], a bit of an outcast, learning to survive and fight while mourning in his own way the massive destruction of elven society during and after the [[Great War]]. 

Eventually, he found his way to the [[Great Library]], where he was recruited to help search for lost artifacts and treasures from before the [[Great War]] in the [[Northern Provinces]] of the [[Chardonian Empire]]. In the city of [[Voltara]], he met [[Adrik]], [[Aglath]], [[Brelith]], and [[Samso]], and became one of the original members of the [[Silver Tempests]].

After the [[Silver Tempests]] defeated the beholder [[Vilaxes]], Aelar departed Voltara, and his current whereabouts are unknown.

%%^Metadata:names:v1%%
- {name: Aelar, language: unknown, pronunciation: EYE-lahr, notes: "Proposed Elvish-style reading of the spelling using the guidance in [[Languages#Elvish]]; the name's language and accepted pronunciation are not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account after Aelar departed Voltara following Vilaxes's defeat, with earlier Chardon backstory; his subsequent whereabouts are unknown.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added `knownTo: [grli]` from Aelar's membership in the Silver Tempests and the Great Library campaign records.
- Added primary name metadata with a proposed pronunciation; left the name's language unknown.
- Added `POV: 1748` and temporal coverage metadata for the existing account after his departure from Voltara.

### Validated judgments
- `status/gameupdate/gl`: not assessable. The reviewed campaign records and [[Silver Tempests]] do not establish a later whereabouts or role that supersedes the departure account, but the tag may reflect an intended update not captured there; preserved for human disposition.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `EYE-lahr` for Aelar. The best available naming guidance is the Tolkien Elvish analogue in [[Languages#Elvish]], used here as a tentative Elvish-style reading rather than evidence for the name's language: `ae` is read as one eye-like diphthong, the second `a` as open ah, with clear `l` and `r` and stress on the first of two syllables. No accepted pronunciation is recorded in the reviewed sources. Confirm or replace the proposal; if accepted, add `pronunciation: EYE-lahr` to frontmatter and change the name entry to `status: documented`.
%%^End%%
