async function generateHeader(tp) {

    function get_displayDateFromYaml(yamlDate) {
        let pieces = yamlDate.split('-');

        if (pieces.length != 3 || pieces[0] == 1) return "(unknown)";


        return get_displayDate(pieces[0], pieces[1] - 1, pieces[2]);
    }

    function get_currentDisplayDate() {
        let currentYear = window.FantasyCalendarAPI.getCalendars()[0].current.year;
        let currentMonth = window.FantasyCalendarAPI.getCalendars()[0].current.month;
        let currentDay = window.FantasyCalendarAPI.getCalendars()[0].current.day;

        return get_displayDate(currentYear, currentMonth, currentDay);
    }

    function get_displayDate(year, month, day) {
        let currentFantasyCal = window.FantasyCalendarAPI.getCalendars()[0];
        console.log(`${year} ${month} ${day}`)
        let date = { year: year, month: month, day: day };
        return window.FantasyCalendarAPI.getDay(date, currentFantasyCal).displayDate;
    }

    const metadataFilePath = app.vault.configDir + "/metadata.json";

    let metadataFile = await app.vault.adapter.read(metadataFilePath);
    let metadata = JSON.parse(metadataFile);


    if (tp.frontmatter.type == "NPC" || tp.frontmatter.type == "Ruler") {
        // create a NPC header // 


        // load metadataUtils via customJS //

        const { metadataUtils } = customJS

        // reformat basic variables //

        let ancestryDisplayValue = metadataUtils.Reformat(tp.frontmatter, "ancestry", " (", ")", "")
        let speciesDisplayValue = metadataUtils.Reformat(tp.frontmatter, "species", "", "", "unknown species")

        // get pronouns //

        let pronounDisplayValue = ", " + metadataUtils.get_Pronouns(tp.frontmatter)
        let locationDisplay = "";

        // get home and origin // 
        if (tp.frontmatter.whereabouts) {
            if (tp.frontmatter.whereabouts.find(s => s.type != undefined) == undefined) {
                locationDisplay = `\n>\`$=dv.view("_scripts/view/get_Whereabouts", {"config": await app.vault.adapter.read(app.vault.configDir +  \"/taelgarConfig.json\"), "prefix": ">", "suffix":""})\``;                
            } else {

                let origin = tp.frontmatter.whereabouts.find(w => w.type === "origin");
                if (origin) {
                    locationDisplay = "\n>> Originally from: " + tp.user.getLocation(tp, origin.place, origin.region);
                }

                let homeCount = tp.frontmatter.whereabouts.filter(w => w.type === "home").length;
                if (homeCount == 1) {
                    let home = tp.frontmatter.whereabouts.find(w => w.type === "home");

                    locationDisplay += "\n>> Based in: " + tp.user.getLocation(tp, home.place, home.region);
                }
                else if (homeCount > 1) {
                    locationDisplay += "\n>> `$=dv.view(\"_scripts/view/get_HomeWhereabouts\")`";
                }



                if (tp.frontmatter.lastSeenByParty) {
                    tp.frontmatter.lastSeenByParty.filter(e => e.prefix != undefined).forEach(element => {
                        let loc = tp.frontmatter.whereabouts.findLast(s => s.date <= element.date);
                        let partyName = "the party";
                        let campaignData = metadata.campaigns;
                        if (campaignData) {
                            let thisCampaign = campaignData.find(search => search.prefix == element.prefix);
                            if (thisCampaign) partyName = thisCampaign.partyName;
                        }
                        if (loc != undefined) {
                            locationDisplay += `\n>>%%Campaign:${element.prefix}%% Last seen by ${partyName} at ${get_displayDateFromYaml(element.date)}: ${tp.user.getLocation(tp, loc.place, loc.region)} %%End%%`;
                        }
                    });
                }

                locationDisplay += "\n>> `$=dv.view(\"_scripts/view/get_CurrentWhereabouts\", {\"config\": await app.vault.adapter.read(app.vault.configDir + \"/taelgarConfig.json\")})`";
            }
        } else {
            let homeDisplayValue = (tp.frontmatter.home || tp.frontmatter.homeRegion) ?
                "\n>Based in: " + tp.user.getLocation(tp, "home") : ""

            let originDisplayValue = (tp.frontmatter.origin || tp.frontmatter.originRegion) ?
                "\n>Originally from: " + tp.user.getLocation(tp, "origin") : ""

            locationDisplay = homeDisplayValue + originDisplayValue;
        }

        // return string //
        let nameString = tp.frontmatter.name;
        if (tp.frontmatter.title) {
            nameString = tp.frontmatter.title + " " + nameString;
        }

        if (tp.frontmatter.type == "NPC") {
            headerString = "# " + nameString + "\n>[!info]+ Biographical Summary" +
                "\n>" + speciesDisplayValue + ancestryDisplayValue + pronounDisplayValue +
                "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? ' +
                'dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`' +
                locationDisplay + "\n"
        } else {
            headerString = "# " + nameString + "\n>[!info]+ Biographical Summary" +
                "\n>" + speciesDisplayValue + ancestryDisplayValue + pronounDisplayValue +
                "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? ' +
                'dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`' +
                "\n>" + '`$=dv.view("_scripts/view/get_RegnalValue", {"currentYear" : (dv.current().yearOverride ? ' +
                'dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`' +
                locationDisplay + "\n"
        }
    } else if (tp.frontmatter.type == "Item") {
        let ownerDisplay = "";
        let makerDisplay = "";
        let timeDisplay = "";
        let mechanics = "";
        let valueDisplay = "";
        if (tp.frontmatter.owner) {
            ownerDisplay = ">Owner: [[" + tp.frontmatter.owner + "]]\n";
        }
        if (tp.frontmatter.maker) {
            makerDisplay = ">Maker: [[" + tp.frontmatter.maker + "]]\n";
        }
        if (tp.frontmatter.created || tp.frontmatter.destroyed) {
            timeDisplay = '>`$=dv.view("_scripts/view/get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? ' +
                'dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`';
        }

        if (tp.frontmatter.gpValueMin || tp.frontmatter.gpValueMax) {
            if (!tp.frontmatter.gpValueMax) {
                valueDisplay = ">Worth at least " + tp.frontmatter.gpValueMin + " gold pieces\n";
            }
            else if (!tp.frontmatter.gpValueMin) {
                valueDisplay = ">Worth at most " + tp.frontmatter.gpValueMax + " gold pieces\n";
            }
            else {
                valueDisplay = ">Worth between " + tp.frontmatter.gpValueMin + " and " + tp.frontmatter.gpValueMax + " gold pieces\n";
            }
        }

        // this order is important to ensure that specific value wins over range
        if (tp.frontmatter.gpValue) {
            valueDisplay = ">Worth " + tp.frontmatter.gpValue + " gold pieces\n";
        }

        if (tp.frontmatter.dbbLink) {
            mechanics = "> [Mechanics](" + tp.frontmatter.dbbLink + ")";
        }

        headerString = "# " + tp.frontmatter.name + "\n";
        if (tp.frontmatter.magical) {
            headerString += "### (magical item)\n";
        } else if (tp.frontmatter.magical != undefined) {
            headerString += "### (mundane item)\n";
        }
        if (ownerDisplay || makerDisplay || timeDisplay || mechanics || valueDisplay) {
            headerString += ">[!info]+ Summary\n" + valueDisplay + ownerDisplay + makerDisplay + timeDisplay + mechanics;
        }
        headerString += "\n";
    }
    else {
        let title = tp.frontmatter.name;
        if (!title) title = tp.file.title;
        headerString = "# " + title + "\n>[!warning]+\n>**Header for type " + tp.frontmatter.type + " doesn't exist!**"
    }
    return headerString
}
module.exports = generateHeader