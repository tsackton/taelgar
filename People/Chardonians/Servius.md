---
type: NPC
name: Servius
pronouciation:
aliases: []
tags:
- NPC/DuFr/aware
- NPC/DuFr/major
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1689
died:
gender: male
pronouns:
ancestry: Chardonian
species: human
affiliations:
- Society of the Open Scroll
family:
whereabouts:
- type: home
  start: 1689-01-02
  end: ''
  location: Chardon, Chardonian Empire
- type: away
  start: 1748-11-23
  end: ''
  location: unknown, Illoria
lastSeenByParty: []
---
# Servius
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A wandering scholar and historian, funded by [[Fausto]] to find rumors of treasure. Currently hunting rumors of treasure in Illoria. 