---
type: NPC
name: Drusa
species: human
ancestry: Chardonian
gender: female
born: 
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/unsorted]
whereabouts:
     - { date: 0001-01-01, place: "Chardon", region: Chardonian Empire}
     - { date: 1748-05-01, place: "Tokra", region: Central Dunmar, excursion: true}
originRegion:
origin:
homeRegion:
home:
---
# Drusa
>[!info]+ Biographical Summary
>human (Chardonian), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A Chardonian wizard on loan to the Dunmari army of [[Nayan Karnas]], commanded by [[Illyan]], in [[Tokra]]. 

Does not particularly like the party given their attempt to scry on [[Illyan]], which Drusa detected, and their refusal to agree to simple magic protocols. 