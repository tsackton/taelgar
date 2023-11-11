---
type: NPC
name: Wendel Quickstep
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1671
died:
gender: male
pronouns:
ancestry:
species: halfling
affiliations: []
family: Quickstep
whereabouts:
- type: home
  start: ''
  end: ''
  location: Tollen, Western Green Sea
- type: home
  start: 1671-01-02
  end: ''
  location: Tollen, Western Green Sea
lastSeenByParty:
- date: 1748-12-30
  prefix: DuFr
---
# Wendel Quickstep
>[!info]+ Biographical Summary
>halfling, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Tollen]], [[Western Green Sea]]
>> Based in: [[Tollen]], [[Western Green Sea]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 30th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Proprietor of *The Windward Sail*, a busy sailor's tavern in Fiskurth. Known as a place for tales and stories - some true, many not - and a place for gossip, as well as a place to find a crew. Has a few dirty, cramped rooms stacked with "human sized" bunks, and some slightly more comfortable halfling rooms. 

Friends with [[Wellby]], who hung around The Windward Sail in his youth.

%%SECRET[1]%%

![[wendel-quickstep.png]]