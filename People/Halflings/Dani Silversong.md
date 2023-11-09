---
type: NPC
name: Dani Silversong
species: halfling
ancestry: 
gender: female
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/minor, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1748-11-23, place: "traveling", region: Nevos Sea, type: excursion }
---
# Dani Silversong
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Quartermaster and chief trader on the [[Emerald Song]].
