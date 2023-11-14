---
tags: []
displayDefaults: {startStatus: created, startPrefix: created, endPrefix: destroyed, endStatus: destroyed}
campaignInfo: []
name: test
pageTargetDate: 1399-11-06
destroyed: 1400
whereabouts:
- {type: home, location: Origin Place}
- {type: home, end: 1399-11-05, location: Home Place}
- {type: away, start: 1399-11-20, end: 1399-12-15, location: P1}
- {type: away, start: 1399-11-27, end: 1399-12-11, location: P2}
- {type: away, start: 1399-11-28, location: P3}
- {type: away, start: 1399-12-30, location: P4}
- {type: home, start: 1400, end: 1500, location: Home23}
---

Home whereabouts
```dataviewjs
await dv.view("_scripts/view/get_HomeWhereabouts")
```

Current Whereabouts

```dataviewjs
await dv.view("_scripts/view/get_CurrentWhereabouts")
```


Current
```dataviewjs
const {metadataUtils} = customJS
let target = metadataUtils.parse_date_to_events_date(dv.current().pageTargetDate);
dv.span(metadataUtils.get_currentWhereabouts(dv.current(), target))
```


Origin
```dataviewjs
const {metadataUtils} = customJS
let target = metadataUtils.parse_date_to_events_date(dv.current().pageTargetDate);
dv.span(metadataUtils.get_originWhereabouts(dv.current(), target))
```

Home
```dataviewjs
const {metadataUtils} = customJS
let target = metadataUtils.parse_date_to_events_date(dv.current().pageTargetDate);
dv.span(metadataUtils.get_homeWhereabouts(dv.current(), target))
```

Last Known
```dataviewjs
const {metadataUtils} = customJS
let target = metadataUtils.parse_date_to_events_date(dv.current().pageTargetDate, false);
dv.span(metadataUtils.get_lastKnownWhereabouts(dv.current(), target))
```


Exact
```dataviewjs
const {metadataUtils} = customJS
let target = metadataUtils.parse_date_to_events_date(dv.current().pageTargetDate, false);
dv.span(metadataUtils.get_exactWhereabouts(dv.current(), target))
```

Additional testing of campaign and date filters.

The following line should be removed:
%%^Date:1750%% hasn't happened %%^End%%

This block should also be removed:
%%^Date:1750%% 
hasn't happened 
%%^End%%

These should stay:
%%^Date:1110%% history stuff %%^End%%

%%^Date:1110%% 
history stuff %%^End%%

%%^Date:1110%% 
history stuff 
%%^End%%

This should stay in based on DuFr campaign:
%%^Campaign:DuFr%%Seeker event %%^End%%

SO SHOULD this:
%%^Campaign:DuFr%%
delwath does stuff
%%^End%%

This should be removed based on DuFr campaign
%%^Campaign:GrLi%%Adrik smash %%^End%%

%%^Campaign:GrLi%%
lily pads
%%^End%%

