---
type: NPC
name: Odo Cordwaner
species: human
ancestry: Sembaran
gender: male
born: 1700
died: 
title: Sergeant
affiliations: 
aliases: []
tags: [NPC/Clee/unsorted, NPC/DuFr/unaware]
family:
whereabouts:
     - { date: 1700-01-02, place: "Cleenseau", region: Sembara}
     - { date: 1719-10-21, place: "Taviose", region: Cleenseau, excursion: true}
---
# Sergeant Odo Cordwaner
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

The sergeant of the [[Army Garrison of Cleenseau|Bridge Patrol]] and a loyal solider. 
![[odo-cordwaner.png]]