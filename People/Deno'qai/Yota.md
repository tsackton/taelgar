---
type: NPC
name: Yota
species: human
ancestry: "Deno'qai"
gender: male
born: 
died: 
title:
family:
affiliations: 
aliases: []
tags: [NPC/DuFr/background, NPC/DuFr/met]
whereabouts:
     - { date: 0001-01-02, place: "Te'kula village", region: Elderwood, type: home }
---
# Yota
>[!info]+ Biographical Summary
>human (Deno'qai), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: Te'kula village, [[Elderwood]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The chief of the Te'kula village.