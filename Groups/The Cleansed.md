---
headerVersion: 2023.11.25
tags: [organization, status/check/tim]
displayDefaults: {defArt: ''}
name: The Cleansed
typeOf: cult
ancestry: mysterious
---
# The Cleansed
>[!info]+ Information  
> A mysterious cult  
> `$=dv.view("_scripts/view/get_Affiliations")`

A mysterious secret society in [[Chardon]] of which [[People/Chardonians/Fausto]] is a member and seem to be dedicated in some way to Drankorian purity. 

%% Tim: Does this need more? %%

%%SECRET

Founded in DR 1637 through [[Apollyon]]'s influence, and the especially working his corrupting spells through the Crown of Purity, in order to formalize and organize the growing group of Drankorian supremacists hiding among the mages of [[Chardon]]. Over time, starts to attempt to infiltrate the [[Society of the Open Scroll]] and use it as a front for its actions.

Think Hydra.

[[Kadmos]] has given the Cleansed the names and races of the party, as well as his suspicion that they are carrying significant magical treasures recovered from [[Agata]], but not detailed descriptions. Anyway high up in the Cleansed will be immediately suspicious if the group travels together (an elf, halfling, two dwarves, and a human is an unusual group makeup), and will instantly know what's up if they use their real names. But, traveling alone or in smaller groups, and especially if disguised / use fake names, will be less suspicious.

Need to add detail on the process - conversion to 'full blooded Hkaran', sometimes works completely, sometimes leaves you a bit addled. Sometimes kills you. 

How can one be restored?

## Motives

-   Help Apollyon restore Hkaran purity and launch the New Drankorian Empire to bring back the glory of the old days and finally cleanse the world of the impure races


%%

%%^Campaign:None%%
### Members

```dataviewjs
const { util } = customJS
dv.table(["Person", "Info", "Current Location"], 
			dv.pages("#person")
				.where(f => util.isAffiliated(dv.current().file.name, f.file, dv.current().pageTargetDate))
				.map(b => [util.s("<name> (<pronouns> <pronunciation>)", b.file, dv.current().pageTargetDate), util.s("<ancestry> <maintype>", b.file, dv.current().pageTargetDate), util.s("<lastknown:2r> (<lastknowndate>)", b.file, dv.current().pageTargetDate)]))
```
%%^End%%