---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T12:58:09-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: halfling
ancestry: null
campaignInfo:
  - {campaign: dufr, person: Wellby, date: 1730, type: met}
  - {campaign: dufr, date: 1748-12-30, type: met}
born: 1685
gender: female
name: Harriet Goodbarrel
aliases: [Harriet]
affiliations:
  - {org: Goodbarrels, type: primary}
  - {org: The Singing Fox, title: Proprietor, type: leader}
whereabouts:
  - {type: home, end: 1722, location: Western Gulf}
  - {type: home, location: The Singing Fox}
  - {type: away, start: 1748-12-30, end: 1748-12-30, location: Vindristjarna}
knownTo: [dufr]
dm_owner: tim
dm_notes: color
POV: 1740s
---
# Harriet Goodbarrel
>[!info]+ Biographical Info  
> A [[Halflings|halfling]] (she/her), of the [[Goodbarrels]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:dufr%% Met by [[Wellby]] on DR 1730 at [[The Singing Fox]], in [[Fairgate Outer]], the [[Tollen|Free City of Tollen]] %%^End%%  
>> %%^Campaign:dufr%% Met by the [[Dunmar Fellowship]] on December 30th, 1748 on [[Vindristjarna]], in the [[Tollen|Free City of Tollen]] %%^End%%

![[harriet-goodbarrel.png|right|300]]%% notes
Secret mostly contains roleplaying notes; ask if they'd be useful
tagged dm_owner only because of connection to Wellby backstory
%%

Harriet's melodious voice graces *[[The Singing Fox]]* on performance nights, drawing an enthusiastic crowd of locals and passing halflings. Though initially reserved, she truly shines when on stage, and alongside her wife, [[Chenna Goodbarrel|Chenna]], she's made the tavern a warm haven for many.

Harriet married into the [[Goodbarrels|Goodbarrel clan]]; while she never had her own children, she feels a matronly duty to all the scattered Goodbarrel youth. 
## Relationships
- [[Chenna Goodbarrel]], wife
- [[Wellby]], a distant relation, something like a third cousin once removed by marriage
%%^Campaign:none%%
```dataview
TABLE WITHOUT ID choice(contains(file.tags,"organization"), "Organization", "Person") as Type, name as Name, choice(species, species, typeof) as Info, file.link as Link
FROM #person OR #organization 
WHERE contains(file.outlinks, this.file.link) OR contains(file.inlinks, this.file.link)
SORT choice(species, species, typeof)
```
%%^End%%



%%SECRET[v2:5d6a1cb74315a062cd32091937ad29c1]%%

%%^Metadata:names:v1%%
- {"name": "Harriet Goodbarrel", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a 1740s portrait of Harriet performing at the Singing Fox with her wife Chenna, with selected older family background; the duration of these relationships is not fully recorded.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Canonicalized frontmatter ordering and collection formatting.
- Added the primary name entry and persistent temporal coverage metadata.
- Added `knownTo: [dufr]` and `POV: 1740s`; normalized the existing Dunmar Frontier and private-block campaign markers and campaignInfo code.

### Validated judgments
- Harriet Goodbarrel is an obvious ordinary name with an English compound surname, so no pronunciation is needed; the name language is not inferred from ancestry.
- [[The Singing Fox]] and [[Chenna Goodbarrel]] corroborate the performance, tavern, and spouse relationships; the note is sufficient for its present role.
- The SECRET block was reviewed separately and preserved; the ordinary comment remains editorial guidance and the existing private query remains private.

### Open findings

- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The current `color` attestation may refer to remembered information or an off-vault source, and in-note SECRET material does not establish external evidence. Retain `color` if useful information remains elsewhere; change it to `none` only after human confirmation.
%%^End%%
