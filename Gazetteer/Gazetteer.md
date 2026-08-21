---
headerVersion: 2023.11.25
lintedAt: "2026-08-21T13:33:35-04:00"
lintVersion: "3.4"
tags: [meta, status/check/lint]
name: Gazetteer
excludePublish: [all]
dm_owner: none
dm_notes: none
POV: modern
---
# Gazetteer

This directory contains **character-facing**, **meta**, and **in-world** pages about the places on Taelgar.

## Region Organization and Notes
Using this as a place for tracking general organization across regions. Regions are generally 

%%^Campaign:none%%
## Regions of Taelgar
```dataviewjs
const { util } = customJS
dv.table(["Place"], 
			dv.pages("#place")
				.where(f => util.currentLocation(f.file.frontmatter, dv.current().pageTargetDate) == "Taelgar" && f.file.frontmatter.typeOf=="region")
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file)]))
```

%%^End%%


## Tagging

```dataview
TABLE WITHOUT ID
split(Combo, "\\|")[0] as "Region",
  split(Combo, "\\|")[1] AS "Descriptive Tag",
  length(rows) AS "Count"

FROM "Gazetteer" 
FLATTEN file.tags AS tag 
WHERE !startswith(tag, "#status")
GROUP BY (default(split(file.folder, "/")[1], "Root") + "|" + tag) AS Combo
SORT Combo ASC

```

## Needs Work

Gazetteer pages that are stubs or need work.

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/", "") AS Status
FROM "Gazetteer"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/") AND !startswith(tag, "#status/cleanup") AND !startswith(tag, "#status/check")
SORT replace(tag, "#status/", "") ASC, length(file.inlinks) DESC

```


## Check

Gazetteer pages that need checking. 

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/check/", "") AS Check
FROM "Gazetteer"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/check")
SORT replace(tag, "#status/check/", "") ASC, length(file.inlinks) DESC

```

## Cleanup

Gazetteer pages that need cleanup.

```dataview
TABLE 
    length(file.inlinks) AS Backlinks, 
    replace(tag, "#status/cleanup/", "") AS Cleanup
FROM "Gazetteer"
FLATTEN file.etags AS tag
WHERE startswith(tag, "#status/cleanup")
SORT replace(tag, "#status/cleanup/", "") ASC, length(file.inlinks) DESC

```

## Publish Exclusions

```dataview
TABLE 
    length(file.inlinks) AS Backlinks,
    pubEx as "Publish Exclusions"
FROM "Gazetteer"
WHERE excludePublish
FLATTEN excludePublish as pubEx
SORT length(file.inlinks) DESC

```

## Unnamed In-Links

Pages that link to a cosmology page and are currently unnamed. 
```dataview
TABLE 
    length(file.inlinks) AS Backlinks
FROM ""
WHERE 
    startswith(file.name, "~") AND
    any(filter(file.inlinks, (b) => contains(meta(b).path, "Gazetteer")))
SORT length(file.inlinks) DESC

```

## Staging

These are staging pages linked to pages in the Gazetteer directory. 

```dataview
TABLE 
    length(file.inlinks) as Backlinks
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Gazetteer")))
SORT length(file.inlinks) DESC
```

%%^povNotes:v1%%
Temporal coverage: broadly modern as a vault-maintenance index; its query results change with the current contents of the Gazetteer.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the explicit meta-page name, normalized the private-block sentinel to `Campaign:none`, and added persistent temporal metadata for the live vault index.

### Validated judgments
- The `Campaign:none` block is an operational Dataview index rather than narrative DM material.
- The local-only `_DM_` candidates were generic matches to the word Gazetteer and do not justify changing `dm_notes: none`.

### Open findings
- [ ] **Suggestion — editorial.prose_clarity:** The passage `Using this as a place for tracking general organization across regions. Regions are generally` ends with an incomplete sentence and obscures the section's purpose. Copy-ready replacement: `This section tracks general organization across regions.`
%%^End%%
