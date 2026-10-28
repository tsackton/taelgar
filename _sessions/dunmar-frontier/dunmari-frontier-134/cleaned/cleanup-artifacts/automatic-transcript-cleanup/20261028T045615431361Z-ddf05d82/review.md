# Automatic transcript cleanup

Session: <code>dunmari-frontier-134</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 16 | 0 | 2 | 0 | 6 | 8 | 14 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>urlich-monastery</code> | supported | <code>u0939:m1</code> | <code>{{Ehrlich Modest}}</code> | <code>Urlich Monastery</code> | The speaker asks about the site of Cha&#x27;mutte&#x27;s death, then immediately says Urlich Pass. Urlich Monastery is the attested name matching the first attempted place name; preserve the following self-correction unchanged. | <code>Gazetteer/Central Highlands/Urlich Pass.md</code> | no |
| <code>kenzos-player</code> | supported | <code>u1322:m1</code> | <code>{{Tom}}</code> | <code>Kong</code> | The DM addresses the player who can decide Kenzo&#x27;s actions. The session participant mapping uniquely identifies David Kong as Kenzo&#x27;s player; Kong is favored over Tom, who is not a listed participant. | <code>_sessions/dunmar-frontier/dunmari-frontier-134/cleaned/dunmari-frontier-134-session.yaml</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>delwath-phrase</code> | <code>u1327:m1</code> | <code>{{Delta&#x27;s 11.}}</code> | <code>Delwath</code> | The next speaker explicitly discusses Delwath and the centaur, but the complete marked phrase includes more than a recognizable name. Its remaining wording cannot be recovered within this name-only pass. |
| <code>isingue-question</code> | <code>u0256:m1</code> | <code>{{He&#x27;s a guy. Isn&#x27;t he?}}</code> | <code>Isingue</code> | The Heartroot&#x27;s former home makes Isingue a plausible name inside this question, but the complete marked wording cannot be resolved as a plain name without reconstructing the question. |
| <code>ley-line-boundary</code> | <code>u0757:m1</code> | <code>{{Ley Line&#x27;s route}}</code> | <code>Ley Lines</code> | Ley Lines is clearly the topic and the reference confirms the early homebrew discussion, but the marked route may represent additional wording. The complete span cannot safely be reduced to a term or replaced by a feat title. |
| <code>possible-beryl-phrase</code> | <code>u0530:m1</code> | <code>{{It&#x27;s a barrel to talk to us.}}</code> | <code>Beryl</code> | The preceding vision concerns Rai speaking to a friend in the sky, so Beryl may underlie barrel, but the rest of the marked sentence is unclear. A whole-span name replacement would discard or reconstruct ordinary wording. |
| <code>rai-fragment</code> | <code>u1068:m1</code> | <code>{{Rise of 2.}}</code> | <code>Rai</code> | The surrounding discussion is about contacting Rai and the other monks, but Rise of 2. contains additional unrecoverable words or a number. Retain the complete phrase rather than reconstruct it. |
| <code>tollen-love-interest</code> | <code>u1325:m1</code> | <code>{{Beryl&#x27;s}}</code> | <code>Delwath&#x27;s</code>, <code>Beryl&#x27;s</code> | The following centaur banter concerns Delwath, making Delwath&#x27;s plausible, but Beryl is also a real character in this conversation and could be a spoken name slip. The sources establish identities, not which name was actually spoken here. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording</code> | <code>u0253:m1</code>, <code>u0255:m1</code>, <code>u0272:m1</code>, <code>u0301:m1</code>, <code>u0922:m1</code>, <code>u1040:m1</code>, <code>u1200:m1</code>, <code>u1363:m1</code> | These spans contain ordinary wording, questions, rules or numeric discussion, rather than complete identifiable names or setting terms. In particular Everyone occurs in an explanation of the research options and is not established as a named facility. Retain all wording unchanged. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-134/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T045615431361Z-ddf05d82/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-134/cleaned/dunmari-frontier-134-source-cleaned.md</code>
Before SHA-256: <code>37c805d8e56ff44c476594b0291b133d8e9a0717d823433905976bef7c19db47</code>
Planned after SHA-256: <code>d36a95579407b37751866fdcbf48fe0992cc9fa1878fec785caa47903b3b661d</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
