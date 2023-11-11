---
type: NPC
name: Herasto
pronouciation:
aliases: []
tags:
- NPC/DuFr/unaware
- NPC/GrLi/unsorted
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
species: centaur
affiliations: []
family:
whereabouts:
- type: away
  start: 1748-11-23
  end: ''
  location: plains south of Voltara, Voltara, Chardonian Empire
lastSeenByParty: []
---
# Herasto
>[!info]+ Biographical Summary
>centaur, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

%%Group of centaurs currently wintering in sheltered valleys south of Voltara%%