---
type: NPC
name: Crispus
pronouciation:
aliases: []
tags:
- NPC/DuFr/aware
- NPC/DuFr/minor
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1697
died:
gender: male
pronouns:
ancestry: Chardonian
species: human
affiliations:
- Great Library
family:
whereabouts:
- type: home
  start: 1697-01-02
  end: ''
  location: Chardon, Chardonian Empire
lastSeenByParty: []
---
# Crispus
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A senior Archivist at the [[Great Library]], in charge of external mercenary contracts, with general responsibility for organizing missions to recover lost treasures for the Great Library. 

%%SECRET[1]%%