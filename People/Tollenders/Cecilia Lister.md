---
type: NPC
name: Cecilia Lister
species: human
ancestry: Tollender
gender: female
born: 1694
died: 
title: 
family: 
affiliations:
  - Dyer's Guild
aliases: 
tags:
  - NPC/DuFr/met
  - NPC/DuFr/minor
lastSeenByParty: 
     - { date: "1748-12-30", prefix: "DuFr" }
whereabouts:
     - { date: "1694-01-01", place: "Tollen", region: "Western Green Sea", type: "origin" }
     - { date: "1694-01-02", place: "Tollen", region: "Western Green Sea", type: "home" }
---
# Cecilia Lister
>[!info]+ Biographical Summary
>human (Tollender), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Tollen]], [[Western Green Sea]]
>> Based in: [[Tollen]], [[Western Green Sea]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 29th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An elegant older woman, very precise, who runs an unmarked but well-known tattoo parlor in Southbridge in [[Tollen]]. Important in the [[Dyer's Guild]], and rich. Extremely skilled in the arts of tattoos, especially magical tattoos made with enchanted dyes.

%%SECRET[1]%%

![[cecilia-lister-portrait.png]]
