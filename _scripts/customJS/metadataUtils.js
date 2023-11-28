class util {


    isAlive(metadata, targetDate) {
        const { DateManager } = customJS

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        else targetDate = DateManager.getTargetDateForPage(metadata)

        return DateManager.getPageDates(metadata, targetDate).isAlive
    }

    isLinkedToPerson(file, target) {
        
        const { NameManager } = customJS
    

        let allowInlinks = NameManager.getPageType(file.frontmatter) != "place"

        if (file.outlinks) {
            if (file.outlinks.includes(target.link)) return true;
        }

        if (file.inlinks && allowInlinks) {
            if (file.inlinks.includes(target.link)) return true;
        }

        return false;
    }


    isKnownToParty(file, personMetadata, campaignPrefix, allowTag, allowSessionNotes, campaignFolder) {

        const { NameManager } = customJS

        if (personMetadata.campaignInfo) {
            if (personMetadata.campaignInfo.some(f => f.campaign.toLowerCase() == campaignPrefix.toLowerCase()))
                return true;
        }

        if (personMetadata.tags) {
            if (allowTag) {
                let campaignTags = personMetadata.tags.filter(f => f.toLowerCase().startsWith(campaignPrefix.toLowerCase()))
                if (campaignTags.some(f => !f.contains("unaware") && !f.contains("unknown") && !f.contains("unsorted")))
                    return true
            }
        }

        if (allowSessionNotes) {
            if (!campaignFolder) {
                campaignFolder = NameManager.getCampaignSessionNoteFolder(campaignPrefix)
            }

            if (campaignFolder) {
                return DataviewAPI.page(file).file.inlinks.some(f => f.path.contains("Campaigns/" + campaignFolder + "/Session Notes") || f.path.contains(campaignFolder))
            }
        }

        return false;
    }

    isOrWasAffiliated(target, metadata, targetDate) {
        
        const { AffiliationManager } = customJS 
        const { DateManager } = customJS

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        else targetDate = DateManager.getTargetDateForPage(metadata.frontmatter)

        return AffiliationManager.isOrWasAffiliated(target, metadata.frontmatter, targetDate)
    }


    isAffiliated(target, metadata, targetDate) {
        
        const { AffiliationManager } = customJS 
        const { DateManager } = customJS

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        else targetDate = DateManager.getTargetDateForPage(metadata.frontmatter)

        return AffiliationManager.isAffiliated(target, metadata.frontmatter, targetDate)
    }

    inLocation(targetLocation, metadata, includeDead, includeLastKnown, targetDate) {

        const { WhereaboutsManager } = customJS
        const { LocationManager } = customJS
        const { DateManager } = customJS

        let pageDates = DateManager.getPageDates(metadata, targetDate)

        if (pageDates) {
            if (!pageDates.isCreated) return false
            if (!pageDates.isAlive && !includeDead) return false
        }

        let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
        if (!wb.current.location) {

            if (!wb.lastKnown.location || !includeLastKnown) return false;
            return LocationManager.isInLocation(wb.lastKnown.location, targetLocation, targetDate)
        }

        return LocationManager.isInLocation(wb.current.location, targetLocation, targetDate)
    }

    inOrHomeLocation(targetLocation, metadata, includeDead, targetDate) {
        return this.inLocation(targetLocation, metadata, includeDead, true, targetDate) || 
                this.homeLocation(targetLocation, metadata, includeDead, targetDate)
    }

    homeLocation(targetLocation, metadata, includeDead, targetDate) {

        const { WhereaboutsManager } = customJS
        const { DateManager } = customJS
        const { LocationManager } = customJS

        let pageDates = DateManager.getPageDates(metadata, targetDate)

        if (pageDates) {
            if (!pageDates.isCreated) return false
            if (!pageDates.isAlive && !includeDead) return false
        }


        let home = WhereaboutsManager.getWhereabouts(metadata, targetDate).home;
        if (home == undefined) return false;
        if (home.location == undefined) return false;

        return LocationManager.isInLocation(home.location, targetLocation, targetDate)
    }

    s(format, targetFile, targetDate) {
        const { StringFormatter } = customJS
        const { DateManager } = customJS

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        else targetDate = DateManager.getTargetDateForPage(targetFile.frontmatter)

        return StringFormatter.getFormattedString(format, {name: targetFile?.name ?? targetFile, frontmatter: targetFile.frontmatter}, targetDate)
    }

}
