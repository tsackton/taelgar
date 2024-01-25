---
headerVersion: 2023.11.25
tags: [organization, status/unknown]
typeOf: family
typeOfAlias: noble family
created: 1594
---
# The House of Lils
>[!info]+ Information  
> A noble family  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

A cadet branch of the [[House of Sewick]], which came to the throne in the 1720s. The house descends from the youngest child of [[Elaine I]] and a Tyrwinghan [[Oracle of the Riven]], [[Morgaine]].

```mermaid 

graph TD

Derik(Derik of Lils) --- Annabeth
Annabeth --- GylesOfLils(Gyles of Lils)
Morgaine --- GylesOfLils
GylesOfLils --- ElaineII(Elaine II)
ElaineII --- ArrynIII(Arryn III)

classDef ruler stroke:green,stroke-width:2px
class ElaineII,ArrynIII ruler;
class GylesOfLils,Annabeth,Morgaine,ElaineII,ArrynIII,Derik internal-link;



```


%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%
