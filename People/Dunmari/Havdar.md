---
type: NPC
name: Havdar
species: human
ancestry: Dunmari
gender: male
born: 1725
died: 
affiliations: ["Havdar's Warband"]
title:
family:
aliases: []
tags: [NPC/DuFr/met, NPC/DuFr/major, stub]
yearOverride: 
whereabouts:
     - { date: 1725-01-01, place: "Karawa", region: Eastern Dunmar}
     - { date: 1748-11-23, place: "Sura's army camp", region: Central Dunmar, excursion: true }
---
# Havdar
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.configDir +  "/taelgarConfig.json"), "prefix": ">", "suffix":""})`

![[havdar.png|500]]

%%SECRET[1]%%