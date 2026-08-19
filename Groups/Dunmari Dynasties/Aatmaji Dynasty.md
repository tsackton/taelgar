---
subTypeOf: dynasty
headerVersion: 2023.11.25
lintedAt: "2026-08-19T09:51:53-04:00"
lintVersion: "2.1"
displayDefaults: {boxInfo: "<ancestry:UA> <subtypeof>"}
tags: [group, status/check/lint]
typeOf: family
ancestry: Dunmari
name: Aatmaji dynasty
dm_owner: tim
dm_notes: important
---
%%^Metadata:article:v1%%
profile: group
mode: historical reference
pov: retrospective current-setting account
%%^End%%

%%^Metadata:names:v1%%
- {name: Aatmaji, role: dynastic name, language: Dunmari, pronunciation: AAT-mah-jee, status: proposed}
%%^End%%

%% have a full list of Samraats of this dynasty in DM notes FWIW%%

# The Aatmaji Dynasty
>[!info]+ Information  
> A [[Dunmar|Dunmari]] dynasty  
> `$=dv.view("_scripts/view/get_Affiliations")`

The first ruling dynasty of [[Dunmar]], founded by [[Bhishma]]. 

%%^Campaign:None%%
### Historical Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Born", "Died"], 
			dv.pages("#person")
				.where(f => util.isOrWasAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.sort(b => b.born)
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<startStatus> <startDate>",b.file, dv.current().pageTargetDate), util.s("<endStatus> <endDate>",b.file, dv.current().pageTargetDate)]))
```
%%^End%%

%%^Lint%%
## Open findings

- [ ] `pronunciation.missing`: the Dunmari-based pronunciation below is a proposal, not accepted frontmatter.
- [ ] `classification.deprecated_subtype`: `subTypeOf: dynasty` is preserved at the conspicuous beginning of frontmatter for human migration.
- [ ] `coverage.established_history`: the visible article omits the dynasty’s seat, duration, and fall, all established elsewhere.
- [ ] `syntax.noncanonical_campaign_block`: change `Campaign:None` to `Campaign:none` if the private block is retained.
- [ ] `dm_notes.attestation`: the moved comment explicitly supports `dm_notes: important`, but the off-vault list cannot be checked by the linter.

## Copy-ready candidates

```yaml
pronunciation: AAT-mah-jee
```

```markdown
The Aatmaji dynasty ruled [[Dunmar]] from DR 1173 to DR 1395, with [[Kharsan]] as its administrative center. It ended when its last Samraat, [[Dasa]], led a disastrous expedition into [[Gazetteer/Drankorian Hinterland/Drankor/Drankor|Drankor]] and never returned.
```

## Applied changes

- Canonicalized frontmatter layout and added lint state.
- Added persistent article and simplified name metadata.
- Moved the existing note-quality/source comment above the title without changing its text.

## Evidence reviewed

- [[Dunmar]] for the dynasty’s dates, Kharsan seat, and end under Dasa.
- [[Kharsan]] and [[Dasa]] for the administrative center, tombs, and last ruler.
- [[Timeline of the Aatmaji Dynasty]] and later campaign-linked references for scope; no cross-note contradiction found.

## Status disposition

- No pre-existing status tags required disposition.
%%^End%%
