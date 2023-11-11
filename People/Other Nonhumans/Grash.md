---
type: NPC
name: Grash
pronouciation:
aliases: []
tags:
- NPC/DuFr/major
- NPC/DuFr/aware
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
ancestry: skeletal
species: undead
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: unknown, unknown
- type: home
  start: ''
  end: ''
  location: unknown, unknown
- type: away
  start: 1748-12-14
  end: ''
  location: Uzgukhar, Xurkhaz
lastSeenByParty: []
---
# Grash
>[!info]+ Biographical Summary
>undead (skeletal), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: unknown, unknown
>> Based in: unknown, unknown
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Known as Grash the Undying, an undead warrior and commander of a large [[Orcs|orc]] army in Kharsan.