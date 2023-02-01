---
type: NPC
name: Resenna
species: human
ancestry: 
gender: female
born: 1724
died: 
affiliations: 
aliases: []
tags: [NPC/DuFr/met_one, NPC/DuFr/background]
yearOverride: 
title:
family:
whereabouts:
     - { date: 1724-01-01, place: Medju, region: Eastern Green Sea, type: origin}
     - { date: 1748-11-23, place: "sea elf village, Quanyi", region: Eastern Green Sea, type: excursion}
---
# Resenna
>[!info]+ Biographical Summary
>human, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Medju]], [[Eastern Green Sea]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Young woman, from Medju. Apprentice to [[Arryn]]. Fled when he vanished into [[Mirror Realm]]; was trapped and enslaved by aboleth. Now dwelling with sea elves until aboleth curse can be removed. 

![[resenna.png|400]]