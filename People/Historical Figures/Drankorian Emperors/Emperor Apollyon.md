---
type: NPC
name: Apollyon
title: Emperor
species: undead
ancestry: 
gender: male
born: 
died: 
affiliations: 
tags: [NPC/historical, NPC/DuFr/aware, NPC/DuFr/major]
family:
yearOverride: 
aliases: [Emperor Apollyon, Apollyon]
whereabouts:
     - { date: 0001-01-01, place: "Drankor", region: Drankorian Empire}
     - { date: 0001-01-02, place: "unknown", region: "unknown"}
---
# Emperor Apollyon
>[!info]+ Biographical Summary
>undead, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

### Apollyon

The last emperor of Drankor, who is said to have wanted to become a god. Creator of the [[Scepter of Command]], as well as the [[Mantle of Protection]] and perhaps other artifacts of power. Was a very successful general and commander. 

Originally allied with [[Cha'mutte]], although towards the end of his reign this relationship turned to conflict and when he died, he was imprisoned and prevented from resurrection by [[Cha'mutte]]. 
