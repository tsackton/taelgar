function get_PageDatedValue(metadata) {

    const { DateManager } = customJS
    const { NameManager } = customJS

    pageExistenceData = DateManager.getPageDates(metadata)        

    return NameManager.getDescriptionOfDateInformation(metadata, pageExistenceData)
}

return get_PageDatedValue(dv.current())