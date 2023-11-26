function get_Whereabouts(metadata) {

    const { WhereaboutsManager } = customJS
    const { DateManager } = customJS
    const { NameManager } = customJS
    const { StringFormatter } = customJS

    let displayDefaults = NameManager.getDisplayData(metadata)
    let file = { name: metadata.file.name, frontmatter: metadata }

    let pageData = DateManager.getPageDates(metadata);
    let pageYear = DateManager.getTargetDateForPage(metadata)
    let unknownStr = displayDefaults.whereaboutsUnknown

    if (!pageData.isCreated) return "";

    let isPageAlive = pageData.isAlive
    if (!isPageAlive) pageYear = pageData.endDate

    let whereabout = WhereaboutsManager.getWhereabouts(metadata, pageYear)
    let showOrigin = whereabout.origin && whereabout.origin.location && (!whereabout.home || whereabout.origin.location != whereabout.home.location)


    let displayString = "";

    if (showOrigin) {

        displayString = StringFormatter.getFormattedString(displayDefaults.whereaboutsOrigin, file, pageYear)
    }

    if (whereabout.home && whereabout.home.location) {
        let formatStr = isPageAlive ? displayDefaults.whereaboutsHome : displayDefaults.whereaboutsPastHome

        if (displayString != "") displayString += "\n"
        displayString += StringFormatter.getFormattedString(formatStr, file, pageYear)

        // if we have a current location that matches home, we are done
        if (whereabout.current && whereabout.home.location == whereabout.current.location)
            return displayString;
    }

    if ((whereabout.current && !whereabout.current.location) || (whereabout.lastKnown && !whereabout.lastKnown.location)) {
        if (isPageAlive) {
            if (displayString != "") displayString += "\n"
            displayString += StringFormatter.getFormattedString(unknownStr, file, pageYear)
        }

        return displayString;
    }



    if (whereabout.current && whereabout.current.location) {

        if (displayString != "") displayString += "\n"

        let formatStr = isPageAlive ? displayDefaults.whereaboutsCurrent : displayDefaults.whereaboutsPast
        displayString += StringFormatter.getFormattedString(formatStr, file, pageYear)

        return displayString;
    }

    if (whereabout.lastKnown && whereabout.lastKnown.location) {
        if (displayString != "") displayString += "\n"

        let frmtStr = displayDefaults.whereaboutsLastKnownNoDate
        
        if (whereabout.lastKnown.awayEnd.display != "") {            
            frmtStr = displayDefaults.whereaboutsLastKnown
        }        

        displayString += StringFormatter.getFormattedString(frmtStr, file, pageYear)
        if (isPageAlive) {
            displayString += "\n" + StringFormatter.getFormattedString(unknownStr, file, pageYear)
        }

        return displayString;
    }

    return displayString;
}

return get_Whereabouts(dv.current());