function get_RegnalValue(metadata) {
    
    const { DateManager } = customJS
    const { NameManager } = customJS

    let regnalData = DateManager.getRegnalDates(metadata)
   
    let displayOverride = 
    {
        pagePast : "reigned until <endDate>",
        pageCurrent: "reign started <startDate> (<length> years ago)",
        pagePastWithStart: "reigned <startDate> - <endDate> (<length> years)"
    }


    return NameManager.getDescriptionOfDateInformation(metadata, regnalData, displayOverride) 
}

return get_RegnalValue(dv.current() )