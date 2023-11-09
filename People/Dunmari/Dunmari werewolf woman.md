---
type: NPC
name: Dunmari werewolf woman
species: human
ancestry: Dunmari
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
     - { date: 0001-01-02, place: "Tokra", region: Central Dunmar, type: home }
---
# Dunmari werewolf woman
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

The unnamed woman who was cured of lycanthropy by [[Riswynn]], one of the few survivors of the [[Fraternity of the Empty Moon]]. 