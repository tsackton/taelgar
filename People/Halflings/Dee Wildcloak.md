---
type: NPC
name: Dee Wildcloak
species: halfling
ancestry: 
gender: female
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/minor, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1748-11-23, place: "somewhere", region: Sea of Storms, excursion: true }
---
# Dee Wildcloak
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Adventurer, funded by [[Fausto]] to explore. Part of the group that brought [[Hralgar's Eyes]] to [[Chardon]] from [[Stormcaller Tower]]. 
