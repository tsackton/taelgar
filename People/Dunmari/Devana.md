---
type: NPC
name: Devana
pronouciation:
aliases: []
tags:
- NPC/DuFr/background
- NPC/DuFr/aware
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
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: north and west of Karawa, Eastern Dunmar
lastSeenByParty: []
---
# Devana
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: north and west of Karawa, [[Eastern Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A Dunmari pastoralist from the area north and west of Karawa. 

In March 1748, his family was attacked by marauding axebeaks, supernaturally enraged by an ancient amulet from the Great War, which had been buried inactive for centuries until uncovered by [[Arcus]] in the old Dunmari fort east of Gomat. One of his sons and nearly half his animals were killed in this attack. 