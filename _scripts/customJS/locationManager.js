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
                let nextLvl = file.frontmatter.partOf
                if (!nextLvl) {
                    if (file.frontmatter.whereabouts) {
                        let current = WhereaboutsManager.getWhereabouts(file.frontmatter, targetDate).current                    
                        if (current) nextLvl = current.location;
                    }
                }

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

    buildFormattedLocationString(formatStr, whereabout, targetDate, endStatus, metStatus, person, startStatus) {

        const { DateManager } = customJS
        const { NameManager } = customJS
        
        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)


        let group = formatStr.match("<loc(:([0-9]*)([a-z]{0,1}))?>")
        let location = ""
        if (group) {
            formatStr = formatStr.replace(group[0], "<loc>")

            let casing = NameManager.PreserveCase
            if (group[3] == "l") casing = NameManager.LowerCase
            else if (group[3] == "t") casing = NameManager.TitleCase
            console.log("following string " + whereabout?.location + " for date " + targetDate?.display)
            location = whereabout ? this.getCurrentLocationName(whereabout.location, targetDate, casing, parseInt(group[2]), NameManager.CreateLink) : ""
        }
        else {
            console.log("following string " + whereabout?.location + " for date " + targetDate?.display)
            location = whereabout ? this.getCurrentLocationName(whereabout.location, targetDate) : ""
        }

        let formatted = formatStr.replace("<loc>", location)
            .replace("<start>", startStatus)
            .replace("<startDate>", whereabout?.start?.display)
            .replace("<endDate>", whereabout?.awayEnd?.display)
            .replace("<end>", endStatus)
            .replace("<person>", person)
            .replace("<met>", metStatus)
            .replace("<target>", (!targetDate ? "" : targetDate.display))

        return (formatted.charAt(0).toUpperCase() + formatted.slice(1)).trim()

    }

    getCurrentLocationName(location, targetDate, casing = "default", maxPieces = 3, linkType = "always") {
        function trimTrailingComma(inStr) {
            let outStr = inStr.trimEnd()
            if (outStr.endsWith(",")) outStr = outStr.substring(0, outStr.length - 1)
            return outStr
        }

        if (maxPieces == undefined || isNaN(maxPieces)) maxPieces = 3

        if (location == undefined) return "Unknown"
        if (location == "") return "Unknown"

        if (location.indexOf(",") == -1) {
            // walk the part of chain
            return trimTrailingComma(this.#getLocationFromPartOfs(location, targetDate, 0, maxPieces, linkType, casing))
        }
        else {
            return location.split(',').map(f => customJS.NameManager.getName(f, linkType, casing)).join(", ")
        }
    }

    // this gets a location string in the form A, B, C based on the start. It will generate at most maxPieces parts including the start
    //  if the startingLocation has a comma we ignore partOf and maxPices
    getLocationName(location, casing = "default", maxPieces = 3, linkType = "always") {
        return this.getCurrentLocationName(location, undefined, casing, maxPieces, linkType)
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

            let nextLevel = file.frontmatter.partOf
            if (!nextLevel) {
                if (file.frontmatter.whereabouts) {
                    let current = WhereaboutsManager.getWhereabouts(file.frontmatter, targeDate).current                    
                    if (current) nextLevel = current.location;
                }
            }

            if (nextLevel) {
                return nameSection + ", " + this.#getLocationFromPartOfs(nextLevel, targeDate, thisDepth + 1, maxDepth, linkType, casing)
            }

            return nameSection
        }
    }
}