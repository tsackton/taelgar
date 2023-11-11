---
type: NPC
name: Eleuha
pronouciation:
aliases: []
tags:
- NPC/DuFr/background
- NPC/DuFr/met_one
- status/uptodate
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
species: dryad
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: Azta Lekua, Orekatu
lastSeenByParty: []
---
# Eleuha
>[!info]+ Biographical Summary
>dryad, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Azta Lekua]], [[Orekatu]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A dryad of the jungle, daughter of a great tree, friend to [[Lengau]]. 