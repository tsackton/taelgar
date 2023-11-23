---
headerVersion: 2023.11.20
tags: [organization/family]
displayDefaults: {definitiveArticle: the, secondaryInfo: ""}
campaignInfo:
name: Stonebridges
typeOf: family
ancestry: halfling
# date is approximate
created: 1200
---
# The Stonebridges
>[!info]+ Information
> `$=dv.view("_scripts/view/get_PageDatedValue")`

A family of halflings who have lived in [[Cleenseau]] since at least the 1200s, and have run the Crossroads Inn since its founding. More sedentary than most halflings and deeply committed to the [[Cleenseau Region]]. 

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file.frontmatter))
				.sort(f => f.born)
				.map(b => [util.getName(b.file.name), util.getLoc(b.file.frontmatter)]))
```
%%^End%%

%% Notes
No real background made up, but see [[Cleenseau History Notes]] - they have been involved in most of the major events. No reason for them to be so tied to the land here had been invented
%%