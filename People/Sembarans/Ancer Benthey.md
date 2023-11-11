---
type: NPC
name: Ancer Benthey
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
born: 1689
died:
gender: male
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family: Benthey
whereabouts:
- type: home
  start: ''
  end: ''
  location: Cleenseau, Sembara
- type: away
  start: ''
  end: ''
  location: Dunfry, Sembara
lastSeenByParty: []
---
# Ancer Benthey
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Cleenseau]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The nephew of [[Ames Benthey]], recently appointed sergeant of the [[Army Garrison of Cleenseau|Bridge Patrol]] after [[Odo Cordwaner]] was dismissed.