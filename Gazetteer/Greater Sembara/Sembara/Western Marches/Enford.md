---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T01:11:18-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: fortified town
name: Enford
whereabouts: Marches of Enford
dm_owner: mike
dm_notes: color
POV: modern
---
# Enford
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

An important garrison town on the south banks of the [[Enst (North Fork)|North Fork]]. It is a bustling place supported primarily as an army depot and a departure point for trade and adventure in the [[Marches of Enford]]. 

%% A few notes:
* Undecided if there is a bridge or just a good fording spot / ferry over the river
* Badly suffered during the undead attacks by a caravan of skeletons lead by a mummy or three
* Very military outpost vibe, but unlike say the Roman camps along the Danube, there isn't a Germanic population nearby. The marches have only slowly been repopulated.

Otherwise not much has been invented although it will eventually be a key place in the Cleenseau campaign so be cautious about putting lots of stuff here
%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Enford", "language": "unknown", "pronunciation": "EN-ford", "status": "proposed", "notes": "Preferred proposal from the English analogue available for Sembaran in [[Languages]]: short e, pronounced n, ordinary English ford with final d, and initial stress. French influence could nasalize En and weaken the final consonant; the name’s language and exact phonology are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern garrison and trade functions; the visible account omits the damage and rebuilding reported in late January DR 1720 and needs a human update disposition.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name and temporal metadata; preserved header versions, human attestations, and non-lint statuses.
- Added the required single-location map skeleton, leaving its unknown locator blank.

### Validated judgments
- No additional validated judgments.

### Editorial assessment
**Underdeveloped** — The visible garrison-town description omits the durable damage, temporary abandonment, and beginning of rebuilding established by the public Enford letter. The smallest useful scope is one dated paragraph on the late-January DR 1720 state, followed by a human choice about updating or preserving the earlier description.

### Open findings

- [ ] **Warning — coverage.later_material_change:** [[Letter from Enford]] reports that the town was abandoned to undead, troops retook it at heavy cost, and much of it needed rebuilding in late January DR 1720. This materially changes the bustling-depot account. Candidate: “During the undead attacks of DR 1720, Enford was abandoned as many inhabitants fled to nearby fortified manors. Soldiers retook the town at heavy cost, and rebuilding began in late January.” Incorporate that dated state and review the viewpoint, defer it for a human game-update disposition, or explicitly preserve the earlier account; the later completion of rebuilding is not established.
- [ ] **Warning — metadata.names_unresolved_status:** Review the persistent proposed pronunciation `EN-ford`. The preferred English adaptation from the Sembaran analogue in [[Languages]] uses short e, pronounced n, ordinary ford with final d, and initial stress. A French-influenced reading could nasalize En and weaken the final consonant; the name’s language and exact phonology remain unestablished. Accept it by adding `pronunciation: EN-ford` to frontmatter and marking the entry documented, or revise the persistent proposal.
- [ ] **Warning — metadata.map_location_missing:** The required settlement map block now contains `{map: world, locator: }`. A human must supply Enford’s verified world-map locator; leave it blank until established.
%%^End%%
