---
type: NPC
name: Wes Strongbones
species: halfling
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
     - { date: 0001-01-02, place: "Tokra", region: Central Dunmar, type: home }
---
# Wes Strongbones
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Proprietor of [[The Red Lily Inn]] in [[Tokra]]. 

%%SECRET[1]%%