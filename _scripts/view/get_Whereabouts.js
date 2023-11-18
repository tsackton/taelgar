function get_Whereabouts(metadata) {

    const { WhereaboutsManager } = customJS
    const { DateManager } = customJS
    const { NameManager } = customJS
    const { LocationManager } = customJS

    let displayDefaults = NameManager.getDisplayData(metadata)

    let pageData = DateManager.getPageDates(metadata);
    let pageYear = DateManager.getTargetDateForPage(metadata)
    let endStatus = displayDefaults.endStatus
    let unknownStr = displayDefaults.whereaboutsUnknown

    if (!pageData.isCreated) return "";

    let isPageAlive = pageData.isAlive
    if (!isPageAlive) pageYear = pageData.endDate

    let whereabout = WhereaboutsManager.getWhereabouts(metadata, pageYear)
    let showOrigin = whereabout.origin && whereabout.origin.location && (!whereabout.home || whereabout.origin.location != whereabout.home.location)


    let displayString = "";

    if (showOrigin) {
        displayString = LocationManager.buildFormattedLocationString(displayDefaults.whereaboutsOrigin, whereabout.origin, pageYear, endStatus)
    }

    if (whereabout.home && whereabout.home.location) {
        let formatStr = isPageAlive ? displayDefaults.whereaboutsHome : displayDefaults.whereaboutsPastHome

        if (displayString != "") displayString += "\n"
        displayString += LocationManager.buildFormattedLocationString(formatStr, whereabout.home, pageYear, endStatus)

        // if we have a current location that matches home, we are done
        if (whereabout.current && whereabout.home.location == whereabout.current.location)
            return displayString;
    }

    if ((whereabout.current && !whereabout.current.location) || (whereabout.lastKnown && !whereabout.lastKnown.location)) {
        if (isPageAlive) {
            if (displayString != "") displayString += "\n"
            displayString += LocationManager.buildFormattedLocationString(unknownStr, undefined, pageYear, endStatus);;
        }

        return displayString;
    }



    if (whereabout.current && whereabout.current.location) {

        if (displayString != "") displayString += "\n"

        let formatStr = isPageAlive ? displayDefaults.whereaboutsCurrent : displayDefaults.whereaboutsPast
        displayString += LocationManager.buildFormattedLocationString(formatStr, whereabout.current, pageYear, endStatus)

        return displayString;
    }

    if (whereabout.lastKnown && whereabout.lastKnown.location) {
        if (displayString != "") displayString += "\n"
        displayString += LocationManager.buildFormattedLocationString(displayDefaults.whereaboutsLastKnown, whereabout.lastKnown, pageYear, endStatus)
        if (isPageAlive) {
            displayString += "\n" + LocationManager.buildFormattedLocationString(unknownStr, undefined, pageYear, endStatus);
        }

        return displayString;
    }

    return displayString;
}

return get_Whereabouts(dv.current());