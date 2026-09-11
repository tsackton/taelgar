# Dunmari Frontier Sessions

```dataviewjs
const sessions = dv.pages('"Campaigns/Dunmari Frontier Campaign/Session Notes"')
    .where(p => typeof p.arc === "string" && p.arc.trim())
    .sort(p => p.sessionNumber, "asc");

const arcs = sessions.groupBy(
    p => p.arc.trim(),
    (a, b) => a.localeCompare(b, undefined, { numeric: true })
);

for (const arc of arcs) {
    dv.header(2, arc.key);
    dv.list(arc.rows.map(p => dv.fileLink(
        p.file.path,
        false,
        `Session ${p.sessionNumber}: ${p.descTitle || p.file.name}`
    )));
}
```
