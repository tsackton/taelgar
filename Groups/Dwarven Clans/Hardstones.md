---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Hardstone Clan
dm_owner: none
dm_notes: none
whereabouts: Tokra
POV: modern
---
```taelgar-header
```

The Hardstones are a prominent dwarven clan in [[Tokra]], known primarily for their long-standing association with the [[Archives|Tokra Archives]]. They settled in Tokra in the years after the [[Fire War]].

The clan has traditionally worked as architects and builders for the Archives, but also generally manages the physical infrastructure of the building. They are also known, at times, to work some minor runic magic to protect scrolls and mend damage. In some cases, they also make magical runic imprints of valuable texts, allowing copies to be sent to [[Nayahar]], [[Darba]], or [[Chardon]] without transcription errors.

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^Metadata:names:v1%%
- {"name": "Hardstone Clan", "language": "Common"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference description of the clan’s continuing work at the Tokra Archives, with post-Fire-War settlement as historical background.
%%^End%%