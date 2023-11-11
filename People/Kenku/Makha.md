---
type: NPC
name: Makha
pronouciation:
aliases: []
tags:
- NPC/DuFr/met_one
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1712
died:
gender: male
pronouns:
ancestry: Islander
species: kenku
affiliations: []
family:
whereabouts:
- type: home
  start: 1712-01-02
  end: ''
  location: Wahacha, Vermillion Isles
lastSeenByParty: []
---
# Makha
>[!info]+ Biographical Summary
>kenku (Islander), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Wahacha]], [[Vermillion Isles]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The port master and unofficial town spokesperson for the kenku settlement of [[Wahacha]].  

![[makha.png|500]]