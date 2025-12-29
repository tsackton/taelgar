
## Group with Missing TypeOf
*typeOf is blank*

```dataview
LIST
FROM #group and !"Worldbuilding"
WHERE !typeOf and !startswith(file.folder, "_")
```


## Group Type Ofs

```dataview
TABLE WITHOUT ID
  typeOf as "Type",
  length(rows) as "Count"
FROM #group and !"Worldbuilding" 
WHERE !startswith(file.folder, "_")
GROUP BY typeOf
SORT length(rows) DESC
```

## Group Sub-categories

```dataview
TABLE WITHOUT ID
  Combo[0] as "Type Of",
  Combo[1] as "Subtype",
  length(rows) as "Count"
FROM #group and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") and subTypeOf
GROUP BY list(typeOf, subTypeOf) as Combo
```


```dataview
TABLE WITHOUT ID
  Combo[0] as "Type Of",
  Combo[1] as Alias,
  length(rows) as "Count"
FROM #group and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") and typeOfAlias
GROUP BY list(typeOf, typeOfAlias) as Combo
```


## Ancestries

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
for (const note of dv.pages("#group")) {
  for (const raw of asArray(note.ancestry)) {
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

dv.table(["Ancestry", "Count", "Has Note?", "Link"], rows);

```

## Bad Ancestries

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

for (const note of dv.pages("#group")) {
  for (const raw of asArray(note.ancestry)) {
    if (!raw) continue;
	if (raw == "unknown") continue;

    // Normalize display for links or plain text
    const display =
      raw?.path
        ? (raw.display ?? raw.path.split("/").pop().replace(/\.md$/, ""))
        : raw.toString();

    const key = norm(display);
    if (!key) continue;

    // If resolves to an existing note/alias, skip
    if (lookup.has(key)) continue;

    // Otherwise record it + which person notes use it
    if (!missing.has(key)) {
      missing.set(key, { display, note: new Map() });
    }
    missing.get(key).note.set(note.file.path, note.file.link);
  }
}

// Rows: Missing species | Count | People notes
const rows = [...missing.values()]
  .sort((a, b) => a.display.localeCompare(b.display, undefined, { sensitivity: "base" }))
  .map(({ display, note }) => [
    display,
    note.size,
    [...note.values()]
  ]);

dv.table(["Ancestry", "Num Notes"], rows);

```
## Part Of Usage


```dataview
TABLE
partOf as "Part Of",
typeOf as "Type Of"
FROM #group AND !#status/stub AND !"_templates"
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
for (const note of dv.pages("#group")) {
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
