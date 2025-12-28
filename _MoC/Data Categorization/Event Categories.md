
# Event Categories

## Events with Missing TypeOf
*TypeOf is blank*

```dataview
LIST
FROM #event and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND !typeOf
```

## Event TypeOfs

```dataview
TABLE WITHOUT ID
  typeOf as "Event Type",
  length(rows) as "Count"
FROM #event and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY typeOf
SORT length(rows) DESC
```

## Notes with Specific TypeOf

typeFilter:: collapse

```dataview
LIST
FROM #event and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND typeOf = this.typeFilter
```


## Uses other categorization

*subTypeOf, typeOfAlias, ancestry*

```dataview
TABLE
subTypeOf as subtype,
typeOfAlias as alias,
ancestry as ancestry
FROM #event AND !#status/stub AND !"_templates"
WHERE subTypeOf or typeOfAlias or ancestry
```

## Part Of Usages

```dataview
TABLE
partOf as "Part Of",
typeOf as "Type Of"
FROM #event AND !#status/stub AND !"_templates"
WHERE partOf
SORT partOf
```

```dataviewjs
const norm = (x) =>
  (x ?? "")
    .toString()
    .replace(/^\[\[|\]\]$/g, "")
    .trim()
    .toLowerCase();

const asArray = (v) => (v == null ? [] : Array.isArray(v) ? v : [v]);

// Lookup: "name or alias" -> page
const lookup = new Map();
for (const p of dv.pages()) {
  lookup.set(norm(p.file.name), p);
  for (const a of (p.file.aliases ?? [])) lookup.set(norm(a), p);
}

// speciesKey -> { display, linkPaths:Set }
const noteMap = new Map();

// change these two links to point to source and field 
for (const note of dv.pages("#event")) {
  for (const raw of asArray(note.partOf)) {
    if (!raw) continue;
    if (raw == "unknown") continue; 

    const display =
      raw?.path
        ? (raw.display ?? raw.path.split("/").pop().replace(/\.md$/, ""))
        : raw.toString();

    const key = norm(display);
    if (!key) continue;

    if (!noteMap.has(key)) noteMap.set(key, { display, linkPaths: new Set() });
    noteMap.get(key).linkPaths.add(note.file.path);
  }
}

const rows = [...noteMap.entries()]
  .sort((a, b) => a[1].display.localeCompare(b[1].display, undefined, { sensitivity: "base" }))
  .map(([key, info]) => {
    const page = lookup.get(key);
    return [
      info.display,
      info.linkPaths.size,
      page ? "✅" : "—",
      page ? page.file.link : ""
    ];
  });

dv.table(["Part Of", "Count", "Has Note?", "Link"], rows);

```

## Ancestry Counts

```dataviewjs
const norm = (x) =>
  (x ?? "")
    .toString()
    .replace(/^\[\[|\]\]$/g, "")
    .trim()
    .toLowerCase();

const asArray = (v) => (v == null ? [] : Array.isArray(v) ? v : [v]);

// Lookup: "name or alias" -> page
const lookup = new Map();
for (const p of dv.pages()) {
  lookup.set(norm(p.file.name), p);
  for (const a of (p.file.aliases ?? [])) lookup.set(norm(a), p);
}

// speciesKey -> { display, peoplePaths:Set }
const speciesMap = new Map();

for (const person of dv.pages("#event")) {
  for (const raw of asArray(person.ancestry)) {
    if (!raw) continue;
    if (raw == "unknown") continue; 

    const display =
      raw?.path
        ? (raw.display ?? raw.path.split("/").pop().replace(/\.md$/, ""))
        : raw.toString();

    const key = norm(display);
    if (!key) continue;

    if (!speciesMap.has(key)) speciesMap.set(key, { display, peoplePaths: new Set() });
    speciesMap.get(key).peoplePaths.add(person.file.path);
  }
}

const rows = [...speciesMap.entries()]
  .sort((a, b) => a[1].display.localeCompare(b[1].display, undefined, { sensitivity: "base" }))
  .map(([key, info]) => {
    const page = lookup.get(key);
    return [
      info.display,
      info.peoplePaths.size,
      page ? "✅" : "—",
      page ? page.file.link : ""
    ];
  });

dv.table(["Ancestry", "Count", "Has Note?", "Link"], rows);

```

## "Bad" Ancestries

```dataviewjs
const norm = (x) =>
  (x ?? "")
    .toString()
    .replace(/^\[\[|\]\]$/g, "")
    .trim()
    .toLowerCase();

const asArray = (v) => (v == null ? [] : Array.isArray(v) ? v : [v]);

// Build lookup: any page filename or alias -> page
const lookup = new Map();
for (const p of dv.pages()) {
  lookup.set(norm(p.file.name), p);
  for (const a of (p.file.aliases ?? [])) lookup.set(norm(a), p);
}

// Map missingSpeciesKey -> { display, people: Map(path -> link) }
const missing = new Map();

for (const person of dv.pages("#event")) {
  for (const raw of asArray(person.ancestry)) {
    if (!raw) continue;
	if (raw == "unknown") continue;

    // Normalize display for links or plain text
    const display =
      raw?.path
        ? (raw.display ?? raw.path.split("/").pop().replace(/\.md$/, ""))
        : raw.toString();

    const key = norm(display);
    if (!key) continue;

    // If species resolves to an existing note/alias, skip
    if (lookup.has(key)) continue;

    // Otherwise record it + which person notes use it
    if (!missing.has(key)) {
      missing.set(key, { display, people: new Map() });
    }
    missing.get(key).people.set(person.file.path, person.file.link);
  }
}

// Rows: Missing species | Count | People notes
const rows = [...missing.values()]
  .sort((a, b) => a.display.localeCompare(b.display, undefined, { sensitivity: "base" }))
  .map(({ display, people }) => [
    display,
    people.size,
    [...people.values()]
  ]);

dv.table(["Ancestry", "Num Events"], rows);

```
