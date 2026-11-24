# Javascript Notes

Use the Taelgarverse note query API for campaign data, DR date normalization, and note display formatting in DataviewJS or Templater. In Taelgarverse 3.2.0, call `await globalThis.Taelgarverse.getNoteQueries()` to get the query helpers. See [[People Known To Review]] for an example.

Use [[taelgar-index]] for rosters and other generated tables.

#### **view**
This folder contains helpers for local Dataview queries. Use `dv.view("/path/to/function", arguments)` to call one in Obsidian. The website publisher processes a working copy of the vault through taelgarverse-core.

#### **templater**
This folder contains templater user functions. 

## KnownTo and Campaign Interactions

Use `knownTo` to record which parties know the subject, for example `knownTo: [dufr, clee]`. Taelgarverse can show a Campaign interactions panel automatically in Obsidian. It uses reviewed recap Cast entries and falls back to session-note links for sessions without a recap.

To place the panel within the note, add an empty native block.

````markdown
```taelgar-interactions
```
````

Campaign IDs are the keys of `_sessions/campaign-registry.json`. Index notes supply display names, party pages and session paths. See [[Campaign Registry]].
