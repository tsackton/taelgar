---
headerVersion: 2023.11.25
tags: [place]
name: Beury
typeOfAlias: village
typeOf: settlement
whereabouts: Manor of Beury
population: 492
pronunciation: BUH-ree
dm_notes: none
dm_owner: mike
---
# Beury
*(BUH-ree)*
>[!info]+ Information  
> pop. 492  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A large farming village six miles downriver of [[Cleenseau]] and the principle (and only) village in the [[Manor of Beury]]. There are about ninety sturdy houses here, many of which predate the [[Third Hobgoblin War (Sembara)|hobgoblin wars]], although the village was abandoned for several years in the 1640s. 

The houses are arranged in two tight concentric circles around a main square, where the one-story wooden manor house sits, as does the slightly larger stone temple of [[The Father]], the blacksmith, and two wells. The entire village, save for the small inn and mill (see below), fit within a thousand-foot diameter circle. 

Beyond the second circle of houses, straddling the [[Great South Road]] is a nameless inn, usually just called "the inn in Beury" (or sometimes, jokingly, "Bee's Rest"). The inn is more of a stable and resting spot for caravans before crossing the [[East Bog|boggy wetlands]] to [[Dallet]] than a proper inn, and the food and drink are notably lacking. Many caravans resting here simply camp in the yard. Across the road and a few dozen feet from the inn is a sturdy stone millhouse.

A small market is held in the caravan yard once a week, which attracts some of the people from [[Asineau]] and [[Ganboa]], especially for iron goods.

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