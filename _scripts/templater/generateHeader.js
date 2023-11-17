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

function get_Population(metadata) {

    if (metadata.population) {

        let intPop = parseInt(metadata.population)
        if (intPop) return "pop. " + metadata.population.toLocaleString()
        return metadata.population
    }

    return undefined

}

function buildTypeHeader(metadata, displayDefaults) {
    const { NameManager } = customJS


    let typeOfs = []

    if (metadata.rarity) {
        typeOfs.push(NameManager.getName(metadata.rarity, NameManager.LinkIfExists, NameManager.LowerCase))
    }

    if (metadata.mundane) {
        typeOfs.push("mundane")
    } else if (metadata.magical) {
        typeOfs.push("magical")
    }

    if (metadata.ancestry) {
        typeOfs.push(NameManager.getName(metadata.ancestry, NameManager.LinkIfExists, NameManager.PreserveCase))
    }

    if (metadata.gender) {
        typeOfs.push(NameManager.getName(metadata.gender, NameManager.LinkIfExists, NameManager.LowerCase))
    }

    if (metadata.species) {
        typeOfs.push(NameManager.getName(metadata.species, NameManager.LinkIfExists, NameManager.LowerCase))
    }

    if (metadata.typeOf && !metadata.partOf) {
        typeOfs.push(NameManager.getName(metadata.typeOf, NameManager.LinkIfExists, NameManager.LowerCase))
    }

    let primaryAffs = []

    if (metadata.affiliations && metadata.affiliations.length > 0 && displayDefaults.affiliationTypeOf && displayDefaults.affiliationTypeOf.length > 0) {
        for (let i = 0; i < metadata.affiliations.length; i++) {
            let aff = metadata.affiliations[i]
            let primaryAff = getPrimaryAffiliationName(aff, displayDefaults)
            if (primaryAff) primaryAffs.push(primaryAff)
        }
    }

    let affiliations = primaryAffs.join(' and ')
    if (primaryAffs.length > 0) {
        typeOfs.push("of " + affiliations)
    }

    if (metadata.ka || metadata.species == "elf") {
        typeOfs.push("(" + NameManager.getName("ka", NameManager.LinkIfExists, NameManager.LowerCase) + " " + (metadata.ka ?? "unknown") + ")")
    }

    let result = typeOfs.join(' ')

    if (metadata.ddbLink) {
        result += " [Mechanics](" + metadata.ddbLink + ")"
    }

    return result.trim()
}

function getPrimaryAffiliationName(affiliation, displayDefaultData) {
    const { NameManager } = customJS
    return NameManager.getFilteredName(affiliation, f => displayDefaultData.affiliationTypeOf && displayDefaultData.affiliationTypeOf.includes(f.typeOf), NameManager.CreateLink)
}

function buildSecondaryHeader(metadata) {

    // builds something like
    // (pronounciation) [key detail]

    let pronc = metadata.pronunciation
    let keyDetail = get_Pronouns(metadata) ?? get_Population(metadata)

    if (pronc && keyDetail) return "*(" + pronc + "),* " + keyDetail
    if (pronc) return "*(" + pronc + ")*"
    if (keyDetail) return keyDetail
}

function buildPartOfHeader(metadata, displayData) {

    const { LocationManager } = customJS
    const { NameManager } = customJS
    if (metadata.partOf) {

        let typeOf = metadata.typeOf ?? displayData.defaultTypeOfForDisplay;
        let firstChar = typeOf.length == 0 ? '' : typeOf[0]
        let article = "a"
        if (firstChar == 'i' || firstChar == 'e' || firstChar == 'a' || firstChar == 'o' || firstChar == 'u') article = "an"

        let formatString = displayData.partOf.replace("<typeof>", typeOf.trim()).replace("<article>", article)
        return LocationManager.buildFormattedLocationString(formatString, { location: metadata.partOf }, undefined, "", "", "")
    }

    return ""
}


/*  # DisplayName
    *(pronunciation)*
    >[!info] BOXNAME
    > TYPE-SPECIFIC TEXT
    > pagedated if it exists (dynamic, insert call to "get page dates")
    > regnal info (dynamic, includes leader of)    
    > partOf if it exists [static line, not auto-generated]
    >> whereabouts if it exists
    >> campaign info
    >> afflitaions
*/

