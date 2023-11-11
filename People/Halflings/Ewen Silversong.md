---
type: NPC
name: Ewen Silversong
pronouciation:
aliases: []
tags:
- NPC/DuFr/minor
- NPC/DuFr/met
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1649
died:
gender: male
pronouns:
ancestry:
species: halfling
affiliations:
- Emerald Song crew
family: Silversong
whereabouts:
- type: away
  start: 1748-08-26
  end: ''
  location: Chardon, Chardonian Empire
- type: away
  start: 1748-11-23
  end: ''
  location: unknown, Nevos Sea
lastSeenByParty: []
---
# Ewen Silversong
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Songmaster and storyteller on the [[Emerald Song]].