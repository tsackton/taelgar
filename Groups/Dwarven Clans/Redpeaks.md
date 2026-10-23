---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Redpeak Clan
whereabouts: Darba
dm_owner: none
dm_notes: none
POV: modern
---
# The Redpeak Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Redpeaks are a dwarven clan, prominent in [[Darba]], with ties to [[Tharn Todor]] and [[Nardith]]. The Redpeaks were among the clans with connections to the [[Dwarven Outpost (Raven's Hold)|dwarven outpost near Raven's Hold]] before the [[Great War]]. After fleeing to [[Nardith]] with many others, they spread west through their trade connections and now maintain estates in Darba’s dwarven quarter.

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```


%%^Metadata:names:v1%%
- {name: Redpeak Clan, language: Common}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern account of the clan's presence in Darba and regional ties, with selected Great War migration history.
%%^End%%
