---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Redhammer Clan
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```


%%^Metadata:names:v1%%
- {"name": "Redhammer Clan", "language": "Common"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern clan identification and membership index; the note makes no narrower dated claims about the clan.
%%^End%%
