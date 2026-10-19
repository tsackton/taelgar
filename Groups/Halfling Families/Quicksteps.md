---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: family
campaignInfo: []
name: Quicksteps
dm_owner: none
dm_notes: none
POV: modern
---
# The Quicksteps
>[!info]+ Information  
> A family  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% nothing invented %%

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
- {"name": "Quicksteps", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern family reference; no founding date or dated family history is established.
%%^End%%
