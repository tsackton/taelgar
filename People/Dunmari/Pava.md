---
type: NPC
name: Pava
species: human
ancestry: Dunmari
gender: male
born: 1673
died: 
affiliations: ["Order of the Awakened Soul"]
title:
family:
aliases: []
tags: [NPC/DuFr/major, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1673-01-01, place: "plains to the east, Songara", region: Central Dunmar}
     - { date: 1673-01-02, place: "Pava and Avaras' House", region: Garamjala Desert}
---
# Pava
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A master of the Order of the Awakened Soul, an old man, bald, with striking blue eyes and surprising agility.

![[pava.png|500]]

%%SECRET[1]%%