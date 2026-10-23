---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Redhammers
dm_owner: none
dm_notes: none
POV: modern
---
# The Redhammers
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"],
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^Metadata:names:v1%%
- {"name": "Redhammers", "language": "Common", "status": "inferred", "notes": "The visible compound follows the convention in [[Dwarves]] and [[Playing a Dwarf]] of rendering clan names in the trade tongue or Common; no Dwarvish original or specific etymology is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern clan identification and membership index; the note makes no narrower dated claims about the clan.
%%^End%%
