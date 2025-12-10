---
headerVersion: 2023.11.25
tags:
  - place
name: Valit
typeOfAlias: village
whereabouts: Manor of Valit
population: 249
pronunciation: Val-le
typeOf: settlement
dm_owner: mike
dm_notes: important
---
# Valit
*(Val-le)*
>[!info]+ Information  
> pop. 249  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A small village overseen by the castellan of the [[Manor of Valit]] of about 50 houses scattered a little more widely than most of the other villages in the region. There is no walls, although the manor complex is walled and fortified and can shelter the population of the village in times of need. The most notable features of the village are the wooden bridge over the [[Amance Brook]], and the three mills built along the brook, as well as the large two-story wooden manor with several outbuildings, rebuilt about 30 years ago after a fire. The manor complex includes a land registry, a temple to the Wildling, a stable, and blacksmith. Just under the eaves of the [[Cleenseau Wood]], is another small ancient shrine to the Wildling, said to date back 
### Notable Residents
* [[Sabine de Brune]], the castellan and magistrate, recently vanished
* [[Warin the Woodsman|Warin]], her master of the guard and woodsman
* [[Giselle]], Sabine's secretary and keeper of the baronial land registry
* Henri, Odette, and Reynard, the three millers
* Julien Leclair, the steward to the temples, and his wife, a skilled carpenter

%%^Campaign:None%%
### People in, or based in Valit
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location", "Home"], 
			dv.pages("#person")
				.where(f => util.inOrHomeLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate))				
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file), util.s("<ancestry> <maintype>", b.file), util.s("<lastknown:2> (<lastknowndate>)", b.file, dv.current().pageTargetDate), util.s("<home:1>", b.file, dv.current().pageTargetDate)]))
```
%%^End%%