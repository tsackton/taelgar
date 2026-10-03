---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:10:06-04:00"
lintVersion: "3.5"
tags: [person, status/cleanup/metadata, status/check/lint]
species: human
ancestry: Dunmari
campaignInfo:
  - {campaign: dufr, date: 1748-06-30, type: first met}
  - {campaign: dufr, date: 1748-07-16, type: began traveling, format: "<met:U> with <person> on <target> <current:2qr>"}
  - {campaign: dufr, date: 1748-08-08, type: parted ways, format: "<met:U> with <person> on <target> <current:2qr>"}
  - {campaign: dufr, date: 1748-10-22, type: scryed, person: Delwath}
  - {campaign: dufr, date: 1748-11-17, type: reached by Sending, person: Riswynn, format: "<met:tx> cast by <person> on <target> <current:2qr>"}
  - {campaign: dufr, date: 1749-02-01, type: reunited, format: "<met:t> with <person> on <target> <current:2qr>"}
born: 1721
gender: male
name: Johar
whereabouts:
  - {type: home, location: Tokra}
  - {type: away, start: 1748-07-17, end: 1748-08-07, location: dufr}
  - {type: away, start: 1748-08-08, end: 1748-08-08, location: Darba}
  - {type: away, start: 1748-08-27, end: 1748-11-16, location: Nayahar}
  - {type: away, start: 1748-11-17, location: Nayahar}
  - {type: away, start: 1748-12-25, end: 1749-02-01, location: Copper Hills}
  - {type: away, start: 1749-02-01, end: 1749-03-02, location: Copper Hills}
  - {type: away, start: 1749-03-02, location: traveling to Tokra}
