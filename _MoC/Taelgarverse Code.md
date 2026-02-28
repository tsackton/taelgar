---
headerVersion: 2023.11.25
tags: [status/check/ai]
---
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
This folder contains dataview functions that can be used with dv.view("/path/to/function", arguments). The intention is that any code in here is needed for export and will be translated into Python for website generation. 

#### **templater**
This folder contains templater user functions. 

## KnownTo and Campaign Interactions

To track and summarize party interactions with NPCs (and other entities) without cluttering YAML with long logs:

- Use `knownTo` in frontmatter as the **source of truth** for “this party knows this subject”.
  - Example: `knownTo: [DuFr, Clee]`
- Rely on session notes as **evidence**: session notes should link entities that appear in them.
- Add a generated “Campaign Interactions” section to the subject page to avoid manually searching backlinks.

Example section on an NPC page:

```markdown
## Campaign Interactions
`$=customJS.OutputHandler.outputCampaignInteractions(dv.current().file.name, dv.current())`
```

To show interactions for a single campaign only:

```markdown
## Campaign Interactions (DuFr)
`$=customJS.OutputHandler.outputCampaignInteractions(dv.current().file.name, dv.current(), "DuFr")`
```

Campaign codes (and mapping to party pages and session-note folders) are configured in `.obsidian/metadata.json` under `campaigns` (`code`, `partyPage`, `sessionNoteFolder`, optional `aliases`).
