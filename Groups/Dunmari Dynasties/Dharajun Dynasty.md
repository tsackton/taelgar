---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: family
typeOfAlias: dynasty
ancestry: Dunmari
name: Dharajun dynasty
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

%%^Campaign:none%%
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
- {name: Dharajun dynasty, role: primary, language: unknown, pronunciation: dhuh-RAH-jun DY-nuh-stee, status: proposed, notes: "The Dunmari context supports the Hindi/Indo-Iranian analogue in [[Languages]]. This proposal reads dh as a breathy voiced d, j as in judge, the medial a as ah, and unstressed vowels as uh; a Persian adaptation would lose the dh aspiration. Stress and vowel length remain tentative, and the English descriptor dynasty retains its ordinary reading."}
- {name: Dynasty of the Horse, role: alias, language: Common, status: inferred, notes: "This descriptive title is recorded in [[Dunmari Government]]; its displayed form is ordinary English."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern identification of a historical Dunmari dynasty; the visible article does not yet describe its chronology or rule.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added primary and alternate name metadata, a proposed pronunciation, and modern POV with a temporal-coverage note.
- Canonicalized `Campaign:None` to `Campaign:none` without changing its nonpublic visibility.

### Validated judgments
- The positive `dm_notes` attestation has confirmed local-source support; it is unchanged.
- The historical-members table is shared DM navigation and does not provide a visible account of the dynasty.

### Editorial assessment
**Underdeveloped**: The visible note gives only a classification. Its central missing dimensions are Jita's foundation, the Chidyan horse succession principle, the Tokra court and associated prosperity, and its fall in the Great War. A short sourced overview would supply the minimum useful reference account; these gaps are established elsewhere rather than invitations to invent a complete royal chronology.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** [[Dunmar#Dharajun Dynasty]], [[Jita]], and [[Dunmari Government#Temple Conclave]] establish the dynasty's defining history and succession principle, none of which appears outside the classification callout. Copy-ready core: “The Dharajun dynasty, also called the Dynasty of the Horse, was founded by [[Jita]] after the fall of the [[Aatmaji Dynasty]]. A horse blessed with the spirit of [[Chidya]] guided the temple conclave's choice of Samraat. Jita established her court in [[Tokra]], and the dynasty presided over a period of Dunmari prosperity before falling in the [[Great War]].” Before adding precise accession dates, reconcile [[Jita]]'s leadership metadata beginning in DR 1402 with [[Dunmar]]'s DR 1403 dynastic foundation; the proposed core preserves that uncertainty by remaining date-free.

- [ ] **Warning — metadata.names_unresolved_status:** The proposed complete reading is `dhuh-RAH-jun DY-nuh-stee`. It follows the Dunmari Hindi/Indo-Iranian analogue in [[Languages]]: breathy voiced `dh`, `j` as in “judge,” medial `a` as `ah`, and unstressed vowels as `uh`; stress and vowel lengths are tentative. A Persian adaptation would lose the `dh` aspiration. Accept or revise the pronunciation; if accepted, set frontmatter `pronunciation: dhuh-RAH-jun DY-nuh-stee` and mark the primary name entry `status: documented`.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Into the Desert (Session 19-25)/Kharsan/Kharsan History]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Copper Hills (OneNote)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Lakan Monastery/Notes from Kassi]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Archive Mysteries]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Tokra/Tokra (OneNote)]]
- [[_DM_/_Dunmari Frontier/Session 83-97 (Ursk)/Session 84 - Dunmar Notes]]
%%^End%%
