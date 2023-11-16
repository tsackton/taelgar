function get_Whereabouts(metadata) {

    const { LocationManager } = customJS
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
        displayString = "Originally from: " + LocationManager.getLocationName(whereabout.origin.location);
    }

    if (whereabout.home && whereabout.home.location) {
        if (!isPageAlive) {
            displayString += "\nLived in: " + LocationManager.getLocationName(whereabout.home.location);
        }
        else {
            displayString += "\nBased in: " + LocationManager.getLocationName(whereabout.home.location);
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
            displayString += "\nCurrent location: (as of " + pageYear.display + "): " + LocationManager.getLocationName(whereabout.current.location)
        }
        else {
            let capitalizedEnd = pageData.endDescriptor.charAt(0).toUpperCase() + pageData.endDescriptor.slice(1);
            displayString += "\n " + capitalizedEnd + " in " + LocationManager.getLocationName(whereabout.current.location)
        }
        return displayString;
    }

    if (whereabout.lastKnown && whereabout.lastKnown.location) {

        displayString += "\nLast known location: (as of " + whereabout.lastKnown.awayEnd.display + "): " + LocationManager.getLocationName(whereabout.lastKnown.location)
        if (isPageAlive) {
            displayString += "\n Current location: Unknown";
        }

        return displayString;
    }

    return displayString;
}

return get_Whereabouts(dv.current());