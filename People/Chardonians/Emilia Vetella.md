---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T09:51:53-04:00"
lintVersion: "2.1"
displayDefaults: {defArt: ""}
tags: [person, status/check/lint]
species: human
ancestry: Chardonian
gender: female
knownTo: []
dm_owner: tim
dm_notes: important
---
%%^Metadata:article:v1%%
profile: person
mode: character reference
pov: current-setting account after DR 1749
%%^End%%

%%^Metadata:names:v1%%
- {name: Emilia Vetella, language: Chardonian, pronunciation: eh-MEE-lee-ah veh-TELL-ah, status: proposed}
%%^End%%

# Emilia Vetella
>[!info]+ Biographical Info  
> A [[Chardonian Empire|Chardonian]] [[Humans|human]] (she/her)

Lord Admiral of the Chardonian Navy. Trusted advisor to [[Mitus Verina Auratan]].

%%^Lint%%
## Open findings

- [ ] `identity.implicit_name`: add the filename-derived name explicitly to frontmatter.
- [ ] `pronunciation.missing`: the Latinate Chardonian pronunciation below is proposed.
- [ ] `coverage.newer_campaign_history`: the later war note establishes her appointment as admiral for the DR 1749 naval campaign, which culminated in victory outside Darba; the character note has not caught up.
- [ ] `knownTo.verify_dufr`: the Dunmari Frontier-derived war synthesis names Emilia, but no direct session mention establishes that the party learned her identity; keep `knownTo: []` unless a human confirms it.
- [ ] `dm_notes.attestation`: `dm_notes: important` asserts significant off-vault information and requires human confirmation.

## Copy-ready candidates

```yaml
name: Emilia Vetella
pronunciation: eh-MEE-lee-ah veh-TELL-ah
```

```markdown
In DR 1749, Emilia was appointed admiral of the fleet for the [[Chardon-Dunmar War]], whose naval campaign culminated in a Chardonian victory outside [[Darba]].
```

## Applied changes

- Canonicalized frontmatter layout and added lint state.
- Added the required explicit `knownTo: []` and persistent article/name metadata.

## Evidence reviewed

- [[Chardon-Dunmar War]], a newer canonical event synthesis tied to the Dunmari Frontier campaign.
- Vault-wide name, alias, backlink, campaign, and DM-material searches; no second Emilia record or conflict found.

## Status disposition

- No pre-existing status tags required disposition.
%%^End%%
