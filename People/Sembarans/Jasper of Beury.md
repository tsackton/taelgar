---
type: NPC
name: Jasper
pronouciation:
aliases: []
tags:
- NPC/unsorted
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1680-09-21
died:
gender: male
pronouns:
ancestry:
species: Human
affiliations: []
family:
whereabouts:
- type: home
  start: null
  end: ''
  location: Beury, Sembara
lastSeenByParty:
- date: 1719-12-04
  prefix: Clee
---
# Jasper
>[!info]+ Biographical Summary
>Human, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Beury]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Jasper is a middle-aged ex-robber skilled in woodcraft, born on September 21st, 1680. He hails from Beury, a village near Cleenseau.
