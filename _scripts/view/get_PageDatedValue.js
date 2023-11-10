function get_PageDatedValue(metadata) {

    const { metadataUtils } = customJS

    let defaultPreexistError = "**(doesn't yet exist)**"
    let defaultStart = "created"
    let defaultEnd = "destroyed"
    let defaultEndStatus = "destroyed"

    if (metadata.type == "NPC" || metadata.type == "PC" || metadata.type == "Ruler") {
        defaultPreexistError = "**(not yet born)**"
        defaultStart = "b.";
        defaultEnd=  "d.";
        defaultEndStatus = "died"
    } else if (metadata.type == "Building") {
        defaultPreexistError =  "**(not yet built)**"
        defaultStart = "built";       
    } else if (metadata.type == "Item") {
        defaultPreexistError = "**(not yet created)**"
        defaultStart = "created";      
    } else if (metadata.type == "Place") {
        defaultPreexistError =  "**(not yet founded)**"
        defaultStart = "founded";       

    }

    preExistError = metadata.preExistError ? metadata.preExistError : defaultPreexistError
    startPrefix = metadata.startPrefix ? metadata.startPrefix : defaultStart
    endPrefix = metadata.endPrefix ? metadata.endPrefix : defaultEnd
    endStatus = metadata.endStatus ? metadata.endStatus : defaultEndStatus

    currentYear = metadataUtils.get_pageEventsDate(metadata, false);
    yearStart = metadataUtils.get_existEventsDate(metadata, false)
    yearEnd = metadataUtils.get_endEventsDate(metadata, true)

    if (!yearStart) {
        if (!yearEnd) return "";
        if (yearEnd.sort > current.sort) return "";
        return endStatus + " " + yearEnd.display;
    } 

    // we have a year start
    let age = metadataUtils.get_Age(currentYear, yearStart)

    if (yearStart.sort > currentYear.sort) return preExistError;

    // no end
    if (!yearEnd) {
        return startPrefix + " " + yearStart.display + " (" + age + " years old)";
    }

    // we have both
    if (yearStart.sort > yearEnd.sort) return "**(timetraveler, check your YAML)**";
    if (yearEnd.sort > current.sort)  return startPrefix + " " + yearStart.display + " (" + age + " years old)";

    return startPrefix + " " + yearStart.display + " - " + endPrefix + " " + yearEnd.display +  ", " + endStatus + " at " + (age) + " years old"
}

return get_PageDatedValue(dv.current())