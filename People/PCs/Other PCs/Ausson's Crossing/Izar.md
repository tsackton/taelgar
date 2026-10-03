---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/stub, status/check/lint]
species: lizardfolk
born: 1579
gender: enby
player: Kiya Nicoll
name: Izar
knownTo: []
dm_owner: player
dm_notes: important
POV: 1680s
---
# Izar
>[!info]+ Biographical Info  
> A [[Lizardfolk|lizardfolk]] (they/them)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`

A retired adventurer, now serving as an accountant, scribe, and occasional trade facilitator to the inhabitants of the [[Ausson's Crossing]] region.

%%^Metadata:names:v1%%
- {"name":"Izar","language":"unknown","pronunciation":"ee-SAHR","status":"proposed","notes":"Proposed from the Lizardling Basque analogue in Languages: i as ee, z as a voiceless s, and a as ah. Final stress is provisional; neither exact name-language nor stress is established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: Izar’s retired professional role around the DR 1688 Ausson’s Crossing setting, identified in PCs; the duration of that role and the adventure’s precise canonical events are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected “retired adventure” to “retired adventurer.”
- Added knownTo: []; no registered campaign knowledge is established.
- Added persistent name metadata with a proposed pronunciation.
- Recorded POV: 1680s from the Ausson’s Crossing setting in [[PCs]], preserving uncertainty about the adventure; normalized frontmatter.

### Validated judgments
- The concise former-adventurer and local professional description serves the minor reference role. The separate play account is explicitly uncertain and does not justify adding its events as settled biography.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm proposed `ee-SAHR`. [[Languages]] gives Lizardling the Basque analogue: i is ee, z is a voiceless s, and a is ah. Final stress is provisional because no exact in-world stress rule or name-language is recorded. Accept or correct it before marking it documented and copying it to frontmatter.
- [ ] **Warning — status.questioned:** The retained `status/stub` is questionable: the visible sentence already gives Izar’s former occupation, current services, and regional connection, satisfying the bounded minor reference role under [[Note Status]]. Human choice: remove `status/stub` if no intended detail remains, or retain it and identify the specific unfinished dimension. The linter leaves the tag unchanged.
%%^End%%
