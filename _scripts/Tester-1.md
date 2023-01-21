---
type: Ruler
name: Tester
species: human
ancestry:
gender: male
born: 1700
reignStart: 1717
died: 1718
endStatus: petrified
affiliations: ["Great Library"]
aliases: []
tags: [NPC/testing]
yearOverride: 
reignEnd:
title:
family:
lastSeenByParty: 
     - { date: 1701-02-03, prefix: clee }
     - { date: 1719-02-03,  prefix: DuFr }
whereabouts:
     - { place: "Home District, Chardon", region: Chardonian Empire, type: origin}
     - {  date:1700-01-01place: "Whitsun District, Chardon", region: Chardonian Empire, type: home}
     - { date: 1717-01-01, place: "mysterious inn, CityName", region: Mawar, type: home }        
     - { date: 1728-05-01, place: "Amberglow", region: Feywild, type: excursion }   
---
# Tester
>[!info]+ Biographical Summary
>human, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>`$=dv.view("_scripts/view/get_RegnalValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: Home District, [[Chardon]], [[Chardonian Empire]]
>> `$=dv.view("_scripts/view/get_HomeWhereabouts")`
>>%%Campaign:DuFr%% Last seen by The Side Quests at February 3rd, 1719: mysterious inn, [[CityName]], Mawar %%End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`


some text


>[!info]+ Location History
> On January 1st, 1700: Home District, [[Chardon]], [[Chardonian Empire]]
> On January 2nd, 1700: Whitsun District, [[Chardon]], [[Chardonian Empire]]
>> 
> On January 1st, 1717 a trip to: mysterious inn, CityName, Mawar
> On January 1st, 1718 a trip to: [[Amberglow]], [[Feywild]]
=======
sad asdlk

%%^Campaign:dufr%% Keep this %%^End%%

%%^Campaign:clee%% Remove this %%^End%%

>>%%^Campaign:dufr%% Keep this %%^End%%
%%^Date:1755%%
Shouldn't see this
%%^End%%

