class util {


    isKnownToParty(file, personMetadata, campaignPrefix, allowTag, allowSessionNotes, campaignFolder) {

        const {NameManager} = customJS

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

    inLocation(targetLocation, metadata, allowDead, targetDate) {

        const { WhereaboutsManager } = customJS
        const { LocationManager } = customJS
        const { DateManager } = customJS

        let pageDates = DateManager.getPageDates(metadata, targetDate)

        if (pageDates) {
            if (!pageDates.isCreated) return false
            if (!pageDates.isAlive && !allowDead) return false
        }

        let current = metadata.partOf
        if (!current) {

            let currentWb = WhereaboutsManager.getWhereabouts(metadata, targetDate).current
            if (currentWb == undefined || currentWb.location == undefined || currentWb.location == "Unknown") {
                return false;
            }

            current = currentWb.location
        }

        return LocationManager.isInLocation(current, targetLocation, targetDate)
    }

    getName(targetFile) {
        const { NameManager } = customJS
        return NameManager.getName(targetFile, "exists", "title")
    }

    homeLocation(targetLocation, metadata, targetDate, includeDead) {

        const { WhereaboutsManager } = customJS
        const { DateManager } = customJS
        const { LocationManager } = customJS

        let pageDates = DateManager.getPageDates(metadata, targetDate)

        if (includeDead || pageDates.isAlive) {
            let home = WhereaboutsManager.getWhereabouts(metadata, targetDate).home;
            if (home == undefined) return false;
            if (home.location == undefined || home.location == "Unknown") return false;

            return LocationManager.isInLocation(home.location, targetLocation)
        }

        return false;
    }

    fromLocation(targetLocation, metadata, targetDate) {

        const { WhereaboutsManager } = customJS
        const { LocationManager } = customJS

        let origin = WhereaboutsManager.getWhereabouts(metadata, targetDate).origin
        if (origin == undefined) return false;
        if (origin.location == undefined || origin.location == "Unknown") return false;

        return LocationManager.isInLocation(origin.location, targetLocation)
    }
}
