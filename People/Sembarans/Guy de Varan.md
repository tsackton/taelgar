---
type: NPC
name: Guy de Varan
pronouciation:
aliases: []
tags:
- NPC/DuFr/unaware
- NPC/Clee/unsorted
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1693
died:
gender: male
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family: de Varan
whereabouts:
- type: home
  start: null
  end: ''
  location: Evis, Duchy of Maseau
- type: away
  start: 1719-10-31
  end: ''
  location: Orc Fort, Duchy of Maseau
- type: away
  start: 1719-11-30
  end: ''
  location: Bandit's Way, Duchy of Maseau
- type: away
  start: 1719-12-01
  end: ''
  location: Cleenseau, Sembara
lastSeenByParty: []
---
# Guy de Varan
>[!info]+ Biographical Summary
>human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Evis]], [[Duchy of Maseau]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A traveler and caravan expediter, he is relatively well-known along [[Bandit's Way]] as a man who can help find guards and organize supplies. The de Varan family is well-known in [[Duchy of Maseau|Maseau]] and was originally from far southern [[Isingue]] before the Great War. 

![[guy-de-varan-maseau.png]]

%%% At times there have been rumors that he sometimes warns bandits of particularly lucrative caravan's coming along the road. But these rumors are disputed, and even his biggest detractors are careful to note that even the caravans he supposively targeted are never brutally attacked -- no deaths have been associated with these rumors %%