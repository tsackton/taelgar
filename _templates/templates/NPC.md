---
<%_*
let title = tp.file.title
if (title.startsWith("Untitled")) {
    title = await tp.system.prompt("NPC Name") ?? "Untitled";
    await tp.file.rename(`${title}`);
}

let folder = tp.file.folder();

let species = "";
let ancestry = "";
let defaultHome = "";

if (folder === "Dwarves") {
	species = "dwarf";
} else if (folder === "Elves") {
	species = "elf"
} else if (folder === "Chardonians") {
	species = "human";
	ancestry = "Chardondian";
	defaultHome = "Chardon, Chardonian Empire";
} else if (folder === "Dunmari") {
	species = "human";;
	ancestry = "Dunmari";
	defaultHome = "Dunmar";
} else if (folder === "Sembarans") {
	species = "human";
	ancestry = "Sembaran";
}

if (species === "") {	
	const speciesFiles = this.app.vault.getAbstractFileByPath("Species").children;
	const speciesNames = speciesFiles.map(f =>
	 this.app.metadataCache.getFileCache(f).frontmatter.speciesDescriptor
	);
	
	speciesNames.push("other");
	let species = await tp.system.suggester(speciesNames, speciesNames);
	
	if (species === "other") {
	  species = await tp.system.prompt("Species") ?? "unknown";
	}
}

if (species === "human" && ancestry === "") {
  ancestry = await tp.system.prompt("Ancestry") ?? "";
}

const genders = ["male", "female", "nonbinary"]
let gender = await tp.system.suggester(genders, genders);

const configFilePath = app.vault.getRoot().path  + ".obsidian/taelgarConfig.json";
let configFile = await app.vault.adapter.read(configFilePath);
let parsed = JSON.parse(configFile);       
const campaignValue = parsed.campaignPrefix;

const homeString = await tp.system.prompt("Home (type with commas, i.e. somwhere along the river, Cleenseau, Sembara)", defaultHome) ?? "";

const originString = await tp.system.prompt("Origin (type with commas, i.e. somwhere along the river, Cleenseau, Sembara)") ?? "";


const partyStatusValues = ["met", "unmet", "unaware"]
let partyStatus = await tp.system.suggester(partyStatusValues, partyStatusValues);

let partyMetDate = "";
if (partyStatus == "met") {
   partyMetDate = window.FantasyCalendarAPI.getCalendars()[0].current.year + "-"
   +  (window.FantasyCalendarAPI.getCalendars()[0].current.month+1) + "-" +  window.FantasyCalendarAPI.getCalendars()[0].current.day;
}

let homeArray = homeString.split(',');
let homeArrayValues = homeArray.map(function(f) {
	pieceValue = f.trim();
	file = tp.file.find_tfile(pieceValue);
	if (file != undefined) { return "[[" + pieceValue + "]]";  }
	return pieceValue;
});

let home = homeArrayValues.join(', ');
let homeRegion = homeArrayValues.last().replaceAll('"', '').replaceAll('[', '').replaceAll(']', '');

let originArray = originString.split(',');
let originArrayValues = originArray.map(function(f) {
	  pieceValue = f.trim();
	  file = tp.file.find_tfile(pieceValue);
	  if (file != undefined) {  return "[[" + pieceValue + "]]";	  }
	  return pieceValue;
});

let origin = originArrayValues.join(', ');
let originRegion = originArrayValues.last().replaceAll('"', '').replaceAll('[', '').replaceAll(']', '');

let originDisplayValue = "";
if (origin != "") originDisplayValue = "Origin: " + origin;

let ancestryDisplayValue = "";
if (ancestry != "") ancestryDisplayValue = "(" + ancestry + ")" 

let homeDisplayValue = "";
if (home != "") homeDisplayValue = "Based in: " + home;

%>
type: NPC
name: <% title %>
species: <% species %>
ancestry: <% ancestry %>
gender: <% gender %>
born: 
died: 
location: 
locationRegion:
home: "<% home %>"
homeRegion: <% homeRegion %>
origin: "<% origin %>"
originRegion: <% originRegion %>
affiliations: 
aliases: []
lastSeenByParty_<%_ campaignValue _%>: <%partyMetDate%>
whereabouts: 
- {dateAr: 0001-01-01, place: "<% home %>", region: <% homeRegion %>}

tags: [NPC/<%_ campaignValue _%>/partyStatus]
---

# <% title %>
>[!info]+ Basic information
><% species %> <% ancestryDisplayValue %> <% tp.user.getPronouns(gender) %>
><%+ tp.user.getAgeBasedValue(tp) %>
><% originDisplayValue %>
><% homeDisplayValue %>
