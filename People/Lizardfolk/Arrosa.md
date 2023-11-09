---
type: NPC
name: Arrosa
species: lizardfolk
ancestry: 
gender: female
born: 
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/DuFr/met_one, NPC/DuFr/background]
yearOverride: 
whereabouts:
     - { date: , place: "Bedez", region: Orekatu, type: home }
---
# Arrosa
>[!info]+ Biographical Summary
>lizardfolk, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Bedez]], [[Orekatu]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A lizardfolk elder, the matriarch of the village of [[Bedez]], in the Kingdom of [[Orekatu]]. 