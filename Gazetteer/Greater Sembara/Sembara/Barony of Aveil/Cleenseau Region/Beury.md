---
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
population: 492
name: Beury
pronunciation: BUH-ree
whereabouts: Manor of Beury
dm_owner: mike
dm_notes: none
POV: 1720s
mapLocation:
  x: 6069.030291448552
  y: 5652.236997808361
  hex: 12.10.I.06/5000
  importance: local
---
```taelgar-header
```

A large farming village six miles downriver of [[Cleenseau]] and the principal (and only) village in the [[Manor of Beury]]. There are about ninety sturdy houses here, many of which predate the [[Third Hobgoblin War (Sembara)|hobgoblin wars]], although the village was abandoned for several years in the 1640s.

The houses are arranged in two tight concentric circles around a main square, where the one-story wooden manor house sits, as does the slightly larger stone temple of [[The Father]], the blacksmith, and two wells. The entire village, save for the small inn and mill (see below), fits within a thousand-foot diameter circle. There is a well-made wooden wall surrounding the outer circle of houses, although the inn and mill are outside the wall.

Beyond the second circle of houses, straddling the [[Great South Road]] is a nameless inn, usually just called "the inn in Beury" (or sometimes, jokingly, "Bee's Rest"). The inn is more of a stable and resting spot for caravans before crossing the [[East Bog|boggy wetlands]] to [[Dallet]] than a proper inn, and the food and drink are notably lacking. Many caravans resting here simply camp in the yard. Across the road and a few dozen feet from the inn is a sturdy stone millhouse.

A [[Manor of Beury#Economy|small market]] is held in the caravan yard once a week, which attracts some of the people from [[Asineau]] and [[Ganboa]].

Beury traditionally celebrates the festival of the Empty Cauldron on May 12. The festival commemorates a famine after the [[Great War]] and a story that [[The Father]] answered an old woman's prayers by filling her empty pot with food. Its central custom is a communal stew made from winter stores and new spring shoots.
## Notable Residents
* [[Erick Murtha]], the lord, and his wife
* Clare Murtha, his daughter and heir
* Roland Murtha, Clare's husband, originally from the Save merchant family in [[Cleenseau]], now steward
* [[Edmund Bracken]], his valet and bodyman
* [[Collette Murtha]], his cousin and temple steward
* [[Jean-Luc d'Aslain]], a disciple of the Father, part-time resident, shares time with [[Dallet]]
* [[Lionel Mortagne]], the captain of the guard, and [[Blanche]], his assistant and the magistrate
* [[Jasper of Beury|Jasper]], a reformed robber and sword-for-hire
* Johanna, the innkeeper and miller, and her sisters and children
* Roaric Ferrystone, the dwarven blacksmith, elderly and semi-retired, originally from the [[Ferrystones]] of [[Rinburg]]

%%^Campaign:None%%
### People in, or based in Beury
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

_Distances:_
* to [[Cleenseau]], 5 miles
* to [[Dallet]], 15 miles
* to [[Rinburg]], 55 miles

%% Some color notes:
* the second most important town in the region after Cleenseau, and the most independent and self-sufficient
* has the feel of a "way point" lots of folks stop here briefly on the way along the road, it is the first town near the bog/haunted stretch of road (see [[East Bog]]) 
* high  compared to its size - number of guards who help out escorting caravans along the road through the east bog
* nonetheless clearly secondary to cleenseau
%%

%%^Metadata:names:v1%%
- {"name": "Beury", "language": "unknown", "pronunciation": "BUH-ree", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the settlement description and named current residents reflect the Cleenseau campaign era around DR 1720; the older abandonment and festival origin are retrospective history.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving existing parsed values.
- Recorded `POV` and a persistent temporal-coverage note.
- Corrected objective spelling, punctuation, duplication, or grammar in the declared passages; lore and visibility are preserved.
- Added a documented primary name entry matching the existing accepted frontmatter pronunciation.
- Added the required typed map block, leaving its unsupported locator blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — content.internal_conflict:** The opening places Beury six miles downriver of [[Cleenseau]], while the distances list gives five miles. Confirm whether these describe different routes or one value is wrong. For a single six-mile distance, replace `* to [[Cleenseau]], 5 miles` with `* to [[Cleenseau]], 6 miles`; for different routes, label each measurement explicitly. Do not silently pick one.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The query section opens with `%%^Campaign:None%%`; the registry’s reserved private sentinel is `%%^Campaign:none%%`. Proposed one-line correction: `%%^Campaign:none%%`. Confirm that the intended private visibility is retained; the block has been preserved for human disposition.
- [ ] **Suggestion — editorial.shared_material_redundant:** The closing “Some color notes” comment repeats the visible inn/caravan account’s waypoint role and the dangerous road by [[East Bog]]. It also contains distinct draft judgments about relative importance, independence, and guard numbers. Remove only the duplicate waypoint material and preserve the unresolved guidance in a bounded comment, for example: `%% Editorial: consider Beury’s relative standing to Cleenseau, its independence, and the number of guards relative to its size; [[Manor of Beury]] documents the caravan-escort trade. %%` The comment’s hierarchy and comparative guard claims remain unadopted.
- [ ] **Warning — metadata.map_location_missing:** The required `Metadata:map:v1` block has a blank `locator`. No supported position was found in the reviewed sources. Supply the settlement’s world-map locator in `locations: [{map: world, locator: <verified locator>}]`; do not infer a coordinate from prose distances.
%%^End%%
