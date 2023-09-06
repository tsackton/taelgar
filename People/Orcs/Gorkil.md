---
type: NPC
name: Gorkil
species: orc
ancestry: 
gender: male
born: 1729
died: 1748
affiliations:
  - Grash's Horde
aliases: []
title: 
family: 
tags:
  - NPC/DuFr/met
  - NPC/DuFr/background
  - status/uptodate
yearOverride: 
whereabouts:
  - date: 1729-01-02
    place: Kharsan
    region: Nashtkar
    type: home
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