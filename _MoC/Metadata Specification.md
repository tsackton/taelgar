# Metadata Specification
*last update: Dec 15th 2025*

This note summarizes the metadata specification for YAML frontmatter. 

Some brainstorming and ideas:
- [[Metadata Brainstorming - Discussion]] (old but still potentially relevant)

## Metadata Field Definitions

### Core Universal Fields

- `headerVersion`: String version marker added by header scripts (typically a date like `2023.11.25`). Automatically added upon header generation. Do not manually edit. 
- `tags`: Obsidian tags for categorization and status. One descriptive tag is usually required (`person`, `place`, `organization`, `item`, `event`, etc.); status tags (e.g. `status/stub`, `status/cleanup/*`, `status/gameupdate/*`) are optional. Represented as an inline list (`tags: [person]`). See: [[Note Categorization]] and [[Note Status]].
- `dm_owner`: String indicating who is responsible for the page. Acceptable values: `tim`, `mike`, `joint`, `player`, `none`. See: [[Note Status]]
- `dm_notes`: String indicating whether dm notes exist. Acceptable values: `important`, `color`, `none`. See: [[Note Status]].
- `name`: Canonical page name used by display code. If omitted, the file name is used. 
- `aliases`: List of alternate names for the subject, including accented forms and alternate identities. Used primarily in link resolution.
- `pronunciation`: Human‑readable pronunciation guide (e.g. `yoo-VAHN-tee`). 
- `image`: Lead image filename (and optionally path) associated with the page (e.g. `egnir-small.png`). Not used by any core header generation functions but very useful in data view tables, i.e. of items.

### Classification and Type Fields

- `typeOf`: Primary type classification for the page (e.g. `settlement`, `region`, `war`, `mirror`, `mystery cult`, `skyship`). Required for many descriptive tags and used by header scripts and dataview queries. Controlled vocabulary; see: [[Note Categorization]].
- `species`: Species of a person or creature (e.g. `human`, `elf`, `orc`). Used as an alias for typeOf on `person` pages. This should usually match the name or an alias of a creature page, and will generate a link in the header if it matches. See: [[Note Categorization]].
- `typeOfAlias`: Human‑friendly display string for `typeOf` (e.g. “mountain range”, “city”). Free text, not controlled. Used to provide more specific and more useful header text than a plain `typeOf` value. See: [[Note Categorization]].
- `subTypeOf`: Secondary type classifier. *Potentially obsolete, and used inconsistently; avoid adding new for now*. See: [[Note Categorization]].
- `subspecies`: Alias for subTypeOf used on person pages. *Potentially obsolete, and used inconsistently across pages; avoid adding new for now.* See: [[Note Categorization]].
- `speciesAlias`: Alias for typeOfAlias used on person pages. *Potentially obsolete, and used inconsistently across pages; avoid adding new for now.* See: [[Note Categorization]].
- `ancestry`:Cultural or ancestry descriptor (e.g. `Chardonian`, `Sembaran`, `Dunmari`, `Dwarven`). Can potentially be used on any note. This should usually match the name or alias of a culture or realm page, and will generate a link in the header if it matches. See: [[Note Categorization]].
- `deity`: On religious organization pages, the associated deity (e.g. `Laka`, `Bhishma`). Typically matches the name of a deity page. ***Warning: possibly obsolete / will likely be depreciated.**

### Temporal and Chronology Fields

