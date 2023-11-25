function get_Affiliations(metadata) {

    const { AffiliationManager } = customJS

    return AffiliationManager.getFormattedNonPrimaryAffiliations(metadata)

}

return get_Affiliations(dv.current())