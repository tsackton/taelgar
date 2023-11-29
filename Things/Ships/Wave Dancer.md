---
headerVersion: 2023.11.25
displayDefaults: {wOrigin: "Home area: <origin>", ruledBy: "<affiliationtitle:t>: <name> <(of )primary>" }
tags: [item/boat]
ancestry: halfling
typeOf: vehicle
typeOfAlias: boat
whereabouts: 
- {type: home, end: 0001, location: Eastern Green Sea, formatSpecifier: ""}
- {type: away, start: 1748-09-30, end: 1748-10-11, location: sailing to Wahacha}
- {type: away, start: 1748-10-12, end: 1748-10-14, location: Wahacha}
---
# The Wave Dancer
>[!info]+ Information
> ([[Halflings|halfling]] boat)
> `$=dv.view("_scripts/view/get_Affiliations")`
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

