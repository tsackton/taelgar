---
headerVersion: 2023.11.25
tags: [organization]
displayDefaults: {partOf: "", boxInfo: "<ancestry:UA> <subtypeof:UA>"}
campaignInfo: []
name: House of Sewick
typeOf: family
ancestry: Sembaran
subTypeOf: noble house
destroyed: 1720
aliases: [Sewick]
dm_notes: none
dm_owner: no
---
# The House of Sewick
>[!info]+ Information
> A [[Sembara|Sembaran]] noble house
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`

The founding royal house of modern [[Sembara]], the House of Sewick ruled between the 1420s and the 1720s. A cadet branch, the [[House of Lils]] rules today.


```mermaid 

graph TD

DerikI(Derik I) --- DerikII(Derik II)
DerikII --- CharlotteI(Charlotte I)
CharlotteI --- Hugh1(Hugh of Sewick)
CharlotteI --- DerikIII(Derik III)
Sarabet --- DerikIIIKidsSara( )
DerikIII --- DerikIIIKidsSara( )
DerikIII --- DerikIIIKidsSJane( )
Jane(Jane of Tollen) --- DerikIIIKidsSJane( )
CharlotteI --- Eloise
DerikIIIKidsSara --- Reginald
DerikIIIKidsSara --- Hugh2(Hugh of Wisenfold)
DerikIIIKidsSJane --- BertramI(Bertram I)
Eloise ---- WisymI(Wisym I)
Reginald --- BertramII(Bertram II)
Reginald --- BlancheI(Blanche I)
Reginald --- ElaineI(Elaine I)
Cynan --- ElaineIKids( )
ElaineI --- ElaineIKids
Reginald --- Anne
Anne --- Wilhema
Anne --- Eloise2(Eloise)
Anne --- Peregrin
Reginald --- Gyles(Gyles of Teckberg)
ElaineIKids --- ArrynI(Arryn I)
ElaineIKids --- BlancheII(Blanche II)
ElaineIKids --- DerikElaineKid(Derik of Lils)
BlancheII --- ArrynII(Arryn II)
ArrynII --- CharlotteII(Charlotte II)
ArrynII --- CeceI(Cece I)
CeceI --- Bertram
CeceI --- DerikCeceKid(Derik)
CeceI --- Elleth
CeceI --- RobertI(Robert I)
CeceI --- Diana
CeceI --- Mara
DerikElaineKid --- HouseOfLils(House of Lils)


KingOrQueen(Names in a green box were kings or queens)

classDef ruler stroke:green,stroke-width:2px
classDef noKids stroke:red,stroke-width:2px

class DerikI,DerikII,CharlotteI,DerikIII,BertramI,BertramII,ArrynI,ElaineI,WisymI ruler;
class BlancheI,DerikI,DerikII,CharlotteI,DerikIII,Jane,BertramI,BertramII,ArrynI,ElaineI internal-link;

class Gyles,Hugh2,WisymI,Hugh1 internal-link;

class BlancheI,DerikIV,BlancheII,ArrynII,CharlotteII,CeceI,RobertI ruler;

class DerikIV,BlancheII,ArrynII,CharlotteII,CeceI,RobertI internal-link;
class Annabeth,Morgaine,HouseOfLils,Cynan,DerikElaineKid internal-link;

class Sarabet,Reginald,Eloise,Anne internal-link;

class KingOrQueen ruler;

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