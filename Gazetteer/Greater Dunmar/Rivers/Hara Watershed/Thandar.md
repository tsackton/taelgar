---
lintedAt: "2026-10-20T11:04:00-04:00"
lintVersion: "3.5"
tags: [place, status/check/lint]
typeOf: waterway
typeOfAlias: river
name: Thandar
pronunciation: TAHN-dur
whereabouts: Hara Watershed
dm_owner: none
dm_notes: color
POV: modern
---
```taelgar-header
```

The Tandar flows about 240 miles from its source in the [[Sentinel Range|Sentinels]] to its confluence with the [[Hara]] on the [[Varashan]]. The upper reaches of the Tandar are swift flowing and marked by rapids and gorges as the river cascades from the steep slopes of the Sentinels to the plains below. 

As the Tandar enters the flat plains of the [[Hara Basin]], it winds slowly southwest across the eastern edge of the [[Songara Plains]]. 

Near the confluence with the [[Hara]] stands a [[Stoneborn Statue Dungeon|massive statue of stoneborn warrior]], of ancient and unknown construction. 

%% notes
perhaps like https://en.wikipedia.org/wiki/Zanskar_River

Probably doesn't belong in this note (rather in the Sentinels note) but I think the Tandar descends from the steepest section of the southern Sentinels, between the two passes
%%

%%^Metadata:names:v1%%
- {name: "Thandar", language: "unknown", pronunciation: "TAHN-dur", status: "documented"}
%%^End%%

%%^Metadata:map:v1%%
locations:
  - {role: source, feature: Sentinel Range, map: world, locator: }
  - {role: outlet, feature: Hara, map: world, locator: }
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern river geography; the article describes the course, terrain, and confluence without an established narrower historical state.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the objective typo “tihnk” to “think” in the existing editorial comment, preserving its uncertainty.
- Normalized frontmatter while preserving its values; recorded the existing accepted pronunciation in a documented name entry, added a typed map block with the established source and outlet features, and recorded a broadly modern viewpoint with temporal notes.

### Validated judgments
- The river’s course and confluence are consistent with [[Hara]] and [[Hara Watershed]]; the existing real-world inspiration and tentative headwaters comment remain noncanonical editorial notes.
- The course, terrain, and distinguishing statue are sufficient for this river’s reference role. No narrower historical snapshot is established.

### Open findings

- [ ] **Warning — correctness.internal_conflict:** Frontmatter and filename use “Thandar,” while the title and article use “Tandar.” [[Hara]], [[Hara Watershed]], and [[Hara Basin]] use `[[Thandar]]`. Confirm the intended displayed form. If Thandar is intended, use `# Thandar` and replace the four article occurrences of Tandar, including the existing comment, with Thandar; otherwise change metadata `name` and the primary name entry to Tandar and explicitly record any intended alternate form. Preserve the filename and existing accepted pronunciation until that decision is made.
- [ ] **Warning — metadata.map_location_missing:** The typed waterway block identifies the [[Sentinel Range]] source and the [[Hara]] outlet, but both `locator` values are blank. Supply their established positions on the world map in the existing source and outlet entries; no coordinates are established by the textual sources reviewed, so none were inferred.
- [ ] **Suggestion — dm.notes_no_local_evidence:** No `_DM_` notes found; verify `dm_notes`. The search checked filenames, names and aliases, backlinks, and the Thandar, Tandar, and Tandhar variants in local DM and relevant shared sources. Keep `dm_notes: color` unless the human attestation is deliberately revised; it may represent remembered information or another off-vault source.
%%^End%%
