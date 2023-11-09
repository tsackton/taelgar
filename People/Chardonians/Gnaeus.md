---
type: NPC
name: Gnaeus
species: human
ancestry: Chardonian
gender: male
born: 1701
title:
family:
died: 
affiliations: ["University of Chardon", "Sibyl's Hall"]
aliases: []
tags: [NPC/DuFr/minor, NPC/DuFr/met]
whereabouts:
     - { date: 1701-01-01, place: "Arendum", region: Chardonian Empire, type: origin}
     - { date: 1701-01-02, place: "Chardon", region: Chardonian Empire, type: home}
---
# Gnaeus
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A disgraced historian and scholar, expelled from the Faculty for using enchantment magic to aid his research, now making a poor living as a tutor. 

Wrote [[On the Lost People of the Forests]], describing travels in his youth among the Deno'qai of the [[Elderwood]]. 