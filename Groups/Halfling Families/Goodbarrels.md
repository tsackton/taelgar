---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
name: Goodbarrels
typeOf: family
ancestry: halfling
dm_notes: none
dm_owner: none
---
# The Goodbarrels
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Goodbarrels are widely distributed halfling trading family, scattered across the [[Western Green Sea]] and the roads of northern [[Sembara]], with a significant presence in [[Tollen]] as well. The most famous Goodbarrel is undoubtedly [[Wellby|Wellby Goodbarrel]], a prominent member of the [[Dunmar Fellowship]]. 

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
