function get_PageDatedValue(metadata, currentYear, existYear, startPrefix, endPrefix, preExistError) {

    preExistError = preExistError ? preExistError : "(not yet born)";
    startPrefix = startPrefix ? startPrefix : "b.";
    endPrefix = endPrefix ? endPrefix : "d.";
    endString = metadata.endString ? metadata.endString : "deceased"
    currentYear = metadata.yearOverride ? metadata.yearOverride : currentYear

    let yearEnd = metadata.died ? metadata.died : metadata.destroyed
    let yearStart = existYear ? existYear : 0
    
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

return get_PageDatedValue(dv.current(), input.currentYear, input.existYear, input.startPrefix, input.endPrefix, input.preExistError)