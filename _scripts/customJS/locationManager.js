class LocationManager {

    isInLocation(startingLocation, targetLocation, targetDate) {

        // this takes a note and a target location
        // and returns true if the note is in the starting location
        // at the target date

        // to think about: if starting location is, e.g. "wandering, north of Tokra" and target location is "Dunmar"
        // this will return false, even though it should return true

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS

        // Check for null, undefined, or empty string
        if (!startingLocation || startingLocation.trim() === "") {
            return false;
        }

        // Check if trimmed values are equal
        if (startingLocation.trim() === targetLocation.trim()) {
            return true;
        }

        // we have a single string
        let file = NameManager.getFileForTarget(startingLocation)
        if (file) {

            let nextLvl = WhereaboutsManager.getWhereabouts(file.frontmatter, targetDate).current.location

            if (nextLvl) {
                return this.isInLocation(nextLvl, targetLocation)
            }

            return false;
        }


        let match = new RegExp("[~A-Z]{1}").exec(startingLocation)
        if (match && match.index > 0) {
            return this.isInLocation(startingLocation.substring(match.index), targetLocation)
        }

        return false;
    }

    getCurrentLocationName(location, targetDate, casing = "preserve", formatString = "", linkType = "always") {
        
        // fasly locations (null, undefined, empty string) are always unknown
        if (!location) return "Unknown"

        // we want the current depth to start at 1, i.e. if the max depth is 2 we want the first and second pieces
        let outStr = this.#getLocationFromPartOfs(location, targetDate, 1, linkType, casing, formatString).trim()
        
        if (outStr.endsWith(",")) outStr = outStr.substring(0, outStr.length - 1)
        
        if (!outStr) return "(location hidden)"
        return outStr
    }

    #shouldAllowPiece(formatStr, currentDepth, targetMetadata) {
        /*** 
            R = include regions only; r = exclude regions (i.e. places with typeOf region)
            L = include locations only; l = exclude locations
            P = include people only; p = exclude people
            I = include items only; p = exclude items
            F = include first step only; f = exclude first step
            O = include organizations only; o = exclude organizations
         */

        let successResult = {
            continue: true,
            allowed: true,
            incrementDepth: true
        }

        let depthFilterFailed = {
            continue: true,
            allowed: false,
            incrementDepth: true
        }

        let typeFilterFailed = {
            continue: true,
            allowed: false,
            incrementDepth: false
        }

        const { NameManager } = customJS
        let pageType = NameManager.getPageType(targetMetadata)

        let maxDepth = undefined
        let minDepth = undefined

        let fsSplit = formatStr.split('-')

        if (fsSplit.length == 2) {
            // we have something like xxx-yyyy
            // the number has to be first, as that is what parseInt expects, that is, parseInt(2ttt) returns 2 but parseInt(ttt2) returns undefined

            minDepth = parseInt(fsSplit[0])
            maxDepth = parseInt(fsSplit[1])
        } else {
            maxDepth = parseInt(formatStr)
        }

        if (minDepth && currentDepth < minDepth) {
            // we are before the min depth, continue without this, but increment
            return depthFilterFailed
        }

        if (formatStr.contains("F")) {
            if (currentDepth != 0) return depthFilterFailed
        }

        if (formatStr.contains("f")) {
            if (currentDepth == 0) return depthFilterFailed
        }

        if (formatStr.contains("r")) {
            if (targetMetadata.typeOf == "region") return typeFilterFailed
        }

        if (formatStr.contains("R")) {
            if (targetMetadata.typeOf != "region") return typeFilterFailed
        }

        if (formatStr.contains("L")) {
            if (pageType != "place") return typeFilterFailed
        }

        if (formatStr.contains("l")) {
            if (pageType == "place") return typeFilterFailed
        }

        if (formatStr.contains("P")) {
            if (pageType != "person") return typeFilterFailed
        }

        if (formatStr.contains("p")) {
            if (pageType == "person") return typeFilterFailed
        }

        if (formatStr.contains("I")) {
            if (pageType != "item") return typeFilterFailed
        }

        if (formatStr.contains("i")) {
            if (pageType == "item") return typeFilterFailed
        }

        if (formatStr.contains("O")) {
            if (pageType != "organization") return typeFilterFailed
        }

        if (formatStr.contains("o")) {
            if (pageType == "organization") return typeFilterFailed
        }

        // this has to be last, or we allow types that are at the max depth but are the wrong kind
        if (maxDepth && currentDepth >= maxDepth) {
            // we have reached the max depth, don't continue but do include this one
            return { continue: false, allowed: true }
        }


        return successResult
    }

    #getLocationFromPartOfs(locationPiece, targetDate, thisDepth, linkType, casing, format) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS

        if (!locationPiece) return ""
        if (locationPiece == "Taelgar") return ""

        let nameSection = NameManager.getName(locationPiece, linkType, casing)
        let file = NameManager.getFileForTarget(locationPiece)


        // we can't keep going, because this piece doesn't exist
        if (!file) {
            // lets see if we have a match to our capital letter check
            let match = new RegExp("[~A-Z]{1}").exec(locationPiece)
            if (match && match.index > 0) {

                // at the moment there is a bug where the filters ignore this type of thing - or more accurately, we end up with the "travelling in " or whatever piece added no matter what
                let potentialNextPiece = locationPiece.substring(match.index)
                return locationPiece.substring(0, match.index) + " " + this.#getLocationFromPartOfs(potentialNextPiece, targetDate, thisDepth, linkType, casing, format)
            }

            return nameSection
        } else {

            let nextLevelCheck = this.#shouldAllowPiece(format, thisDepth, file.frontmatter)

            if (!nextLevelCheck.continue) {
                return nameSection ?? ""
            }

            let nextDepth = nextLevelCheck.incrementDepth ? thisDepth + 1 : thisDepth
            let nextLevel = WhereaboutsManager.getWhereabouts(file.frontmatter, targetDate).current.location
            let returnValue = ""

            if (nextLevelCheck.allowed) {
                // this piece is allowed, add it //
                returnValue += nameSection + ", "
            }

            if (nextLevelCheck.continue && nextLevel) {
                // we are allowed to continue, and we have somewhere to go //
                returnValue += this.#getLocationFromPartOfs(nextLevel, targetDate, nextDepth, linkType, casing, format)
            }

            return returnValue
        }
    }
}