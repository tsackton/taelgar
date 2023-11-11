---
type: NPC
name: Nika Hyne
pronouciation:
aliases:
- Nika
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1728
died:
gender: female
pronouns:
ancestry: Tollender
species: human
affiliations: []
family: Hyne
whereabouts:
- type: home
  start: 1730-01-01
  end: ''
  location: Fiskurth, Tollen, Western Green Sea
- type: home
  start: 1730-01-02
  end: ''
  location: Tollen, Western Green Sea
lastSeenByParty:
- date: 1748-12-17
  prefix: DuFr
---
# Nika Hyne
>[!info]+ Biographical Summary
>human (Tollender), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Fiskurth]], [[Tollen]], [[Western Green Sea]]
>> Based in: [[Tollen]], [[Western Green Sea]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 17th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Nika Hyne, is a sly young woman in her early twenties known to frequent The Windward Sail, listening to stories and doing odd jobs for coin. She was a student at the [[University of Tollen]]: although she dropped out, she knows the area and the people well. She is a bit of a hustler. 

%%SECRET[1]%%

![[nika-hyne.png]]