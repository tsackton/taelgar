---
type: NPC
name: Dani Silversong
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
born:
died:
gender: female
pronouns:
ancestry:
species: halfling
affiliations: []
family:
whereabouts:
- type: away
  start: 1748-11-23
  end: ''
  location: traveling, Nevos Sea
lastSeenByParty: []
---
# Dani Silversong
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Quartermaster and chief trader on the [[Emerald Song]].
