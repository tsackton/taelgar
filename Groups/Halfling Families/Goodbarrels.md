---
headerVersion: 2023.11.25
tags: [organization, status/stub]
displayDefaults: {defArt: the}
campaignInfo: []
name: Goodbarrels
typeOf: family
ancestry: halfling
dm_notes: color
dm_owner: tim
---
# The Goodbarrels
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% some Wellby backstory notes to incorporate %%

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