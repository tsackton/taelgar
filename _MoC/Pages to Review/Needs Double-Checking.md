# Pages that might have inaccurate data

### Needs Name Confirmation
```dataview
list from #status/check/name 
sort file.name
```

### Needs Facts Checked
```dataview
list from #status/check/minor 
```

### Other Checking Needed
```dataview
list from #status/check and !#status/check/tim and !#status/check/name and !#status/check/mike and !#status/check/minor
```

### Check: Mike
```dataview
list from #status/check/mike and !#status/check/tim
```

### Check: Tim
```dataview
list from #status/check/tim and !#status/check/mike
```

### Check: Mike & Tim
```dataview
list from #status/check/tim and #status/check/mike
```

