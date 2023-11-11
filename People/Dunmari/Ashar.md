---
type: NPC
name: Ashar
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
born: 1688
died:
gender: male
pronouns:
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Tokra, Central Dunmar
- type: home
  start: 1688-01-02
  end: ''
  location: Tokra, Central Dunmar
lastSeenByParty: []
---
# Ashar
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Tokra]], [[Central Dunmar]]
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An old Dunmari solider from [[Tokra]], who fought in the [[Summer of Red Storms]], lost an eye, and retired to drink and reminisce with his war buddies. Spends a lot of time at [[Darshana’s caravanserai]] in [[Tokra]].
