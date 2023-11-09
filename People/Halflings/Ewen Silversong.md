---
type: NPC
name: Ewen Silversong
species: halfling
ancestry: 
gender: male
born: 1649
died: 
affiliations: ["Emerald Song crew"]
aliases: []
title:
family: Silversong
tags: [NPC/DuFr/minor, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1748-08-26, place: "Chardon", region: Chardonian Empire, type: excursion }
     - { date: 1748-11-23, place: "unknown", region: Nevos Sea, type: excursion }
---
# Ewen Silversong
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Songmaster and storyteller on the [[Emerald Song]].