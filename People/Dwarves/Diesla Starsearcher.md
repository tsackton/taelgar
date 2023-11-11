---
type: NPC
name: Diesla Starsearcher
pronouciation:
aliases: []
tags:
- NPC/Clee/unsorted
- NPC/DuFr/unaware
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1512
died:
gender: female
pronouns:
ancestry:
species: dwarf
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Ardith, unknown
- type: home
  start: 1512-01-02
  end: ''
  location: Taviose, Sembara
lastSeenByParty: []
---
# Diesla Starsearcher
>[!info]+ Biographical Summary
>dwarf, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Ardith]], unknown
>> Based in: [[Taviose]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

[[Brot Starsearcher]]'s wife, a respected metalsmith in [[Taviose]].