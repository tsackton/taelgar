---
type: NPC
name: Shandan
pronouciation:
aliases: []
tags:
- NPC/DuFr/aware
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1692
died:
gender: male
pronouns:
ancestry: Dunmari
species: human
affiliations:
- Shandan's Warband
family:
whereabouts:
- type: home
  start: 1692-01-02
  end: ''
  location: plains east of Songara, Central Dunmar
lastSeenByParty: []
---
# Shandan
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: plains east of Songara, [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A charismatic leader of a warband based near [[Songara]]. 