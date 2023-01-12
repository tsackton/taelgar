---
type: NPC
name: Tester
species: human
ancestry: Chardonian
gender: male
born: 1741
died: 1745
home: Chardon
homeRegion: "Chardonian Empire"
origin: OldTown
originRegion: "Lost Empire"
affiliations: ["Great Library"]
aliases: []
tags: [NPC/testing]
yearOverride: 
---
```dataviewjs NPCBioBlock

await forceLoadCustomJS();
const {npcUtils} = customJS
let pronouns = npcUtils.getPronouns(dv.current().gender, dv.current().pronouns)
let species = npcUtils.getSpecies(dv.current().species)
let ancestry = npcUtils.getAncestry(dv.current().ancestry)
let age = npcUtils.getAgeString(dv.current().born, dv.current().died,dv.current().yearOverride)
let homeLoc = npcUtils.getHomeLoc(dv.current().home, dv.current().homeRegion, dv.current().origin, dv.current().originRegion)
let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year

dv.header(1,dv.current().name)

if (currentYear >= dv.current().born) {
  dv.paragraph(">[!info]+ Biographical Summary\n>" + species + ancestry + ", " + pronouns + "\n>" + age + "\n>" + homeLoc)
} else {
  dv.paragraph(">[!info]+ Biographical Summary\n>**Warning: this person is not yet born**\n>\n>" + species + ancestry + ", " + pronouns + "\n>" + age + "\n>" + homeLoc)
}
```

<date 1745-03-11> Text goes here. more text here </date>

<1745-03-11> Test test test </>

<div class="mindate1719"> Test test test </div>

<date>1745-03-11</date> Test <date></date>

%%^Date:1745-03-11%% Text goes here %%^End%%

## Chronology
- item 1
- item 2
%%^Date:1745-03-11%%
- thing that hasn't happened 
%%^End%%
%%SECRET[1]%%