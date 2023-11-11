---
type: NPC
name: Cecilia Lister
pronouciation:
aliases: []
tags:
- NPC/DuFr/met
- NPC/DuFr/minor
pageTargetDate:
endStatus: died
endPrefix: d.
startStatus: born
startPrefix: b.
preExistError: '**(not yet born)**'
title:
born: 1694
died:
gender: female
pronouns:
ancestry: Tollender
species: human
affiliations:
- Dyer's Guild
family:
whereabouts:
- type: home
  start: ''
  end: ''
  location: Tollen, Western Green Sea
- type: home
  start: '1694-01-02'
  end: ''
  location: Tollen, Western Green Sea
lastSeenByParty:
- date: '1748-12-30'
  prefix: DuFr
---
# Cecilia Lister
>[!info]+ Biographical Summary
>human (Tollender), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Originally from: [[Tollen]], [[Western Green Sea]]
>> Based in: [[Tollen]], [[Western Green Sea]]
>>%%^Campaign:DuFr%% Last seen by The Side Quests at December 29th, 1748: [[Tollen]], [[Western Green Sea]] %%^End%%
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

An elegant older woman, very precise, who runs an unmarked but well-known tattoo parlor in Southbridge in [[Tollen]]. Important in the [[Dyer's Guild]], and rich. Extremely skilled in the arts of tattoos, especially magical tattoos made with enchanted dyes.

%%SECRET[1]%%

![[cecilia-lister-portrait.png]]
