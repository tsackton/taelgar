---
lintedAt: "2026-10-20T07:22:39-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: watershed
name: Teft Watershed
whereabouts:
  - {type: home, location: Greater Sembara, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Teft watershed drains northwestern [[Sembara]] into the [[Western Gulf]]. Its principal river, the [[Teft]], gathers swift mountain waters from the [[Sentinel Range|Sentinels]] before plunging through the [[Great Chasm]] on its way to the sea north of [[Embry]]. Few of the rivers in this watershed are navigable, and the Teft and its tributaries often function as barriers to movement and serve as borders. 

%%^Campaign:none%%

### Mapped rivers

Mapped rivers of the Teft Watershed:

[[Teft]]: 
source: 10.10.B18
end (ocean): 11.11.H.20

[[Berze]]:
source: 10.10.D.03
end (Teft): 10.10.E.09

[[Vilna]]:
source: 10.10.E.11
end (Teft): 10.10.E.09

[[Selgrava]]:
source (Breva): 10.10.G.23
end (Teft): 10.11.B.02

Unnamed 1:
source (Breva): 10.11.B.17
end (Teft): 10.11.B.16

Unnamed 2:
source (Breva): 10.11.E.11
end (Teft): 10.11.F.07

Unnamed 3:
source (Aine Hills): 11.11.D.01
end (Teft): 11.11.D.14

There are probably at least two missing rivers:

Approximately source (Braebin): 10.11.I.03, end (Teft): 11.11.H.05
Approximately source (Sembara): 11.11.E.14 end (Teft): 11.11.H.10

## Places in the Teft Watershed

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
- {"name": "Teft Watershed", "language": "unknown", "pronunciation": "TEFT WAW-ter-shed", "status": "proposed", "notes": "Complete-form proposal combines the accepted TEFT in [[Teft]] with ordinary English watershed. The river name is documented as Sembaran there; the compound form’s language and the added descriptor’s reading remain unconfirmed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference geography; no narrower temporal reading position is required.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter where needed and recorded the article’s broadly modern POV with persistent temporal coverage.
- Added an explicit subject name where absent and a persistent primary name entry.
- Corrected “There is probably at least two missing rivers:” to “There are probably at least two missing rivers:” (objective grammar).

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm or revise `TEFT WAW-ter-shed` in `Metadata:names:v1`. Complete-form proposal combines the accepted TEFT in [[Teft]] with ordinary English watershed. The river name is documented as Sembaran there; the compound form’s language and the added descriptor’s reading remain unconfirmed. If accepted, copy the accepted primary pronunciation to frontmatter and mark the entry `documented`; preserve uncertainty until that decision.
%%^End%%
