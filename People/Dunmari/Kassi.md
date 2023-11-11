---
type: NPC
name: Kassi
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
born: 1695
died:
gender: female
pronouns:
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 1695-01-02
  end: ''
  location: Lakan Monastery, Tokra, Central Dunmar
lastSeenByParty: []
---
# Kassi
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Lakan Monastery]], [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The librarian at the Lakan monastery in Tokra. 