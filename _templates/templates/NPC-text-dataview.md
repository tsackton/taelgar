<%*

// load campaign prefix and path to dv.view() scripts from config //

const configFilePath = app.vault.getRoot().path  + ".obsidian/taelgarConfig.json";
let configFile = await app.vault.adapter.read(configFilePath);
let parsed = JSON.parse(configFile);       
const campaignValue = parsed.campaignPrefix;
const dViewPath = parsed.dViewPath;

// load metadataUtils via customJS //

await forceLoadCustomJS();
const {metadataUtils} = customJS

// reformat basic variables //

let ancestryDisplayValue = metadataUtils.Reformat(tp.frontmatter, "ancestry", " (", ")", "")
let speciesDisplayValue = metadataUtils.Reformat(tp.frontmatter, "species", "", "", "unknown species")

// get pronouns //

let pronounDisplayValue = ", " + metadataUtils.get_Pronouns(tp.frontmatter)

// get home and origin // 

let homeDisplayValue = (tp.frontmatter.home || tp.frontmatter.homeRegion) ? 
    "Based in: " + metadataUtils.TP_get_Location(tp.frontmatter, "home") : ""

let originDisplayValue = (tp.frontmatter.origin || tp.frontmatter.originRegion) ? 
    "Originally from: " + metadataUtils.TP_get_Location(tp.frontmatter, "origin") : ""

// get values for dv.view //

let existYear = metadataUtils.get_existYear(tp.frontmatter)

%>

# <% tp.frontmatter.name %>
>[!info]+ Basic information
><% speciesDisplayValue %><% ancestryDisplayValue %><% pronounDisplayValue %>
>`$=dv.view("<% dViewPath %>get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year), "existYear" : <% existYear %>})`
><% originDisplayValue %>
><% homeDisplayValue %>
