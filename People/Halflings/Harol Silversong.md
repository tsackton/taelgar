---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, date: 1748-08-09, type: met}
  - {campaign: dufr, date: 1748-08-21, type: last seen}
born: null
gender: male
name: Harol Silversong
affiliations:
  - {org: Silversongs, type: primary}
  - {org: Emerald Song, title: Captain, start: 1, type: leader}
whereabouts:
  - {location: Emerald Song, type: home, prefix: sailing}
knownTo: [dufr]
dm_owner: none
dm_notes: color
POV: 1740s
---
# Harol Silversong
>[!info]+ Biographical Info
> A [[Halflings|halfling]] (he/him)
> `$=dv.view("_scripts/view/get_Affiliations")`
>> `$=dv.view("_scripts/view/get_Whereabouts")`
>> %%^Campaign:dufr%% Met by [[Dunmar Fellowship]] on August 9th, 1748 in the [[Emerald Song]], [[Darba]], [[Dunmar]] %%^End%%
>> %%^Campaign:dufr%% Last seen by [[Dunmar Fellowship]] on August 21st, 1748 in the [[Emerald Song]], [[Chardon]], the [[Chardonian Empire]] %%^End%%

Captain of the [[Emerald Song]]. He is tough and wiry, tall for a halfling, with olive-brown skin and curly white hair, with bright silver eyes. Although not very talkative for a halfling, he has a good singing voice and often takes up the bass viol in the evenings.
## Relationships
- [[Ewen Silversong]], his uncle
- [[Dani Silversong]], his niece

%%^Campaign:none%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", choice(contains(file.tags,"person"),"Person", "Thing")) as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization OR #item
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%

%%^Metadata:names:v1%%
- {name: "Harol Silversong", language: "unknown", pronunciation: "HAH-rohl SIL-ver-song", notes: "Proposed using the provisional Halfling analogue in Languages as guidance: full a and o vowels and sounded h, r, and l, retaining the written final consonant as a name adaptation; initial stress is tentative, no tone is inferred, and Silversong keeps its ordinary English reading. The full name language is unconfirmed.", status: "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Harol as captain of the Emerald Song, corroborated during the DR 1748 voyage; the start and end of his captaincy are not established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting.
- Recorded supported campaign knowledge in `knownTo`, the article viewpoint in `POV`, and its temporal limits in `povNotes`.
- Added the primary name entry with a proposed pronunciation, leaving its language unconfirmed.
- Normalized the private query block’s `Campaign:None` marker to the equivalent canonical `Campaign:none` sentinel.

### Validated judgments
- The captaincy, family relationships, and evening music are corroborated by [[Emerald Song]], [[Ewen Silversong]], [[Dani Silversong]], and [[Pearl Copperharp]].

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm `HAH-rohl SIL-ver-song` in `Metadata:names:v1`. [[Languages]] gives Halfling the provisional analogue “Igbo, but may change or be diverse.” The proposal keeps full a and o vowels with sounded h, r, and l, retaining the final written consonant as a name adaptation. First-syllable stress is tentative and no tone is inferred; the transparent surname uses ordinary English. This qualified analogue does not establish exact Halfling phonology or the complete name’s language. If accepted, change the entry to `status: documented` and copy the pronunciation to frontmatter; otherwise revise it.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. Keep `dm_notes: color` if useful information remains in memory or another private source; change it to `none` only if a human confirms that all useful material is already shared.
%%^End%%
