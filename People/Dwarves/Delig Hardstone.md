---
type: NPC
name: Delig Hardstone
species: dwarf
ancestry: 
gender: male
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/background, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: , place: "Tokra", region: Central Dunmar, type: home}
---
# Delig Hardstone
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Patriach of the Hardstone clan, father to [[Dag Hardstone]]. 