---
type: NPC
name: Erdu
species: lizardfolk
ancestry: 
gender: male
born: 1441
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/Clee/unaware, NPC/DuFr/unaware]
yearOverride: 
whereabouts:
     - { date: 1441-01-02, place: "Ganboa", region: Semabara, type: home }
     - { date: 1719-12-04, place: "Ganboa", region: Semabara, type: excursion }
---
# Erdu
>[!info]+ Biographical Summary
>lizardfolk, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], Semabara
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The spokesperson for the village of [[Ganboa]] when dealing with humans. Older, with graying scale.

![[lizardfolk-erdu.png]]