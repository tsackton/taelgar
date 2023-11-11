---
type: NPC
name: Warin the Woodsman
pronouciation:
aliases: []
tags:
- NPC/DuFr/unaware
- NPC/Clee/unaware
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1671
died:
gender: male
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 1671-01-02
  end: ''
  location: Valit, Sembara
lastSeenByParty: []
---
# Warin the Woodsman
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Valit]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A tracker and woodsman from [[Valit]], and confidant of [[Sabine de Brune]].

![[warin-the-woodsman.png]]