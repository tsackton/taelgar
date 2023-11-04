---
type: NPC
name: Vistra Fireforge
species: dwarf
ancestry: 
gender: female
born: 1589
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/minor, NPC/DuFr/met, NPC/Clee/unsorted]
yearOverride: 
whereabouts:
     - { date: 1589-01-01, place: "Tharn Todor", region: Nardith}
     - { date: 1620-01-01, place: "Ausson's Crossing", region: Greater Sembara}
     - { date: 1730-01-01, place: "Tokra", region: Central Dunmar}
## years are arbitrary for Nardith -> Ausson's Crossing -> Tokra
## could be changed but should be in Tokra by 1735 at the latest
---
# Vistra Fireforge
>[!info]+ Biographical Summary
>unknown species, they/them
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A dwarven blacksmith, trader, innkeep, and adventurer. She is of the Traveler thuhr and originally from [[Nardith]]. She was born after the [[Events/1500s/Great War]] and has always been eager to work with humans. She is charming and pleasant enough, but perhaps not that bright and she sometimes makes mistakes in her trades, although she rarely wants to believe it.

In her youth she was a blacksmith and trader in [[Ausson's Crossing]] a crossroads inn south of [[Sembara]]. She is now settled in [[Tokra]] where she runs the dwarven inn, [[The Iron Swan]].

![[vistra-fireforge.png|320]]








