---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
name: Boulderbeard Clan
typeOf: clan
ancestry: dwarven
dm_notes: none
dm_owner: none
---
# The Boulderbeard Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Boulderbeards are one of several founding clans of the kingdom of [[Nardith]], having fled the fall of the [[Ardith]] during the [[Great War]] to start a new life in a safer place. The Boulderbeards were among the prominent clans that occupied the [[Dwarven Outpost (Raven's Hold)]] before the [[Great War]].

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%