function get_Whereabouts(metadata) {

    const { metadataUtils } = customJS
    const { WhereaboutsManager } = customJS
    const  { DateManager } = customJS


    let pageData = DateManager.getPageDates(metadata);
    let pageYear = DateManager.getTargetDateForPage(metadata)
    if (!pageData.isCreated) return "";

    let isPageAlive = pageData.isAlive
    if (!isPageAlive) pageYear = pageData.endDate

    let whereabout = WhereaboutsManager.getWhereabouts(metadata, pageYear)
    let showOrigin = whereabout.origin && whereabout.origin.location && (!whereabout.home || whereabout.origin.location != whereabout.home.location)

    let displayString = "";

    if (showOrigin) {
        displayString = "Originally from: " + metadataUtils.get_Location(whereabout.origin, false);
    }

    if (whereabout.home && whereabout.home.location) {
        if (!isPageAlive) {
            displayString += "\nLived in: " + metadataUtils.get_Location(whereabout.home, false);
        }
        else {
            displayString += "\nBased in: " + metadataUtils.get_Location(whereabout.home, false);
        }

        // if we have a current location that matches home, we are done
        if (whereabout.current && whereabout.home.location == whereabout.current.location)
            return displayString;
    }

    if ((whereabout.current && !whereabout.current.location) || (whereabout.lastKnown && !whereabout.lastKnown.location)) {
        if (isPageAlive) {
            displayString += "\n Current location: Unknown";
        }

        return displayString;
    }

    if (whereabout.current && whereabout.current.location) {
        if (isPageAlive) {
            displayString += "\nCurrent location: (as of " + pageYear.display + "): " + metadataUtils.get_Location(whereabout.current, false)
        }
        else {
            let capitalizedEnd = pageData.endDescriptor.charAt(0).toUpperCase() + pageData.endDescriptor.slice(1);
            displayString += "\n " + capitalizedEnd + " in " + metadataUtils.get_Location(whereabout.current, false)
        }
        return displayString;
    }

    if (whereabout.lastKnown && whereabout.lastKnown.location) {

        displayString += "\nLast known location: (as of " + whereabout.lastKnown.awayEnd.display + "): " + metadataUtils.get_Location(whereabout.lastKnown, false)
        if (isPageAlive) {
            displayString += "\n Current location: Unknown";
        }

        return displayString;
    }

    return displayString;
}

return get_Whereabouts(dv.current());