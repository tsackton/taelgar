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
     - { date: 1689-01-02, place: "Chardon", region: Chardonian Empire, type: home }
     - { date: 1748-11-23, place: "unknown", region: Illoria, type: excursion}
---
# Servius
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A wandering scholar and historian, funded by [[Fausto]] to find rumors of treasure. Currently hunting rumors of treasure in Illoria. 