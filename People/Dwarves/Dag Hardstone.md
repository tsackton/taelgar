---
type: NPC
name: Dag Hardstone
species: dwarf
ancestry: 
gender: male
born: 1729
died: 
affiliations: 
aliases: []
title:
family: Hardstone
tags: [NPC/DuFr/minor, NPC/DuFr/met]
yearOverride: 
whereabouts:
     - { date: 1729-01-02, place: "Tokra", region: Central Dunmar, type: home}
---
# Dag Hardstone
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

One of the Hardstone dwarves, who help maintain the [[Tokra]] [[Archives]]. Dag was caught by werewolves when the [[Archives]] were raided, and wounded, becoming cursed by lycanthropy. 

Cured by [[Delwath]], via the blessing of [[Yezali]]. 