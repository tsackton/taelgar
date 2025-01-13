---
headerVersion: 2023.11.25
tags: [organization, status/check/tim]
displayDefaults: {partOf: ""}
ancestry: Chardonian
name: Society of the Open Scroll
typeOf: scholary society
---
# The Society of the Open Scroll
>[!info]+ Information
> A [[Chardonian Empire|Chardonian]] scholary society

%% Tim: anything to add? %%
A scholarly society founded in the aftermath of the [[Great War]], to preserve and protect knowledge against future disaster, and to learn the secrets of the past to better protect [[Chardon]] and the world from existential magical threats.

They have meetings, sometimes public lectures or demonstrations, sponsorship of individual scholars and research projects, including expeditions, and the like. The membership is largely made up of academics already associated with the [[Great Library]] or the [[University of Chardon]], but formally neither is a requirement to join - sponsorship and approval by a vote of the members is enough. In the past 20-30 years have been recruiting more "practical historians" and now have kind of an "explorer's wing" for adventurers and the like. This is funded primary by the [[Great Library]], but occasionally by individual patrons.

Generally speaking in favor of preserving knowledge, against chaltye magic, and in favor of sharing within the group but secrecy outside the group for fear of passing along dangerous magic.

## History

- (DR::1561): The Society of the Open scroll is founded in [[Chardon]], in the aftermath of the [[Great War]], with a mission to preserve and protect knowledge of magic against future disaster, and to learn the secrets of the past to better protect Chardon and the world from existential magical threats. 

%%SECRET[1]%%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%