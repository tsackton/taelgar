---
headerVersion: 2023.11.25
tags: [organization, status/unknown]
displayDefaults: {partOf: "", boxInfo: "<ancestry:UA> <typeof:UA> of <deity:UA>"}
typeOf: mystery cult
ancestry: Dunmari
deity: Laka
---
# The Lakan Mystai
>[!info]+ Information  
> A [[Dunmar|Dunmari]] mystery cult of [[Laka]]  
> `$=dv.view("_scripts/view/get_Affiliations")`

The mystery cult of the Dunmari god [[Laka]]. Guardians of secret knowledge, especially concerning the lore of other planes, and the secrets of manipulating planar energy to create magic.

%%SECRET

Mystery cult dedicated to Laka.

Based in a monastery outside Tokra (Lakan Monastery), although have additional smaller monasteries associated with the order. The head of the Mystai outside Tokra is Speaker Lara.

Kenzo was a student and then initiate at this monastery for five years.

Their mystical knowledge, experience, and role takes the form of keepers of scholarly pursuits, knowledge of magic, the archives of wisdom of the ages.

The magic of Lakan Mystai often is associated with scholarly study, especially true wizardry.

Keepers of metaphysical knowledge of the planes.
%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%