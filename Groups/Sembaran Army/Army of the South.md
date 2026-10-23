---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: army
partOf: Sembaran Army
name: Army of the South
whereabouts: Fellburn
dm_owner: mike
dm_notes: important
POV: 1720
---
# The Army of the South
>[!info]+ Information  
> An army  
> `$=dv.view("_scripts/view/get_Affiliations")`  
> Parent Organization: the [[Sembaran Army]], [[Sembara]]  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%%^Date:1720%%
The Army of the South is a regiment of 400 soldiers, divided into four regiments of 80 soldiers each plus the garrison at Fellburn. Usually two regiments rotate on patrol in the [[Borderlands]] and two are based at the garrison in Fellburn. 

Since the [[Undead Attacks in Sembara]] this army has been dispersed. The surviving troops are largely part of an informal army under the command of [[Jacques Bellemont]], the Duke of Wisford. Some question whether this is treason, but the Duke feels this is necessary to defend the [[Duchy of Wisford]] from undead, given the failure of the Army of the South to do so.

One of the regiments is scattered across the [[Borderlands]], although various patrols have turned up in [[Cleenseau]] and elsewhere. 
%%^End%%

%%% Note: Conceptually the post-1720 history of this army is very different but it is hard to write because it depends a bit on events in the Clee game. Currently, the army is basically the personal army of the Duke of Wisford; this can't last, but how it gets resolved is a little bit unclear. Most likely, the Army is recreated after the various crises of 1720 largely along the same lines as it was before, but that could change.
%%

%%^Metadata:names:v1%%
- {"name": "Army of the South", "language": "Common", "status": "inferred", "notes": "The displayed form is an ordinary English descriptive title."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 account of the Army of the South during the undead crisis, combining its earlier normal strength and patrol pattern with its dispersal and surviving troops; the opening paragraph’s temporal framing requires clarification.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name and temporal metadata; preserved the header version and human attestations.
- Corrected “disbursed” to “dispersed” for scattered troops and restored the missing “is” in the editorial comment.

### Validated judgments
- The article records the army’s defining disruption; the existing shared comment explicitly preserves uncertainty about its later restoration and is not adopted as settled history.

### Open findings

- [ ] **Warning — editorial.prose_clarity:** The opening calls the Army of the South “a regiment of 400 soldiers, divided into four regiments of 80 soldiers each,” leaving the military level unclear. The arithmetic leaves 80 soldiers at Fellburn, but does not establish the intended unit names; [[Claire of Fellburn]] and [[Rene Dubois]] also identify a Ninth Company. Confirm the hierarchy. A neutral candidate pending that decision is: “The Army of the South numbered 400 soldiers, divided into four units of 80 soldiers each plus the garrison at Fellburn.” Do not substitute companies or regiments without confirming the organization.

- [ ] **Warning — temporal.inconsistent_viewpoint:** Inside the existing `Date:1720` block, the first paragraph says the normal force “is” organized and patrols “rotate,” while the next paragraph describes the army’s dispersal after the [[Undead Attacks in Sembara]]. The two states need explicit framing. After confirming the unit terminology, a bounded first-paragraph candidate is: “Before the undead attacks of DR 1720, the Army of the South numbered 400 soldiers, divided into four units of 80 soldiers each plus the garrison at Fellburn. Usually two units rotated on patrol in the [[Borderlands]] and two were based at the garrison in Fellburn.” Retain the existing later-state paragraphs. If this baseline should also appear in earlier exports, propose moving only that paragraph outside `Date:1720`; that visibility decision requires approval.
%%^End%%
