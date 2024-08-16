---
headerVersion: 2023.11.25
tags: [organization, status/needswork/wip]
displayDefaults: {defArt: the}
campaignInfo: []
name: Hardstones
typeOf: clan
ancestry: dwarven
---
# The Hardstones
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`


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