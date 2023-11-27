function get_Whereabouts(metadata) {

    const { WhereaboutsManager } = customJS
    const { DateManager } = customJS
    const { NameManager } = customJS
    const { StringFormatter } = customJS

    let displayDefaults = NameManager.getDisplayData(metadata)
    let file = { name: metadata.file.name, frontmatter: metadata }

    let pageData = DateManager.getPageDates(metadata);
    let pageYear = DateManager.getTargetDateForPage(metadata)

    if (!pageData.isCreated) return "";

    let isPageAlive = pageData.isAlive

    // if page is dead/destroyed, get whereabouts as of died/destroyed date //
    // if we want to allow dead bodies to move around, would need to change this //
    // however, currently don't have a good location to track "Died at" so might be complicated //
    // but commenting to track for the future //
    if (!isPageAlive) pageYear = pageData.endDate

    let whereabout = WhereaboutsManager.getWhereabouts(metadata, pageYear)

    displayString = ""

    // knownLastKnown is false if whereabout.lastKnown.awayEnd.display is falsey (it was 0001 or 9999) //
    // or if whereabout.lastKnown.awayEnd is nullish //
    let knownLastKnown = whereabout.lastKnown.awayEnd?.display ? true : false

    // origin string construction //
    // if origin is unknown, use unknown string //
    // don't care about alive/dead for origin //
    originString = StringFormatter.getFormattedString(whereabout.origin.location ? (whereabout.origin.originFormat ?? displayDefaults.whereaboutsOrigin) : displayDefaults.whereaboutsOriginUnknown, file, pageYear)

    // home string construction //
    if (isPageAlive) {
        homeString = StringFormatter.getFormattedString(whereabout.home.location ? (whereabout.home.homeFormat ?? displayDefaults.whereaboutsHome) : displayDefaults.whereaboutsHomeUnknown, file, pageYear)
    } else {
        homeString = StringFormatter.getFormattedString(whereabout.home.location ? (whereabout.home.pastHomeFormat ?? displayDefaults.whereaboutsPastHome) : displayDefaults.whereaboutsPastHomeUnknown, file, pageYear)
    }

    // current string construction //    
    currentString = StringFormatter.getFormattedString((isPageAlive ? (whereabout.current.currentFormat ?? displayDefaults.whereaboutsCurrent) : (whereabout.current.pastFormat ?? displayDefaults.whereaboutsPast)), file, pageYear)

    // last known string construction //
    knownString = StringFormatter.getFormattedString(knownLastKnown ? (whereabout.current.lastKnownFormat ?? displayDefaults.whereaboutsLastKnown) : (whereabout.current.lastKnownFormat ?? displayDefaults.whereaboutsLastKnownNoDate), file, pageYear)


    if (!whereabout.origin.location || whereabout.origin.location != whereabout.home.location) {
        // display origin if it is not the same as home or it is unknown //
        displayString += originString + "\n"
    }

    // always display home
    displayString += homeString + "\n"

    if (!whereabout.current.location || whereabout.current.location != whereabout.home.location) {
        // display current if it is not the same as home or if current is unknown //
        displayString += currentString + "\n"
    }

    if (!whereabout.current.location && whereabout.lastKnown.location && whereabout.lastKnown.location != whereabout.home.location) {
        // display last known if current is unknown and last known is known, as long as it isn't the same as home //        
        // note it is not clear last known can ever be same as home but this is added to just double-confirm we don't show 2x of the same thing //
        displayString += knownString + "\n"
    }

    // remove extra newlines //
    return displayString.replace(/\n\n+/g, "\n");
}

return get_Whereabouts(dv.current());