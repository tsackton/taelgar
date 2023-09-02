---
type: NPC
name: Lyra
species: human
ancestry: Chardonian
gender: female
born: 1705
title:
family:
died: 
affiliations: ["Great Library"]
aliases: []
tags: [NPC/DuFr/met, NPC/DuFr/minor, NPC/GrLi/met, NPC/GrLi/major]
lastSeenByParty:
 - { date: 1748-08-26, prefix: DuFr}
whereabouts:
     - { date: 1705-01-01, place: "Darba", region: Western Dunmar}
     - { date: 1705-01-02, place: "Voltara", region: Chardonian Empire}
     - { date: 1748-11-23, place: "Chardon", region: Chardonian Empire, excursion: true }
---
# Lyra
>[!info]+ Biographical Summary
>human (Chardonian), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`


An archivist with the Great Library, responsible for arranging adventuring expeditions to recover magic, knowledge, and treasure. Spend considerable time in the north of the [[Chardonian Empire]].

Friends with [[Roscelia]].

%%SECRET[1]%%