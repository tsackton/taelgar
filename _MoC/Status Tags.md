---
tags: [meta]
---

Updated: January 9th, 2024

Status tags broadly are used to communicate between us (or between ourselves and our future selves) about the state of a page. Having a shared vocabulary of status tags helps ensure we understand what we are using as canonical in our games, and what is still a work in progress, as well as the state of a work in progress note.

The following status tags have a shared meaning:

**Canonical Tracking Tags**
The following tags are used to track the canonical status of the contents of a note. If the note has none of the below tags (and also doesn't have status/unknown) it is reasonable to consider it canonical in game.

- **status/needswork**: this note does not contain all of the information about this topic and shouldn't be treated as "complete." optional secondary tags include:
	- **notes**: additional details exist and are recorded in non-Obsidian notes or in someone's head, but haven't yet been captured in Obsidian
	- **wip**: additional details need to invented has someone has some thoughts on them. 
	- **blankslate**: this is clearly a note that needs invented details (contrast with stub, below) but the note author has no ideas. Valid target for anyone to make up
	- **internal**: additional details exist in Obsidian, e.g. in the form of dates on other notes, comments in the note itself, etc, but haven't been fully incorporated into the note text
	- **secret**: additional details are secret (a complete note with secrets will just have them in a %%Secret%% block or %%%% )
	- **collate**: details need to be checked with other pages. Used somewhat interchangably with internal. 
	- **draft**: the note is largely complete, but some tidy-up is still going on
	- Other secondary tags are possible and in general the "main" author of the note should be the only one to change needswork tags, although that isn't a hard and fast rule
- **status/factcheck**: this note has a comment about consistency accuracy and needs someone to do a check. Usually this means, check with session notes or a timeline elsewhere. Use this only when the facts are verifiable from Obsidian source material (usually session notes). Anyone can remove a factcheck status by checking the facts and updating the note.
- **status/namecheck**: this note introduces a new "world level" name and should be confirmed. The inventor of the name should be the one to remove namecheck. If the name needs to be confirmed with someone else, see status/mike + status/tim
- **status/mike**, **status/tim**: Either Mike or Tim or both should review the note contents and remove their own status/name when they are happy with the note contents. Use when the author of the note wants the other person to confirm before switching away from a needswork status or similar. Only remove status/yourownname. Perfectly reasonable to create a note with status/yourownname to remind yourself to review in the future. Typically the last status tag on a note.
- **status/unknown** for the status of the note is unclear

**Work Tracking Notes**
In addition to tracking the canonical status of the information in a note, status tags can be used to track needed work. 

- **status/refactor**: this note has something about it that is not well captured by current Obsidian note organization, and might benefit from refactoring note structure (examples could be narrative history notes that should be refactored into timelines; or item notes that mix general and specific lore). The information in the note is fine but it needs some kind of reorganization
- **status/stub** basically empty pages where nothing is known. Once basic header information is filled in can be removed. When creating an empty page set status/needswork instead of status/stub if the page needs more than full header. Anyone can remove this tag by filling in the header details usually without a status/mike or status/tim, unless significant color details are invented or something
- **status/images** for pages that might benefit from additional of some images or descriptive text

Old: **status/uptodate**, **status/docreview**, **status/draft**, and **status/notes** have no consistent meaning and should not be trusted. Any page with **status/unknown** and other **status** tags should not be trusted either. 