---
type: NPC
name: Grandpa Remy
pronouciation:
aliases: []
tags: []
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1640
died:
gender: male
pronouns:
ancestry: Sembaran
species: Human
affiliations: []
family:
whereabouts:
- type: home
  start: 1640-04-09
  end: ''
  location: Tavoise, Sembara
- type: home
  start: 1719-10-23
  end: ''
  location: Tavoise, Sembara
lastSeenByParty:
- date: 1719-10-23
  prefix: Clee
---
# Grandpa Remy
>[!info]+ Biographical Summary
>Human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: Tavoise, [[Sembara]]
>> Based in: Tavoise, [[Sembara]]
>>%%^Campaign:Clee%% Last seen by the party at October 23rd, 1719: Tavoise, [[Sembara]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Grandpa Remy is well-liked for his off-color jokes and his fondness for apple brand.