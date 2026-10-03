---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Tollender
campaignInfo: []
born: 1504
gender: female
died: 1559
name: Jane of Tollen
affiliations:
  - {org: Vostok, type: leader, title: Queen Regent, end: 1551}
  - {org: Sembara, type: leader, title: Queen Regent, end: 1555}
  - {org: Ardlas, type: leader, title: Queen Regent, end: 1555}
  - {org: Lavnoch, type: leader, title: Queen Regent, end: 1555}
  - {org: Breva, type: leader, title: Queen Regent, end: 1555}
knownTo: []
dm_owner: none
dm_notes: none
POV: modern
---
# Jane of Tollen
>[!info]+ Biographical Info  
> A [[Tollen|Tollender]] [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

The second wife of [[Derik III]], from a powerful and rich merchant family in [[Tollen]]. She was Queen Regent in the immediate aftermath of the Great War, and history has not always been kind to her reign. Many consider her short-sighted and overly concerned with promoting her son, [[Bertram I]], at the expense of his older half-siblings, [[Reginald]] and [[Hugh of Sewick|Hugh]]. Others argue that her intelligence and careful stewardship of the throne prevented further deterioration of Sembara in the aftermath of the [[Great War]].

All agree that she was shrewd, at times spiteful, and always economical. She was known for her dislike of waste: wasted effort, wasted money, wasted time.

%%^Metadata:names:v1%%
- {"name": "Jane of Tollen", "language": "Tollish"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective assessment of Jane’s regency and historical reputation; the exact regency boundaries remain inconsistent across reference sources.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added required campaign knowledge metadata, a persistent name entry, and a modern retrospective POV with temporal coverage notes.
- Normalized frontmatter order and collection formatting where needed.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Error — correctness.cross_note_conflict:** The phrase `his older half-siblings, [[Reginald]] and [[Hugh of Sewick|Hugh]]` links the wrong Hugh. [[Derik III]] and [[House of Sewick]] identify Bertram’s half-brother as [[Hugh of Wisenfold]], son of Derik and Sarabet; [[Hugh of Sewick]] was Charlotte I’s son and died in DR 1518. Copy-ready correction: `his older half-siblings, [[Reginald]] and [[Hugh of Wisenfold|Hugh]]`. Confirm this identity correction before changing the authored link.
- [ ] **Warning — chronology.regency_conflict:** All five Queen Regent affiliations omit a start year, although [[Bertram I]] and [[Timeline of Sembaran History]] place Jane’s accession to the regency in DR 1549. Her Sembara, Ardlas, Lavnoch and Breva affiliations end in 1555, consistent with the start fields in [[Bertram II]], while the timeline explicitly ends her regency in winter DR 1553. Add `start: 1549` to the existing entries after confirming the chronology, and choose either `end: 1553` or the retained `end: 1555` for those four entries; reconcile [[Bertram II]] and the timeline at the same time. Keep the separately recorded Vostok end and the timeline’s qualified highland history distinct; do not apply one end year to every realm.
%%^End%%
