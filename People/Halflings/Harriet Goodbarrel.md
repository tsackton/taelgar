---
type: NPC
name: Harriet 
species: halfling
ancestry: 
gender: female
born: 1685
died: 
family: Goodbarrel
affiliations:
  - "The Singing Fox"
aliases: []
tags:
  - NPC/DuFr/met
  - NPC/DuFr/background
lastSeenByParty: 
     - { date: 1748-12-30, prefix: DuFr }
whereabouts:
     - { date: 1685-01-01, place: "At Sea", region: "Western Gulf", type: origin}
     - { date: 1685-01-02, place: "At Sea", region: "Western Gulf", type: home}
     - { date: 1722-03-10, place: "Tollen", region: "Western Green Sea", type: home}
---
# Harriet
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: At Sea, [[Western Gulf]]
>> `$=dv.view("_scripts/view/get_HomeWhereabouts")`
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 30th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Harriet's melodious voice graces *[[The Singing Fox]]* on performance nights, drawing in patrons from all walks of life. Though initially reserved, she truly shines when on stage, and alongside her wife, Chenna, she's made the tavern a warm haven for many.

%%SECRET[1]%%

![[harriet-goodbarrel.png]]

