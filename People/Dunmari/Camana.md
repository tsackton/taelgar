---
type: NPC
name: Camana
pronouciation:
aliases: []
tags:
- NPC/DuFr/aware
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1721
died: 1748
gender: female
pronouns:
ancestry: Dunmari
species: human
affiliations:
- Havdar's Warriors
family:
whereabouts:
- type: home
  start: 1721-01-02
  end: ''
  location: Eastern Dunmar
- type: away
  start: 1748-05-01
  end: ''
  location: deceased, unknown
lastSeenByParty: []
---
# Camana
>[!info]+ Biographical Summary
>human (Dunmari), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Eastern Dunmar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A Dunmari warrior, archer, and scout. She is associated with [[Havdar]] and his warrior band, and functions as the leader of his scouting group. 

In May 1748, she died in battle fighting [[Orcs]] affiliated with [[Grash]] in the desert west of [[Kharsan]]. [[Havdar]] gifted her [[Flaming Bowstring]] to [[Wellby]] in thanks for the aid of [[The Dunmar Fellowship]] in battle. 