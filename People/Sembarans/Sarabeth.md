---
type: NPC
name: Sarabeth
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
born: 1686
died:
gender: female
pronouns:
ancestry: Sembaran
species: human
affiliations: Lord's Guard of Cleenseau
family:
whereabouts:
- type: home
  start: null
  end: ''
  location: Dunfry, Sembara
- type: home
  start: null
  end: ''
  location: Cleenseau, Sembara
lastSeenByParty: []
---
# Sarabeth
>[!info]+ Biographical Summary
>human (Sembaran), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Dunfry]], [[Sembara]]
>> Based in: [[Cleenseau]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A senior guardswoman under [[Ysabel]] and veteran of the [[Army of the West]].