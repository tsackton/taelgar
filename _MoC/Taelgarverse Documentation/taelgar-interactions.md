# `taelgar-interactions`

In Obsidian, this block places a Campaign interactions panel at a chosen point in a note. It uses the note’s resolved `knownTo`, including the authored list such as `knownTo: [dufr, clee]` and any applicable directory inheritance.

Leave the block body empty.

````markdown
```taelgar-interactions
```
````

The panel draws on reviewed recap Cast entries. For sessions without a recap, it uses explicit links in the session note. When **Automatic campaign interactions** is enabled in Obsidian, eligible notes get a footer by default. An explicit block takes the footer’s place and still works with that setting disabled. The website places its campaign interactions panel after the article.

See [[_MoC/Campaign Registry|Campaign Registry]] for campaign IDs and [[Taelgarverse Code#KnownTo and Campaign Interactions|KnownTo and Campaign Interactions]] for the vault convention.
