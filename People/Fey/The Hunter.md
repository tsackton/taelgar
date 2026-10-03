---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T13:42:28-04:00"
lintVersion: "3.5"
tags: [status/stub, person, status/check/lint]
species: fey
name: The Hunter
whereabouts:
  - {type: home, location: Duskmire}
  - {type: away, location: Ashcombe, start: "1719-01", end: 9999}
knownTo: [clee]
dm_owner: mike
dm_notes: important
POV: 1720s
---
# The Hunter
>[!info]+ Biographical Info  
> A [[Fey|fey]]  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

His real name is Kiastíōn Hēmiárktos (_Kee-as-TEE-ōn_ Hay-mee-ARK-tos)

%% 
an alias - he didn't give his name and I havent made it up
one of his kids:

![[the-hunter-bear-cub.jpg|200]]


![[the-hunter-fey-img2.jpg|left|400]]
![[the-hunter-fey-img1.jpg|left|400]]




















%%

%%^Metadata:names:v1%%
- {"name": "The Hunter", "language": "unknown"}
- {"name": "Kiastíōn Hēmiárktos", "role": "personal name", "language": "unknown", "pronunciation": "Kee-as-TEE-ōn Hay-mee-ARK-tos", "status": "documented", "notes": "The authored body explicitly supplies this personal name and pronunciation; the earlier drafting comment remains unresolved."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early DR 1720s reference frame for the named fey associated with Ashcombe; the very sparse article does not narrate the conflicts recorded in the Cleenseau sessions.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and collection formatting.
- Added supported campaign knowledge, primary name metadata, and persistent temporal viewpoint metadata.

### Validated judgments
- `status/stub` is supported: the visible article still lacks a useful account of the subject’s established role.
- The title needs no pronunciation; the authored personal-name pronunciation is preserved as documented metadata.
- Local dm_notes review is outside the applicable ownership gate for dm_owner: mike.

### Editorial assessment
**Underdeveloped**: the visible article identifies a personal name but omits the Hunter’s defining role as a hostile fey, his servants and captives, and his recurring conflict with the Heroes of Cleenseau. The smallest useful addition is a short identity-and-conflict paragraph grounded in the played records; a full encounter chronology is unnecessary.

- Discussion research: multiple indexed Worldbuilding notes discuss this subject. Use `_scripts/generate_worldbuilding_discussion_index.rb --query` with this note's path before developing the missing material.

### Open findings
- [ ] **Warning — coverage.established_fact_missing:** [[Cleenseau - Session 21]] records abduction, captives, and retreat; [[Cleenseau - Session 31]] records his later attempted abduction of Queen Elaine II. These establish his defining antagonist role, which the name-only body omits. Add a concise account such as: “The Hunter, whose personal name is Kiastíōn Hēmiárktos, is a fey adversary of the [[Heroes of Cleenseau]]. He held captives in a cave until the heroes freed them and forced him to retreat. In DR 1720 he later led an unsuccessful attempt to abduct Queen [[Elaine II]].” Keep the two events distinct and link the session records; this does not require a full campaign log.

- [ ] **Suggestion — editorial.stale_comment:** The ordinary comment says “I havent made it up” about his name, while the visible body explicitly names Kiastíōn Hēmiárktos. Confirm whether that drafting reminder is obsolete. If so, remove only “an alias - he didn’t give his name and I havent made it up” and retain the child/image staging material; otherwise clarify which part of the name remains undecided.
%%^End%%
