---
lintedAt: "2026-10-20T11:28:01-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/wip, status/check/lint]
typeOf: region
name: Nevos and Apporia
whereabouts:
  - {type: home, location: Taelgar, linkText: in}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

%% Status:
* [ ] In world intro
* [ ] Map
* [ ] Topography
* [ ] Civilizations and Culture
* [ ] History
* [ ] Climate
* [ ] Climate - Real World
* [x] DM Notes
%%

{intro text}
## Map

{link to leaflet map of region}
## Topography and Major Features
_See more: {links}_

{descriptive text of topography and major features}
## Civilizations and Cultures
_See more: [[Illoria]]_

The pirate realm of [[Illoria]] is the major culture of the [[Nevos Sea]], although since its conquest by the [[Chardonian Empire]] the southern (unconquered) islands have splintered somewhat. Historically, [[Castrella]] was a major realm in the region, although it has been part of the [[Chardonian Empire]] for over a hundred years now.

%%
Elves:  None
Dwarves:  ??
Lizardfolk: ??
Humans:  [[Illoria]] + ??
Stoneborn:  ??
Hobgoblins: ??
Dangerous Wildernesses: Yes
%%
## Climate

{descriptive in world text about climate}

%%^Campaign:None%%

{real world climate analogs and inspiration}

%%^End%%

## Major Historical Eras
_See more: {links}_

{descriptive text of major era}

%%^Campaign:None%%
## DM Notes and Meta
_See also: {links to lists, e.g. Places in Region}_

*Canonical Development and Constraints:* The general vibes of Illoria are canonical. There is some significant post-Great War historical development, mostly concerning Dunmar and Apporia, that involves Illoria and needs to be considered in any future developments concerning Illoria. 

*Brainstorming and Potential Canon:* The exact cultural heritage of [[Illoria]] is unclear, as is its history during the [[History of the Drankorian Empire|Drankorian Era]].

*Needs Development:* Illoria itself lacks anything more than some basic vibes, and the Emerald Bay coast of the Apporian Peninsula, outside the terminus of the [[Old Chardon Canal]], is nearly entirely blank. The southern and eastern coasts of the Apporian Peninsula is plausibly either Illorian or something mysterious, but has not been canonically developed at all. The overall history of this region, at least outside the intentionally blank areas, could use development building on the existing fragments. 

*Intentionally Blank:* On the Apporia Peninsula, the interior and western coasts are intentionally left blank and mysterious

*Adventures:* Illoria has been at the edge of several Dunmari Frontier adventures, but only two sessions were actually set in the Nevos Sea, and primarily involved traveling to and then through the [[Old Chardon Canal]]. The merfolk arc of the Dunmari Frontier was partially set on the north coast of Apporia. 

*Important Places in Staging:* None.

%%^End%%

%%^Metadata:names:v1%%
- {name: Nevos and Apporia, role: primary, language: unknown, pronunciation: "NEH-vohs and a-POHR-ree-ah", status: proposed, notes: "Combines a cautious spelling-based NEH-vohs (initial stress, short e, v as written, final os read ohs) with the documented a-POHR-ree-ah in [[Apporia]] and ordinary English and. The full regional name and its source language are not separately attested."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern regional geography and political relationships, after the Chardonian conquest of Illoria; the historical and climate overview sections remain unfinished.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the objective typo “have splinted somewhat” to “have splintered somewhat.”
- Normalized frontmatter formatting and added the explicit regional name.
- Added persistent name metadata with a proposed complete pronunciation, a modern POV, and a temporal-coverage note.

### Validated judgments
- `status/wip` is supported by the unfinished regional template and is retained.
- The interior and western Apporian coasts are intentionally left largely undeveloped in the note's existing guidance; completing the overview does not require inventing those areas.

### Editorial assessment
**Underdeveloped** — The introduction and central topographic, historical, and climate sections are placeholders. The visible culture paragraph does not orient the reader to the sea and peninsula or summarize their established history and climatic contrasts. The smallest useful completion is a defined regional scope and short, linked geography, history, and climate summaries from existing sources, preserving uncertainty and intentionally blank areas rather than developing them.

### Open findings

- [ ] **Warning — coverage.established_fact_missing:** The introduction, “Topography and Major Features,” “Major Historical Eras,” and “Climate” contain only placeholders despite established material in [[Apporia]], [[Emerald Bay]], [[Old Chardon Canal]], [[Illoria]], and [[Castrella]]. Add bounded summaries. Intro/geography candidate: “This region includes the [[Nevos Sea]], the islands of [[Illoria]], and [[Apporia|the Apporian Peninsula]]. Apporia stretches west between the [[Gulf of Chardon]] to the northeast, [[Emerald Bay]] and the Nevos Sea to the southeast, and the [[Endless Ocean]] to the west. The [[Old Chardon Canal]] crosses the base of the peninsula, connecting the two sides.” Historical candidate: “After the fall of Drankor, [[Castrella]] became a major maritime power. Following the [[Great War]], Illorian pirates controlled much of what is now [[Portalia]] and parts of [[Cedrano]]. The [[War of the Dark Rift]] devastated the Apporian coast; Chardon later consolidated control over Portalia and Cedrano.” A minimal sourced climate statement is: “The northern plain of [[Raziolo]] has hot, dry summers and mild winters.” These statements summarize the existing [[Apporia]] account; they do not establish a uniform climate for the whole region or fill the intentionally blank coasts and interior. Complete or remove unused template scaffolding as part of that bounded human edit.
- [ ] **Warning — metadata.names_unresolved_status:** The name block proposes **NEH-vohs and a-POHR-ree-ah**, combining a cautious spelling-based reading of Nevos with the documented **a-POHR-ree-ah** in [[Apporia]] and ordinary English “and.” Nevos has no established language or explicit pronunciation in the reviewed sources; the full compound is also unattested. Confirm or replace the complete proposal. If accepted, set frontmatter `pronunciation: NEH-vohs and a-POHR-ree-ah` and mark the entry documented; retain the unknown compound language unless supported.
- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The real-world-climate placeholder block and “DM Notes and Meta” block both open with `%%^Campaign:None%%`; the adopted private sentinel is `%%^Campaign:none%%`. Confirm the intended publication filtering, then replace both opening markers with that exact lowercase form. The markers were preserved because they control visibility.
%%^End%%
