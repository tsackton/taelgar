---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: town
created: 1652
population: 1187
name: Aslain
pronunciation: Ahz-lane
whereabouts: Barony of Aveil
dm_owner: mike
dm_notes: color
POV: modern
---
# Aslain
*(Ahz-lane)*
>[!info]+ Information  
> pop. 1,187  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Aslain is a busy market town near the confluence of the [[Auberonne]] and [[Leandre]] rivers in the [[Barony of Aveil]]. The town, and much of the farmland to the east along the banks of the [[Auberonne]], is historically controlled by the [[d'Aslains|d'Aslain]] family. It is not fortified, and was rebuilt during the reign of [[Cece I]] after the ravages of the [[Third Hobgoblin War (Sembara)|hobgoblin wars]], across the river from the ancient town of the same name, now in ruins. This is a rich agricultural region, but the town does not have any large industries or significant trade, other than a small number of halflings mostly plying the cloth trade. This is too far north for the timber trade in Aveil, although some masonry and stone does make its way downriver to Rinburg, for building.

There is a large temple to [[The Mother]] here, and a small and still once-active temple to [[The Night Queen]] in the ruins across the river, as well as two inns: [[The Resting Ox]] and [[The Setting Sun]].

There is a large dwarven community here, mostly [[Ferrystones]], who specialize in rebuilding with reclaimed stones, and are renowned in the region for their work at reclaiming stone from the old town ruins. 

In DR 1720, the Temple to the Night Queen was destroyed on suspicion of harboring necromancies, in response to the [[Undead Attacks in Sembara]]. The temple was never rebuilt, and the small community in the old town ruins has dispersed to Aslain or moved south to [[Rinburg]].

%%^Metadata:names:v1%%
- {"name": "Aslain", "language": "unknown", "pronunciation": "Ahz-lane", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern town description with a dated account of the Night Queen temple’s destruction in DR 1720; the contradictory undated temple wording still requires human revision.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing parsed values.
- Added an explicit `name` matching the existing subject and filename.
- Recorded `POV` and a persistent temporal-coverage note.
- Corrected objective spelling, punctuation, duplication, or grammar in the declared passages; lore and visibility are preserved.
- Added a documented primary name entry matching the existing accepted frontmatter pronunciation.
- Added the required typed map block, leaving its unsupported locator blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — content.internal_conflict:** The second paragraph says there is “a small and still once-active temple” to the Night Queen, but the last paragraph says that temple was destroyed in DR 1720 and never rebuilt. Clarify the undated description without silently choosing a different period. For the post-destruction account, replace the second paragraph with: `There is a large temple to [[The Mother]] here. Across the river lie the ruins of a former temple to [[The Night Queen]]. The town also has two inns: [[The Resting Ox]] and [[The Setting Sun]].` If the earlier state is wanted instead, explicitly frame it before destruction and retain the dated aftermath separately; any new Date block needs human approval.
- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block has a blank `locator`. No supported position was found in the reviewed sources. Supply the settlement’s world-map locator in `locations: [{map: world, locator: <verified locator>}]`; do not infer a coordinate from prose distances.
%%^End%%
