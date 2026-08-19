---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T09:51:53-04:00"
lintVersion: "2.1"
tags: [place, status/check/lint]
typeOf: neighborhood
typeOfAlias: ward
whereabouts: Tollen
dm_owner: none
dm_notes: none
---
%%^Metadata:article:v1%%
profile: place
mode: geographic reference
pov: current-setting account with explicitly provisional ancient history
%%^End%%

%%^Metadata:names:v1%%
- {name: Aesganstrad, language: Skaegish, pronunciation: AYS-gan-strahd, derivedFrom: Aesgan, status: proposed, notes: Aesgan's exact nature is not canonical}
%%^End%%

# Aesganstrad
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

One of the ancient original wards of the city of [[Tollen]]. 

%% DM Notes
Name derives from Aesgan, a semi-mythical Skaegish hero who is said to have protected/resettled Tollen after the Downfall. Who or what Aesgan was is not canonical, but their existence in some form, at least in myth, is canonical. E.g. Aesgan could have been an elf or a dragon and later became associated with the Skaer, but should have a real existence of some kind. 

Best preserved of the ancient districts. Likely some landmarks or other features that date to before the Downfall. 

Dunmar campaign never went to this district, except maybe as part of an un-narrated walk to some other destination. 
%%

%%^Lint%%
## Open findings

- [ ] `identity.implicit_name`: add the filename-derived name explicitly to frontmatter.
- [ ] `pronunciation.missing`: the Skaer/Skaegish-based pronunciation below is proposed.
- [ ] `coverage.established_geography`: the body does not capture the ward’s established location, streetscape, or relationship to Tollen’s ancient core.
- [ ] `development.provisional_history`: the DM comment correctly keeps Aesgan’s nature and ancient landmarks provisional; do not turn these into incorrectness findings.

## Copy-ready candidates

```yaml
name: Aesganstrad
pronunciation: AYS-gan-strahd
```

```markdown
Aesganstrad lies north and west along the [[Volta]] from [[Fiskurth]]. Together with Fiskurth and [[Skepwalk]], it forms the ancient core of pre-Drankorian [[Tollen]]; today it is a tangle of narrow streets, leaning houses, and old statues to forgotten heroes.
```

## Applied changes

- Canonicalized frontmatter layout and added lint state.
- Added persistent article and simplified name metadata.

## Evidence reviewed

- [[History of Tollen]] for the ward’s Skaer-era origin, river position, name tradition, and preserved ancient fabric.
- [[Tollen]], [[Wards of Tollen]], [[Port of Tollen]], and [[Hydrology of Tollen]] for current geography and streetscape.
- The existing DM comment and [[Tollen - Design Note]] as provisional development evidence, not canon.

## Status disposition

- No pre-existing status tags required disposition.
%%^End%%
