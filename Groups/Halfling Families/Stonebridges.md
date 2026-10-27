---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the, partOf: ""}
tags: [group]
typeOf: family
ancestry: halfling
campaignInfo: null
created: 1200
name: Stonebridges
dm_owner: mike
dm_notes: color
POV: modern
---
```taelgar-header
```

%% Frontmatter note for created: 1200
# date is approximate
%%

A family of halflings who have lived in [[Cleenseau]] since at least the 1200s, and have run the Crossroads Inn since its founding. More sedentary than most halflings and deeply committed to the [[Cleenseau Region]]. 

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

%% Notes
No real background made up, but see [[Cleenseau History Notes]] - they have been involved in most of the major events. No reason for them to be so tied to the land here had been invented
%%

%%^Metadata:names:v1%%
- {"name": "Stonebridges", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern account of the family’s enduring connection to Cleenseau and the Crossroads Inn, with origins described only approximately as at least the DR 1200s.
%%^End%%
