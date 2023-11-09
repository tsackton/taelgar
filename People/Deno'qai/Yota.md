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
     - { date: 0001-01-02, place: "Te'kula village", region: Elderwood}
     - { date: 1748-11-23, place: "unknown", region: Elderwood, type: excursion }
---
# Yota
>[!info]+ Biographical Summary
>human (Deno'qai), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

The chief of the Te'kula village.