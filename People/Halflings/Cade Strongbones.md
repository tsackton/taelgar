---
type: NPC
name: Cade Strongbones
species: halfling
ancestry: 
gender: male
born: 1709
died: 
affiliations: ["Strongbones"]
title:
family:
aliases: []
tags: [NPC/DuFr/met, NPC/DuFr/background]
yearOverride: 
whereabouts:
     - { date: 1709-01-02, place: "Tokra", region: Central Dunmar, type: home }
---
# Cade Strongbones
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Son of [[Wes Strongbones]], helps run [[The Red Lily Inn]] in [[Tokra]].
