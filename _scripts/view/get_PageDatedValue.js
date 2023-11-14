function get_PageDatedValue(metadata) {

    const { metadataUtils } = customJS

    currentYear = metadataUtils.get_pageEventsDate(metadata, false);
    pageExistenceData = metadataUtils.get_pageExistenceData(metadata, false)        

    if (!pageExistenceData.isCreated) return "**(doesn't yet exist)**";
    
    if (!pageExistenceData.isAlive) {
        if (pageExistenceData.age) {
            return pageExistenceData.startDescriptor[0] + ". " + pageExistenceData.startDate.display + " - " + pageExistenceData.endDescriptor[0] + ". " + pageExistenceData.endDate.display +  ", " + pageExistenceData.endDescriptor + " at " + (pageExistenceData.age) + " years old"
        }
        else {
            return pageExistenceData.endDescriptor + " " + yearEnd.display;
        }
    }
    else if (pageExistenceData.age) {
        // we are alive with a start date
        return pageExistenceData.startDescriptor + " " + pageExistenceData.startDate.display + " (" + pageExistenceData.age + " years old)";
    }
    else {
        // alive with no start date
        return "";
    }  
}

return get_PageDatedValue(dv.current())