---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: city
ancestry: Dunmari
created: 1557
mapLocation: { x: 4757, y: 7710, hex: 17.08.D.22/1410, importance: local, symbol: square }
name: Nayahar
whereabouts: Western Dunmar
dm_owner: tim
dm_notes: none
POV: 1740s
---
# Nayahar
>[!info]+ Information
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A Dunmari city located close to the head of navigation of the [[Nayan]] river. The administrative center of the [[Nayan Dynasty]], home of the Samraat court. 

%%  notes
history:
Founded in DR 1557. Originally the site of a monument constructed to the holy family in honor of surviving the great war and in thanks for the fertile lands of the Nayan floodplains. Later an administrative city grew up around the monument, and then eventually a thriving metropolis.
vibe:
not sure, but definitely a big religious/ceremonial aspect and big royal administration. monumental architecture dating from ~1580s might be common, for example
%%

%%^Metadata:names:v1%%
- {"name": "Nayahar", "language": "unknown", "pronunciation": "nuh-YAH-hur", "notes": "Proposed from the Dunmari cultural context and the Hindi option in the Hindi or other Indo-Iranian (Persian) guidance in [[Languages]]: consonantal y, audible h, reduced initial and final a vowels, an open middle ah vowel, and middle-syllable emphasis as a reading aid. A Persian-informed reading could keep fuller a vowels or different stress; the name's specific language, vowel lengths, and in-world stress are unconfirmed.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a pre-partition DR 1740s description of Nayahar as the Nayan administrative center and home of the Samraat court; the account does not describe the DR 1749 division of Dunmar.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and list formatting.
- Added a typed settlement map skeleton with its unknown locator left blank.
- Added a proposed primary name pronunciation and recorded the pre-partition DR 1740s viewpoint in `POV` and `povNotes`.

### Validated judgments
- The authored city description is eligible; there are no non-check status tags to assess. The human `dm_notes: none` attestation is preserved.
- Reviewed the hidden history and provisional atmosphere notes separately. Local private material is excluded from this report; any recoveries remain in the private handoff.

### Editorial assessment
**Underdeveloped**. This major administrative city has only a location and court-role identification in visible prose. Its founding around a religious monument and subsequent civic growth remain in a hidden draft, while the visible political role does not distinguish the realms established by the DR 1749 settlement. The smallest useful scope is one reviewed founding/ceremonial paragraph and a bounded decision about the later political frame. No separate uninvented central dimension is asserted.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — metadata.map_location_missing:** The required settlement map entry has no locator. Supply Nayahar's verified world-map hex in `- {map: world, locator: VERIFIED_HEX}`; no exact locator is established by the reviewed prose sources, and no coordinate was guessed.
- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise `nuh-YAH-hur` in the primary name entry. [[Languages]] gives Dunmari the analogue “Hindi or other Indo-Iranian (Persian)”. The preferred Hindi-informed proposal uses consonantal y, pronounced h, reduced initial and final a vowels, an open middle ah vowel, and middle-syllable emphasis as a reading aid. A Persian-informed reading could use fuller vowels or different stress; exact in-world phonology and this name's specific language remain unconfirmed. If accepted, copy `pronunciation: nuh-YAH-hur` to frontmatter and mark the entry `documented`.
- [ ] **Suggestion — editorial.public_material_candidate:** The `history:` paragraph in the ordinary `notes` comment is a coherent founding and growth account, distinct from the explicitly uncertain `vibe:` ideas. It would give this administrative city a defining ceremonial origin. Candidate for human adoption: “Founded in DR 1557, Nayahar grew around a monument to the holy family, built in thanks for surviving the [[Great War]] and for the fertile lands of the [[Nayan Floodplains]]. An administrative city developed around the monument and eventually grew into a metropolis.” This proposal comes from the Git-shared comment, rather than treating its account as adopted canon. If adopted, remove that historical paragraph from the comment and retain the uncertain architectural ideas as clearly labelled planning; do not turn the suggested 1580s architecture into established history.
- [ ] **Warning — coverage.later_material_change:** “The administrative center of the Nayan Dynasty, home of the Samraat court” leaves the city's political scope unclear after Dunmar's partition. [[Chardon-Dunmar War#Settlement and Ramifications]] and [[Session 129 (DuFr)]] establish the treaty of DR 1749-07-25, after which Karnas retained a southern realm around the Nayan Floodplains while Sura held the north and center. Copy-ready later context: “The peace settlement of July 25th, DR 1749 divided [[Dunmar]] between [[Sura]] and [[Nayan Karnas]]; Karnas retained the southern realm around the [[Nayan Floodplains]].” Decide whether to update the political account and POV, defer the update with an appropriate human-assigned game-update tag, or intentionally preserve the pre-partition account. If adding the later context while retaining the earlier article frame, the smallest useful dated layer is `%%^Date:1749-07-25%%` around that sentence followed by `%%^End%%`; apply this visibility change only after human approval. Do not infer additional treaty boundaries, a new capital, or a relocation of the court.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Northern Plains (Sessions 6-16)/Travel to Raven's Hold/Distances and Travel Time]]
%%^End%%
