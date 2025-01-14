---
headerVersion: 2023.11.25
tags: [organization/family]
displayDefaults: {defArt: the}
campaignInfo: []
name: Quicksteps
typeOf: family
---
# The Quicksteps
>[!info]+ Information  
> A family  
> `$=dv.view("_scripts/view/get_Affiliations")`


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