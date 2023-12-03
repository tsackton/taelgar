# Unlinked Whereabouts

```dataviewjs
const {util} = customJS

dv.table(["File", "Location"], 
		dv.pages().where(b=>b.whereabouts).
		flatMap(page => dv.array(page.whereabouts).map(w => {return {f: page.file.name, w: (dv.isArray(page.whereabouts) ? w.location : w) }})).
		where(f => !util.isLinked(f.w)).
		sort(w => w.w).
		map(w => [dv.fileLink(w.f), w.w]))
		
		
```

# Location Prefixes

```dataviewjs
const {util} = customJS

dv.table(["File", "Location"], 
		dv.pages().where(b=>b.whereabouts).
		flatMap(page => dv.array(page.whereabouts).map(w => {return {f: page.file.name, w: w.prefix  }})).
		where(f => f.w).
		map(x => [dv.fileLink(x.f), x.w]))
```


```dataviewjs
const {util} = customJS

dv.table(["File", "Location"], 
		dv.pages().where(b=>dv.isArray(b.whereabouts)).
		flatMap(page => dv.array(page.whereabouts).map(w => {return {f: page.file.name, w: w.formatSpecifier ?? w.format,  }})).
		where(f => f.w ).
		map(x => [dv.fileLink(x.f), x.w]))
```