# Pages That Need Review

These are pages that need checking of some kind. Usually this is just a simple review. Pages that need extensive work should be tagged needswork, cleanup, or something else as appropriate. 

### Needs Name Confirmation
```dataview
list from #status/check/name 
sort file.name
```

### Needs Facts Checked
```dataview
list from #status/check/minor 
```

### Needs AI Cleanup
```dataview
list from #status/check/ai 
```

### Other Checking Needed (See Note for Details)
```dataview
list from #status/check and !#status/check/tim and !#status/check/name and !#status/check/mike and !#status/check/minor and !#status/check/ai
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

