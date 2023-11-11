---
type: NPC
name: Aram
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1717
died:
gender: male
pronouns:
ancestry: Dunmari
species: human
affiliations:
- Havdar's Warband
family:
whereabouts:
- type: away
  start: 1748-11-15
  end: ''
  location: Sura's army camp, Central Dunmar
lastSeenByParty: []
---
# Aram
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A holy warrior of [[Aagir]] in [[Havdar]]'s service, and unofficial spiritual leader of [[Havdar's Warband]]
