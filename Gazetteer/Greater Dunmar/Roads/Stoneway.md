---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {linkText: "on", ltPlace: "on", defArt: the}
tags: [place, status/check/lint]
typeOf: road
name: Stoneway
whereabouts: Dunmar
dm_owner: tim
dm_notes: color
POV: modern
---
# The Stoneway
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% some notes on features along the road that probably aren't worth their own pages but would be nice to record in OneNote %%

The Stoneway is the Dunmari name for the ancient Drankorian road that once connected [[Chardon]] and [[Isingue]]. It is wide enough for two wagons to pass, paved with massive, smooth stones, with drainage ditches on both sides for almost its entire length. It is heavily traveled for much of its length and serves as a key linkage between [[Karawa]] and [[Eastern Dunmar]], [[Tokra]], and [[Songara]], especially during the monsoons when mud and rain can make passage overland across the plains difficult at times. 

Since the [[Great War]] and the upheavals that followed, much of the road east of [[Gomat]] is in ruins: the [[Daraar Canyon]] cuts across the path of the Stoneway, and beyond it is in poor repair.

%%^Campaign:DuFr%%
About halfway between Tokra and Karawa, a three-mile segment of an old Drankorian aqueduct still exists, carrying a faded enchantment that amplifies the volume of water flowing over it. While it cannot create water out of thin air, a gallon of water poured into the aqueduct will grow to two gallons as it travels. 

[[Seeker]] built [[Session 33 (DuFr)|an earthen berm along these ruins]], to make access easier, so Dunmari can use it as a mini-oasis.
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {feature: Chardon, map: world, locator: 13.07.B09}
  - {feature: Isingue, map: world, locator: 14.11.F21}
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Stoneway", "language": "Dunmari", "status": "documented", "notes": "The article explicitly identifies Stoneway as the Dunmari name of the road; the displayed form uses ordinary English words and needs no pronunciation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern surviving road and post-Great-War damage, with a campaign-specific account of the aqueduct improvement made in June DR 1748; the historical endpoint metadata does not imply continuous modern passage.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Repaired the missing conjunction in the Great War sentence and the missing article/object in the aqueduct-improvement sentence.
- Normalized frontmatter and added the explicit name Stoneway.
- Added road endpoint metadata from the Chardon and Isingue map locators, plus name metadata and modern temporal metadata.

### Validated judgments
- Supplemental local sources under the older working label support the positive `dm_notes` attestation; no private contents were added to this report.
- Stoneway is explicitly identified as a Dunmari name; its ordinary English form needs no pronunciation.
- The map entries identify the road's stated historical endpoints; they do not claim that the entire route is passable today.
- The roadside-feature comment is an editorial reminder, not a hidden account.

### Open findings

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The aqueduct section begins with the recognized alias `Campaign:DuFr`. [[Campaign Registry]] requires lowercase `dufr`. Replace only the opening marker with the canonical lowercase campaign code while retaining the section, closing marker, and visibility intent. The marker was preserved because campaign filtering is visibility-sensitive.

### DM evidence
- [[_DM_/Secret Worldbuilding/Dunmar Notes]]
- [[_DM_/Secret Worldbuilding/History of Dunmar]]
- [[_DM_/Timelines/Old Timeline (Table)]]
- [[_DM_/Timelines/Unified Timeline From OneNote]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Karawa Redux (Sessions 17-18)/Session 18]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 1/Into the Wild - Part 1]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Rampaging Beasts (Session 1-3)/Session 2-3/Into the Wild Part 2]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Old Trade Road]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Road to Darba/Road to Darba]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 42]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Session 43]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 33]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 40]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Campaign Notes/OLD NOTES/Secrets of Karawa]]
%%^End%%
