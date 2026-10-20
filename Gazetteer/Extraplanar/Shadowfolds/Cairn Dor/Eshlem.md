---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/gameupdate/gl, status/check/lint]
typeOf: settlement
typeOfAlias: village
ancestry: "Yo'nari"
name: Eshlem
whereabouts: Cairn Dor
dm_owner: none
dm_notes: none
POV: 1748
---
# Eshlem
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Eshlem is the largest settlement in [[Cairn Dor]] and the home of most of the realm's native population. It is an agricultural village surrounded by old woods, scattered homesteads, and smaller communities. Wolf plinths define its outskirts, reflecting the authority of [[Yeshara]], the Wolf-Queen.

The people of Eshlem, known as the Nurim-Dor, are descended from the [[Yo'nari]] who entered Cairn Dor with Yeshara. Their society is shaped by a pervasive fear of sleep and dreams. Residents regard ordinary sleep as a spiritual contamination that can steal or corrupt the soul, while the sleepless [[Shemra Azem]] are honored as guardians who protect the community from that danger.

Nightly customs are intended to delay sleep rather than welcome it. Bonfires, drinking, dancing, chanting, and communal celebrations keep villagers awake, and many inhabitants accept chronic exhaustion as an ordinary condition of life.

%%^Metadata:names:v1%%
- {"name": "Eshlem", "language": "unknown", "pronunciation": "ESH-lem", "notes": "Proposed using the Northros/Semitic naming context recorded in [[Yo'nari]] and [[Languages]], with Hebrew/Arabic comparators for Deno'qai: sh is read as sh and e as short eh; the initial stress is tentative. Eshlem's exact historical language and in-world phonology are not established.", "status": "proposed"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: the waking village and its customs before Yeshara's defeat in October DR 1748; the inhabitants' subsequent sleep and continued slumber in DR 1752 are not incorporated.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name metadata with a proposed pronunciation for human review.
- Added the required typed map skeleton, leaving its unsupported locator blank.
- Recorded a DR 1748 viewpoint for the waking village before Yeshara's defeat.

### Validated judgments
- [[Great Library Session Notes - Arc 5#Session 63]] corroborates the village's fear of sleep and its communal efforts to stay awake; the cultural account is retained.
- The name's language is left unknown rather than equating ancient Yo'nari usage with a modern descendant language.
- `status/gameupdate/gl` is not assessable until the human chooses whether to update, defer, or preserve the earlier article; the tag is unchanged.
- The local-only DM dossier has no matches; shared DM preparation is a separate source category and does not change `dm_notes: none`.

### Editorial assessment
**Underdeveloped** — The article omits Eshlem's central later population state: sleep following Yeshara's DR 1748 defeat and continued slumber in DR 1752. A short dated outcome and a decision about retaining the earlier cultural portrait are the smallest useful changes.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Great Library Session Notes - Arc 5#Session 63]] records that the inhabitants of [[Cairn Dor]] fell asleep when [[Yeshara]] fell on October 14, DR 1748, and remained asleep when the visitors awoke on June 28, DR 1752. [[Cairn Dor]] identifies Eshlem as the home of most of those natives and confirms that their later fate is unknown. The present-tense village customs omit this durable change. Choose to update the article and POV, defer with the existing game-update tag, or intentionally retain the pre-defeat account and disposition that tag. A copy-ready addition, if updating, is: “When [[Yeshara]] fell in October DR 1748, the native inhabitants of [[Cairn Dor]], including the people of Eshlem, fell asleep. They remained asleep when the realm emerged from stasis in June DR 1752; their later fate is unknown.” If retaining both layers, propose `Date:1748-10-14` around the first sentence and `Date:1752-06-28` around the second, each with its matching End marker, after deciding visibility. No date block or game-update status was changed automatically.

- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes `ESH-lem`. [[Yo'nari]] places this culture among early Northros speakers, while [[Languages]] gives Northros a general Semitic analogue and Deno'qai Hebrew or Arabic analogues. The proposal reads `sh` as sh and `e` as short eh; initial stress is tentative, and no exact historical language or phonology is established. Accept it by recording `pronunciation: ESH-lem` in frontmatter and marking the entry documented, or supply a correction; the name itself is unchanged.

- [ ] **Warning — metadata.map_location_missing:** The required settlement map entry has an empty `locator`; no supported position for this extraplanar village is established in the consulted sources. Supply the appropriate map and a supported locator in `Metadata:map:v1`. Do not invent a Material Plane hex from the location of a portal into Cairn Dor.
%%^End%%
