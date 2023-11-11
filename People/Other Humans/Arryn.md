---
type: NPC
name: Arryn
pronouciation:
aliases: []
tags:
- NPC/DuFr/met_one
- NPC/DuFr/minor
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
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Free City of Tollen, Greater Sembara
- type: away
  start: 1748-11-13
  end: ''
  location: unknown, Eastern Green Sea
lastSeenByParty: []
---
# Arryn
>[!info]+ Biographical Summary
>human, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: Free City of Tollen, Greater Sembara
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A wizard of significant power, originally from [[Tollen]]; dwells in a tower in the northern part of the isles. Fascinated by other dimensions, recently the hypothesized [[Mirror Realm]] in particular. Freed from the [[Mirror Realm]] by [[Wellby]], [[Alimash]], and [[Shoal]] during [[Session 57-58 (DuFr)|Wellby's adventures in the eastern Green Sea]]

![[arryn-the-wanderer-portrait.png|500]]