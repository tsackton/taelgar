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
     - { date: 1705-01-01, place: "Darba", region: Western Dunmar, type: origin }
     - { date: 1705-01-02, place: "Voltara", region: Chardonian Empire, type: home}
     - { date: 1748-11-23, place: "Chardon", region: Chardonian Empire, type: excursion }
---
# Lyra
>[!info]+ Biographical Summary
>human (Chardonian), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Darba]], [[Western Dunmar]]
>> Based in: [[Voltara]], [[Chardonian Empire]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at August 26th, 1748: [[Voltara]], [[Chardonian Empire]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`


An archivist with the Great Library, responsible for arranging adventuring expeditions to recover magic, knowledge, and treasure. Spend considerable time in the north of the [[Chardonian Empire]].

Friends with [[Roscelia]].

%%SECRET[1]%%