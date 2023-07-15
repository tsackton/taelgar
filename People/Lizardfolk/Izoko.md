---
type: NPC
name: Izoko
species: lizardfolk
ancestry: 
gender: male
born: 1688
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/Clee/unaware, NPC/DuFr/unaware]
yearOverride: 
whereabouts:
     - { date: 1688-01-02, place: "Ganboa", region: Semabara, type: home }
     - { date: 1719-12-04, place: "Ganboa", region: Semabara, type: excursion }
---
# Izoko
>[!info]+ Biographical Summary
>lizardfolk, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], Semabara
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`


A young lizardfolk, sweet on [[Gentza]].
![[lizardfolk-Izoko.png]]