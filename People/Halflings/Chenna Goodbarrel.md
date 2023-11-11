---
type: NPC
name: Chenna
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1688
died:
gender: female
pronouns:
ancestry:
species: halfling
affiliations:
- The Singing Fox
family: Goodbarrel
whereabouts:
- type: home
  start: ''
  end: ''
  location: Sembara, Western Green Sea
- type: home
  start: 1722-03-10
  end: ''
  location: Tollen, Western Green Sea
lastSeenByParty:
- date: 1748-12-30
  prefix: DuFr
---
# Chenna
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Sembara]], [[Western Green Sea]]
>> Based in: [[Tollen]], [[Western Green Sea]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 30th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Together with her spouse, Harriet, Chenna runs the charming halfling tavern *The Singing Fox* in Fairgate Outer. Warm, welcoming, and charming, she's the heart of the establishment.

%%SECRET[1]%%

![[chenna-goodbarrel-portrait.png]]
