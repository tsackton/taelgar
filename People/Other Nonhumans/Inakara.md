---
type: NPC
name: Inakara
species: derro
ancestry: 
gender: female
born: 1702
died: 1748
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/minor, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1702-01-02, place: "Dwarven outpost, Raven's Hold", region: "Eastern Dunmar", type: home }
     - { date: 1748-11-23, place: "deceased, Dwarven outpost, Raven's Hold", region: "Eastern Dunmar", type: excursion }
---
# Inakara
>[!info]+ Biographical Summary
>derro, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Dwarven outpost]], [[Raven's Hold]], [[Eastern Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A mad twisted creature and sorcerer living in the old [[Dwarven outpost]] near Raven's Hold. 

Killed by [[Magran Boulderbeard]] and company in July 1748, according to [[Travok Redpeak]] who brough [[Riswynn]] messenges in [[Darba]]. 

