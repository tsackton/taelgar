# Missing TypeOf

### Places (Excluding Tentative)
```dataview
LIST from #place and !"Worldbuilding" where !typeOf 
```

### Groups
```dataview
LIST from #organization and !#status/stub where !typeOf
```

## People
```dataview
LIST from #person and !#status/stub and !"_templates" where !species 
```

## Things
```dataview
list from #object and !#status/stub where !typeOf
```
