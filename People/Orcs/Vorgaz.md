---
type: NPC
name: Vorgaz
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
- status/uptodate
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title: Commander
born: 1707
died: 1748
gender: male
pronouns:
ancestry:
species: orc
affiliations:
- The People of the Rainbow
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Uzgukar, Xurkhaz
- type: home
  start: 1741-01-01
  end: ''
  location: Khumarz, Xurkhaz
lastSeenByParty:
- date: 1748-12-04
  prefix: DuFr
---
# Commander Vorgaz
>[!info]+ Biographical Summary
>orc, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: Uzgukar, [[Xurkhaz]]
>> Based in: [[Khumarz]], [[Xurkhaz]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 4th, 1748: [[Khumarz]], [[Xurkhaz]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Vorgaz was a skilled [[Orcs|orc]] warrior and the commander of the garrison at [[Khumarz]], on the western border of [[Xurkhaz]], known for his tactical brilliance but lack of political acumen. 

Killed in battle against Grash's armies on Dec 7th, 1748. 

%%SECRET[1]%%

