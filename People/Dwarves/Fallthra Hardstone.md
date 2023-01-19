---
type: NPC
name: Fallthra Hardstone
species: dwarf
ancestry: 
gender: female
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/met, NPC/DuFr/minor]
yearOverride: 
whereabouts:
     - { date: 0001-01-02, place: "Tokra", region: Central Dunmar}
---
# Fallthra Hardstone
>[!info]+ Biographical Summary
>dwarf, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

Matriach of the Hardstone clan; mother to [[Dag Hardstone]]. 