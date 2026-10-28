# Automatic transcript cleanup

Session: <code>dunmari-frontier-102</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 25 | 1 | 0 | 0 | 4 | 20 | 24 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>cedrano</code> | high | <code>u0084:m1</code> | <code>{{Sadrano}}</code> | <code>Cedrano</code> | Milo recounts the departure of the Stormdancer; the written version of this same story explicitly names Cedrano, whose reference note establishes the spelling. | <code>Campaigns/Dunmari Frontier Campaign/Tales and Stories/Milo&#x27;s Story.md</code>, <code>Gazetteer/Greater Chardon/Chardonian Empire/Apporia/Cedrano.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>amulet-thrower</code> | <code>u3453:m1</code> | <code>{{Thinker}}</code> | <code>Seeker</code>, <code>Wellby</code> | Thinker resembles Seeker, but the surrounding dialogue and session narrative identify Wellby as the amulet thrower. This could be a spoken name mistake; neither the phonetic reading nor the factually correct actor alone safely resolves the span. |
| <code>split-ability-reference</code> | <code>u2778:m1</code>, <code>u2779:m1</code> | <code>{{soul}}</code>, <code>{{Play}}</code> | <code>Soul Sight</code> | The exchange introduces information about Buruli and may invoke Soul Sight, but the marked fragments are split between speakers and do not establish a unique complete name replacement within either span. Retain both fragments without reconstructing the utterance. |
| <code>sword-discussion-address</code> | <code>u0378:m1</code> | <code>{{Priscilla}}</code> | <code>Delwath</code> | The span may be an address to Delwath or ordinary garbled wording. The sword discussion identifies Delwath as the interlocutor, but does not establish a complete replacement for Priscilla. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-dialogue</code> | <code>u0429:m1</code>, <code>u0915:m1</code>, <code>u1433:m1</code>, <code>u2078:m1</code>, <code>u3504:m1</code>, <code>u3596:m1</code>, <code>u3718:m1</code> | Ordinary description, dialogue, or action wording without a supported name or setting-term correction; retain the complete marked spans. |
| <code>rules-and-combat-wording</code> | <code>u1107:m1</code>, <code>u1146:m1</code>, <code>u1310:m1</code>, <code>u1388:m1</code>, <code>u2251:m1</code>, <code>u2373:m1</code>, <code>u2814:m1</code>, <code>u2887:m1</code>, <code>u3733:m1</code> | Rules explanations, distances, spell discussion, or combat wording. These are not complete identifiable name replacements and repairing them would reconstruct mechanics or surrounding phrases. |
| <code>story-wording</code> | <code>u0111:m1</code>, <code>u0117:m1</code> | Damaged source-reading wording and a numerical expression in Milo’s story; repairing the surrounding prose or numbers is outside this name pass. |
| <code>water-activation-fragment</code> | <code>u3059:m1</code> | Friend follows an unmarked water fragment during discussion of activating an effect. A complete feature name is not present within the marked boundaries; repairing the fragment would reconstruct the rules discussion. |
| <code>weapon-wording</code> | <code>u2871:m1</code> | Riswynn is comparing cantrips with ordinary weapon attacks; the earlier crossbow description does not establish Camaro as a named item. Restoring a generic weapon phrase is outside this name pass. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-102/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T043818072693Z-7047a051/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-102/cleaned/dunmari-frontier-102-source-cleaned.md</code>
Before SHA-256: <code>1af85b61b1df4f8a9cce1881f38db8aee6d020c9ac60cdf8a2f8499b8dc48671</code>
Planned after SHA-256: <code>fc668e6ff6ed0250b6461d7a2c3d51822c0ae74dd781c1da347c0995674dcd8f</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
