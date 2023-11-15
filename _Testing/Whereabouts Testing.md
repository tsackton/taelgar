---
pageTargetDate: 1503
whereabouts:
- { type: home, location: origin }
- { type: home, location: home }
- { type: away, start: 1500, location: trip }
---


```dataviewjs
const {WhereaboutsManager} = customJS
const {DateManager} = customJS
let target = DateManager.parse_date_to_events_date(dv.current().pageTargetDate, false);

let wb = WhereaboutsManager.getWhereabouts(dv.current(), target)

dv.paragraph("o: " + wb.origin?.location ?? "unknown")
dv.paragraph("h: " + wb.home?.location ?? "unknown")
dv.paragraph("c: " + wb.current?.location ?? "unknown")
dv.paragraph("lk: " + wb.lastKnown?.location ?? "unknown")
```
