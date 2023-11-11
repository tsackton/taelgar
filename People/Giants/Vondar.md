---
type: NPC
name: Vondar
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
gender: male
pronouns:
ancestry: cursed
species: giant
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-01
  end: ''
  location: unknown, unknown
- type: away
  start: 1748-11-23
  end: ''
  location: unknown, Amberglow
lastSeenByParty: []
---
# Vondar
>[!info]+ Biographical Summary
>giant (cursed), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: unknown, unknown
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A cursed giant who guards the passes from [[Shimmersong]] into [[Amberglow]], asking for a toll of a memory in order to pass. Killed, but presumably not permanently, by [[Seeker]] and friends.