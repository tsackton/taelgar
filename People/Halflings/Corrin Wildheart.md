---
type: NPC
name: Corrin Wildheart
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
gender: male
pronouns:
ancestry:
species: hafling
affiliations: []
family:
whereabouts:
- type: away
  start: 1748-11-23
  end: ''
  location: unknown, Eastern Green Sea
lastSeenByParty: []
---
# Corrin Wildheart
>[!info]+ Biographical Summary
>hafling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Halfling man in his prime. Navigator, with a touch of weather magic. Part of the crew of the [[Wave Dancer]].
