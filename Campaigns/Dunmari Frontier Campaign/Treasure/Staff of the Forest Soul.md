---
lintedAt: "2026-10-20T07:49:48-04:00"
lintVersion: "3.5"
tags: [object, status/cleanup/text, status/check/lint]
typeOf: staff
rarity: unique
name: Staff of the Forest Soul
whereabouts: Kenzo
knownTo: [dufr]
POV: modern
---
```taelgar-header
```

%% disentangle mechanics from text %%

![[staff-of-the-forest-soul.png|left|300]]This staff was constructed by [[Kenzo]] from a branch of the ancient elven tree in [[Tokra]], a relative of the massive trees called God trees by the Deno’qai of the [[Elderwood]]. This staff is a +1 magic quarterstaff. While attuned, this staff has the following additional functions:

-  Forest Ki: Your connection to the soul of the forest allows you to draw on the forest for extra ki. The staff contains a ki reservoir equal to your Wisdom modifier, which you can use interchangeably with your normal ki pool. This ki is restored whenever you take a short rest. 
-  Commune with Nature: Once per day, you can connect yourself to the natural world around you, entering a trance to commune with nature. This has the effect of the  Commune with Nature spell, but may reveal additional information at the DM’s discretion. If you have already used this ability, you can use it again by spending 6 ki. 
-  Speak with Plants: Once per day, you can use the staff to extend your consciousness and allow you to speak with plants, as the Speak with Plants spell. If you have already used this ability, you can spend 4 ki to use it again. 
- Spirit Guidance: You can reach out to the spirits of the Dreamworld through your ki. You can spend 3 ki to cast Augury; you can only do this once per day.
- Death Blessing: You have advantage on Death saving throws. 
- Time Manipulation: When you score a critical hit against a creature with your staff, the creature must make a Wisdom saving throw against your ki save DC. Succeed or fail, the target takes an extra **1d6**![](chrome-extension://gnblbpbepfbfmoobegdogkglpbhcjofh/images/icons/badges/custom20.png) necrotic damage. On a fail, they are also under the effects of the slow spell; they can repeat the save at the end of each turn to end the effect.

The spiritual beings of the [[Azta Lekua|Footprint of the Gods]] carved four tokens on [[Kenzo]]’s staff, each representing a different spiritual ki. 

- Amezza ki: You can spend 3 ki to cast Augury; you can only do this once per day. You also have a pool of Amezza ki, which does not regenerate. You can drain the Amezza ki to enter a trance that allows you to visit the [[Dreamworld]].
- Hutsu ki: You have advantage on death saving throws. You also have a pool of Hutsu ki, which does not regenerate. You can drain this pool to grasp one departing spirit and, if they are willing, return them to the material plane. Choose one creature that has been dead for no more than 24 hours; if the body is intact, you restore them to life.
- Urtaro ki: You have a pool of Urtaro ki, which does not regenerate. You can drain the Urtaro ki to cleanse the spirit of one creature. This removes all conditions, curses, reductions to their ability scores, and reductions to their hit point maximum.
- Ohana ki: When you score a critical hit against a creature with your staff, the creature must make a Wisdom saving throw against your ki save DC. Succeed or fail, the target takes an extra 1d6 necrotic damage. On a fail, they are also under the effects of the Slow spell; they can repeat the save at the end of each turn to end the effect. You also have a pool of Ohana ki, which does not regenerate. You can drain the Ohana ki to enhance your speed and reflexes, granting you the benefits of the Haste spell for the next minute. You do not need to maintain concentration on this effect

The spirit of [[Hralgar]] lingers in the staff, granting you access to storm giant ki. 
- Storm giant ki: You can expend this ki to contact Hralgar or another storm giant elder whose name you know (if you meet/learn about any others). Doing so allows you to meld with the storm giant, allowing you to ask up to 5 questions, which can be answered with no more than a sentence or two. You must ask all your questions, and receive your answers, within no more than 10 minutes. When you break contact, you must make a DC 17 Wisdom saving throw, taking 2d6 lightning damage for each question asked on a failed save, and half as much on a successful save. Once you use this ki, it can be recharged after 24 hours have passed by taking at least 35 points of lightning damage at once.

[[Kaikkea]] briefly inhabited the staff while striking to destroy the scepter, granting you access to ocean ki.
- Ocean ki: You can expend this ki to....

%%^Metadata:names:v1%%
- {"name": "Staff of the Forest Soul", "language": "unknown"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern account of Kenzo’s staff, combining its construction and successive spiritual gifts; the undated mechanics are not a dated progression of its powers.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter; added the explicit display name and knownTo: [dufr] from Kenzo’s construction and use.
- Added a minimal primary name entry and broadly modern POV with temporal coverage metadata; the plain-English title needs no pronunciation.
- Corrected Wisdome to Wisdom and allow you speak to allow you to speak.

### Validated judgments
- status/cleanup/text is supported by the unresolved ocean-ki placeholder and the existing reminder to disentangle mechanics from text; preserved unchanged.
- The staff has substantial setting-specific origin, spiritual relationships and powers, so its unfinished final ability does not make the whole note Underdeveloped.

### Open findings

- [ ] **Suggestion — editorial.prose_clarity:** The final bullet, “Ocean ki: You can expend this ki to....”, leaves a promised usable ability undefined. The nearby [[Kaikkea]] sentence establishes the gift but does not establish a mechanical effect. Supply the intended rule, or replace only the unfinished bullet with `The effect of the ocean ki has not been recorded.` No effect has been invented or inferred from unrelated abilities.
- [ ] **Warning — coverage.later_material_change:** The account of the staff’s spiritual additions omits its durable adornment with the complete remains of [[Jade Piece of Rai's Hand|Rai’s jade hand]]. [[Session 113 (DuFr)]] explicitly describes the completed hand on the staff and the visions it triggers on May 22, 1749. Candidate addition: `By [[Session 113 (DuFr)|May 22, 1749]], the complete remains of [[Jade Piece of Rai's Hand|Rai’s jade hand]] adorned [[Kenzo]]’s staff, which revealed visions of Rai’s actions in the [[Temple of the Eight Divines]].` Decide whether to update the article and temporal coverage, defer with an appropriate human-managed game-update status, or intentionally preserve the earlier account. If later-date filtering is desired, wrap that addition in `%%^Date:1749-05-22%%` and `%%^End%%`; no visibility change has been applied.
- [ ] **Suggestion — syntax.nonportable_image:** The Time Manipulation bullet includes the empty image `![](chrome-extension://gnblbpbepfbfmoobegdogkglpbhcjofh/images/icons/badges/custom20.png)` between its explicit die value and damage type. That browser-extension asset is not a portable vault image. Remove just this image token, leaving `**1d6** necrotic damage`; the independently stated damage and effect need no replacement icon.
%%^End%%
