---
type: NPC
name: Unai
pronouciation:
aliases: []
tags:
- NPC/Clee/unaware
- NPC/DuFr/unaware
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1602
died:
gender: female
pronouns:
ancestry:
species: lizardfolk
affiliations: []
family:
whereabouts:
- type: home
  start: 1602-01-02
  end: ''
  location: Ganboa, Sembara
lastSeenByParty: []
---
# Unai
>[!info]+ Biographical Summary
>lizardfolk, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An herbalist and healer, teacher of [[Gentza]].

![[lizardfolk-unai.png]]