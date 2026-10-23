---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group]
typeOf: clan
ancestry: dwarven
name: Silverspark Clan
dm_owner: tim
dm_notes: none
POV: modern
---
```taelgar-header
```

The Silversparks are a historically minor dwarven clan from [[Nardith]]. The most prominent member of the clan, [[Nora Silverspark]], was a decorated warrior, but vanished in DR 1575 with the rest of the dwarves who had traveled north to aid refugees still trapped in [[Ardith]] after the [[Great War]]. Subsequent to her disappearance, the clan fell into obscurity. 

%%^Date:1749-05-01%%
More recently, the clan has seen renewed prominence due to their association with the famous dwarven hero [[Riswynn|Riswynn Brawnanvil]], particularly through [[Kethra|Kethra Silverspark]].
%%^End%%

###  Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^Metadata:names:v1%%
- {name: Silverspark Clan, language: Common, status: inferred, notes: "Transparent Common rendering; [[Kethra]] identifies Silverspark as a translated dwarven family name."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern clan history after the DR 1575 disappearance; the existing Date block separately introduces renewed prominence from DR 1749-05-01.
%%^End%%
