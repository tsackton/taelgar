---
type: NPC
name: Delig Firebrand
pronouciation:
aliases: []
tags:
- NPC/DuFr/minor
- NPC/DuFr/met_one
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
ancestry:
species: dwarf
affiliations: []
family:
whereabouts:
- type: away
  start: 1748-11-23
  end: ''
  location: Tharn Todor, Nardith
lastSeenByParty: []
---
# Delig Firebrand
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The cousin of [[Hagrim]], trapped in [[Morkalan]] for many years. During that time lost much of his memory and mind. Known as the Mad Priest.