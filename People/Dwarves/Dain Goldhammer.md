---
type: NPC
name: Dain Goldhammer
species: dwarf
ancestry: 
gender: male
born: 1710
died: 
title:
family:
affiliations: 
aliases: []
tags: [NPC/DuFr/minor, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1710-01-01, place: "Chardon", region: Chardonian Empire}
     - { date: 1710-01-02, place: "Chardon", region: Chardonian Empire}
     - { date: 1748-11-23, place: "unknown", region: Illoria, type: excursion }
---
# Dain Goldhammer
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

An adventurer, working for the [[Society of the Open Scroll]], funded by [[Fausto]]. Often travels with [[Dee Wildcloak]]. 

Part of the group that explored [[Gazetteer/The Central Lowlands Region/Dunmar/Eastern Dunmar/Stormcaller Tower]] and brought [[Hralgar's Eyes]] and the [[Binding Stones]] back to [[Chardon]].