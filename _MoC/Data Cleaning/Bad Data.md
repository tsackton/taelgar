## Null affiliations

```dataview
table where affiliations and contains(affiliations, null)
```

## Comma in whereabouts

```dataview
table where whereabouts and contains(whereabouts.location, ",")
```


### Whereabouts duplicated

```dataview
table where whereabouts and length(whereabouts) = 2 and whereabouts[0].location = whereabouts[1].location
```


## Old display info
```dataview
table where displayDefaults.whereaboutsHome or displayDefaults.definitiveArticle or displayDefaults.whereaboutsOrigin or displayDefaults.secondaryInfo or displayDefaults.whereaboutsCurrent or displayDefaults.whereaboutsLastKnown or displayDefaults.whereaboutsParty or displayDefaults.pageCurrent or displayDefaults.pagePast or displayDefaults.pagePastWithStart or displayDefaults.definitiveArticle = "" or displayDefaults.secondaryInfo = ""
```


### Unused display info
```dataview
table where displayDefaults.startPrefix or displayDefaults.endPrefix or displayDefaults.whereaboutsUnknown or displayDefaults.affiliationTypeOf
```

# Place with Part Of

```dataview
TABLE length(file.inlinks) as Backlinks
from #place where partOf 
SORT length(file.inlinks) DESC
```

# Contains all data files that have a valid type but not current header

```dataview
TABLE length(file.inlinks) as Backlinks
from #person or #item or #place or #organization and -#status/stub and !"Worldbuilding/Tentative" and !"Worldbuilding/Staging"
where headerVersion != "2023.11.25"
sort length(file.inlinks) desc
```
