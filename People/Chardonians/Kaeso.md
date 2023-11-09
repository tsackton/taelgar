---
type: NPC
name: Kaeso
species: human
ancestry: Chardonian
gender: male
born: 1691
died: 
affiliations: ["Shakun Mystai"]
aliases: []
tags: [NPC/DuFr/minor, NPC/DuFr/met]
family:
title:
lastSeenByParty: 
- { date: 1748-10-23, prefix: DuFr }
whereabouts:
 - { date: 1691-01-01, place: "Chardon", region: Chardonian Empire, type: origin }
 - { date: 1691-01-02, place: "Chardon", region: Chardonian Empire, type: home }
 - { date: 1713-01-01, place: "traveling", region: Dunmar, type: excursion}
 - { date: 1717-01-01, place: "Karawa", region: Eastern Dunmar, type: excursion}
 - { date: 1719-01-01, place: "traveling", region: "The Central Highlands Region", type: excursion}
 - { date: 1723-01-01, place: "Chardon", region: Chardonian Empire, type: home }
 - { date: 1748-09-10, place: "traveling", region: Chardonian Empire, type: excursion}
 - { date: 1748-10-12, place: "Hamri", region: "Mawakel Peninsula", type: excursion}
---
# Kaeso
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_HomeWhereabouts")`
>>%%^Campaign:DuFr%% Last seen by The Side Quests at October 23rd, 1748: [[Hamri]], [[Mawakel Peninsula]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

[[Kenzo]]'s mentor and friend. A Chardonian, but widely traveled. Former student of [[Roscelia]] and member of the [[Society of the Open Scroll]], but expelled for keeping secrets, specifically about Dunmari magic. 

Secretly a member of the [[Shakun Mystai]]. 