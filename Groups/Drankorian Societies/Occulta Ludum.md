---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {defArt: "the"}
name: Occulta Ludum
typeOf: magical society
ancestry: Drankorian
dm_owner: tim
dm_notes: important
---
# The Occulta Ludum
>[!info]+ Information  
> A [[Drankorian Empire|Drankorian]] magical society  
> `$=dv.view("_scripts/view/get_Affiliations")`

A magical society associated with the development of magic and especially with practical inventions of harnessing magical power. 

While they rejected the extremist claims of the [[Omnis Pura]] in the later years of the [[Drankorian Empire]], there is little evidence that has come down to current day that they actively opposed [[Omnis Pura]].

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