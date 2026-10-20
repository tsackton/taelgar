---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: settlement
typeOfAlias: village
campaignInfo: null
population: 308
name: Dallet
pronunciation: da-LEH
whereabouts: Barony of Aveil
dm_owner: mike
dm_notes: color
POV: 1720s
---
# Dallet
*(da-LEH)*
>[!info]+ Information  
> pop. 308  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A pastoral village known for its sheep and the first village east of [[Beury]] along the [[Enst]]. It is built about 500 feet north of the main road, and has three notable buildings: the large manor house, a blacksmith, and a mill. The area east of Dallet along the [[Enst]] is good pasture, although there are no river crossings here and the area south of the [[Enst]] is largely unpopulated scrublands.

It is a common stopping spot for travelers, who generally prefer to cross the [[East Bog]] in a single day. 

The current lord is Lady [[Elodie Blanchard]]. 

%% Impact of Undead:
Jean Luc responds: "A few days ago out in the pastures to the north the dead rose. Mostly two packs of dead wolves, come alive again, but lead by a skeletal warrior with a sword". He shudders. "May the Father's words reach the Night Queen and keep this from happening again. I feel a sense of anger from him, like this is not the will of the Divine. Anyway, the sheep - and to our great sorrow, several of the herder boys and girls out watching them -- were overwhelmed.  Lady Blanchard's household guard drove them off, but with heavy losses - five of them died."

People are scared for their livelihoods with so much livestock dead, and no one quite knows if they are safe to butcher. So we debate. The Father's guidance has been unclear on this, I fear"
%%

_Distances:_
* to [[Cleenseau]], 20 miles
* to [[Beury]], 15 miles
* to [[Champimont]], 13 miles
* to [[Rinburg]], 40 miles

%%^Metadata:names:v1%%
- {"name": "Dallet", "language": "unknown", "pronunciation": "da-LEH", "status": "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s pastoral village account under Lady Elodie Blanchard; the visible article does not incorporate the hidden description of the January undead losses.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Recorded supported primary-name metadata without changing accepted frontmatter pronunciation; normalized frontmatter formatting.
- Recorded the article viewpoint and concise temporal coverage in persistent metadata.
- Corrected 3 objective spelling, grammar, or punctuation defects.
- Added the required typed settlement map entry, leaving its unsupported locator blank for human completion.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.map_location_missing:** The required settlement map entry has `map: world` and a blank `locator`; no supported world-map coordinate was established by this review. Supply the verified locator in `Metadata:map:v1`, retaining the existing entry rather than adding a second one.

- [ ] **Suggestion — editorial.public_material_candidate:** The ordinary comment headed `Impact of Undead`, particularly Jean Luc's account of the destroyed sheep, young herders, and five dead household guards, contains a developed account of a consequential village event absent from the visible article. Consider this public-safe addition after confirming adoption: `During the [[Undead Attacks in Sembara|undead attacks of DR 1720]], Dallet suffered heavy losses among its sheep and young herders. Lady [[Elodie Blanchard|Blanchard]]'s household guard drove off the attackers but lost five soldiers.` This explains the local consequences without reproducing the dialogue or its divine speculation. Keep any still-useful encounter voice and unresolved religious interpretation in a separate hidden comment; do not promote that remainder.
%%^End%%
