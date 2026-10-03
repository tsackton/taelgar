---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
displayDefaults: {aNoDate: "Traveled with <affiliations>"}
tags: [person, status/check/lint]
species: lizardfolk
ancestry: null
born: null
gender: male
player: Eric Rosenbaum
name: Izzarak
affiliations:
  - {org: Dunmar Fellowship, title: Guest}
knownTo: [dufr]
excludePublish: [clee]
dm_owner: player
dm_notes: important
POV: 1748
---
# Izzarak
>[!info]+ Biographical Info  
> A [[Lizardfolk|lizardfolk]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`

A lizardfolk shaman, traveler, and guardian to two young lizardfolk babies. Came to [[Bedez]] because he was told that the babies must get to the [[Azta Lekua|Footprint of the Gods]]. Traveled with [[Kenzo]]. After helping to heal the wounds to the [[Azta Lekua|Footprint of the Gods]], decided to stay and raise the babies in the protection of the spirits of the [[Azta Lekua]]. 

%%^Metadata:names:v1%%
- {"name": "Izzarak", "language": "unknown", "pronunciation": "ee-SAH-rahk", "status": "proposed", "notes": "Lizardfolk context supplies the Lizardling Basque analogue in [[Languages]]: i is ee, a is ah, z is voiceless s, r is a light tap, and final k remains k. Middle stress is an approximation; exact name language and phonology are unconfirmed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait after Izzarak chooses to remain at Azta Lekua and care for the babies; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo` from the established party relationship and campaign records.
- Removed a stray quotation mark from the affiliation title `Guest`.
- Normalized frontmatter field order and collection formatting.
- Added persistent name metadata and a supported `POV`/`povNotes` interpretation.

### Validated judgments
- The bounded reference performs its present role; routine campaign episodes do not require additional reference prose.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The note calls the two dependents “lizardfolk babies,” but [[Session 64 (DuFr)]] records Eleuha identifying them as Lengau’s shapeshifting children, followed by Lengau thanking Izzarak for bringing them home. Their nature is central to his guardianship and decision to remain. Candidate addition: `The babies in his care were identified by [[Eleuha]] as shapeshifting children of [[Lengau]], whose forms were not yet fixed.` Preserve the distinction between their initial appearance and the later revelation.

- [ ] **Warning — metadata.names_unresolved_status:** The proposed `ee-SAH-rahk` follows the Lizardling Basque analogue in [[Languages]]: i = ee, a = ah, z = a voiceless s, a light tapped r, and pronounced final k. Middle stress is tentative, and no accepted in-world pronunciation was located in the consulted sources. Confirm or revise the proposal, then copy it to frontmatter and mark it documented.
%%^End%%
