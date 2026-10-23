---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the, boxInfo: "One of the <partOf:1UA>", wHome: ""}
tags: [ancestry, status/check/lint]
typeOf: tribe
partOf: Northern Tribes
name: "Shu'anra"
dm_owner: none
dm_notes: none
POV: modern
---
# The Shu'anra
>[!info]+ Information  
> One of the [[Northern Tribes|Northern Tribes of the Deno'qai]]

The Shu'anra are one of the [[Northern Tribes|northern]] [[Deno'qai]] tribes. Like other northern Deno'qai tribes, the Shu'anra are descended from the survivors of the [[Great War]]. They survived the [[Conclave War]] and the [[Blood Years]] in hiding, before emerging from the marginal lands in the low passes of the mountains, and now largely live in the forests east of the [[Blackwater Fens]] and west of the [[Sentinel Range|Sentinels]]. 

Less isolated than the [[Ko'zula]], a number of Shu'anra families have drifted south over the years, some settling as far south as the [[Elderwood]].

## Members of the Shu'anra Tribe

```dataview
TABLE WITHOUT ID file.link AS Person, affiliations AS Affiliations
FROM #person
WHERE contains(affiliations, this.file.link) OR contains(affiliations.org, this.file.link) OR contains(affiliations, this.name) OR contains(affiliations.org, this.name)
SORT file.name ASC
```



%%^Campaign:none%%

Session notes:
- [[Session 52 (DuFr)]]: [[Ariel]] met the [[Dunmar Fellowship]] in the [[Neshet|Te'kula village]] and told [[Delwath]] stories of the northern Deno'qai and the [[Meswati]].
- [[Ariel]] is a Shu'anra woman whose home was in the [[Forest of Dreams]], between the Blackwater Fens and the [[Sentinel Range|Sentinels]], before settling with the [[Te'kula]]. Source: [[Ariel]].
- Ariel preserves stories of the Shu'anra surviving the [[Great War]], fleeing into the Sentinels during the [[Blood Years]], dragonfire from the sky, and later migration south for better prospects. Source: [[Ariel]].
- Ariel knows northern stories of [[Yezali]] and the lost tanshi called the [[Meswati]]. Source: [[Ariel]].

%%^End%%

%%^Metadata:names:v1%%
- {"name": "Shu'anra", "language": "unknown", "pronunciation": "shoo-ahn-RAH", "status": "proposed", "notes": "Proposed from the Deno'qai cultural context and the Hebrew side of the Hebrew-or-Arabic analogue in [[Languages]]: sh as in ship, u as oo, a as ah, an audible r, and tentative final stress; the apostrophe separates the initial vowels. An Arabic-informed shoo-AHN-rah stress pattern is also possible. The name's source language, vowel length, and exact phonology are unrecorded."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern Shu'anra settlement east of the Blackwater Fens and migration south; the Great War, Conclave War, and Blood Years supply historical context rather than a narrower article date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Quoted the display template to repair invalid YAML and normalized frontmatter order without changing its template text.
- Removed the duplicated “the” from the header and corrected “familes” to “families”.
- Added primary name metadata with a proposed pronunciation, plus the modern POV and temporal coverage.

### Validated judgments
- The brief article establishes the tribe's identity, displacement, present territory, and southward migration. The Campaign:none passage remains a useful source index to [[Ariel]] and [[Session 52 (DuFr)]].

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Review `shoo-ahn-RAH` for Shu'anra. This uses the Hebrew side of the Deno'qai cultural guidance in [[Languages]]: sh as in ship, u as oo, a as ah, an audible r, and tentative final stress, with the apostrophe separating the initial vowels. An Arabic-informed `shoo-AHN-rah` stress pattern is also possible. Exact language, vowel length, and name-specific phonology are unrecorded. Accept or revise the `Metadata:names:v1` proposal; on acceptance, mark it `documented` and copy the accepted pronunciation to frontmatter.
%%^End%%
