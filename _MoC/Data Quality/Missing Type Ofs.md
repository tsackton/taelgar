# Missing TypeOf

### Places (Excluding Tentative)
```dataview
TABLE partOf, placeType from #place and !#status/stub and !"Worldbuilding/Tentative" where !typeOf 
```

### Groups
```dataview
LIST from #organization and !#status/stub where !typeOf
```

## People
```dataview
LIST from #person and !#status/stub where !species
```

## Things
```dataview
list from #item and !#status/stub where !typeOf
```