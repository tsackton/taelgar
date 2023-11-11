---
type: NPC
name: Akaston
pronouciation:
aliases: []
tags:
- NPC/historical
- NPC/DuFr/aware
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title: Emperor
born:
died: 911
gender: male
pronouns:
ancestry: Hkaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-01
  end: ''
  location: Drankor, Drankorian Empire
lastSeenByParty: []
---
# Emperor Akaston
>[!info]+ Biographical Summary
>human (Hkaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Drankor]], [[Drankorian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An Emperor of Drankor. Ruled during Hralgar's time. 