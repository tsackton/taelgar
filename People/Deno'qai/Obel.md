---
type: NPC
name: Obel
species: human
ancestry: "Deno'qai"
gender: male
born: 1688
died: 
title:
family:
affiliations: 
aliases: []
tags: [NPC/DuFr/minor, NPC/DuFr/met]
whereabouts:
     - { date: 1688-01-02, place: "Te'kula village", region: Elderwood}
     - { date: 1748-11-23, place: "Te'kula village", region: Elderwood, excursion: true }
---
# Obel
>[!info]+ Biographical Summary
>human (Deno'qai), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

An old ranger of the Te'kula who volunteered to fight [[Mezzar|Grimbaskal]] with the party. Miraculously survived. 
