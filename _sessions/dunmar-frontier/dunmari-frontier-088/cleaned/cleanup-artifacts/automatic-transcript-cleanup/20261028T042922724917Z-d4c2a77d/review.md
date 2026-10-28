# Automatic transcript cleanup

Session: <code>dunmari-frontier-088</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 42 | 1 | 5 | 0 | 5 | 31 | 36 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>feywild</code> | high | <code>u0086:m1</code> | <code>{{bay. Wall}}</code> | <code>Feywild</code> | The fly discussion refers to the realm where Agata was imprisoned; the session record establishes Feywild as the place name. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 67 (DuFr).md</code> | no |
| <code>skyship</code> | supported | <code>u0334:m1</code> | <code>{{industry}}</code> | <code>Vindristjarna</code> | Writing on the exterior and bridging away from the party ship both identify Vindristjarna. The reference establishes its spelling; these short ASR forms are distorted. | <code>Things/Ships/Vindristjarna.md</code> | no |
| <code>blessing-of-perception</code> | supported | <code>u0792:m1</code> | <code>{{last thing of perception}}</code> | <code>Blessing of Perception</code> | Delwath immediately explains that this named ability lets him see invisible things. The shield correspondence attests the existing Blessing of Perception name and that function; proposed later buffs are not being adopted. | <code>Campaigns/Dunmari Frontier Campaign/Treasure/Deno&#x27;qai Lynx Shield.md</code>, <code>Worldbuilding/Chats and Emails/Chats/2025-10-11 - Calendars and Holidays.md</code> | no |
| <code>armor-of-agathys</code> | supported | <code>u1345:m1</code> | <code>{{armor box}}</code> | <code>Armor of Agathys</code> | Delwath names a protective effect lost to damage. The matching battle reference explicitly identifies his Armor of Agathys, strongly favoring that complete term over the distorted armor box. | <code>_DM_/_Dunmari Frontier/Session 76-82 (The War of the Cloak)/Grash Statblock.md</code> | no |
| <code>arheste</code> | supported | <code>u2143:m1</code> | <code>{{Rs day}}</code> | <code>Arheste</code> | The short utterance follows about a week after and refers back to the recently visited elf. Arheste matches the sound and recent session context; the reference establishes the spelling. | <code>People/Elves/Arheste.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 87 (DuFr).md</code> | no |
| <code>skyship</code> | supported | <code>u2197:m1</code> | <code>{{district}}</code> | <code>Vindristjarna</code> | Writing on the exterior and bridging away from the party ship both identify Vindristjarna. The reference establishes its spelling; these short ASR forms are distorted. | <code>Things/Ships/Vindristjarna.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>bow-item</code> | <code>u1144:m1</code> | <code>{{Let me boast}}</code> | <code>Flaming Bowstring</code>, <code>Wayfarer&#x27;s Bow</code> | Wellby is spending charges while shooting; Flaming Bowstring and his bow are plausible, but Let me boast does not securely recover the complete spoken item term. |
| <code>flight-phrase</code> | <code>u0920:m1</code> | <code>{{but it can fly while we can fly}}</code> | <code>Wellby</code>, <code>Buck Beak</code> | Buck Beak and Wellby are discussed nearby, but the whole marked flight phrase cannot be reduced to a uniquely recoverable name without reconstructing its wording. |
| <code>ladder-order</code> | <code>u1835:m1</code> | <code>{{Bladder sound before him}}</code> | <code>Ladder</code> | Ladder is plausible in the initiative-order discussion, but the remaining words in the complete marked question are not recoverable as a name-only correction. |
| <code>recipient-question</code> | <code>u1828:m1</code> | <code>{{that model}}</code> | <code>Wellby</code> | The hand needs to reach Wellby, and the next line locates him, but that model may contain additional wording or a different reference. Replacing the complete span with a person name would require guessing its boundaries. |
| <code>ship-weapon</code> | <code>u0940:m1</code> | <code>{{iphone}}</code> | <code>Icicle Turret</code> | The ship offensive capability suggests the Icicle Turret, but iphone does not establish whether the speaker named the turret or used an ordinary description such as ice thing. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0076:m1</code>, <code>u0086:m2</code>, <code>u0118:m1</code>, <code>u0558:m1</code>, <code>u0611:m1</code>, <code>u0783:m1</code>, <code>u0828:m1</code>, <code>u0874:m1</code>, <code>u0874:m2</code>, <code>u0892:m1</code>, <code>u0906:m1</code>, <code>u0907:m1</code>, <code>u1146:m1</code>, <code>u1175:m1</code>, <code>u1185:m1</code>, <code>u1276:m1</code>, <code>u1483:m1</code>, <code>u1535:m1</code>, <code>u1671:m1</code>, <code>u1722:m1</code>, <code>u1791:m1</code>, <code>u1833:m1</code>, <code>u1918:m1</code>, <code>u1918:m2</code>, <code>u1943:m1</code>, <code>u2072:m1</code>, <code>u2100:m1</code>, <code>u2156:m1</code>, <code>u2200:m1</code>, <code>u2202:m1</code>, <code>u2251:m1</code> | Ordinary dialogue, damaged descriptive phrases, combat mechanics, rolls, and sentence reconstruction fall outside this name and setting-term pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-088/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T042922724917Z-d4c2a77d/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-088/cleaned/dunmari-frontier-088-source-cleaned.md</code>
Before SHA-256: <code>1c68cafc686b75748180c0407d73de2570664ffcc843db67e577fcadae0da663</code>
Planned after SHA-256: <code>8fabde1ac334c0b35f31cda7511ab177e36bd7459f1b61a5c774288685fb05ba</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
