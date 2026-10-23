---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group]
typeOf: clan
ancestry: dwarven
name: Brawnanvil Clan
dm_owner: none
dm_notes: none
POV: 1749
---
# The Brawnanvil Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Brawnanvils are a moderately prominent dwarven clan of [[Tharn Todor]], with roots in the lost kingdom of [[Ardith]]. Before and during the [[Great War]], the clan had a major presence at the [[Dwarven Outpost (Raven's Hold)|dwarven outpost near Raven's Hold]], an iron mine, forge, and trading post linking dwarves from the southern [[Sentinel Range|Sentinels]] with the Dunmari. 

By far the most famous member of the Brawnanvil Clan is [[Riswynn]], companion of the [[Dunmar Fellowship]], hero of the [[War of the Cloak]], champion of the [[Bahrazel]], and the bearer of the [[Crown of Purity]]. 

### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"],
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^Metadata:names:v1%%
- {"name": "Brawnanvil Clan", "language": "unknown", "notes": "[[Dwarves]] lists Brawnanvil among clan names and explains that these forms are rendered in the trade tongue; the original dwarven form is not recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1749 clan overview after Riswynn became bearer of the Crown of Purity, alongside the clan's older Ardith and Raven's Hold roots; the article does not establish her Crown-bearing status before May 1749.
%%^End%%
