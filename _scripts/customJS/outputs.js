class OutputHandler {

    regenerateHeader(oldContents, fileName, metadata, dynamic) {

        const versionNumber = "2023.11.25"
        const prevVersionNumber = "legacy"
        const nextVersionNumber = "2023.11.25"           
        
        let currentContents = oldContents.split('\n');  
    
        let version = metadata.version
    
        let vnToUse = versionNumber
        if (version == "next") vnToUse = nextVersionNumber
        else if (version == "old") vnToUse = prevVersionNumber
    
    
        // the end of the yaml -- this is 0-counting, so if the file is just a yaml start and end it will be 1
        let indexOfYamlEnd = currentContents.findIndex((f, i) => i>0 && f == "---");
        
        if (indexOfYamlEnd > 0) {
            let yaml = currentContents.filter((v, i) => i >= 0 && i <indexOfYamlEnd)
            let headerVersionIndex = yaml.findIndex(f => f.trim().startsWith("headerVersion"))
            if (headerVersionIndex >= 0) {
                currentContents[headerVersionIndex] = "headerVersion: " + vnToUse
            } else {
                currentContents.splice(1, 0, "headerVersion: " + vnToUse)
                indexOfYamlEnd++
            }
        }
    
        // find the end of the header block -- the first newline (blank line) after the YAML block
        let indexOfHeaderBlockEnd = currentContents.findIndex((f, i) => i > indexOfYamlEnd && f.trim() == "");
    
        // the file is ONLY yaml
        if (indexOfHeaderBlockEnd == -1) {
            indexOfHeaderBlockEnd = currentContents.length;
        }
        
        // starting from the first newline, find the first non-newline
        let emptySpaceEnd = currentContents.findIndex((f, i) => i > indexOfHeaderBlockEnd && f.trim() != "");
        if (emptySpaceEnd != -1) {
            indexOfHeaderBlockEnd = emptySpaceEnd - 1
        }
    
        if (currentContents.slice(indexOfYamlEnd, indexOfHeaderBlockEnd).filter(f => f.trim().startsWith("#")).length == 0) {
            // there is no H1 block in the "header" so it cannot have been an actual header. 
            indexOfHeaderBlockEnd = indexOfYamlEnd
        }
    
        let data =  this.generateHeader(fileName, metadata, dynamic, version)
    
        // remove the header block
        currentContents.splice(indexOfYamlEnd+1, indexOfHeaderBlockEnd-indexOfYamlEnd);          
        // insert the template
        currentContents.splice(indexOfYamlEnd+1, 0, data);  
    
        // rewrite the file
        return currentContents
    }


    /*  # DisplayName
    *(pronunciation)*
    >[!info] BOXNAME
    > TYPE-SPECIFIC TEXT
    > pagedated if it exists (dynamic, insert call to "get page dates")
    > regnal info (dynamic, includes leader of)    
    > partOf if it exists [static line, not auto-generated]
    >> whereabouts if it exists
    >> campaign info
    >> afflitaions
    */

    generateHeader(fileName, metadata, dynamic = true, version = undefined) {

        const { EventManager } = customJS
        const { NameManager } = customJS
        const { OutputHandler } = customJS
        const { TokenParser } = customJS
        const { DateManager } = customJS
    
        let file = { name: fileName, frontmatter: metadata }
        let displayDefaults = NameManager.getDisplayData(metadata)
        let pageDates = DateManager.getPageDates(metadata)
        let hasPageDates = pageDates.startDate || pageDates.endDate
        let pageType = NameManager.getPageType(metadata)
    
        let output = TokenParser.parseDisplayString("# <name:tn>", file) + "\n"
    
        let secondary = TokenParser.parseDisplayString("*(<pronunciation>)*", file)
        if (secondary && secondary.length > 0) {
            output += secondary + "\n"
        }
    
        let summaryBlockLines = []
    
        let typeOf = TokenParser.parseDisplayString(displayDefaults.boxInfo, file)
        if (typeOf && typeOf.length > 0) {
            summaryBlockLines.push("> " + typeOf)
        }
    
        if (metadata.ddbLink && displayDefaults.mechanicsLink && displayDefaults.mechanicsLink.length > 0) {
            summaryBlockLines.push("> [" + displayDefaults.mechanicsLink + "](" + metadata.ddbLink + ")")
        }
    
        if (hasPageDates) {
    
            let line = '`$=dv.view(\"_scripts/view/get_PageDatedValue\")`'
            if (!dynamic) {
                line = OutputHandler.outputPageDatedValue(fileName, metadata)
            }
    
            summaryBlockLines.push("> " + line)
        }
    
        if (metadata.leaderOf || metadata.affiliations || pageType == "place" || pageType == "organization" || pageType == "item") {
    
            let line = '`$=dv.view(\"_scripts/view/get_Affiliations\")`'
            if (!dynamic) {
                line = OutputHandler.outputAffiliations(fileName, metadata)
            }
            summaryBlockLines.push("> " + line)
        }
    
        let partOf = TokenParser.parseDisplayString(displayDefaults.partOf, file)
        if (partOf && partOf.length > 0) {
            summaryBlockLines.push("> " + partOf)
        }
    
        if (metadata.whereabouts || (pageType == "place" && metadata.partOf)) {
            let line = '`$=dv.view(\"_scripts/view/get_Whereabouts\")`';
            if (!dynamic) {
                line = OutputHandler.outputWhereabouts(fileName, metadata)
            }
    
            summaryBlockLines.push(">> " + line.trim())
        }
    
        for (let meeting of EventManager.getPartyMeeting(file)) {
            summaryBlockLines.push(`>> %%^Campaign:${meeting.campaign}%% ${meeting.text} %%^End%%`);
        }
    
        if (summaryBlockLines.length > 0) {
            output += ">[!info]+ " + displayDefaults.boxName + "\n"
        }
    
        output += summaryBlockLines.join("\n")
        return output + "\n"
    }

    outputWhereabouts(fileName, metadata) {

        const { WhereaboutsManager } = customJS
        const { DateManager } = customJS
        const { NameManager } = customJS
        const { TokenParser } = customJS
    
        let displayDefaults = NameManager.getDisplayData(metadata)
        let file = { name: fileName, frontmatter: metadata }
    
        let pageData = DateManager.getPageDates(metadata);
        let pageYear = DateManager.getTargetDateForPage(metadata)
    
        if (!pageData.isCreated) return "";
    
        let isPageAlive = pageData.isAlive
    
        // if page is dead/destroyed, get whereabouts as of died/destroyed date //
        // if we want to allow dead bodies to move around, would need to change this //
        // however, currently don't have a good location to track "Died at" so might be complicated //
        // but commenting to track for the future //
        if (!isPageAlive) pageYear = pageData.endDate
    
        let whereabout = WhereaboutsManager.getWhereabouts(metadata, pageYear)
    
        let displayString = "", homeString = ""
    
        // knownLastKnown is false if whereabout.lastKnown.awayEnd.display is falsey (it was 0001 or 9999) //
        // or if whereabout.lastKnown.awayEnd is nullish //
        let knownLastKnown = whereabout.lastKnown.awayEnd?.display ? true : false
    
        // origin string construction //
        // if origin is unknown, use unknown string //
        // don't care about alive/dead for origin //
        let originString = TokenParser.parseDisplayString(whereabout.origin.location ? (whereabout.origin.originFormat ?? displayDefaults.wOrigin) : displayDefaults.wOriginU, file, pageYear)
    
        // home string construction //
        if (isPageAlive) {
            homeString = TokenParser.parseDisplayString(whereabout.home.location ? (whereabout.home.homeFormat ?? displayDefaults.wHome) : displayDefaults.wHomeU, file, pageYear)
        } else {
            homeString = TokenParser.parseDisplayString(whereabout.home.location ? (whereabout.home.pastHomeFormat ?? displayDefaults.wPastHome) : displayDefaults.wPastHomeU, file, pageYear)
        }
    
        // current string construction //    
        let currentString = TokenParser.parseDisplayString((isPageAlive ? (whereabout.current.currentFormat ?? displayDefaults.wCurrent) : (whereabout.current.pastFormat ?? displayDefaults.wPast)), file, pageYear)
    
        // last known string construction //
        let knownString = TokenParser.parseDisplayString(knownLastKnown ? (whereabout.lastKnown.lastKnownFormat ?? displayDefaults.wLastKnown) : (whereabout.lastKnown.lastKnownFormat ?? displayDefaults.wLastNoDate), file, pageYear)
    
    
        if (!whereabout.origin.location || whereabout.origin.location != whereabout.home.location) {
            // display origin if it is not the same as home or it is unknown //
            displayString += originString + "\n"
        }
    
        // always display home
        displayString += homeString + "\n"
    
        if (!whereabout.current.location || whereabout.current.location != whereabout.home.location) {
            // display current if it is not the same as home or if current is unknown //
            displayString += currentString + "\n"
        }
    
        if (!whereabout.current.location && whereabout.lastKnown.location && whereabout.lastKnown.location != whereabout.home.location) {
            // display last known if current is unknown and last known is known, as long as it isn't the same as home //        
            // note it is not clear last known can ever be same as home but this is added to just double-confirm we don't show 2x of the same thing //
            displayString += knownString + "\n"
        }
    
        // remove extra newlines //
        return displayString.replace(/\n\n+/g, "\n");
    }

    outputAffiliations(fileName, metadata) {
        const { AffiliationManager } = customJS

        let leadBy = AffiliationManager.getLeadBy(fileName)
        return (leadBy + "\n" + AffiliationManager.getFormattedNonPrimaryAffiliations(metadata)).trim()
    }


    outputPageDatedValue(fileName, metadata) {
        const { DateManager } = customJS
        const { TokenParser } = customJS
        const { NameManager } = customJS

        let dateInfo = DateManager.getPageDates(metadata)
        let pageDisplayData = NameManager.getDisplayData(metadata)
        let formatStr = ""

        if (!dateInfo.isCreated) return "**(page is future dated)**"

        if (dateInfo.endDate && dateInfo.endDate.display == "") {
            formatStr = pageDisplayData.dPast
        }
        else if (dateInfo.isAlive) {
            if (!dateInfo.startDate) {
                // we have a death date in the future and no start date, output nothing
                return ""
            }
            formatStr = pageDisplayData.dCurrent
        }
        else if (dateInfo.age || (dateInfo.age == 0 && dateInfo.startDate?.display?.length > 0)) {
            formatStr = pageDisplayData.dPastHasStart
        }
        else if (dateInfo.endDate) {
            formatStr = pageDisplayData.dPast
        }
        else {
            return ""
        }

        return TokenParser.parseDisplayString(formatStr, { name: fileName, frontmatter: metadata })

    }

}