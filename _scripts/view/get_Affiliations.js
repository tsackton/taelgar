function get_Affiliations(metadata) {

    const { AffiliationManager } = customJS

    let leadBy = AffiliationManager.getLeadBy(metadata.file.name)    
    return (leadBy + "\n" + AffiliationManager.getFormattedNonPrimaryAffiliations(metadata)).trim()

}

return get_Affiliations(dv.current())