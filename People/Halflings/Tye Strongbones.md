---
type: NPC
name: Tye Strongbones
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
born:
died:
gender: male
pronouns:
ancestry:
species: halfling
affiliations: []
family: Strongbones
whereabouts:
- type: home
  start: 0001-01-02
  end: ''
  location: Tokra, Central Dunmar
lastSeenByParty: []
---
# Tye Strongbones
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Tokra]], [[Central Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Son of [[Wes Strongbones]].