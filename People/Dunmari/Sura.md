---
headerVersion: 2023.11.25
tags: [status/needswork/gameupdate, person, testcase]
campaignInfo:
- {campaign: DuFr, date: 1748-12-26, type: scryed}
name: Nayan Sura
born: 1720
species: human
ancestry: Dunmari
gender: female
aliases: [Nayan Sura]
affiliations: 
- {org: Nayan Dynasty, type: primary}
- {org: Eastern Dunmar, type: leader, start: 1748-07-22, title: Samraat }
whereabouts:
- {type: home, end: 1740, location: 'Darba'}
- {type: home, start: 1735, end: 1737, location: Lakan Monastery}
- {type: away, start: 1740, end: 1748-06-08, location: Mirror of Soul Trapping}
- {type: away, start: 1748-06-08, end: 1748-07-22, location: Karawa}
- {type: away, start: 1748-07-22, end: 1748-12-14, location: Central Dunmar}
- {type: away, start: 1748-12-14, end: 1748-12-22, location: Tokra}
- {type: away, start: 1748-12-22, end: 1748-12-26, location: plains south of Tokra}
dm_notes: important
dm_owner: tim
---
# Nayan Sura
>[!info]+ Biographical Info
> A [[Dunmar|Dunmari]] [[Humans|human]] (she/her), of the [[Nayan Dynasty|Nayan dynasty]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:DuFr%% Scryed by the [[Dunmar Fellowship]] on December 26th, 1748 on the [[~Southern Tokra Plains~|plains south of Tokra]], [[Dunmar]] %%^End%%

Nayan Sura is the younger sister of Samraat [[Nayan Karnas]]. Once seen as a future Samraat and a unifier of [[Eastern Dunmar|eastern]] and [[Western Dunmar]], she vanished eight years ago, trapped by [[Agata]] Dustmother in the [[Mirror of Soul Trapping]]. In her absence, her brother, [[Nayan Karnas]], claimed the throne of [[Dunmar]]. In DR 1748, Nayan Sura was freed from [[Agata]]'s imprisonment, and now seeks to reclaim her destiny. 
## Overview

Sura was born in [[Darba]], but traveled widely in her youth, including spending several years at the [[Lakan Monastery]] in [[Tokra]]. From a young age, she was seen as god-touched, and perceived as a potential heir to the Dunmari throne, one who could unite the eastern and western factions of the divided country. Her future was cut short in DR 1740, when she was just 20 years old: she was trapped by [[Agata]] Dustmother in the [[Mirror of Soul Trapping]], and vanished. In DR 1748, she was freed by [[Dunmar Fellowship]], and began to contemplate reclaiming the throne, especially in light of her perception that Karnas had neglected the east, most notably in his decision to leave the eastern nomads to their fate during the [[Summer Gnoll Raids of 1748]]. In December of DR 1748, she defeated a small force of Karnas' warriors and their Chardonian allies in the [[Battle of Tokra]], laying claim to central and [[Eastern Dunmar]]. 
## Description

![[sura.png|400]]

Sura is a tall, striking Dunmari woman, with high cheekbones, light brown skin, medium length dark hair, and a regal bearing. 
## Events

- Spent two years learning under the guidance of the [[Lakan Mystai]] at the monastery outside [[Tokra]], from DR 1735 - DR 1737. 
- Traversed across [[Eastern Dunmar]] in DR 1740 with the then Samraat, Nayan Marathu, as part of a great census of all [[Dunmar]], the first census to travel east in many years. Between [[Bas Udda]] and [[Askandi]], she was kidnapped by [[Agata]]'s servants - lured out of her tent by a magically disguised [[Orcs|orc]] and then knocked unconscious and brought to [[Gazetteer/Greater Dunmar/Hara Basin/Agata's Lair]] by [[Samerki]], where she was imprisoned in the [[Mirror of Soul Trapping]]. 
- Freed from the [[Mirror of Soul Trapping]] by [[Dunmar Fellowship]] in the summer of DR 1748. Seeing what seemed to be continued neglect of the needs of the east by her brother, she prepared to press her claim to rule, hopefully avoiding war and relying on the gods to give a clear sign of her favor. 
- Led her troops to victory against the Chardonian battle mages and a small group of Dunmari warriors loyal to Karnas during the [[Battle of Tokra]] on December 14th, 1748. 

%%SECRET[1]%%


```dataviewjs
await dv.view("_scripts/view/get_EventsTable", {   yearStart: 1,   yearEnd: 2000,   pageFilter: "\"People/Dunmari/Sura\"",  includeAll : true })
 ```

```dataview
LIST WITHOUT ID events.text from #timeline or #event-source  flatten file.lists as events where contains(events.text, this.file.name) sort events.DR
```

