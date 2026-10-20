---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
displayDefaults: {wPastHome: "A former <ancestry:sx> <typeof:UA> of <origin:1>", dPastHasStart: "Existed <startDate> - <endDate>, <end> after <length>", endStatus: "conquered by [[Lord Umbraeth]]", wSecondary: "Now part of <secondary:2>"}
tags: [place, status/check/lint]
typeOf: extraplanar domain
typeOfAlias: realm
ancestry: fey
created: 1050
destroyed: 1570
name: Refuge of the Gossamer Veil
whereabouts:
  - {type: home, location: Amberglow, end: 1570}
  - {type: secondary, location: Duskmire}
dm_owner: mike
dm_notes: none
POV: modern
---
# The Refuge of the Gossamer Veil
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

%% dates in metadata are approx %%

The Refuge of the Gossamer Veil was a hidden redoubt in [[Amberglow]], remembered in stories as one of the last pockets of safety after the realm began to fade after [[Cloudspinner]]'s disappearance. 

%%^Campaign:clee%%
The Refuge of the Gossamer Veil was home to [[Greymalkin]], who [[Greymalkin's Story|recounted]] being born there in the years before the [[Great War]], and serving beside [[Aelirios Sunblade]] in its defense. In time, though, [[Lord Umbraeth]] coveted the Refuge and attacked; Aelirios fell, and the Gossamer Veil was lost. Greymalkin survived only to have his wings shorn, and to carry the memory of the Refuge’s fall into later years.
%%^End%%

%% 

See also:
- [[Amberglow]]
- [[Greymalkin]]
- [[Greymalkin's Story]]
- [[Aelirios Sunblade]]
- [[Lord Umbraeth]]
- [[Duskmire]]
- [[Amberlight]]
- [[Aelirios Sunblade]]

Dates of founding and destruction in metadata are not based on any canonical information  and could be changed. 

Details in [[Greymalkin's Story]] should be considered canonical, subject to the fact that Greymalkin suffered a lot of trauma and could be a (slightly) unreliable narrator.

The relationship between the Gossamer Veil and Cloudspinner, other than "loyalists", is not clear and it is intended to not really matter. The only future plans for the Refuge specifically is an eventual quest to find Greymalkin's wings, where having some clues and an adventure in Duskmire or Amberglow is plausible. But this adventure is not written and is targeted for 10th level or so, and can easily accomodate future worldbuilding around fey politics

Note the refuge is presumably part of the larger set of strongholds established by Cloudspinner's allies in the years after her disappearance, including [[Redsun Watch]] and [[Night's Edge Keep]]. 

Aeririos presumably possessed an [[Amberlight]], which may have been connected to the creation of the [[Lantern of the Bright Hearth]]

%%

%%^Metadata:names:v1%%
- {"name": "Refuge of the Gossamer Veil", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a modern retrospective account of the lost refuge, including Greymalkin's DR 1720 recollection; the precise founding and conquest dates are explicitly unestablished.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter while preserving the original dates, whereabouts and display controls; added the explicit name.
- Added primary-name metadata with unknown in-world language and no unnecessary pronunciation guide.
- Added a broadly modern retrospective POV and a note distinguishing the DR 1720 recollection from the unestablished exact lifecycle dates.

### Validated judgments
- [[Greymalkin's Story]] supports the hidden refuge, its defenders and conquest as an attributed, potentially imperfect recollection. The existing campaign section already covers the defining fall; no speculative Amberlight history was adopted.
- The short date comment and longer planning comment were reviewed. The latter mixes source pointers, explicit uncertainty and future plans, rather than a developed public account requiring adoption or deletion.

### Open findings

- [ ] **Warning — metadata.unsupported_lifecycle_dates:** The article has `created: 1050`, `destroyed: 1570`, and an Amberglow whereabouts end of `1570`, but its own long comment explicitly says the founding and destruction dates are not based on canonical information. [[Greymalkin's Story]] supplies only a relative pre-Great-War history, not those exact years. Choose to adopt and justify the approximate dates explicitly, replace them with independently supported bounds, or remove the unsupported exact values together. For the removal option, the bounded YAML candidate is `created: null`, `destroyed: null`, and the first whereabouts entry `{type: home, location: Amberglow}`; retain the conquest and uncertainty in prose and review the date-dependent display text. No year was guessed or automatically removed.
%%^End%%
