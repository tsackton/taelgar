---
headerVersion: 2023.11.25
lintedAt: "2026-08-19T11:00:23-04:00"
lintVersion: "2.1"
displayDefaults: {boxInfo: "<ancestry:UA> <typeof>"}
typeOf: family
typeOfAlias: dynasty
tags: [group]
ancestry: Dunmari
name: Aatmaji dynasty
pronunciation: AAT-mah-jee
dm_owner: tim
dm_notes: important
---
# The Aatmaji Dynasty
*(AAT-mah-jee)*
>[!info]+ Information  
> A [[Dunmar|Dunmari]] dynasty  
> `$=dv.view("_scripts/view/get_Affiliations")`

%% have a full list of Samraats of this dynasty in DM notes FWIW%%

The first ruling dynasty of [[Dunmar]], founded by [[Bhishma]]. The Aatmaji dynasty ruled [[Dunmar]] from DR 1173 to DR 1395, with [[Kharsan]] as its administrative center. It ended when its last Samraat, [[Dasa]], led a disastrous expedition into [[Gazetteer/Drankorian Hinterland/Drankor/Drankor|Drankor]] and never returned.

%%^Campaign:none%%
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

%%^Metadata:article:v1%%
mode: historical reference
pov: current-setting reference looking back on a completed dynasty
povNotes: The visible article speaks retrospectively about a dynasty that ended in DR 1395. Its incompleteness is a coverage problem, not a need for a separate timeline POV comment.
%%^End%%

%%^Metadata:names:v1%%
- {name: Aatmaji, language: Dunmari, pronunciation: AAT-mah-jee, status: documented}
%%^End%%
