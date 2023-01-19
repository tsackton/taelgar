---
type: NPC
name: Ulfgar Frostbeard
species: dwarf
ancestry: 
gender: male
born: 1599
died: 
affiliations: ["Faculty of Metaphysics", "University of Chardon", "Society of the Open Scroll"]
aliases: []
tags: [NPC/DuFr/met, NPC/DuFr/minor]
title:
yearOverride: 
family:
whereabouts:
     - { date: 1599-01-02, place: "Chardon", region: Chardonian Empire}
---
# Ulfgar Frostbeard
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A dwarven scholar and theoretical metaphysicist, on the Faculty of Metaphysics at the [[University of Chardon]].  Author of [[The Lore of the Feywild]]. 

Met [[Seeker]] in December 1757, when [[Seeker]] passed through [[Chardon]] before arriving in [[Karawa]].