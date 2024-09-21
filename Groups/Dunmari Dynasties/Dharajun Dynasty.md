---
headerVersion: 2023.11.25
tags: [organization, status/needswork/wip, status/tim]
typeOf: family
ancestry: Dunmari
typeOfAlias: dynasty
name: Dharajun dynasty
---
# The Dharajun Dynasty
>[!info]+ Information  
> A [[Dunmar|Dunmari]] dynasty  
> `$=dv.view("_scripts/view/get_Affiliations")`

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