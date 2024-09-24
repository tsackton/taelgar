# Pages that might have inaccurate data

Tag a page here with either status/namecheck (for a new 'world level' name where opinions are being sought) or status/factcheck for a page that needs facts confirmed.

### Needs Name Confirmation
```dataview
list from #status/check/name 
sort file.name
```

### Needs Facts Checked
```dataview
list from #status/check/minor 
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

