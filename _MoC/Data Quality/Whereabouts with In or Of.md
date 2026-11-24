# Unlinked Whereabouts

```dataviewjs
const api = globalThis.Taelgarverse;
if (api?.apiVersion !== 1) {
    dv.paragraph("This query requires a Taelgarverse build with the note query API.");
    return;
}
const queries = await api.getNoteQueries();

dv.table(["File", "Location"], 
		dv.pages().where(b=>b.whereabouts).
		flatMap(page => dv.array(page.whereabouts).map(w => ({f: page.file.path, w: dv.isArray(page.whereabouts) ? w?.location : w}))).
		where(({f, w}) => {
			const target = typeof w === "string" ? w : w?.path;
			return target && !queries.isResolvable(target, f);
		}).
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
