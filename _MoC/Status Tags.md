---
tags: [meta]
---

Updated: March 15th, 2024

Status tags broadly are used to communicate between us (or between ourselves and our future selves) about the state of a page. Having a shared vocabulary of status tags helps ensure we understand what we are using as canonical in our games, and what is still a work in progress, as well as the state of a work in progress note.

The following status tags have a shared meaning:

**Canonical Tracking Tags**
The following tags are used to track the canonical status of the contents of a note. If the note has none of the below tags (and also doesn't have status/unknown) it is reasonable to consider it canonical in game.

- **status/needswork**: this note does not contain all of the information about this topic and shouldn't be treated as "complete." There are a variety of optional secondary tags. 
	- The primarily ones currently in use are:
		- **external**: additional details exist and are recorded in non-Obsidian notes or Google Docs, but haven't yet been captured in Obsidian. 
		- **internal**: additional details exist in Obsidian, e.g. in the form of dates on other notes, comments in the note itself, etc, but haven't been fully incorporated into the note text. This should be used to refer to shared notes only, not DM folder notes, which should be considered external.
		- **wip**: note author has ideas for this but they are not fully formed and haven't been recorded. The author is ideally recorded via status/mike or status/tim.
		- **blankslate**: a blank page that has no canonical details yet, but clearly could use them. Unless there is a status/active tag, this should be considered an open invitation to invent something.
	- Other secondary tags are possible and in general the "main" author of the note should be the only one to change needswork tags, although that isn't a hard and fast rule
- **status/factcheck**: this note has a comment about consistency accuracy and needs someone to do a check. Usually this means, check with session notes or a timeline elsewhere. Use this only when the facts are verifiable from Obsidian source material (usually session notes). Anyone can remove a factcheck status by checking the facts and updating the note.
- **status/active**: this note represents a page that is active in a campaign. Use this to flag places where additional invention, without consultation, might impinge on a campaign. This can be thought of as a "permanent" status/update
- **status/namecheck**: this note introduces a new "world level" name and should be confirmed. The inventor of the name should be the one to remove namecheck. If the name needs to be confirmed with someone else, see status/mike + status/tim
- **status/mike**, **status/tim**: Either Mike or Tim or both should review the note contents and remove their own status/name when they are happy with the note contents. Use when the author of the note wants the other person to confirm before switching away from a needswork status or similar. Only remove status/yourownname. Perfectly reasonable to create a note with status/yourownname to remind yourself to review in the future. Typically the last status tag on a note.
- **status/unknown** for the status of the note is unclear
- **status/update** for notes where game events have changed things, but these are not captured in the note body yet.
- **status/complex** for pages that have wide implications or are large projects that are not really started, or where the implications of changes are far reaching

**Work Tracking Notes**
In addition to tracking the canonical status of the information in a note, status tags can be used to track needed work. 

- **status/cleanup**: this note is reasonably complete and information can be trusted as canonical, but is missing some header information, often whereabouts or campaign info, or this note requires reorganization in some way. Optional secondary tags include:
	- **refactor**: this note has something about it that is not well captured by current Obsidian note organization and header tags; examples might include undead with both pre-death and post-death details (requiring tracking whereabouts after death, for example) or NPCs a person or party is aware of but hasn't met (where it is not obvious how to handle campaign info). 
	- **reformat**: the information in this note is not optimally structured and might benefit from refactoring note structure (examples could be narrative history notes that should be refactored into timelines; or item notes that mix general and specific lore). 
	- **header**: this note is missing header details, usually whereabouts and/or campaign information, and this information needs to be extracted from session notes, timelines or other notes
	- **language**: the information in the note is fine, but the language could be improved, i.e. either because it is repeatively or clunky, or more likely, because it is currently quite focused on a specific campaign
- **status/stub**: basically empty pages where nothing is known. Once basic header information is filled in can be removed. When creating an empty page set status/needswork instead of status/stub if the page needs more than full header. Anyone can remove this tag by filling in the header details usually without a status/mike or status/tim, unless significant color details are invented or something
- **status/image**: for pages that might benefit from additional of some images or descriptive text
- **status/map**: for pages that might benefit from a map

