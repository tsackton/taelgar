---
type: NPC
name: Gentza
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
born: 1681
died: 1719
gender: female
pronouns:
ancestry:
species: lizardfolk
affiliations: []
family:
whereabouts:
- type: home
  start: 1681-01-02
  end: ''
  location: Ganboa, Semabara
- type: away
  start: 1719-11-01
  end: ''
  location: deceased
lastSeenByParty: []
---
# Gentza
>[!info]+ Biographical Summary
>lizardfolk, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], Semabara
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An apprentice lizardfolk herbalist, said to be skilled at experimenting with remedies.

![[lizardfolk-gentza.png]]