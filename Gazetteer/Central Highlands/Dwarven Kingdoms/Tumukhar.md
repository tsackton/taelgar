---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
ancestry: dwarven
campaignInfo:
  - {campaign: GL, type: explored, date: 1747-12-13}
name: Tumukhar
whereabouts: "Am'khazar"
dm_owner: none
dm_notes: none
POV: 1748
---
```taelgar-header
```

Tumukhar was a southern hold of [[Am'khazar]], lying down‑valley from [[Zarkandur]], and serving as a high mountain entrance to the underground routes and roads in [[Am'khazar]]. Before its abandonment, Tumukhar served as a way‑city for travelers and traders bound toward the Stoneborn villages and other destinations in the [[Sentinel Range|Sentinels]], with stout gateworks, tiered streets, and well‑kept cisterns fed by mountain rills. Its craftsmen were known for practical ironwork and serviceable tools destined for the frontier, and for the quiet hospitality expected of a road city: a warm seat by the brazier, a pot on the hearth, and news from the passes.

During the Long Winter, cold unlike any living dwarf recalled swept down from the heights. Tumukhar’s fountains glazed over; ice traced the carvings on lintels and doors; and frost‑spirits slipped through shuttered alleys. With the lower wards glazed and patrols reporting mephits and worse in the streets, the elders ordered an orderly withdrawal toward Zarkandur and the deeper halls of Am’khazar. By the time the exodus was complete, the outer gates stood silent beneath wind‑packed snow and the city lay in uneasy stillness.

Since the thaw’s beginning, plans for Tumukhar’s renewal have begun to be developed. As of DR 1748 settlers have not returned to the city, but initial plans for reopening wayhouses and the gate, and staffing a garrison, are underway. 

%%
GL Arc 3 notes (campaign):

- The city was encountered frozen and abandoned (DR 1747‑12‑13), with ice mephits, snow golems, and an ice troll reported within the wards. The party traversed Tumukhar en route to Stoneborn villages and the source of the freezing in the high peaks, and narrowly avoided an avalanche trap at the mountain exit.
- Session references: GL Arc 3 notes for 1747‑12‑13 and follow‑on sessions; background indicates a glacier around the frost‑giant stronghold of [[Vangebekkr]] as the proximate source of the unnatural cold.
%%

%%^Metadata:names:v1%%
- {name: Tumukhar, language: unknown, pronunciation: TOO-moo-khar, status: proposed, notes: "Tentative dwarf-context proposal using the Tolkien Dwarvish analogue in Languages: both u vowels as oo, kh as the throaty ch in loch, final ar as in far, and tentative initial stress. The exact name language and in-world stress rule are not established."}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 snapshot after the cursed cold, when the article describes Tumukhar as still uninhabited and renewal only planned, with earlier history of the hold and its abandonment.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving parsed values, existing campaign identifiers, and headerVersion.
- Corrected the objective typo “severing as” to “serving as”.
- Added a tentative name pronunciation, a typed settlement map skeleton, and a DR 1748 viewpoint with temporal coverage notes.

### Validated judgments
- [[Great Library Session Notes - Arc 3]] supports the frozen, abandoned city in December DR 1747 and the subsequent defeat of the cursed cold. The source comment remains useful campaign provenance; incidental encounters need no further reference-note expansion.
- The recorded DR 1748 renewal plans anchor the article’s current state. The available sources do not establish later resettlement, and no later continuity is inferred.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `TOO-moo-khar` in the persistent name entry. The dwarf context and [[Languages]]’ Tolkien Dwarvish analogue inform full oo vowels and kh as the throaty ch in loch, with final ar as in far. Initial stress is a tentative practical choice, and the exact name language remains unknown. Accept or correct the proposal; if accepted, copy the accepted form to frontmatter and mark the entry `documented`.

- [ ] **Warning — metadata.map_location_missing:** The new settlement map entry has a blank `locator`. Supply Tumukhar’s verified world-map position in `Metadata:map:v1`; no coordinate was established by the reviewed evidence.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The header marker uses `%%^Campaign:GL%%`; [[Campaign Registry]] resolves that alias to `grli`. After confirming equivalent filtered visibility, replace only the opening marker with `%%^Campaign:grli%%` and use `campaign: grli` in the existing campaignInfo entry. Preserve the exploration date, text, and closing marker.

- [ ] **Suggestion — editorial.reference_voice:** In the first paragraph, the passage beginning “and for the quiet hospitality expected of a road city” and ending “news from the passes” expands the city’s account into a generic road-city hospitality vignette. Have a human rewrite or remove this bounded passage. Preserve the distinct stated facts about the hold’s route and trade role, practical ironwork, and tools; this finding does not authorize an automatic rewrite or declare those facts false.
%%^End%%
