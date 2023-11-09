---
type: NPC
name: Unai
species: lizardfolk
ancestry: 
gender: female
born: 1602
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/Clee/unaware, NPC/DuFr/unaware]
yearOverride: 
whereabouts:
     - { date: 1602-01-02, place: "Ganboa", region: Sembara, type: home }
---
# Unai
>[!info]+ Biographical Summary
>lizardfolk, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An herbalist and healer, teacher of [[Gentza]].

![[lizardfolk-unai.png]]