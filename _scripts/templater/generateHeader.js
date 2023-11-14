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
    } else if (metadata.gender) {
        return "they/them"
    }

    return undefined
}

async function generateHeader(tp) {

    const { metadataUtils } = customJS

    const metadataFilePath = app.vault.configDir + "/metadata.json";

    let metadataFile = await app.vault.adapter.read(metadataFilePath);
    campaignMetadata = JSON.parse(metadataFile);



    let nameString = metadataUtils.get_Name(tp, false);

    if (!nameString) {
        new Notice("The file does not have a name; please set the name before processing the header")
        return "<% tp.user.generateHeader(tp) %>"
    }

    let output = "# " + nameString + "\n"

    let pronunciation = tp.frontmatter.pronunciation
    if (pronunciation) {
        output += "*(" + pronunciation + ")*\n"
    }

    let isPerson = tp.frontmatter.tags.filter(f => f.startsWith("person")).length > 0
    let isPlace = tp.frontmatter.tags.filter(f => f.startsWith("place")).length > 0
    let isOrganization = tp.frontmatter.tags.filter(f => f.startsWith("organization")).length > 0
    let isItem = tp.frontmatter.tags.filter(f => f.startsWith("item")).length > 0
    let isSessionNote = tp.frontmatter.tags.filter(f => f.startsWith("sessionNote")).length > 0

    let isRuler = isPerson && tp.frontmatter.tags.filter(f => f.contains("ruler")).length > 0

    let hasPageDates = tp.frontmatter.born || tp.frontmatter.died || tp.frontmatter.created || tp.frontmatter.destroyed
    let hasReignInfo = isRuler && (tp.frontmatter.reignStart || tp.frontmatter.reignEnd)

    if (isPerson) {
        output += ">[!info]+ Biographical Summary"

        let ancestryDisplayValue = undefined
        let speciesDisplayValue = undefined
        let pronounDisplayValue = get_Pronouns(tp.frontmatter)

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


        if (tp.frontmatter.rulerOf && isRuler) {
            let locationDisplay = metadataUtils.get_Location(tp.frontmatter.rulerOf)
            let title = tp.frontmatter.title ?? "Ruler"
            if (locationDisplay) {
                output += "\n>" + title + " of " + locationDisplay
            }
        }

        if (ancestryDisplayValue || speciesDisplayValue || pronounDisplayValue) {
            output += "\n>"
        }

        if (speciesDisplayValue) {
            output += speciesDisplayValue
        }

        if (ancestryDisplayValue) {
            if (speciesDisplayValue) output += " " + ancestryDisplayValue
            else output += ancestryDisplayValue
        }

        if (pronounDisplayValue) {
            if (speciesDisplayValue || ancestryDisplayValue) output += ", " + pronounDisplayValue
            else output += pronounDisplayValue
        }

        let elfDisplay = "";
        if (tp.frontmatter.ka || species == "elf") {
            elfDisplay = " ([[The Cycle of Generations|ka " + (tp.frontmatter.ka ?? "unknown") + "]])"
        }

        if (hasPageDates) {
            output += "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`' + elfDisplay
        }
    }

    if (isOrganization && (hasPageDates || tp.frontmatter.basedIn)) {
        output += ">[!info]+ Summary"
        if (hasPageDates) output += "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`'
        if (tp.frontmatter.basedIn) {
            let locationDisplay = metadataUtils.get_Location(tp.frontmatter.basedIn)
            if (locationDisplay) {
                output += "\n> Based in: " + locationDisplay
            }
        }
    }

    if (hasReignInfo || (isRuler && tp.frontmatter.rulerOf)) {
        output += "\n>" + '`$=dv.view("_scripts/view/get_RegnalValue")`'
    }

    if (isItem) {
        output += ">[!info]+ Item Info"


        let mechanicsLink = undefined
        if (tp.frontmatter.ddbLink) {
            mechanicsLink = "(" + tp.frontmatter.ddbLink + ")"
        }

        let itemType = undefined
        if (tp.frontmatter.unique == true && tp.frontmatter.magical == true) {
            itemType = "(unique magical item)"
        }
        else if (tp.frontmatter.unique == true && tp.frontmatter.magical == false) {
            itemType = "(unique mundane item)"
        }
        else if (tp.frontmatter.unique == false && tp.frontmatter.magical == true) {
            itemType = "(magical item)"
        }
        else  /*if (tp.frontmatter.unique == false && tp.frontmatter.magical == false)*/ { 
            itemType = "(mundane item)"
        }

        if (mechanicsLink) {
            output += "\n> [" + itemType + "]" + mechanicsLink
        }
        else {
            output += "\n>" + itemType
        }

        if (tp.frontmatter.owner) {
            output += "\n> Owner: " + metadataUtils.get_NameForPossibleLink(tp.frontmatter.owner, true)
        }

        if (tp.frontmatter.maker) {
            output += "\n> Maker: " + metadataUtils.get_NameForPossibleLink(tp.frontmatter.maker, true)
        }

        if (hasPageDates) {
            output += "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`'
        }
    }

    if (isPlace) {
        output += ">[!info]+ Summary"
        if (hasPageDates) {
            output += "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`'
        }

        if (tp.frontmatter.population) {
            if (!hasPageDates) {
                output += "\n>"
            }
            output += " *(pop. " + tp.frontmatter.population.toLocaleString() + ")*"
        }

        if (tp.frontmatter.partOf) {

            let locationDisplay = metadataUtils.get_Location(tp.frontmatter.partOf)

            if (tp.frontmatter.placeType) {
                let firstChar = tp.frontmatter.placeType[0]
                if (firstChar == 'i' || firstChar == 'e' || firstChar == 'a' || firstChar == 'o' || firstChar == 'u') {
                    output += "\n> an " + tp.frontmatter.placeType + " in " + locationDisplay
                } else {
                    output += "\n> a " + tp.frontmatter.placeType + " in " + locationDisplay
                }
            } else {
                output += "\n> a place in " + locationDisplay
            }
        }
    }

    if (tp.frontmatter.whereabouts && (isPerson)) {
        output += "\n>> `$=dv.view(\"_scripts/view/get_HomeWhereabouts\")`";

        if (tp.frontmatter.campaignInfo) {
            tp.frontmatter.campaignInfo.filter(e => e.campaign && e.date).forEach(element => {
                let parsedDate = metadataUtils.parse_date_to_events_date(element.date, false);
                let locForThisDate = metadataUtils.get_currentWhereabouts(tp.frontmatter, parsedDate);

                if (locForThisDate) {
                    let partyName = metadataUtils.get_party_name_for_party(campaignMetadata, element.campaign)
                    if (partyName) {
                        let type = element.type ?? "seen"
                        let newText = `\n>>%%^Campaign:${element.campaign}%% Last ${type} by ${partyName} on ${parsedDate.display} in: ${metadataUtils.get_Location(locForThisDate)} %%^End%%`;
                        output += newText
                    }
                }
            });
        }

        output += "\n>> `$=dv.view(\"_scripts/view/get_CurrentWhereabouts\")`";
    }

    return output
}
module.exports = generateHeader