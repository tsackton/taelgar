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

    // if page is dead/destroyed, get whereabouts as of died/destroyed date //
    // if we want to allow dead bodies to move around, would need to change this //
    // however, currently don't have a good location to track "Died at" so might be complicated //
    // but commenting to track for the future //
    if (!isPageAlive) pageYear = pageData.endDate

    let whereabout = WhereaboutsManager.getWhereabouts(metadata, pageYear)

    displayString = ""

    // whereabout.lastKnown.awayEnd.display false-y if it was 0001 or 9999 //
    // or if whereabout.lastKnown.location == "unknown" //
    let knownLastKnown = whereabout.lastKnown.awayEnd.display ? true : false

    originString = StringFormatter.getFormattedString(displayDefaults.whereaboutsOrigin, file, pageYear)
    homeString = StringFormatter.getFormattedString((isPageAlive ? displayDefaults.whereaboutsHome : displayDefaults.whereaboutsPastHome), file, pageYear)
    currentString = StringFormatter.getFormattedString((isPageAlive ? displayDefaults.whereaboutsCurrent : displayDefaults.whereaboutsPast), file, pageYear)
    knownString = StringFormatter.getFormattedString(knownLastKnown ? displayDefaults.whereaboutsLastKnown : displayDefaults.whereaboutsLastKnownNoDate, file, pageYear)

    if (whereabout.origin.location != whereabout.home.location) {
        // display origin if it is not the same as home //
        displayString += originString + "\n"
    }

    if (whereabout.home.location) {
        // display home if it is not unknown //
        displayString += homeString + "\n"
    }

    if (whereabout.current.location != whereabout.home.location || !whereabout.current.location) {
        // display current if it is not the same as home, or if both current and home are unknown //
        displayString += currentString + "\n"
    }

    if (!whereabout.current.location && whereabout.lastKnown) {
        displayString += knownString + "\n"
    }

    return displayString;
}

return get_Whereabouts(dv.current());