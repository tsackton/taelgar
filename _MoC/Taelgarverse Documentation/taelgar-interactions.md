# `taelgar-interactions`

This block places a Campaign interactions panel at a chosen point in a note. It reads the registered campaign IDs in the note’s `knownTo` frontmatter, such as `knownTo: [dufr, clee]`.

Leave the block body empty.

````markdown
```taelgar-interactions
```
````

The panel draws on reviewed recap Cast entries. For sessions without a recap, it uses explicit links in the session note. When **Automatic campaign interactions** is enabled in Obsidian, eligible notes get a footer by default. An explicit block takes the footer’s place and still works with that setting disabled.

See [[_MoC/Campaign Registry|Campaign Registry]] for campaign IDs and [[Taelgarverse Code#KnownTo and Campaign Interactions|KnownTo and Campaign Interactions]] for the vault convention.
