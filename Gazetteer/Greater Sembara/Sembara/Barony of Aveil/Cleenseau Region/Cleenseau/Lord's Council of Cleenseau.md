---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T00:45:23-04:00"
lintVersion: "3.5"
displayDefaults: {boxInfo: ""}
tags: [group, status/check/lint]
typeOf: council
name: "Lord's Council of Cleenseau"
whereabouts: Cleenseau
dm_owner: mike
dm_notes: none
POV: 1720
---
# The Lord's Council of Cleenseau
>[!info]+ Information  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The Lord's Council is an advisory group to the lord of [[Cleenseau]], currently [[Rosalind Essford]] for all practical purposes.  It is advisory, but Rosalind convenes it before important decisions and respects the advice she receives. It consists of:

* [[Marigold Stonebridge]], the owner of [[The Crossroads Inn]], as an observer in the tradition of the Sembaran Royal Council
* [[Jonathon Henwyn]], the steward
* [[Ames Benthey]], the captain of the household guard 
* [[Annet Bybet]], the chamberlain
* [[Anselm]], the administrator of the Temple of the Warlord
* [[Nicholas Wysson]], the magistrate

[[Ida Rosfeld]], the captain of the [[Army Garrison of Cleenseau]], often attends and provides advice, but is not a formal member.

%%^Campaign:None%%
### Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Lord's Council of Cleenseau", "language": "unknown", "pronunciation": "LORDZ KOWN-sil uv Klen-sew", "status": "proposed", "notes": "Complete-form proposal uses the accepted Klen-sew in [[Cleenseau]], with the ordinary English possessive Lords, Council, and of. The complete assembled form and its source language are not independently attested."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early DR 1720 council portrait centered on Rosalind Essford's practical leadership and the listed offices; it does not establish later changes to council membership.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter field order and collection formatting while preserving parsed values.
- Added persistent primary name metadata, preserving existing accepted pronunciations and leaving newly composed pronunciations proposed.
- Recorded the supported article viewpoint and concise temporal-coverage metadata.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Accept or revise the proposed complete pronunciation `LORDZ KOWN-sil uv Klen-sew` in `Metadata:names:v1`. Complete-form proposal uses the accepted Klen-sew in [[Cleenseau]], with the ordinary English possessive Lords, Council, and of. The complete assembled form and its source language are not independently attested. If accepted, mark the entry `documented` and copy the accepted complete pronunciation to frontmatter; otherwise revise the persistent proposal. The name's language remains `unknown`.

- [ ] **Suggestion — syntax.noncanonical_campaign_block:** The existing block before “Members” opens with `%%^Campaign:None%%`; the current validator and [[Campaign Registry]] specify lowercase `Campaign:none`. Proposed replacement opener: `%%^Campaign:none%%`, retaining the existing payload and matching closing marker. Equivalent filtered visibility has not been verified, so this normalization remains proposal-only; confirm visibility and approve the change before applying it.
%%^End%%
