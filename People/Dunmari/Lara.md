---
type: NPC
name: Lara
pronouciation:
aliases: []
tags:
- NPC/DuFr/minor
- NPC/DuFr/met
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1707
died:
gender: female
pronouns:
ancestry: Dunmari
species: human
affiliations:
- Lakan Mystai
family:
whereabouts:
- type: home
<<<<<<< HEAD
  start: ''
=======
  start: 1707-01-02
>>>>>>> 51f7760 (massive metadata cleanup and update)
  end: ''
  location: Lakan Monastery, Tokra, Central Dunmar
lastSeenByParty: []
---
# Lara
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Lakan Monastery]], [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The leader of the [[Lakan Mystai]] in Tokra.
