---
type: NPC
name: Arrosa
pronouciation:
aliases: []
tags:
- NPC/DuFr/met_one
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born:
died:
gender: female
pronouns:
ancestry:
species: lizardfolk
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Bedez, Orekatu
lastSeenByParty: []
---
# Arrosa
>[!info]+ Biographical Summary
>lizardfolk, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Bedez]], [[Orekatu]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A lizardfolk elder, the matriarch of the village of [[Bedez]], in the Kingdom of [[Orekatu]]. 