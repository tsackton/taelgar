---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T09:51:53-04:00"
lintVersion: "2.1"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: market town
name: Tygate
whereabouts: Addermarch
dm_owner: none
dm_notes: none
---
%%^Metadata:article:v1%%
profile: place
mode: geographic reference
pov: current-setting account independent of the noncanonical Plaguelands campaign
%%^End%%

%%^Metadata:names:v1%%
- {name: Tygate, language: ancient Addermarian, pronunciation: TY-gayt, meaning: dwelling near a road or entrance, status: proposed}
%%^End%%

%%^Metadata:map:v1%%
status: missing
locations: []
%%^End%%

# Tygate
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Tygate is a small market town near the southern sources of the [[Aure]], set against the edge of the [[Darkwood]]. Its position makes it a last provisioning point before entering the forest or a first safe haven on the way out. Timber, resin, and pelts flow north through Tygate. A wooden palisade protects the town, with several watchtowers keeping a wary eye on the forest and wildlands to the south. 

The main road from Adderfell passes through Tygate before turning southwest to supply [[Darkwood Keep]] on the frontier.

%%^Lint%%
## Open findings

- [ ] `pronunciation.missing`: the naming worksheet supplies the proposal below; it is not yet accepted frontmatter.
- [ ] `map.required_missing`: a settlement requires map metadata, but no map locator was found; the persistent map block records this explicitly.
- [ ] `freshness.noncanonical_dm_material`: Plaguelands DM notes describe refugees fleeing Tygate, but [[Campaigns - Open Questions]] explicitly classifies that campaign as noncanonical. They do not make this article incorrect.

## Copy-ready candidates

```yaml
pronunciation: TY-gayt
```

## Applied changes

- Canonicalized frontmatter layout and added lint state.
- Added persistent article, simplified name, and required missing-map metadata; removed trailing whitespace from the touched final body line.

## Evidence reviewed

- [[Addermarch]] and [[Darkwood Keep]] for the settlement’s current regional role and road connection.
- [[Addermarch Village Names]] for the proposed pronunciation and etymology.
- Plaguelands DM notes together with [[Campaigns - Open Questions]] for their explicitly noncanonical status.
- Vault-wide map-locator search; no hex or coordinate for Tygate found.

## Status disposition

- No pre-existing status tags required disposition.
%%^End%%
