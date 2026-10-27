---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: family
ancestry: halfling
name: Strongbones
whereabouts: Tokra
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

A family of halfling innkeepers and merchants, traditionally based in [[Central Dunmar]], most recently [[Tokra]]. 

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
- {"name": "Strongbones", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern family identity and association with Central Dunmar and Tokra; the note does not establish a date for the family’s move.
%%^End%%
