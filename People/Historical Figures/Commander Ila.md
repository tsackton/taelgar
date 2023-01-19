---
type: NPC
name: Ila
species: human
ancestry: Dunmari
gender: male
born: 
died: 
affiliations: 
aliases: []
title: Commander
family:
tags: [NPC/historical, NPC/DuFr/aware]
yearOverride: 
whereabouts:
     - { date: 0001-01-02, place: "unknown", region: Central Dunmar}
---
# Commander Ila
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

The commander of the eastern Dunmari army around the time of the [[Second Hobgoblin War]]. Involved in [[The Exile of Fraternity of the Empty Moon]] in the DR 1610s.

