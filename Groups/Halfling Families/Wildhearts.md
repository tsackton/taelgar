---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: family
ancestry: halfling
name: Wildhearts
dm_owner: none
dm_notes: none
POV: 1740s
---
# The Wildhearts
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Wildhearts are a halfling family based in the [[Eastern Green Sea]]. Two brothers, [[Corrin Wildheart]] and [[Lerry Wildheart]], are crew on the [[Wave Dancer]]. 

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
- {"name": "Wildhearts", "language": "Common", "status": "inferred", "notes": "The transparent English display form follows the Common-name convention in [[Languages]]."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the late-1740s reference to the Wildheart family and the two brothers serving aboard Wave Dancer; no later crew changes are established here.
%%^End%%
