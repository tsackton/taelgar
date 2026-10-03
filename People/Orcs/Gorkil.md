---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: orc
campaignInfo:
  - {campaign: dufr, person: Seeker, type: killed, date: 1748-05-05}
born: 1729
gender: male
died: 1748-05-05
name: Gorkil
affiliations:
  - {org: "Grash's Horde", type: primary}
whereabouts:
  - {type: home, start: 1747, location: Kharsan}
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1748
---
# Gorkil
>[!info]+ Biographical Info  
> An [[Orcs|orc]] (he/him), of [[Grash's Horde]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Killed by [[Seeker]] on May 5th, 1748 in [[Kharsan]] %%^End%%

An [[Orcs|orc]] cleric in [[Grash's Horde|Grash's army]]. 

%%^Campaign:dufr%%
Captured in battle in May 1748 by [[Dunmar Fellowship]], and interrogated before using magic to convince [[Seeker]] to kill him, seemingly because he insisted he could not die under [[Grash]]'s power. After his death, his body was burned and did not reanimate. 
%%^End%%

%%One Note
A loyal servant of Grash captured and interrogated by party and Havdar at Havdar's camp in the eastern wastes.
 
Demanded to be killed and eventually got Seeker to do it with the _command_ spell.
 
**Current Location: dead, burned outside Havdar's camp in the eastern wastes**
%%

%%^Metadata:names:v1%%
- {name: "Gorkil", language: "unknown", pronunciation: "gor-KEEL", status: "proposed", notes: "Proposed from the Turkic analogue for Orcish in Languages: hard g and k, a pure o vowel, tapped r, clear ee for i, and final-syllable stress. The name language and exact in-world phonology are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account of Gorkil's role in Grash's army and his final encounter; the campaign-scoped paragraph includes his death in May of that year.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` and normalized the existing campaign metadata and markers to `dufr`.
- Added a proposed pronunciation with its cultural analogue and derivation, and recorded the DR 1748 temporal frame.

### Validated judgments
- [[Session 21 (DuFr)]] corroborates the cleric’s allegiance, interrogation and death.
- The matched local evidence contains no useful uncaptured remainder; `dm_notes: none` is retained.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review proposed pronunciation `gor-KEEL` in the name block. It uses the Turkic analogue for Orcish in [[Languages]]: hard g and k, a pure o vowel, a tapped r, clear ee for i and final-syllable stress. This is a cultural-analogue proposal, not established in-world phonology; the name’s source language remains unknown. If accepted, copy the pronunciation to frontmatter and mark the entry `documented`.

- [ ] **Warning — correctness.cross_note_conflict:** The header says Gorkil was killed “in [[Kharsan]]”, but [[Session 21 (DuFr)]] places his interrogation and death in Havdar’s camp before the party travels toward Kharsan. The undated home entry supplies a misleading encounter location. Retain the Kharsan home, and consider adding `{type: away, start: 1748-05-05, end: 1748-05-05, location: "Havdar's camp"}` to whereabouts; then regenerate the header so the encounter location reads “at Havdar’s camp”. This is a source-backed correction proposal, not a change to his home.

- [ ] **Suggestion — editorial.shared_material_redundant:** The ordinary comment headed “One Note” substantially repeats the visible capture, interrogation, commanded death and burned corpse. After correcting the camp location above, remove those repeated sentences and retain only a source pointer plus the distinct spell-identification caveat. Copy-ready comment contents: “Source: [[Session 21 (DuFr)]]. The original OneNote summary identifies Gorkil’s spell as command; confirm before adopting that identification.”
%%^End%%
