---
type: NPC
name: Elazar
species: lizardfolk
ancestry: 
gender: male
born: 1665
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/minor, NPC/DuFr/met_one]
yearOverride: 
whereabouts:
     - { date: 1665-01-02, place: "Bedez", region: Orekatu}
---
# Elazar
>[!info]+ Biographical Summary
>lizardfolk, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A lizardfolk man in the prime of his life, a prophet, seer, and spirit guide who has deeply felt visions and exceptional perception into the spirit realms. [[Kenzo]]’s teacher. A bit of an outcast in his village, seen as someone who sees trouble in everything, although with the recent events in the [[Azta Lekua|Footprint of the Gods]] this reputation is changing. 

![[elazar-portrait.png|500]]