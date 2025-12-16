---
headerVersion: 2023.11.25
tags: [organization]
name: Silverspark Clan
typeOf: clan
ancestry: dwarven
dm_notes: none
dm_owner: tim
---
# The Silverspark Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Silversparks are a historically minor dwarven clan from [[Nardith]]. The most prominent member of the clan, [[Nora Silverspark]], was a decorated warrior, but vanished in DR 1575 with the rest of the dwarves who had traveled north to aid refugees still trapped in [[Ardith]] after the [[Great War]]. Subsequent to her disappearance, the clan fell into obscurity. 

%%^Date:1749-05-01%%
More recently, the clan has seen renewed prominence due to their associated with the famous dwarven hero [[Riswynn|Riswynn Brawnanvil]], particularly through [[Kethra|Kethra Silverspark]].
%%^End%%

### Current and Former Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%