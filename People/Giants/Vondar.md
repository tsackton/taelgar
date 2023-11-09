---
type: NPC
name: Vondar
species: giant
ancestry: cursed
gender: male
born: 
died: 
affiliations: 
aliases: []
title:
tags: [NPC/DuFr/background, NPC/DuFr/met_one, status/uptodate]
yearOverride: 
family:
whereabouts:
     - { date: 0001-01-01, place: "unknown", region: unknown}
     - { date: 1748-11-23, place: "unknown", region: Amberglow, type: excursion }
---
# Vondar
>[!info]+ Biographical Summary
>giant (cursed), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A cursed giant who guards the passes from [[Shimmersong]] into [[Amberglow]], asking for a toll of a memory in order to pass. Killed, but presumably not permanently, by [[Seeker]] and friends.