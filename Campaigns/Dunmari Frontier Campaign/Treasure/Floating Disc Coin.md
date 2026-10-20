---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:26:32-04:00"
lintVersion: "3.5"
tags: [object, status/check/lint]
typeOf: coin
subTypeOf: magic
ddbLink: https://www.dndbeyond.com/magic-items/1872181-floating-coin
name: Floating Disc Coin
knownTo: [dufr]
POV: modern
---
# The Floating Disc Coin
>[!info]+ Information  
> (magic coin)  
> [Mechanics](https://www.dndbeyond.com/magic-items/1872181-floating-coin)  
> `$=dv.view("_scripts/view/get_Affiliations")`

A small golden coin, unusually heavy for its size, and without a recognizable mark. 

%%^Campaign:DuFr%%

Found by the [[Dunmar Fellowship]] near the petrified form of [[Arcus]] in the fort east of [[Gomat]]. 

Viewed in [[Mirror of the Past]]: 

![[Floating Disc Coin Vision]]
%%^End%%

%%SECRET[v2:4ee3b267cf98fcce31653a791097e567]%%

%%^Metadata:names:v1%%
- {"name": "Floating Disc Coin", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern physical description with a DR 1748 discovery account and visions of undated earlier owners; no current owner is asserted.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added supported identity, campaign knowledge, and temporal metadata.
- Recorded the descriptive subject name without a pronunciation; its ordinary title and established name component need no new guide.

### Validated judgments
- The descriptive title is plain English and needs no pronunciation guide.
- The physical description, mechanics link, discovery account, and linked vision supply a usable bounded reference; a concise operational and later-ownership addition is provided privately as a worth-expanding candidate.
- Reviewed the SECRET block; its contents and recovery proposal remain confined to the private handoff.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The opening marker `%%^Campaign:DuFr%%` uses a registry alias. [[Campaign Registry]] specifies the lowercase short code. Replace only that opening marker with `%%^Campaign:dufr%%`, preserving its contents and closing marker; confirm the intended filtered visibility when adopting the syntax change.
%%^End%%
