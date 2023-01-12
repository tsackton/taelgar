<%*
const configFilePath = app.vault.getRoot().path  + ".obsidian/taelgarConfig.json";
let configFile = await app.vault.adapter.read(configFilePath);
let parsed = JSON.parse(configFile);       
const campaignValue = parsed.campaignPrefix;

// maybe add code to autogenerate dv.view javascript path based on config //

const currentYear = FantasyCalendarAPI.getCalendars()[0].current.year
if (tp.frontmatter.yearOverride) currentYear = tp.frontmatter.yearOverride

// get home // 

let homeString = tp.frontmatter.home + ", " + tp.frontmatter.homeRegion
let homeArray = homeString.split(',');
let homeArrayValues = homeArray.map(function(f) {
	pieceValue = f.trim();
	file = tp.file.find_tfile(pieceValue);
	if (file != undefined) { return "[[" + pieceValue + "]]";  }
	return pieceValue;
});

let home = homeArrayValues.join(', ');

// get origin // 

let originString = tp.frontmatter.origin + ", " + tp.frontmatter.originRegion
let originArray = originString.split(',');
let originArrayValues = originArray.map(function(f) {
	  pieceValue = f.trim();
	  file = tp.file.find_tfile(pieceValue);
	  if (file != undefined) {  return "[[" + pieceValue + "]]";	  }
	  return pieceValue;
});

let origin = originArrayValues.join(', ');

let originDisplayValue = "";
if (tp.frontmatter.origin || tp.frontmatter.originRegion) originDisplayValue = "Origin: " + origin;

let homeDisplayValue = "";
if (tp.frontmatter.home || tp.frontmatter.homeRegion) homeDisplayValue = "Based in: " + home;

let ancestryDisplayValue = "";
if (tp.frontmatter.ancestry) ancestryDisplayValue = " (" + tp.frontmatter.ancestry + ")" 

let speciesDisplayValue = tp.frontmatter.species;
if (!tp.frontmatter.species) speciesDisplayValue = "unknown species"

%>


# <% tp.frontmatter.name %>
>[!info]+ Basic information
><% speciesDisplayValue %><% ancestryDisplayValue %>, <% tp.user.getPronouns(tp) %>
>`$=dv.view(agefunction, {"currentYear" : <% currentYear %>})`
><% originDisplayValue %>
><% homeDisplayValue %>


```dataviewjs

await forceLoadCustomJS();
const {metadataUtils} = customJS
let metadata = dv.current()
let Name = metadata.name

let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year
let existYear = metadataUtils.get_existYear(metadata)
let Pronouns = metadataUtils.get_Pronouns(metadata)
let Species = metadataUtils.Reformat(metadata, "species", "", "", "unknown species")
let Ancestry = metadataUtils.Reformat(metadata, "ancestry", " (", ") ", "")
let PageDatedValue = metadataUtils.get_PageDatedValue(metadata,existYear)


let BLOCKSTRING_EXIST = "# " + Name + "\n>[!info]+ Biographical Summary" + "\n>" + dv.fileLink(Species) + Ancestry + ", " + Pronouns + "\n>" + PageDatedValue + "\n"
let BLOCKSTRING_NOTEXIST = "# " + Name + "\n>[!fail] **This entity does not yet exist!**"

if (currentYear >= existYear) {
  dv.paragraph(BLOCKSTRING_EXIST)
} else {
  dv.paragraph(BLOCKSTRING_NOTEXIST)
}
```
