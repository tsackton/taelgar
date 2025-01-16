---
headerVersion: 2023.11.25
displayDefaults: {partOf: '<typeof:AU> of <partof>', boxInfo: ''}
tags: [organization, status/cleanup/text]
typeOf: regiment
partOf: Army of the West
dm_notes: important
dm_owner: mike
---
# The Dunfry Regiment
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
> A regiment of the [[Army of the West]], the [[Sembaran Army]], [[Sembara]]

%% status/update -> status/check/mike %%

%% Significant events of undead attack here in my DM notes only ; need incorporation %

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

