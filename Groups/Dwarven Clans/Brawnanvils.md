---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
name: Brawnanvil Clan
typeOf: clan
ancestry: dwarven
dm_notes: none
dm_owner: none
---
# The Brawnanvil Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Brawnanvils are a moderately prominent dwarven clan of [[Tharn Todor]], with roots in the lost kingdom of [[Ardith]]. Before and during the [[Great War]], the clan had a major presence at the [[Dwarven Outpost (Raven's Hold)|dwarven outpost near Raven's Hold]], an iron mine, forge, and trading post linking dwarves from the southern [[Sentinel Range|Sentinels]] with the Dunmari. 

By far the most famous member of the Brawnanvil Clan is [[Riswynn]], companion of the [[Dunmar Fellowship]], hero of the [[War of the Cloak]], champion of the [[Bahrazel]], and the bearer of the [[Crown of Purity]]. 

### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"],
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
