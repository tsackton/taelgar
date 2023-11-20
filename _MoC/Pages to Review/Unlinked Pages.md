# Unlinked Pages

These are notes that are not linked from any other note.

```dataview
TABLE split(file.path,"/",1)[0] as Folder 
FROM -"_DM_" and -"_MoC" and -"_templates" and -"_templates" and -"_Testing" and -"Worldbuilding"
WHERE length(file.inlinks)=0 SORT split(file.path,"/",1)[0]
```

These are worldbuliding notes that ARE linked

```dataview
TABLE length(file.inlinks) as Backlinks
FROM "Worldbuilding"
WHERE length(file.inlinks)>0 SORT length(file.inlinks)
```
