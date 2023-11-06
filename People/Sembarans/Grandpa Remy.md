---
type: NPC
name: Grandpa Remy
species: Human
ancestry: Sembaran
gender: male
born: 1640
died: 
lastSeenByParty: 
  - { date: 1719-10-23, prefix: Clee }
whereabouts: 
  - { date: 1640-04-09, place: Tavoise, region: Sembara, type: origin }
  - { date: 1719-10-23, place: Tavoise, region: Sembara, type: home }
---
# Grandpa Remy
>[!info]+ Biographical Summary
>Human (Sembaran), he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: Tavoise, [[Sembara]]
>> Based in: Tavoise, [[Sembara]]
>>%%^Campaign:Clee%% Last seen by the party at October 23rd, 1719: Tavoise, [[Sembara]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Grandpa Remy is well-liked for his off-color jokes and his fondness for apple brand.