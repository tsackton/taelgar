---
type: NPC
name: Hektor
species: human
ancestry: Chardonian
gender: male
born: 1726
died: 
affiliations: 
title:
aliases: []
tags: [NPC/DuFr/major, NPC/DuFr/met]
family:
whereabouts:
     - { date: 1726-01-01, place: "Chardon", region: Chardonian Empire, type: home }
###secret[1]
     - { date: 1748-11-15, place: "somewhere in Dunmar", region: Dunmar, type: excursion}
###secret[2]
---
# Hektor
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.getRoot().path + ".obsidian/taelgarConfig.json"), "prefix": ">", "suffix":""})`

A barbarian. A huge Chardonian man, muscled and over 6 feet tall. Silent. Does not wear any armor, just a simple sailor’s cloak, and carries a clearly well-loved and dangerous-looking halberd. 

According to [[Marcella]], he was once a sweet sailor with a beautiful singing voice, but was turned somehow by [[Kadmos]] and now is his devoted servant. 

![[hektor.png|500]]

%%SECRET[3]%%