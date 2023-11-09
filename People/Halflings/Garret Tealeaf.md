---
type: NPC
name: Garret Tealeaf
species: halfling
ancestry: 
gender: male
born: 1656
died: 
affiliations: 
tags: [NPC/DuFr/met, NPC/DuFr/major]
title:
family: Tealeaf
yearOverride: 
lastSeenByParty: 
- { date: 1748-07-15, prefix: DuFr }
aliases: [Garret]
whereabouts:
  - { date: 1737-01-01, place: "Agata's lair", region: Garamjala Desert, type: excursion }
  - { date: 1748-06-08, place: "Karawa", region: Eastern Dunmar, type: excursion }
  - { date: 1748-06-08, place: "Karawa", region: Eastern Dunmar, type: excursion }
  - { date: 1748-06-30, place: "Tokra", region: Central Dunmar, type: excursion } 
###secret[1]
---
# Garret Tealeaf
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>>%%^Campaign:DuFr%% Last seen by The Side Quests at July 15th, 1748: [[Tokra]], [[Central Dunmar]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

%%SECRET[2]%%