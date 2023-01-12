---
type: NPC
name: Tester
species: 
ancestry:
gender: 
born: 1721
died: 1755
location: 
locationRegion:
home: 
homeRegion: 
origin: 
originRegion: 
affiliations: 
affiliations: ["Great Library"]
aliases: []
tags: [NPC/testing]
yearOverride: 
lastSeenByParty_DuFr: 
whereabouts: 
- {dateAr: 0001-01-01, place: "", region: }
---

home: "Whitsun District, Chardon"
homeRegion: "Chardonian Empire"
origin: "Arendum, Chasa River Valley"
originRegion: "Chardonian Empire"




# Tester
>[!info]+ Basic information
>unknown species, they/them
>`$=dv.view(agefunction, {"currentYear" : 1748})`
>
>


```dataviewjs

await forceLoadCustomJS();
const {metadataUtils} = customJS
let metadata = dv.current()
let Name = metadata.name

let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year
let existYear = metadataUtils.get_existYear(metadata)
let Pronouns = metadataUtils.get_Pronouns(metadata)
let Species = metadataUtils.Reformat(metadata, "species", "", "", "unknown species")
let Ancestry = metadataUtils.Reformat(metadata, "ancestry", " (", ") ", "")
let PageDatedValue = metadataUtils.get_PageDatedValue(metadata,existYear)


let BLOCKSTRING_EXIST = "# " + Name + "\n>[!info]+ Biographical Summary" + "\n>" + dv.fileLink(Species) + Ancestry + ", " + Pronouns + "\n>" + PageDatedValue + "\n"
let BLOCKSTRING_NOTEXIST = "# " + Name + "\n>[!fail] **This entity does not yet exist!**"

if (currentYear >= existYear) {
  dv.paragraph(BLOCKSTRING_EXIST)
} else {
  dv.paragraph(BLOCKSTRING_NOTEXIST)
}
```

