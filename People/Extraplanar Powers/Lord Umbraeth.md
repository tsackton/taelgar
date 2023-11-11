---
type: NPC
name: Lord Umbraeth
pronouciation:
aliases:
- Gloomshaper
tags:
- NPC/unsorted
- NPC/DuFr/unaware
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born:
died:
gender: male
pronouns:
ancestry:
species: fey
affiliations: []
family:
whereabouts:
- type: home
  start: 0001-01-01
  end: ''
  location: Twilight's Grace, Feywild
- type: home
  start: 0001-01-02
  end: ''
  location: Duskmire, Feywild
lastSeenByParty:
- date: 0001-01-01
  prefix: null
---
# Lord Umbraeth
>[!info]+ Biographical Summary
>fey, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: Twilight's Grace, [[Feywild]]
>> Based in: [[Duskmire]], [[Feywild]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Lord Umbraeth, the Gloomshaper, is the ruler of [[Duskmire]]. 

![[Lord_Umbraeth_Potrait.png]]