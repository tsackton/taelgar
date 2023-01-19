---
type: NPC
name: Resenna
species: human
ancestry: 
gender: female
born: 
died: 
affiliations: 
aliases: []
tags: [NPC/DuFr/met, NPC/DuFr/background]
yearOverride: 
title:
family:
whereabouts:
     - { date: 1748-11-23, place: "sea elf village, Quanyi", region: Eastern Green Sea, excursion: true }
---
# Resenna
>[!info]+ Biographical Summary
>human, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Young woman, from Medju. Apprentice to [[Arryn]]. Fled when he vanished into [[Mirror Realm]]; was trapped and enslaved by aboleth. Now dwelling with sea elves until aboleth curse can be removed. 

![[resenna.png|400]]