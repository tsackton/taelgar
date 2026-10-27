---
lintedAt: "2026-10-20T12:23:59-04:00"
lintVersion: "3.5"
displayDefaults: {defArt: ""}
tags: [place, status/check/lint]
typeOf: building
typeOfAlias: fey manor
name: "Lord Endless Ending's Manor"
aliases: ["Lord of the Ended Revel's Manor"]
whereabouts: Twilight Kingdom
dm_owner: none
dm_notes: none
POV: 1740
---
```taelgar-header
```


Lord Endless Ending's Manor is a fey manor in the [[Twilight Kingdom]], caught in the repeated ending of a party hosted by [[Lord Endless Ending]].

The manor stands behind a silver gate and a great hedgerow, with long lawns sloping toward a river. Patios, open doors, and uneven light from lanterns whose candles are already burning low spill out of the house, where a party is ending. The party is always ending: glasses are empty, food is picked over, musicians call for one more piece, and guests linger in small groups as if departing, without ever quite leaving.

The manor itself has a long covered porch, with several open doorways inside, where a library, a grand ballroom, and many other rooms can be found. Notable is a large and prominent grandfather clock, of strange design with many numbers on its face.

> [!image]
> ![[the-endlessly-ending-party.jpg]]
> *The endlessly ending party at Lord Endless Ending's Manor*

%%^Date:1740-10-07%%
However, now, the revel has ended. The paper lanterns are extinguished, the grounds are silent, and the guests have departed. The manor remains standing as the home of the [[Lord Endless Ending|Lord of the Ended Revel]], who watches from an upper room toward the [[Twilight Promontory]] and remembers the child they befriended before the party began.
%%^End%%

%%^Metadata:names:v1%%
- {"name": "Lord Endless Ending's Manor", "language": "unknown"}
- {"name": "Lord of the Ended Revel's Manor", "role": "alias", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a DR 1740 description of the endlessly ending revel, with aftermath in the existing Date:1740-10-07 block; the undated revel descriptions still require a human decision about their visibility after that cutoff.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter ordering and added persistent name and temporal metadata.

### Validated judgments
- Both displayed manor names are transparent English descriptive titles and need no pronunciation.
- The dated aftermath is supported by Lord Endless Ending’s current account and the conclusion of [[Lost in the Feywild - Episode 07]]; no date blocks were changed.

### Open findings

- [ ] **Warning — temporal.mixed_current_state:** The undated opening says the manor is “caught in the repeated ending” and the next paragraph says “The party is always ending,” while Date:1740-10-07 says the revel has ended and the guests have departed. After the cutoff both incompatible present states remain visible. Preserve the lasting manor identity outside date blocks and propose the smallest before-layer for the repeated revel: replace the opening paragraph with “Lord Endless Ending’s Manor is a fey manor in the [[Twilight Kingdom]].”, then insert `%%^Date:1740-10-07b%%` before “The manor is caught in the repeated ending of a party hosted by [[Lord Endless Ending]].” followed by the existing second paragraph unchanged, and close that before-layer with `%%^End%%` before the paragraph beginning “The manor itself has a long covered porch”. Keep the existing aftermath block. This is a visibility-changing proposal requiring human adoption. Confirm the intended cutoff against [[Lost in the Feywild - Episode 07]], dated DR 1740-10-06; the currently authored next-day cutoff may be intentional and was not automatically changed.
%%^End%%
