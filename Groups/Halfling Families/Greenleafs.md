---
headerVersion: 2023.11.25
tags: [organization/family]
displayDefaults: {defArt: the, partOf: "" }
campaignInfo: []
name: Greenleafs
typeOf: family
ancestry: halfling
---
# The Greenleafs
>[!info]+ Information
> A [[Halflings|halfling]] family
> `$=dv.view("_scripts/view/get_Affiliations")`

%% no information exists about this family; only created members were two brothers traveling for unknown reasons%%
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