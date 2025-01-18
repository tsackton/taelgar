---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {partOf: "", boxInfo: "", defArt: "the"}
typeOf: family
whereabouts: Ainwick
aliases: [Bybet]
dm_owner: none
dm_notes: none
---
# The Bybets
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A minor manorial family.

%% No details exist; the husband of a major NPC is of this family but no idea as to why he left his family's main stomping ground %%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2Fr> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%