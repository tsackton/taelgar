---
type: NPC
name: Crispus
species: human
ancestry: Chardonian
gender: male
born: 1697
died: 
title:
family:
affiliations: ["Great Library"]
aliases: []
tags: [NPC/DuFr/aware, NPC/DuFr/minor]
whereabouts:
     - { date: 1697-01-02, place: "Chardon", region: Chardonian Empire, type: home }
---
# Crispus
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A senior Archivist at the [[Great Library]], in charge of external mercenary contracts, with general responsibility for organizing missions to recover lost treasures for the Great Library. 

%%SECRET[1]%%