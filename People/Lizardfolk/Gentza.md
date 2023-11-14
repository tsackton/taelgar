---
tags: [clee/unaware, person, dufr/unaware]
displayDefaults: {startStatus: born, startPrefix: b., endPrefix: d., endStatus: died}
campaignInfo: []
name: Gentza
born: 1681
species: lizardfolk
ancestry:
gender: female
died: 1719
whereabouts:
- {type: home, start: 1681-01-02, end: '', location: 'Ganboa, Semabara'}
- {type: away, start: 1719-11-01, end: '', location: deceased}
---
# Gentza
>[!info]+ Biographical Summary
>lizardfolk, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Ganboa]], Semabara
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An apprentice lizardfolk herbalist, said to be skilled at experimenting with remedies.

![[lizardfolk-gentza.png]]