---
type: NPC
name: Nora Silverspark
species: dwarf
ancestry: 
gender: female
born: 
died: 
affiliations: 
aliases: [Nora]
tags: [NPC/DuFr/minor, NPC/DuFr/met_one]
yearOverride: 
title:
family:
whereabouts:
     - { date: 1748-11-23, place: "deceased", region: unknown, type: excursion }
---
# Nora Silverspark
>[!info]+ Biographical Summary
>dwarf, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A dwarven warrior, once a ghost in [[Morkalan]] and now passed on. The first victim of [[Hagrim]]'s betrayal. 
