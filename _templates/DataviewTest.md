---
type: NPC
name: Tester
species: human
ancestry: Chardonian
gender: male
born: 1697
died: 1755
home: Chardon
homeRegion: "Chardonian Empire"
origin: OldTown
originRegion: "Lost Empire"
affiliations: ["Great Library"]
aliases: []
tags: [NPC/unsorted]
yearOverride: 
---

```dataviewjs

await forceLoadCustomJS();
const {npcUtils} = customJS
let pronouns = npcUtils.getPronouns(dv.current().gender, dv.current().pronouns)
let species = npcUtils.getSpecies(dv.current().species)
let ancestry = npcUtils.getAncestry(dv.current().ancestry)
let age = npcUtils.getAgeString(dv.current().born, dv.current().died,dv.current().yearOverride)
dv.header(1,dv.current().name)
let homeLoc = npcUtils.getHomeLoc(dv.current().home, dv.current().homeRegion, dv.current().origin, dv.current().originRegion)
dv.paragraph(">[!info]+ Biographical Summary" + "\n>" + species + ancestry + ", " + pronouns + "\n>" + age + "\n>" + homeLoc)
```
