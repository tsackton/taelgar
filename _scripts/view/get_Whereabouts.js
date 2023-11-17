function get_Whereabouts(metadata) {

    const { LocationManager } = customJS
    const { WhereaboutsManager } = customJS
    const  { DateManager } = customJS
    const  { NameManager } = customJS

    let displayDefaults = NameManager.getDisplayData(metadata)

    let pageData = DateManager.getPageDates(metadata);
    let pageYear = DateManager.getTargetDateForPage(metadata)

    if (!pageData.isCreated) return "";

    let isPageAlive = pageData.isAlive
    if (!isPageAlive) pageYear = pageData.endDate

    let whereabout = WhereaboutsManager.getWhereabouts(metadata, pageYear)
    let showOrigin = whereabout.origin && whereabout.origin.location && (!whereabout.home || whereabout.origin.location != whereabout.home.location)

    let displayString = "";

    if (showOrigin) {
        displayString =  displayDefaults.whereaboutsOrigin.replace("<loc>",  LocationManager.getLocationName(whereabout.origin.location))
    }

    if (whereabout.home && whereabout.home.location) {
        if (showOrigin) displayString += "\n"

        let formatStr = isPageAlive ? displayDefaults.whereaboutsHome : displayDefaults.whereaboutsPastHome
        displayString += formatStr.replace("<loc>",  LocationManager.getLocationName(whereabout.home.location))

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

    let pageDisplayData = NameManager.getDisplayData(metadata)

    if (whereabout.current && whereabout.current.location) {
        if (isPageAlive) {
            displayString += "\nCurrent location: (as of " + pageYear.display + "): " + LocationManager.getLocationName(whereabout.current.location)
        }
        else {
            console.log(pageDisplayData)
            let capitalizedEnd = pageDisplayData.endStatus.charAt(0).toUpperCase() + pageDisplayData.endStatus.slice(1);
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