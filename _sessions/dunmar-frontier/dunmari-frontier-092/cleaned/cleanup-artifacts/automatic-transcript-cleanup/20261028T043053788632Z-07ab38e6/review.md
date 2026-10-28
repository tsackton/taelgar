# Automatic transcript cleanup

Session: <code>dunmari-frontier-092</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 20 | 4 | 0 | 0 | 9 | 7 | 16 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>shadow-armband</code> | high | <code>u0491:m1</code> | <code>{{armbed}}</code> | <code>armband</code> | The recollection of Zegron locating the object and the trapped hobgoblin army identifies the armband; the session record and item note establish the term. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 55 (DuFr).md</code>, <code>Campaigns/Dunmari Frontier Campaign/Treasure/Cha&#x27;mutte’s Shadow Armband.md</code> | no |
| <code>skaer-arrows</code> | high | <code>u1472:m1</code> | <code>{{honed scare}}</code> | <code>honed Skaer</code> | Wellby is using the purchased Skaer arrows. The initial span includes the established honed property, and the following attacks refer to the same ammunition. | <code>Things/Materials/Skaer Steel.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Hoards/Gifts and Purchases.md</code> | no |
| <code>skaer-arrows</code> | high | <code>u1706:m1</code> | <code>{{scare}}</code> | <code>Skaer</code> | Wellby is using the purchased Skaer arrows. The initial span includes the established honed property, and the following attacks refer to the same ammunition. | <code>Things/Materials/Skaer Steel.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Hoards/Gifts and Purchases.md</code> | no |
| <code>skaer-arrows</code> | high | <code>u1877:m1</code> | <code>{{scary}}</code> | <code>Skaer</code> | Wellby is using the purchased Skaer arrows. The initial span includes the established honed property, and the following attacks refer to the same ammunition. | <code>Things/Materials/Skaer Steel.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Hoards/Gifts and Purchases.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>island-name</code> | <code>u1272:m1</code>, <code>u1273:m1</code> | <code>{{Erawa}}</code>, <code>{{Airla}}</code> | — | The two adjacent route-planning remarks appear to name the same island, but inspected filenames, names, aliases, geography and campaign sources provide no unique spelling. |
| <code>northern-mountain-name</code> | <code>u0695:m1</code> | <code>{{Yokoscar}}</code> | — | The range north of the Ket is identifiable, but inspected geography and session sources do not establish this spoken name or a preferred spelling. |
| <code>scholar-origin-phrase</code> | <code>u1109:m1</code> | <code>{{Toe intel crap}}</code> | — | The remembered scholar is discussed immediately afterward, but this marked phrase mixes a possible place reference with damaged ordinary wording. No complete name-only replacement is established. |
| <code>stone-giant-question</code> | <code>u0121:m1</code> | <code>{{Lister Cod}}</code> | — | The brief interjection after the dwarf question may be a name or ordinary wording; the reply does not identify a unique referent or complete replacement. |
| <code>wellby-mixed-phrase</code> | <code>u1901:m1</code> | <code>{{As Wellbe is}}</code> | <code>Wellby</code> | The marker includes a probable Wellby reference inside an unclear clause. Correcting only the name would require editing part of a marker; replacing the complete span would reconstruct ordinary wording. |
| <code>white-dragon-name</code> | <code>u0754:m1</code>, <code>u0758:m1</code> | <code>{{Eskanyar}}</code>, <code>{{Eskanyar}}</code> | <code>Eskanyar</code> | Both spans refer to a white dragon in Brimskarda&#x27;s story. The inspected reference and session notes do not establish its name or resolve the spelling. |
| <code>zegron-recollection</code> | <code>u0483:m1</code> | <code>{{zoom}}</code> | <code>Zegron</code> | The context identifies Zegron, but this second span could be a repeated name or an ordinary pronoun. The source establishes the encounter but cannot settle what was said. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-numbers</code> | <code>u0100:m1</code>, <code>u0332:m1</code>, <code>u0429:m1</code>, <code>u0829:m1</code>, <code>u1717:m1</code>, <code>u1826:m1</code>, <code>u1899:m1</code> | Ordinary dialogue, an extended damaged presentation phrase, and combat numbers or damage wording are outside the name and setting-term pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-092/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T043053788632Z-07ab38e6/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-092/cleaned/dunmari-frontier-092-source-cleaned.md</code>
Before SHA-256: <code>83c441274d6b1dee3b624010f583a1ae28ba8178450133d559362479c8f4a3fa</code>
Planned after SHA-256: <code>7be18c49882a30287d1c0a0ac94a0cacdc27f9e9c8b677a7bf31d015dd295915</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
