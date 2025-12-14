# Pages That Need Finishing

These are pages tagged as stubs. 

## High Priority

These are stubs that have 10 or more backlinks and should be cleaned as quickly as possible.

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub  and !#status/check/ai
where length(file.inlinks) > 9
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Background

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Background"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```


## Cosmology

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Cosmology"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```


## Creatures

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Creatures" and !#status/check/ai
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Events

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Events" and !#status/check/ai
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```


## Gazetteer

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Gazetteer" and !#status/check/ai
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```


## Gods and Religions

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Gods and Religions"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```


## Groups

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Groups" and !#status/check/ai
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
sort join(split(file.path, "/", 2),"/"), length(file.inlinks) DESC
```

## Primary Sources

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Primary Sources"
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```

## Things

```dataview
TABLE join(split(file.path, "/", 2),"/") as Folder, length(file.inlinks) as Backlinks
from #status/stub and "Things" and !#status/check/ai
sort length(file.inlinks) DESC, join(split(file.path, "/", 2),"/")
```
