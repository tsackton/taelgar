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
    const { StringFormatter } = customJS
    const { DateManager } = customJS

    let file = { name: tp.file.title, frontmatter: tp.frontmatter }
    let displayDefaults = NameManager.getDisplayData(tp.frontmatter)
    let pageDates = DateManager.getPageDates(tp.frontmatter)
    let hasPageDates = pageDates.startDate || pageDates.endDate

    let output = StringFormatter.getFormattedString("# <name:tn>", file) + "\n"

    let secondary = StringFormatter.getFormattedString("*(<pronunciation>)*", file)
    if (secondary && secondary.length > 0) {
        output += secondary + "\n"
    }

    let summaryBlockLines = []

    let typeOf = StringFormatter.getFormattedString(displayDefaults.secondaryInfo, file)
    if (typeOf && typeOf.length > 0) summaryBlockLines.push("> " + typeOf)

    if (tp.frontmatter.ddbLink && displayDefaults.ddbLinkText && displayDefaults.ddbLinkText.length > 0) {
        summaryBlockLines.push("> [" + displayDefaults.ddbLinkText + "](" + tp.frontmatter.ddbLink + ")")
    }

    if (hasPageDates) {
        summaryBlockLines.push("> " + '`$=dv.view("_scripts/view/get_PageDatedValue")`')
    }

    if (tp.frontmatter.leaderOf) {
        summaryBlockLines.push("> " + '`$=dv.view("_scripts/view/get_RegnalValue")`')
    }

    let partOf = StringFormatter.getFormattedString(displayDefaults.partOf, file)
    if (partOf && partOf.length > 0) {
        summaryBlockLines.push("> " + partOf)
    }

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