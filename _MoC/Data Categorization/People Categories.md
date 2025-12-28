# Species

## People with Missing Species
*Species is blank*

```dataview
LIST
FROM #person AND !#status/stub AND !"_templates"
WHERE !species
```

## People with Unknown Species
*Species is explicitly listed as unknown*

```dataview
LIST
FROM #person AND !#status/stub AND !"_templates"
WHERE species = "unknown"
```

## Species Count

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

for (const person of dv.pages("#person")) {
  for (const raw of asArray(person.species)) {
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

dv.table(["Species", "Count", "Has Note?", "Link"], rows);

```

## "Bad" Species

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

for (const person of dv.pages("#person")) {
  for (const raw of asArray(person.species)) {
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

dv.table(["Species", "Num People", "Notes"], rows);

```

# Ancestry

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

for (const person of dv.pages("#person")) {
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

for (const person of dv.pages("#person")) {
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

dv.table(["Ancestry", "Num People"], rows);

```


## People with Missing Ancestry

```dataview
TABLE WITHOUT ID
  species AS Species,
  length(rows) AS "Count"
FROM #person  AND !#status/stub AND !"_templates"
WHERE !ancestry and species != "unknown"
GROUP BY species 
```

# Other Classifications

## Uses subspecies

```dataview
TABLE 
species AS "Species",
subspecies AS "Subspecies",
ancestry AS "Ancestry"
from #person 
where subspecies
sort species, subspecies
```

## Uses speciesAlias

```dataview
TABLE 
species AS "Species",
speciesAlias AS "Alias"
from #person 
where speciesAlias
sort species, subspecies
```
