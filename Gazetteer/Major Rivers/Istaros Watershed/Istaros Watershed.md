---
headerVersion: 2023.11.25
tags: [place, status/stub]
campaignInfo: []
name: Istaros Watershed
typeOf: region
whereabouts:
- { type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: color
---
# The Istaros Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% overview page for Istaros watershed, needs some basic summaries and such %%


%%^Campaign:None%%
### Places in the Istaros Watershed
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%