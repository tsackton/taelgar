---
type: NPC
name: Dunmari werewolf woman
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
gender: female
pronouns:
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: Tokra, Central Dunmar
lastSeenByParty: []
---
# Dunmari werewolf woman
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The unnamed woman who was cured of lycanthropy by [[Riswynn]], one of the few survivors of the [[Fraternity of the Empty Moon]]. 