See: [[Metadata Specification#Date Formats|Date Formats]]

- `born` / `created`: Start date for a person, organization, place, or item. Typically in DR as `YYYY`, `YYYY‑MM`, or `YYYY‑MM‑DD`. Synonyms and treated the same way in code. `born` is used for person notes, `created` for other notes. 
- `died` / `destroyed`: End date for a person, organization, place, or item. Same date formats as `born`/`created`. Synonyms and treated the same way in code. `died` is used for person notes, `destroyed` for other notes. Note that a died of 0001 can be used to indicate "died at a unknown but long ago date"
- `DR`: Primary in‑world date for an event or session. Typically `YYYY`, `YYYY‑MM`, or `YYYY‑MM‑DD` in Drankorian Reckoning.
- `DR_end`: End date for a DR range, used when the event or session spans multiple days. Same date format as DR. 
- `realWorldDate`: Real‑world date a session was played, in `YYYY‑MM‑DD` form.
- `timelineDescriptor`:Label used in timelines and event lists (e.g. “War of the Cloak”) for dates extracted from this note. Often matches or summarizes the page title. ***Warning: possibly obsolete / possibly not working, and inconsistently used.***
- `pageTargetDate`: Optional override for “current date” used by queries and header scripts, primarily for debugging. 

### Type-Specific Fields

For person pages, for additional display/identity information:
- `title`: In‑world title or honorific (e.g. `Queen`, `High King`, `Captain`). Combined with `name` to produce a full name; see [[Display Control]].
- `gender`: Textual gender marker. Common values are `male`, `female`, or other strings; header scripts derive default pronouns from this.
- `pronouns`: Explicit pronoun string when the default from `gender` is not appropriate.
- `ka`: Numeric “ka” value, used for elves to indicate their cycle/generation (see [[Elven Cycle of Generations]]). Only appears on elven character notes.

For PC pages:
- `player`: Real‑world player name on PC notes (e.g. `player: Chris Kelly`).

For items:
- `pcOwner`: Name of the PC that owns an item; used mainly on treasure/equipment notes for dataview queries. ***Warning: inconsistently used, possibly will be depreciated***
- `rarity`: Used specifically for magic items. ***Warning: inconsistently used, possibly will be depreciated***

For item and PC pages:
- `ddbLink`: External link to mechanics pages (typically D&D Beyond). 

For settlements or possibly realms, to set a population:
- `population`: Population description for places. May be numeric or free‑form; numeric values are usually displayed with a `pop.` prefix.

For session notes to generate headers and indexes:
- `tagline`: Short tagline or one‑line description. 
- `descTitle`: Short descriptive title.
- `companions`: List of NPCs that traveled with the party during a session. 
- `players`: List of PC names present in a session (e.g. `[Kenzo, Wellby, Delwath, Seeker, Riswynn]`).
- `sessionNumber`: Numeric session identifier within a campaign.

### Relationship and Linkage Fields

- `whereabouts`: Current and historical location data. Can be a simple string, or a list of objects. Typically used for people and places, and occasionally for organizations and items. See [[Metadata Specification#Metadata Specification#Whereabouts Specification|details below]]. 
- `affiliations`: Organizations or places the subject is associated with. Can be a list of strings (shorthand for member affiliations) or full objects. Typically only used for people. See [[Metadata Specification#Metadata Specification#Affiliations Specification|details below]]. 
- `campaignInfo`: List of objects capturing when and how campaigns interacted with this page. Each entry may include `campaign` (short code like `dufr`), `type` (e.g. `met`, `killed`, `seen`), optional `person`, `date`, and optional format overrides. Drives “Met by X on Y in Z” style header lines. Typically used only for people, but in principle could be used for any note. See [[Metadata Specification#Metadata Specification#CampaignInfo Specification|details below]].
- `partOf`: Simple parent relationship field. Used for non-location based relationships. Principally used to indicate organizations that are part of a larger organization (e.g., a unit in an army), or events that are part of a larger event (e.g., a battle in a war). For place-based relationships, use `whereabouts` which can handle much more complex information. 

### Display and header control

- `displayDefaults`: Object controlling how the header box is rendered for this page. See: [[Display Control]]. 

### Taelgarverse

- `excludePublish`: List of strings used to exclude the page from specific outputs or sites. Acceptable values: "all" or a campaign string (e.g., "dufr", "clee", "adma", etc). Used to exclude a page from Taelgarverse display. 
- `hide`: Used by Taelgarverse / Material for Markdown for display control. 
- `template`: Used by Taelgarverse / Material for Markdown for display control. 
- `activeYear`: Can be used to control page display; building Taelgarverse with an active year < the activeYear of a page will treat the page as not existing. 

## Frontmatter Patterns by Tag

Different page types (defined by descriptive tags) expect different metadata patterns. These are typical, not required. ALL notes may have one or more of the core universal fields; these are not listed below. 

### `person`

Typical person pages (e.g. `People/*/*.md`) have:

- Identity and Classification fields: `name`, `species`, `ancestry`, `gender`, optional `pronouns`if different from what is implied by gender, `aliases`, `pronunciation`, optional `image`
- Chronology: `born`, optional `died`
- Relationships: `affiliations`, `whereabouts`, optional `campaignInfo`
- Special cases: `ka` for elves; `player` and `ddbLink` for PCs

### `place`

Typical place pages (e.g. `Gazetteer/*/*.md`) have:

- Identity and Classification: `typeOf`, optional `typeOfAlias`, optional `ancestry`, `name`, sometimes `population`, `pronunciation`
- Chronology: optional `created` / `destroyed`
- Relationships: `whereabouts` 

### `organization`

Typical organization pages (e.g. factions, noble houses, mystery cults) have:

- Identity and Classification: `typeOf`, optional `typeOfAlias`, optional `ancestry`, `name`, `pronunciation`
- Chronology: optional `created` / `destroyed`
- Relationships: `partOf` and/or `whereabouts`

### `item`

Typical item/treasure pages (mostly under campaign treasure folders) have:

- Classification: `typeOf` (e.g. `mirror`, `ring`), optional `subTypeOf` (e.g. `magical`), `typeOfAlias`
- Identity: `name`, optional `image`, `rarity`
- Relationships: `whereabouts`, optional `pcOwner`
- Mechanics: `ddbLink` where appropriate

### `event`

Event pages (e.g. historical battles or wars) typically have:

- Classification: optional `typeOf` (e.g. `war`), `timelineDescriptor`
- Chronology: `DR`, optional `DR_end`
- Relationships: `whereabouts` for main location, optional `partOf` for larger conflicts

### `session-note`

Session notes (primarily under `Campaigns/*/Session Notes`) typically have:

- Identity: `name` (often `Campaign – Session N`), `tagline`, `descTitle`
- Chronology: `campaign`, `sessionNumber`, `realWorldDate`, `DR`, optional `DR_end`
- Relationships: `players`, optional `companions`

## Whereabouts Specification

Purpose: drive header/location lines and queries. Used on people, places, items, organizations. Strings are accepted for simple cases; use objects for history. Whereabouts are encoded as a YAML object with a set of defined fields, that allow everything from very simple "Based in (Location)" to complex chains of locations across the journey of an NPC. 
### Object Fields

The following object fields are used to define a whereabout entry; see Derived Whereabouts, below:
- `location` (required): string target; NameManager resolves the file.
- `type`: `home`, `away`, or `secondary`; `primary` is used as a synonym for `home`, typically for clarity in places with both primary and secondary whereabouts. 
- `start` / `date`: start date; `date` is an alias for `start`. Typical date formatting applies. 
- `end`: end date. Typical date formatting applies. 

The following object fields are used for display formatting; see Whereabouts Formatting, below:
- `alias`: alternate display text, shown instead of `location`. 
- `linkText`: custom link text/prefix when embedded in chains.
- `format`: per-hop format override (applied after displayDefault).
- `startFilter`: per-chain filter override when the chain starts from this whereabout.
- any valid displayDefault key can also be specified in a whereabout. 

#### Valid Types

There are currently three valid types, `home`, `away`, and `secondary`; `primary` is a synonym for `home`.
- Type `away` always represents a location where something is
- Type `home` is used not just to represent location, but also creator/founder/maker/owner etc
	- Generally speaking, for people, home is where you are from and where you are based
	- Generally speaking, for things/organizations, home defines either founder/creator if it points to a person, or place founded/created if it points to a location. To get made by person in location, you need to set the whereabouts of the person for created date, as presumably that person must have been in that place at that time. 
	- For locations, home is always used to represent current physical location, as places cannot typically go on trips (if they can, they are probably vehicles, not places)
- Type `secondary` is used when a particular target, usually a location, is located in two overlapping context. For example, a river can be both in a watershed, and in a region. The primary whereabout is aliased to home in the code and is used for chain construction; the secondary location is only displayed on the target page, and is never shown as part of a whereabout chain on other pages. 

#### Shorthand

Whereabouts in the format: `whereabouts: string` are converted by whereabouts manager to: `whereabouts: [{type: home, location: string}]`

### Derived Whereabouts

The whereabouts manager derives five whereabouts for a given page at the targetDate of the page. 

* The `origin` whereabout is the earliest home whereabout, or if there are multiples with the same date, the first in the file. It represents where someone is from
* The `home` whereabout is the home whereabout that is (a) valid (i.e. it has started and hasn't ended) and (b) with the most recent start date
* The `current` whereabout is the whereabout that is (a) valid (i.e. it has started and hasn't ended) and (b) has the most recent start date
* The `lastKnown` whereabout is only set if the current whereabout is not found (i.e. there are no valid current whereabouts). In that case, the lastKnown whereabout is the home or away whereabout with the most recent end date
- The `secondary` whereabout is the most recent valid `secondary` (independent of `home/current`); only exists if a `secondary` whereabout is defined. 

These are used in formatting; see below. 

### Whereabouts Formatting

Each derived whereabouts is formatted as a chain of locations, which are then displayed in the header following displayDefaults. See [[Display Control]] for more details about basic formatting and substitution tokens. Some whereabouts-specific overrides are described here. 

Each whereabout change is generated by following a chain from `location` to the target page's `current`, repeating until filters stop traversal. This full chain is then used as the `<origin>`, `<home>`, `<current>`,`<lastKnown>`, or `<secondary>` token for string generation. By default, formatting of the chain is determined by the displayDefault substitution tokens - see [[Display Control]]. However, the whereabouts object has a variety of ways to override the default display, that can be useful for handling special cases. 

(1) `displayDefaults` key. This overrides the displayDefaults specifically when that whereabouts line is used. For example, if a whereabouts line specifies a format string for `wLastKnown`, that format string is only used if that whereabouts line is used to generate `wLastKnown`. If a different whereabouts line is used for `lastKnown`, the display override will not come into effect. 

(2) `startFilter`. This overrides the typical location chain formatting (see: [[Display Control]]), whenever this location is used in a whereabout chain. This applies to all display lines originating from this whereabout; to override the location chain *only for a specific derived whereabout*, you need to rewrite the correct displayDefaults. `startFilter` can use any of the location chain formatting tokens, see [[Display Control]]. Does not apply if this whereabout is the middle part of a chain. 

(3) `format`. This overrides the `<name>` format used by the formatter for this whereabout, whenever it is used. This applies to all display lines involving this whereabout; to override the location chain *only for a specific derived whereabout*, you need to rewrite the correct displayDefaults. `format` can use any of the linking, casing, or other formatting tokens, see [[Display Control]]. Does apply even if this whereabout is the middle part of a chain. 

(4) `alias`. This generates an alias for the location string when this whereabout is used; only relevant for linking, which is displayed as `[[location|alias]]`. Functions like a whereabout-specific version of the `alias` metadata otherwise present in a note. Does apply even if this whereabout is the middle part of a chain. 

(5) `linkText`. This overrides the usual link text leading to this whereabout location in a location chain. Used any time this location is part of a chain and prepositions are displayed. Does apply even if this whereabout is the middle part of a chain. 

**Usage guidance.**

Whereabouts formatting can be complicated. Some general patterns/tips:
- `alias` and `linkText` can be used to generate simply display tweaks: a ship moored at a port could use `linkText: "moored at"` to generate a whereabouts "moored at (location)". These are fairly simple to use and have obvious meanings, as they always replace the location and prepositions for that whereabout. If `linkText` doesn't display, it might be because the standard displayDefaults for that page do not display prepositions, in this case setting format to `<name:q>` can fix the problem. 
- `startFilter` and `format` are less frequently used. `startFilter` replaces the location chain when this whereabout is the start of chain; `format` replaces the name formatting for this whereabout everywhere. Start formatting is most commonly used for complex whereabouts to reduce information or avoid annoying chains (for example, a person imprisoned in the Mirror of Soul Trapping on Vindristjarna might want a startFormat: 2 to avoid displaying Vindristjarna's full location). `format` is frequently used to add a preposition to `wLastKnown` and `wLastNoDate`, which by default don't include prepositions. These are complementary: `startFormat` only affects location chain filtering; `format` only affects name display
- `displayDefaults` can be used if needed for complex overrides, but are rarely required and should be avoided unless needed. 

### Whereabouts Examples 

```yaml
# Simple home via string shorthand (People/Dunmari/Shandan)
whereabouts: [{type: home, location: plains of Songara}]
```

```yaml
# Home + away with dates (People/Orcs/Nogu)
whereabouts:
  - {type: home, location: Xurkhaz}
  - {type: away, location: Mirror of Soul Trapping, start: 1680, end: 1748-12-04}
```

```yaml
# Vehicle with startFilter and per-hop linkText/alias (Things/Ships/Wave Dancer)
whereabouts:
- {type: home, end: 0001, location: Eastern Green Sea}
- {type: away, start: 1748-09-30, end: 1748-10-11, location: sailing to Wahacha, startFilter: "2" }
- {type: away, start: 1748-10-12, end: 1748-10-14, alias: main port of Wacahca, location: Wahacha, linkText: moored in, format: "<name:q>", startFilter: "2" }
```

```yaml
# Secondary container displayed via wSecondary (Cosmology/Plane of Creation)
displayDefaults: {wSecondary: "Sometimes considered part of <secondary:1>", wHome: "A <typeOf> in the <home:1s>"}
whereabouts: 
  - {type: primary, location: Multiverse}
  - {type: secondary, location: Astral Plane}
```

```yaml
# Per-hop display tweak with linkText and format (People/Dunmari/Illyan)
whereabouts:
  - {type: away, start: 1748-06-03, end: 1748-12-14, linkText: camped near, location: Tokra, format: "<name:q>"}
```

### Deprecated Behavior 

Some behavior that does not conform to the above requirements is still supported by code, including:

- Location specified as place/region, concatenated into a location string.
- Heuristic splitting of `location` strings on capital letters to continue a chain when the exact target note is missing; prefer real targets/aliases instead.
- Place pages with no `whereabouts` but with `partOf` are treated as `{type: home, location: <partOf>}` (kept for backward compatibility; avoid adding new).

## Affiliations Specification

Purpose: track organizational ties between a page and organizations, places, families, ships, and similar entities. Used primarily on people, and occasionally on organizations, places, or items. Affiliations are encoded as YAML values that range from simple strings (“member of X”) to structured objects, and can drive both header lines and queries. 

### Object Fields

The following object fields are used to define an affiliation entry; see Derived Affiliations, below:
- `org` (required for new data): name of the organization, place, family, ship, etc. that the page is affiliated with. NameManager resolves this to a file when possible.
- `place`: synonym for `org: place, type: leader`.
- `type`: `member`, `primary`, or `leader`. If omitted, defaults to `member`; if `place` is present and `type` is omitted, defaults to `leader`. `primary` marks the main affiliation for this page.
- `title`: role label for this affiliation (Captain, Lord, Guardsman, Proprietor, etc.). Defaults to the page’s `title` when `type: leader`, otherwise to the affiliation `type`.

The following object fields are used for dating; see Affiliations Formatting, below:
- `start`: start date of the affiliation. If omitted, defaults to `0001`. Typical date formatting applies.
- `end`: end date of the affiliation. If omitted, defaults to the page’s end date (`died` / `destroyed` / `DR_end`) when present, otherwise to `9999`. Typical date formatting applies.

The following object fields are used for display formatting; see Affiliations Formatting, below:
- `format`: per‑affiliation display override used when explicit formatting is required and dates are not driving the choice. Overrides all other formatting. 
- `formatPast`: per‑affiliation display override used when the affiliation has ended. Must be present with `formatCurrent`; overrides all other formatting. 
- `formatCurrent`: per‑affiliation display override used when the affiliation is current. Must be present with `formatPast`; overrides all other formatting. 

#### Valid Types

Affiliations distinguish between several common cases:

- `member`: the default; indicates a straightforward membership or association (guild member, soldier in a regiment, etc.).
- `primary`: the main or defining affiliation for a page. Primary affiliations are surfaced via `<primary>` tokens; by default, these are displayed in a header line like “of the Chapmans” instead of in the affiliations line. 
- `leader`: indicates that the page is in charge of the `org`/`place` (lord of a manor, captain of a ship, commander of a regiment, etc.). Leader affiliations are used by “ruled by / led by” logic and are date‑aware.

#### Shorthand

- If the affiliation line is a string, it is shorthand for `{org: <value>, type: member }`, and note this can be mixed and matched with full objects in the affiliations list. 
* Setting `place` instead of `org` is a shorthand for setting `org` and `type: leader`
* If the type is not set, it is considered to be  `member`
* If the type is leader the page's title is used for the title
* If the type is not leader, the title is "Member" if it is not set
* If the start date is not set it is considered `0001`
* If the end date is not set it is considered the page end date, if set, or `9999` otherwise

###  Affiliations Display

For a given page at its targetDate, the affiliation manager normalizes, filters, and then groups affiliations for display:

- Only affiliations whose `start` date is on or before the targetDate are considered; future affiliations are ignored.
- Primary affiliations (`type: primary`) are kept as a separate list, used by `<primary>` tokens and by some header `boxInfo` templates.
- Non‑primary affiliations (anything not `primary`) are grouped by `title + startDate + endDate + format`, so multiple entries with identical dates and role share a single display line and list of orgs.

These normalized groups are then used by the affiliations header view to build the “Affiliations” block for the page, and by helper functions such as `isAffiliated` and `isOrWasAffiliated` to answer query questions.

### Affiliations Formatting

Affiliation display is driven by the `aNoDate`, `aCurrent`, `aPast`, and `aPastHasStart` displayDefaults for the page type, plus optional per‑affiliation overrides:

(1) `format`. If an affiliation has `format` (including the empty string), that string is used as the format for that group, regardless of dates. This is the strongest per‑line override and completely replaces the default “member of X” style string for that group.

(2) `formatPast` / `formatCurrent`. If both `formatPast` and `formatCurrent` are present, the code picks one based on whether the affiliation is still active at the targetDate. This allows a single affiliation to have different text while current vs. historical.

(3) Default displayDefaults. When no per‑line formats are provided, the code chooses between `aCurrent`, `aPastHasStart`, `aPast`, and `aNoDate` based on whether the start and end dates are displayable and whether the affiliation is still active.

All of these formats can use the standard substitution tokens documented in [[Display Control]], plus two affiliation‑specific values:

- `affiliationtitle`: the resolved `title` for the group (“Captain”, “Lord Mayor”, etc.).
- `affiliations`: the set of affiliations in the group, used to build the “org list” for that line (typically rendered as “org A, org B, and org C”).

Primary affiliations use the same rules but are displayed only in contexts that explicitly request `<primary>` (for example, as part of a header line “of the Chapmans”).

**Usage guidance.**

Affiliation formatting is typically much simpler than whereabouts. Some general patterns/tips:
- For most NPCs, a simple object `{org: X, type: primary}` or a shortlist like `[Org A, Org B]` is sufficient; dates are often left blank and inferred from the page.
- Use `type: leader` (and optionally `title`) when the page represents someone in charge of a place, ship, inn, regiment, or similar; this enables “ruled by / led by” logic and date‑aware leadership queries.
- Reserve custom `format` / `formatPast` / `formatCurrent` for special cases where the default “Member of X” phrasing is not appropriate; keep them local to the one affiliation that truly needs custom text. Note that while custom formatting is supported in the code, it is almost never used in practice and probably is not necessary. It is typically better to override the appropriate displayDefaults for a page if needed. 

### Affiliations Examples 

```yaml
# Simple primary with no dates (People/Orcs/Azogar)
affiliations: [{org: People of the Rainbow, type: primary}]
```

```yaml
# Simple leader using place shorthand, defaults to title in main metadata
affiliations: [{place: Manor of Asineau}]

# Leader with explicit title and dates (People/Sembarans/Lorin Valbert)
affiliations:
  - {org: Manor of Asineau, start: 1715, end: 1720-01-13, title: Lord, type: leader}
  
# Leader of multiple places
affiliations:
- {place: Sembara, start: 1648-12-11}
- {place: Tyrwingha, start: 1648-12-11}
- {org: House of Sewick, type: primary}
  
# Proprietor of an inn
affiliations: 
- {org: Strongbones, type: primary}
- {org: The Red Lily Inn, title: Proprietor, type: leader, start: 0001} 
```

```yaml
# Explicit staff role with a title (People/Addermarians/Isolde of Roscombe)
affiliations: [{org: Temple of the Sibyl , title: temple steward, type: member}]
```

### Deprecated Behavior

Some behavior that does not fully conform to the above requirements is still supported by code, including:

- leaderOf frontmatter, which is converted into type: leader affiliations based on its place entries and reignStart date. New notes should prefer writing affiliations directly.
- Legacy per‑line aNoDate / aPast / aPastWithStart / aCurrent keys, which are retained for backwards compatibility; treat them as shorthand for format / formatPast / formatCurrent when editing older notes.

## CampaignInfo Specification

Purpose: track when and how specific campaigns interacted with the subject of a page. Used primarily on people (and occasionally places/items) to drive “Met by X on Y in Z” style header lines and to answer “does this party know about this entity?” queries. CampaignInfo entries are encoded as structured objects and can range from simple “met on this date” records to fully customized lines that reference specific session notes. If a campaign and date are present, generates a static header line with the campaign interaction information. 

### Object Fields

The following object fields are used to define a campaignInfo entry; see Derived Campaign Interactions, below:
- `campaign` (required): short code for the campaign (e.g., `DuFr`, `Clee`, `MC`). Used both for display and to match against configured campaign prefixes in `.obsidian/metadata.json`. Output lines are wrapped in campaign blocks with this code. 
- `date` (required for display): the in‑world date of the interaction. Typical date formatting applies; if missing, the entry can still be used for “knows about” queries but will not generate a header line.
- `type`: describes the interaction itself (e.g., `met`, `killed`, `freed`, `seen`, `attended his lecture`). Defaults to `seen` when omitted. 
- `person`: optional override for who did the interacting. If omitted, defaults to the `campaign` code (which is then resolved to a page via NameManager and linkmap). Typically used when only a specific PC should appear in the output line. 

The following object fields are used for display formatting; see CampaignInfo Formatting, below:
- `format`: per‑entry display override for this campaignInfo record. Acts as a replacement for the default `wParty` template for this entry.
- `wParty`: synonym for `format`, kept for backwards compatibility, but `format` is preferred. 

#### Minimal vs. Displayable Entries

CampaignInfo entries can be present without a `date`. These entries:

- Still mark the page as “known to” a campaign (for `isKnownToParty` checks).
- Do **not** generate any visible header lines, as display requires both `campaign` and `date` and a resolvable whereabouts at that date.

In practice, this allows you to track that a party is aware of an NPC even if you don’t care about the exact first‑met date.

### Derived Campaign Interactions

For a given page, the event manager derives a list of “party meeting” entries by:

- Filtering `campaignInfo` to entries that have both `campaign` and `date`.
- For each such entry:
	- Normalizing `date` via `DateManager.normalizeDate`.
	- Looking up the page’s whereabouts at that date and computing the `current` location via `WhereaboutsManager.getWhereabouts(metadata, date).current`.
	- Skipping the entry if no current location can be determined (no line is emitted if the location is unknown at that date).
	- Determining `person` as `person` if set, otherwise the `campaign` string.
	- Determining `type` as `type` if set, otherwise `seen`.

The result is a list of records:

- `text`: fully formatted “Met by X on Y in Z” style line for that entry.
- `campaign`: the campaign code for the entry (e.g., `DuFr`).
- `date`: normalized date of the interaction.
- `location`: the resolved `current` location name at that date.

These are ordered as they appear in `campaignInfo` and output as header lines, wrapped in campaign blocks. 

### CampaignInfo Formatting

CampaignInfo display is driven by the `wParty` displayDefault for the page type, potentially overwritten by the `format` entry on a specific campaignInfo line. See [[Display Control]] for more about formatting. 

CampaignInfo display strings recognize some special tokens in addition to the usual tokens:
- `met`: the interaction type for this entry (from `type`, default `seen`).
- `person`: the actor for this entry (from `person`, or the campaign code if `person` is omitted).

**Usage guidance.**

CampaignInfo is easiest to work with if you follow some simple patterns:
- For straightforward “met the party” records, use just `campaign`, `date`, and (optionally) `type` and `person`, letting the default `wParty` handle formatting.
- Set `person` when only a subset of the party was present (e.g., `Seeker`).
- Use `format` on an entry only when you need to:
	- Link directly to a specific session note in the line (e.g., wrapping `<target>` in a `[[Session N|…]]` link).
	- Change the sentence structure away from the default `wParty` pattern.
- It is often useful to add a campaignInfo entry **without** a date to mark that a party knows about someone; do this when you want `isKnownToParty` to succeed even if no specific “met on X” header line is needed.
- Note that typically linking prepositions are hard-coded in the display string, so you need to generate a full `format` line if you want to change prepositions. 
### CampaignInfo Examples 

```yaml
# Simple kill record with default formatting (People/Orcs/Gorkil)
campaignInfo:
  - {campaign: DuFr, person: Seeker, type: killed, date: 1748-05-05}
```

```yaml
# Custom free‑from‑mirror line with a session link (People/Orcs/Nogu)
campaignInfo:
  - {campaign: DuFr,
     type: "freed from the [[Mirror of Soul Trapping]] into [[Lubash|Lubash's]] care",
     date: 1748-12-05,
     format: "<met:u> by <person> on [[Session 71 (DuFr)|<target>]] in <current:1>"}
```

```yaml
# Complex interaction description using met/person tokens (People/Dunmari/Johar)
campaignInfo:
  - {campaign: DuFr, date: 1749-02-01, type: reunited,
     format: "<met:t> with <person> on <target> <current:2qr>"}
```

## Date Formats

Date handling is centralized in `DateManager`. Currently, most dates are assumed to be DR dates, input as number or strings, in `YYYY`, `YYYY-MM`, or `YYYY-MM-DD` formats.  There is the potential for `DateManager` to handle non-DR dates, but this is not yet implemented cleanly. 

Normalization: `normalizeDate(value, isEnd)` returns `{display, sort, year, days, isHiddenDate}` using DR as the base calendar. Numeric years default to Jan 1 for starts and Dec 31 for ends; month-level strings default to the last day of the month for starts and the first day for ends. Sentinel years `0001`/`9999` are hidden but usable for ranges; see below. 

Page dates: `born/created` set the start date; `died/destroyed` set the end date. For event pages, `DR`/`DR_end` act as start/end when no born/created/destroyed dates exist. `pageTargetDate` overrides the “current date”; otherwise Calendarium/Fantasy Calendar supplies it.

Display and math: DR display uses `Month Day, Year` (e.g., “December 9th, 1748”). Age/length calculations use the `days` delta between normalized dates, with `0001`/`9999` omitted from display. 

Special dates: `0001` and `9999` are treated as special dates. They are never displayed, and treated as "before all possible dates" and "after all possible dates", respectively. The `0001` date is useful for people who are definitely dead in modern campaigns but don't have an assigned date of death; the `9999` date is useful for away whereabouts to imply "at a temporary location at all future times". 
