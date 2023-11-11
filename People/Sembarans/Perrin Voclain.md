---
type: NPC
name: Perrin Voclain
pronouciation:
aliases: []
tags:
- NPC/Clee/unsorted
- NPC/DuFr/unaware
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1659
died:
gender: male
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Taviose, Sembara
- type: away
  start: 1719-10-21
  end: ''
  location: Valit, Sembara
lastSeenByParty:
- date: 1719-10-20
  prefix: Clee
---
# Perrin Voclain
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Taviose]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Perrin Voclain is a sage and druid who lives in [[Taviose]]. He is known for his friendship with the animals of [[Cleenseau Wood|the Wood]].

![[perrin-the-druid.png]]