---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: family
ancestry: halfling
name: Brightmoons
dm_owner: none
dm_notes: none
POV: modern
---
# The Brightmoons
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Brightmoons are a seafaring halfling clan, scattered across the [[Eastern Green Sea]]. 

%%^Campaign:none%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Brightmoons", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern identification of the seafaring family and its distribution across the Eastern Green Sea; no particular leader or voyage is asserted.
%%^End%%
