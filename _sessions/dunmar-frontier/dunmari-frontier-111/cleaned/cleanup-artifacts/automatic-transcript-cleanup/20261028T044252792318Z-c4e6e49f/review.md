# Automatic transcript cleanup

Session: <code>dunmari-frontier-111</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 25 | 5 | 3 | 0 | 4 | 13 | 17 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>fey-steel</code> | high | <code>u0251:m1</code> | <code>{{face steel}}</code> | <code>fey steel</code> | The listed forge metals match the recovered forge inventory, which explicitly names fey steel. | <code>Campaigns/Dunmari Frontier Campaign/Treasure/Forge Components.md</code> | no |
| <code>serandris</code> | high | <code>u0331:m1</code> | <code>{{sarandres}}</code> | <code>Serandris</code> | The hoard inventory gives this exact silver vial inscription and establishes the name Serandris. | <code>Campaigns/Dunmari Frontier Campaign/Hoards/Ra&#x27;ghemdros&#x27; Hoard.md</code> | no |
| <code>wellby</code> | supported | <code>u0830:m1</code> | <code>{{well-being}}</code> | <code>Wellby</code> | Willow is expressing fear for a companion and herself, then the rest of the party. Wellby is the strongly favored personal referent; the ordinary noun well-being is less natural in this construction. | <code>People/PCs/Dunmar Fellowship/Wellby.md</code>, <code>People/Halflings/Willow Copperharp.md</code> | no |
| <code>arheste-prompt</code> | supported | <code>u1296:m1</code> | <code>{{Day}}</code> | <code>Arheste</code> | The DM supplies the forgotten name of the ancient elven opponent of Apollyon, immediately repeated by Delwath. Arheste uniquely matches that visit and role, despite the poor phonetic rendering. | <code>People/Elves/Arheste.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 87 (DuFr).md</code> | no |
| <code>arheste-repeat</code> | high | <code>u1297:m1</code> | <code>{{Her estate}}</code> | <code>Arheste</code> | Delwath repeats the supplied name of the ancient elf interviewed about Apollyon; Arheste and the recorded Orenlas visit match the full description. | <code>People/Elves/Arheste.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 87 (DuFr).md</code> | no |
| <code>ursk</code> | high | <code>u1700:m1</code> | <code>{{Ersk}}</code> | <code>Ursk</code> | The dagger with sight-related magic is identified as Urskan by its reference note, establishing Ursk as the place named here. | <code>Campaigns/Dunmari Frontier Campaign/Treasure/Watcher&#x27;s Dagger.md</code> | no |
| <code>vindristjarna</code> | supported | <code>u1917:m1</code> | <code>{{vignette}}</code> | <code>Vindristjarna</code> | The immediate exchange names Vindristjarna while discussing the danger posed by automated defensive towers to the ship. The shortened recognition is strongly favored as that same named skyship. | <code>Things/Ships/Vindristjarna.md</code> | no |
| <code>bahrazel</code> | high | <code>u2702:m1</code> | <code>{{Barzelle}}</code> | <code>Bahrâzel</code> | The protective divine light follows Riswynn&#x27;s feast and refers to the dwarven gods, whose documented name is Bahrâzel. | <code>Gods and Religions/Gods/Embodied Gods/Bahrazel/Bahrazel.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>alexandria-place</code> | <code>u1301:m1</code>, <code>u1302:m1</code> | <code>{{Alexandria}}</code>, <code>{{Alexandria}}</code> | <code>Vetta</code>, <code>Skaer Islands</code> | The recalled scepter destruction is recorded at Vetta in the Skaer Islands, but that does not establish which place name was uttered here or rule out a spoken misremembering. The complete marked replacement remains unclear. |
| <code>new-york-city</code> | <code>u1782:m1</code> | <code>{{New York City}}</code> | <code>Uzgukhar</code>, <code>orc city</code> | The recalled deception resembles the recorded trick at Uzgukhar, but the marker could reflect ordinary wording such as orc city or a different reference. Evidence does not establish a complete proper-name replacement. |
| <code>peikong-boundaries</code> | <code>u0345:m1</code> | <code>{{peikong}}</code> | <code>Kong</code> | The exchange interrupts a statement about killing a dragon as Kong joins. This may contain a greeting to Kong, but the marked span and adjacent words do not establish a complete standalone name replacement. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0036:m1</code>, <code>u0471:m1</code>, <code>u0505:m1</code>, <code>u1219:m1</code>, <code>u1946:m1</code>, <code>u2169:m1</code>, <code>u2200:m1</code>, <code>u2705:m1</code>, <code>u3163:m1</code>, <code>u3237:m1</code>, <code>u3280:m1</code>, <code>u3283:m1</code>, <code>u3286:m1</code> | Ordinary chatter, numbers, rules explanations, or damaged spellcasting wording without a clear standalone name or setting term; reconstructing these spans is outside names-v1. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-111/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T044252792318Z-c4e6e49f/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-111/cleaned/dunmari-frontier-111-source-cleaned.md</code>
Before SHA-256: <code>6b3c32ccce961510a17902649a63839ce0c511ae0d8f2cc5a866c380c204663f</code>
Planned after SHA-256: <code>3fefca26b272fcd979e827c19026b970b5afa4733fbe154b89e67d73d5dd3782</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
