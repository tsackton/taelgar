---
type: NPC
name: Jorma
pronouciation:
aliases: []
tags:
- NPC/DuFr/aware
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1716
died: 1748
gender: male
pronouns:
ancestry: Skaer
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Skaerhem
- type: home
  start: 1737-01-02
  end: ''
  location: Vetta, Skaerhem
lastSeenByParty: []
---
# Jorma
>[!info]+ Biographical Summary
>human (Skaer), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Skaerhem]]
>> Based in: [[Vetta]], [[Skaerhem]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Jorma, a Skaer priest in his early 30s, served as the Priest of the Waters in [[Vetta]]. He was killed by [[Urgall the Black]] in May 1748.