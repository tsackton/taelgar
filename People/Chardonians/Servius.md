---
type: NPC
name: Servius
species: human
ancestry: Chardonian
gender: male
born: 1689
died: 
title:
family:
affiliations: ["Society of the Open Scroll"]
aliases: []
tags: [NPC/DuFr/aware, NPC/DuFr/major]
whereabouts:
     - { date: 1689-01-02, place: "Chardon", region: Chardonian Empire}
     - { date: 1748-11-23, place: "unknown", region: Illoria, type: excursion}
---
# Servius
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A wandering scholar and historian, funded by [[Fausto]] to find rumors of treasure. Currently hunting rumors of treasure in Illoria. 