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
     - { date: 0001-01-02, place: "Tokra", region: Central Dunmar}
---
# Delig Hardstone
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Patriach of the Hardstone clan, father to [[Dag Hardstone]]. 