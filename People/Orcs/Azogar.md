---
type: NPC
name: Azogar
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
- status/uptodate
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title: Loremaster
born: 1678
died:
gender: male
pronouns:
ancestry:
species: orc
affiliations:
- The People of the Rainbow
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Xurkhaz, Central Lowlands
- type: home
  start: 1678-01-02
  end: ''
  location: Uzgukar, Xurkhaz, Central Lowlands
lastSeenByParty:
- date: 1748-12-09
  prefix: DuFr
---
# Loremaster Azogar
>[!info]+ Biographical Summary
>[[Orcs|orc]], he/him
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Xurkhaz]], Central Lowlands
>> Based in: Uzgukar, [[Xurkhaz]], Central Lowlands
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 9th, 1748: Uzgukar, [[Xurkhaz]], Central Lowlands %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

Azogar is an old [[Orcs|orc]] loremaster from [[Xurkhaz]], one of the unchained [[Orcs]] of the [[People of the Rainbow]]. He has dark green skin, which is almost black in patches, and long, but thinning white hair. He is frail and uses a cane to walk. Generally prefers simple robes and understated dress. Although he speaks with a wavering voice, he is clear and precise in this language. 

Azogar is very knowledgable about the history of his people, and can tell many stories of the [[People of the Rainbow]], both before and after the founding of [[Xurkhaz]]. Serves as one of the primary advisors to [[Lubash]], the chief of [[Xurkhaz]]. 

%% SECRET
May potentially be a low-level wizard, although it didn't come up before
%%