---
type: NPC
name: Ikram
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
born: 1710
died:
gender: male
pronouns:
ancestry: Dunmari
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: 1710-01-02
  end: ''
  location: Karawa, Eastern Dunmar
lastSeenByParty: []
---
# Ikram
>[!info]+ Biographical Summary
>human (Dunmari), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Karawa]], [[Eastern Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The owner of the caravanserai in Karawa, the eponymously named [[Ikram’s]]. He is proud of his establishment, the food and drink it serves, and the commerce it attracts. Perennially optimistic, sociable, and friendly. Always ready with a drink and a story, to tell or to hear; prone to gossip and particularly fond of travelers and new stories. 

%%SECRET[1]%%