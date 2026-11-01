# Importance within one session

`entities[*].importance` is exactly `star`, `supporting`, or `cameo`. Assess it
from the complete session, relative to the other non-PC entities. A character's
importance elsewhere, later identity, or extensive vault page cannot raise this
session's tier. PCs remain the real protagonists and are not the comparison bar.

| Tier | Test |
| --- | --- |
| `star` | Does this entity substantially drive this session as a key ally, enemy, or central participant in important encounters? A sustained decisive encounter can suffice; repeated appearances alone cannot. Usually zero, one, or two; a comparably important group can justify more. |
| `supporting` | Is there at least one meaningful scene centered on this entity, such as a substantive conversation or negotiation? A distinctive consequential interaction can qualify without speech. Routine combat against an unnamed creature does not suffice. |
| `cameo` | The entity qualifies for the inventory, but lacks that meaningful scene-centered role. Brief introductions, mentions, discoveries, and item uses often belong here. |

Apply the standard to NPCs, divine beings, items, and organizations. For an item,
consider its role in the action and decisions, not just how much time the players
spend discussing its rules. For a group, assess the group actually mapped, without
automatically giving every member its tier. Neither a proper name nor anonymity
determines importance.

The hierarchy is qualitative. Do not score word counts, count occurrences, reserve
star slots, require a minimum number of stars, or impose a hard maximum. Compare
the entire proposed inventory before finalizing. A supporting scene need not be
an entire geographic scene-map span; scene maps remain optional.

## Dunmari Frontier 99 calibration

These are the user's calibration judgments for this session. They specify
importance, not blanket approval of identities, matches, or previous cuts.

| Entity | Tier | Extraction implication |
| --- | --- | --- |
| Caloria | `cameo` | The earlier remains/bracelet passage retained too much surrounding search and recovery. A substantive mention or discovery can be brief even when it matters to someone else's story. |
| Dorian | `supporting` | His affliction, the party's intervention, and his response form a meaningful scene. The tested level of detail was broadly appropriate. |
| Kazuro | `supporting` | The conversation and offer of a school justify a complete focused exchange, without promoting him to a session star. |
| Sentient Ocean | `supporting` | Preserve its challenge and relevant perceptions or responses. Underwater preparation is not its interaction. The session ends before an answer. |
| Martino | `cameo` | The short passage about his sailing knowledge and injury was appropriately brief. |
| Immovable Rod | `cameo` | The short rowing exchange is enough. Being the focal object of two useful lines does not make it supporting. |

This set needs no star. It is not the whole inventory; it does not assign tiers
to the other session-99 entities or to these entities in other sessions.

## Handoff to extraction

The focal entity of a passage and a session-level `star` are different concepts.
Any tier may be selected as the focus. The tier changes how much surrounding
material is useful:

- Stars can warrant several substantial interactions across the session.
- Supporting entities warrant their meaningful scene, cut more tightly around
  the interaction and its necessary setup than for a star.
- Cameos warrant much tighter cuts: often one sentence or a short exchange about
  the entity, with almost no surrounding background.

These are selection priorities, not length caps or permission to rewrite. Preserve
questions and answers, actions and responses, uncertainty, and necessary outcomes.
Never inflate a cameo to justify a long excerpt or truncate a meaningful exchange
solely to hit a word count. Keep all retained transcript wording verbatim.

Items have a tighter default at every tier: extract the minimum needed to
understand their use or acquisition. Preserve original setting history or lore
fully as a coherent account, including a custom history for a standard item;
routine rules text is not that exception. Mark actual Mirror of the Past
examinations with `examinedInMirrorOfPast: true`, independently of importance.
See the [item extraction rules](../../extract-entity-passages/SKILL.md#items-brief-use-or-acquisition-complete-original-lore).

## Existing maps and review

V3 maps have no importance assessment. Their existing identity decisions remain
usable, but missing importance is not `cameo`. An intentional v4 upgrade requires
assessment of every included entity from the whole session and a guarded save.
Preserve stable IDs, labels, matches, and evidence unless separately corrected.
Do not silently transfer human approval of an identity into approval of a new
importance judgment. Recheck the expanded whole record before its review status
claims completion; preserve earlier accepted identity decisions throughout.
