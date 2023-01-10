---
type: NPC
name: Tester
species: human
ancestry: Chardonian
gender: male
born: 1734
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
let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year

let Overview = await dv.io.load("_templates/testing/Tester.text.md")
let Chronology = await dv.io.load("_templates/testing/Tester.chronology.md")

if (currentYear >= dv.current().born) {
  dv.paragraph(">[!info]+ Biographical Summary" + "\n>" + species + ancestry + ", " + pronouns + "\n>" + age + "\n>" + homeLoc)
  dv.paragraph(Overview)
  dv.paragraph(Chronology)
} else {
  dv.paragraph("**This person is not yet born**")
}
```
