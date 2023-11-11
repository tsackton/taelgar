function get_Pronouns(metadata) {

    // if pronouns are defined in note metadata, use those

    if (metadata.pronouns) {
        return metadata.pronouns
    }

    // otherwise calculate pronouns from note metadata gender

    if (metadata.gender == "male") {
        return "he/him"
    } else if (metadata.gender == "female") {
        return "she/her"
    }

    // if no gender or nonbinary, use they/them pronouns
    return "they/them"
}

async function generateHeader(tp) {

    const { metadataUtils } = customJS

    const metadataFilePath = app.vault.configDir + "/metadata.json";

    let metadataFile = await app.vault.adapter.read(metadataFilePath);
    let metadata = JSON.parse(metadataFile);


    if (tp.frontmatter.type == "NPC" || tp.frontmatter.type == "Ruler" || tp.frontmatter.type == "PC") {
        let ancestryDisplayValue = ""
        let speciesDisplayValue = ""

        let species = tp.frontmatter.species;
        if (species) {
            let link = app.plugins.plugins.dataview.api.pages().where(p => p.speciesDescriptor == species).first()
            if (link) {
                speciesDisplayValue = "[[" + link.file.name + "|" + species + "]]"
            }
            else {
                speciesDisplayValue = species;
            }
        }

        let ancestry = tp.frontmatter.ancestry;
        if (ancestry) {
            let link = app.plugins.plugins.dataview.api.pages().where(p => p.cultureDescriptor == ancestry).first()
            if (link) {
                if (species) ancestryDisplayValue = " ([[" + link.file.name + "|" + ancestry + "]])"
                else ancestryDisplayValue = "[[" + link.file.name + "|" + ancestry + "]]"
            }
            else {
                if (species) ancestryDisplayValue = " (" + ancestry + ")"
                else ancestryDisplayValue = ancestry;
            }
        }

        let pronounDisplayValue = ", " + get_Pronouns(tp.frontmatter)
        let locationDisplay = "";

        // get home and origin // 
        if (tp.frontmatter.whereabouts) {
            locationDisplay += "\n>> `$=dv.view(\"_scripts/view/get_HomeWhereabouts\")`";

            if (tp.frontmatter.lastSeenByParty) {
                tp.frontmatter.lastSeenByParty.filter(e => e.prefix && e.date).forEach(element => {

                     console.log(element) ;
                     
                    let parsedDate = metadataUtils.parse_date_to_events_date(element.date);
                    let locForThisDate = metadataUtils.get_currentWhereabouts(tp.frontmatter, parsedDate);

                    console.log(locForThisDate)

                    if (locForThisDate) {
                        let partyName = "the party";
                        let campaignData = metadata.campaigns;
                        if (campaignData) {
                            let thisCampaign = campaignData.find(search => search.prefix == element.prefix);
                            if (thisCampaign) {
                                partyName = thisCampaign.partyName;
                                if (thisCampaign.partyFile) {
                                    partyName = "[[" + thisCampaign.partyFile + "|" + partyName + "]]"
                                }
                            }
                            locationDisplay += `\n>>%%^Campaign:${element.prefix}%% Last seen by ${partyName} at ${parsedDate.display}: ${metadataUtils.get_Location(locForThisDate)} %%^End%%`;
                        }
                    }
                });
            }

            locationDisplay += "\n>> `$=dv.view(\"_scripts/view/get_CurrentWhereabouts\")`";
        }


        // return string //
        let nameString = tp.frontmatter.name;
        if (tp.frontmatter.title) {
            nameString = tp.frontmatter.title + " " + nameString;
        }

        let elfDisplay = "";
        if (tp.frontmatter.ka) {
            elfDisplay = " ([[The Cycle of Generations|ka " + tp.frontmatter.ka + "]])";
        }

        if (tp.frontmatter.type == "NPC" || tp.frontmatter.type == "PC") {
            headerString = "# " + nameString + "\n>[!info]+ Biographical Summary" +
                "\n>" + speciesDisplayValue + ancestryDisplayValue + pronounDisplayValue +
                "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`' + elfDisplay +
                locationDisplay + "\n"
        } else {
            headerString = "# " + nameString + "\n>[!info]+ Biographical Summary" +
                "\n>" + speciesDisplayValue + ancestryDisplayValue + pronounDisplayValue +
                "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`' + elfDisplay +
                "\n>" + '`$=dv.view("_scripts/view/get_RegnalValue")`' +
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
            timeDisplay = '>`$=dv.view("_scripts/view/get_PageDatedValue")`';
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