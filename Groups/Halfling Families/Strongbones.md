---
headerVersion: 2023.11.25
tags: [organization/family]
displayDefaults: {defArt: the}
campaignInfo: []
name: Strongbones
typeOf: family
ancestry: halfling
whereabouts: Tokra
---
# The Strongbones
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A family of halfling innkeepers and merchants, traditionally based in [[Central Dunmar]], most recently [[Tokra]]. 

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