---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: extraplanar domain
ancestry: fey
name: Amberglow
whereabouts: Feywild
excludePublish: [clee]
dm_owner: joint
dm_notes: none
POV: modern
---
# Amberglow
>[!info]+ Information
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Amberglow is a fey realm, located by many sources, including [[The Lore of the Feywild]], on the southern and eastern borders of [[Shimmersong]]. This realm features frequently in the tales and legends of [[Drankorian Empire|Drankor]] as a place of great beauty, a land of constant sunsets and golden skies on wide open plains of amber grasses and lush flowers. However, more recent sources suggest that it has fallen into decay. Many fey ballads sing the tragedy of the [[Cloudspinner]], the Queen of Sunsets, who vanished long ago, and the slow destruction of her once-marvelous realm that followed. 

![[amberglow-plains.png]]

%%^Campaign:dufr%%
There are, however, some pockets of the [[Cloudspinner]]'s court that remain. [[Lady Eventide]] hides in the crumbled remains of the [[Cloud Palace]]. [[Caulaus]], a trapped Drankorian soldier who once wronged the [[Cloudspinner]] but has forgotten his mistakes, now guards the [[Heartwood Grove]] where [[Agata|Agata Dustmother]] remains imprisoned. Rumors of other holdouts and defenders exist as well, although what truth there is to these tales is not clear. Nonetheless, the land remains a bleak place, where the vibrant colors of sunset are bleached and desaturated, and those that linger struggle against malicious fey.
%%^End%%

%%SECRET[v2:f9d0ceab5e525f0fd7e5dbdf9d2a79dd]%%

%%^Metadata:names:v1%%
- {name: Amberglow, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern during Amberglow's long decline, before Cloudspinner's restoration on DR 1749-06-13; the campaign passage describes the surviving court and Agata's imprisonment after the DR 1748 visit.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting while preserving existing values and headerVersion.
- Added the explicit name and a minimal primary-name block; Amberglow is a transparent English compound and needs no pronunciation guide, while its in-world name language remains unknown.
- Added a modern POV and temporal coverage note for the long decline and the campaign passage's DR 1748 state.
- Corrected “Drankorian solider” to “Drankorian soldier”.

### Validated judgments
- The descriptions of the ruined Cloud Palace, Lady Eventide, and Caulaus guarding Agata's prison are supported by [[Session 65 (DuFr)]] and [[Session 67 (DuFr)]].
- The attribution to [[The Lore of the Feywild]] remains an account of in-world sources; the treatise's report of Cloudspinner's death is not adopted as omniscient fact.
- Reviewed the local-only SECRET block and the complete local evidence dossier; private recovery proposals remain outside this report, and the human dm_notes attestation is unchanged.

### Editorial assessment
**Underdeveloped**: the realm's central account omits the established northern conquest and eastern invasion during its decline, and Cloudspinner's restoration in DR 1749. The smallest useful scope is a short account of those pressures and a bounded restoration update, or an explicit decision to preserve the earlier snapshot. The sources do not establish the extent or speed of the realm's subsequent recovery.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The campaign paragraph reduces the threats to unspecified “malicious fey,” but [[Session 118 (DuFr)]], [[Session 120 (DuFr)]], and [[Session 121 (DuFr)]] establish a durable change in the realm: northern territories and refuges had been taken by [[Lord Umbraeth]], while darkness from the eastern realms breached the [[Sunset Gate]] and engulfed [[Redsun Watch]]. [[Session 122 (DuFr)]] directly records that darkness extending into Amberglow. Add a brief subject-focused account within the existing Dunmar campaign section, preserving its audience restriction: “During [[Cloudspinner]]'s absence, [[Lord Umbraeth]] expanded [[Duskmire]] into Amberglow's northern lands and refuges. Along the eastern border, darkness from [[Hollowdark]] and [[Darkfall]] broke through the [[Sunset Gate]], overwhelming [[Redsun Watch]] and spreading into the realm.” Keep this explicitly part of the decline; the sources do not establish that all these conquests or breaches ended when Cloudspinner returned.

- [ ] **Warning — coverage.later_material_change:** The article leaves Cloudspinner vanished and the land in uninterrupted decline, but [[Session 123 (DuFr)]] records her release at the [[Prismwell]] on DR 1749-06-13, her defeat of the shadows threatening the sanctuary, and her renewed presence in Amberglow. This changes the realm's defining ruler and prospects even if the older account is intentionally retained. Choose to update the article and temporal metadata, defer with the appropriate human-managed game-update tag, or explicitly preserve the earlier snapshot. For an update, add within the existing Dunmar campaign section: “On DR 1749-06-13, the [[Dunmar Fellowship]] freed [[Cloudspinner]] at the [[Prismwell]]. She drove back the shadows threatening the sanctuary and returned to rule in Amberglow. [[Valeris]] remained to help restore the damaged realm.” If filtered chronology is desired, propose a `Date:1749-06-13` block around this addition, with a corresponding `Date:1749-06-13b` block around any earlier state that should cease to display. New date blocks and status changes need human disposition; do not infer complete restoration, a repaired Cloud Palace, Agata's fate, or Caulaus's later whereabouts.

### DM evidence
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Amberglow - Combat Ideas]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Redsun Watch - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 118 - DM Notes]]
- [[_DM_/_Dunmari Frontier/Session 118-123 (Cloudspinner)/Session 123 - DM Notes]]
%%^End%%
