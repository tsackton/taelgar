# Unlinked Pages

These are notes that are not linked from any other note.

## Gazetteer
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "Gazetteer" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## Cosmology
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "Cosmology" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## Events
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "Events" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## History
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "History" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## People
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "People" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## Species
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "Species" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## Things
```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "Things" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## Campaigns

```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "Campaigns" 
WHERE length(file.inlinks)=0 
SORT length(file.inlinks) DESC
```

## Assets

```dataview
TABLE file.inlinks as Backlinks, length(file.inlinks) as Total 
FROM "assets" 
WHERE length(file.inlinks)=0
SORT length(file.inlinks) DESC
```
