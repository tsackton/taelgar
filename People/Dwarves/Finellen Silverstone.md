---
type: NPC
name: Finellen Silverstone
pronouciation:
aliases: []
tags:
- NPC/DuFr/background
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
species: dwarf
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: Darba, Western Dunmar
lastSeenByParty: []
---
# Finellen Silverstone
>[!info]+ Biographical Summary
>dwarf, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Darba]], [[Western Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A dwarven antiquities dealer in [[Darba]].