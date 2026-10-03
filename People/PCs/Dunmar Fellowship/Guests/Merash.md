---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
displayDefaults: {aNoDate: "Traveled with <affiliations>"}
tags: [person, status/check/lint]
species: dwarf
ancestry: null
born: null
gender: null
player: Sara Smith
name: Merash
aliases: [Merash Emberfoot]
affiliations:
  - {org: Dunmar Fellowship, title: Guest}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Merash
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

A dwarven fighter and blacksmith, summoned to aid the [[Bahrazel]] because of a debt owed for a miracle saving her life in a storm at sea.

%%^Metadata:names:v1%%
- {"name":"Merash","language":"unknown","pronunciation":"MEH-rahsh","notes":"Tentative adaptation of the Tolkien Dwarvish analogue in Languages to this dwarven name: clear eh and ah vowels, pronounced r, sh as in ship, and proposed first-syllable stress; the source language and exact phonology are unestablished.","status":"proposed"}
- {"name":"Merash Emberfoot","role":"full name","language":"unknown","pronunciation":"MEH-rahsh EM-ber-foot","notes":"The full name is recorded in [[Session 68 (DuFr)]]. Merash follows the tentative Tolkien Dwarvish-informed proposal; Emberfoot is read as the ordinary English compound.","status":"proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the DR 1748 divine summons described in the article, with earlier backstory explaining the debt; the note does not describe her later life.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added knownTo: [dufr], the documented full-name alias Merash Emberfoot, and persistent name metadata.
- Recorded POV: 1748 and temporal coverage of the divine summons; normalized frontmatter and removed the stray quote from the Guest affiliation title.

### Validated judgments
- The dwarf fighter and smith description performs this minor guest character’s reference role. [[Session 68 (DuFr)]] records the full name Merash Emberfoot.
- Reviewed the clustered local DM evidence and retained the existing positive dm_notes attestation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed pronunciations `MEH-rahsh` and `MEH-rahsh EM-ber-foot` in the persistent name block. Merash’s dwarven context and the Tolkien Dwarvish analogue in [[Languages]] support clear eh/ah vowels, pronounced r, and sh as in “ship”; first-syllable stress is tentative. Emberfoot is read as an ordinary English compound. No exact name-language or pronunciation source was found, so both remain proposals. If accepted, copy `pronunciation: MEH-rahsh` to frontmatter and mark the matching name entries documented; otherwise supply the intended readings.

### DM evidence
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Riswynn Solo Arc/Main Quest - Riswynn Solo]]
%%^End%%
