---
type: NPC
name: Susanne Garay
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
born: 1666
died:
gender: female
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 1666-01-02
  end: ''
  location: Embry, Sembara
lastSeenByParty: []
---
# Susanne Garay
>[!info]+ Biographical Summary
>human (Sembaran), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Embry]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A wealthy cloth merchant from [[Embry]], she sponsors many causes including the [[Lord Mayor’s Workhouse]], an orphanage. 
