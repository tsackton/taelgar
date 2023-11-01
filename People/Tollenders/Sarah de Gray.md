---
type: NPC
name: Sarah de Grey
species: human
ancestry: Isinguer
gender: female
born: 1733 
died: 
title: 
family: de Grey
affiliations: 
aliases: 
tags: 
  - NPC/DuFr/met
  - NPC/DuFr/background
lastSeenByParty: 
  - { date: 1748-12-29, prefix: DuFr } # Please replace YYYY-MM-DD with the actual date
whereabouts: 
  - { date: 1733-01-01, place: "", region: "Duchy of Maseau", type: origin }
  - { date: 1746-01-01, place: "Tollen", region: "Western Green Sea", type: home }
---
# Sarah de Grey
>[!info]+ Biographical Summary
>human (Isinguer), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Duchy of Maseau]]
>> Based in: [[Tollen]], [[Western Green Sea]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 29th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Sarah de Grey, a 16-year-old from the distinguished Isinguer family, is a student at the University of [[Tollen]]. Originally from the [[Duchy of Maseau]] in the south, she has come to [[Tollen]] to study, and has developed connections to the Insinguer community in the city, especially [[Guy Marchand]].  

%%SECRET[1]%%

![[sarah-de-gray.png]]