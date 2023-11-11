---
type: NPC
name: Vincent de Arban
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
born: 1677
died:
gender: male
pronouns:
ancestry: Sembaran
species: Human
affiliations:
- Garay Family
family:
whereabouts:
- type: home
  start: 1677-05-18
  end: ''
  location: Embry, Sembara
- type: away
  start: 1719-11-07
  end: ''
  location: Cleenseau, Sembara
- type: home
  start: 1719-11-22
  end: ''
  location: Embry, Sembara
lastSeenByParty:
- date: 1719-11-07
  prefix: Clee
---
# Vincent de Arban
>[!info]+ Biographical Summary
>Human, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Embry]], [[Sembara]]
>>%%^Campaign:Clee%% Last seen by the party at November 7th, 1719: [[Cleenseau]], [[Sembara]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Vincent de Arban is an agent of [[Susanne Garay]]. He visited [[Cleenseau]] to investigate [[Viepuck]] (when he was masquerading as [[Viepuck|Najeer Garay]]). 

He was extremely interested in Viepuck's spider silk scheme, and may return to see how it is faring. 