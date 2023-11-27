
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
    let pageType = NameManager.getPageType(tp.frontmatter)

    let output = StringFormatter.getFormattedString("# <name:tn>", file) + "\n"

    let secondary = StringFormatter.getFormattedString("*(<pronunciation>)*", file)
    if (secondary && secondary.length > 0) {
        output += secondary + "\n"
    }

    let summaryBlockLines = []

    let typeOf = StringFormatter.getFormattedString(displayDefaults.secondaryInfo, file)
    if (typeOf && typeOf.length > 0) {
        summaryBlockLines.push("> " + typeOf)
    }

    if (tp.frontmatter.ddbLink && displayDefaults.ddbLinkText && displayDefaults.ddbLinkText.length > 0) {
        summaryBlockLines.push("> [" + displayDefaults.ddbLinkText + "](" + tp.frontmatter.ddbLink + ")")
    }

    if (hasPageDates) {
        summaryBlockLines.push("> " + '`$=dv.view("_scripts/view/get_PageDatedValue")`')
    }

    if (tp.frontmatter.leaderOf || tp.frontmatter.affiliations) {
        summaryBlockLines.push("> " + '`$=dv.view("_scripts/view/get_Affiliations")`')
    }

    let partOf = StringFormatter.getFormattedString(displayDefaults.partOf, file)
    if (partOf && partOf.length > 0) {
        summaryBlockLines.push("> " + partOf)
    }

    if (tp.frontmatter.whereabouts || (pageType == "place" && tp.frontmatter.partOf)) {        
        summaryBlockLines.push(">> `$=dv.view(\"_scripts/view/get_Whereabouts\")`")
    } 

    for (let meeting of WhereaboutsManager.getPartyMeeting(tp.frontmatter, undefined)) {
        summaryBlockLines.push(`>> %%^Campaign:${meeting.campaign}%% ${meeting.text} %%^End%%`);
    }

    if (summaryBlockLines.length > 0) {
        output += ">[!info]+ " + displayDefaults.boxName + "\n"
    }

    output += summaryBlockLines.join("\n")
    return output + "\n"
}

module.exports = generateHeader