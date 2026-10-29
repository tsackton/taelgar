# Campaign interaction extraction — review materials

## Current reviews

**Start with the [new v6 session reviews](v6/README.md)** for the YAML-integrated process. The [ten-session v5 directory](v5/README.md) remains available for comparison. Each session opens with its entity list, followed by overviews, vault matches, confidence and review questions. Quotes and interactions expand beneath each entity; scenes are linked supporting context. The [model overview](MODEL_OVERVIEW.md) explains the agreed structured model; [bulk review and preprocessing](WORKFLOW_DISCUSSION.md) describes the adopted workflow.

The current executable baseline is **v6, session-YAML-owned metadata with transcript-only interaction enrichment**. It prefers registered polished transcripts while retaining original UID ranges. Processing evidence includes excluded blocks and reasons, input fingerprints, metadata findings and separate semantic review. The new sample uses the two currently registered polished bundles, Dunmar 10 and 41; it is an availability sample, not a representative cross-campaign trial. This is a design checkpoint, not a deployed Taelgarverse feature.

[Extraction skill](../../.agents/skills/extract-campaign-interactions/SKILL.md) · [JSON format](../../.agents/skills/extract-campaign-interactions/references/format.md) · [Operations](../../.agents/skills/extract-campaign-interactions/references/operations.md) · [Current trial index](v6/README.md) · [Historical v5 trial](v5/README.md)

## Historical v3 reviews

| Session | Review | NPC cards | Item cards | JSON |
| --- | --- | --- | --- | --- |
| Dunmari 8 | [Review](v3/dunmari-frontier-008/review.md) | [NPCs](v3/dunmari-frontier-008/npcs.md) | [Items](v3/dunmari-frontier-008/items.md) | [JSON](v3/dunmari-frontier-008/extraction.json) |
| Dunmari 60 | [Review](v3/dunmari-frontier-060/review.md) | [NPCs](v3/dunmari-frontier-060/npcs.md) | [Items](v3/dunmari-frontier-060/items.md) | [JSON](v3/dunmari-frontier-060/extraction.json) |
| Dunmari 108 | [Review](v3/dunmari-frontier-108/review.md) | [NPCs](v3/dunmari-frontier-108/npcs.md) | [Items](v3/dunmari-frontier-108/items.md) | [JSON](v3/dunmari-frontier-108/extraction.json) |
| Mawar 2 | [Review](v3/mawar-adventures-002/review.md) | [NPCs](v3/mawar-adventures-002/npcs.md) | [Items](v3/mawar-adventures-002/items.md) | [JSON](v3/mawar-adventures-002/extraction.json) |
| Lost in the Feywild 6 | [Review](v3/lost-in-the-feywild-006/review.md) | [NPCs](v3/lost-in-the-feywild-006/npcs.md) | [Items](v3/lost-in-the-feywild-006/items.md) | [JSON](v3/lost-in-the-feywild-006/extraction.json) |

Each session folder also contains `evidence.md` with expanded excerpts. The review links use repository-relative paths; transcript line links open GitHub's source view. Source JSON retains its original vault-relative paths and hashes.

## Earlier experiments

- [Initial random sample](review.txt): illustrative passages from Dunmari 10, 12 and 59; [data](interactions.json).
- [Dunmari 11 prototype](session-011/review.txt): early scene/NPC format; [data](session-011/extraction.json).
- [Dunmari 8](session-008/review.md) and [Dunmari 60](session-060/review.md): first skill trials.
- [v2 trials](v2/README.md): NPC-focused predecessor.
- [v4 mixed-source experiment](v4/README.md): **superseded**. Its note-derived events are excluded from the current baseline. Preserved for design history only.

Historical builders and archived validators are included as work materials, with their original local paths and version assumptions. The active validator and tests live with the skill. Extraction data and transcript sources have not been rewritten for publication; only review navigation has been made portable.

## Validation

From the repository root:

```sh
PYTHONDONTWRITEBYTECODE=1 python -m unittest discover -s .agents/skills/extract-campaign-interactions/scripts
python .agents/skills/extract-campaign-interactions/scripts/validate.py \
  --vault . --input _sessions/interaction-pilot/v3/dunmari-frontier-108/extraction.json
```

The v3 examples remain readable through the compatibility validator. Current checks cover schema/provenance, preparation, review state protection and replay of published review decisions. The batch indexes distinguish completed review executions from high-confidence facts ready for use; structural validation alone cannot approve a claim.
