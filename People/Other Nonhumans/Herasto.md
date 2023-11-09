---
type: NPC
name: Herasto
species: centaur
ancestry: 
gender: male
born: 
died: 
affiliations: 
aliases: []
yearOverride: 
tags: [NPC/DuFr/unaware, NPC/GrLi/unsorted]
family:
title:
whereabouts:
     - { date: 1748-11-23, place: "plains south of Voltara, Voltara", region: Chardonian Empire, type: excursion }
---
# Herasto
>[!info]+ Biographical Summary
>centaur, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

%%Group of centaurs currently wintering in sheltered valleys south of Voltara%%