function get_PageDatedValue(metadata) {

    const { DateManager } = customJS
    const { NameManager } = customJS

    pageExistenceData = DateManager.getPageDates(metadata)        
    pageExistenceData.notExistenceError =  "**(doesn't yet exist)**";
    pageExistenceData.lengthDescriptor = "years old"
    pageExistenceData.lengthPrefix = "at"

    return NameManager.getDescriptionOfDateInformation(pageExistenceData)
}

return get_PageDatedValue(dv.current())