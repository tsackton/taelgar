---
lintedAt: "2026-10-20T11:59:58-04:00"
lintVersion: "3.5"
tags: [place, status/wip, status/check/ai, status/check/lint]
typeOf: region
name: Northern Green Sea
whereabouts:
  - {type: home, location: Taelgar, linkText: in}
dm_owner: joint
dm_notes: important
POV: modern
---
```taelgar-header
```

The northern coastline of the [[Green Sea]] is a strange place, where even halfling traders rarely go. The land of [[Ursk]] is unwelcoming even to halflings, and few have traveled its roads and rivers. North of [[Ursk]] is a cold land of mighty forests and rivers, rushing in the brief summer but frozen during the long winter. Our reports come from the few halfling travelers and traders who brave the cold. 
## Map

```taelgar-map 
id: region-map-taelgar
image: [[north-green-sea-region.png]] 
bounds: 
- [0,0]
- [1423,3341]
height: 400px  
width: 900px
lat: 697
long: 1700
minZoom: -2
maxZoom: 0
defaultZoom: -2
unit: miles 
scale: 0.5
calibration:
  hexMiles: 24
  hexPixels: 30.250000000000004
  imageSize: [2534, 1076]
  imageSha256: 4bb3154966e59f9d6494cc5e97f8b6734bfa9a84abcbd412120f7cd94ec34e56
draw: false
darkMode: false
markerTag: location-source
```

## Topography and Major Features
[[Yengorza Mountains]], [[Ket]], [[Svinjo Mountains]], [[Great Northern Forest]]

## Civilizations and Cultures
_See more: [[Ursk]], [[Vargaldi]]_

The northern coasts of the [[Green Sea]] are a cold and unforgiving land, and it is a place to be careful and on your guard. The land of [[Ursk]] is closed to outsiders, and halfling traders report much fear and suspicion of anyone expressing interest in venturing beyond the trading enclaves of [[Praznitsky]] and [[Zakat]]. The wizard rulers of Ursk, the halflings warn, are not to be disobeyed lightly.

To the north and west of [[Ursk]] the forests stretch for hundreds of miles, and there is little safety here. Halflings bring tales of giant bats, dragons breathing frost, and ice worms the size of small boats. Along the [[Ket]] there are whispered tales of scattered humans known as the [[Vargaldi]] - but the halflings say they are skittish, and are unwilling to spill their secrets. 

The [[Svinjo Mountains]], the halflings say, should be explored cautiously. The dwarves and stoneborn living here are mostly indentured to the frost giants of [[Kaldhalla]], who are not forgiving of questioning outsiders. Little profitable trade can be had here and it is best to avoid the area. 
## Climate

%%^Campaign:none%%

%% TODO
* [ ] Real world examples
%%

%%^End%%

## Major Historical Eras

%%^Campaign:none%%
## DM Notes and Meta
_See more: [[List of Places in the Northern Green Sea]]_

*Canonical Development and Constraints:* The culture of [[Ursk]] is well developed, although there are a number of blank spots in the history. The [[Vargaldi]] are also reasonably well developed, although generally only in broad strokes. This area has a significant frost giant presence, in [[Kaldhalla]], and the conflict between frost giants and white dragons has substantially shaped some of the details of the wilderness here. Canonically there are established dwarven and stoneborn cultures in the [[Svinjo Mountains]], but no details are invented about these peoples. The existence of a vampire kingdom on the western borders of Ursk is canonical, although the fate of this region after the interventions of the [[Dunmar Fellowship]] has not been determined. 

*Brainstorming and Potential Canon:* In general, this region is assumed to be largely wilderness, and dangerous, outside the developed regions, but details are somewhat vague, especially along the coast to the west of Ursk, which is canonically dangerous but whether something beyond vampires lurks here is undetermined. There is plenty of room for additional oddities and dangers in this region, and the coast west of [[Ursk]] is relatively undeveloped. This longer term history of this region is largely blank, except for recent history of Ursk and ancient history of the Vargaldi. However, the region as a whole is largely complete from a vibes perspective, so new development needs to conform to the existing overall design of the region. 

*Needs Development:* The history of [[Ursk]] is relatively poorly developed, especially prior to the Great War; the origins of the Urskan people are not canonically determined, although these are presumed to be mariners of some kind. The religion of Ursk is unclear, although divine magic is exceedingly rare among Urskans. The history of [[Kaldhalla]] before [[Vimfrost's War]] is only weakly sketched.

*Intentionally Blank:*  None.

*Adventures:*  The Ursk arc of the Dunmar Frontier campaign traveled extensively across this region, including to [[Kaldhalla]], the [[Great Northern Forest]], and [[Ursk]],

*Important Places in Staging:*  [[Yengorza Mountains]]
%%^End%%

%%^Metadata:names:v1%%
- {"name":"Northern Green Sea","language":"unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography; no narrower temporal anchor is established for the visible description.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit name, a minimal name block, and broadly modern temporal metadata.
- Corrected “wizards rulers” to “wizard rulers.”
- Converted the equivalent legacy `Campaign:None` sentinels to canonical `Campaign:none`.

### Validated judgments
- The descriptive English regional name does not need a pronunciation; its source language is not established.
- `status/wip` is supported by the unfinished regional sections. Existing human-review check tags are preserved.
- The shared DM/meta constraints and brainstorming remain nonpublic and are not promoted into the article.

### Editorial assessment
**Underdeveloped**: the regional overview has a link-only topography section and no visible account under Climate or Major Historical Eras. Its central gaps are the relationship among the mountains, forest, and rivers; the regional seasonal contrast; and a minimal account of the established giant/dragon history. A short synthesis of the existing geographic notes is sufficient; a comprehensive invented regional history is not required.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The existing Topography and Major Features, Climate, and Major Historical Eras sections provide links, a TODO, or no visible account. [[Great Northern Forest]], [[Yengorza Mountains]], [[Ursk]], and [[Kaldhalla]] establish enough for a minimal regional account. Proposed additions, placed under those headings respectively: “The [[Great Northern Forest]] stretches east from the [[Svinjo Mountains]] across much of the [[Ket]] drainage. The [[Yengorza Mountains]] mark the northern border of [[Ursk]] and feed rivers including the [[Beyil]] and [[Dalinka]].” “Ursk’s coastal plains have long snowy winters and short summers that support agriculture. Farther north, the Great Northern Forest has a late muddy thaw, brief bright summers, and an early return of frost.” “[[Kaldhalla]] predates human settlement around the Green Sea. It shrank after [[Vimfrost's War]] and [[Bjarnfrost|Bjarnfrost’s]] death; its giants now rarely leave their mountain strongholds.” These bounded additions fill the established central gaps without inventing a region-wide chronology.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes: important`. The mechanical direct-identity dossier has no matches. Keep the human attestation unless its owner confirms a change; remembered or off-vault information may support it.
%%^End%%
