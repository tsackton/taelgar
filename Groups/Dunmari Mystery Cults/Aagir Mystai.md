---
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: mystery cult
ancestry: Dunmari
name: Aagiri
affiliations:
  - {type: primary, org: Aagir}
dm_owner: tim
dm_notes: important
POV: modern
---
```taelgar-header
```

The mystery cult dedicated to the Dunmari god [[Aagir]], a traveling order of warriors who protect the roads of [[Dunmar]]. 

%%^Campaign:none%%
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
- {name: Aagiri, role: primary, language: Dunmari, pronunciation: AA-gir-ee, status: proposed, notes: "The stem AA-gir follows the accepted pronunciation in [[Aagir]]; final i is read ee using the Hindi/Indo-Iranian guidance in [[Languages]], while retaining the stem's stress and hard g. The complete form remains a proposal because no Aagiri-specific pronunciation is recorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the itinerant order's road-protection role; the visible article does not describe its earlier fortified bases.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Added a persistent name entry with a proposed pronunciation, plus modern POV and temporal coverage metadata.
- Canonicalized `Campaign:None` to `Campaign:none`; both exporters compare the sentinel without case distinctions, preserving its nonpublic visibility.

### Validated judgments
- The brief definition adequately identifies the order's deity, itinerant character, and road-protection role; the historical fortifications are an optional bounded expansion.
- The positive `dm_notes` attestation has confirmed local-source support. The shared members table remains DM navigation.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The new Aagiri name entry proposes `AA-gir-ee`, using the accepted `AA-gir` stem in [[Aagir]] and a final `i` pronounced `ee` under the Hindi/Indo-Iranian analogue documented in [[Languages]]. The hard `g` and initial stress are retained from that accepted stem, but the full derived form is not yet documented. Accept or revise the complete pronunciation; if accepted, set frontmatter `pronunciation: AA-gir-ee` and the entry's `status: documented`.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Copper Hills (OneNote)]]
- [[_DM_/_Dunmari Frontier/Session 103-110 (The Last Jade)/Session 103 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 129 - (Plaguelands)/Desolation of Cha'mutte Brainstorming]]
%%^End%%
