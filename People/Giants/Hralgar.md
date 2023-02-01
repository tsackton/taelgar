---
type: NPC
name: Hralgar
species: giant
ancestry: storm
gender: male
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/major, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1748-11-23, place: "trapped in Stormcaller Tower", region: Eastern Dunmar, type: excursion }
---
# Hralgar
>[!info]+ Biographical Summary
>giant (storm), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An ancient storm giant, of great power, who could become a storm and travel across the world, who was trapped by Drankorian mages and then slumbered for centuries, until disturbed and awoken by Chardonian explorers. Now trapped in a dream and a nightmare in [[Gazetteer/The Central Lowlands Region/Dunmar/Eastern Dunmar/Stormcaller Tower]].

%%SECRET[1]%%