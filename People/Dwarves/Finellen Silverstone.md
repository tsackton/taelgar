---
type: NPC
name: Finellen Silverstone
species: dwarf
ancestry: 
gender: female
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/background, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 0001-01-02, place: "Darba", region: Western Dunmar, type: home }
---
# Finellen Silverstone
>[!info]+ Biographical Summary
>dwarf, they/them
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A dwarven antiquities dealer in [[Darba]].