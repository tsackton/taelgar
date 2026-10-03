---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:44:02-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
born: 1690
name: Isolde
whereabouts:
  - {type: home, location: Asineau, start: 1717, end: 1720-01-10}
  - {type: away, location: Champimont, start: 1720-01-11}
knownTo: [clee]
dm_owner: mike
dm_notes: color
POV: 1720
---
# Isolde
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]]  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[isolde-asineau.png|right|320]]A skilled brawler and swordswoman, currently employed by [[Lorin Valbert]] to watch over his interests. Seems attached to her lord in a professional way.

%% Fled with Lorin after the events in [[Cleenseau - Session 11]]. %%

%%^Metadata:names:v1%%
- {"name": "Isolde", "language": "Sembaran", "pronunciation": "ee-ZOLD", "status": "proposed", "notes": "French-influenced reading under [[Languages]]: initial i as ee, intervocalic s as z, final e silent, and emphasis on zold. An English ih-ZOLD reading is also plausible; the preferred proposal is not adopted phonology."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a January DR 1720 portrait of Lorin Valbert's retainer, with dated whereabouts marking her departure from Asineau; no later settled residence is established.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added `knownTo: [clee]` from campaign evidence, persistent name metadata, and a supported article POV with temporal notes.
- Normalized frontmatter order and collection formatting where needed.
- Corrected “watch over is interests” to “watch over his interests.”

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The primary name remains `proposed`. Preferred pronunciation: `ee-ZOLD`. French-influenced reading under [[Languages]]: initial i as ee, intervocalic s as z, final e silent, and emphasis on zold. An English ih-ZOLD reading is also plausible; the preferred proposal is not adopted phonology. Accept the intended pronunciation and record it in frontmatter, or revise the name-block proposal before clearing this task.
- [ ] **Warning — coverage.later_material_change:** The final comment and [[Asineau]] record Isolde's departure with Lorin, while [[Cleenseau - Session 12]] establishes their onward flight from [[Champimont]] across the river. Her open-ended Champimont whereabouts therefore should not imply a continuing stay. Candidate visible addition: `In January DR 1720, Isolde left [[Asineau]] with [[Lorin Valbert]] and remained in his service as he fled east through [[Champimont]].` Confirm a supported end bound for that stop, leaving the later residence unknown rather than inventing one. Update the location/temporal account, defer with the appropriate game-update status, or intentionally retain an earlier snapshot.
%%^End%%
