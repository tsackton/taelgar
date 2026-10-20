---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T09:38:32-04:00"
lintVersion: "3.5"
tags: [source, status/check/lint]
campaign: Cleenseau
name: Letter from Rosalind (January 14th)
POV: 1720
---
# Letter from [[Rosalind Essford|Rosalind]] to the [[Heroes of Cleenseau]]
_Received January 15th, in [[Champimont]]_

Friends:

I have reached Wisford, and am continuing onward to Embry with all haste. I wept for the land, each village we pass has the same tale of woe. Some have been mysteriously spared, and have seen no dead rise from the ground or walk from afar into their lives. Others have seen a mere handful, one or two. The worst is that rare village where it seems the dead outnumbered the living. In one hamlet, all that remained were two small children, hiding in an attic, and a dozen skeletons, aimlessly pacing through the village square. We dispatched the skeletons, and I have taken the children under my wing. They have not yet spoken.

There is much news from Wisford, and I do not know what to make of it. I had the following story from one of the Duke's stewards, an old friend of my father's:

Four days ago, he said - this would be the 8th, the same day we were riding past Fellburn - news came of hundreds of skeletons converging on Gowerbourne. It seems the whole western part of the Duchy was spared any small problems, and has traded for a large one. By some luck, or perhaps ill fortune, two hundred soldiers from the Army of the South were bivouacked outside of Wisford on their way to Embry. There was an altercation, I hear. The details are unclear, but it seems the major refused to assist the Duke, saying his orders were to march to Embry above all else. There was a mutiny - led by the Duke, I gather - the major is now dead, and the Army marches off for Gowerbourne.

The steward tells me he fears there will be consequences, and the Duke's temper got the better of him. But can I really blame him? The news from Fellburn has certainly reached the Duke, and I know he will ride south as soon as he can.

I will write more when I have news, or reach Embry. I anxiously await any news of how my people are faring in these dark times. I tarry not here, it is best to write me in Embry. 

I hear rumors that several other lords have been summoned to Embry, in particular border lords without ancient title. I do not know what it could mean.

Yours in peace,
Lady Rosalind Essford
The 12th of January, in the blackest year of Robert's reign

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added the Cleenseau campaign identity, explicit display name, and DR 1720 document viewpoint.
- Closed the receipt line’s unmatched emphasis marker and corrected “bivouaced” to “bivouacked”.

### Validated judgments
- The text is a source record: Rosalind’s reports, uncertainties, and hearsay remain attributed to her rather than treated as omniscient facts.

### Open findings

- [ ] **Warning — correctness.internal_date_ambiguity:** The filing/display label says “January 14th”, but the signature says “The 12th of January” and the letter calls January 8th “four days ago”. The receipt line separately says January 15th. These distinguish receipt from composition but leave the 14th unexplained. Confirm the intended composition date; if the signature is authoritative, use the display metadata `name: Letter from Rosalind (January 12th)` while preserving the filename and receipt line. Otherwise correct the signature and relative-date passage together from the intended chronology. Do not silently choose a date or rename the file.
%%^End%%
