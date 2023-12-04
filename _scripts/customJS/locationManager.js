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
                return this.isInLocation(nextLvl, targetLocation, targetDate)
            }

            return false;
        }

        return false
    }

    getCurrentLocationName(whereabout, targetDate, filter = "", sourcePageType, format, firstFormat) {

        // we want the current depth to start at 1, i.e. if the max depth is 2 we want the first and second pieces
        let outStr = this.#getLocationFromPartOfs(whereabout, targetDate, 1, format, filter, sourcePageType, firstFormat).trim()

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
            if (currentDepth != 1) return depthFilterFailed
        }

        if (formatStr.contains("f")) {
            if (currentDepth == 1) return depthFilterFailed
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

    #getDescriptionForThisPiece(whereabout, format, targetDate, sourcePageType) {

        const { TokenParser } = customJS
        const { NameManager } = customJS

        let file = NameManager.getFileForTarget(whereabout.location)
        if (!file) {
            // we don't have a file, we are not going to be able to do a lot of fancy formattting, but lets see what we can do
            file = { frontmatter: {} }

        } else {
            file = { frontmatter: file.frontmatter }
        }

        let formatStr = whereabout.format ?? "<name:" + format + ">"

        let name = NameManager.getNameObject(whereabout.location, sourcePageType, {
            alias: whereabout.alias,
            linkText: whereabout.linkText,
        })

        return TokenParser.parseDisplayString(formatStr, file, targetDate, {
            name: name
        })
    }

    #getLocationFromPartOfs(whereabout, targetDate, thisDepth, format, filter, sourcePageType, firstFormat) {

        const { NameManager } = customJS
        const { WhereaboutsManager } = customJS

        let formatToUse = thisDepth == 1 ? firstFormat : format;

        if (!whereabout || !whereabout.location) {
            let returnForUnknown = "";
            if (whereabout.linkText) returnForUnknown = whereabout.linkText + " "
            if (whereabout.alias) returnForUnknown += whereabout.alias

            if (!whereabout.linkText && !whereabout.alias)
                returnForUnknown = "Unknown"

            return returnForUnknown.trim()
        }

        if (whereabout.location == "Taelgar") {
            // Taelgar is handling specially
            if (thisDepth > 1) return ""
            if (filter.includes("r")) return ""

            // for now this is hardcoded
            return this.#getDescriptionForThisPiece(whereabout, formatToUse, targetDate, sourcePageType, "Gazetteer")
        }

        let file = NameManager.getFileForTarget(whereabout.location)

        // we can't keep going, because this piece doesn't exist
        if (!file) {
            // lets see if we have a match to our capital letter check
            let match = new RegExp("[~A-Z]{1}").exec(whereabout.location)
            if (match && match.index > 0) {
                let potentialNextPiece = whereabout.location.substring(match.index)
                return this.#getLocationFromPartOfs({
                    location: potentialNextPiece,
                    linkText: whereabout.location.substring(0, match.index),
                    alias: whereabout.alias,
                    format: whereabout.format
                }, targetDate, thisDepth, format, filter, sourcePageType, firstFormat)
            }

            return this.#getDescriptionForThisPiece(whereabout, formatToUse, targetDate, sourcePageType, undefined)
        }


        let pageType = NameManager.getPageType(file.frontmatter)
        let nameSection = this.#getDescriptionForThisPiece(whereabout, formatToUse, targetDate, sourcePageType, file.name)
        let nextLevelCheck = this.#shouldAllowPiece(filter, thisDepth, file.frontmatter)

        if (!nextLevelCheck.continue) {
            return nameSection
        }

        let nextDepth = nextLevelCheck.incrementDepth ? thisDepth + 1 : thisDepth
        let nextLevel = WhereaboutsManager.getWhereabouts(file.frontmatter, targetDate).current
        let returnValue = ""

        if (nextLevelCheck.allowed) {
            // this piece is allowed, add it //
            returnValue += nameSection + ", "
        }

        if (nextLevelCheck.continue && nextLevel && nextLevel.location) {
            // we are allowed to continue, and we have somewhere to go //                
            returnValue += this.#getLocationFromPartOfs(nextLevel, targetDate, nextDepth, format, filter, pageType, firstFormat)
        }

        return returnValue
    }
}