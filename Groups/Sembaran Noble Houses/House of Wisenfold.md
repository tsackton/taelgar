---
lintedAt: "2026-10-19T07:04:00-04:00"
lintVersion: "3.5"
tags: [group, status/check/lint]
typeOf: family
name: House of Wisenfold
dm_owner: none
dm_notes: none
POV: modern
---
```taelgar-header
```

The Wisenfold family has significant presence along the upper Wistel, especially south and west of [[Gowerbourne]]. 

%% This exists merely as a historical family but felt worth keeping around in case someone needs the name of an important noble family in the  %%

%%^Campaign:none%%
### Members
```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Metadata:names:v1%%
- {"name": "House of Wisenfold", "language": "unknown", "pronunciation": "HOUSE of WYE-zen-fohld", "status": "proposed", "notes": "No recorded pronunciation was found for Wisenfold. The English strand of the Sembaran analogue in [[Languages]] suggests sounded w, long i in wise, voiced s, an unstressed en, and long o in fold, with first-syllable stress. A short-i WIZ-en-fohld reading is also possible; the proposal remains uncertain."}
%%^End%%

%%^povNotes:v1%%
Temporal coverage: broadly modern family presence along the upper Wistel; the historical editorial reminder does not establish a narrower speaking date.
%%^End%%

%%^Lint%%
## Taelgar note lint

### Applied changes
- Normalized frontmatter order and added the explicit subject name.
- Added persistent name metadata and the article’s POV and temporal-coverage note.
- Normalized `Campaign:None` to `Campaign:none`; the current exporter casefolds both to the same private sentinel, preserving filtered visibility.

### Validated judgments
- No additional validated judgments.

### Open findings

- [ ] **Warning — metadata.names_unresolved_status:** Confirm the proposed full pronunciation `HOUSE of WYE-zen-fohld` in `Metadata:names:v1`. No source gives an accepted Wisenfold pronunciation. The English strand of the Sembaran analogue in [[Languages]] motivates sounded w, long i in wise, voiced s, unstressed en, long o in fold, and first-syllable stress. A short-i WIZ-en-fohld reading is also plausible. Accept it by copying it to frontmatter and marking the entry documented, or supply the intended pronunciation. The form’s language remains uncertain unless independently established.

%%^End%%
