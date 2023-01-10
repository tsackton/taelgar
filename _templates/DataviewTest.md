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
Still to do:
figure out how to handle current location. For most NPCs, this is just home location 
however some NPCs travel around and it is useful to know where they are at any time 
so ideally want to autogenerate chronology/location sections 
this would be based I guess on separate notes? probably can't do it with frontmatter
would query to get all the list items that occur before current day, and return those
in an ideal world this would allow a single NPC Timelines and NPC Relationships doc and could query those
more likely need separate notes per NPC at least