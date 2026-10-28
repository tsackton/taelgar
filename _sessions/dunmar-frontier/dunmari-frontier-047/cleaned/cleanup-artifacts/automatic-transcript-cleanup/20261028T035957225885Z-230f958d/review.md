# Automatic transcript cleanup

Session: <code>dunmari-frontier-047</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 27 | 2 | 5 | 0 | 5 | 15 | 20 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>great-war-adversary</code> | supported | <code>u0149:m1</code> | <code>{{Sherman}}</code> | <code>Cha&#x27;mutte</code> | Delwath describes preventing another rise of the Great War adversary; his backstory and the reference identify Cha&#x27;mutte. Sherman has no matching role in these sources. | <code>People/Extraplanar Powers/Cha&#x27;mutte.md</code>, <code>People/PCs/Dunmar Fellowship/Delwath.md</code> | no |
| <code>southern-river</code> | high | <code>u0539:m1</code> | <code>{{shroud}}</code> | <code>Shrev</code> | The southern jungle and undead-border rumor identify the Shrev; the session narrative records the same rumor. | <code>Gazetteer/Greater Dunmar/Rivers/Shrev.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 47 (DuFr).md</code> | no |
| <code>dunmari-ruler</code> | high | <code>u0541:m1</code> | <code>{{Nine chernoff}}</code> | <code>Nayan Karnas</code> | The named ruler discussing southern defenses is Nayan Karnas; the personal reference establishes the complete name. | <code>People/Dunmari/Nayan Karnas.md</code>, <code>Gazetteer/Greater Dunmar/Rivers/Shrev.md</code> | no |
| <code>dunmari-gods</code> | supported | <code>u0713:m1</code> | <code>{{mardi gras}}</code> | <code>Dunmari gods</code> | Kenzo identifies Bhishma as one of the Dunmari gods. The religion note records this term and the order note establishes its dedication to Bhishma. | <code>Gods and Religions/Religions/Five Siblings/Dunmari Religion.md</code>, <code>Groups/Dunmari Mystery Cults/Order of the Awakened Soul.md</code> | no |
| <code>coastal-voyage-port</code> | supported | <code>u0752:m1</code> | <code>{{bar}}</code> | <code>Darba</code> | Jasmine describes the expected routine ship voyage between Chardon and the departure port Darba; the session and ship references support this route. Darba is favored over an otherwise unidentified port named bar. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 47 (DuFr).md</code>, <code>Things/Ships/Emerald Song.md</code> | no |
| <code>ship-family-contemporary-form</code> | supported | <code>u1343:m1</code> | <code>{{soul our hearts}}</code> | <code>Silverhearts</code> | The context concerns the ship-owning family, and the contemporary session source supports Silverhearts. Preserve that spoken-era form rather than substituting the later Silversongs form. | <code>_DM_/_Dunmari Frontier/Dunmari Frontier OneNote/Adventures/Road to Chardon (Session 42-47)/Emerald Song (OneNote).md</code>, <code>Things/Ships/Emerald Song.md</code> | no |
| <code>storm-giant-ally</code> | supported | <code>u2377:m1</code> | <code>{{programmers}}</code> | <code>Hralgar&#x27;s</code> | The discussion repeatedly identifies Hralgar as the giant whose freedom could provide passage across the Sea of Storms. Hralgar&#x27;s fits the contracted subject in this line; programmers has no contextual referent. | <code>People/Giants/Hralgar.md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>earlier-ship-family</code> | <code>u1345:m1</code> | <code>{{A sweat talks}}</code> | — | The fragment may name an earlier ship-owning family, but the inspected ship history does not identify a unique matching name or establish complete replacement boundaries. |
| <code>future-battle-target</code> | <code>u1571:m1</code> | <code>{{a return}}</code> | <code>Auratan</code> | Auratan is plausible from the later discussion, but the marked fragment could instead be damaged ordinary wording or a destination. The intended target and complete replacement remain uncertain. |
| <code>historical-wizard-fragment</code> | <code>u1550:m1</code> | <code>{{Their history}}</code> | — | The subject is the historical hobgoblin wizard imprisoned in the mirror, but this fragment may be ordinary wording rather than a name; no complete name replacement is recoverable. |
| <code>tentative-city-watch-name</code> | <code>u1702:m1</code>, <code>u1717:m1</code> | <code>{{regarding the second day}}</code>, <code>{{down for a second}}</code> | — | These passages discuss a provisional name for the city watch. The reference uses Praecanti Vigiles, but it does not establish the tentative form spoken here; substituting the later name would override the dialogue. The first span also contains unrecoverable surrounding wording. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0013:m1</code>, <code>u0532:m1</code>, <code>u1455:m1</code>, <code>u1455:m2</code>, <code>u1540:m1</code>, <code>u1550:m2</code>, <code>u1556:m1</code>, <code>u1557:m1</code>, <code>u1565:m1</code>, <code>u1565:m2</code>, <code>u1574:m1</code>, <code>u1598:m1</code>, <code>u1695:m1</code>, <code>u2223:m1</code>, <code>u2227:m1</code> | Damaged ordinary wording, grammar, pronouns, creature descriptions, numbers, or message phrasing outside this name-and-setting-term pass; no surrounding reconstruction is authorized. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-047/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T035957225885Z-230f958d/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-047/cleaned/dunmari-frontier-047-source-cleaned.md</code>
Before SHA-256: <code>964682ed01c438cf0aaa9f43d6223c1cce1fb346eaf022cf761e2a30edb56b38</code>
Planned after SHA-256: <code>9e953f42c5205a7517cced7b840c5913c8eae0d83e5e08cb82ddf1db725a9438</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
