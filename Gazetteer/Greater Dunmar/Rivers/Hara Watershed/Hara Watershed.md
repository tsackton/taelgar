---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T09:51:53-04:00"
lintVersion: "2.1"
tags: [place, status/check/lint]
typeOf: watershed
whereabouts: Hara Basin
dm_owner: tim
dm_notes: important
---
%%^Metadata:article:v1%%
profile: place
mode: geographic reference
pov: current-setting account
%%^End%%

%%^Metadata:names:v1%%
- {name: Hara, role: watershed name, language: Dunmari, pronunciation: HAH-rah, status: proposed}
%%^End%%

# The Hara Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Hara Watershed is the river system that drains the central plains of [[Dunmar]]. Its principal river, the [[Hara]], flows from the northern uplands past [[Tokra]], into the lowlands. Seasonal monsoon rains define the rhythm of the watershed: dry winters with low flows, and summers when rivers run full. Culturally, the watershed aligns with [[Central Dunmar]], and the Hara is the lifeblood of this region for the water it provides, though even the major rivers are typically only reliably navigable during the wettest parts of the year. 

The major tributaries of the Hara river include:
- The [[Sone]], which flows east across the [[Songara Plains]]
- The [[Sukal]], a seasonal river that flows east from the [[Copper Hills]]. 
- The [[Thandar]], which flows south from the [[Sentinel Range|Sentinels]] and joins the Hara north of [[Tokra]]. 

%%^Lint%%
## Open findings

- [ ] `identity.implicit_name`: add the filename-derived article name explicitly to frontmatter.
- [ ] `pronunciation.missing`: the Dunmari-based pronunciation below is proposed.
- [ ] `dm_notes.attestation`: `dm_notes: important` asserts significant off-vault information and requires human confirmation.
- [ ] `editorial.list_punctuation`: the tributary list mixes terminal punctuation.

## Copy-ready candidates

```yaml
name: Hara Watershed
pronunciation: HAH-rah
```

## Applied changes

- Canonicalized frontmatter layout and added lint state.
- Added persistent article and simplified name metadata.

## Evidence reviewed

- [[Hara]], [[Sone]], [[Sukal]], and [[Thandar]] for the river system and seasonal flow.
- [[Dunmar]] and [[Central Dunmar]] for regional significance.
- Later changes since the target’s most recent commit only link the watershed and do not add contradictory invention.

## Status disposition

- No pre-existing status tags required disposition.
%%^End%%
