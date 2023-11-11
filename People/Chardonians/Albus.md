---
type: NPC
name: Albus
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
born: 1694
died:
gender: male
pronouns:
ancestry: Chardonian
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Chardon, Chardonian Empire
- type: home
  start: 1694-01-02
  end: ''
  location: Darba, Western Dunmar
lastSeenByParty: []
---
# Albus
>[!info]+ Biographical Summary
>human (Chardonian), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Chardon]], [[Chardonian Empire]]
>> Based in: [[Darba]], [[Western Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A Chardonian bookseller who lives and works in [[Darba]]. Well connected to the local academic community. 
%%^Date:1748-08-05%%
In August 1748, came to the attention of [[The Dunmar Fellowship]] when he purchased the Lyrics of a New Age (a book of elvish poetry by Nelawe) from Delwath, and passed along rumors of Servius. 
%%^End%%

