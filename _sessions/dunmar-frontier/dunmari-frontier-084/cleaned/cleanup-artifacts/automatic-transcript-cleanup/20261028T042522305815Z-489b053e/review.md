# Automatic transcript cleanup

Session: <code>dunmari-frontier-084</code>
Status: <code>applied</code>
Pass: <code>names-v1</code>

| Markers before | High | Supported | Marker-only removals | Name review | Outside scope | Markers after | Undone |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 25 | 3 | 2 | 0 | 2 | 18 | 20 | 0 |

Counts describe this run and its recorded reversions; other later edits are excluded.

## Applied replacements

| Group | Confidence | Marker | Before | After | Reason | Evidence | Reverted |
| --- | --- | --- | --- | --- | --- | --- | --- |
| <code>chalyte-spellbook</code> | high | <code>u0121:m1</code> | <code>{{chalet}}</code> | <code>chalyte</code> | The same named spellbook is being inventoried twice; the session record explicitly identifies Casian&#x27;s chalyte spellbook and the material note establishes chalyte. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 84 (DuFr).md</code>, <code>Things/Materials/Chalyte.md</code> | no |
| <code>chalyte-spellbook</code> | high | <code>u0276:m1</code> | <code>{{chill out}}</code> | <code>chalyte</code> | The same named spellbook is being inventoried twice; the session record explicitly identifies Casian&#x27;s chalyte spellbook and the material note establishes chalyte. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 84 (DuFr).md</code>, <code>Things/Materials/Chalyte.md</code> | no |
| <code>guildgate</code> | high | <code>u0304:m1</code> | <code>{{Gilgate}}</code> | <code>Guildgate</code> | The wealthy Tollen guild ward uniquely matches Guildgate, whose reference note places merchant palaces and guildhalls there. | <code>Gazetteer/Greater Sembara/Tollen/Wards/Guildgate.md</code> | no |
| <code>repeated-chalyte-spellbook</code> | supported | <code>u0538:m1</code> | <code>{{Jay White Spellbook, Casian&#x27;s Jay White Spellbook}}</code> | <code>chalyte spellbook, Casian&#x27;s chalyte spellbook</code> | The repeated item label accompanies placing Casian&#x27;s spellbook beside the grimoire; the session record identifies that traded book as the chalyte spellbook. Jay White is a plausible ASR rendering of chalyte, with no competing book established. | <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 84 (DuFr).md</code>, <code>Things/Materials/Chalyte.md</code>, <code>People/Chardonians/Casian.md</code> | no |
| <code>denoqai-cuisine</code> | supported | <code>u0984:m1</code> | <code>{{den}}</code> | <code>Deno&#x27;qai</code> | While choosing human dishes from his travels, Delwath names another people after Dunmar. His documented stay and feast among the Deno&#x27;qai strongly favor Deno&#x27;qai for the clipped den; Dunmari was considered but is already represented by the preceding Dunmar reference. | <code>Groups/Cultures/Deno&#x27;qai Tribes/Deno&#x27;qai.md</code>, <code>Campaigns/Dunmari Frontier Campaign/Session Notes/Session 53 (DuFr).md</code> | no |

## Name decisions left for review

| Group | Markers | Before | Candidates | Reason |
| --- | --- | --- | --- | --- |
| <code>grash-in-damaged-phrase</code> | <code>u0834:m1</code> | <code>{{We&#x27;re crossing the mirror}}</code> | <code>Grash</code> | The next speaker immediately mentions Grash, making a Grash-and-mirror reference plausible, but the marked span contains a whole damaged clause with uncertain words and boundaries. Do not reduce it to a name or reconstruct the clause. |
| <code>kassi-in-damaged-phrase</code> | <code>u0093:m1</code> | <code>{{So you don&#x27;t cosy}}</code> | <code>Kassi</code> | The librarian who is Basu&#x27;s partner is Kassi, but the complete marked span includes unclear surrounding words. Replacing it with the name alone would discard speech; reconstructing the phrase exceeds this pass. |

## Outside this pass

| Group | Marker IDs | Reason |
| --- | --- | --- |
| <code>ordinary-wording-and-numbers</code> | <code>u0006:m1</code>, <code>u0128:m1</code>, <code>u0129:m1</code>, <code>u0147:m1</code>, <code>u0208:m1</code>, <code>u0255:m1</code>, <code>u0396:m1</code>, <code>u0409:m1</code>, <code>u0569:m1</code>, <code>u0676:m1</code>, <code>u0781:m1</code>, <code>u0783:m1</code>, <code>u0788:m1</code>, <code>u0832:m1</code>, <code>u0933:m1</code>, <code>u0989:m1</code>, <code>u1240:m1</code>, <code>u1781:m1</code> | Numbers, mechanics, ordinary conversation, and damaged non-name phrases are outside this name/setting-term pass. The cooking instruction and Frankar follow-up cannot be repaired as complete name spans. |

## Reversion

Use the exact journal path with `undo`; add `--marker-id uNNNN:mN` to undo selected replacements.

```text
python .agents/skills/automatic-transcript-cleanup/scripts/name_pass.py undo --journal '/Users/tim/Library/Mobile Documents/iCloud~md~obsidian/Documents/Taelgar/_sessions/dunmar-frontier/dunmari-frontier-084/cleaned/cleanup-artifacts/automatic-transcript-cleanup/20261028T042522305815Z-489b053e/journal.json'
```

## Provenance

Transcript: <code>_sessions/dunmar-frontier/dunmari-frontier-084/cleaned/dunmari-frontier-084-source-cleaned.md</code>
Before SHA-256: <code>252f8295e2a3b175f129185da32f567521daf4d2f750d148cb8cf3a1dbd4299b</code>
Planned after SHA-256: <code>7e289d35f8b6c117e912aa1f0ef43d7e0c6a550130dc722387b622d8c006a45c</code>

## Downstream artifacts

Existing cleanup assessments, acceptance records, beats, facts, recaps, and polished transcripts were not refreshed. Their fingerprints or wording may be stale. Remaining uncertainty is not human-accepted by this pass.
