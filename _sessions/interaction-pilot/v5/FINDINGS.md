# Findings from the ten-session trial

All ten sampled transcripts were processed: **165 scenes, 197 entities and 358 interactions** across six campaigns. The sample was fixed before extraction, using seed `20261028` and a population of 153 available transcripts. No sessions were replaced after seeing their results.

The rebuilt [entity review directory](README.md) displays **195 entities**: two ordinary-treasure entries are omitted under the updated inclusion rule. Original JSON and review decisions are preserved. Transcript links use the reviewed source version at `5c88c732c`; Dunmar 57, 58 and 64 have newer transcripts, so those pages explicitly identify the extraction as historical.

**191 of 197 entity records passed critical review. Eight session metadata groups remain provisional:** six have chronology questions, and the two Dragonets sessions lack individual vault pages for their participating PCs. There are 14 critical queue entries overall. These are unresolved questions, not a measured count of factual errors.

## Useful places to start

| Review | What it tests |
| --- | --- |
| [Labyrinths 2](labyrinths-of-the-lost-002/review.md) | A whole ghost conversation, multiple quotes, important clues, a recording gap and a corrected companion alias. |
| [Mawar 3](mawar-adventures-003/review.md) | A complex tomb expedition, items, and Wazir participating in a DM-narrated epilogue despite his player’s absence. |
| [Feywild 1](lost-in-the-feywild-001/review.md) | Conversations spanning locations, magical household items, and a destination that the party has not yet reached. |
| [Dunmari 57](dunmari-frontier-057/review.md) | A major NPC with several quotes, spiritual visions, collective entities and conservative confidence judgments. |
| [Dragonets 2](dragonets-002/review.md) | Unlinked PCs, ambiguous names, talking objects and a cutaway witnessed by the audience rather than the party. |

## What the review changed

Review corrected attendance, midnight boundaries, interaction modes and quote attribution; it also found a few omitted consequential objects. Existing beat data helped some reviews locate chronology questions. It was not treated as independent confirmation when it repeated a manifest date or introduced detail absent from the transcript.

Most remaining bulk-review work concerns **calendar anchors and PC-page matching**. Resolving those once per campaign would likely help more than repeatedly regenerating scene summaries. Confidence categories still need calibration; a missing optional vault link should not alone imply an uncertain entity.

Two choices deserve feedback: how selective to be about magical tools/consumables, and how to classify divine collectives or specific speaking plants. Wazir also exposes the distinction between a participating character and an attending player.

The Dunmari 57 independent audit records two minor wording/quote-framing issues and an uncertain omitted name after its correction round. They remain visible observations for review.

## Limits of the trial

Agents performed extraction and semantic review; Python handled preparation, validation, review application and rendering. Nine sessions received a different agent’s semantic review; Dunmari 57 received a separate sequential review and then an independent targeted audit. Some reviewers reread entire transcripts for calibration, while others used targeted evidence windows. This trial does not measure API cost, bulk throughput or calibrated confidence accuracy.

The audit preserves each initial extraction and its evidence-backed decisions, permits one correction/recheck round, protects human-reviewed claims, and binds outputs to the original sample. All ten chains pass; 53 automated infrastructure tests pass. The output is a review prototype, not a deployed Taelgarverse feature.
