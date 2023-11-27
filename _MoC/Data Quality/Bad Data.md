## Null affiliations

```dataview
list where affiliations and contains(affiliations, null)
```

## Comma in whereabouts

```dataview
list where whereabouts and contains(whereabouts.location, ",")
```


### Whereabouts duplicated

```dataview
list where whereabouts and length(whereabouts) = 2 and whereabouts[0].location = whereabouts[1].location
```
