---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [group, status/check/mike, status/check/lint]
typeOf: family
ancestry: halfling
name: Merriweathers
dm_owner: mike
dm_notes: none
POV: modern
---
```taelgar-header
```

%% check mike for tags, and if there is more to say %%

The Merriweathers are a notable halfling family in the [[Barony of Aveil]], especially plying the route along the [[Auberonne]] between [[Aslain]] and [[Rinburg]]. 

%% 

The family was involved in the exile of the old baron of aveil. (Reginald Rusebek) in that they found out about his embezzlement and he killed them to try to cover it up. It was the murder of several important halflings that led to his execution and his family scattering mostly voluntarily.

It is possible but not decided that this was all faked by the lich. If faked, the halflings did not know it was faked and are innocent dupes. Either way, they are, in 1720, reeling from a recent tragedy that killed 6-10 elders of the family, basically. 

From game intro:
- The Merriweathers, a halfling family in the area, who are apparently the family the old lord killed (Reginald Rusebek) to cover up his embezzlement. Fin (mentioned above) is one of them

%%

%%^Campaign:none%%
### Current Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2Fr> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Merriweathers", "language": "unknown", "pronunciation": "MERR-ee-weh-therz", "status": "documented", "notes": "The surname pronunciation MERR-ee-weh-ther is recorded in the frontmatter of [[Primrose Merriweather]] and [[Corrin Merriweather]]; this family plural adds the ordinary voiced z ending."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern description of the family’s trading region; the hidden tragedy and related campaign sources concern DR 1719–1720 and are not yet integrated into the visible account.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter without changing its existing values and added persistent name and temporal metadata.
- Added the filename-derived explicit name and preserved the accepted surname pronunciation from Primrose and Corrin in the family plural.
- Canonicalized the equivalent private campaign sentinel.

- Corrected “volunteerly” to “voluntarily” and the stray apostrophe in the plural family name in the shared comment.

### Validated judgments
- The comment’s possible lich manipulation remains unresolved development material; it is not a basis for naming the actual killer.

### Editorial assessment
**Underdeveloped**: the trading-route sentence omits the family’s consequential losses in the DR 1719 Rusebek scandal and the later uncertainty over responsibility. A short, attributed history paragraph is sufficient; no family origin story or invented explanation is required.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The visible account does not mention the family tragedy described in the shared comment and corroborated by [[Cleenseau - Session 27]], which recalls Merriweathers executed on false pretenses. [[Reginald Rusebek]] records the DR 1719 murder charges and the summer-1720 evidence suggesting he was framed. Add a bounded account without asserting the perpetrator: `In DR 1719, members of the Merriweather family were killed in a scandal attributed at the time to [[Reginald Rusebek]]. Evidence presented in the summer of DR 1720 later suggested that Rusebek had been framed.` Confirm the intended campaign/date visibility before adoption. Do not promote the comment’s uncertain victim count or conjectured lich explanation.
%%^End%%
