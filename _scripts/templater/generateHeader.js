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


function getDefaultTypeOf(metadata) {

    if (metadata.typeOf) return metadata.typeOf;

    if (metadata.tags.length > 0) {
        let itemTag = metadata.tags.filter(f => f.startsWith("item") || f.startsWith("place")).first()
        if (itemTag) {
            return itemTag.split("/")[0]
        }
    }

    return undefined;
}

function buildTypeHeader(metadata, displayDefaults) {
    const { NameManager } = customJS

    let formatString = displayDefaults.secondaryInfo

    let gender = NameManager.getName(metadata.gender, "exists", "lower");
    let species = NameManager.getName(metadata.species, "exists", "lower");
    let subspecies = NameManager.getName(metadata.subspecies, "exists", "lower");
    let rarity = NameManager.getName(metadata.rarity, "exists", "lower");
    let type = NameManager.getName(metadata.typeOf, "exists", "lower");
    let subType = NameManager.getName(getSubTypeOf(metadata), "exists", "lower");
    let pronouns = get_Pronouns(metadata)
    let ancestry = NameManager.getName(metadata.ancestry, "exists", "preserve");
    let population = get_Population(metadata)


    let initialTypeLine = formatString.replace("<gender>", gender ?? "")
        .replace("<rarity>", rarity ?? "")
        .replace("<pronouns>", pronouns ?? "")
        .replace("<population>", population ?? "")
        .replace("<ancestry>", ancestry ?? "")
        .replace("<typeof>", type ?? getDefaultTypeOf(metadata) ?? "")
        .replace("<subtypeof>", subType ?? "")
        .replace("<species>", species ?? "")
        .replace("<subspecies>", subspecies ?? "")
        .replace("<mainType>", subspecies ?? species ?? type ?? subType ?? getDefaultTypeOf(metadata) ?? "")

    // remove interior spaces and trailing/leading commas
    initialTypeLine = (initialTypeLine.split(' ').map(f => f.trim()).filter(f => f.length > 0).join(' ')).trim()
    if (initialTypeLine.startsWith(',')) initialTypeLine = initialTypeLine.substr(1).trim()
    if (initialTypeLine.endsWith(",")) initialTypeLine = initialTypeLine.substr(0, initialTypeLine.length - 1).trim()

    initialTypeLine = initialTypeLine.replace(new RegExp("\\(\\s*"), "(")
    initialTypeLine = initialTypeLine.replace(new RegExp("\\s*\\)"), ")")
    initialTypeLine = initialTypeLine.replace(new RegExp("\\(\\s*\\)"), "")


    let typeOfs = []

    if (initialTypeLine.length > 0) {
        typeOfs.push(initialTypeLine)
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
        if (typeOfs.length > 0) typeOfs.push("of")
        else typeOfs.push("Of")
        typeOfs.push(affiliations)
    }

    if (metadata.ka || metadata.species == "elf") {
        typeOfs.push("(" + NameManager.getName("ka", NameManager.LinkIfExists, NameManager.LowerCase) + " " + (metadata.ka ?? "unknown") + ")")
    }

    let result = typeOfs.join(' ')

    return result.trim()
}

function getPrimaryAffiliationName(affiliation, displayDefaultData) {
    const { NameManager } = customJS

    if (displayDefaultData.affiliationTypeOf == undefined)
        return undefined

    if (displayDefaultData.affiliationTypeOf.length == 0)
        return undefined

    return NameManager.getFilteredName(affiliation, f => {
        if (!f.typeOf) return false;
        return displayDefaultData.affiliationTypeOf.includes(f.typeOf)
    }, NameManager.CreateLink)
}

function buildSecondaryHeader(metadata) {

    // builds something like
    // (pronounciation)

    let pronc = metadata.pronunciation

    if (pronc) return "*(" + pronc + ")*"
    return undefined
}

function getSubTypeOf(metadata) {

    let subTypeBase = metadata.subTypeOf
    if (!subTypeBase && metadata.tags.length > 0) {
        let itemTag = metadata.tags.filter(f => f.startsWith("item/") || f.startsWith("place/")).first()
        if (itemTag) {
            let splittag = itemTag.split('/')
            subTypeBase = splittag[1]
        }
    }

    return subTypeBase
}

function buildPartOfHeader(metadata, displayData) {

    const { LocationManager } = customJS
    const { NameManager } = customJS

    if (metadata.partOf) {

        let typeOf = metadata.typeOf ?? metadata.species ?? metadata.subspecies ?? getSubTypeOf(metadata) ?? getDefaultTypeOf(metadata)
       
        if (typeOf == undefined) { 
            typeOf = "UNKNOWN TYPEOF"
        }
        
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
    let hasPageDates = pageDates.startDate || pageDates.endDate

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

    if (tp.frontmatter.leaderOf) {
        summaryBlockLines.push("> " + '`$=dv.view("_scripts/view/get_RegnalValue")`')
    }

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