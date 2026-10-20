---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: watershed
name: Semb Watershed
whereabouts:
  - {type: home, location: Greater Sembara, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
---
# The Semb Watershed
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Semb watershed gathers the waters of the [[Semb]] and its tributaries, draining the highlands and foothills of [[Greater Sembara]] into the [[Western Gulf]]. In its upper reaches, the Semb flows past [[Lake Derwent]] in [[Ardlas]]; downriver, it becomes one of the principal waterways of Sembara.

The city of [[Embry]] stands above the Semb and serves as one of the great river ports of the Sembaran heartlands, where goods from upriver are gathered and traded.


%%^Campaign:none%%

### Mapped rivers

Mapped rivers of the Semb Watershed:

[[Semb]]:
source (Lake Derwent): 11.10.D.21
end (ocean): 11.11.I.08

Unnamed River 1:
source (Lavnoch): 10.10.F.05
end (Lake Derwent): 10.10.F.16

Unnamed River 2:
source (Sentinels): 11.10.A.21
end (Unnamed River 1): 10.10.F.16

Unnamed River 3:
source (Sentinels): 11.10.D.18
end (Semb): 11.10.D.22

Unnamed River 4:
source (Lavnoch): 10.10.H.04
end (Semb): 11.10.G.06

Unnamed River 5:
source (Lavnoch): 10.10.H.16
end (Semb): 11.10.G18

Unnamed River 6:
source (Aine Hills): 11.10.H.10
end (Semb): 11.11.B.07

Unnamed River 7:
source (Aine Hills): 11.10.I.22
end (Semb): 11.11.C.09

Unnamed River 8:
source (Braebein): 11.11.A.09
end (Semb): 11.11.A.03

Unnamed River 9:
source (Braebein): 11.11.A.20
end (Unnamed River 11): 11.11.B.21

Unnamed River 10:
source (Braebein): 11.11.A.19
end (Unnamed River 11): 11.11.A.24

Unnamed River 11:
source (Braebein): 11.11.D.03
end (Semb): 11.11.C.21

Mapped Lakes of the Semb Watershed:

[[Lake Derwent]]:
10.10.F.16, 10.10.F20, 11.10.D.13, 11.10.D.17, 11.10.D21

## Places in the Semb Watershed
```dataviewjs
const { util } = customJS
dv.table(["Place", "Type Of"], 
			dv.pages("#place")
				.where(f => util.inLocation(dv.current().file.name, f.file.frontmatter, dv.current().pageTargetDate) && (f.typeOf == "river" || f.typeOf == "waterway" || f.typeOf == "lake"))
				.sort(b => util.s("<maintype>", b.file))
				.map(b => [util.s("<name> (<pronunciation>)", b.file), util.s("<maintype>", b.file)]))
```

%%^End%%

%%^Metadata:names:v1%%
- {"name":"Semb Watershed","language":"unknown","pronunciation":"SEMB WAW-ter-shed","status":"proposed","notes":"Proposed using the English side of the Sembaran analogues in [[Languages]]: Semb is one syllable with short e and both final consonants; watershed has its ordinary English reading. The exact name language and accepted pronunciation are not established."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern basin geography and the river-port role of Embry; no narrower dated state is asserted.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and collection formatting while preserving parsed values.
- Added a persistent name entry, preserving recorded pronunciation and meaning and leaving unsupported language unknown.
- Recorded POV: modern and concise persistent temporal interpretation.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `SEMB WAW-ter-shed`. Proposed using the English side of the Sembaran analogues in [[Languages]]: Semb is one syllable with short e and both final consonants; watershed has its ordinary English reading. The exact name language and accepted pronunciation are not established. Confirm or replace this full-name proposal; if accepted, copy it to frontmatter and mark the existing entry `documented`.
%%^End%%
