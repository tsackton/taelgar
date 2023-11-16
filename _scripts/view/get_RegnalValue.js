function get_RegnalValue(metadata) {
    
    const { DateManager } = customJS
    const { NameManager } = customJS

    let regnalData = DateManager.getRegnalDates(metadata)
    console.log(regnalData)
    regnalData.notExistenceError = ""
    regnalData.startDescriptor = "reigning since"
    regnalData.startPrefix = "reigned"
    regnalData.endPrefix = ""
    regnalData.endDescriptor = ""
    regnalData.lengthDescriptor = "years"
    regnalData.lengthPrefix = "for"

    return NameManager.getDescriptionOfDateInformation(regnalData) 
}

return get_RegnalValue(dv.current() )