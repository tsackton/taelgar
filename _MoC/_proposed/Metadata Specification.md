---
tags: [status/check/ai]
---
# Metadata Specification

This note summarizes the metadata specification for YAML frontmatter 

This note summarizes YAML frontmatter that is actually in use in the Taelgar vault, based on an automated scan of all Markdown files whose first line is `---` (as of 2025‑12‑10). It is descriptive of current practice rather than a normative design; see [[Metadata Spec]] and [[Display Control]] for implementation details, and [[Note Categorization]] for tag conventions.

## Scan summary

- ~2,400 notes currently have YAML frontmatter.
- ~60 distinct top‑level keys appear in those frontmatter blocks.
- The most common structural fields are `tags`, `dm_owner`, `dm_notes`, `headerVersion`, `whereabouts`, `name`, `typeOf`, `ancestry`, `species`, and `gender`.
- The sections below group fields by how they are used in practice and call out typical patterns by descriptive tag.

## Core structural fields

- `headerVersion`  
  String version marker added by header scripts (typically a date like `2023.11.25`). Present on most notes that have had their header regenerated.

- `tags`  
  Obsidian tags for categorization and status. Usually includes one descriptive tag (`person`, `place`, `organization`, `item`, `event`, etc.) and status tags (e.g. `status/stub`, `status/cleanup/*`, `status/gameupdate/*`). Represented as an inline list (`tags: [person]`).

- `dm_owner`  
  String indicating who is responsible for the page (`tim`, `mike`, `joint`,`player`, `none`, etc.). Used for workflow/ownership, not in‑world canon.

- `dm_notes`  
  Short status/priority note for DMs (`important`, `color`, `none`, etc.). Used heavily in clean‑up and review queries.

- `excludePublish`  
  List of strings used to exclude the page from specific outputs or sites (e.g. `["all"]`, `["Clee"]`, `["clee"]`). Values are interpreted by publishing/export workflows.

- `hide`  
  List controlling rendered site chrome, typically for published views (e.g. `hide: [toc]` or `hide: [toc, navigation]`). Often used on campaign landing pages and other meta notes.

- `template`  
  Name of a presentation template for some exported views (e.g. `template: home.html` on campaign home pages). Rare.

## Identity and naming

- `name`  
  Canonical page name used by display code. If omitted, the file name is used. Common on people, places, items, and session notes.

- `title`  
  In‑world title or honorific (e.g. `Queen`, `High King`, `Captain`). Combined with `name` in some contexts and used in affiliation displays.

- `aliases`  
  List of alternate names for the subject, including accented forms and alternate identities. Used in header displays and link resolution.

- `pronunciation`  
  Human‑readable pronunciation guide (e.g. `yoo-VAHN-tee`). 

- `gender`  
  Textual gender marker. Common values are `male`, `female`, or other strings; header scripts derive default pronouns from this.

- `pronouns`  
  Explicit pronoun string when the default from `gender` is not appropriate.

- `ka`  
  Numeric “ka” value, used for elves to indicate their cycle/generation (see `Elven Cycle of Generations`). Only appears on elven character notes.

- `image`  
  Lead image filename (and optionally path) associated with the page (e.g. `egnir-small.png`). Used in many person and item notes.

- `ddbLink` 
  External link to mechanics pages (typically D&D Beyond). 

- `population`  
  Population description for places. May be numeric or free‑form; numeric values are usually displayed with a `pop.` prefix.

- `tagline`  
  Short tagline or one‑line description. Common on session notes and some events/items, often used in header callouts.

- `descTitle`  
  Short descriptive title, used alongside or in place of the main `name` in session headers and some other notes.

## Classification and type

- `typeOf`  
  Primary type classification for the page (e.g. `settlement`, `region`, `war`, `mirror`, `mystery cult`, `skyship`). Required for many descriptive tags and used by header scripts and dataview queries.

