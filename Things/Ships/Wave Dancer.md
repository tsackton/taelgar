---
headerVersion: 2023.11.20
displayDefaults: {"whereaboutsOrigin": "Home area: <loc>", "secondaryInfo": "(<rarity> <ancestry> <subtypeof>)"}
tags: [item/boat]
typeOf: vehicle
subTypeOf: boat
whereabouts: 
- {type: home, end: 0001, location: Eastern Green Sea}
- {type: away, start: 1748-10-12, end: 1748-10-14, location: Wahacha}
---
# The Wave Dancer
>[!info]+ Information
> (boat)
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A halfling ship plying the trade routes of the eastern Green Sea, regularly visiting [[Praznitsky]], [[Wahacha]], [[Quanyi]], and [[Medju]].  
## Crew
[[Wella Brightmoon]], captain and matriach of the family
[[Rose Brightmoon]], musician and Wella's wife
[[Pearl Brightmoon]], first mate and captain of the guard
[[Corrin Wildheart]], navigator
[[Lerry Wildheart]], quartermaster

%%^Campaign:None%%
```dataviewjs
const { util } = customJS
dv.table(["Person", "Current", "Known to DuFr"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation("Wave Dancer", f.file.frontmatter, false))
				.map(b => [util.getName(b.file.name), util.getLoc(b.file.frontmatter), util.isKnownToParty(b.file.name, b.file.frontmatter, "dufr", true, true)]))
```
%%^End%%

![[wave-dancer-1.png|500]]

