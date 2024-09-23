---
headerVersion: 2023.11.25
tags: [organization/family]
displayDefaults: {defArt: the, partOf: ""}
campaignInfo:
name: Stonebridges
typeOf: family
ancestry: halfling
# date is approximate
created: 1200
dm_notes: color
dm_plans: no
---
# The Stonebridges
>[!info]+ Information
> A [[Halflings|halfling]] family
> `$=dv.view("_scripts/view/get_PageDatedValue")`

A family of halflings who have lived in [[Cleenseau]] since at least the 1200s, and have run the Crossroads Inn since its founding. More sedentary than most halflings and deeply committed to the [[Cleenseau Region]]. 

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

%% Notes
No real background made up, but see [[Cleenseau History Notes]] - they have been involved in most of the major events. No reason for them to be so tied to the land here had been invented
%%