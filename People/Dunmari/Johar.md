---
type: NPC
name: Johar
species: human
ancestry: Dunmari
gender: male
born: 1721
died: 
affiliations: 
title:
family:
aliases: []
tags: [NPC/DuFr/major, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1721-01-02, place: "Tokra", region: Central Dunmar}
     - { date: 1748-11-23, place: "Nayahar", region: Western Dunmar, excursion: true }
---
# Johar
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Johar is a confidant and close friend of [[Kenzo]]'s from the [[Lakan Monastery]] in [[Tokra]]. He works in the [[Tokra]] [[Archives]], primary interested in documenting the miracles of [[Laka]], and the history of the [[Lakan Monastery]] and the community there. 

%%SECRET[1]%%