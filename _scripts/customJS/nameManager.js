class NameManager {

    LowerCase = "lower"
    TitleCase = "title"
    PreserveCase = "preserve"
    CreateLink = "always"
    NoLink = "never"
    LinkIfValid = "exists"

    #getElementFromMetadata(elem) {
        if (customJS.state.coreMeta) {
            return customJS.state.coreMeta[elem];
        }

        return undefined;
    }

    #getPageType(metadata) {

        if (!metadata) return "unknown"

        let tags = metadata.tags ?? [];


        if (tags.some(f => f.startsWith("person"))) return "person"
        else if (metadata.location || tags.some(f => f.startsWith("place"))) return "place"
        else if (tags.some(f => f.startsWith("organization"))) return "organization"
        else if (tags.some(f => f.startsWith("item"))) return "item"
        else if (tags.some(f => f.startsWith("deity"))) return "deity"
        else if (tags.some(f => f.startsWith("religion"))) return "religion"
        else if (tags.some(f => f.startsWith("species"))) return "species"
        else if (tags.some(f => f.startsWith("item")) || metadata.DR || metadata.DR_end || metadata.CY || metadata.CY_end) return "event"

        return "unknown"
    }


    #toTitle(str) {
        const lowers = ['A', 'An', 'The', 'And', 'But', 'Or', 'For', 'Nor', 'As', 'At', 'By', 'For', 'From', 'In', 'Into', 'Near', 'Of', 'On', 'Onto', 'To', 'With'];

        return str.
            split(' ').
            map((elem, index) => (lowers.findIndex(item => elem.toLowerCase() === item.toLowerCase()) >= 0 && index > 0) || elem.length == 0 ? elem : (elem[0].toUpperCase() + elem.substr(1))).
            join(' ')
    }

    #processDescriptiveName(descriptiveName, targetLink, article, linkType = "exists", casing = "default") {

        if (!article) article = ""
        if (!descriptiveName) return undefined

        descriptiveName = descriptiveName.trim()

        // name is one piece, don't change descriptiveName
        if (casing == this.TitleCase) {
            descriptiveName = this.#toTitle(descriptiveName)
            article = article.charAt(0).toUpperCase() + article.slice(1);
        } else if (casing == this.LowerCase) {
            descriptiveName = descriptiveName.toLowerCase()
            article = article.toLowerCase()
        }

        descriptiveName = descriptiveName.trim()
        article = article.trim()

        let link = linkType == this.CreateLink || (linkType == this.LinkIfValid && targetLink)

        if (link) {
            if (descriptiveName == targetLink || !targetLink) return (article + " " + "[[" + descriptiveName + "]]").trim();
            else return (article + " " + "[[" + targetLink + "|" + descriptiveName + "]]").trim()
        }

        return (article + " " + descriptiveName).trim()
    }

    getFileForTarget(target, filter = undefined) {

        let root = window.app.vault.getRoot().path
        // quick search
        let tfile = window.app.metadataCache.getFirstLinkpathDest(target, root);
        if (tfile) {
            let fm = (window.app.metadataCache.getFileCache(tfile)?.frontmatter) ?? {}
            if (filter && !filter(fm)) return undefined
            return { filename: tfile.basename, isAlias: false, frontmatter: fm }
        }

        for (let file of window.app.vault.getMarkdownFiles()) {
            let cachedMetadata = window.app.metadataCache.getFileCache(file)
            let aliases = cachedMetadata?.frontmatter?.aliases

            let possibleReturn = undefined

            if (aliases) {
                if (typeof aliases === 'string' || aliases instanceof String) {
                    if (aliases.toLowerCase() == target.toLowerCase()) {
                        possibleReturn = { filename: file.basename, isAlias: true, frontmatter: cachedMetadata?.frontmatter ?? {} }
                    }
                }
                else {
                    for (let checker of aliases) {
                        if (checker.toLowerCase() == target.toLowerCase()) {
                            possibleReturn = { filename: file.basename, isAlias: true, frontmatter: cachedMetadata?.frontmatter ?? {} }
                        }
                    }
                }
            }

            if (possibleReturn) {
                if (!filter) return possibleReturn
                if (filter(possibleReturn.frontmatter)) return possibleReturn
            }
        }

        // custom map
        let map = this.#getElementFromMetadata("linkmap")?.find(f => f.from.toLowerCase() == target.toLowerCase())
        if (map) {
            let mappedTfile = window.app.metadataCache.getFirstLinkpathDest(map.to, root);
            if (mappedTfile) {
                let fm = window.app.metadataCache.getFileCache(mappedTfile)?.frontmatter ?? {}
                if (filter && !filter(fm)) return undefined
                return { filename: mappedTfile.basename, isAlias: map.isAlias, frontmatter: fm }
            }
        }

        return undefined
    }

    getDisplayData(target) {

        function merge_options(obj1, obj2) {
            var obj3 = {};
            if (obj1) for (var attrname in obj1) { obj3[attrname] = obj1[attrname]; }
            if (obj2) for (var attrname in obj2) { obj3[attrname] = obj2[attrname]; }
            return obj3;
        }

        let metadata = target

        if (typeof target === 'string' || target instanceof String) {
            // we have an input as a file
            let file = this.getFileForTarget(target)
            if (file) {
                // we found something for this target
                metadata = file.frontmatter
            }
            else {
                metadata = {}
            }
        }

        let displayDefaultData = this.#getElementFromMetadata("displayDefaults")
        let defaultForThisItem = displayDefaultData ? displayDefaultData[this.#getPageType(metadata)] : undefined
        if (!defaultForThisItem) defaultForThisItem = this.#getElementFromMetadata("displayDefaults")?.default


        // definitiveArticle is not required to be present

        let required = {
            startStatus: "",
            endStatus: "",
            whereaboutsOrigin: "<loc>",
            whereaboutsHome: "<loc>",
            whereaboutsPastHome: "<loc>",
            whereaboutsCurrent: "Current location (as of <target>): <loc>",
            whereaboutsPast: "<end> in <loc>",
            whereaboutsLastKnown: "Last known location: (as of <endDate>): <loc>",
            whereaboutsUnknown: "Current location: Unknown",
            whereaboutsParty: "<met> by <person> on <target> in <loc>",
            pageCurrent: "<start> <startDate>",
            pagePastWithStart: "<start> <startDate> - <end> <endDate>",
            pagePast: "<end> <endDate>",
            boxName: "Information",
            partOf: "<loc>",
            affiliationTypeOf: [],
            secondaryInfo: "",
            ddbLinkText: "Mechanics"
        }

        let base = merge_options(required, defaultForThisItem)
        return merge_options(base, metadata.displayDefaults)
    }


    // this returns a name only if the (a) file exists and (b) matches the filter
    getFilteredName(target, filter, linkType = this.LinkIfValid, casing = this.PreserveCase) {

        // this gets the canonical name of a potential link
        if (!target || target == "Untitled") return undefined

        if (linkType == this.CreateLink) {
            let fragmentsThatDontAlwaysLink = this.#getElementFromMetadata("fragmentsThatDontAutoLink")
            if (fragmentsThatDontAlwaysLink) {
                for (let word of target.split(' ')) {
                    if (fragmentsThatDontAlwaysLink.includes(word.toLowerCase())) {
                        linkType = this.LinkIfValid
                        break
                    }
                }
            }
        }

        let fileData = this.getFileForTarget(target, filter)

        if (!fileData) {
            if (filter) return undefined

            return this.#processDescriptiveName(target, undefined, "", linkType, casing)
        }

        let frontmatter = fileData.frontmatter
        let selectedDescriptiveName = fileData.isAlias ? target : fileData.filename
        let article = ""

        if (!fileData.isAlias) {
            if (frontmatter.title && frontmatter.name) {
                selectedDescriptiveName = frontmatter.title + " " + frontmatter.name
            }
            else if (frontmatter.name) {
                selectedDescriptiveName = frontmatter.name
            } else if (frontmatter.campaign && frontmatter.sessionNumber) {
                selectedDescriptiveName = frontmatter.campaign + " " + frontmatter.sessionNumber
            }

            let displayData = this.getDisplayData(frontmatter)

            // add definitive article //
            if ("definitiveArticle" in displayData) {
                // we have a page override, use as is
                // if null or undefined or blank, don't add anything
                if (displayData.definitiveArticle)
                    article = displayData.definitiveArticle;
            }
            else if (selectedDescriptiveName.split(' ').length > 1) {
                // name is more than one piece
                article = "the";
            }
        }

        return this.#processDescriptiveName(selectedDescriptiveName, fileData.filename, article, linkType, casing)

    }

    // linkType = "never" | "always" | "exists"
    // casing = "title" | "lower" | "preserve"
    getName(target, linkType = this.LinkIfValid, casing = this.PreserveCase) {
        return this.getFilteredName(target, undefined, linkType, casing)
    }

    getDescriptionOfDateInformation(metadata, dateInfo, overrideDisplayInfo) {

        if (!dateInfo.isCreated) return "**(page is future dated)**"

        let pageDisplayData = overrideDisplayInfo ?? this.getDisplayData(metadata)
        let formatStr = undefined

        if (dateInfo.endDate && dateInfo.endDate.display == "") formatStr = pageDisplayData.pagePast
        else if (dateInfo.isAlive) {
            if (!dateInfo.startDate) {
                // we have a death date in the future and no start date, output nothing
                return ""
            }
            formatStr = pageDisplayData.pageCurrent
        }
        else if (dateInfo.age) formatStr = pageDisplayData.pagePastWithStart
        else if (dateInfo.endDate) formatStr = pageDisplayData.pagePast
        else return ""

        return formatStr.replace("<length>", dateInfo.age)
            .replace("<start>", pageDisplayData.startStatus)
            .replace("<end>", pageDisplayData.endStatus)
            .replace("<startDate>", dateInfo.startDate?.display ?? "")
            .replace("<endDate>", dateInfo.endDate?.display ?? "")
    }
}