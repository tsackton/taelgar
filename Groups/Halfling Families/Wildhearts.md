---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {defArt: the}
name: Wildhearts
typeOf: family
ancestry: halfling
dm_notes: none
dm_owner: none
---
# The Wildhearts
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Wildhearts are a halfling family based in the [[Eastern Green Sea]]. Two brothers, [[Corrin Wildheart]] and [[Lerry Wildheart]], are crew on the [[Wave Dancer]]. 

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