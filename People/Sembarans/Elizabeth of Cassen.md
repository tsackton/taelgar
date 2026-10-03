---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T09:37:56-04:00"
lintVersion: "3.5"
tags: [person, status/check/lint]
species: human
ancestry: Sembaran
gender: female
name: Elizabeth of Cassen
whereabouts:
  - {type: home, location: Champimont}
  - {type: home, location: Cassen}
  - {type: away, location: Rinburg, start: 1720-01-08, end: 1720-02-03}
  - {type: away, location: Cleenseau, start: 1720-02-06, end: 1720-02-10}
knownTo: [clee]
dm_owner: none
dm_notes: none
POV: 1720
---
# Elizabeth of Cassens
>[!info]+ Biographical Info  
> A [[Sembara|Sembaran]] [[Humans|human]] (she/her)  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

![[elizabeth-of-cassen.png|right|420]]A middle aged woman, who became a soldier in her later life. She worked for the lord of [[Cassen]] until the [[Undead Attacks in Sembara]] decimated her village.

Her story is [[Elizabeth of Cassen's Story|here]].

%%^Metadata:names:v1%%
- {name: "Elizabeth of Cassen", language: "Sembaran", pronunciation: "ih-LIZ-uh-beth uv KASS-en", status: "proposed", notes: "The English strand of Sembaran in [[Languages]] supports the ordinary Elizabeth reading and short-a, first-stressed KASS-en. A French-influenced alternative is eh-lee-zah-BET uv kah-SAHN, with th simplified to t and the final en of Cassen nasalized; the English reading is preferred because Elizabeth is presented in its familiar English form. The village note supplies no accepted pronunciation, so the complete name remains proposed."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1720 portrait of Elizabeth after the attack on Cassen, with dated travel through Rinburg and Cleenseau in January and February.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter and added supported name and temporal metadata.
- Recorded the existing filename identity in name metadata.
- Added knownTo: [clee] from the recorded campaign interaction or the campaign’s known-NPC index.
- Corrected “solider” to “soldier”.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** The name entry remains proposed. Candidate pronunciation: `ih-LIZ-uh-beth uv KASS-en`. The English strand of Sembaran in [[Languages]] supports the ordinary Elizabeth reading and short-a, first-stressed KASS-en. A French-influenced alternative is eh-lee-zah-BET uv kah-SAHN, with th simplified to t and the final en of Cassen nasalized; the English reading is preferred because Elizabeth is presented in its familiar English form. The village note supplies no accepted pronunciation, so the complete name remains proposed. Accept or revise this reading; if accepted, copy it to frontmatter and mark the existing primary name entry documented.

- [ ] **Suggestion — identity.inconsistent_display_name:** The heading says “Elizabeth of Cassens,” while the filename, [[Cassen]], and [[Elizabeth of Cassen's Story]] use Cassen. Candidate heading: `# Elizabeth of Cassen`. Confirm this name correction; the linter has preserved the existing heading.
%%^End%%
