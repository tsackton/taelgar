class LocationManager {

    isInLocation(startingLocation, targetLocation, targetDate) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS

        if (startingLocation == "")
            return false

        if (startingLocation == undefined)
            return false

        if (startingLocation.trim() === targetLocation.trim())
            return true;


        if (startingLocation.indexOf(",") == -1) {
            // we have a single string
            let file = NameManager.getFileForTarget(startingLocation)
            if (file) {
                let nextLvl = undefined
                let current = WhereaboutsManager.getWhereabouts(file.frontmatter, targetDate).current
                if (current) nextLvl = current.location;

                if (nextLvl) {
                    return this.isInLocation(nextLvl, targetLocation)
                }

                return false;
            }


            let match = new RegExp("[A-Z]{1}").exec(startingLocation)
            if (match && match.index > 0) {
                return this.isInLocation(startingLocation.substring(match.index), targetLocation)
            }

            console.log("Unable to retrieve file for " + startingLocation)
            return false;
        } else {
            return startingLocation.contains(targetLocation)
        }
    }

    getCurrentLocationName(location, targetDate, casing = "preserve", formatString = "", linkType = "always") {
        function trimTrailingComma(inStr) {
            let outStr = inStr.trimEnd()
            if (outStr.endsWith(",")) outStr = outStr.substring(0, outStr.length - 1)
            return outStr
        }

        let maxPieces = parseInt(formatString) ?? undefined

        if (location == undefined) return "Unknown"
        if (location == "") return "Unknown"

        if (location.indexOf(",") == -1) {
            // walk the part of chain
            return trimTrailingComma(this.#getLocationFromPartOfs(location, targetDate, 0, maxPieces, linkType, casing, formatString))
        }
        else {
            return location.split(',').map(f => customJS.NameManager.getName(f, linkType, casing)).join(", ")
        }
    }

    #getLocationFromPartOfs(locationPiece, targeDate, thisDepth, maxDepth, linkType, casing) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS

        if (thisDepth == maxDepth) return ""
        if (!locationPiece) return ""
        if (locationPiece == "Taelgar") return ""

        let nameSection = NameManager.getName(locationPiece, linkType, casing)
        let file = NameManager.getFileForTarget(locationPiece)

        // we can't keep going, because this piece doesn't exist
        if (!file) {
            // lets see if we have a match to our capital letter check
            let match = new RegExp("[A-Z]{1}").exec(locationPiece)
            if (match && match.index > 0) {
                return locationPiece.substring(0, match.index) + " " + this.#getLocationFromPartOfs(locationPiece.substring(match.index), targeDate, thisDepth, maxDepth, linkType, casing)
            }

            return nameSection
        } else {
            let nextLevel = undefined    

            let current = WhereaboutsManager.getWhereabouts(file.frontmatter, targeDate).current
            if (current) nextLevel = current.location;

            if (nextLevel) {
                return nameSection + ", " + this.#getLocationFromPartOfs(nextLevel, targeDate, thisDepth + 1, maxDepth, linkType, casing)
            }

            return nameSection
        }
    }
}