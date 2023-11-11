---
type: NPC
name: Gorkil
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/background
- status/uptodate
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1729
died: 1748
gender: male
pronouns:
ancestry:
species: orc
affiliations:
- Grash's Horde
family:
whereabouts:
- type: home
  start: 1729-01-02
  end: ''
  location: Kharsan, Nashtkar
lastSeenByParty: []
---
# Gorkil
>[!info]+ Biographical Summary
>[[Orcs|orc]], he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Kharsan]], [[Nashtkar]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An [[Orcs|orc]] cleric in [[Grash's Horde|Grash's army]]. 

%%^Campaign:DuFr%%
Captured in battle in May 1748 by [[The Dunmar Fellowship]], and interrogated before using magic to convince [[Seeker]] to kill him, seemingly because he insisted he could not die under [[Grash]]'s power. After his death, his body was burned and did not reanimate. 
%%^End%%