- `typeOfAlias`  
  Human‑friendly display string for `typeOf` (e.g. “mountain range”, “city”). Used where a plain `typeOf` value would read awkwardly in prose.

- `subTypeOf`
  Secondary type classifier (e.g. `magical`, `ruined`, `caravanserai`). 

- `species`  
  Species of a person or creature (e.g. `human`, `elf`, `orc`). On some notes this is also used as the primary classification for species pages.

- `subspecies`  
  More specific subtype within a species (e.g. kinds of hag or undead). Not consistently used across the vault.

- `speciesAlias`  
  Display alias for a species, analogous to `typeOfAlias`.

- `ancestry`  
  Cultural or ancestry descriptor (e.g. `Chardonian`, `Sembaran`, `Dunmari`, `Dwarven`). Used on people, places, organizations, and some items for both display and querying.

- `deity`  
  On religious organization pages, the associated deity (e.g. `Laka`, `Bhishma`). Typically matches the name of a deity page.

## Temporal and chronology fields

- `born` / `created`  
  Start date for a person, organization, place, or item. Typically in DR as `YYYY`, `YYYY‑MM`, or `YYYY‑MM‑DD`. `born` is more common on people, `created` on items/organizations/places. 

- `died` / `destroyed`  
  End date for a person, organization, place, or item. Same date formats as `born`/`created`.

- `activeYear`  
  Single year representing when a person is active when precise birth date is unknown (e.g. orc leaders whose stories center on a particular conflict).

- `DR`  
  Primary in‑world date for an event, session, or sometimes a person or item. Typically `YYYY`, `YYYY‑MM`, or `YYYY‑MM‑DD` in Drankorian Reckoning.

- `DR_end`  
  End date for a DR range, used when the event or session spans multiple days.

- `realWorldDate`  
  Real‑world date a session was played, in `YYYY‑MM‑DD` form.

- `timelineDescriptor`  
  Label used in timelines and event lists (e.g. “War of the Cloak”). Often matches or summarizes the page title.

- `pageTargetDate`  
  Optional override for “current date” used by queries and header scripts, primarily for debugging or special displays.

## Relationship and linkage fields

- `whereabouts`  
  Current and historical location data. Older notes sometimes use a simple string; newer notes mostly use a list of objects with fields such as `type` (`home`/`away`), `location`, `start`, `end`, `prefix`, `linkText`, and optional formatting hints. Consumed by `get_Whereabouts` and many dataview queries.

- `affiliations`  
  Organizations or places the subject is associated with. Can be a list of strings (shorthand for member affiliations) or full objects with `org`, `place`, `type` (`primary`, `member`, `leader`), `title`, `start`, `end`, and optional formatting overrides. Used by `get_Affiliations` and various tables.

- `partOf`  
  Simple parent relationship field, primarily for events and organizations (e.g. an event being part of a war). For places, `whereabouts` is preferred.

- `companions`  
  List of notable NPCs, creatures, or groups associated with a session, person, or item (e.g. names of traveling companions on session notes, or linked NPCs on item notes).

- `players`  
  List of PC names present in a session (e.g. `[Kenzo, Wellby, Delwath, Seeker, Riswynn]`).

- `player`  
  Real‑world player name on PC notes (e.g. `player: Chris Kelly`).

- `pcOwner`  
  Name of the PC that owns an item; used mainly on treasure/equipment notes for dataview queries.

- `campaignInfo`  
  List of objects capturing when and how campaigns interacted with this page. Each entry may include `campaign` (short code like `dufr`), `type` (e.g. `met`, `killed`, `seen`), optional `person`, `date`, and optional format overrides. Drives “Met by X on Y in Z” style header lines.

- `sessionNumber`  
  Numeric session identifier within a campaign.


## Display and header control

- `displayDefaults`  
  Object controlling how the header box is rendered for this page. Common keys include `startStatus`, `endStatus`, `wOrigin`, `wHome`, `wCurrent`, `wPast`, `wParty`, `boxName`, `boxInfo`, `partOf`, `aNoDate`, `aPast`, `aCurrent`, and variants. Many pages rely on type‑level defaults; some override specific entries (e.g. places with custom origin phrases or organizations that display deity information).



