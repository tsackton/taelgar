---
type: NPC
name: Tester
species: elf
ancestry: Chardonian
gender: male
born: 1732
died: 1755
home: Chardon
pronouns:
homeRegion: "Chardonian Empire"
origin: OldTown
originRegion: "Lost Empire"
affiliations: ["Great Library"]
aliases: []
tags: [NPC/testing]
yearOverride: 
---

```dataviewjs

await forceLoadCustomJS();
const {metadataUtils} = customJS
let metadata = dv.current()
let Name = metadata.name

let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year

let existYear = metadataUtils.get_existYear(metadata)
let Pronouns = metadataUtils.get_Pronouns(metadata)
let Species = metadataUtils.get_Species(metadata)
let Ancestry = metadataUtils.get_Ancestry(metadata)
let PageDatedValue = metadataUtils.get_PageDatedValue(metadata,existYear)

let BLOCKSTRING_EXIST = "# " + Name + "\n>[!info]+ Biographical Summary" + "\n>" + Species + Ancestry + ", " + Pronouns + "\n>" + PageDatedValue + "\n"
let BLOCKSTRING_NOTEXIST = "# " + Name + "\n**This entity does not yet exist!**"

if (currentYear >= existYear) {
  dv.paragraph(BLOCKSTRING_EXIST)
} else {
  dv.paragraph(BLOCKSTRING_NOTEXIST)
}
```
