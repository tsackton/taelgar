# 10-session interaction trial

[Findings and suggested starting points](FINDINGS.md) · [Model overview](../MODEL_OVERVIEW.md)

Schema v5 · Agent extraction followed by a separate semantic review · Existing beats used only as optional review hints.

This is a prototype of the extraction and review process, not an automatic promotion of all records into canon. Medium/low critical records remain provisional.

Seed: `20261028`. 10 sessions selected without replacement from 153 available transcripts, with campaign variety guaranteed before filling remaining slots.

| Session | Scenes / entities / interactions | Critical metadata | Provisional entities | Review |
| --- | --- | --- | --- | --- |
| labyrinths-of-the-lost-002 | 23 / 12 / 29 | Ready | 0 | [Cards](labyrinths-of-the-lost-002/review.md) · [JSON](labyrinths-of-the-lost-002/session.json) |
| mawar-adventures-003 | 21 / 23 / 48 | medium · provisional | 0 | [Cards](mawar-adventures-003/review.md) · [JSON](mawar-adventures-003/session.json) |
| dragonets-002 | 11 / 28 / 38 | low · provisional | 1 | [Cards](dragonets-002/review.md) · [JSON](dragonets-002/session.json) |
| lost-in-the-feywild-001 | 12 / 18 / 31 | Ready | 0 | [Cards](lost-in-the-feywild-001/review.md) · [JSON](lost-in-the-feywild-001/session.json) |
| into-the-chasm-004 | 13 / 29 / 50 | medium · provisional | 0 | [Cards](into-the-chasm-004/review.md) · [JSON](into-the-chasm-004/session.json) |
| dunmari-frontier-064 | 12 / 24 / 43 | medium · provisional | 0 | [Cards](dunmari-frontier-064/review.md) · [JSON](dunmari-frontier-064/session.json) |
| dunmari-frontier-058 | 18 / 15 / 38 | medium · provisional | 1 | [Cards](dunmari-frontier-058/review.md) · [JSON](dunmari-frontier-058/session.json) |
| dunmari-frontier-007 | 18 / 15 / 20 | medium · provisional | 1 | [Cards](dunmari-frontier-007/review.md) · [JSON](dunmari-frontier-007/session.json) |
| dragonets-001 | 16 / 15 / 26 | low · provisional | 0 | [Cards](dragonets-001/review.md) · [JSON](dragonets-001/session.json) |
| dunmari-frontier-057 | 21 / 18 / 35 | medium · provisional | 3 | [Cards](dunmari-frontier-057/review.md) · [JSON](dunmari-frontier-057/session.json) |

Execution coverage: **10/10 reviewed**. A reviewed execution may still have provisional critical facts.

## What to critique

- Are scenes divided usefully, and do conversations remain whole?
- Are the selected NPCs, items and organizations useful without becoming exhaustive creature lists?
- Do the quotes and short summaries make the source worth opening?
- Are the unresolved critical questions specific enough for fast review?

Each folder preserves the initial extraction, digest-bound review decisions, any one-round correction candidate, final session, execution evidence and unresolved queue. Links open the original source range. AI summaries are navigation aids.

The Python commands prepare inputs, validate provenance, apply externally authored review judgments and render results. Agents perform semantic extraction and review; this trial does not measure autonomous API cost or calibrated confidence accuracy.
