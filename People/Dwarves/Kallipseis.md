---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
ancestry: Drankorian
gender: female
name: Kallipseis
pronunciation: kah-LIP-sees
whereabouts:
  - {type: away, location: 27th House, end: 1740-10-06}
knownTo: [feywild]
dm_owner: none
dm_notes: none
POV: 1740
---
# Kallipseis
>[!info]+ Biographical Info  
> A [[Drankorian Empire|Drankorian]] [[Dwarves|dwarf]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Kallipseis is an ancient Drankorian dwarven wizard, gardener, and fungal researcher who spent many years within the [[27th House]]. She claimed leadership of [[Arithrimos Lamperum]] after [[Thalestria|Thalestria's]] disappearance or death. During her many years in the [[27th House]], she established a greenhouse and laboratory filled with cultures, terraria, strange helpers, and fungus growing on severed limbs. She studied how the fungus colonized flesh and attempted to reverse that relationship by culturing pieces of herself to take control of a fungal body. Her work reflected her conviction that "all progress involves sacrifice."

![[kallipseis-fungal-golem-v3.png|left|300]]When the 27th House began to collapse in DR 1740, Kallipseis transformed herself into a fungal golem. Her new body, shaped like a dwarven woman but made from fungi and lichens, sat up and looked upon the lifeless dwarven corpse that had previously held her soul. She consulted a book filled with long lists of six-digit numbers and disappeared. She is now, one presumes, somewhere in the Multiverse attempting to reestablish the [[Arithrimos Lamperum]].

%%^Metadata:names:v1%%
- {name: Kallipseis, language: unknown, pronunciation: kah-LIP-sees, notes: 'Explicit pronunciation recorded in [[_dm_notes/The 27th Room - DM Notes#Kallipseis, the Gardener]].', status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740 portrait combining her earlier work in the 27th House with her transformation and escape during its collapse; her subsequent whereabouts and success in rebuilding the order are presumed, not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added explicit `name`, documented pronunciation from [[_dm_notes/The 27th Room - DM Notes#Kallipseis, the Gardener]], supported `knownTo: [feywild]`, and temporal metadata.
- Normalized frontmatter while preserving its values.

### Validated judgments
- [[Lost in the Feywild - Episode 04]] and [[Lost in the Feywild - Episode 07]] support the scientist, claimed leadership, fungal body and departure. The note preserves uncertainty about her later whereabouts and rebuilding efforts.

### Open findings

- [ ] **Suggestion — temporal.date_scope_proposal:** The final paragraph beginning “When the 27th House began to collapse in DR 1740” reveals a later transformation and escape while the earlier description can serve a pre-collapse reading. [[Lost in the Feywild - Episode 07]] dates the collapse to DR 1740-10-06. Consider wrapping that entire final paragraph in `%%^Date:1740-10-06%%` and its matching end marker, then review whether the earlier article frame needs a broader POV. The current `POV: 1740` describes the unfiltered account; no visibility-changing block was added.
%%^End%%
