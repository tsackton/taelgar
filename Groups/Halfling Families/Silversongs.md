---
headerVersion: 2023.11.25
tags: [organization/family]
displayDefaults: {defArt: the}
typeOf: family
ancestry: halfling
name: Silversongs
affiliations:
- {place: Emerald Song, type: leader, title: Owners}
---
# The Silversongs
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

A halfling family of traders and sailors based in the [[Nevos Sea]]. 

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