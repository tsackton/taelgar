---
type: NPC
name: Fallthra Hardstone
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
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
species: dwarf
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: Tokra, Central Dunmar
lastSeenByParty: []
---
# Fallthra Hardstone
>[!info]+ Biographical Summary
>dwarf, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Matriach of the Hardstone clan; mother to [[Dag Hardstone]]. 