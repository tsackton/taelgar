class LocationManager {
    
    isInLocation(startingLocation, targetLocation) {

        const { NameManager } = customJS

        if (startingLocation.trim() === targetLocation.trim())
            return true;

        if (startingLocation == "")
            return false

        if (startingLocation.indexOf(",") == -1) {
            // we have a single string
            let file = NameManager.getFileForTarget(startingLocation)
            if (file) {
                let nextLvl = file.frontmatter.partOf
                if (nextLvl) {
                    return isInLocation(nextLvl, targetLocation)
                }

                return false;
            }

            console.log("Unable to retrieve file for " + startingLocation)
            return false;
        } else {
            return startingLocation.contains(targetLocation)
        }
    }

    // this gets a location string in the form A, B, C based on the start. It will generate at most maxPieces parts including the start
    //  if the startingLocation has a comma we ignore partOf and maxPices
    getLocationName(location, casing = "default", maxPieces = 3, linkType = "always") {
        function trimTrailingComma(inStr) {
            let outStr = inStr.trimEnd()
            if (outStr.endsWith(",")) outStr = outStr.substring(0, outStr.length - 1)
            return outStr
        }
        const {NameManager} = customJS

        if (location == undefined) return "Unknown"
        if (location == "") return "Unknown"

        if (location.indexOf(",") == -1) {
            // walk the part of chain
            return trimTrailingComma(this.#getLocationFromPartOfs(location, 0, maxPieces, linkType, casing))
        }
        else {
            return location.split(',').map(f => customJS.NameManager.getName(f, linkType, casing)).join(", ")            
        }
    }

    #getLocationFromPartOfs(locationPiece, thisDepth, maxDepth, linkType, casing) {
      
        const {NameManager} = customJS

        if (thisDepth == maxDepth) return ""
        if (!locationPiece) return ""
        if (locationPiece == "Taelgar") return ""

        let nameSection = NameManager.getName(locationPiece, linkType, casing)
        let file = NameManager.getFileForTarget(locationPiece)
        
        // we can't keep going, because this piece doesn't exist
        if (!file) {
            return nameSection
        }  else {
            return nameSection + ", " + this.#getLocationFromPartOfs(file.frontmatter.partOf, thisDepth+1, maxDepth, linkType, casing)
        }
    }
}