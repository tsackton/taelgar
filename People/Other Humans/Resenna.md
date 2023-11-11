---
type: NPC
name: Resenna
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
born: 1724
died:
gender: female
pronouns:
ancestry:
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Medju, Eastern Green Sea
- type: away
  start: 1748-11-23
  end: ''
  location: sea elf village, Quanyi, Eastern Green Sea
lastSeenByParty: []
---
# Resenna
>[!info]+ Biographical Summary
>human, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Medju]], [[Eastern Green Sea]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Young woman, from Medju. Apprentice to [[Arryn]]. Fled when he vanished into [[Mirror Realm]]; was trapped and enslaved by aboleth. Now dwelling with sea elves until aboleth curse can be removed. 

![[resenna.png|400]]