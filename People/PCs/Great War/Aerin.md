---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: kenku
gender: male
player: David Schwartz
name: Aerin
affiliations:
  - {type: primary, org: Heroes of the Great War}
knownTo: [dufr]
dm_owner: player
dm_notes: important
POV: 1740s
---
# Aerin
>[!info]+ Biographical Info  
> A [[Kenku|kenku]] (he/him), of the [[Heroes of the Great War]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

A kenku, rogue, and traveler. Current whereabouts are unknown. 

%%NOTES
Kenku rogue, also effectively the Firstborn of the Kenku.

Known for ability to shapeshift, seal his mind from outside influence, speak telepathically, and vanish from sight and magic.

Current whereabouts are unknown.
%%

%%^Metadata:names:v1%%
- {"name": "Aerin", "language": "unknown", "pronunciation": "AIR-in", "status": "proposed", "notes": "Cautious spelling proposal: ae as air, short i, retained r/n and first-syllable stress. [[Kenku]] limits the Sioux naming inspiration to islander examples and explicitly leaves wider application unsettled; no evidence ties Aerin to that pattern, so no exact Kenku phonology is inferred."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740s retrospective capsule of a Great War hero whose later whereabouts remain unrecorded in [[Research from Kassi]]; the hidden notes do not establish a dated later state.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added `knownTo: [dufr]`, supported by [[Research from Kassi]].
- Added persistent name metadata with a proposed pronunciation, and the retrospective temporal frame.

### Validated judgments
- The header already identifies membership in the [[Heroes of the Great War]], and [[Research from Kassi]] supports the limited record of later whereabouts.

### Editorial assessment
**Underdeveloped**: the visible capsule does not explain Aerin's individual role or remembered contribution as one of the four Heroes of the Great War. The smallest useful scope is one short, public-facing identity-and-contribution paragraph; the existing hidden ability notes may help distinguish him, but his private cosmological status must remain separate and uncertain.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Review the proposed `AIR-in`: a cautious reading of ae as “air,” short i, retained r/n and first-syllable stress. Although [[Languages]] lists a Sioux analogue for Kenku, [[Kenku#Language and Naming]] explicitly restricts that inspiration to islander examples and leaves its wider application unsettled. No evidence connects Aerin's name to that pattern. Confirm the player's reading rather than presenting this spelling-based proposal as adopted Kenku phonology.

- [ ] **Suggestion — editorial.public_material_candidate:** The middle sentence of the ordinary `NOTES` comment contains a developed character description absent from the short visible capsule. Consider adopting: “Aerin is remembered for shapeshifting, shielding his mind from outside influence, speaking telepathically, and hiding from both sight and magic.” This would distinguish him from a generic rogue. Keep the remaining cosmological claim in private guidance and preserve its unresolved status; trim the duplicated identity/whereabouts lines only if reorganizing that comment is approved.

- [ ] **Suggestion — editorial.note_underdeveloped:** The visible body gives only a species, profession, and unknown whereabouts, although [[Heroes of the Great War]] and [[Battle of Urlich Pass]] establish the importance of the four heroes. Develop one short paragraph about Aerin's individual contribution or remembered reputation in that story. The current sources establish collective victory but do not settle his distinctive individual role; that missing account requires human development, not invented connective lore or automatic adoption of the private cosmological claim.
%%^End%%
