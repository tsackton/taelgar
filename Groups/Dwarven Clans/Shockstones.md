---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Shockstone Clan
whereabouts: Zarkandur
dm_owner: none
dm_notes: none
POV: modern
---
# The Shockstone Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Shockstones are one of the most prominent dwarven clans in [[Am'khazar]], and the de facto rulers of [[Zarkandur]]. 

%%^Date:1747-12-01%%
The clan is best known, at least outside dwarven circles, through [[Brelith|Brelith Shockstone]], a priest of the [[Bahrazel]] and hero of the [[Battle of Voltara]]. 
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
- {name: Shockstone Clan, language: Common}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of the clan's standing in Am'khazar and Zarkandur, referring retrospectively to Brelith's role in the Battle of Voltara.
%%^End%%
