# Automatic transcript cleanup

Session: <code>dunmari-frontier-129</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 23 | 2 | 2 | 0 | 3 | 16 | 19 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>yeraad-basin</code> | high | <code>u0017:m1</code> | <code>{{Iran River Basin}}</code> | <code>Yeraad River Basin</code> | The opening recounts the flight to the Chataan Mountains. Session 127 explicitly places that flight across the Yeraad Watershed, whose reference note calls it the Yeraad River Basin. | <code>Gazetteer/Major Rivers/Yeraad Watershed/Yeraad Watershed.md</code>, <code>Gazetteer/Greater Chardon/Rivers/Yeraad.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 127 (DuFr).md</code> | no |
| <code>local-university</code> | supported | <code>u0644:m1</code> | <code>{{University of Bend}}</code> | <code>University of Chardon</code> | Wellby is researching planar travel while staying in Chardon; the local University of Chardon has a Faculty of Metaphysics for planar studies. That institution is strongly favored over the unestablished Bend form. | <code>Gazetteer/Greater Chardon/Chardonian Empire/Chardon/University of Chardon.md</code> | no |
| <code>plaguelands</code> | supported | <code>u0830:m1</code> | <code>{{Plaguands}}</code> | <code>Plaguelands</code> | The near spelling and repeated discussion of the approaching host from the Plaguelands strongly favor the established regional name. The awkward following statement about pace is preserved, without substituting hobgoblins or reconstructing the sentence. | <code>Gazetteer/Upper Istaros/Plaguelands.md</code> | no |
| <code>douren</code> | high | <code>u1276:m1</code> | <code>{{DORA}}</code> | <code>Douren</code> | Marcella describes the river on the western edge of the Plaguelands that runs through difficult gorges. The Douren reference and Plaguelands geography establish this uniquely. | <code>Gazetteer/Major Rivers/Istaros Watershed/Douren.md</code>, <code>Gazetteer/Upper Istaros/Plaguelands.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>board-and-kenzo</code> | <code>u0689:m1</code> | <code>{{chart and Kenzo}}</code> | <code>Chardon</code>, <code>Kenzo</code> | Kenzo is clear and Chardon is plausible, but the complete marked phrase may contain a false start or conjunction. No unique whole-span name replacement preserves the uncertain wording. |
| <code>cloud-size-comparison</code> | <code>u1667:m1</code> | <code>{{Vincent&#x27;s size}}</code> | <code>Vindristjarna</code> | The marked comparison could refer to Vindristjarna or could be ordinary size wording such as decent-sized. The ship is a plausible comparison, but the complete marked phrase is not uniquely recoverable. |
| <code>future-teaching-place</code> | <code>u0620:m1</code> | <code>{{inside place}}</code> | <code>Calcara Island</code> | Kazuro and Calcara Island are plausible contextual connections, but the marked words are an unclear place description rather than a recoverable name. Replacing them with a location would supply wording not established by the utterance. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-mechanics</code> | <code>u0058:m1</code>, <code>u0226:m1</code>, <code>u0295:m1</code>, <code>u0296:m1</code>, <code>u0342:m1</code>, <code>u1029:m1</code>, <code>u1119:m1</code>, <code>u1214:m1</code>, <code>u1406:m1</code>, <code>u1719:m1</code>, <code>u2079:m1</code>, <code>u2188:m1</code>, <code>u2206:m1</code>, <code>u2395:m1</code>, <code>u2583:m1</code>, <code>u2585:m1</code> | These spans contain ordinary speech, descriptive wording, participant chatter, or rules discussion. Resolving them would require prose or mechanics reconstruction rather than a supported setting-name correction. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-129/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045456746883Z-990970cc/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-129/cleaned/dunmari-frontier-129-source-cleaned.md</code>
Before SHA-256: <code>a335e7ac349f02f5a31924fef14a7bbda42d656c3fc327587bef7ed01cf98162</code>
Planned after SHA-256: <code>cb66236be082508fd3261fa7933d62cd6c837db517bb0e8cb7824123f04f9a0b</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
