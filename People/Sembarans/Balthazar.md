---
type: NPC
name: Balthazar
pronouciation:
aliases: []
tags:
- null
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1705-03-15
died:
gender: male
pronouns:
ancestry:
species: Human
affiliations:
- null
family:
whereabouts:
- type: home
  start: null
  end: ''
  location: Evis, Duchy of Maseau
- type: home
  start: 1719-12-06
  end: ''
  location: Cleenseau, Sembara
lastSeenByParty:
- date: 1719-12-04
  prefix: Clee
---
# Balthazar
>[!info]+ Biographical Summary
>Human, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Evis]], [[Duchy of Maseau]]
>> Based in: [[Cleenseau]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Balthazar is a young boy, born on March 15th, 1705, hailing from Evis in the Duchy of Maseau. He possesses a bright intellect but appears malnourished, bearing the marks of recent captivity by orcs. He has been in Cleenseau since December 6th, 1719.