knownTo: [dufr]
dm_owner: tim
dm_notes: important
POV: 1748
---
# Johar
>[!info]+ Biographical Info  
> A [[Dunmar|Dunmari]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:DuFr%% First met by the [[Dunmar Fellowship]] on June 30th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%  
>> %%^Campaign:DuFr%% Began traveling with the [[Dunmar Fellowship]] on July 16th, 1748 in [[Tokra]], [[Dunmar]] %%^End%%  
>> %%^Campaign:DuFr%% Parted ways with the [[Dunmar Fellowship]] on August 8th, 1748 in [[Darba]], [[Dunmar]] %%^End%%  
>> %%^Campaign:DuFr%% Scryed by [[Delwath]] on October 22th, 1748 in [[Nayahar]], [[Dunmar]] %%^End%%  
>> %%^Campaign:DuFr%% Reached by Sending cast by [[Riswynn]] on November 17th, 1748 in [[Nayahar]], [[Dunmar]] %%^End%%  
>> %%^Campaign:DuFr%% Reunited with the [[Dunmar Fellowship]] on February 1st, 1749 in the [[Copper Hills]], [[Dunmar]] %%^End%%

![[johar.jpg|left|450]]Johar is a confidant and close friend of [[Kenzo]]'s from the [[Lakan Monastery]] in [[Tokra]]. He works in the [[Tokra]] [[Archives]], primarily interested in documenting the miracles of [[Laka]], and the history of the [[Lakan Monastery]] and the community there.

%%SECRET[v2:3144b8559c38b97ea299118a33fa6626]%%

%%^Metadata:names:v1%%
- {name: Johar, language: unknown, pronunciation: JOH-hur, notes: "Proposed from the Dunmari cultural context and the Hindi analogue in Languages: j as in judge, a long o, an audible h, a reduced final vowel and a light r, with initial stress. The documented Persian alternative could instead favor jo-HAR. The name's specific language and accepted pronunciation are not established.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of Johar as Kenzo's friend and a Tokra archivist, before the diplomatic developments described in later campaign records; dated whereabouts extend into early DR 1749. The original qualification on the Copper Hills whereabouts entry beginning 1748-12-25 is preserved here: "start is approx".
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [dufr]` from the existing campaign interactions and normalized the frontmatter interaction codes to `dufr`.
- Corrected “primary interested” to “primarily interested”.
- Added a proposed pronunciation in `Metadata:names:v1`, leaving the name's language unknown and accepted frontmatter pronunciation unset.
- Added `POV: 1748` and persistent temporal guidance. Preserved the inline whereabouts qualification “start is approx”, explicitly associated with the Copper Hills entry beginning 1748-12-25, in that guidance so frontmatter can be safely formatted.

### Validated judgments
- The visible friendship and archive role fit [[Session 34 (DuFr)]]; no unsupported background or routine campaign itinerary has been added.
- The existing `dm_notes: important` attestation has confirmed local evidence. The `SECRET` block was reviewed and preserved; its contents are excluded from this report.
- `status/cleanup/metadata` is supported while the travel-start discrepancy and proposed name metadata still need human decisions; the tag is preserved.

### Editorial assessment
**Underdeveloped** — the visible account identifies a Tokra archivist and Kenzo's friend but omits his defining diplomatic commission, subsequent hostage status, and renewed role carrying messages during the peace negotiations. These dimensions are established in campaign records; a short account through early DR 1749 would fill the central gap without reproducing routine travel or conversations.

### Open findings

- [ ] **Warning — coverage.later_material_change:** The visible article stops at Johar's archive work, although [[Session 41 (DuFr)]] establishes Lara's diplomatic commission, [[Scrying Late Dec 1748]] records his hostage status, and [[Session 90 (DuFr)]] plus [[Scrying Delwath Tollen Downtime]] establish his later work between the camps and planned return with a request for a conclave. These are defining changes in his role and circumstances, beyond the dated locations already in metadata. Decide whether to update the article and POV, defer the update with the appropriate game-update status, or deliberately retain the pre-mission DR 1748 portrait and its POV. Copy-ready addition for an updated account: “In July DR 1748, Speaker [[Lara]] sent Johar to [[Nayahar]] to seek peace between [[Nayan Karnas]] and [[Sura]]. By late December, Karnas was taking him north as a hostage. By February DR 1749, Johar was carrying letters between the rival camps in the [[Copper Hills]] and helped arrange contact with [[Abha]]. In early March, he was seen traveling northeast, apparently returning to [[Tokra]] with a request for Lara to summon a conclave of Dunmar's religious leaders.” The early-March destination and mission retain the scrying record's uncertainty. If the pre-mission portrait should remain the visible frame, the smallest useful dated alternatives are a `Date:1748-07-13` passage for Lara's commission and a `Date:1749-03` passage for the retrospective diplomatic account; any such visibility change requires human adoption.
- [ ] **Warning — metadata.whereabouts_date_conflict:** The first traveling `away` entry begins on `1748-07-17`, one day after both the note's “began traveling” campaign interaction and [[Session 42 (DuFr)]] place Johar leaving Tokra with the party on July 16. Confirm replacing only that entry's start date with `{type: away, start: 1748-07-16, end: 1748-08-07, location: dufr}`; all other location boundaries remain unchanged.
- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed pronunciation `JOH-hur` in the persistent name block. [[Languages]] supplies Hindi or other Indo-Iranian (Persian) guidance for Dunmari; the preferred Hindi-informed proposal uses j as in “judge”, a long o, audible h, reduced final vowel and light r, with initial stress. A Persian-informed alternative could favor `jo-HAR`. No exact in-world phonology or accepted pronunciation is documented, and the particular name's language is left unknown. If accepted, copy `pronunciation: JOH-hur` to frontmatter and mark the entry documented; otherwise revise the proposal.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** Refresh the six generated-header campaign markers from `%%^Campaign:DuFr%%` to the canonical `%%^Campaign:dufr%%` required by [[Campaign Registry]], preserving their contents, hard line breaks and end markers. The export filter casefolds these identifiers, so this casing change has identical visibility. It remains a human refresh proposal because the current lint whitespace check rejects those changed lines with their existing two-space Markdown hard breaks preserved. During that same bounded header refresh, correct “October 22th” to “October 22nd”; the underlying date stays unchanged.

### DM evidence
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Hralgar (Session 62- )/Session 62/Session 62 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 44]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 45]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/The Elderwood (Session 50)/Character Developments/Scrying]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Lakan Monastery (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Clues]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/Events Since Chardon]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 63 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 63-65 (Stormcaller Tower)/Session 64 - DM notes]]
- [[_DM_/_Dunmari Frontier/Session 66-68 (Phasing Stone)/Session 68 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 76 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%
