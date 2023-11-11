---
type: NPC
name: Lyra
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
- NPC/GrLi/met
- NPC/GrLi/major
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1705
died:
gender: female
pronouns:
ancestry: Chardonian
species: human
affiliations:
- Great Library
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Darba, Western Dunmar
- type: home
  start: 1705-01-02
  end: ''
  location: Voltara, Chardonian Empire
- type: away
  start: 1748-11-23
  end: ''
  location: Chardon, Chardonian Empire
lastSeenByParty:
- date: 1748-08-26
  prefix: DuFr
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