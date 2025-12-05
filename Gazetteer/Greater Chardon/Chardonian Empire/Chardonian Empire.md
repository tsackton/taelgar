---
headerVersion: 2023.11.25
tags: [place, status/stub]
aliases: [Chardonian]
name: Chardonian Empire
typeOf: realm
whereabouts: Greater Chardon
dm_owner: tim
dm_notes: important
---
# The Chardonian Empire
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

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