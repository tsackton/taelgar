---
headerVersion: 2023.11.25
tags: [group]
displayDefaults: {boxInfo: "<ancestry:UA> <subtypeof>"}
name: Aatmaji dynasty
typeOf: family
subTypeOf: dynasty
ancestry: Dunmari
dm_owner: tim
dm_notes: important
---
# The Aatmaji Dynasty
>[!info]+ Information  
> A [[Dunmar|Dunmari]] dynasty  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% have a full list of Samraats of this dynasty in DM notes FWIW%%

The first ruling dynasty of [[Dunmar]], founded by [[Bhishma]]. 

%%^Campaign:None%%
### Historical Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%