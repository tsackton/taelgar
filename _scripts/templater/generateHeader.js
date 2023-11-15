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

    let nameString = metadataUtils.get_Name(tp, false, true);

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

    let primaryOrgType = "family"
    if (tp.frontmatter.displayDefaults && tp.frontmatter.displayDefaults.primaryOrgType) {
        primaryOrgType = tp.frontmatter.displayDefaults.primaryOrgType
    }

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


        let leadersCheck = []

        if (tp.frontmatter.leaderOf && tp.frontmatter.leaderOf.length > 0) {
            let title = tp.frontmatter.title ?? "Ruler"
            leadersCheck = tp.frontmatter.leaderOf
            let source = tp.frontmatter.leaderOf.map(leader => {
                return {
                    title: tp.frontmatter.displayDefaults?.leaders == undefined ? title : tp.frontmatter.displayDefaults.leaders.filter(f => f.name == leader).first()?.title ?? title,
                    place: metadataUtils.get_NameForPossibleLink(leader, true, undefined, false)
                };
            }).filter(f => f.place != undefined)

            while (source.length > 0) {

                let thisOne = source.first();
                let matched = source.filter(x => x.title == thisOne.title)
                source = source.filter(x => x.title != thisOne.title)

                output += "\n>" + thisOne.title + " of "
                for (let i = 0; i < matched.length; i++) {
                    let rl = matched[i].place
                    output += rl
                    if (i < matched.length - 1) output += " and "
                }
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

        let familyDisplay = undefined
        let hasOrg = false;
        let orgText = undefined

        if (tp.frontmatter.affiliations && tp.frontmatter.affiliations.length > 0) {
            orgText = "\n> Member of: "
            for (let i = 0; i < tp.frontmatter.affiliations.length; i++) {
                let aff = tp.frontmatter.affiliations[i]

                if (leadersCheck.includes(aff)) continue

                if (!familyDisplay) {
                    familyDisplay = metadataUtils.get_NameForOrganization(aff, true, primaryOrgType, false)
                    if (familyDisplay) continue
                }

                orgText += metadataUtils.get_NameForPossibleLink(aff, true, undefined, true)
                hasOrg = true
                if (i < tp.frontmatter.affiliations.length - 1) orgText += ", "
            }

            orgText = orgText.trimEnd()
            if (orgText.endsWith(",")) orgText = orgText.substring(0, orgText.length - 1)
        }

        if (familyDisplay) {
            output += " of " + familyDisplay
        }
        if (hasOrg) {
            output += orgText
        }

        if (hasPageDates) {
            output += "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`' + elfDisplay
        }

        if (hasReignInfo || (isRuler || tp.frontmatter.leaderOf)) {
            output += "\n>" + '`$=dv.view("_scripts/view/get_RegnalValue")`'
        }

        if (tp.frontmatter.whereabouts) {
            output += "\n>> `$=dv.view(\"_scripts/view/get_Whereabouts\")`";
            if (tp.frontmatter.campaignInfo) {
                tp.frontmatter.campaignInfo.filter(e => e.campaign && e.date).forEach(element => {
                    let parsedDate = metadataUtils.parse_date_to_events_date(element.date, false);
                    let locForThisDate = metadataUtils.get_currentWhereabouts(tp.frontmatter, parsedDate);

                    if (locForThisDate) {
                        let partyName = metadataUtils.get_party_name_for_party(element.campaign)
                        if (partyName) {
                            let type = element.type ?? "seen"
                            let newText = `\n>>%%^Campaign:${element.campaign}%% Last ${type} by ${partyName} on ${parsedDate.display} in: ${metadataUtils.get_Location(locForThisDate, true)} %%^End%%`;
                            output += newText
                        }
                    }
                });
            }
        }
    }

    if (isSessionNote) {

    }

    if (isOrganization && (hasPageDates || tp.frontmatter.basedIn || tp.frontmatter.partOf)) {
        output += ">[!info]+ Summary"
        if (hasPageDates) output += "\n>" + '`$=dv.view("_scripts/view/get_PageDatedValue")`'
        if (tp.frontmatter.basedIn) {
            let locationDisplay = metadataUtils.get_Location(tp.frontmatter.basedIn, true)
            if (locationDisplay) {
                output += "\n> Based in: " + locationDisplay
            }
        }
        if (tp.frontmatter.partOf) {
            let partOf = metadataUtils.get_NameForPossibleLink(tp.frontmatter.partOf, true, "organization", true)
            if (partOf) {
                output += "\n> Parent Organization: " + partOf
            }

        }
    }

    if (isItem) {
        output += ">[!info]+ Item Info"

        let mechanicsLink = undefined
        if (tp.frontmatter.ddbLink) {
            mechanicsLink = "(" + tp.frontmatter.ddbLink + ")"
        }

        let itemType = undefined
        let itemRarity = ""
        if (tp.frontmatter.rarity) {
            itemRarity = tp.frontmatter.rarity + " "
        }

        let typeOfLinked = false;

        let typeOf = tp.frontmatter.typeOf
        if (typeOf) {
            let file = window.app.metadataCache.getFirstLinkpathDest(typeOf, ".");
            if (file) {
                typeOfLinked = true
                typeOf = "[[" + typeOf + "]]"
            }
        }

        if (!typeOf) typeOf = "item"

        if (tp.frontmatter.mundane) {
            itemType = "(" + itemRarity + "mundane " + typeOf + ")"
        }
        else {
            itemType = "(" + itemRarity + "magical " + typeOf + ")"
        }

        if (mechanicsLink) {
            if (typeOfLinked) {
                output += "\n> " + itemType + " [Mechanics](" + mechanicsLink + ")"
            }
            else {
                output += "\n> [" + itemType + "]" + mechanicsLink
            }
        }
        else {
            output += "\n>" + itemType
        }

        if (tp.frontmatter.owner) {
            output += "\n> Owner: " + metadataUtils.get_NameForPossibleLink(tp.frontmatter.owner, true, undefined, true)
        }

        if (tp.frontmatter.maker) {
            output += "\n> Maker: " + metadataUtils.get_NameForPossibleLink(tp.frontmatter.maker, true, undefined, true)
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

            let locationDisplay = metadataUtils.get_Location(tp.frontmatter.partOf, false)

            if (tp.frontmatter.placeType) {
                let firstChar = tp.frontmatter.placeType[0]
                if (!tp.frontmatter.placeType.startsWith("uni") && (firstChar == 'i' || firstChar == 'e' || firstChar == 'a' || firstChar == 'o' || firstChar == 'u')) {
                    output += "\n> an " + tp.frontmatter.placeType + " in " + locationDisplay
                } else {
                    output += "\n> a " + tp.frontmatter.placeType + " in " + locationDisplay
                }
            } else {
                output += "\n> a place in " + locationDisplay
            }
        }
    }

    return output + "\n"
}
module.exports = generateHeader