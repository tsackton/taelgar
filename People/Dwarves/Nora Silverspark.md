---
type: NPC
name: Nora Silverspark
pronouciation:
aliases:
- Nora
tags:
- NPC/DuFr/minor
- NPC/DuFr/met_one
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
species: dwarf
affiliations: []
family:
whereabouts:
- type: away
  start: 1748-11-23
  end: ''
  location: deceased, unknown
lastSeenByParty: []
---
# Nora Silverspark
>[!info]+ Biographical Summary
>dwarf, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A dwarven warrior, once a ghost in [[Morkalan]] and now passed on. The first victim of [[Hagrim]]'s betrayal. 
