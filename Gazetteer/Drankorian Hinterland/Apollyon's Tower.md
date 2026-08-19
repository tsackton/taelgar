---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T16:23:04-04:00"
lintVersion: "2.3"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: building
typeOfAlias: tower
name: "Apollyon's Tower"
whereabouts:
  - {type: home, location: Circular Island, startFilter: "1", linkText: "on"}
dm_owner: tim
dm_notes: important
POV: 1749
---
# Apollyon's Tower
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

Apollyon's Tower is a black marble spire on the coast of the [[Circular Island]], once a stronghold and retreat of the Drankorian emperor [[Apollyon]], a place of dark study and craft. The tower itself is almost 250 feet tall, with a main section that rises 140 feet from the ground, and battlements and a tower extension that rise another 100 feet, capped with a platform open to the sky. After the [[Fall of Drankor]], the tower stood abandoned and warded, looming over the island’s storm‑lashed shore. 

%%^Campaign:dufr%%
In DR 1749 the [[Dunmar Fellowship]] assaulted the ruin, uncovering its forge, libraries, and throne room, and carrying away the treasures now catalogued as [[Apollyon's Tower Treasure]].
%%^End%%

%%SECRET[v2:336d2b6a742073ad1667272cfcf6ff5e]%%

%%^Metadata:names:v1%%
- {name: "Apollyon's Tower", role: primary, language: Common, pronunciation: inherited from Apollyon, status: inferred, notes: descriptive possessive title; the component pronunciation remains unresolved}
- {name: Apollyon, role: name component, language: unknown, status: unresolved}
%%^End%%

%%^Metadata:article:v1%%
mode: campaign-era place reference
povNotes: "Accuracy range: DR 1749 after the Dunmar Fellowship's assault. The visible article combines stable physical and historical description with the party's dated exploration; the SECRET block contains private encounter design rather than a second article viewpoint."
%%^End%%

%%^Lint%%
## Taelgar note lint

### Open findings

- [ ] **warning — `name.pronunciation_inherited_unresolved`:** The title’s pronunciation is inherited from `Apollyon`, but [[Apollyon]] has no accepted pronunciation. A cautious conventional-English proposal is `uh-POL-ee-on`; the source language remains unknown. Copy-ready candidate for the Apollyon note:
  ```yaml
  pronunciation: uh-POL-ee-on
  ```
  Accept or replace that pronunciation before treating the tower’s inherited exception as resolved.

### Applied changes

- Canonicalized frontmatter, added the explicit name and `POV: 1749`, changed the campaign marker to `Campaign:dufr`, and migrated the article/name blocks to the current schemas.

### Validated

- Existing local hidden notes support `dm_notes: important`; they are not an open finding. The SECRET block remains private encounter material and is not legacy syntax.
%%^End%%
