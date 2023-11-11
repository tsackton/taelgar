---
type: NPC
name: Mermin Stonebridge
pronouciation:
aliases: []
tags:
- NPC/DuFr/unaware
- NPC/Clee/unsorted
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born:
died:
gender: male
pronouns:
ancestry:
species: halfling
affiliations: []
family: Stonebridge
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: Cleanseau
lastSeenByParty: []
---
# Mermin Stonebridge
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: Cleanseau
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A young halfling and broker based out of Cleanseau, although he travels between Sembara and Cleanseau somewhat regularly. 

He was working with [[Gentza]] to potentially sell her remedy before she died.
