---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
campaignInfo: []
name: Redpeaks
typeOf: clan
ancestry: dwarven
whereabouts: Darba
dm_notes: none
dm_owner: none
---
# The Redpeaks
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Redpeaks are a dwarven clan, prominent in [[Darba]], with ties to [[Tharn Todor]] and [[Nardith]]. The Redpeaks were among the clans with connections to the [[Dwarven Outpost (Raven's Hold)|dwarven outpost near Raven's Hold]] before the [[Great War]]; since they fled with many others to [[Nardith]], they have spread west with trade connections, and now maintain estates in the Darba's dwarven quarter.

###  Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

