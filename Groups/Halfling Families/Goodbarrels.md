---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: family
ancestry: halfling
name: Goodbarrels
dm_owner: none
dm_notes: none
POV: 1740s
---
# The Goodbarrels
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Goodbarrels are a widely distributed halfling trading family, scattered across the [[Western Green Sea]] and the roads of northern [[Sembara]], with a significant presence in [[Tollen]] as well. The most famous Goodbarrel is undoubtedly [[Wellby|Wellby Goodbarrel]], a prominent member of the [[Dunmar Fellowship]].

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
- {"name": "Goodbarrels", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1740s account of the family, with Wellby already prominent in the Dunmar Fellowship; earlier and later family prominence is not established.
%%^End%%
