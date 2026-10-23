---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Boulderbeard Clan
dm_owner: none
dm_notes: none
POV: modern
---
# The Boulderbeard Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Boulderbeards are one of several founding clans of the kingdom of [[Nardith]], having fled the fall of [[Ardith]] during the [[Great War]] to start a new life in a safer place. The Boulderbeards were among the prominent clans that occupied the [[Dwarven Outpost (Raven's Hold)]] before the [[Great War]].

%%^Date:1747-12-01%%
Outside of dwarven circles, they are best known through [[Adrik|Adrik Boulderbeard]], one of the heroes of the [[Battle of Voltara]] and a founding member of the [[Silver Tempests]]. 
%%^End%%

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^Metadata:names:v1%%
- {"name": "Boulderbeard Clan", "language": "Common"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern clan overview after Adrik's role in the DR 1747 Battle of Voltara, with the Great War and the founding of Nardith as historical background; it does not establish the clan's complete intervening history.
%%^End%%
