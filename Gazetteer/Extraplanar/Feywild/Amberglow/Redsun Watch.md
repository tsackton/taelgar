---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: building
typeOfAlias: keep
ancestry: fey
name: Redsun Watch
whereabouts: Amberglow
dm_owner: tim
dm_notes: important
POV: modern
---
# Redsun Watch
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Redsun Watch is one of several outposts established by the [[Cloudspinner]] on the eastern edge of [[Amberglow]], near the [[Sunset Gate]]. Since her disappearance, the fate of Redsun Watch and other border outposts is unknown.

%%^Campaign:DuFr%%
According to [[Lirien|Lirien]], who was the Lanternkeeper of Redsun Watch, some time after the [[Cloudspinner]]'s disappearance "rivers of shadow" invaded across the [[Sunset Gate]], from [[Hollowdark]] and [[Darkfall]], and Redsun Keep was destroyed.
%%^End%%

%%SECRET[v2:23366c3f52dc1d5737e66eea6b4fe0a3]%%

%%^Metadata:names:v1%%
- {name: Redsun Watch, language: Common, status: inferred, notes: descriptive Common name}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern after Cloudspinner's disappearance; the campaign account preserves Lirien's report of the fall and has not incorporated the direct observations made in DR 1749.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting without changing existing values.
- Added explicit subject-name metadata, a primary name entry, and the article POV with its temporal interpretation.

### Validated judgments
- The name is a transparent English compound and needs no pronunciation; the descriptive Common form is inferred from the place-name guidance in [[Languages]].
- Confirmed local sources support the existing positive `dm_notes` attestation; the field is unchanged.
- The local-only SECRET block was reviewed and preserved; its contents are not repeated in this report.

### Editorial assessment
**Underdeveloped**: the article omits the keep's defining Amberlight defense and surviving Prismwell beacon, and its campaign account ends with an uncertain report of destruction despite direct DR 1749 observations of the occupied ruins. A short functional description and a dated update within the existing campaign section would fill these established central gaps; no new history or post-restoration fate needs to be invented.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The opening identifies an outpost but omits its defining means of guarding the border. [[Lirien]] and her account in [[Session 118 (DuFr)]] establish that she used an [[Amberlight]] to seal cracks in the [[Sunset Gate]]. Add within the existing Dunmar campaign section: “Its Lanternkeeper, [[Lirien]], used an [[Amberlight]] to seal cracks in the [[Sunset Gate]] and hold back the encroaching darkness.” This states the stable function without adding the party's conversation or private leadership history.

- [ ] **Warning — coverage.later_material_change:** The campaign paragraph ends with Lirien's report that the keep was destroyed. [[Session 121 (DuFr)]], [[Session 122 (DuFr)]], and [[Session 123 (DuFr)]] establish surviving ruined towers occupied by minions of [[Harrow]] and [[Wend]], and a beacon beneath the keep that was reignited and revealed the [[Prismwell]]. This is a material state and function, beyond an incidental visit. Choose to update the campaign account and temporal framing, defer the update with the appropriate game-update status by human action, or intentionally preserve the earlier report as history. Smallest update candidate inside the existing campaign section: “By DR 1749, the ruined keep was engulfed in darkness flowing from [[Hollowdark]] through a breach in the [[Sunset Gate]], and occupied by minions of [[Harrow]] and [[Wend]]. On DR 1749-06-13, the [[Dunmar Fellowship]] reignited a beacon beneath the keep whose light revealed the [[Prismwell]].” If adopting that update, propose `%%^Date:1749-06-13%%` before these sentences and `%%^End%%` after them. Keep Lirien's account attributed, retain the campaign restriction, and do not infer the keep's fate after Cloudspinner's restoration. The new date block and any game-update status require a human decision.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing opener uses `DuFr`; [[Campaign Registry]] requires lowercase `dufr`. Replace only `%%^Campaign:DuFr%%` with `%%^Campaign:dufr%%`, preserving the same campaign restriction and contents. The existing block was left intact for review.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Redsun Watch - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 118 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 119 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 120 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 121 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 122 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 123 - DM Notes]]
%%^End%%
