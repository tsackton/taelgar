class metadataUtils {

    #coreMetadata;

    #getElementFromMetadata(elem) {        
        if (this.#coreMetadata) return this.#coreMetadata[elem];
        else if (customJS.state.coreMeta) {        
            this.#coreMetadata = customJS.state.coreMeta
            return this.#coreMetadata[elem];
        }
        return undefined;
    }


    inLocation(targetLocation, metadata, targetDate) {

        const {WhereaboutsManager} = customJS
        
        let current = WhereaboutsManager.getWhereabouts(metadata, targetDate).current
        if (current == undefined || current.location == undefined || current.location == "Unknown") {
            return false;
        }

        return this.#locationSearch(current.location, targetLocation)
    }

    homeLocation(targetLocation, metadata, targetDate, includeDead) {

        const {WhereaboutsManager} = customJS
        const {DateManager} = customJS

        let pageDates = DateManager.getPageDates(metadata, targetDate)

        if (includeDead || pageDates.isAlive) {

            let home = WhereaboutsManager.getWhereabouts(metadata, targetDate).home;
            if (home == undefined) return false;
            if (home.location == undefined || home.location == "Unknown") return false;

            let found = this.#locationSearch(home.location, targetLocation)

            return found;
        }

        return false;
    }

    fromLocation(targetLocation, metadata, targetDate) {
       
        const {WhereaboutsManager} = customJS
   
        let origin = WhereaboutsManager.getWhereabouts(metadata, targetDate).origin
        if (origin == undefined) return false;
        if (origin.location == undefined || origin.location == "Unknown") return false;

        let found = this.#locationSearch(origin.location, targetLocation)

        return found;

    }

    #locationSearch(startingLocation, targetLocation) {

        if (startingLocation.trim() === targetLocation.trim())
            return true;

        if (startingLocation.indexOf(",") == -1) {
            // we have a single string
            let file = window.app.metadataCache.getFirstLinkpathDest(startingLocation, ".");
            if (file) {
                let fm = window.app.metadataCache.getFileCache(file)
                if (fm && fm.frontmatter && fm.frontmatter.partOf) {
                    return this.#locationSearch(fm.frontmatter.partOf, targetLocation)
                }

                return false;
            }

            console.log("Unable to retrieve linkpath for " + startingLocation)
            return false;
        } else {
            return startingLocation.contains(targetLocation)
        }
    }

    get_NameForOrganization(input, link, orgType, titleCase) {
        let file = window.app.metadataCache.getFirstLinkpathDest(input, ".");
        if (file) {

            let fm = window.app.metadataCache.getFileCache(file)
            if (!fm.frontmatter.tags || fm.frontmatter.tags.length == 0) return undefined
            if (fm.frontmatter.orgType != orgType) return undefined
            if (fm.frontmatter.tags.filter(f => f.startsWith("organization")).length == 0) return undefined;
            return this.get_Name({ file: file, frontmatter: fm.frontmatter }, link, titleCase)

        }

        return undefined
    }

    get_NameForPossibleLink(input, link, requiredTag, titleCase) {
        let file = window.app.metadataCache.getFirstLinkpathDest(input, ".");
        if (file) {

            let fm = window.app.metadataCache.getFileCache(file)

            if (requiredTag) {
                if (!fm.frontmatter.tags || fm.frontmatter.tags.length == 0) return undefined
                if (fm.frontmatter.tags.filter(f => f.startsWith(requiredTag)).length == 0) return undefined;
            }

            return this.get_Name({ file: file, frontmatter: fm.frontmatter }, link, titleCase)

        }

        if (link) return "[[" + input + "]]"
        return input
    }

    get_Name(input, link, titleCase, returnArticle = true) {

        function toTitle(str) {
            const lowers = ['A', 'An', 'The', 'And', 'But', 'Or', 'For', 'Nor', 'As', 'At', 'By', 'For', 'From', 'In', 'Into', 'Near', 'Of', 'On', 'Onto', 'To', 'With'];

            return str.
                split(' ').
                map((elem, index) => lowers.findIndex(item => elem.toLowerCase() === item.toLowerCase()) >= 0 && index > 0 ? elem : (elem[0].toUpperCase() + elem.substr(1))).
                join(' ')
        }

        // we have three possible inputs - a templater "tp" object or a dataview "file" object or a constructed object where x.file is obsidian file and x.frontmatter is metadata

        let fileName = input.file ? (input.file.title ?? input.file.basename ?? input.file.name) : input.name;

        if (fileName == undefined) return fileName;

        let descriptiveName = fileName;

        if (input.frontmatter && input.frontmatter.name) {
            if (input.frontmatter.title) {
                descriptiveName = input.frontmatter.title + " " + input.frontmatter.name
            }
            else if (input.frontmatter.name) {
                descriptiveName = input.frontmatter.name
            }
        } else if (input.frontmatter && input.frontmatter.campaign) {
            if (input.frontmatter.sessionNumber) {
                descriptiveName = input.frontmatter.campaign + " " + input.frontmatter.sessionNumber
            }
        }

        if (descriptiveName == "Untitled") return undefined;

        let article = ""
        let isPerson = input.frontmatter && input.frontmatter.tags && input.frontmatter.tags.some(f => f.startsWith("person"))

        // add definitive article //
        if (input.frontmatter && input.frontmatter.displayDefaults && "definitiveArticle" in input.frontmatter.displayDefaults) {
            // we have a page override, use as is
            // if null or undefined or blank, don't add anything
            if (input.frontmatter.displayDefaults.definitiveArticle) article = input.frontmatter.displayDefaults.definitiveArticle + " ";
        }
        else if (descriptiveName.split(' ').length > 1 && !isPerson) {
            // name is more than one piece
            article = "the ";
        }
        // name is one piece, don't change descriptiveName

        if (titleCase) {
            descriptiveName = toTitle(descriptiveName)
            article = article.charAt(0).toUpperCase() + article.slice(1);
        }

        if (!returnArticle) {
            article = ""
        }

        if (!link) return (article + descriptiveName);
        else if (descriptiveName == fileName) return (article + "[[" + descriptiveName + "]]");
        else return "[[" + fileName + "|" + article + descriptiveName + "]]"
    }

    get_party_name_for_party(prefix) {

        let partyName = undefined;
        let campaignData = this.#getElementFromMetadata("campaigns")
        if (campaignData) {
            let thisCampaign = campaignData.find(search => search.prefix.toUpperCase() == prefix.toUpperCase());
            if (thisCampaign) {
                partyName = thisCampaign.partyName;
                if (thisCampaign.partyFile) partyName = "[[" + thisCampaign.partyFile + "|" + partyName + "]]"
            }
        }

        return partyName;
    }

    #shouldLink(potentialLinkItem) {
        let skipList = this.#getElementFromMetadata("placeNameFragmentsThatSkipAutoLinking")

        if (!skipList) return true;

        for (let word of potentialLinkItem.split(' ')) {
            if (skipList.includes(word)) return false;
        }

        return true;
    }

    #get_LocationFromPieces(singleLoc, depth, titleCase) {
        if (singleLoc == undefined) return "Unknown"
        if (singleLoc == "") return "Unknown"
        if (typeof singleLoc === 'string' || singleLoc instanceof String) {

            if (singleLoc.indexOf(",") == -1) {
                // we have a single string
                let file = window.app.vault.getFiles().find(f => f.basename == singleLoc);
                if (file) {

                    let fm = window.app.metadataCache.getFileCache(file)
                    let name = this.get_Name({ file: file, frontmatter: fm.frontmatter }, true, titleCase)
                    if (fm && fm.frontmatter && fm.frontmatter.partOf && depth < 2) {
                        let parent = this.#get_LocationFromPieces(fm.frontmatter.partOf, depth + 1, titleCase)
                        return name + ", " + parent
                    }

                    return name
                }

                if (this.#shouldLink(singleLoc)) return "[[" + singleLoc + "]]"
                return singleLoc
            }

            let locArrayValues = singleLoc.split(",").map(function (f) {
                let pieceValue = f.trim();

                if (this.#shouldLink(pieceValue)) return "[[" + pieceValue + "]]"
                return pieceValue
            }, this);

            return locArrayValues.join(', ');
        }

        return "Unknown"
    }


    get_Location(place, titleCase) {

        if (place == undefined) return "";
        if (place.region && !place.place) return this.#get_LocationFromPieces(place.region, 0, titleCase)
        if (!place.region && place.place) return this.#get_LocationFromPieces(place.place, 0, titleCase)
        if (place.region && place.place) return this.#get_LocationFromPieces(place.place + ", " + place.region, 0, titleCase)
        if (place.location) return this.#get_LocationFromPieces(place.location, 0, titleCase)

        return this.#get_LocationFromPieces(place, 0, titleCase)
    }
}
