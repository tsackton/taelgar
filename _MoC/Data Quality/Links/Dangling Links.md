# Files with Unresolved Links

This live view lists every indexed file containing one or more unresolved links, sorted by the number of unresolved link occurrences. The generated [[Unresolved Links]] report is omitted because its clickable missing targets are intentional.

```dataviewjs
const excludedSources = new Set([
    "_MoC/Data Quality/Links/Unresolved Links.md",
]);
const ignoredPatterns = typeof dv.app.vault.getConfig === "function"
    ? (dv.app.vault.getConfig("userIgnoreFilters") ?? [])
    : [];

const isIgnoredByObsidian = source => ignoredPatterns.some(pattern => {
    try {
        return new RegExp(pattern).test(source);
    } catch {
        return source.includes(pattern);
    }
});

const rows = Object.entries(dv.app.metadataCache.unresolvedLinks)
    .filter(([source, targets]) =>
        !excludedSources.has(source)
        && !isIgnoredByObsidian(source)
        && Object.keys(targets).length > 0
    )
    .map(([source, targets]) => {
        const unresolvedLinks = Object.values(targets)
            .reduce((total, occurrences) => total + occurrences, 0);
        const missingLinks = unresolvedLinks < 6
            ? Object.keys(targets)
                .sort((a, b) => dv.compare(a, b))
                .map(target => dv.fileLink(target))
            : "";

        return {
            source,
            file: dv.fileLink(source),
            unresolvedLinks,
            missingLinks,
        };
    })
    .sort((a, b) =>
        b.unresolvedLinks - a.unresolvedLinks || dv.compare(a.source, b.source)
    );

dv.table(
    ["File", "Unresolved links", "Missing link(s), if fewer than 6"],
    rows.map(row => [row.file, row.unresolvedLinks, row.missingLinks])
);
```
