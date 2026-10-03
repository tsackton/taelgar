---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T14:58:27-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
campaignInfo:
  - {campaign: clee, date: 1719-12-01}
born: 1693
gender: male
name: Guy de Varan
whereabouts:
  - {type: home, location: Evis}
  - {type: away, start: 1719-10-26, end: 1719-11-29, location: "Wakog's Camp"}
  - {type: away, start: 1719-11-29, end: 1719-12-01, location: "Bandit's Way"}
  - {type: away, start: 1719-12-01, end: 1719-12-10, location: Cleenseau}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1710s
---
# Guy de Varan
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (he/him)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`  
>> %%^Campaign:clee%% Seen by the [[Heroes of Cleenseau]] on December 1st, 1719 in [[Cleenseau]], the [[Manor of Cleenseau]], the [[Barony of Aveil]] %%^End%%

![[guy-de-varan-maseau.png|right|320]]A traveler and caravan expediter, he is relatively well-known along [[Bandit's Way]] as a man who can help find guards and organize supplies. The de Varan family is well-known in [[Duchy of Maseau|Maseau]] and was originally from far southern [[Isingue]] before the Great War. 

%%^Date:1719-10-30%%
He was captured by [[Wakog]] in the late fall of 1720, and his escape to [[Cleenseau]] was the trigger that led to the [[Battle Against Wakog]] and [[Wakog|Wakog's]] defeat.
%%^End%%

%%^Campaign:none%%
At times there have been rumors that he sometimes warns bandits of particularly lucrative caravans coming along the road. But these rumors are disputed, and even his biggest detractors are careful to note that even the caravans he supposedly targeted are never brutally attacked -- no deaths have been associated with these rumors.
%%^End%%

%% His story, which contains some color and background, is here [[Guy de Varan's Story]] %%

%%^Metadata:names:v1%%
- {"name": "Guy de Varan", "language": "unknown", "pronunciation": "gee duh vah-RAHN", "notes": "The southern Sembaran context favors the French analogue in [[Languages]]: Guy has hard g and ee, de has an unstressed schwa, and Varan has a nasal final an. RAHN is an English-readable approximation of that nasal vowel, not a released final n. In-world pronunciation is unrecorded.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a late-1710s portrait of Guy as an active caravan expediter, with his captivity and escape recorded in a dated layer; the prose and metadata dates require reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the primary name entry and the article’s POV and temporal-coverage note.
- Recorded supported campaign knowledge in `knownTo`.
- Corrected `the trigger that lead to` → `the trigger that led to`; `lucrative caravan's coming` → `lucrative caravans coming`.
- Normalized the existing private campaign sentinel to `Campaign:none`, preserving its enclosed material.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — correctness.cross_note_conflict:** The dated paragraph says Guy was captured in late fall 1720, while [[Guy de Varan's Story]], [[Cleenseau - Session 04]], and [[Cleenseau - Session 05]] place his captivity and arrival in DR 1719; the latter sources date his arrival to December 4, whereas this note’s `campaignInfo` and Cleenseau whereabouts begin December 1. Reconcile the dates together. Candidate prose: `He was captured by [[Wakog]] in late fall 1719, and his escape to [[Cleenseau]] helped prompt the [[Battle Against Wakog]] and Wakog’s defeat.` If the session chronology is adopted, use `campaignInfo: [{campaign: clee, date: 1719-12-04}]` and change the final whereabouts transition to December 4. The earlier capture and marching dates still need confirmation.

- [ ] **Suggestion — temporal.date_block_scope:** `%%^Date:1719-10-30%%` exposes the paragraph’s account of Wakog’s defeat before the battle on December 6 recorded in [[Cleenseau - Session 05]]. After the chronology is resolved, the smallest safe proposal is to change the enclosing marker for this complete retrospective paragraph to `%%^Date:1719-12-06%%`. This visibility change requires human approval and has not been applied.

- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `gee duh vah-RAHN`. The southern Sembaran context favors the French analogue in [[Languages]]: Guy has hard g and ee, de has an unstressed schwa, and Varan has a nasal final an. RAHN is an English-readable approximation of that nasal vowel, not a released final n. In-world pronunciation is unrecorded. Confirm or revise the pronunciation, then mark the entry documented and copy the accepted primary pronunciation to frontmatter.
%%^End%%
