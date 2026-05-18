# Pages That Need Finishing

These are pages tagged as stubs. 

## Dunmar

```dataview
TABLE 
    length(file.inlinks) as Backlinks,
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Dunmari Frontier Campaign")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM #status/stub
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Dunmari Frontier Campaign")))
SORT length(file.inlinks) DESC
```

## Addermarch

```dataview
TABLE 
    length(file.inlinks) as Backlinks,
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Addermarch Campaign")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM #status/stub
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Addermarch Campaign")))
SORT length(file.inlinks) DESC
```


## Mawar

```dataview
TABLE 
    length(file.inlinks) as Backlinks,
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Mawar Adventures")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM #status/stub
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Mawar Adventures")))
SORT length(file.inlinks) DESC
```



## Great Library

```dataview
TABLE 
    length(file.inlinks) as Backlinks,
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Great Library Campaign")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM #status/stub
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Great Library Campaign")))
SORT length(file.inlinks) DESC
```

## One Shots

```dataview
TABLE 
    length(file.inlinks) as Backlinks,
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "One Shots")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM #status/stub
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "One Shots")))
SORT length(file.inlinks) DESC
```



## Cleenseau

```dataview
TABLE 
    length(file.inlinks) as Backlinks,
  (
    length(
      filter(
        file.inlinks,
        (b) => contains(b.file.path, "Cleenseau Campaign")
      )
    )
    = length(file.inlinks)
  ) AS Unique
FROM #status/stub
WHERE any(filter(file.inlinks, (b) => contains(meta(b).path, "Cleenseau Campaign")))
SORT length(file.inlinks) DESC
```


