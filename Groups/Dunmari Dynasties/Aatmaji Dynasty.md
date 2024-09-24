---
headerVersion: 2023.11.25
tags: [organization, status/needswork/wip, status/check/tim]
displayDefaults: {boxInfo: "<ancestry:UA> <subtypeof>"}
campaignInfo:
name: Aatmaji dynasty
typeOf: family
subTypeOf: dynasty
ancestry: Dunmari
---
# The Aatmaji Dynasty
>[!info]+ Information  
> A [[Dunmar|Dunmari]] dynasty  
> `$=dv.view("_scripts/view/get_Affiliations")`

The first ruling dynasty of [[Dunmar]], founded by [[Bhishma]]. 

%% Tim: Do you have more information? If you don't have things actively made up I think it is fine to leave these dynasty / family pages mostly just placeholders %%

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