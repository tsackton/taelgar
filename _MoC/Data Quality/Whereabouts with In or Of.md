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

```dataview
TABLE WITHOUT ID link(file.name) AS "File", loc AS "Location"
WHERE whereabouts
FLATTEN whereabouts AS w
FLATTEN w.prefix AS loc
WHERE loc
```


```dataview
TABLE WITHOUT ID link(file.name) AS "File", loc AS "Location"
WHERE typeof(whereabouts) = "array"
FLATTEN whereabouts AS w
FLATTEN default(w.formatSpecifier, w.format) AS loc
WHERE loc
```