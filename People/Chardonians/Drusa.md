---
type: NPC
name: Drusa
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
born: 1711
died:
gender: female
pronouns:
ancestry: Chardonian
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Chardon, Chardonian Empire
- type: away
  start: 1748-05-01
  end: ''
  location: Tokra, Central Dunmar
lastSeenByParty: []
---
# Drusa
>[!info]+ Biographical Summary
>human (Chardonian), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A Chardonian wizard on loan to the Dunmari army of [[Nayan Karnas]], commanded by [[Illyan]], in [[Tokra]]. 

Does not particularly like the party given their attempt to scry on [[Illyan]], which Drusa detected, and their refusal to agree to simple magic protocols. 