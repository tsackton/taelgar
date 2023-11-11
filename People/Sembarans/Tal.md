---
type: NPC
name: Tal
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
born:
died:
gender: male
pronouns:
ancestry:
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Embry, Sembara
- type: away
  start: 1719-10-21
  end: ''
  location: somewhere, River Semb, Sembara
lastSeenByParty: []
---
# Tal
>[!info]+ Biographical Summary
>human, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Embry]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An orphan and friend of [[Viepuck|Viepuck]], from [[Embry]]. He is currently working as a cabin boy and riverboat hand on the [[Semb]].