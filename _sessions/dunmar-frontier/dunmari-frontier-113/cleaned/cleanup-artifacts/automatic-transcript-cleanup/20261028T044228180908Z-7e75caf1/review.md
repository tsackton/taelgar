# Automatic transcript cleanup

Session: <code>dunmari-frontier-113</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 19 | 2 | 2 | 0 | 3 | 12 | 15 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>elven-divine-realm</code> | supported | <code>u1580:m1</code> | <code>{{Elven Device}}</code> | <code>Elven divine realm</code> | The reply refers directly to the teleport destination named in the preceding utterance; the session record confirms the Elven divine realm. Device has no contextual referent. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 113 (DuFr).md</code>, <code>Cosmology/Spiritual Realms/Divine Realms.md</code> | no |
| <code>radiant-path-alternate</code> | supported | <code>u1787:m1</code> | <code>{{auto, Lucas}}</code> | <code>Ordo Lucis</code> | The speaker explicitly gives an alternate name for the Radiant Path; the consulted naming table supplies a matching form. Its development status is not used to alter the spoken group identity. | <code>Groups/Drankorian Societies/Radiant Path.md</code>, <code>_dm_notes/_Dunmar Frontier/Session 103-110 - The Last Jade/Circular Island/04 Tables and Clues/Table - Drankorian Societies - Last Jade.md</code> | no |
| <code>valanthe</code> | high | <code>u2166:m1</code> | <code>{{volanthi}}</code> | <code>Valanthe</code> | Both occurrences identify the elven writer whose courtyard and silver quill the party investigates; the reference note establishes Valanthe. | <code>People/Historical Figures/Valanthe.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 113 (DuFr).md</code> | no |
| <code>valanthe</code> | high | <code>u2443:m1</code> | <code>{{violanthea}}</code> | <code>Valanthe</code> | Both occurrences identify the elven writer whose courtyard and silver quill the party investigates; the reference note establishes Valanthe. | <code>People/Historical Figures/Valanthe.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 113 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>clipped-apollyon-reference</code> | <code>u0467:m1</code> | <code>{{a pie}}</code> | <code>Apollyon&#x27;s notes</code> | The context concerns Rai lacking the construction notes, but the marked fragment cannot uniquely establish a complete name or possessive replacement without reconstructing missing wording. |
| <code>foreign-human-name</code> | <code>u1928:m1</code> | <code>{{not very it&#x27;s}}</code> | <code>Khemut</code> | The foreign human is later called Khemut in this transcript and in the reference note, but the marked words have no convincing phonetic connection and may be interrupted commentary rather than the spoken name. Retain rather than substitute a factually matching identity. |
| <code>rai-in-damaged-phrase</code> | <code>u0503:m1</code> | <code>{{Ryan? Why not well could drive?}}</code> | <code>Rai</code> | Rai is the contextual subject, but the marked span includes an unrecoverable question; replacing it would require reconstructing ordinary wording. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0310:m1</code>, <code>u0367:m1</code>, <code>u0477:m1</code>, <code>u0507:m1</code>, <code>u0507:m2</code>, <code>u0664:m1</code>, <code>u0690:m1</code>, <code>u0891:m1</code>, <code>u1208:m1</code>, <code>u1697:m1</code>, <code>u2304:m1</code>, <code>u2513:m1</code> | Ordinary conversational fragments, rules and spell discussion, burial wording, a saving-throw response, and authentication wording are outside this name and setting-term pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-113/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044228180908Z-7e75caf1/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-113/cleaned/dunmari-frontier-113-source-cleaned.md</code>
Before SHA-256: <code>df97a43e33b5cc5d34821f446c03b2f774d77b69ad2cacbad726406f314608b9</code>
Planned after SHA-256: <code>389da47b1e5afe433ea1d6baeac784a321bb36597e50e888ce33e3880b47ba6b</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
