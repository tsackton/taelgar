---
type: NPC
name: Delig Hardstone
pronouciation:
aliases: []
tags:
- NPC/DuFr/background
- NPC/DuFr/met
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
affiliations:
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Tokra, Central Dunmar
lastSeenByParty: []
---
# Delig Hardstone
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Patriach of the Hardstone clan, father to [[Dag Hardstone]]. 