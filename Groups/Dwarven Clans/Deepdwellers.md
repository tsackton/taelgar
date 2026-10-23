---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Deepdweller Clan
dm_owner: none
dm_notes: none
POV: modern
---
# The Deepdweller Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Deepdwellers are a dwarven clan originally from the lost kingdom of [[Enderra]], now mostly living around [[Apporia]]. 

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^Metadata:names:v1%%
- {"name": "Deepdweller Clan", "language": "Common", "status": "documented"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference prose about the clan’s Enderran origin and present Apporian distribution; no precise migration date or narrower period is established.
%%^End%%
