---
headerVersion: 2023.11.25
tags:
  - place
  - status/stub
  - status/check/ai
aliases:
  - Chardonian
name: Chardonian Empire
typeOf: realm
whereabouts: Greater Chardon
dm_owner: tim
dm_notes: important
typeOfAlias: empire
---
# The Chardonian Empire
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Chardonian Empire is a growing realm ruled from the city of [[Chardon]]. Its power rests on the legions, the city’s institutions of learning and magic, and the wealth of the [[chalyte]] trade.

Chardonian historians often date the empire’s rise to the aftermath of the [[War of the Dark Rift]], when Chardon defeated the Shadow Armada and began to extend its authority over neighboring provinces and coasts.

## Territories

- [[Chardon]] (capital)
- The Apporian Provinces of [[Portalia]], [[Cedrano]], and [[Raziolo]] (on [[Apporia|the Apporian Peninsula]])

## Sources

- [[Chardon]]
- [[Apporia]]
- [[Letter from Chardon for Samso on the Umbral Covenant]]

%%needs tons of work, mostly can't pull from existing notes%%

%%% Some notes from GDrive, may be old/wrong
#### Chardon

- Huge city, with significant hinterlands near the mouth of ~MainWestRiver~
    
- Mostly on [[South Bank]]; [[North Bank]] poorer, chalyte refineries on [[North Bank]], power magic item industry in Chardon
    
- Large, anomalous extinct volcano on [[North Bank]]
    
- Heir to imperial Drankor, now capitol of a growing Empire stretching north and south
    
- Great Library major center of learning and magic in Taelgar
    
- Hinterlands small farms in river valley and south to forest edge and the hills around small river
%%

%%^Campaign:None%%
### Places in Chardonian Empire
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%

%%^Campaign:none%%

## DM notes

%% AI note: This page is intentionally conservative; a lot of existing empire-level detail lives in campaign and staging materials. %%

%% DM sources: _DM_/Staging/Mitus Verina Auratan Revised; _DM_/_Dunmari Frontier/*; _DM_/Secret Worldbuilding/* %%

%%^End%%
