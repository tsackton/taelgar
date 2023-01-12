function get_PageDatedValue(metadata, currentYear) {

    // get type //

    if (metadata.type == "NPC") {
        yearStart = metadata.born
        yearEnd = metadata.died
        preExistError = metadata.preExistError ? metadata.preExistError : "**(not yet born)**"
        startPrefix = metadata.startPrefix ? metadata.startPrefix : "b.";
        endPrefix = metadata.endPrefix ? metadata.endPrefix : "d.";
        endStatus = metadata.endStatus ? metadata.endStatus : "died"
    } else if (metadata.type == "Ruler") {
        yearStart = metadata.born
        yearEnd = metadata.died
        preExistError = metadata.preExistError ? metadata.preExistError : "**(not yet born)**"
        startPrefix = metadata.startPrefix ? metadata.startPrefix : "b.";
        endPrefix = metadata.endPrefix ? metadata.endPrefix : "d.";
        endStatus = metadata.endString ? metadata.endString : "died"
    } else if (metadata.type == "Building") {
        yearStart = metadata.built
        yearEnd = metadata.destroyed
        preExistError = metadata.preExistError ? metadata.preExistError : "**(not yet built)**"
        startPrefix = metadata.startPrefix ? metadata.startPrefix : "built";
        endPrefix = metadata.endPrefix ? metadata.endPrefix : "destroyed";
        endStatus = metadata.endString ? metadata.endString : "destroyed"
    } else if (metadata.type == "Item") {
        yearStart = metadata.created
        yearEnd = metadata.destroyed
        preExistError = metadata.preExistError ? metadata.preExistError : "**(not yet created)**"
        startPrefix = metadata.startPrefix ? metadata.startPrefix : "created";
        endPrefix = metadata.endPrefix ? metadata.endPrefix : "destroyed";
        endStatus = metadata.endString ? metadata.endString : "destroyed"
    }

    currentYear = metadata.yearOverride ? metadata.yearOverride : currentYear
    
    if (!yearStart && !yearEnd) return "";
    if (yearStart && yearEnd && yearStart > yearEnd) return "(timetraveler, check your YAML)";
    
    // we have a created year, no ended year
    if (yearStart && !yearEnd) {
        if (yearStart > currentYear) return preExistError;
        
        let age = currentYear - yearStart;

        return startPrefix + " " + yearStart + " (" + age + " years old)";
    }

    // we have a death year, no born year
    if (yearEnd && !yearStart) {
        if (yearEnd < currentYear) return endPrefix + " " + yearEnd + ", " + endStatus + " at unknown age";
        // they have a death date, and it hasn't happened yet, but no born date, so nothing to show
        return "";
    }

    if (yearStart > currentYear) return preExistError;

    // we have both a start and end date - and they died before now
    if (yearEnd < currentYear) {       
        return startPrefix + " " + yearStart + " - " + endPrefix + " " + yearEnd +  ", " + endStatus + " at " + (yearEnd-yearStart) + " years old"
    }

    return startPrefix + " " + yearStart + " (" + (currentYear-yearStart) + " years old)";
}

return get_PageDatedValue(dv.current(), input.currentYear)