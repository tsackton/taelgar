# Automatic transcript cleanup

Session: <code>dunmari-frontier-101</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 46 | 1 | 3 | 0 | 3 | 39 | 42 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>merfolk-bodies</code> | supported | <code>u2437:m1</code> | <code>{{merge}}</code> | <code>merfolk</code> | The search immediately follows combat with merfolk guards and continues with the separate word Bodies. Merfolk is the supported people-name behind merge; no surrounding wording or punctuation is reconstructed. Ordinary wording is possible but less consistent with the search targets. | <code>Creatures/Species/Merfolk.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 101 (DuFr).md</code> | no |
| <code>yuvanti</code> | supported | <code>u2645:m1</code> | <code>{{you want the}}</code> | <code>Yuvanti</code> | The marked syllables closely match Yuvanti immediately before dwarven coins. The regional reference establishes the dwarven association and preferred spelling; Dunmari or ordinary wording fits the sound and adjacent dwarven qualifier less well. | <code>Gazetteer/Greater Dunmar/Yuvanti Mountains.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Hoards/Merfolk Quest Treasure.md</code> | no |
| <code>delwath</code> | high | <code>u3049:m1</code> | <code>{{Delaware}}</code> | <code>Delwath</code> | Wellby refers the surviving prisoner to the party member conducting the interrogation; the session configuration establishes Delwath, and the following response is his. Delaware has no competing contextual identity. | <code>_sessions/dunmar-frontier/dunmari-frontier-101/cleaned/dunmari-frontier-101-session.yaml</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 101 (DuFr).md</code> | no |
| <code>wellby-address</code> | supported | <code>u3443:m1</code> | <code>{{Lonnie}}</code> | <code>Wellby</code> | Kenzo addresses the halfling-rescue discussion to the party halfling, who answers Yep and explains the crew, then discusses his telepathy. The participant configuration and session note establish Wellby. The sound alone is weak, but this specific responder and role strongly favor Wellby over an unattested Lonnie. | <code>_sessions/dunmar-frontier/dunmari-frontier-101/cleaned/dunmari-frontier-101-session.yaml</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 101 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>kill-target</code> | <code>u3467:m1</code> | <code>{{layer}}</code> | <code>Buruli</code> | The escape plan makes Buruli a plausible intended target, but layer is not a clear complete rendering of that name and could be a fragment of longer ordinary wording. Context establishes the foe, not exactly what was said. |
| <code>language-attempt</code> | <code>u2962:m1</code> | <code>{{a summon}}</code> | <code>Sylvan</code>, <code>Abyssal</code> | Delwath is trying another spoken language after Common and Elvish fail. Sylvan and Abyssal are plausible readings, but the inspected language overview and earlier campaign record do not uniquely identify the complete marked form; retain it. |
| <code>milo-phrase</code> | <code>u2653:m1</code> | <code>{{20 miles, then}}</code> | <code>Milo Thistlefoot</code> | The dialogue concerns Milo and his recovered possessions, but the entire marked phrase includes unrecoverable ordinary wording. A name-only substitution would erase that wording or invent its boundaries. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>dates-and-elapsed-time</code> | <code>u3962:m1</code>, <code>u3965:m1</code>, <code>u3966:m1</code>, <code>u3967:m1</code>, <code>u3968:m1</code>, <code>u3969:m1</code>, <code>u3971:m1</code>, <code>u3973:m1</code> | Month, year, and elapsed-time discussion, including the fragment Wells before Months ago. Chronology and conversational corrections are outside this names-only pass. |
| <code>ordinary-fragments</code> | <code>u0198:m1</code>, <code>u0232:m1</code>, <code>u0415:m1</code> | These fragments occur in portal-blocking tactics, a generic sailing-background explanation, and initiative setup interrupted by off-table chatter. The contextual readings concern ordinary wording rather than a supported proper name or named setting term. |
| <code>wording-and-mechanics</code> | <code>u0090:m1</code>, <code>u0108:m1</code>, <code>u0112:m1</code>, <code>u0201:m1</code>, <code>u0363:m1</code>, <code>u0485:m1</code>, <code>u0591:m1</code>, <code>u0866:m1</code>, <code>u1201:m1</code>, <code>u1418:m1</code>, <code>u1451:m1</code>, <code>u1809:m1</code>, <code>u1828:m1</code>, <code>u1930:m1</code>, <code>u1967:m1</code>, <code>u2142:m1</code>, <code>u2245:m1</code>, <code>u2971:m1</code>, <code>u2972:m1</code>, <code>u3539:m1</code>, <code>u3557:m1</code>, <code>u3636:m1</code>, <code>u3654:m1</code>, <code>u3728:m1</code>, <code>u3739:m1</code>, <code>u3894:m1</code>, <code>u3910:m1</code>, <code>u4032:m1</code> | Ordinary conversational or descriptive wording, combat and healing mechanics, movement, item-use explanations, and incomplete phrases. Repair would require reconstructing speech beyond an established name or setting term; retained unchanged. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-101/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T043844303040Z-96fa6770/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-101/cleaned/dunmari-frontier-101-source-cleaned.md</code>
Before SHA-256: <code>7b2781ec861ee63e4cea3938303a8e5fd3c2208b819c3d972c889669be4a7d1b</code>
Planned after SHA-256: <code>8ed7e08c50e8c732bb4eb38807e95a504f81adaf0529e280f7eb6d22b4bf61ca</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
