---
type: NPC
name: Corrin Wildheart
species: hafling
ancestry: 
gender: male
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/met_one, NPC/DuFr/background]
yearOverride: 
whereabouts:
     - { date: 1748-11-23, place: "unknown", region: Eastern Green Sea, type: excursion }
---
# Corrin Wildheart
>[!info]+ Biographical Summary
>hafling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Halfling man in his prime. Navigator, with a touch of weather magic. Part of the crew of the [[Wave Dancer]].