## Common frontmatter patterns by descriptive tag

Based on the scan, the following patterns are typical for different descriptive tags. These are descriptive, not hard requirements, but are useful as templates when creating or cleaning up notes.

### `person`

Typical person pages (e.g. `People/*/*.md`) have:

- `headerVersion`, `tags: [person, …]`
- Identity fields: `name`, `species`, `ancestry`, `gender`, optional `pronouns`, `aliases`, `pronunciation`, optional `image`
- Chronology: `born`, optional `died`
- Relationships: `affiliations`, `whereabouts`, optional `campaignInfo`
- Special cases: `ka` for elves; `player` for PCs
- Meta: `dm_owner`, `dm_notes`, and sometimes status tags under `tags`

### `place`

Typical place pages (e.g. `Gazetteer/*/*.md`) have:

- `headerVersion`, `tags: [place, …]`
- Classification: `typeOf` (e.g. `settlement`, `region`, `topographical feature`), optional `typeOfAlias`, optional `ancestry`
- Identity: `name`, sometimes `population`
- Chronology: optional `created` / `destroyed`
- Relationships: `whereabouts` (string or list, often nested), occasional `affiliations`
- Display: optional `displayDefaults` overrides (e.g. custom `startStatus`)
- Meta: `dm_owner`, `dm_notes`, sometimes `excludePublish`

### `organization`

Typical organization pages (e.g. factions, noble houses, mystery cults) have:

- `headerVersion`, `tags: [organization, …]`
- Classification: `typeOf` (e.g. `mystery cult`, `adventuring company`), optional `ancestry`
- Identity: `name`, occasionally `title` for leaders
- Chronology: optional `created` / `destroyed`
- Relationships: `affiliations` and/or `whereabouts`, optional `deity`
- Meta: `dm_owner`, `dm_notes`

### `item`

Typical item/treasure pages (mostly under campaign treasure folders) have:

- `headerVersion`, `tags` including `item` or `item/*`
- Classification: `typeOf` (e.g. `mirror`, `ring`), optional `subTypeOf`/`subtypeOf` (e.g. `magical`)
- Identity: `name`, optional `image`, `rarity`
- Relationships: `whereabouts` (often a list of home/away locations over time), optional `pcOwner`
- Mechanics: `ddbLink` where appropriate
- Display: optional `displayDefaults` tweaks

### `event`

Event pages (e.g. historical battles or wars) typically have:

- `headerVersion`, `tags: [event]`
- Classification: optional `typeOf` (e.g. `war`), `timelineDescriptor`
- Chronology: `DR`, optional `DR_end`
- Relationships: `whereabouts` for main location, optional `partOf` for larger conflicts
- Meta: `dm_owner`, `dm_notes`

### `session-note`

Session notes (primarily under `Campaigns/*/Session Notes`) typically have:

- `tags: [session-note]`
- Identity: `name` (often `Campaign – Session N`), `tagline`, `descTitle`
- Chronology: `campaign`, `sessionNumber`, `realWorldDate`, `DR`, optional `DR_end`
- Relationships: `players`, optional `companions`

### `species` and other background/meta pages

Species pages and many background/meta notes often have minimal metadata:

- `tags: [species]` (or other background/meta tag) and optionally `headerVersion`
- Optional `ancestry`/`species` classification fields if they are meant to be linked from person/place notes
- `dm_owner`, `dm_notes` where relevant

Pages under `_MoC`, `_templates`, `_scripts`, and other meta directories frequently omit descriptive tags entirely or use `meta`, and rely mainly on `hide`, `template`, and `status/*` tags.

---

This specification is intended to reflect how metadata is currently used in the vault. Future clean‑up passes can refine it into a stricter, prescriptive schema and update this note accordingly.