async function generateHeader(tp) {

    const { WhereaboutsManager } = customJS
    const { NameManager } = customJS
    const { LocationManager } = customJS
    const { DateManager } = customJS

    let nameString = NameManager.getName(tp.file.title, NameManager.NoLink, NameManager.TitleCase);
    let displayDefaults = NameManager.getDisplayData(tp.frontmatter)
    let pageDates = DateManager.getPageDates(tp.frontmatter)
    let regnalDates = DateManager.getRegnalDates(tp.frontmatter)
    let hasPageDates = pageDates.startDate || pageDates.endDate
    let hasRegnalDates = regnalDates.startDate || regnalDates.endDate

    if (!nameString) {
        new Notice("The file does not have a name; please set the name before processing the header")
        return "<% tp.user.generateHeader(tp) %>"
    }

    let output = "# " + nameString + "\n"

    let secondary = buildSecondaryHeader(tp.frontmatter)
    if (secondary) {
        output += secondary + "\n"
    }

    let summaryBlockLines = []

    let typeOf = buildTypeHeader(tp.frontmatter, displayDefaults)
    if (typeOf) summaryBlockLines.push("> " + typeOf)      
    if (hasPageDates) summaryBlockLines.push("> " + '`$=dv.view("_scripts/view/get_PageDatedValue")`')
    
    let leadersCheck = []

    if (tp.frontmatter.leaderOf && tp.frontmatter.leaderOf.length > 0) {
        leadersCheck = tp.frontmatter.leaderOf
        let title = tp.frontmatter.title ?? "Ruler"
        let source = tp.frontmatter.leaderOf.map(leader => {
            return {
                title: displayDefaults.leaders == undefined ? title : displayDefaults.leaders.filter(f => f.name == leader).first()?.title ?? title,
                place: NameManager.getName(leader, NameManager.CreateLink)
            };
        })

        while (source.length > 0) {
            let thisOne = source.first();
            let matched = source.filter(x => x.title == thisOne.title)
            source = source.filter(x => x.title != thisOne.title)
            let thisOneLine = thisOne.title + " of "

            for (let i = 0; i < matched.length; i++) {
                let rl = matched[i].place
                thisOneLine += rl
                if (i < matched.length - 1) thisOneLine += " and "
            }

            summaryBlockLines.push("> " + thisOneLine)
        }
    }

    if (hasRegnalDates) summaryBlockLines.push("> " + '`$=dv.view("_scripts/view/get_RegnalValue")`')

    let partOf = buildPartOfHeader(tp.frontmatter, displayDefaults)
    if (partOf) summaryBlockLines.push("> " + partOf)      

    if (tp.frontmatter.whereabouts) {
        summaryBlockLines.push(">> `$=dv.view(\"_scripts/view/get_Whereabouts\")`")         
    }

    for (let meeting of WhereaboutsManager.getPartyMeeting(tp.frontmatter, undefined)) {
        summaryBlockLines.push(`>> %%^Campaign:${meeting.campaign}%% ${meeting.text} %%^End%%`);
    }

    let memberOfLines = []

    if (tp.frontmatter.affiliations && tp.frontmatter.affiliations.length > 0) {
        for (let i = 0; i < tp.frontmatter.affiliations.length; i++) {
            let aff = tp.frontmatter.affiliations[i]

            if (leadersCheck.includes(aff)) continue
            if (getPrimaryAffiliationName(aff, displayDefaults)) continue

            memberOfLines.push(NameManager.getName(aff, NameManager.CreateLink, NameManager.TitleCase))
        }
    }

    if (memberOfLines.length > 0) {
        summaryBlockLines.push(">> Member of: " + memberOfLines.join(", "));
    }

    if (summaryBlockLines.length > 0) {
        output += ">[!info]+ " + displayDefaults.boxName + "\n"
    }

    output += summaryBlockLines.join("\n")
    return output + "\n"
}
module.exports = generateHeader