---
lintedAt: "2026-10-20T07:57:56-04:00"
lintVersion: "3.5"
tags: [meta, status/check/lint]
typeOf: hoard
campaign: Dunmar Frontier
name: Tower of the Colossus Treasure
POV: 1749
---

## Treasure from the Tower of the Colossus

- A [[Taurion's Manual of Golems|manual of stone golems]], found in the basement storeroom guarded by a stone golem.
- Material for making spell scrolls, containing enough inks and special paper to produce 4 scrolls: 3 up to 3rd level, and 1 up to 5th level. Each scroll requires 8 hours of work to produce, using the kit.
- Four spell scrolls: Sending, Private Sanctum, Reverse Gravity, and Passwall
- Six magical lenses of a variety of sizes, once apparently part of a telescope. %%SECRET[v2:819d3a95b8db19dac7ec2448073099a0]%%
- A collection of about 150 scrolls, highly fragile and prone to disintegration if handled. A sampling of six scrolls revealed poems and plays, in Drankorian and Elvish. All but one particularly sturdy one left behind in the tower. %%SECRET[v2:58595e496a592ce6628b41e2c8da8381]%%
- Copies of five scrolls read in the tower, but not brought along for risk of disintegration. 

%%SECRET[v2:fd739bcc57f659de4bb0519347860cb9]%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added explicit `name`, `campaign: Dunmar Frontier`, and `POV` metadata.
- Applied objective corrections: `to produce, with the kit` → `to produce, using the kit.`; `telepscope` → `telescope`.

### Validated judgments
- The campaign-meta ledger does not require name or temporal-interpretation blocks; its substantive inventory is sufficient for its record-keeping role.
- Local-only SECRET material was reviewed and preserved; no private contents are reproduced in this report.

### Open findings

- [ ] **Warning — correctness.quantity_ambiguity:** The lenses bullet records six magical lenses, whereas [[Party Treasure#Unusual Materials or Components]] records four from this same hoard. [[Session 104 (DuFr)]] confirms the recovery but gives no lens count. Resolve whether six were recovered and only four later retained, or whether one ledger has a mistaken count. Preserve the original count until that choice is established; then either change this bullet to ‘Four magical lenses of a variety of sizes, once apparently part of a telescope’ or retain six and add the documented later disposition of the other two. No quantity or fate has been inferred.
%%^End%%
