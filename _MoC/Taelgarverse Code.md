# Javascript Notes
**WARNING: outdated and incomplete**

The `_scripts` directory has three kinds of Javascript code. 

#### **customJS**
This folder contains javascript code that can be imported into either a templater javascript block or a dataviewjs block by using:
```
const {FUNCTIONNAME} = customJS
```
FUNCTIONNAME is the name of a file containing a class with various methods. My understanding is the file needs to be named FUNCTIONNAME.js and the class should be the same as the filename. You'll need to set the customJS scripts folder to `_scripts/customJS`, of course. 

(to add...documentation of classes that exist and functions one might want to use for dataviewjs)

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
