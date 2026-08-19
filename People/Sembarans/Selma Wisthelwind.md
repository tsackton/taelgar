---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T09:51:53-04:00"
lintVersion: "2.1"
tags: [person, status/check/lint]
species: human
ancestry: Zimka
born: 1644
gender: female
name: Selma Wisthelwind
affiliations:
  - {org: "The Fox's Flagon", type: leader, title: Proprietor, start: 1712}
whereabouts:
  - {type: home, location: Ardlas}
  - {type: home, start: 1709, end: 1711, location: Cleenseau}
  - {type: home, start: 1712, location: "The Fox's Flagon"}
knownTo: [Clee]
dm_owner: mike
dm_notes: none
---
%%^Metadata:article:v1%%
profile: person
mode: character reference
pov: DR 1720 Cleenseau campaign reference
%%^End%%

%%^Metadata:names:v1%%
- {name: Selma Wisthelwind, language: Zimka, pronunciation: SELL-mah WISS-thel-wind, status: proposed}
%%^End%%

# Selma Wisthelwind
>[!info]+ Biographical Info  
> A Zimka [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[selma-wisthelwind.png|right|320]]Selma bought The Fox's Flagon for cash 8 years ago, and seems to enjoy running the inn as a retirement of sorts. From what exactly is not clear. She has always been a bit of an outsider in town and is one of the few people who keeps the old [[Kestavo]] religion of [[Zimkova]].

%%^Lint%%
## Open findings

- [ ] `pronunciation.missing`: the Zimka-based pronunciation below is proposed.
- [ ] `temporal.relative_date`: “8 years ago” is suitable only under the newly recorded DR 1720 POV; a dated formulation would survive later campaign views better.
- [ ] `coverage.established_role`: [[Cleenseau]] records that Selma sponsors the local Wanderer shrine, an established public role absent here.
- [ ] `dm_owner.verify`: `dm_owner: mike` is a human coordination attestation and cannot be verified from shared files.

## Copy-ready candidates

```yaml
pronunciation: SELL-mah WISS-thel-wind
```

```markdown
Selma bought [[The Fox's Flagon]] for cash in DR 1712 and appears to enjoy running the inn as a form of retirement.
```

```markdown
She also sponsors the shrine to the [[The Wanderer|Wanderer]] in [[Cleenseau]], whose practices retain strong [[Kestavo]] characteristics.
```

## Applied changes

- Canonicalized frontmatter layout and added lint state.
- Added evidence-backed `knownTo: [Clee]` and persistent article/name metadata; removed trailing whitespace from the touched body line.

## Evidence reviewed

- [[Cleenseau Campaign - Index of NPCs]], which explicitly lists Selma among people known to the party.
- [[The Fox's Flagon]] for her ownership and campaign-specific relationship with Viepuck.
- [[Cleenseau]] for the shrine sponsorship; Cleenseau campaign dates establish the DR 1720 POV.

## Status disposition

- No pre-existing status tags required disposition.
%%^End%%
