---
headerVersion: 2023.11.25
lintedAt: "2026-10-20T07:49:48-04:00"
lintVersion: "3.5"
tags: [object, status/check/lint]
typeOf: sword
subTypeOf: cursed
destroyed: 1748-11-20
name: Medusa Blade
whereabouts: Havdar
knownTo: [dufr]
POV: modern
---
# The Medusa Blade
>[!info]+ Information  
> (cursed sword)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`  
>> `$=dv.view("_scripts/view/get_Whereabouts")`

This longsword, of unknown make, is decorated with reptilian motifs, and radiates transmutation magic. 

It was taken from [[Agata's Lair]] by the [[Dunmar Fellowship]] and gifted to [[Havdar]]. Later, the [[Dunmar Fellowship]] learned it was a cursed sword, and responsible for turning [[Havdar]] to stone at one point, along with his increasing paranoia in the fall of DR 1748. Grants the bearer the power to turn those they strike to stone, but will turn on the bearer as well, if given the chance. [[Session 69 (DuFr)|Destroyed]] by the [[Bahrazel]] at [[Riswynn]]'s request, freeing [[Havdar]] of its curse.
 
 %%SECRET[v2:b0dd651ac8b1d7fafb0da0e04182465a]%%

%%^Metadata:names:v1%%
- {name: Medusa Blade, language: unknown}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: a broadly modern retrospective account through the sword’s destruction in DR 1748; the undated present-tense description of its appearance and powers preserves an earlier layer requiring human reconciliation.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Added an explicit name, `knownTo: [dufr]`, persistent primary name metadata, and `POV: modern` with retrospective temporal coverage; normalized frontmatter order.
- Corrected “it was cursed sword” to “it was a cursed sword”.

### Validated judgments
- [[Session 69 (DuFr)]] supports the recorded destruction on DR 1748-11-20 and Havdar’s release from the curse.
- The ordinary name “Medusa Blade” needs no pronunciation guide; its in-world naming language is not established.
- Reviewed the SECRET block; any recovery proposal remains confined to the private handoff.

### Open findings

- [ ] **Warning — temporal.mixed_current_state:** The undated opening says the sword “is decorated” and “radiates transmutation magic”, and its power description says it “will turn on the bearer”, while the same article and [[Session 69 (DuFr)]] establish its destruction. Choose a consistently retrospective account, or explicitly retain and date the earlier description. A bounded retrospective candidate is: “This longsword, of unknown make, was decorated with reptilian motifs and radiated transmutation magic.” Replace the powers sentence with: “It granted the bearer the power to turn those they struck to stone, but would turn on the bearer as well, if given the chance.” Retain the supported destruction and release. Any new `Date:*` wrapper remains a human visibility decision.
%%^End%%
