---
type: NPC
name: Jita
species: human
ancestry: Dunmari
gender: female
born: 1713
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/DuFr/background, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1713-01-01, place: "plains north of Tokra", region: Central Dunmar, type: home }
---
# Jita
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: plains north of Tokra, [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A Dunmari herder living on the northern plains, north of Tokra. Niece of [[Saka]], and has generally taken charge of helping Saka around camp. 