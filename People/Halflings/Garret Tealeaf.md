---
type: NPC
name: Garret Tealeaf
species: halfling
ancestry: 
gender: male
born: 1656
died: 
affiliations: 
tags: [NPC/DuFr/met, NPC/DuFr/major]
title:
family: Tealeaf
yearOverride: 
lastSeenByParty_DuFr: 1748-07-15
aliases: [Garret]
whereabouts:
  - { date: 1737-01-01, place: "Agata's lair", region: Garamjala Desert, excursion: true }
  - { date: 1748-06-08, place: "Karawa", region: Eastern Dunmar, excursion: true }
  - { date: 1748-06-08, place: "Karawa", region: Eastern Dunmar, excursion: true }
  - { date: 1748-06-30, place: "Tokra", region: Central Dunmar, excursion: true } 
###secret[1]
---
# Garret Tealeaf
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

%%SECRET[2]%%