---
type: NPC
name: Sabine de Brune
pronouciation:
aliases: []
tags:
- NPC/DuFr/unaware
- NPC/Clee/aware
- NPC/Clee/minor
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1662
died:
gender: female
pronouns:
ancestry: Sembaran
species: human
affiliations: []
family:
whereabouts:
- type: home
  start: null
  end: ''
  location: Valit, Sembara
lastSeenByParty: []
---
# Sabine de Brune
>[!info]+ Biographical Summary
>human (Sembaran), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Valit]], [[Sembara]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

The aging castellan of [[Valit]], a vassal of the [[Baron of Aveil]]. Organized about managing the manor, but with a soft spot for bardic tales and romance. Never married, although is rumored to have had several great loves in her youth.

![[sabine-de-brune-valit.png]]