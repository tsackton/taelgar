---
pageTargetDate: 1399-12-10
whereabouts:
- {type: home, location: Origin Place }
- {type: home, end: 1399-11-05, location: Home Place }
- {type: away, start: 1399-11-20, end: 1399-12-15, location: P1 }
- {type: away, start: 1399-11-27, end: 1399-12-11, location: P2 }
- {type: away, start: 1399-11-28, location: P3 }
- {type: away, start: 1399-12-30, location: P4 }
- {type: home, start: 1400, end: 1500, location: Home23 }
---

```dataviewjs
await dv.view("_scripts/view/get_Homewhereabouts")
```

Origin
```dataviewjs
const {metadataUtils} = customJS
let target = metadataUtils.parse_date_to_events_date(dv.current().yearOverride);
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
