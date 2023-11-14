---
tags: [dufr/background, status/uptodate, dufr/met_one, person]
displayDefaults: {startStatus: born, startPrefix: b., endPrefix: d., endStatus: died}
campaignInfo: []
name: Melusine
born:
species: fey
ancestry: nymph
gender: female
whereabouts:
- {type: home, start: 0001-01-02, end: '', location: 'Amberglow, Feywild'}
---
# Melusine
>[!info]+ Biographical Summary
>fey (nymph), she/her
>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`
>> Based in: [[Amberglow]], [[Feywild]]
>> `$=dv.view("_scripts/view/get_CurrentWhereabouts", {"config": await app.vault.adapter.read(app.vault.configDir + "/taelgarConfig.json")})`

A water nymph in [[Amberglow]]. She resides in a small, secluded grotto near a river, overgrown with vines and foliage. 

%%SECRET[1]%%