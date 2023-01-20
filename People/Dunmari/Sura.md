---
type: NPC
name: Sura
species: human
ancestry: Dunmari
gender: female
born: 1712
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/DuFr/met, NPC/DuFr/major]
yearOverride: 
whereabouts:
     - { date: 1712-01-01, place: "Darba", region: Western Dunmar}
     - { date: 1740-01-01, place: "Mirror of Soul Trapping", excursion: true}
     - { date: 1748-06-08, place: "Karawa", region: "Eastern Dunmar", excursion: true}
     - { date: 1748-11-23, place: "Sura's army camp, north of Tokra", region: Central Dunmar, excursion: true }
---
# Sura
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

The sister of [[Nayan Karnas]], trapped in the [[Mirror of Soul Trapping]] by Agata for 8 years. Now emerged and contemplating war against her brother.

![[sura.png|400]]

%%SECRET[1]%%