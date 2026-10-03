---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/review, status/check/lint]
species: human
ancestry: Sembaran
born: 1396
gender: male
died: 1462
title: King
name: Derik I
affiliations:
  - {org: House of Sewick, type: primary}
  - {place: Tyrwingha, start: 1425}
  - {place: Sembara, start: 1429}
  - {place: Duchy of Telham, title: Duke, start: 1429}
knownTo: [adma, clee]
dm_owner: none
dm_notes: none
POV: modern
---
# King Derik I
>[!info]+ Biographical Info
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him), of the [[House of Sewick]]
> `$=dv.view("_scripts/view/get_PageDatedValue")`
> `$=dv.view("_scripts/view/get_Affiliations")`

%% status/review -> Important figure with more information in various linked notes and backlinks, so could probably use a review pass %%

The founder of the [[House of Sewick]], he established modern Sembara at the [[Treaty of Wisford]] in the fall of 1429 and reigned over a united Sembara and Tyrwingha until his death in DR 1462.

He had five children, and was succeeded by his second son, [[Derik II]].  His third child, Matilda, inherited the Duchy of Telham, and after his reign the Sembaran royalty no longer styled themselves "Dukes of Telham".

%%^Metadata:names:v1%%
- {"name": "Derik I", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: modern retrospective summary of the founder of the House of Sewick and his succession in DR 1462; this is not a snapshot of a living king.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the primary name entry and the article’s POV and temporal-coverage note.
- Recorded supported campaign knowledge in `knownTo`.

### Validated judgments
- `status/review` is supported by the specific missing founding history identified below; the existing review comment is an editorial pointer and remains unchanged.
- Derik is an ordinary recognizable given name, and I is the regnal numeral; no pronunciation is needed.

### Editorial assessment
**Underdeveloped**. The note names Derik as the founder of modern Sembara but omits his rise in Tyrwingha and victory over Avatus, the established events that explain that founding role. A short account of those two linked developments is sufficient; the unsettled campaign-by-campaign chronology need not be adopted.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** The opening jumps directly to the Treaty of Wisford. [[Derik I's Arrival in Tyrwingha]], [[Stories of Tyrwingha for Profit]], [[Dominion of Avatus]], and [[Army of Mostreve]] establish the rise and military victory behind his foundational role. Add a bounded paragraph: `Derik rose to prominence during the wars against [[Avatus]]. In DR 1425 he [[Derik I's Arrival in Tyrwingha|arrived in Tyrwingha]], where tradition describes [[Archfey Ethlenn|Ethlenn]] blessing him before his proclamation as king. He organized the Iron Guard and led the forces that defeated Avatus, whose dominion collapsed before the [[Treaty of Wisford]] established the new kingdom.` Keep the miracle attributed to tradition and avoid the conflicting detailed battle dates in [[Timeline of Sembaran History]].
%%^End%%
