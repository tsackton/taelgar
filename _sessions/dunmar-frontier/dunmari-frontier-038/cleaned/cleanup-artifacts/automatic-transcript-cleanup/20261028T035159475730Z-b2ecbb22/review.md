# Automatic transcript cleanup

Session: <code>dunmari-frontier-038</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 25 | 3 | 3 | 0 | 1 | 18 | 19 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>bhishma</code> | high | <code>u2471:m1</code> | <code>{{reshma}}</code> | <code>Bhishma</code> | The monk being sought belongs to the mystai of Bhishma; the order and Saka notes establish the divine name. | <code>Groups/Dunmari Mystery Cults/Order of the Awakened Soul.md</code>, <code>People/Dunmari/Saka.md</code> | no |
| <code>chardonian-scholar</code> | supported | <code>u2658:m1</code> | <code>{{cardone}}</code> | <code>Chardonian</code> | The copied scroll that prompted a journey to Darba belongs to the Chardonian scholar Servius. The demonym is strongly favored over Ardan, who supplies the copy; adjacent unmarked wording is preserved. | <code>People/Chardonians/Servius.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 35 (DuFr).md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 38 (DuFr).md</code> | no |
| <code>great-war-enemy</code> | high | <code>u2685:m1</code> | <code>{{Jamaat}}</code> | <code>Cha&#x27;mutte</code> | The Great War reference explicitly identifies the war against its established adversary; the reference note supplies the spelling. | <code>Events/1500s/Great War.md</code> | no |
| <code>illoria</code> | supported | <code>u2695:m1</code> | <code>{{elbow I}}</code> | <code>Illoria</code> | A proposed destination beyond Darba for the evacuated treasures strongly matches Illoria, explicitly listed as a possible refuge in the letter being discussed. | <code>Campaigns/Dunmari Frontier Campaign/Letters and Notes/Archives Letter.md</code>, <code>Gazetteer/Nevos and Apporia/Illoria.md</code> | no |
| <code>kaleha-assistant</code> | supported | <code>u2800:m1</code> | <code>{{ad varney}}</code> | <code>Uvani</code> | The speaker is Kaleha referring to her assistant, already encountered at the temple. The matching role and local session notes strongly support Uvani; no private characterization is used. | <code>_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 35.md</code>, <code>_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Tokra (Session 33-41)/Session 36.md</code>, <code>Worldbuilding/Tentative/Uvani.md</code> | no |
| <code>saka</code> | high | <code>u2971:m1</code> | <code>{{soccer}}</code> | <code>Saka</code> | The party plans to resume seeking the Bhishma master north of Tokra; the earlier session establishes Saka as that objective. | <code>People/Dunmari/Saka.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 35 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>letter-reading</code> | <code>u2668:m1</code> | <code>{{garden Carson}}</code> | <code>Kharsan</code> | The source letter has a Kharsan reference here, but the marked span also includes damaged ordinary words. A name-only replacement cannot preserve the full spoken phrase, so the entire marker remains. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0255:m1</code>, <code>u0350:m1</code>, <code>u0350:m2</code>, <code>u0425:m1</code>, <code>u1080:m1</code>, <code>u1123:m1</code>, <code>u1395:m1</code>, <code>u1721:m1</code>, <code>u1965:m1</code>, <code>u2251:m1</code>, <code>u2405:m1</code>, <code>u2419:m1</code>, <code>u2557:m1</code>, <code>u2572:m1</code>, <code>u2681:m1</code>, <code>u2704:m1</code>, <code>u2807:m1</code>, <code>u2912:m1</code> | Combat rolls, spell and healing mechanics, damaged conversational or descriptive phrases, historical pronouns and literal horse recollection are outside this name pass. No complete supported name replacement is established within these spans; surrounding wording remains unchanged. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-038/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T035159475730Z-b2ecbb22/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-038/cleaned/dunmari-frontier-038-source-cleaned.md</code>
Before SHA-256: <code>22efe99ec9527e28f05b3e053e46c7a576df2c86cdd8d7c70a020025064cb750</code>
Planned after SHA-256: <code>4693cabdb8af168efeebf64d6b2d1a619b40869863fbf511f36500fcfbd3ecec</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
