---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Wellby, date: 1748-09-30, type: met}
  - {campaign: dufr, person: Wellby, date: 1748-10-12, type: last seen}
born: 1639
gender: female
name: Wella Brightmoon
aliases: [Wella]
affiliations:
  - {org: Brightmoons, type: primary}
  - {place: Wave Dancer, title: Captain, type: leader, start: 1}
whereabouts: Wave Dancer
knownTo: [dufr]
dm_owner: none
dm_notes: none
POV: 1748
---
# Wella Brightmoon
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (she/her), of the [[Brightmoons]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met with [[Wellby]] on September 30th, 1748 in the [[Wave Dancer]], sailing to [[Wahacha]], the [[Vermillion Isles]] %%^End%%
>> %%^Campaign:dufr%% Last seen with [[Wellby]] on October 12th, 1748 in the [[Wave Dancer]], moored in the [[Wahacha|main port of Wacahca]], the [[Vermillion Isles]] %%^End%%

Wella is an elderly halfling woman with curly white hair, and the captain of the [[Wave Dancer]]. She is married to [[Rose Brightmoon]], and is the matriarch of the Brightmoon clan. 
%%^Date:1748%%
Although now getting old and stiff and sometimes slow on her feet, she has been sailing all her life, and her weather sense is deeply respected by the crew of the [[Wave Dancer]]. 
%%^End%%
## Relationships
- [[Rose Brightmoon]], wife
- [[Pearl Brightmoon]], cousin
- [[Corrin Wildheart]], cousin-in-law

%%^Metadata:names:v1%%
- {name: "Wella Brightmoon", language: "unknown", pronunciation: "WEH-lah BRYTE-moon", notes: "Adapted using the provisional Igbo analogue for Halfling in Languages: pronounced w and l, unglided e and a, two syllables. Initial emphasis is a reading aid, not an invented tone pattern; the English compound surname is retained. Halfling naming may be diverse and the individual name language remains unknown.", status: "proposed"}
- {name: Wella, role: alias, language: unknown, pronunciation: WEH-lah, notes: Same provisional given-name reading as the primary entry., status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 portrait of the elderly captain and clan matriarch, with the dated sailing experience passage supplementing that same life stage.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added persistent name and temporal-viewpoint metadata; unestablished name languages remain `unknown`.
- Added the campaign knowledge code supported by existing interactions or finalized session evidence.

### Validated judgments
- The captaincy, marriage and family links are corroborated by the Wave Dancer and family notes. The matched local DM cluster adds no useful material beyond the public/shared record, so `dm_notes: none` is retained without a recovery handoff.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed pronunciation `WEH-lah BRYTE-moon` in `Metadata:names:v1`. Review the matching Wella alias entry together with the primary form. The provisional Igbo analogue in [[Languages]] motivates unglided e/a and sounded w/l in the two-syllable given name; initial emphasis is only a reading aid, not an invented tone pattern. The English compound surname is retained, consistent with the guidance that halfling naming may be diverse. These are analogue-informed proposals, not documented in-world phonology. On acceptance, set the entry to `status: documented` and copy the accepted primary pronunciation to frontmatter; no frontmatter pronunciation has been asserted.
%%^End%%
