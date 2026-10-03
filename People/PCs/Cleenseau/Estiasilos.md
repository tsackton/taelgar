---
headerVersion: 2023.11.25
lintedAt: "2026-10-03T17:51:33-04:00"
lintVersion: "3.5"
displayDefaults: {startStatus: hatched from an egg on}
tags: [person, status/check/lint]
species: mysterious aberration
born: 1719-11-05
pronouns: it/they/him/her
name: "Es\\*tiasilos"
aliases: ["Es*tiasilos"]
affiliations:
  - {org: Heroes of Cleenseau, title: Companion}
knownTo: [clee]
dm_owner: player
dm_notes: important
POV: 1720s
---
# Es\*tiasilos
>[!info]+ Biographical Info  
> A mysterious abberation (it/they/him/her)  
> `$=dv.view("_scripts/view/get_PageDatedValue")`  
> `$=dv.view("_scripts/view/get_Affiliations")`

A strange egg hatched by [[Viepuck]] into a mysterious flying octopus creature. Curious but very alien.

%%^Metadata:names:v1%%
- {"name": "Es*tiasilos", "language": "unknown", "pronunciation": "ehs-tee-AH-see-lohs", "notes": "Cautious spelling-based proposal: initial Es as ehs, ti as tee, a as ah, si as see, and los as lohs. The asterisk is provisionally treated as an unspoken separator; its intended sound or function and the name language are not established.", "status": "proposed"}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: an early-1720s portrait of Viepuck’s familiar, with its hatching in DR 1719 as backstory; later changes are not described.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Corrected the spelling of “aberration” in the species field; the generated header is preserved pending refresh.
- Added `knownTo: [clee]`, a proposed name entry, and temporal metadata.
- Encoded literal asterisks as YAML Unicode escapes in the staged name and alias without changing their parsed values, allowing finalization’s formatter to process them safely.

### Validated judgments
- The short creature description performs its companion-reference role; [[Samuel]] identifies the creature as Viepuck’s familiar, and Cleenseau records corroborate its continuing presence.

### Open findings

- [ ] **Suggestion — editorial.objective_typo:** The generated biographical line still spells “aberration” as “abberation.” Regenerate that line from the corrected species value, preserving its Markdown hard break; the text should read “A mysterious aberration (it/they/him/her).”
- [ ] **Warning — frontmatter.format_unsafe:** The deterministic formatter treats the literal asterisk in the existing name and alias as a YAML-anchor risk, even inside quoted scalars. The YAML parses, and the asterisk is part of the displayed name, not a genuine YAML alias. The staging representation uses equivalent Unicode escapes, but the formatter renders the literal asterisk again, so this conservative warning remains. Correct the formatter’s quoted-scalar handling before a future re-lint; retain the exact parsed name and alias values.
- [ ] **Warning — metadata.names_unresolved_status:** The persistent name entry proposes `ehs-tee-AH-see-lohs` from the spelling alone (Es = ehs, ti = tee, a = ah, si = see, los = lohs), provisionally treating `*` as an unspoken separator. No language or accepted pronunciation is established. Confirm how the asterisk is spoken and accept or revise the proposal; if accepted, copy it to frontmatter and change the entry to `status: documented`.
%%^End%%
