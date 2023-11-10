

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
        defaultStart =  "created";      
    } else if (metadata.type == "Place") {
        defaultPreexistError =  "**(not yet founded)**"
        defaultStart =  "founded";       
    }

    preExistError = metadata.preExistError ? metadata.preExistError : defaultPreexistError
    startPrefix = metadata.startPrefix ? metadata.startPrefix : defaultStart
    endPrefix = metadata.endPrefix ? metadata.endPrefix : defaultEnd
    endStatus = metadata.endStatus ? metadata.endStatus : defaultEndStatus

    currentYear = metadataUtils.get_pageEventsDate(metadata);
    yearStart = metadataUtils.get_existEventsDate(metadata)
    yearEnd = metadataUtils.get_endEventsDate(metadata)

    console.log("Using " + currentYear.display + " as current, " + yearStart.display + " as start")

    if (!yearStart && !yearEnd) return "";
    if (yearStart && yearEnd && yearStart.sort > yearEnd.sort) return "**(timetraveler, check your YAML)**";

    // we have a created year, no ended year
    if (yearStart && !yearEnd) {
        if (yearStart.sort > currentYear.sort) return preExistError;
        
        let age = metadataUtils.get_Age(currentYear.jsDate, yearStart.jsDate)

        return startPrefix + " " + yearStart.display + " (" + age + " years old)";
    }

    // we have a death year, no born year
    if (yearEnd && !yearStart) {
        if (yearEnd.sort  <= currentYear.sort) return endStatus + " " + yearEnd.display;
        // they have a death date, and it hasn't happened yet, but no born date, so nothing to show
        return "";
    }

    if (yearStart.sort  > currentYear.sort ) return preExistError;

    // we have both a start and end date - and they died before now
    if (yearEnd.sort  <= currentYear.sort) {       
        return startPrefix + " " + yearStart.display + " - " + endPrefix + " " + yearEnd.display +  ", " + endStatus + " at " + (metadataUtils.get_Age(yearEnd.jsDate, yearStart.jsDate)) + " years old"
    }

    return startPrefix + " " + yearStart.display + " (" + ( metadataUtils.get_Age(currentYear.jsDate, yearStart.jsDate)) + " years old)";
}

return get_PageDatedValue(dv.current())