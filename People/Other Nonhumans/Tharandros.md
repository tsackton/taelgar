---
type: NPC
name: Tharandros
species: centaur
ancestry: 
gender: male
born: 
died: 
affiliations: 
aliases: []
title:
family:
tags: [NPC/DuFr/met, NPC/DuFr/major]
yearOverride: 
whereabouts:
     - { date: 1748-06-03, place: "Karawa", region: Eastern Dunmar, type: excursion }
###secret[1]
###secret[2]
---
# Tharandros
>[!info]+ Biographical Summary
>centaur, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A centaur, the leader of a herd who the party met traveling across the northern plains of [[Dunmar]]. Convinced to aid [[Karawa]], and proved crucial in driving off gnoll attacks. 

![[tharandros.png|500]]

Left to travel north in [[Session 29 (DuFr)]], around 1 June 1748. %%SECRET[3]%%

%%SECRET[4]%%