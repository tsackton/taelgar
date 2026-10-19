---
headerVersion: 2023.11.25
lintedAt: "2026-10-19T00:14:58-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: the}
tags: [status/cleanup/text, group, status/check/lint]
typeOf: clan
ancestry: dwarven
name: Ferrystone Clan
whereabouts: Barony of Aveil
dm_owner: none
dm_notes: none
POV: modern
---
# The Ferrystone Clan
>[!info]+ Information  
> A [[Dwarves|dwarven]] clan  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

A fairly prominent dwarven clan with longstanding ties to [[Rinburg]] and [[Aslain]], known since at least the [[Third Hobgoblin War (Sembara)|hobgoblin wars]] for their work building with recovered stones from ruins.

%% 
dwarven clan in Rinburg and Aslain,; have a small clanhouse in Aslain and larger buildings in Rinburg
important  / connected enough to have sent 2 of their members from Rinburg to Aslain to get news when there was little news of the north in Rinburg
from game intro:
- The Ferrystones, a dwarven clan, a group of whom are staying at the Resting Ox. They are important in Rinburg, and might have some useful information to share (and see Bolgrim and Kazak above)

Prominent enough that a clan member was brought in during an investigation into a ruined temple for their expertise in ruins
%%

### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2Fr> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```

%%^Metadata:names:v1%%
- {name: Ferrystone Clan, language: Common, status: documented, notes: "[[Bolgrim Ferrystone]] and [[Kazak Ferrystone]] identify Ferrystone as a Common rendering; the displayed clan name has transparent English pronunciation."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern clan identity, regional ties, and masonry reputation; the reference to the hobgoblin wars supplies historical depth without fixing the article to that period.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering.
- Added persistent name metadata, recording the Common rendering documented in [[Bolgrim Ferrystone]] and [[Kazak Ferrystone]]; the transparent clan name needs no pronunciation guide.
- Added `POV: modern` and a broadly modern temporal-coverage statement.

### Validated judgments
- The concise visible account adequately identifies the clan, its regional ties, and its masonry specialty; [[Aslain]], [[Bolgrim Ferrystone]], and [[Kazak Ferrystone]] corroborate that reference role.
- `status/cleanup/text` is supported by the remaining mixed draft comment and its unresolved public/private disposition; the tag is preserved.

### Open findings

- [ ] **Suggestion — editorial.public_material_candidate:** The opening of the shared comment records a small clanhouse in Aslain and larger buildings in Rinburg, a coherent institutional detail that would make the clan's two-town presence more useful. The consulted public notes confirm its ties to both towns but do not independently establish those premises, so adoption requires human judgment. Candidate: `The clan maintains a small clanhouse in [[Aslain]] and larger buildings in [[Rinburg]].` If adopted, remove that resolved draft fragment and the repeated general identity/masonry statements; keep any needed provenance in a concise source comment. The Resting Ox encounter, news-gathering trip, and temple-investigation appearances belong in their campaign or individual records and need not become clan history.
%%^End%%
