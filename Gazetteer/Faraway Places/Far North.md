---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/cleanup/map, status/check/lint]
typeOf: region
name: Far North
whereabouts:
  - {type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
---
# The Far North
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% convert map to leaflet %%

Far north, beyond the northern lands of [[Vostok]] and [[Ursk]] lies a mysterious land of long winters and bitter cold. Rarely visited, even rumors from this region rarely reach the populated lands of the south. The stories that do reach the south tell of frost-breathing dragons, obsidian statues as tall as the hills, and singing caves of ice that devour unwary travelers. More prosaic stories of wooly mammoths with heavy ivory tusks and short summers filled with rushing snowmelt and clouds of gnats as far as the eye can see have also come south. Who is to say which stories are true?
## Map

![[far-north-map.png]]

## Topography and Major Features
Few have mapped this region, and little is known about the lands. A few features are well-attested:

%% note: all of these features are in tentative, largely because they are too ill-defined to name, but mostly are expected to exist in some form %%

* A [[~Far North Steppe~|cold, dry expanse of open land]] north of [[Vostok]] and the [[Grastenvakt|Gråstenvakt]]
* A [[~Far North White Dragon Mountains~|range of mountains]] north of the [[Ket]], said to be the birthplace of [[Vimfrost]] and home to many frost-breathing dragons
* A [[~North Ursk River System~|river system]] that drains from the [[~Far North White Dragon Mountains~|range of mountains]] north of the [[Ket]] to the eastern [[Green Sea]]

## Civilizations and Cultures
Although rumors persist of [[Kenku|kenku]] flying across the [[~Far North Steppe~|northern steppe]], few can say where exactly these winged creatures live.
## Climate
This region of Taelgar is nearly entirely within the subpolar or polar climates, a mix of [vast subarctic forests](https://geodiode.com/climate/subarctic) and [barren tundra](https://geodiode.com/climate/tundra). But few rumors or tales come to the south from these regions, and in the distant north, who knows what strange magic may sustain life in unlikely places?
## Major Historical Eras
Little is known of the history of this region, although [[Vimfrost's War]] was partially fought here.

%%^Campaign:none%%
## DM Notes and Meta
*Area:* This region is poorly defined as little geographic development exists, but roughly speaking it includes everything north of the [[Slate Sea]] coast, [[Pandar]], [[Vostok]], and the [[Ket]], and then follows an arbitrary line north of the Green Sea east of [[Ursk]]. In general, permanent 'normal' human civilizations should be south of this region, although of course an arctic culture is possible.

*Canonical Development and Constraints:* This region, particularly the mountains north of [[Ursk]], is home to many white dragons, including the descendants of [[Vimfrost]], which has significant influences both on this area and regions to the south. A large number of [[Kenku]] canonically make their home on the [[~Far North Steppe~|northern steppes]], on the eastern slopes of the [[Sentinel Range|Sentinels]] north of [[Zimka]] but few details have been developed.

*Brainstorming and Potential Canon:* The area north of [[Vostok]] is tentatively invented as a subarctic grassland - like the interior Canadian plains / northern Great Plains - large mammals, cold winters, mammoths - and tentatively assumed to be a place where kenku settled after escaping from Pandar. However, details are vague, at best, and the geography / climate is not set in stone. 

*Needs Development:* None. 

*Intentionally Blank:* The entire region is largely blank on purpose. Any human civilizations here would be highly magic or scattered and small, and not likely to impact other cultures or the grand sweep of history. 

*Adventures:* No adventures have been set in this region.

*Important Places in Staging:* None. The features this far north plausibly have no known names in the southern lands.
%%^End%%

%%^Metadata:names:v1%%
- {name: Far North, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern geography and southern reports about the region; Vimfrost's War is historical backstory.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter, added the explicit name and a minimal name entry; the plain-English regional name needs no pronunciation guide.
- Added a broadly modern POV and temporal-coverage interpretation.
- Corrected “nothern” to “northern,” “particular” to “particularly,” subject agreement in “this region ... is home,” and the missing “of” in “eastern slopes of the Sentinels”; normalized the private-block sentinel to `Campaign:none`.

### Validated judgments
- The deliberately lightly developed region has a useful geographic and rumor-based account; no additional civilization or history was invented.
- `status/cleanup/map` is supported by the static map and the outstanding conversion reminder. The tag and map were preserved.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The “Civilizations and Cultures” paragraph presents kenku settlement only as rumor, whereas [[Kenku#Settlements and Homelands]] establishes that many settled after the Great War in the northern plains east of the Sentinels and north of Vostok. Their exact extent remains uncertain. Candidate: “Many [[Kenku|kenku]] settled in the northern plains east of the [[Sentinel Range]] and north of [[Vostok]] after the [[Great War]]. Outsiders rarely visit these settlements, and the extent of their communities remains a subject of rumor and mystery.” Preserve the unnamed steppe's unsettled physical details rather than treating its tentative geography as established.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Market Magical Items]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 95 - DM Notes]]
%%^End%%
