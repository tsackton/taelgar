# Place Categories

canonical::  "neighborhood", "realm", "settlement", "region", "watershed",  "extraplanar domain", "planar link", "plane", "forest", "wetlands", "desert", "grassland", "waterway", "lake", "marine feature", "topographical feature", "subterranean feature", "island", "inn", "building", "holy site", "road", "infrastructure"

communities:: "neighborhood", "realm", "settlement"
regions:: "region", "watershed"
extraplanar:: "extraplanar domain", "planar link", "plane"
biomes:: "forest", "wetlands", "desert", "grassland"
waterfeatures:: "waterway", "lake", "marine feature"
landforms:: "topographical feature", "subterranean feature", "island"
structures:: "inn", "building", "holy site"
infrastructure:: "road", "infrastructure"

## Missing Type Of

```dataview
LIST from #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND !typeOf
```

## Wrong Type Of

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND !contains(this.canonical, typeOf)
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

for (const person of dv.pages("#place")) {
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

for (const person of dv.pages("#place")) {
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

dv.table(["Ancestry", "Num Places"], rows);

```


## Communities

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.communities, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.communities, typeOf) and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.communities, typeOf) AND subTypeOf
SORT typeOf
```


## Geographic Regions

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.regions, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.regions, typeOf) and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.regions, typeOf) and subTypeOf
SORT typeOf
```

## Extraplanar 

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.extraplanar, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.extraplanar, typeOf) and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.extraplanar, typeOf) and subTypeOf
SORT typeOf
```


## Biomes 

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.biomes, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.biomes, typeOf) and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.biomes, typeOf) and subTypeOf
SORT typeOf
```


## Water Features 

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.waterfeatures, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.waterfeatures, typeOf) and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.waterfeatures, typeOf) and subTypeOf
SORT typeOf
```

## Landforms  

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.landforms, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.landforms, typeOf) and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.landforms, typeOf) and subTypeOf
SORT typeOf
```


## Structures  

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.structures, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.structures, typeOf)and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.structures, typeOf) and subTypeOf
SORT typeOf
```


## Infrastructure  

### Counts

```dataview
TABLE WITHOUT ID
  split(Combo, "\\|")[0] AS "Place Type",
  split(Combo, "\\|")[1] AS "Alias",
  length(rows) as "Count"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.infrastructure, typeOf)
GROUP BY (typeOf + "|" + typeOfAlias) as Combo
SORT split(Combo, "\\|")[0], length(rows) DESC
```
### No Alias

```dataview
TABLE
typeOf as "Place Type"
FROM #place and !"Worldbuilding"
WHERE !startswith(file.folder, "_") AND contains(this.infrastructure, typeOf) and !typeOfAlias
SORT typeOf
```

### Uses subTypeOf

```dataview
TABLE
typeOf as "Place Type",
subTypeOf as "Subtype"
FROM #place and !"Worldbuilding" 
WHERE !startswith(file.folder, "_") AND contains(this.infrastructure, typeOf) and subTypeOf
SORT typeOf
```
