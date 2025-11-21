---
name: Tester
gender: nonbinary
species: elf
ancestry: Drankorian
---

```dataviewjs
await forceLoadCustomJS();
const {npcUtils} = customJS
let pronouns = npcUtils.getPronouns(dv.current().gender, dv.current().pronouns)
let species = npcUtils.getSpecies(dv.current().species)
let ancestry = npcUtils.getAncestry(dv.current().ancestry)
dv.header(1,dv.current().name)
dv.span(">[!info]+ Biographical Summary" + "\n" + ">" + species + ancestry + ", " + pronouns + "\n")

```