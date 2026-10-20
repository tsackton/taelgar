---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T10:36:55-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [place, status/wip, status/check/ai, status/check/lint]
typeOf: region
name: Drankorian Hinterland
whereabouts:
  - {type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
---
# The Drankorian Hinterland
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% Status:
* [ ] In world intro
* [x] Map
* [ ] Topography
* [ ] Civilizations and Culture
* [ ] History
* [ ] Climate
* [ ] Climate - Real World
* [x] DM Notes
%%

{intro text}
## Map


```taelgar-map 
id: region-map-drankor
image: [[region-drankorian-hinterland.png]] 
bounds: 
- [0,0]
- [2232, 4429]
height: 600px  
width: 1100px
lat: 1122
long: 2122
minZoom: -2
maxZoom: 0
defaultZoom: -2
unit: miles 
scale: 1
calibration:
  hexMiles: 24
  hexPixels: 40.333333333333336
  imageSize: [4429, 2232]
  imageSha256: fd72c6130b8b0dd39ee89af3e40b2d1d0c68714bc8ea578c86305db53c65173e
draw: false
darkMode: false
markerTag: location-source
```

## Topography and Major Features
_See more: {links}_

{descriptive text of topography and major features}
## Civilizations and Cultures
_See more: [[Drankorian Empire|Drankor]]

%%
Elves:  [[Rostaure|Rostaurë]] (long destroyed) and [[Drankor]]
Dwarves: None currently. [[~Eastern Mountains~]] undefined and may hold current or historical dwarves
Lizardfolk: Likely none; perhaps strange small communities in the jungle somewhere, mostly too arid
Humans: [[Drankor]] historically; none otherwise
Stoneborn:  Likely none
Hobgoblins: Perhaps in the east; unclear, leave blank
Dangerous Wildernesses: Yes
%%
## Climate

{descriptive in world text about climate}

%%^Campaign:none%%

{real world climate analogs and inspiration}

%%^End%%

## Major Historical Eras
_See more: {links}_

{descriptive text of major era}

%%^Campaign:none%%
## DM Notes and Meta
_See also: [[Places in the Drankorian Hinterland]]

*Area and Border Notes*: The eastern border of this region is not particularly canonical, but is broadly assumed to coincide with the eastern border of the Drankorian Empire. The northern border is similarly unclear, but is broadly meant to be the dividing line between "established civilization" and "dangerous wilderness". This does not preclude civilization lurking somewhere in this region, but in general any future invention with close ties to [[~South Cymea~]] or [[Cymea]] should be in the Western Green Sea region, even if it means moving the border.

*Canonical Development and Constraints:* This region was the core of the Drankorian Empire, which has a canonical history in broad strokes with patches of more extensive development. The basic geography and climate is mostly well-developed. The ruins of the city of [[Drankor]], the [[Circular Island]], and some details of the historical elven realm of [[Rostaure|Rostaurë]] are developed in some detail, as are [[Awakened Jungle|parts]] of the jungle along the coast of the [[Sea of Storms]]. The history of this region after the [[Fall of Drankor]], the wastes of the [[Garamjala Plateau]], and the jungles south of the [[Shrev]] are less developed.

*Brainstorming and Potential Canon:* Although it is assumed that at least the parts of this region closest to Drankor are dangerous wilderness after the [[Fall of Drankor]], the exact fate of this region in the years between the [[Fall of Drankor]] and the [[Great War]] is an area of active brainstorming but little canon. The [[~Eastern Mountains~]] are tentatively the eastern border of the [[Drankorian Empire]], but this is not strictly canonical. The region immediately south of the [[Shrev]] has some potential brainstorming context around Dunmari history, but nothing has been introduced in game beyond the bare existence of battles across the Shrev with zombies and other strange creatures. 

*Needs Development:* Much of the history of the Drankorian Empire is only loosely sketched: see [[Drankorian Empire - Open Questions]] for potential development needs. The climate and topography of the eastern part of this region (between the [[Istaros]] and the [[~Eastern Mountains~]] is largely blank, although generally assumed to be arid in the current day. The topography of the eastern part of this region may be better left blank until needed to be developed for [[~South Cymea~]] development.

*Intentionally Blank:* The desolation around Drankor and the wastes of the [[Garamjala Desert|Garamjala]] may hold many mysteries (e.g., the [[Tower of the Colossus]], and are best left as a blank area until needed for a game. The exact impact of the [[Downfall Wars]] on [[Alcarinque]], and the fall of the elven empires, is explicitly left blank, to be explored in a potential future [[Downfall Wars]] campaign. 

*Adventures:* The Dunmar Frontier campaign traveled across the [[Garamjala Plateau]], to the [[Awakened Jungle]], the [[Circular Island]], and [[Drankor]], during the end of the Apollyon arc. 

*Important Places in Staging:* The [[Circular Island]] needs to either be named "The Circular Island" in-game, or be renamed. The [[~Eastern Mountains~]] could use a name, as could the [[~Great Bay~]]. 

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Drankorian Hinterland", "language": "unknown", "pronunciation": "dran-KOR-ee-un HIN-ter-land", "status": "proposed", "notes": "The accepted stem DRAN-kor is recorded in [[Drankor]]. This proposal retains its consonants and broad vowels while cautiously adapting the adjective with stress before the ee-un ending; Hinterland uses ordinary English HIN-ter-land. The compound is a descriptive regional label with no established original language. The Drankorian analogue in [[Languages]] is Classical Latin with occasional Classical Greek loan words, within a broadly Hellenic and Romance language family. That supplies root context, not an exact rule for this mixed descriptive label; the adjective stress remains uncertain."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern regional geography with imperial history as background; the reader-facing descriptive sections are still largely unfinished.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting without changing existing values.
- Recorded the filename-supplied subject name explicitly.
- Recorded a broadly modern article POV and persistent temporal-coverage guidance.
- Corrected the case of both existing private Campaign:none sentinels, retaining their content and placement.
- Added persistent subject-name metadata with a proposed complete pronunciation and its derivation.

### Validated judgments
- `status/wip` is supported: the region-page reformatting remains unfinished, with multiple central placeholders. The tag is preserved.
- The map and substantive shared planning make this an eligible authored note; shared planning is not silently promoted to canon.

### Editorial assessment
**Underdeveloped** — The public region article has a map but no substantive introduction, and its topography, culture, climate, and history sections remain placeholders or hidden planning. Its central geographical identity, major developed landscapes, and imperial historical context are missing from the reader-facing account. The smallest useful scope is a concise regional overview and short source-grounded summaries of those developed features; leave explicitly unestablished eastern geography and post-imperial transitions uncertain.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The introduction is `{intro text}`, and the central geographical, climate and historical sections contain placeholders. [[Garamjala Plateau]], [[Awakened Jungle]] and [[Drankor]] already supply a bounded account of major features and their context. Copy-ready starting overview: “The Drankorian Hinterland includes the high, arid [[Garamjala Plateau]], the coastal [[Awakened Jungle]], and the ruins of [[Drankor]] near the mouth of the [[Istaros]]. Drankor was a center of the [[Drankorian Empire]] before the [[First Plague]] devastated the city in DR 1059.” Use those sources to replace the corresponding topography, climate and historical placeholders with brief summaries. Preserve uncertainty about the region’s precise borders, eastern terrain and unestablished transitions rather than filling them by inference.

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise the complete pronunciation `dran-KOR-ee-un HIN-ter-land` in the persistent name entry. The accepted stem DRAN-kor is recorded in [[Drankor]]. This proposal retains its consonants and broad vowels while cautiously adapting the adjective with stress before the ee-un ending; Hinterland uses ordinary English HIN-ter-land. The compound is a descriptive regional label with no established original language. The Drankorian analogue in [[Languages]] is Classical Latin with occasional Classical Greek loan words, within a broadly Hellenic and Romance language family. That supplies root context, not an exact rule for this mixed descriptive label; the adjective stress remains uncertain. If accepted, copy the complete value into frontmatter and mark the existing entry `documented`.
%%^End%%
