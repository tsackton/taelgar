---
tags: [dufr/met_one, person, dufr/minor]
displayDefaults: {startStatus: born, startPrefix: b., endPrefix: d., endStatus: died}
campaignInfo: []
name: Enari
born:
species: lizardfolk
ancestry:
gender: male
whereabouts:
- {type: home, start: "", end: '', location: 'Orekatu'}
- {type: away, start: 1748-11-01, end: 1749-12-01, location: 'Bedez, Orekatu'} #check start and end dates on session notes from Kenzo solo
---
# Enari
>[!info]+ Biographical Summary
>lizardfolk, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: unknown, [[Orekatu]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A well-muscled lizardfolk hunter and wanderer, who earned a reputation and honor traveling among the villages of the kingdom of [[Orekatu]]. Guided [[Kenzo]] and [[Izzarak]] to the [[Azta Lekua]], the [[Azta Lekua|Footprint of the Gods]], and returned to [[Bedez]] after they succeeded in their quest, to report to the elders of the kingdom. 

![[enari-portrait.png|400]]