---
type: NPC
name: Gentza
species: lizardfolk
ancestry: 
gender: female
born: 1681
died: 1719
affiliations: 
title:
family:
aliases: []
tags: [NPC/Clee/unaware, NPC/DuFr/unaware]
yearOverride: 
whereabouts:
     - { date: 1681-01-02, place: "Ganboa", region: Semabara, type: home }
     - { date: 1719-11-01, place: "deceased", type: excursion }
---
# Gentza
>[!info]+ Biographical Summary
>lizardfolk, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], Semabara
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An apprentice lizardfolk herbalist, said to be skilled at experimenting with remedies.

![[lizardfolk-gentza.png]]