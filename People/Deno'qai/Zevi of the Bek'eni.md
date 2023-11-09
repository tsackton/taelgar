---
type: NPC
name: Zevi
species: human
ancestry: "Deno'qai"
gender: male
born: 
died: 1748
title:
family:
affiliations: 
aliases: []
tags: [NPC/DuFr/background, NPC/DuFr/met]
whereabouts:
     - { date: 0001-01-02, place: "unknown", region: Elderwood}
     - { date: 1748-11-23, place: "deceased", region: "", type: excursion }
---
# Zevi
>[!info]+ Biographical Summary
>human (Deno'qai), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A scout and warrior of the [[Bek'eni]]. Part of the patrol that originally found the party in the [[Elderwood]]. 

Accompanied the party back to the God tree to meet [[Mezzar]], and killed by [[Mezzar|Grimbaskal]]'s breath weapon after [[Mezzar]] dropped his elven form. 