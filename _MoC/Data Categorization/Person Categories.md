# Species

## Missing Species

```dataview
LIST
FROM #person AND !#status/stub AND !"_templates"
WHERE !species
```

## Unknown Species


```dataview
LIST
FROM #person AND !#status/stub AND !"_templates"
WHERE species = "unknown"
```

## Species Counts

```dataview
TABLE WITHOUT ID
  species AS Species,
  length(rows) AS "Count"
FROM #person AND !#status/stub AND !"_templates"
WHERE species != "unknown"
GROUP BY species
```

## Species Pages

```dataviewjs
// 1) Collect all species values from #person notes
// 2) For each species, check whether a note exists whose filename OR alias matches it
// 3) Output a table: species name | has note? | link to note

const norm = (x) =>
  (x ?? "")
    .toString()
    .replace(/^\[\[|\]\]$/g, "") // strip [[...]] if someone stored species that way
    .trim()
    .toLowerCase();

const asArray = (v) => (v == null ? [] : Array.isArray(v) ? v : [v]);

// Build a lookup map: "name or alias" -> page
const lookup = new Map();
for (const p of dv.pages()) {
  lookup.set(norm(p.file.name), p);
  for (const a of (p.file.aliases ?? [])) lookup.set(norm(a), p);
}

// Pull unique species from #person notes
const speciesDisplayByKey = new Map();

for (const person of dv.pages("#person")) {
  for (const raw of asArray(person.species)) {
    if (!raw) continue;
    if (raw == "unknown") continue;

    // If species is already a link (e.g., [[Elf]]), Dataview often gives an object with .path
    const display =
      (raw?.path ? raw.display ?? raw.path.split("/").pop().replace(/\.md$/, "") : raw.toString());

    const key = norm(display);
    if (!key) continue;

    // keep first-seen casing as display value
    if (!speciesDisplayByKey.has(key)) speciesDisplayByKey.set(key, display);
  }
}

// Create rows
const rows = [...speciesDisplayByKey.entries()]
  .sort((a, b) => a[1].localeCompare(b[1], undefined, { sensitivity: "base" }))
  .map(([key, display]) => {
    const page = lookup.get(key);
    return [
      display,
      page ? "✅" : "—",
      page ? page.file.link : ""
    ];
  });

dv.table(["Species", "Has Note?", "Note"], rows);

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

```dataview
TABLE WITHOUT ID
  ancestry AS Ancestry,
  length(rows) AS "Count"
FROM #person AND !#status/stub AND !"_templates"
WHERE ancestry != "unknown"
GROUP BY ancestry
```

## Ancestry Pages

```dataviewjs
// 1) Collect all species values from #person notes
// 2) For each species, check whether a note exists whose filename OR alias matches it
// 3) Output a table: species name | has note? | link to note

const norm = (x) =>
  (x ?? "")
    .toString()
    .replace(/^\[\[|\]\]$/g, "") // strip [[...]] if someone stored species that way
    .trim()
    .toLowerCase();

const asArray = (v) => (v == null ? [] : Array.isArray(v) ? v : [v]);

// Build a lookup map: "name or alias" -> page
const lookup = new Map();
for (const p of dv.pages()) {
  lookup.set(norm(p.file.name), p);
  for (const a of (p.file.aliases ?? [])) lookup.set(norm(a), p);
}

// Pull unique species from #person notes
const speciesDisplayByKey = new Map();

for (const person of dv.pages("#person")) {
  for (const raw of asArray(person.ancestry)) {
    if (!raw) continue;
    if (raw == "unknown") continue;

    // If species is already a link (e.g., [[Elf]]), Dataview often gives an object with .path
    const display =
      (raw?.path ? raw.display ?? raw.path.split("/").pop().replace(/\.md$/, "") : raw.toString());

    const key = norm(display);
    if (!key) continue;

    // keep first-seen casing as display value
    if (!speciesDisplayByKey.has(key)) speciesDisplayByKey.set(key, display);
  }
}

// Create rows
const rows = [...speciesDisplayByKey.entries()]
  .sort((a, b) => a[1].localeCompare(b[1], undefined, { sensitivity: "base" }))
  .map(([key, display]) => {
    const page = lookup.get(key);
    return [
      display,
      page ? "✅" : "—",
      page ? page.file.link : ""
    ];
  });

dv.table(["Ancestry", "Has Note?", "Link"], rows);

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

dv.table(["Species", "Num People"], rows);

```
