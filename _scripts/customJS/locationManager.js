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


            let match = new RegExp("[~A-Z]{1}").exec(startingLocation)
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

    #shouldAllowPiece(formatStr, currentDepth, targetMetadata) {
        /*** 
            R = include regions only; r = exclude regions (i.e. places with typeOf region)
            L = include locations only; l = exclude locations
            P = include people only; p = exclude people
            I = include items only; p = exclude items
            F = include first step only; f = exclude first step
            O = include organizations only; o = exclude organizations
         */

        const { NameManager } = customJS
        let pageType = NameManager.getPageType(targetMetadata)


        if (formatStr.contains("F")) {
            if (currentDepth != 0) return false
        } 
        
        if (formatStr.contains("f")) {
            if (currentDepth == 0) return false
        }

        if (formatStr.contains("r")) {
            if (targetMetadata.typeOf == "region") return false
        }
        
        if (formatStr.contains("R")) {
            if (targetMetadata.typeOf != "region") return false
        }

        if (formatStr.contains("L")) {
            if (pageType != "place") return false
        }

        if (formatStr.contains("l")) {
            if (pageType == "place") return false
        }

        if (formatStr.contains("P")) {
            if (pageType != "person") return false
        }

        if (formatStr.contains("p")) {
            if (pageType == "person") return false
        }


        if (formatStr.contains("I")) {
            if (pageType != "item") return false
        }

        if (formatStr.contains("i")) {
            if (pageType == "item") return false
        }
        
        if (formatStr.contains("O")) {
            if (pageType != "organization") return false
        }

        if (formatStr.contains("o")) {
            if (pageType == "organization") return false
        }

        return true
    }

    #getLocationFromPartOfs(locationPiece, targeDate, thisDepth, maxDepth, linkType, casing, format) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS

        if (thisDepth == maxDepth) return ""
        if (!locationPiece) return ""
        if (locationPiece == "Taelgar") return ""

        let nameSection = NameManager.getName(locationPiece, linkType, casing)
        let file = NameManager.getFileForTarget(locationPiece)

        if (!this.#shouldAllowPiece()) nameSection = undefined

        // we can't keep going, because this piece doesn't exist
        if (!file) {
            // lets see if we have a match to our capital letter check
            let match = new RegExp("[~A-Z]{1}").exec(locationPiece)
            if (match && match.index > 0) {

                // at the moment there is a bug where the filters ignore this type of thing - or more accurately, we end up with the "travelling in " or whatever piece added no matter what
                let potentialNextPiece = locationPiece.substring(match.index)              
               
                return locationPiece.substring(0, match.index) + " " + this.#getLocationFromPartOfs(potentialNextPiece, targeDate, thisDepth, maxDepth, linkType, casing)
            }

            return nameSection
        } else {
            let nextLevel = undefined

            let current = WhereaboutsManager.getWhereabouts(file.frontmatter, targeDate).current
            if (current) nextLevel = current.location;

            if (nextLevel && nameSection) {
                return nameSection + ", " + this.#getLocationFromPartOfs(nextLevel, targeDate, thisDepth + 1, maxDepth, linkType, casing)
            } else if (nextLevel) {
                return this.#getLocationFromPartOfs(nextLevel, targeDate, thisDepth + 1, maxDepth, linkType, casing)
            } else if (nameSection) {
                return nameSection
            } else {
                return ""
            }
        }
    }
}