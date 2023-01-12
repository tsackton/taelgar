get_PageDatedValue(metadata, existYear, strings) {

    if (!strings) {
        strings = ""
    }
            
    let preExistError = "(not yet born)";
    let startPrefix = "b.";
    let endPrefix = "d.";
    let yearEnd = metadata.died;
    let yearStart = existYear

    if (strings != undefined) {
        if (strings.preExistError != undefined) preExistError = strings.preExistError;    
        if (strings.startPrefix != undefined) startPrefix = strings.startPrefix;
        if (strings.endPrefix != undefined) endPrefix = strings.endPrefix;
    }
    
    if (yearEnd == undefined) yearEnd = metadata.destroyed;
    
    let currentYear = metadata.yearOverride;
    if (currentYear == undefined) currentYear =  window.FantasyCalendarAPI.getCalendars()[0].current.year


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
        if (yearEnd < currentYear) return endPrefix + " " + yearEnd;
        // they have a death date, and it hasn't happened yet, but no born date, so nothing to show
        return "";
    }

    if (yearStart > currentYear) return preExistError;

    // we have both a start and end date - and they died before now
    if (yearEnd < currentYear) {       
        return startPrefix + " " + yearStart + " - " + endPrefix + " " + yearEnd +  " at age " + (yearEnd-yearStart);
    }

    return startPrefix + " " + yearStart + " (" + (currentYear-yearStart) + " years old)";
}