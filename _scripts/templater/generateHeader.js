function generateHeader(tp,config) {

    if (tp.frontmatter.type == "NPC" || tp.frontmatter.type == "Ruler") {
        // create a NPC header // 

        // load campaign prefix and path to dv.view() scripts from config //
        const campaignValue = config.campaignPrefix;
        const dViewPath = config.dViewPath;
        
        // load metadataUtils via customJS //
    
        const {metadataUtils} = customJS

        // reformat basic variables //
        
        let ancestryDisplayValue = metadataUtils.Reformat(tp.frontmatter, "ancestry", " (", ")", "")
        let speciesDisplayValue = metadataUtils.Reformat(tp.frontmatter, "species", "", "", "unknown species")
        
        // get pronouns //
        
        let pronounDisplayValue = ", " + metadataUtils.get_Pronouns(tp.frontmatter)
        
        // get home and origin // 
        
        let homeDisplayValue = (tp.frontmatter.home || tp.frontmatter.homeRegion) ? 
            "\n>Based in: " + tp.user.getLocation(tp, "home") : ""
        
        let originDisplayValue = (tp.frontmatter.origin || tp.frontmatter.originRegion) ? 
            "\n>Originally from: " + tp.user.getLocation(tp, "origin") : ""

        // return string //

        if (tp.frontmatter.type == "NPC") { 
            
            headerString = "# " + tp.frontmatter.name + "\n>[!info]+ Biographical Summary" +
            "\n>" + speciesDisplayValue + ancestryDisplayValue + pronounDisplayValue +
            "\n>" + '`$=dv.view("' + dViewPath + 'get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? ' +
            'dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`' +
            originDisplayValue + homeDisplayValue + "\n"

        } else {
            
            headerString = "# " + tp.frontmatter.name + "\n>[!info]+ Biographical Summary" +
            "\n>" + speciesDisplayValue + ancestryDisplayValue + pronounDisplayValue +
            "\n>" + '`$=dv.view("' + dViewPath + 'get_PageDatedValue", {"currentYear" : (dv.current().yearOverride ? ' +
            'dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`' +
            "\n>" + '`$=dv.view("' + dViewPath + 'get_RegnalValue", {"currentYear" : (dv.current().yearOverride ? ' +
            'dv.current().yearOverride : FantasyCalendarAPI.getCalendars()[0].current.year)})`' +
            originDisplayValue + homeDisplayValue + "\n"

        }

    } else {
        headerString = "# " + tp.frontmatter.name + "\n>[!warning]+\n>**Header for type " + tp.frontmatter.type + " doesn't exist!**"
    }
    return headerString
}
module.exports = generateHeader