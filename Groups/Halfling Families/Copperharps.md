---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: family
ancestry: halfling
name: Copperharps
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

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
- {"name": "Copperharps", "language": "Common", "status": "documented", "notes": "[[Languages]] explicitly names Copperharps as a Common name."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern reference identifying the Copperharps as a halfling family; no particular household, leadership, or date-dependent state is asserted.
%%^End%%
