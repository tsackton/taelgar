The `Staging` directory in `Worldbuilding` is used as a place to put notes that describe something that canonically exists, but is not ready to be incorporated into the main directory structure for whatever reason. 

Places that are not backlinked from any canonical page should go in `Brainstorming` or `Tentative`, not `Staging`, or be linked from a canonical page, at least in a comment.

This note organizes pages in the staging directory that are linked from specific vault locations to facilitate review and cleanup. 

## Dunmari Frontier Staging 

```dataview
TABLE
  length(file.inlinks) AS "All Backlinks",
  length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Dunmari Frontier Campaign"))) AS "Campaign Backlinks",
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE
  length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Dunmari Frontier Campaign"))) > 0
  AND length(filter(file.inlinks, (b) =>
    contains(meta(b).path, "Campaigns/")
    AND !contains(meta(b).path, "Campaigns/Dunmari Frontier Campaign")
  )) = 0
SORT length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Dunmari Frontier Campaign"))) DESC
```


---

## Great Library Staging

```dataview
TABLE
  length(file.inlinks) AS "All Backlinks",
  length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Great Library Campaign"))) AS "Campaign Backlinks",
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE
  length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Great Library Campaign"))) > 0
  AND length(filter(file.inlinks, (b) =>
    contains(meta(b).path, "Campaigns/")
    AND !contains(meta(b).path, "Campaigns/Great Library Campaign")
  )) = 0
SORT length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Great Library Campaign"))) DESC
```


---


## Cleenseau Staging

```dataview
TABLE
  length(file.inlinks) AS "All Backlinks",
  length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Cleenseau Campaign"))) AS "Campaign Backlinks",
  contains(file.tags, "status/check/ai") AS "AI Text"
FROM "Worldbuilding/Staging"
WHERE
  length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Cleenseau Campaign"))) > 0
  AND length(filter(file.inlinks, (b) =>
    contains(meta(b).path, "Campaigns/")
    AND !contains(meta(b).path, "Campaigns/Cleenseau Campaign")
  )) = 0
SORT length(filter(file.inlinks, (b) => contains(meta(b).path, "Campaigns/Cleenseau Campaign"))) DESC

```

---

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

## Multiple Campaigns

```dataviewjs
const campaignRoots = [
  "Campaigns/Addermarch Campaign",
  "Campaigns/Cleenseau Campaign",
  "Campaigns/Dunmari Frontier Campaign",
  "Campaigns/Great Library Campaign",
  "Campaigns/Great War Campaign",
  "Campaigns/Mawar Adventures",
  "Campaigns/One Shots"
];

const rows = dv.pages('"Worldbuilding/Staging"')
  .map(p => {
    const linkedCampaigns = campaignRoots.filter(root =>
      p.file.inlinks.some(link => dv.page(link.path)?.file.path.startsWith(root + "/") || dv.page(link.path)?.file.path === root)
    );

    return {
      page: p.file.link,
      backlinks: p.file.inlinks.length,
      campaigns: linkedCampaigns,
      ai: p.file.tags?.includes("#status/check/ai") ?? false
    };
  })
  .where(row => row.campaigns.length > 1)
  .sort(row => row.campaigns.length, "desc");

dv.table(
  ["Note", "Backlinks", "Campaigns", "AI Text"],
  rows.map(row => [
    row.page,
    row.backlinks,
    row.campaigns.map(c => c.replace("Campaigns/", "")).join(", "),
    row.ai
  ])
);
```


---

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

Currently: Gazetteer

```dataview
TABLE 
    length(file.inlinks) as Backlinks, 
  contains(file.tags, "status/check/ai") AS "AI Text",
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Gazetteer")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM "Worldbuilding/Staging"
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "People")))
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


