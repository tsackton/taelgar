---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, status/check/ai, status/check/lint]
species: human
ancestry: Zimka
born: 1673
gender: female
name: Avelina Smith
whereabouts: Cleenseau
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720
---
# Avelina Smith
>[!info]+ Biographical Info  
> A Zimka [[Humans|human]] (she/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

An important smith and leader of the metalworking community of [[Cleenseau]]. She trained with dwarves in her youth.

After injuring her shoulder and right arm in the troubles of 1720, Avelina left her Cleenseau weaponsmithing shop to her journeymen. She went to [[Asineau]] to spend time with its dwarven smiths and became the manor's armoury master.

%%^Metadata:names:v1%%
- {"name":"Avelina Smith","language":"unknown","pronunciation":"ah-veh-LEE-nah SMITH","notes":"Proposed using the Zimkovan Baltic analogue in [[Languages]] for the given name: separate a-ve-li-na syllables, v as v, and a provisional stress on li. Smith follows the ordinary English spelling of the displayed occupational surname. Zimka ancestry does not settle the language of this mixed full form; Baltic stress and any intended local adaptation remain uncertain.","status":"proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 account spanning her Cleenseau smithing career and the later injury and move to Asineau, with the latter state established toward the end of May.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and recorded the explicit name, campaign knowledge, name metadata, and temporal viewpoint where missing.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.whereabouts_conflict:** The frontmatter has `whereabouts: Cleenseau`, while the final paragraph places her in Asineau as armoury master; [[Asineau Hirelings - Authored Turns]] places this transition toward the end of May DR 1720. Preserve the Cleenseau origin while recording the new base, subject to confirming the intended home/away distinction. Copy-ready candidate:
```yaml
whereabouts:
  - {type: home, location: Cleenseau}
  - {type: home, location: Asineau, start: 1720-05}
```
The month is a coarse bound; the source does not establish an exact move day.

- [ ] **Warning — metadata.names_unresolved_status:** The proposed pronunciation `ah-veh-LEE-nah SMITH` in `Metadata:names:v1` needs human acceptance. Proposed using the Zimkovan Baltic analogue in [[Languages]] for the given name: separate a-ve-li-na syllables, v as v, and a provisional stress on li. Smith follows the ordinary English spelling of the displayed occupational surname. Zimka ancestry does not settle the language of this mixed full form; Baltic stress and any intended local adaptation remain uncertain. If accepted, copy it to frontmatter `pronunciation` and mark the entry `documented`; otherwise revise the proposed entry.
%%^End%%
