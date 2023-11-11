---
type: NPC
name: Anselm
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
born: 1655
died:
gender: male
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 1655-01-02
  end: ''
  location: Cleenseau, Sembara
- type: home
  start: 1719-10-21
  end: ''
  location: Cleenseau, Sembara
lastSeenByParty: []
---
# Anselm
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Cleenseau]], [[Sembara]]
>> Based in: [[Cleenseau]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The temple administrator of the [[Temple of the Warlord in Cleenseau|Temple of the Warlord]] in [[Cleenseau]]. An amibitious man and not very religious.

![[anselm-portrait.png]]