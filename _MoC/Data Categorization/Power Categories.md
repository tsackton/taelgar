## Powers with Missing TypeOf
*TypeOf is blank*

```dataview
LIST
FROM #power AND !#status/stub AND !"_templates"
WHERE !typeOf
```

## Power TypeOfs

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

for (const person of dv.pages("#power")) {
  for (const raw of asArray(person.typeof)) {
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

dv.table(["Type Of Power", "Count", "Has Note?", "Link"], rows);

```
