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
table where displayDefaults.whereaboutsHome or displayDefaults.definitiveArticle or displayDefaults.whereaboutsOrigin or displayDefaults.secondaryInfo or displayDefaults.whereaboutsCurrent or displayDefaults.whereaboutsLastKnown or displayDefaults.whereaboutsParty or displayDefaults.pageCurrent or displayDefaults.pagePast or displayDefaults.pagePastWithStart
```