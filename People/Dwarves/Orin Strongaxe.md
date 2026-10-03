---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: dwarf
gender: male
campaignInfo:
  - {campaign: grli, type: met, date: "1747-09"}
name: Orin Strongaxe
affiliations:
  - {org: Strongaxes, type: primary}
whereabouts:
  - {type: home, location: Zarkandur}
  - {type: away, start: "1747-09", end: "1747-10", location: Voltara}
knownTo: [grli]
dm_owner: none
dm_notes: none
POV: 1740s
---
# Orin Strongaxe
>[!info]+ Biographical Info  
> A [[Dwarves|dwarf]] (he/him), of Strongaxes  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:grli%% Met by the [[Silver Tempests]] on September 1747 in [[Voltara]], [[Greater Voltara]], the [[Northern Provinces]] %%^End%%

Orin Strongaxe is a dwarf from [[Zarkandur]], a skilled warrior and respected commander. He is also an older cousin of [[Brelith]]. 

During [[Grumella's War]], he led a dwarven host to [[Voltara]] at [[Brelith]]'s request to aid in the defense of the city, and participated in several war councils. 


%%^Campaign:none%%

## DM notes

- DM notes describe him as an older cousin of Brelith, a seasoned commander, and the leader of about 400 dwarven soldiers sent to aid Voltara. **Source:** [[GL - Session 36 - DM Notes]].
- After the victory at Voltara, Orin told Brelith and the party of trouble to the south and invited them toward Brelith's home. Later Arc 3 notes say Orin and his warriors had left roughly three weeks before the party followed up on that promise. **Sources:** [[GL - Final battle]]; [[GL - Session 38 - DM Notes]].

%%^End%%

%%^Metadata:names:v1%%
- {name: "Orin Strongaxe", language: "unknown", pronunciation: "OH-rin STRONG-aks", notes: "Tolkien-inspired Dwarvish analogue from Languages; full o, short i, pronounced r and n, and first-syllable stress; English compound surname retained. This is an adaptation rather than an adopted phonological rule.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait anchored by his command during the DR 1747 defense of Voltara; the later southern-border material is retained as shared DM guidance.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal-viewpoint metadata; unestablished name languages remain `unknown`.
- Added the campaign knowledge code supported by existing interactions or finalized session evidence.
- Canonicalized the existing campaign code in metadata and its generated header without changing the campaign scope.

### Validated judgments
- The cousin relationship and war command are corroborated by the Great Library Arc 2 session record; the later southern-border hook stays in its existing shared DM block.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed pronunciation `OH-rin STRONG-aks` in `Metadata:names:v1`. The [[Languages]] Tolkien Dwarvish analogue motivates a full o, short i, pronounced r/n and initial stress; the English compound surname is read as written. These are analogue-informed proposals, not documented in-world phonology. On acceptance, set the entry to `status: documented` and copy the accepted primary pronunciation to frontmatter; no frontmatter pronunciation has been asserted.
- [ ] **Warning — relationship.unresolved:** The `affiliations` target `Strongaxes` does not resolve to a note, and the searched Strongaxe/Strongaxes/Strongaze references do not establish a separate clan identity beyond the surname. Confirm that this denotes a clan and authorize an appropriately sourced target, or remove `- {org: Strongaxes, type: primary}` and regenerate the corresponding “of Strongaxes” header if the affiliation is unintended. The linter has preserved it.
- [ ] **Suggestion — editorial.public_material_candidate:** The first bullet of the shared DM block repeats the visible cousin/commander description but also preserves the useful troop count from [[GL - Session 36 - DM Notes]]. Consider the bounded public addition: “He led about four hundred dwarven soldiers to [[Voltara]] during [[Grumella's War]].” If adopted, replace only that bullet with its source pointer; retain the later southern-border invitation and follow-up as separate campaign/DM guidance. The count remains a human adoption choice because the supporting account is shared DM preparation.
%%^End%%
