class util {


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

            console.log(campaignFolder)
            if (campaignFolder) {
                return DataviewAPI.page(file).file.inlinks.some(f => f.path.contains("Campaigns/" + campaignFolder + "/Session Notes") || f.path.contains(campaignFolder))
            }
        }

        return false;
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

        let current = metadata.partOf
        if (!current) {

            let currentWb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
            if (currentWb.current == undefined || currentWb.current.location == undefined || currentWb.current.location == "Unknown") {

                console.log(currentWb)

                if (includeLastKnown && currentWb.lastKnown && currentWb.lastKnown.location) {
                    return LocationManager.isInLocation(currentWb.lastKnown.location, targetLocation, targetDate)
                }
                return false;
            }

            current = currentWb.location
        }

        return LocationManager.isInLocation(current, targetLocation, targetDate)
    }

    inOrHomeLocation(targetLocation, metadata, includeDead, targeDate) {
        return this.inLocation(targetLocation, metadata, includeDead, true, targeDate) || this.homeLocation(targetLocation, metadata, includeDead, targeDate)
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
        if (home.location == undefined || home.location == "Unknown") return false;

        return LocationManager.isInLocation(home.location, targetLocation, targetDate)
    }

    getName(targetFile) {
        const { NameManager } = customJS
        return NameManager.getName(targetFile, "exists", "title")
    }

    getLoc(metadata, targetDate) {
        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS
        const { LocationManager } = customJS

        let wb = WhereaboutsManager.getWhereabouts(metadata, targetDate)
        
        if (wb.current) {
            return LocationManager.buildFormattedLocationString("<loc:2>", wb.current, targetDate, "", "", "", "")
        }
        else if (wb.lastKnown) {
            return LocationManager.buildFormattedLocationString("Last seen on <endDate> at <loc:2>", wb.lastKnown, targetDate, "", "", "", "")            
        }
        return "Unknown"        
    }

}
