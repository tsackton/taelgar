---
headerVersion: 2023.11.25
lintedAt: "2026-10-18T23:48:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: realm
ancestry: elven
name: Alcarinquë
aliases: [Alcarinquë, status/check/mike]
pronunciation: ahl-KAH-rin-kweh
whereabouts: Taelgar
dm_owner: joint
dm_notes: none
POV: modern
---
# Alcarinquë
*(ahl-KAH-rin-kweh)*
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% marked joint just as a "part of elven stuff" but might not need to be, feel free to change to none %%

Alcarinquë is the name for the ancient elven realm of the north, part of the vast forests that once stretched from [[Orenlas]] in the east, across the [[Istaros Watershed]], west across the [[Hara Basin]], and north through the forests of the [[Elderwood]] and [[Ainumarya]]. 

Only pockets of this ancient forest remain to this day, primarily around [[Orenlas]] and scattered parts of [[Ainumarya]]. 

%% dm notes that might add color

Re: Orenlas remnant:

Orenlas is the last remaining ancient forest of the vast elven kingdom of Alcarinque, which once stretched from what is now the western coast of Dunmar to the [[Green Sea]] (South Cymea area). While many of the ancient trees have died, here still can be found pockets of forest originally called into being by the footsteps of Aldanor, the living tree. 

Intro about Stormcaller Tower:

*In younger days, when the vast forests of the elves stretched across these lands, a tower stood here, perched on a cliff. The cliff was less weathered then, its former form as a skyship of the storm giants clearer. Then, the winds brought news from across the vast kingdom of Alcarinquë, and for those who cared to hear it, even tidings of the humans on the distant island of Hkar. 

General:
- vibe is like [[Elderwood]] or [[Orenlas]] but bigger, more magical
- the big tree in Tokra is a remnant (not well documented)

Other than vibes, not really developed.

%%

%%^Metadata:names:v1%%
- {name: Alcarinquë, language: unknown, pronunciation: ahl-KAH-rin-kweh, status: documented}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective description of the ancient elven realm and its surviving forests; the identification of present-day remnants remains unresolved against Orenlas.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added a documented name entry preserving the accepted pronunciation; the name’s language remains unknown.
- Added a modern retrospective POV and temporal coverage identifying the unresolved remnant claim.

### Validated judgments
- The accepted frontmatter pronunciation is the name entry’s source; no new pronunciation was invented.
- The exact cause of the realm’s fall is deliberately left open in [[Historical Framework]] and was not inferred from private material.

### Editorial assessment
**Underdeveloped**. The visible realm entry identifies its former extent and possible remnants but omits the basic transition from the pre-Downfall elven realm to the depopulated lands settled by early Drankor. The smallest useful addition is a brief account of that established transition, leaving the mechanism of the realm’s fall uninvented and reconciling which forests survive.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The visible article does not situate the realm’s disappearance around the Downfall or explain its relationship to early Drankor. [[Historical Framework#The Downfall]] describes the end of the elven forest empires; [[History of the Drankorian Empire#Beginnings of Empire]] and its First Age of Expansion describe Drankor growing into changed, depopulated former Alcarinquë territory. Candidate: “The [[Downfall Wars]] and [[The Downfall]] ended the age of the great elven forest realms. In the centuries that followed, the [[Drankorian Empire]] expanded into lands formerly occupied by Alcarinquë.” Preserve the intentionally unknown mechanism and chronology of the elven retreat.
- [ ] **Warning — correctness.cross_note_conflict:** The second public paragraph identifies surviving pockets in both Orenlas and Ainumarya. [[Orenlas]] calls itself the last remnant of Alcarinquë, and [[Historical Framework#Founding Period]] explicitly describes Orenlas as the only modern survivor while leaving earlier fragments possible. Decide whether Ainumarya contains surviving Alcarinquë forest or is a distinct later elven realm. If the Orenlas account controls, a bounded replacement is: “[[Orenlas]] is the last surviving remnant of Alcarinquë’s ancient forests.” Do not adopt that replacement until the scope distinction is settled.
- [ ] **Suggestion — editorial.public_material_candidate:** In the shared comment, the passage introduced by “Intro about Stormcaller Tower” contains a concrete example of the ancient realm’s presence, alongside atmosphere and an explicitly undocumented Tokra-tree possibility. [[Stormcaller Tower]] independently establishes the public-safe historical core. Candidate: “Before [[The Downfall]], elves of Alcarinquë built [[Stormcaller Tower]] on the prow of a fallen storm-giant skyship.” Consider adopting that one sentence; keep the Tokra-tree suggestion and other undeveloped atmosphere as editorial notes, and resolve the Orenlas remnant wording under the separate conflict finding.
- [ ] **Warning — metadata.alias_status_value:** `aliases: [Alcarinquë, status/check/mike]` contains a status-shaped string as a name alias. It is not an actual review tag. Confirm the intended human-review state; the name-only candidate is `aliases: [Alcarinquë]`. If Mike review was intended, have a human separately authorize the appropriate tag. The linter did not remove the value or create a status tag.

### DM evidence
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
%%^End%%
