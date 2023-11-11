---
type: NPC
name: Conrad
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
born: 1699
died:
gender: male
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Cleenseau, Sembara
lastSeenByParty: []
---
# Conrad
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Cleenseau]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

[[Anselm|Anselm's]] assistant at the [[Temple of the Warlord in Cleenseau|Temple of the Warlord]]. 