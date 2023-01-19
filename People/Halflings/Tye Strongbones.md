---
type: NPC
name: Tye Strongbones
species: halfling
gender: male
ancestry: 
affiliations: 
aliases: []
title:
family: Strongbones
died:
born:
tags: [NPC/DuFr/met, NPC/DuFr/background]
yearOverride: 
whereabouts:
     - { date: 0001-01-02, place: "Tokra", region: Central Dunmar}
---
# Tye Strongbones
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Son of [[Wes Strongbones]].