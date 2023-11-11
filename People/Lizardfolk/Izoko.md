---
type: NPC
name: Izoko
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
born: 1688
died:
gender: male
pronouns:
ancestry:
species: lizardfolk
affiliations: []
family:
whereabouts:
- type: home
  start: 1688-01-02
  end: ''
  location: Ganboa, Semabara
lastSeenByParty: []
---
# Izoko
>[!info]+ Biographical Summary
>lizardfolk, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], Semabara
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`


A young lizardfolk, sweet on [[Gentza]].
![[lizardfolk-Izoko.png]]