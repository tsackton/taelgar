---
type: NPC
name: Faldrak Bronzehammer
species: dwarf
ancestry: 
gender: male
born: 1516 # Calculated as current year (1749) minus 183
died: 
title: 
family: Bronzehammer
affiliations: 
aliases: 
tags: 
  - NPC/DuFr/met
  - NPC/DuFr/minor
lastSeenByParty: 
  - { date: 1748-12-30, prefix: DuFr } # Please replace YYYY-MM-DD with the actual date
whereabouts: 
  - { date: 1516-01-01, place: "Fahnukan", region: "", type: origin }
  - { date: 1516-01-02, place: "Fahnukan", region: "", type: home }
  - { date: 1693-01-01, place: "Feywild", region: "", type: excursion } # Began his journey to Feywild at age 127
  - { date: 1698-01-01, place: "Feywild", region: "", type: excursion } # Ended his journey from Feywild after five years
  - { date: 1727-01-02, place: "Tollen", region: "", type: home } # Moved to Tollen at age 161
---
# Faldrak Bronzehammer
>[!info]+ Biographical Summary
>dwarf, he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Fahnukan]]
>> `$=dv.view("_scripts/view/get_HomeWhereabouts")`
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 30th, 1748: [[Tollen]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Faldrak Bronzehammer is an aged dwarf runecrafter and tinker, with a touch of Feywild whimsy.
## Overview

Faldrak Bronzehammer, with his eccentric blend of traditional dwarven craftsmanship and fey magic, has become a subject of both admiration and curiosity. Born in Fahnukan, a strange northern dwarven kingdom, his life took an unexpected turn during an accidental sojourn in the Feywild. Although he emerged with peculiar behaviors, his enhanced craft bearing fey enchantments has left many in awe.
## Description

Despite his aging exterior and graying, rune-braided beard, Faldrak's eyes sparkle with mischief. His wardrobe—a combination of dwarven armor and fey fabrics—reflects his diverse experiences. A small pouch, perpetually moving, is always by his side. He walks with a cane, which seems to be magical and multipurpose. 
## Events

- In DR 1748, during [[Pyravela]] in [[Tollen]], Faldrak attended the party hosted by The Dunmar Fellowship on [[Vindristjarna]], where he met and bonded with Seeker, requesting his aid in journeying to the Edge of Echoes, a mysterious place where the boundaries between the planes (especially between Taelgar and the elemental planes) are thin. 

%%SECRET[1]%%