# Missing TypeOf

### Places
```dataview
TABLE partOf, placeType from #place where !typeOf 
```

### Groups
```dataview
LIST from #organization where !typeOf
```

## People
```dataview
LIST from #person where !species 
```

## Things
```dataview
list from #item where !typeOf
```