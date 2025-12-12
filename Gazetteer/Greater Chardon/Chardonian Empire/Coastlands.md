---
headerVersion: 2023.11.25
displayDefaults: {defArt: "the"}
tags: [place, status/check/name]
whereabouts: 
- {type: home, location: Chardonian Empire}
typeOf: region
dm_notes: none
dm_owner: none
---
# The Coastlands
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Coastlands is the colloquial name for the coastal region of the Chardonian Empire, stretching from the borders of [[Portalia]] in the south to the [[~Mawakel Border Mountains~]] in the north, and bounded inland by the [[~Lake Valandros Hills~]] and the [[~Chardon Hills~]]. 

The Low Coast, the portion of coastlands south of [[Chardon]], is hot and dry in the summer, with mild winters and extensive coastal wetlands. 

The Upper Coast, the portion of the coastlands north of [[Chardon]], is rich agricultural land, with many rivers and mild weather, sandy beaches and small stands of ancestral forests among fields of wheat. The land here slopes gently up to the [[~Lake Valandros Hills~]]. 

Much of the Upper Coast was occupied by [[Hobgoblins|hobgoblins]] during the [[Blood Years]]. 

Five major rivers, and several smaller ones, flow through the coastlands. From south to north, they are:
- [[Dashun]]
- [[Zar]]
- [[Corvessa]]
- [[Sevros]]
- [[Breakrock]]

## Places in the Coastlands
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```


%%^Campaign:none%%

See: [[Hobgoblin Movements After Cha'Mutte]] and [[West Coast History Framework]] for historical context. 

Sandy beaches, leading to land of rivers and farms and pastures, breadbasket of Chardon (Upper Coast)
Geography of Low Coast less developed. 

Relatively few big cities? perhaps one or two in the north? Not sure yet about urbanization in this area. Open to develop. 

Generally part of the "core" of the Chardonian Empire and generally Chardonian rule is popular here. 

%%^End%%
