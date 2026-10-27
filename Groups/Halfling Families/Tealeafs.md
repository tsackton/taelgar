---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: family
ancestry: halfling
name: Tealeafs
dm_owner: tim
dm_notes: none
POV: modern
---
```taelgar-header
```

The Tealeafs are a halfling trading family based in the [[Greater Dunmar]] area. They were a rich and prominent family of long-distance traders,  known for long overland caravan circuits between [[Chardon]], [[Songara]], [[Tokra]], and [[Eastern Dunmar]], in the first decades of the DR 1700s.

In DR 1737 the Tealeaf caravan was attacked by [[Agata]] and [[Dustthorn Horde]] orc raiders. [[Garret Tealeaf]], the patriarch of the family, was captured, and the family wealth was scattered among the survivors, who turned to shorter, safer, and less profitable routes. 

Garret was freed eleven years later, in DR 1748, by the [[Dunmar Fellowship]], though he was left changed by his imprisonment, and the family has not recovered its former wealth and prominence.

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
- {"name": "Tealeafs", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern trading-family reference with selected DR 1737 and DR 1748 history; the post-rescue account does not establish when or whether the family later regained its former prominence.
%%^End%%
