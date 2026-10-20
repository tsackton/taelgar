---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [status/cleanup/text, place, status/check/lint]
typeOf: settlement
typeOfAlias: village
population: 448
name: Maudorville
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: 1720s
---
# Maudorville
>[!info]+ Information  
> pop. 448  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% Notes for game prep

At the confluence of the Madour Brook and Auberonne

Maudorville is a small town of about 500 people, more in the Rinburg orbit than north. 

People in Maudorville

* innkeep
* lord
* temple admin of Sibyl

Maudorville is an ancient place, it was far enough north that it didn't fall in the hobgoblin wars. 
timber trade, nearish river, old buildings, temple is impressive 2 story with moon carvings
Temple of Sibyl here, administrator is Wilhelm, moon guy.

Temple of Sibyl was founded after a moonlight square (it was a perfect square) healed all those inside the square
recently moon lore vs other aspects of Sibyl has become important

Important place for timber trade downriver to rinburg; there is a horsepath along the river and barges sometimes; plus timber floating

Lord Antoine Chevalier ahn-TWAHN shuh-VAL-ee-ay

Wilhem - temple admin

Susanna - innkeep / unnamed inn / small, sign of a bed, only inn in town
her daughter and daughter-in-law are missing (Amelie and Anna)

%%

%%^Metadata:names:v1%%
- {"name": "Maudorville", "language": "unknown", "pronunciation": "moh-dor-VEEL", "status": "proposed", "notes": "The French analogue within Sembaran in [[Languages]] supports au as oh, ville as veel, a light r, and final phrase stress. English MAW-dor-vil is a possible alternative under Sembaran’s other analogue, but the French-shaped ville ending favors the stated proposal; the source language is not explicitly attested. Exact in-world pronunciation remains unconfirmed."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: hidden game preparation and its named offices belong to the Cleenseau campaign around DR 1720; the page has no visible authored reference account or established later snapshot.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing parsed values.
- Added an explicit `name` matching the existing subject and filename.
- Recorded `POV` and a persistent temporal-coverage note.
- Added a persistent primary name entry with a proposed pronunciation and its derivation; accepted frontmatter pronunciation is unchanged.
- Added the required typed map block, leaving its unsupported locator blank for human completion.

### Validated judgments
- `status/cleanup/text` is supported: substantive town material remains entirely in a rough preparation comment.

### Editorial assessment
**Underdeveloped** — The settlement has no visible reference account. Its established local lord and temple are absent, and its coherent but unadopted timber-trade and architectural description remains in game preparation. The smallest useful scope is one short town paragraph plus a human decision on that developed draft material, without publishing encounter hooks or unresolved fates.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The visible body contains no town account. [[Antoine Chevalier]] identifies Maudorville’s lord, [[Wilhem of Maudorville]] identifies its temple administration, and [[cleenseau-016-session-recap]] confirms those roles in the February DR 1720 visit. Proposed baseline: `Maudorville is a settlement in the [[Barony of Aveil]], ruled by [[Antoine Chevalier]]. Its temple to [[The Sibyl]] is administered by [[Wilhem of Maudorville|Wilhem]], who has a keen interest in lunar lore.` The missing-person investigation is incidental to the settlement account and need not become its history.
- [ ] **Suggestion — editorial.public_material_candidate:** The ordinary comment headed “Notes for game prep” has a coherent public-safe account in the passages beginning “Maudorville is an ancient place,” “timber trade,” and “Important place for timber trade downriver.” These give the otherwise invisible town a useful economic and physical identity, but remain unadopted working material. Candidate: `Maudorville is an ancient timber-trading town. Timber is floated downstream toward [[Rinburg]], and barges and a horsepath also serve the river trade. Its two-story temple to [[The Sibyl]] is decorated with carvings of the moon.` If adopted, remove only those resolved draft statements from the comment. Retain the proposed temple-foundation story, the unresolved brook spelling and population approximation as separate editorial questions, and keep the named missing-person hooks in private preparation.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent primary entry proposes `moh-dor-VEEL`. The French analogue within Sembaran in [[Languages]] supports au as oh, ville as veel, a light r, and final phrase stress. English MAW-dor-vil is a possible alternative under Sembaran’s other analogue, but the French-shaped ville ending favors the stated proposal; the source language is not explicitly attested. This is an analogue-informed proposal, not established in-world phonology. Accept or revise it; if accepted, copy the complete pronunciation to frontmatter and set the entry to `status: documented`.
- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block has a blank `locator`. No supported position was found in the reviewed sources. Supply the settlement’s world-map locator in `locations: [{map: world, locator: <verified locator>}]`; do not infer a coordinate from prose distances.
%%^End%%
