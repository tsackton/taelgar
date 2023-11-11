---
type: NPC
name: Pearl Brightmoon
pronouciation:
aliases: []
tags:
- NPC/DuFr/met_one
- NPC/DuFr/background
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born:
died:
gender: female
pronouns:
ancestry:
species: halfling
affiliations: Sea
family:
whereabouts:
- type: away
  start: 1748-11-23
  end: ''
  location: unknown, Eastern Green
lastSeenByParty: []
---
# Pearl Brightmoon
>[!info]+ Biographical Summary
>halfling, she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Halfing woman in her prime. Captain of the guard and first mate. Buff, good with a rapier. Cousin to [[Wella Brightmoon|Wella]] by blood and [[Rose Brightmoon|Rose]] by marriage. 