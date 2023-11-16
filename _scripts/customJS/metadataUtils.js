class metadataUtils {

    inLocation(targetLocation, metadata, targetDate) {

        const {WhereaboutsManager} = customJS
        const {LocationManager} = customJS

        let current = WhereaboutsManager.getWhereabouts(metadata, targetDate).current
        if (current == undefined || current.location == undefined || current.location == "Unknown") {
            return false;
        }

        return LocationManager.isInLocation(current.location, targetLocation)
    }

    homeLocation(targetLocation, metadata, targetDate, includeDead) {

        const {WhereaboutsManager} = customJS
        const {DateManager} = customJS
        const {LocationManager} = customJS

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
       
        const {WhereaboutsManager} = customJS
        const {LocationManager} = customJS

        let origin = WhereaboutsManager.getWhereabouts(metadata, targetDate).origin
        if (origin == undefined) return false;
        if (origin.location == undefined || origin.location == "Unknown") return false;

        return LocationManager.isInLocation(origin.location, targetLocation)        
    }
}
