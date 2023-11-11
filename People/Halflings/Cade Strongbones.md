---
type: NPC
name: Cade Strongbones
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1709
died:
gender: male
pronouns:
ancestry:
species: halfling
affiliations:
- Strongbones
family:
whereabouts:
- type: home
  start: 1709-01-02
  end: ''
  location: Tokra, Central Dunmar
lastSeenByParty: []
---
# Cade Strongbones
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Son of [[Wes Strongbones]], helps run [[The Red Lily Inn]] in [[Tokra]].
