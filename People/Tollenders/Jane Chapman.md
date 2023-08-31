---
type: NPC
name: Jane Chapman
species: human
ancestry: Tollender
gender: female
born: 1715
died: 
title: Captain
family: Chapman
affiliations:
  - Dyer's Guild
aliases: 
tags:
  - NPC/DuFr/met
  - NPC/DuFr/background
lastSeenByParty: 
     - { date: "1748-12-30", prefix: "DuFr" }
whereabouts:
     - { date: "1715-01-01", place: "Tollen", region: "Western Green Sea", type: "origin" }
     - { date: "1715-01-02", place: "Tollen", region: "Western Green Sea", type: "home" }
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