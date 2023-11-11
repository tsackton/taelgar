---
type: NPC
name: Dee Wildcloak
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
  location: somewhere, Sea of Storms
lastSeenByParty: []
---
# Dee Wildcloak
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Adventurer, funded by [[Fausto]] to explore. Part of the group that brought [[Hralgar's Eyes]] to [[Chardon]] from [[Stormcaller Tower]].

During the fall of DR 1748, fled Chardon for the unknown south. 