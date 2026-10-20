---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:49:48-04:00"
lintVersion: "3.5"
displayDefaults: {wOrigin: "", wOriginU: "", defArt: ""}
tags: [object, status/check/lint]
typeOf: ring
subTypeOf: magical
ancestry: Drankorian
ddbLink: https://www.dndbeyond.com/magic-items/3643042-ring-of-displacement
pcOwner: Delwath
rarity: uncommon
image: "[[delwath-ring-of-displacement.jpg]]"
name: Ring of Displacement
whereabouts:
  - {type: home, location: Agata, end: 1748}
  - {type: home, location: Delwath, start: 1748}
knownTo: [dufr]
POV: 1748
---
# Ring of Displacement
>[!info]+ Information  
> (uncommon [[Drankorian Empire|Drankorian]] magical ring)  
> [Mechanics](https://www.dndbeyond.com/magic-items/3643042-ring-of-displacement)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[delwath-ring-of-displacement.jpg|right|320]]An unadorned ring made of three entwined golden braids, that radiates illusion magic. It was possessed by [[Agata]] for many years, and carried on her person. Taken by [[Delwath]] after [[Agata]] was slain by [[Dunmar Fellowship]] in 1748.

Seen in [[Mirror of the Past]]: 

![[Ring of Displacement Vision]]

%%SECRET[v2:cab234c892ec56e6442a40fa51361b00]%%

%%^Metadata:names:v1%%
- {name: "Ring of Displacement", language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1748 account after the ring passed from Agata to Delwath; the ownership metadata does not include its later transfer to Jotha.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added the explicit name, `knownTo: [dufr]`, primary name metadata, and the DR 1748 article viewpoint and coverage limits.
- Corrected “An unadorned ring of made of” to “An unadorned ring made of”.

### Validated judgments
- The local-only SECRET block was reviewed; its contents remain outside this report.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Party Treasure - Former]] records that the Ring of Displacement was given to [[Jotha]], while this note still has `pcOwner: Delwath` and an unbounded Delwath home entry starting in 1748. Decide whether to update the ownership account and POV, defer the update with the appropriate human-managed `status/gameupdate/dufr`, or intentionally preserve the DR 1748 snapshot. Copy-ready addition if updating: “The ring later passed from [[Delwath]] to [[Jotha]].” An updated current ownership field would be `pcOwner: Jotha`; reconcile the existing whereabouts history at the same time. The source supplies no transfer date, so do not invent a dated boundary.
%%^End%%
