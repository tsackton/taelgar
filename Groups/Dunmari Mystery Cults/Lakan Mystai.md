---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: mystery cult
ancestry: Dunmari
name: Lakan Mystai
affiliations:
  - {type: primary, org: Laka}
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

The mystery cult of the Dunmari god [[Laka]]. Guardians of secret knowledge, especially concerning the lore of other planes, and the secrets of manipulating planar energy to create magic.

%%SECRET[v2:60be7cf0f5470ad1592a57a360cc44c6]%%

%%^Campaign:None%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {name: Lakan Mystai, language: unknown, pronunciation: "lah-KAHN mis-TAI", notes: "Proposed from the Dunmari cultural guidance in [[Languages]], choosing a Persian-leaning reading of this spelling with final-syllable stress. The source language and intended vowels are unestablished; y and ai are interpreted cautiously as short i and an eye-like diphthong.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern; the visible account describes the cult's enduring religious and scholarly role without a narrower dated state.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and affiliation formatting; added the explicit name `Lakan Mystai`.
- Added a persistent name entry with a proposed pronunciation and an unestablished source language.
- Added `POV: modern` and a persistent temporal-coverage explanation for the visible reference account.

### Validated judgments
- The existing `group` / `mystery cult` classification and primary affiliation with Laka fit the article.
- Confirmed local source matches support the existing positive `dm_notes` attestation; the SECRET block was separately reviewed. Private contents remain outside this report.

### Editorial assessment
**Underdeveloped** — The visible note identifies the cult and its magical interests but lacks the central institutional account already established in canonical references: its Tokra base, its custodianship of Dunmari history, and the Speaker’s historical role in selecting the Samraat. A short paragraph covering those dimensions is the smallest useful completion; a campaign chronology is unnecessary.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** [[Dunmari Mystery Cults]] establishes the cult’s role as keeper of Dunmari history and its base at the monastery near Tokra; [[Dunmari Government]] establishes the Speaker’s significant historical role in choosing the Samraat. Omitting that institutional account leaves the reference reduced to magical interests. Add: “The Lakan Mystai keep the secrets of Dunmari history and are based at the [[Lakan Monastery]] near [[Tokra]], with a presence elsewhere in Dunmar. During the Aatmaji Dynasty, their Speaker traditionally received dreams and visions from [[Laka]] guiding the choice of the Samraat; the temple conclave often confirmed the Speaker’s choice.” This keeps the succession role explicitly historical and does not infer a present selection procedure.
- [ ] **Warning — metadata.names_unresolved_status:** Review `lah-KAHN mis-TAI` in the persistent name entry. The proposal uses the Persian option in [[Languages]]’ Dunmari cultural analogue: distinct l/k/n/m/s/t consonants, short i for y, an eye-like ai diphthong, and final-syllable stress. This is an analogue-informed proposal, not an attested pronunciation or proof that the whole form is Dunmari; the Hindi alternative, intended vowels and stress remain uncertain. If accepted, copy `pronunciation: lah-KAHN mis-TAI` to frontmatter and change the entry’s status to `documented`.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The generated “Current Members” section begins with `%%^Campaign:None%%`; the documented shared-DM sentinel is `%%^Campaign:none%%`. Replace the opening marker with the lowercase form after confirming the intended publication filtering. The existing marker and table were preserved because this controls visibility.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Timelines/NPC Travels]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Uncategorized Events]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Johar (OneNote)]]
- [[_DM_/_Dunmari Frontier/Complicated OneNote NPCs/Nayan Sura]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Downtime]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Shakun's Heart (Session 26-32)/Session 32/Session 32]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Elven Ruins]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Lakan Monastery (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 41]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra Area Map/Tokra Area Map]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%
