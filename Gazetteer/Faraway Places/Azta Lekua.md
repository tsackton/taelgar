---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: region
name: Azta Lekua
aliases: [Footprint of the Gods]
whereabouts: Orekatu
dm_owner: tim
dm_notes: important
POV: modern
---
# Azta Lekua
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%copy notes from OneNote%%

A place in the lizardfolk jungles, just west of the border of [[Orekatu]], where the power of the outer planes is particularly strong and present. Also known as the Footprint of the Gods.

Protected by a spirit creature, [[Lengau]].

%%^Metadata:names:v1%%
- {name: Azta Lekua, language: unknown, pronunciation: "AHS-tah leh-KOO-ah", status: proposed, notes: "Basque-informed proposal from the Lizardfolk naming context and the Lizardling analogue in [[Languages]]: z as an unvoiced s, a as ah, e as eh, u as oo, and separate u/a vowels. Initial stress in Azta and penultimate stress in Lekua are tentative; the source language and exact in-world phonology are unrecorded."}
- {name: Footprint of the Gods, role: alias, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the jungle's enduring planar connections and guardian; the disruption and restoration recorded in DR 1747–1748 are not yet summarized in this article.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added primary and alias name entries, a proposed primary pronunciation, and broadly modern temporal metadata.
- Corrected the subject–verb agreement in “the power of the outer planes is particularly strong.”

### Validated judgments
- The alias Footprint of the Gods is a plain-English title and needs no separate pronunciation guide.
- Confirmed matching local-DM source clusters support the existing positive dm_notes attestation; its value is preserved.

### Editorial assessment
**Underdeveloped**: The note identifies the jungle's planar character and guardian but omits the disruption of that balance by Motua and the established beginning of restoration. Those are lasting changes to the subject, rather than incidental visits. A short, dated crisis-and-restoration paragraph closes the central missing account; the evidence does not establish that restoration was already complete.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.names_unresolved_status:** Review `AHS-tah leh-KOO-ah` in Metadata:names:v1. The Lizardfolk naming context and the Basque analogue for Lizardling in [[Languages]] inform unvoiced s for z, ah/eh/oo vowels, and separate u/a vowels in Lekua. Initial stress in Azta and penultimate stress in Lekua are provisional; the source language and exact in-world phonology are not established. Accept or revise the proposal; on acceptance, add the full pronunciation to frontmatter and mark the entry documented.

- [ ] **Warning — coverage.established_fact_missing:** [[Session 57 (DuFr)]], [[Session 59 (DuFr)]], [[Session 64 (DuFr)]], and [[Motua]] establish a durable crisis and the beginning of recovery, neither of which appears here. Candidate: “In DR 1747, the wounded [[Motua]] arrived in Azta Lekua and began draining its spiritual energy, upsetting the balance of the jungle and allowing elemental forces to intrude. After Motua was healed on November 6, DR 1748, [[Lengau]] returned and undertook to restore the jungle with Motua's help. [[Izzarak]] remained to care for Lengau's children and aid the recovery.” Review the campaign audience and any appropriate dated or campaign block before adoption; no new visibility block was added. This records the lasting disruption and restoration effort without recapping the expedition or asserting that recovery was complete.

- [ ] **Warning — correctness.internal_conflict:** The prose places Azta Lekua “just west of the border of [[Orekatu]],” while `whereabouts: Orekatu` records that realm as its physical container. The campaign-scoped catalog in [[Extraplanar Weak Point]] also calls it a place in Orekatu. Confirm the intended boundary relationship before changing either. If it is outside the realm, a bounded metadata candidate is `whereabouts: Far South`, retaining the existing “just west” sentence. If it is inside the realm, a bounded prose candidate is “A place in the lizardfolk jungles of western [[Orekatu]], where the power of the outer planes is particularly strong and present.” Neither geographic interpretation was selected automatically.

### DM evidence
- [[_DM_/_Dunmari Frontier/Campaign Outline - Arcs and Levels]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Azta Lekua (DM Notes)]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Kenzo Solo Arc]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Session 1 - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Kenzo Solo Arc/Session 2 - Kenzo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Kenzo (OneNote)]]
%%^End%%
