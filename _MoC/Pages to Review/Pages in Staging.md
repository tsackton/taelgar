The `Staging` directory in `Worldbuilding` is used as a place to put notes that describe something that canonically exists, but is not ready to be incorporated into the main directory structure for whatever reason. 

Places that are not backlinked from any canonical page should go in `Brainstorming` or `Tentative`, not `Staging`, or be linked from a canonical page, at least in a comment.

This note organizes pages in the staging directory that are linked from specific vault locations to facilitate review and cleanup. 
## Dunmari Frontier Staging - Unique

```dataview
TABLE
  length(file.inlinks) AS Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE length(file.inlinks) > 0
AND length(
  filter(
    file.inlinks,
    (b) => contains(b.file.path, "Dunmari Frontier Campaign")
  )
) = length(file.inlinks)
SORT length(file.inlinks) DESC

```

## Dunmari Frontier Staging - Any

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text",
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Dunmari Frontier Campaign")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Dunmari Frontier Campaign")))
SORT length(file.inlinks) DESC
```


---


## Great Library Staging - Unique

```dataview
TABLE
  length(file.inlinks) AS Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE length(file.inlinks) > 0
AND length(
  filter(
    file.inlinks,
    (b) => contains(b.file.path, "Great Library Campaign")
  )
) = length(file.inlinks)
SORT length(file.inlinks) DESC

```

## Great Library Staging - Any

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text",
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Great Library Campaign")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Great Library Campaign")))
SORT length(file.inlinks) DESC
```



---


## Cleenseau Staging - Unique

```dataview
TABLE
  length(file.inlinks) AS Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE length(file.inlinks) > 0
AND length(
  filter(
    file.inlinks,
    (b) => contains(b.file.path, "Cleenseau Campaign")
  )
) = length(file.inlinks)
SORT length(file.inlinks) DESC

```

## Cleenseau Staging - Any

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text",
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Cleenseau Campaign")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Cleenseau Campaign")))
SORT length(file.inlinks) DESC
```


## Addermarch Staging

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Addermarch Campaign")))
SORT length(file.inlinks) DESC
```

## Mawar Staging

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Mawar Adventures")))
SORT length(file.inlinks) DESC
```

## One Shot Staging

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "One Shots")))
SORT length(file.inlinks) DESC
```

## Only Linked from DM Notes

```dataview
TABLE
  length(file.inlinks) AS Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE length(file.inlinks) > 0
AND length(
  filter(
    file.inlinks,
    (b) => contains(b.file.path, "_dm_notes")
  )
) = length(file.inlinks)
SORT length(file.inlinks) DESC

```


## Not Linked from Campaigns

```dataview
TABLE
  length(file.inlinks) AS Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE
  length(file.inlinks) > 0
  AND
  length(
    filter(
      file.inlinks,
      (b) => contains(b.file.path, "Campaigns/")
    )
  ) = 0
SORT length(file.inlinks) DESC


```


## Staging Linked to Specific Directory

Currently: Cosmology

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text",
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Cosmology")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Cosmology")))
SORT length(file.inlinks) DESC
```

## AI Text to Review

```dataview
TABLE
  length(file.inlinks) AS Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging" and #status/check/ai
SORT length(file.inlinks) DESC

```



## Not Linked 

```dataview
TABLE
  length(file.inlinks) AS Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE length(file.inlinks) = 0 
SORT length(file.inlinks) DESC

```
