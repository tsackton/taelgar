# Automatic transcript cleanup

Session: <code>dunmari-frontier-066</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 50 | 0 | 1 | 0 | 3 | 46 | 49 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>lastlight-falls</code> | supported | <code>u2941:m1</code> | <code>{{last one for life}}</code> | <code>Lastlight Falls</code> | The speaker repeats the portal name immediately after the DM says Lastlight Falls twice; the reference note and session record establish that destination. The ASR form is substantially distorted, so this is supported rather than high confidence. | <code>Gazetteer/Extraplanar/Feywild/Amberglow/Lastlight Falls.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 66 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>agata-description</code> | <code>u2959:m2</code> | <code>{{a sandwich}}</code> | <code>a sand witch (possibly Agata)</code> | The speaker asks whether Agata or another described figure rode the fly. A sand witch is plausible descriptive wording, but the marked span does not uniquely establish a named identity or title, and replacing it would risk reconstructing an ordinary phrase. |
| <code>group-description</code> | <code>u0236:m1</code> | <code>{{Center and}}</code> | <code>Sembaran</code> | This fragment may be a regional identity such as Sembaran while the kenku describes the unusual group. Wellby has Sembaran origins, but Alimash is from Svolhas, and the fragment does not establish the referent or whether surrounding connective wording is inside the marker. Retain rather than reconstruct. |
| <code>shield-or-shoal</code> | <code>u2886:m1</code> | <code>{{shell}}</code> | <code>Shoal</code>, <code>shield</code> | The exchange concerns Alimash retrieving or discussing his shield, but shell could also resemble the companion name Shoal. The complete phrase does not uniquely identify a name or a complete setting-term replacement. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0024:m1</code>, <code>u0027:m1</code>, <code>u0063:m1</code>, <code>u0115:m1</code>, <code>u0178:m1</code>, <code>u0429:m1</code>, <code>u0542:m1</code>, <code>u0784:m1</code>, <code>u0890:m1</code>, <code>u0962:m1</code>, <code>u0981:m1</code>, <code>u1016:m1</code>, <code>u1090:m1</code>, <code>u1113:m1</code>, <code>u1136:m1</code>, <code>u1172:m1</code>, <code>u1238:m1</code>, <code>u1349:m1</code>, <code>u1438:m1</code>, <code>u1479:m1</code>, <code>u1491:m1</code>, <code>u1586:m1</code>, <code>u1611:m1</code>, <code>u1768:m1</code>, <code>u1806:m1</code>, <code>u1890:m1</code>, <code>u1920:m1</code>, <code>u1987:m1</code>, <code>u2145:m1</code>, <code>u2183:m1</code>, <code>u2211:m1</code>, <code>u2261:m1</code>, <code>u2301:m1</code>, <code>u2334:m1</code>, <code>u2343:m1</code>, <code>u2392:m1</code>, <code>u2572:m1</code>, <code>u2583:m1</code>, <code>u2607:m1</code>, <code>u2633:m1</code>, <code>u2672:m1</code>, <code>u2833:m1</code>, <code>u2852:m1</code>, <code>u2949:m1</code>, <code>u2959:m1</code>, <code>u3001:m1</code> | These spans concern ordinary narration, incomplete phrases, incidental chatter, equipment descriptions, action declarations, attack outcomes, numbers, or rules explanations. Name-like ASR fragments such as Mickey, Barrett, and Overch have no contextual named referent; correcting them or names embedded in damaged wording would require reconstruction outside this pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-066/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T041235159488Z-76f274ce/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-066/cleaned/dunmari-frontier-066-source-cleaned.md</code>
Before SHA-256: <code>9592fc36101de86c3b18e157d16c32f880b54723e1a401b28397f462cab89ade</code>
Planned after SHA-256: <code>6625dedbc5df77852b1746537b0279554b4f7158dedb932894d70c5acc86641e</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
