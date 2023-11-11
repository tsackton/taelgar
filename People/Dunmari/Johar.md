---
type: NPC
name: Johar
pronouciation:
aliases: []
tags:
- NPC/DuFr/major
- NPC/DuFr/met
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1721
died:
gender: male
pronouns:
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 1721-01-02
  end: ''
  location: Tokra, Central Dunmar
- type: away
  start: 1748-08-08
  end: ''
  location: Darba, Central Dunmar
- type: away
  start: 1748-08-27
  end: ''
  location: Nayahar, Western Dunmar
lastSeenByParty:
- date: 1748-11-15
  prefix: DuFr
---
# Johar
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests on November 15th, 1748: [[Nayahar]], [[Western Dunmar]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Johar is a confidant and close friend of [[Kenzo]]'s from the [[Lakan Monastery]] in [[Tokra]]. He works in the [[Tokra]] [[Archives]], primary interested in documenting the miracles of [[Laka]], and the history of the [[Lakan Monastery]] and the community there. 

%%SECRET[1]%%