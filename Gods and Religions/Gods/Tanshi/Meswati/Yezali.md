---
lintedAt: "2026-10-19T10:39:23-04:00"
lintVersion: "3.5"
tags: [power, religion/tanshi, status/check/lint]
typeOf: tanshi
name: Yezali
aliases: [Aaviskar]
pronunciation: yeh-ZAH-lee
affiliations:
  - {org: Meswati, type: primary}
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The spirit of the hunt, the moon, and the night. Particularly attracted by offerings from a fresh hunt. 

Trapped in a shadow demi-plane after the defeat of [[Cha'mutte]] in the [[Great War]], and thought dead by the Deno'qai, considered one of the [[Meswati]], the lost tanshi. 

%%^Campaign:dufr%%
Survived, however, in the demi-plane, and became associated with [[Delwath]], calling themselves Aaviskar. Freed finally by [[Delwath]] in his [[Session 53 (DuFr)|adventures]] in the [[Forest of Nightmares]].  
%%^End%%

%%^Metadata:names:v1%%
- {name: Yezali, language: unknown, pronunciation: yeh-ZAH-lee, status: documented}
- {name: Aaviskar, role: alias, language: unknown, pronunciation: AH-viss-kar, meaning: the Shadow, notes: "The account of Delwath's sacrifice in [[Delwath]] records the forgotten name and the adopted identity as the Shadow. The pronunciation is a cautious spelling-based proposal: aa as ah, i as in hiss, hard k, and initial stress; no name-specific pronunciation or established source language was found.", status: proposed}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern domains and Great War history; the campaign-scoped paragraph includes Yezali's release on DR 1748-10-08, but that later event is not yet date-filtered.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and affiliation formatting; added `POV: modern` and persistent temporal guidance.
- Recorded the accepted Yezali pronunciation and the documented Aaviskar alias, with an explicitly proposed alias pronunciation, in `Metadata:names:v1`.

### Validated judgments
- [[Research from Kassi]] supports the domains and fresh-hunt offerings. The note already identifies the central imprisonment, patron relationship, and release; incidental later campaign appearances do not require a running history here.
- Private-source recovery candidates remain in the private handoff; the human `dm_notes` attestation is unchanged.

### Open findings
- [ ] **Warning — correctness.cross_note_conflict:** The second paragraph says Yezali was trapped “after the defeat of Cha'mutte” and “thought dead by the Deno'qai.” [[Meswati]] places the loss of the six tanshi in the Great War battles and says the northern Deno'qai believed them imprisoned, because they did not believe tanshi could be killed. [[Session 53 (DuFr)]] independently records Ninu's account of that belief; [[Session 54 (DuFr)]] identifies Yezali's fall with the Battle of Darkfire. Confirm the intended chronology and belief rather than silently adopting the older wording. A bounded replacement is: `During the [[Great War]], Yezali was trapped in a shadow demi-plane at the Battle of Darkfire. Among the northern Deno'qai, Yezali was counted among the [[Meswati]], the lost tanshi believed imprisoned by [[Cha'mutte]].`
- [ ] **Warning — temporal.undated_state_change:** The release sentence has no date boundary and links to [[Session 53 (DuFr)]], which records preparation for the rescue. [[Session 54 (DuFr)]] records Yezali's release on DR 1748-10-08, when Delwath and his companions destroyed the armband at the Battle of Darkfire. To retain the broader reference POV while preventing the later outcome from appearing in earlier views, replace only the final sentence inside the existing `Campaign:dufr` block with the following dated passage; retain the existing campaign wrapper. This changes filtered visibility and requires human approval.

```markdown
%%^Date:1748-10-08%%
Freed finally by [[Delwath]] in his [[Session 54 (DuFr)|adventures]] in the [[Forest of Nightmares]].
%%^End%%
```

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed alias pronunciation `AH-viss-kar` in `Metadata:names:v1`. The spelling and the “Shadow” identity are documented in [[Delwath]], but no accepted pronunciation or established language for this form was found. The proposal is deliberately spelling-based: aa as ah, i as in “hiss,” a hard k, and initial stress; the vowel values and stress remain uncertain. If accepted, mark that alias entry `documented`; otherwise supply the preferred alias pronunciation. Preserve the accepted primary `yeh-ZAH-lee` pronunciation.

### DM evidence
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Delwath Solo Arc/Magic Items - Delwath Solo Arc]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Delwath Solo Arc/Main Quest/Battle of Darkfire]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Solo Arcs (Session 51-60)/Delwath Solo Arc/Tanshi - Delwath Solo]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 34]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 38]]
- [[_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Player Characters/Delwath (OneNote)]]
%%^End%%
