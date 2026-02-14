---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {defArt: the}
name: Tealeafs
typeOf: family
ancestry: halfling
dm_owner: tim
dm_notes: none
---
# The Tealeafs
>[!info]+ Information  
> A [[Halflings|halfling]] family  
> `$=dv.view("_scripts/view/get_Affiliations")`

The Tealeafs are a halfling trading family based in the [[Greater Dunmar]] area. They were a rich and prominent family of long-distance traders,  known for long overland caravan circuits between [[Chardon]], [[Songara]], [[Tokra]], and [[Eastern Dunmar]], in first decades of the DR 1700s. 

In DR 1737 the Tealeaf caravan was attacked by [[Agata]] and [[Dustthorn Horde]] orc raiders. [[Garret Tealeaf]], the patriarch of the family, was captured, and the family wealth was scattered among the survivors, who turned to shorter, safer, and less profitable routes. 

Garret was freed eleven years later, in DR 1748, by the [[Dunmar Fellowship]], though was left changed by his imprisonment, and the family has not recovered its former wealth and prominence. 

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%
