---
headerVersion: 2023.11.25
lintedAt: "2026-08-28T16:53:46-04:00"
lintVersion: "3.5"
displayDefaults: {aNoDate: "Traveled with <affiliations>"}
tags: [person, status/check/lint]
species: dwarf
ancestry: null
born: null
gender: male
player: David Schwartz
name: Thror
aliases: [Thror Redpeak]
affiliations:
  - {org: Dunmar Fellowship, title: Guest}
knownTo: [dufr]
dm_owner: player
dm_notes: important
POV: 1748
---
# Thror
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`

A sailor, pirate, and storm sorcerer, Thror felt remorse and prayed to the [[Bahrazel]] to give him another chance, and was nearly instantly pulled away to aid [[Riswynn]].

%% stayed to help dwarves of [[Morkalan]] reach tharn todar %%

%%^Metadata:names:v1%%
- {name: Thror, role: primary, language: Dwarvish, pronunciation: THROHR, status: proposed, notes: "Proposed from the Tolkien Dwarvish analogue; exact in-world pronunciation is not documented."}
- {name: Thror Redpeak, role: full name, language: Dwarvish, notes: "The fuller form is recorded in [[Session 68 (DuFr)]].", status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait centered on Thror's summons to aid Riswynn and his search for redemption; earlier and later life are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the opening sentence's spelling and grammar without changing its meaning.
- Corrected the malformed `Guest` affiliation title.
- Added the documented fuller form `Thror Redpeak` as an alias and persistent name entry.
- Added `knownTo: [dufr]` from [[Session 56 (DuFr)]], [[Session 58 (DuFr)]], and [[Session 68 (DuFr)]].
- Added a proposed Dwarvish pronunciation record for Thror.
- Added `POV: 1748` and a temporal-coverage note.
- Reordered and normalized frontmatter to the canonical form.

### Validated judgments
- [[Session 68 (DuFr)]] records the fuller name Thror Redpeak; the existing primary display name Thror was preserved.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `THROHR` uses the documented Tolkien Dwarvish analogue, but exact in-world phonology is not documented. Accept it, revise it, or leave the name entry proposed.
- [ ] **Suggestion — editorial.public_material_candidate:** The shared comment records a useful public-safe endpoint for Thror's story, and [[Session 58 (DuFr)]] establishes it. If approved, add after the visible paragraph: `After Hagrim's redemption, Thror stayed with [[Riswynn]] to help the freed dwarves of [[Morkalan]] travel to [[Tharn Todor]] and begin reintegrating into dwarven society.`
%%^End%%
