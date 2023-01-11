---
type: NPC
name: Sembara Person
species: human
ancestry: Chardonian
gender: male
born: 1705
died: 1765
home: Chardon
homeRegion: "Chardonian Empire"
origin: OldTown
originRegion: "Lost Empire"
affiliations: ["Great Library"]
aliases: []
tags: [NPC/testing]
yearOverride: 
cssClasses: embed-strict
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

let Overview = dv.sectionLink("Tester.text","Overview")
let Chronology = dv.sectionLink("Tester.chronology", "Chronology")
if (currentYear >= dv.current().born) {
  dv.paragraph(">[!info]+ Biographical Summary" + "\n>" + species + ancestry + ", " + pronouns + "\n>" + age + "\n>" + homeLoc)
  dv.paragraph(Overview);
} else {
  dv.paragraph("**This person is not yet born**")
}
```

### Chronology and Events

```dataviewjs
let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year
let currentFolder = "\"" + dv.current().file.folder + "\""
for (let group of dv.pages(currentFolder).sort(f => f.eventEndDate)) {
   if (group.name == dv.current().name && group.type == "NPC_Event")  {  
      if (group.eventEndDate <= currentYear) {
	 	var link = group.file.link
		link.embed = true
		link.display = "natural"
		dv.span(link)
      }
   }
}
```
