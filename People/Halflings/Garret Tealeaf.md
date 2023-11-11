---
type: NPC
name: Garret Tealeaf
pronouciation:
aliases:
- Garret
tags:
- NPC/DuFr/met
- NPC/DuFr/major
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1656
died:
gender: male
pronouns:
ancestry:
species: halfling
affiliations: []
family: Tealeaf
whereabouts:
- type: away
  start: 1737-01-01
  end: ''
  location: Agata's lair, Garamjala Desert
- type: away
  start: 1748-06-08
  end: ''
  location: Karawa, Eastern Dunmar
- type: away
  start: 1748-06-08
  end: ''
  location: Karawa, Eastern Dunmar
- type: away
  start: 1748-06-30
  end: ''
  location: Tokra, Central Dunmar
- type: away
  start: 1748-08-13
  end: ''
  location: Darba, Western Dunmar
lastSeenByParty:
- date: 1748-07-15
  prefix: DuFr
---
# Garret Tealeaf
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>>%%^Campaign:DuFr%% Last seen by The Side Quests at July 15th, 1748: [[Tokra]], [[Central Dunmar]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

%%SECRET[1]%%