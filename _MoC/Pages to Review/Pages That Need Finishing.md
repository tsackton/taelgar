# Pages That Need Finishing

These are pages that are not finished.

## High Priority

These are stubs that have 10 or more backlinks and should be cleaned as quickly as possible.

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub 
where length(file.inlinks) > 9
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Cosmology

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Cosmology"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```



## Events

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Events"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```


## Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Gazetteer"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Groups

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Groups"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## History

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "History"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## People

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "People"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Sources

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Primary Sources"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Species

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Species"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Things

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Things"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Time

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Time"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Worldbuilding

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Worldbuilding"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```


