---
type: NPC
name: Odo Cordwaner
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
title: Sergeant
born: 1700
died:
gender: male
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: null
  end: ''
  location: Cleenseau, Sembara
- type: away
  start: 1719-10-21
  end: ''
  location: Taviose, Cleenseau
lastSeenByParty: []
---
# Sergeant Odo Cordwaner
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Cleenseau]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The sergeant of the [[Army Garrison of Cleenseau|Bridge Patrol]] and a loyal solider. 
![[odo-cordwaner.png]]