---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [power, status/check/lint]
typeOf: archfey
gender: male
name: Lord Sorven
affiliations:
  - {org: Emberwine, type: leader, title: Master}
whereabouts: Sunwine Hall
dm_owner: tim
dm_notes: none
POV: modern
---
# Lord Sorven
>[!info]+ Information  
> An archfey (he/him)  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

The ruler of [[Emberwine]], known as the Master of the Revels, the Keeper of the Dance, and the Warden of the Endless Song. 

%%SECRET[v2:956aafa4687103cbbdd2883f3990cb1b]%%

%%^Metadata:names:v1%%
- {"name": "Lord Sorven", "role": "primary", "language": "unknown", "pronunciation": "lord SOR-ven", "status": "disputed", "notes": "Frontmatter and heading use Sorven; Sunwine Hall and Session 120 (DuFr) use Soven. Pronunciation is a cautious spelling-based reading, with initial personal-name stress; neither spelling nor pronunciation is accepted by this entry."}
- {"name": "Lord Soven", "role": "alternate spelling", "language": "unknown", "pronunciation": "lord SOH-ven", "status": "proposed", "notes": "Spelling appears in Sunwine Hall and Session 120 (DuFr). Cautious spelling-based pronunciation with long o and initial personal-name stress; source language and in-world phonology are unestablished."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern reference to the archfey ruler of Emberwine; the visible article does not depend on the dated encounter in DR 1749.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added persistent name and temporal-viewpoint metadata.

### Validated judgments
- The visible ruler-and-epithets entry is sufficient for its bounded reference role.
- Local-only evidence and the SECRET block were reviewed; no private contents were added to the shared note.

### Open findings

- [ ] **Warning — identity.name_conflict:** The frontmatter and heading say “Lord Sorven,” while [[Sunwine Hall]] and the narrative of [[Session 120 (DuFr)]] name the same ruler “Lord Soven.” Confirm the intended spelling. If Soven is intended, use `name: Lord Soven` and `# Lord Soven`; preserve the filename and resolve the two name entries together.

- [ ] **Warning — metadata.names_unresolved_status:** The name block records unresolved spelling and pronunciation. Pending the spelling decision, the cautious proposals are `lord SOR-ven` for Sorven and `lord SOH-ven` for Soven: initial stress on the personal name, with the written r retained only in Sorven and a long o proposed in Soven. No language-specific rule or recorded public pronunciation was found. Confirm a reading, copy the accepted primary value to frontmatter, and mark the accepted entry documented.
%%^End%%
