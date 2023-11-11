---
type: NPC
name: Jane Chapman
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
title: Captain
born: 1715
died:
gender: female
pronouns:
ancestry: Tollender
species: human
affiliations:
- Dyer's Guild
family: Chapman
whereabouts:
- type: home
  start: ''
  end: ''
  location: Tollen, Western Green Sea
- type: home
  start: '1715-01-02'
  end: ''
  location: Tollen, Western Green Sea
lastSeenByParty:
- date: '1748-12-30'
  prefix: DuFr
---
# Captain Jane Chapman
>[!info]+ Biographical Summary
>human (Tollender), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Tollen]], [[Western Green Sea]]
>> Based in: [[Tollen]], [[Western Green Sea]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 30th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A Tollender-born woman in her early 30s, from the well-off and well-established Chapman merchant family, Jane became a Dyer's Guild captain known for her skill and her luck at sea. 

%%SECRET[1]%%