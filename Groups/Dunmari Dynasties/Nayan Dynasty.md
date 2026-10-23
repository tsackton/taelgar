---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: family
subTypeOf: dynasty
name: Nayan dynasty
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```
The Dunmari dynasty founded in the aftermath of the Great War. 

%%^Campaign:None%%
### Historical Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Nayan dynasty, language: Dunmari, pronunciation: "NYE-ann DYE-nuh-stee", notes: "Proposed complete form using the accepted Nayan pronunciation in [[Marathu]] (NYE-ann muh-RAH-too), followed by the ordinary English word dynasty. The full dynastic title remains for human confirmation.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern retrospective identification of the dynasty founded after the Great War; the article does not yet describe its subsequent rule or political divisions.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order without changing existing values.
- Added persistent name metadata with a source-based proposal for the complete pronunciation.
- Added `POV: modern` and a temporal note describing the limited retrospective account.

### Validated judgments
- The positive `dm_notes` attestation is supported by confirmed local source matches; private content has not been added to this report.
- The historical-members query was preserved, including its noncanonical private-block opener, for the syntax decision below.

### Editorial assessment
**Underdeveloped**. The public article identifies only the dynasty's founding era. It lacks its established western administrative center and character of rule, and the later division between its rival rulers. A short overview and a dated settlement sentence would supply these central dimensions without requiring a complete genealogy or reign-by-reign history.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The sole visible sentence omits the dynasty's defining political context. [[Dunmar#Nayan Dynasty]] dates its foundation to DR 1557 and locates its administrative center at Nayahar; [[Dunmari Government#Temple Conclave]] explains its semi-hereditary succession. Candidate: “Founded in DR 1557 after the [[Great War]], the Nayan dynasty established its administrative center at [[Nayahar]] and gradually reclaimed Dunmari territory eastward toward the [[Karawa Desert]]. Under its Samraats, appointment of heirs made the monarchy semi-hereditary, although the temple conclave retained the formal role of choosing the ruler.” These public sources establish the missing context independently of private notes.
- [ ] **Warning — coverage.later_material_change:** [[Session 129 (DuFr)]] records the lasting settlement on July 25th, DR 1749, a central consequence absent from this dynasty account. Candidate: “On July 25th, DR 1749, a peace settlement divided [[Dunmar]] between [[Sura]] and [[Nayan Karnas]], while [[Darba]] became a free port.” Choose whether to incorporate this development, defer it with an appropriate human-assigned game-update tag, or explicitly preserve an earlier historical focus. If incorporating it into the broad retrospective article, the smallest visibility proposal is to wrap just this sentence in `%%^Date:1749-07-25%%` and `%%^End%%`; no date block was applied automatically. The source does not establish that the dynasty ended.
- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed complete pronunciation `NYE-ann DYE-nuh-stee`. [[Marathu]] explicitly records `NYE-ann muh-RAH-too`, providing a stronger basis for the shared dynastic component than an analogue-only reading. The proposal retains that component and uses ordinary English for “dynasty”; the complete form remains unconfirmed. If accepted, add `pronunciation: NYE-ann DYE-nuh-stee` to frontmatter and mark the name entry `documented`.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The historical-members query begins with `%%^Campaign:None%%`. The canonical shared-DM opener is `%%^Campaign:none%%`. Replace only that opener while retaining the query and its closing marker; this visibility-related syntax proposal has not been applied automatically.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 17]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Clues]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Calendar Eras - DuFr Player Background]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Dates - Dunmar Campaign Player Background]]
- [[_DM_/_Dunmari Frontier/Pre-Session-63/DM Version - Bhishma Monastery]]
- [[_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Session 78 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Brainstorming]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%
