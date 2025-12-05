---
headerVersion: 2023.11.25
tags: [place, status/wip]
displayDefaults: {defArt: 'the' }
typeOf: region
whereabouts: [{type: home, location: Taelgar, linkText: "in" }]
dm_owner: none
dm_notes: none
---
# The Central Highlands
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

```leaflet 
id: region-map-taelgar
image: [[region-central-highlands.png]] 
bounds: 
- [0,0]
- [2930, 1876]
height: 700px  
width: 500px
lat: 1500
long: 900
minZoom: -2
maxZoom: 0
defaultZoom: -2
unit: miles 
scale: 1
draw: false
darkMode: false
markerTag: location-source
```

## Topography and Major Features
_See more: {links}_

%% Mountains, mostly - organizing features:
Forests: [[Elderwood]] and [[Crimson Forest]]
Sentinels: [[Sentinel Range]]
[[Myraeni Gap]] and foothills
Some river headwaters to identify
%%

{descriptive text of topography and major features}
## Civilizations and Cultures
_See more: {links}_

{descriptive text of civilizations and cultures}
%%
Elves: [[Ainumarya]] (now mostly or entirely gone?)
Dwarves: [[Khatridun]] [[Nidzahar]] and [[Am'khazar]] of the dwarves
Lizardfolk: None
Humans: [[Deno'qai]]
Stoneborn:  significant settlement around [[Kunda]]?
Hobgoblins: remains of [[Shattered Ice Clan]] in the southern sentinels
Dangerous Wildernesses: Yes
%%

## Climate

{descriptive in world text about climate}

%%^Campaign:None%%

{real world climate analogs and inspiration}

%%^End%%

## Major Historical Eras
_See more: {links}_

{descriptive text of major era}

%%^Campaign:None%%
## DM Notes and Meta
_See also: [[Places in the Central Highlands]]_

*Canonical Development and Constraints:* Three major extant dwarven kingdoms of the Sentinels are fairly well established, although many details remain to be invented. The elven kingdoms of [[Ainumarya]] are canonical, but not well established and potentially a source of some mystery, although once it was the thriving heartland of elves on Taelgar. In general this region has few humans, with only the [[Deno'qai]] a major developed culture. The general geography and climate of this area is well established. 

*Brainstorming and Potential Canon:* [[Kunda]] is a canonical Stoneborn settlement in the southern Sentinels, and this region is likely has significant Stoneborn communities, but details are not canonical or well-established in game. The existence of Underdark-like deep caverns below the Sentinels is canonical, but not fully developed (see: [[The Underdark]]). 

*Needs Development:*  Although the dwarven kingdoms have been invented in broad strokes, further invention around details, settlements, and history would be valuable. A more fully-fleshed out development of [[Deno'qai]] culture and settlement in this area would also be valuable. The history of the elves in this region could use more thought, although the post-Great War fate of [[Ainumarya]] is intentionally left somewhat mysterious. 

*Intentionally Blank:* [[Urlich Pass]], now a region of significant devastation, is canonically important as the site of Cha'mutte's defeat, but why it was important is unclear, although probably has something to do with being a locus of the power of the Firstborn, and the details are left intentionally vague. The devastation of [[Urlich Pass]] and the the Underdark are intentionally blank slates, and both may plausibly feature in a future [[Cleenseau Campaign]] arc. Exactly what happened to the elves after the [[Great War]] is left intentionally blank, although canonically there are many fewer of them than before the Great War. 

*Adventures:* The Dunmari Frontier campaign Elderwood arc occurred in this region, as did the short adventure to Hralgar's Palace. The Great Library dwarven kingdom arc also occurred in this region, including passing through a Deno'qai village from early days of Deno'qai development ([[Raha]]), and significant invention around [[Am'khazar]]. The [[Great War Campaign]] involved the final battle ([[Battle of Urlich Pass]]) against [[Cha'mutte]] at or near [[Urlich Pass]], and also included a short arc involving a hidden forest ([[Valley of the Hidden Forest]]) with strange magic where Rai first met Dimitaur. 

*Important Places in Staging:* The Deno'qai villages from the Elderwood arc ([[~Bek'eni village~]], [[~Te'kula village~]]) could use names. 
%%^End%%

---

%% OLD BELOW %%
## Overview

The Central Highlands Region is a land of contrasts, from vast forests dominated by ancient elven trees, to the high, inaccessible peaks of the northern [[Sentinel Range|Sentinels]] where only [[Stoneborn]] and frost [[Giants]] can survive. Few people call this region their home: the [[Deno'qai]], who live mostly in small villages among the forests hugging the western foothills of the [[Sentinel Range|Sentinels]], and the [[Elves]], who once could be found throughout the woodlands of [[Ainumarya]], and the main inhabitants. The [[Sentinel Range]] creates a barrier to ...
## Boundaries

The Central Highlands includes the [[Sentinel Range]], as well as the forests along the western slopes of the mountains, and the east bank and upper watershed of the [[~North Nahadi River~]].

- To the north, this region is bordered by the cold polar regions of the [[Far North]]. 
- To the east, this region is bordered by the [[Highland Kingdoms]], the [[The Western Marches]] of [[Sembara]], and the [[Refounded Alliance of Aurbez]]. 
- To the south, this region is bordered by the plains of [[Dunmar]]. 
- To the west, this region is bordered by the [[Chardonian Empire]], the northern hinterlands of the [[Chardonian Empire]], and the coastal north. 

## Major Features

%% TO DO
Some of this description should be ported to individual pages, with real world details in comments
Update boundaries of what is considered "once part of Ainumarya" in forest notes
%%

- [[Sentinel Range]]: The [[Sentinel Range]] is the dominate feature of the Central Highlands Region, stretching 2300 miles from volcano mountains of the former kingdom of [[Pandar]] in the north, to the northern foothills of the Dunmari plains in the south. 
	- The northern section, from roughly [[Pandar]] south past the [[Forest of Nightmares]] to the area northeast of the [[Blackwater Fens]], is snowy, rocky, and volcanic, marked by pine forests on the western slopes and long, bitter winters. 
		- ***Real world analogs:*** This region is at approx. 52 degrees north, and probably has some similarities with the Canadian Rockies, especially Banff and Jasper national parks, including the flat plains to the east of the mountains (int he [[Far North]]). The volcanic mountains of [[Pandar]] share some similarities with the Pacific Ring of Fire, but with a much more magical vibe, and less moderating coastal influence on climate. 
	- The middle section, roughly the area starting west of [[Zimkova]] and running south to the desolation west of the [[Western Marches]], is rocky and very tall, with extensive underground development associated with the [[Dwarven Kingdoms]], and more dangerous things. These are stereotypical high mountains. 
		- ***Real world analogs:*** This region stretches from roughly 40 degrees N to 50 degrees N. This is a classic high mountain range, sharing features with the northern Rockies, the Alps, and Patagonia, but even the tallest peaks are unlikely to reach the heights of something like the Himalayas in the real world. 
	- The southern section, covering the area that was once the dwarven kingdom of [[Ardith]], from roughly west of [[Duchy of Maseau|Maseau]] or [[Refounded Alliance of Aurbez]] to the end of the [[Sentinel Range]] north of [[Dunmar]], is full of high, barren peaks that rise sharply from the plains, and is generally dry, with arid regions to the west and south. 
		- ***Real world analogs:*** This is warmer and further south, from approx. 34 degrees N to 38 degrees N. Probably shares some similarities with the dry Andes, or possibly some of the mountains in central Asia, such as Hindu Kush or Pamir Mountains. 
	- The northern and middle sections are separated by a region of lower hills, a more habitable region with mixed forests and rocky slopes, but relatively easy passage between the west and east. This is likely the route by which the early northerners crossed into the Sembaran highlands. 
		- ***Real world analogs***: Perhaps somewhat similar to something like the less mountainous Yellowstone / Montana, or even perhaps the Whites. 
	- The middle and southern sections are separated by the desolate of Urlich, created by [[Cha'mutte]]'s death. What this actually looks like is currently unknown, but it is dangerous and contains both random isolated mountains and vast chasms, and safe travel is impossible, not only because of dangerous inhabitants but because of unstable terrain. 
		- ***Real world analogs:*** None, although perhaps some bits of Mordor could be a reasonable mental model. 
	- Passes: the [[Sentinel Range]] is easily crossable only in a few places. 
		- To the north, the gap between the middle section and the northern section is traversable in all seasons, but lightly settled; the northern section itself is extremely inhospitable in the highest peaks.
		- The middle section has passes around [[~High Horn~]], west of the [[Highland Kingdoms]], and in the area west of the [[Western Marches]]. But the latter was disrupted by [[Cha'mutte]]'s death and is no longer considered passable. 
		- The south section has several routes that cross between the [[Refounded Alliance of Aurbez]] and northern [[Dunmar]]. 
- [[Ainumarya]]: A vast forest in the foothills and lowlands west of the [[Sentinel Range|Sentinels]], that stretches from the [[Elderwood]] in the south to the [[Crimson Forest]] in the north. Historically a major center of elvish civilization. Most of this region is a dominated by huge conifers and a rich ecosystem. 
	- ***Real world analogs:*** Temperate rainforests, especially the forests of the Pacific Northwest, are probably the best model, albeit with more magic. 
- [[Forest of Dreams]]: North of [[Ainumarya]] is the [[Forest of Dreams]], clinging to the western slopes of the [[Sentinel Range|Sentinels]] east of the [[Erbalta Plains]] and the [[Blackwater Fens]], and spreading west along the foothills of [[Pandar]]. This forest is cooler and dried than [[Ainumarya]], with cold winters and significant snow at higher elevations. 
	- ***Real world analogs:*** Temperate coniferous forest, especially the pine forests of western Canada and the interior Rockies, and classic mixed forests of the Alps. The lowlands north of the [[Blackwater Fens]] are probably more like temperate broadleaf and mixed forests. 


%% comments
- climatically, Ainumarya probably shouldn't be a temperate rainforest (too far from the coast), but the vibe is very much coastal redwoods, high producitivity; so this is a good place for elven magic, perhaps a high density of feywild connections brings rain and moisture. The mountains can also produce a rain shadow effect but it is very far inland for coastal moisture in a "normal earth" world, as least as understand it. But perhaps if the Sierras didn't exist, Utah would be a rainforest?
- mountain passes: for worldbuilding reasons it is pretty important that Sembara - Chardon trade was once easy via Urlich but is now impossible, more or less, except via the dwarves as an intermediary. need to figure out the deal with High Horn, and also think a little bit about how to make it feasible that trade does not cross; presumably part is just the mountains are quite high and thus picking your way through is slow. Drankor presumably built roads but these would have largely connected via Urlich. 
%%

## Climate

The region is climatically dominated by the Sentinel Range, which forms a barrier between the east and west of Taelgar. Entirely inland, this region has a largely [continental climate](https://geodiode.com/climate/continental), generally with balanced rainfall or with wet winters and dry summers at the lower elevations. At higher elevations, the climate is temperate [highlands](https://geodiode.com/biomes/highlands), with the highest peaks covered in ice and snow year round.

***Real world analogs:***
- Mountains of the Pacific Northwest, which have a similar north-south orientation, high peaks, and roughly equivalent latitude
- Canadian Rockies, which mirror the northernmost section of the Sentinel Range