---
type: NPC
name: Valius
pronouciation:
aliases: []
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
born: 1722
died:
gender: male
pronouns:
ancestry: Chardonian
species: human
affiliations:
- Chardonian Legion
- Society of the Open Scroll
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Chardon, Chardonian Empire
- type: home
  start: 1722-01-02
  end: ''
  location: Chardon, Chardonian Empire
- type: away
  start: 1748-12-09
  end: ''
  location: Trapped in the Mirror of Soul Trapping
lastSeenByParty:
- date: 1748-12-09
  prefix: DuFr
---
# Valius
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Chardon]], [[Chardonian Empire]]
>> Based in: [[Chardon]], [[Chardonian Empire]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 9th, 1748: Trapped in the Mirror of Soul Trapping %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A former mercenary and adventurer, Valius now finds himself ensnared by the machinations of [[Fausto]] and trapped in the [[Mirror of Soul Trapping]]. Alongside his twin, [[Vargus]], he once sought treasures and wealth, but now seeks only to free his brother from [[Fausto]]'s curse.
