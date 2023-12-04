class NameManager {

    LowerCase = "lower"
    TitleCase = "title"
    PreserveCase = "preserve"
    InitialUpperCase = "initialUpper"
    CreateLink = "always"
    NoLink = "never"
    LinkIfValid = "exists"

    #getIncludePreposition(format) {

        return format.includes("q") && !format.includes("Q")
    }

    #getArticleType(format) {

        // a: indefinite article, A: indefinite article if first, x: no article, q: preposition

        if (format.includes("x")) return "none"
        else if (format.includes("a")) return "indef"

        return "def"
    }

    #getCasing(format) {

        let casing = this.PreserveCase

        if (format.includes("s")) casing = this.LowerCase
        else if (format.includes("t")) casing = this.TitleCase

        return casing
    }

    #getLinkType(format) {

        let linkType = this.LinkIfExists
        if (format.includes("n")) linkType = this.NoLink
        else if (format.includes("y")) linkType = this.CreateLink

        return linkType
    }


    #getElementFromMetadata(elem) {
        if (customJS.state.coreMeta) {
            return customJS.state.coreMeta[elem];
        }

        return undefined;
    }

    getPageType(metadata) {

        if (!metadata) return "unknown"

        let tags = metadata.tags ?? [];


        if (tags.some(f => f.startsWith("person"))) return "person"
        else if (metadata.location || tags.some(f => f.startsWith("place"))) return "place"
        else if (tags.some(f => f.startsWith("organization"))) return "organization"
        else if (tags.some(f => f.startsWith("item"))) return "item"
        else if (tags.some(f => f.startsWith("deity"))) return "deity"
        else if (tags.some(f => f.startsWith("religion"))) return "religion"
        else if (tags.some(f => f.startsWith("species"))) return "species"
        else if (tags.some(f => f.startsWith("event")) || metadata.DR || metadata.DR_end || metadata.CY || metadata.CY_end) return "event"

        return "unknown"
    }


    #toTitle(str) {
        const lowers = ['A', 'An', 'The', 'And', 'But', 'Or', 'For', 'Nor', 'As', 'At', 'By', 'For', 'From', 'In', 'Into', 'Near', 'Of', 'On', 'Onto', 'To', 'With'];

        return str.
            split(' ').
            map((elem, index) => (lowers.findIndex(item => elem.toLowerCase() === item.toLowerCase()) >= 0 && index > 0) || elem.length == 0 ? elem : (elem[0].toUpperCase() + elem.substr(1))).
            join(' ')
    }

    #processDescriptiveName(descriptiveName, targetLink, article, linkType = "exists", casing = "preserve", initialUpper = false) {


        if (!descriptiveName) return undefined
        if (!article) article = ""


        descriptiveName = descriptiveName.trim()

        // name is one piece, don't change descriptiveName
        if (casing == this.TitleCase) {
            descriptiveName = this.#toTitle(descriptiveName)
            article = article.charAt(0).toUpperCase() + article.slice(1);
        } else if (casing == this.LowerCase) {
            descriptiveName = descriptiveName.toLowerCase()
            article = article.toLowerCase()
        }


        if (initialUpper) {
            if (article && article.length > 0) {
                article = article.charAt(0).toUpperCase() + article.slice(1);
            } else {
                descriptiveName = descriptiveName.charAt(0).toUpperCase() + descriptiveName.slice(1)
            }
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

    getCampaignSessionNoteFolder(prefix) {
        let metadata = this.#getElementFromMetadata("campaigns")
        if (metadata) {
            let cmp = metadata.filter(f => f.prefix.toLowerCase() == prefix.toLowerCase()).first()
            if (cmp) {
                return cmp.sessionNoteFolder
            }
        }

        return undefined
    }

    getFileForTarget(target, filter = undefined) {

        // thought: should getFileForTarget return as well the descriptive text? e.g. //
        // getFileForTarget("climbing the Sentinel Range") returns //
        // { filename: "Sentinel Range", prefix: "climbing the ", isAlias: false, frontmatter: { ... } } //
        // getFileForTarget("climbing the Sentinels") returns //
        // { filename: "Sentinel Range", linktext: "Sentinels", prefix: "climbing the ", isAlias: true, frontmatter: { ... }
        // getFileForTarget("Sentinel Range") returns //
        // { filename: "Sentinel Range", isAlias: false, frontmatter: { ... }

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
        let required = this.#getElementFromMetadata("requiredDisplayDefaults")
        let typeDefault = this.#getElementFromMetadata("typeDisplayDefaults")
        let defaultForThisItem = typeDefault ? typeDefault[this.getPageType(metadata)] : undefined
        let base = merge_options(required, defaultForThisItem)
        return merge_options(base, metadata.displayDefaults)
    }


    #getArticle(descriptiveName, metadata, articleType, includePreposition, linkTextOverride, sourcePageType) {

        if (!descriptiveName) return ""

        let displayData = metadata ? this.getDisplayData(metadata) : {}
        let article = ""

        if (articleType == "def") {
            // add definitive article //
            if ("defArt" in displayData) {
                // we have a page override, use as is
                // if null or undefined or blank, don't add anything
                if (displayData.defArt)
                    article = displayData.defArt;
                else
                    article = ""
            }
            else if (metadata && descriptiveName.split(' ').length > 1) {
                // name is more than one piece
                article = "the";
            }
        } else if (articleType == "indef") {
            // add definitive article //
            if ("indefArt" in displayData) {
                // we have a page override, use as is
                // if null or undefined or blank, don't add anything
                if (displayData.indefArt)
                    article = displayData.indefArt;
                else
                    article = ""
            } else {

                let lowered = descriptiveName.toLowerCase()
                article = "a"
                if (lowered.startsWith("uni")) {
                    article = "a"
                } else if (lowered[0] == "a" || lowered[0] == "e" || lowered[0] == "i" || lowered[0] == "o" || lowered[0] == "u") {
                    article = "an"
                }
            }
        }

        if (includePreposition) {

            let prep = ""

            if (linkTextOverride) {
                prep = linkTextOverride
            }
            else {

                switch (sourcePageType) {
                    case "person":
                        prep = displayData.ltPerson != undefined ? displayData.ltPerson : displayData.linkText
                        break
                    case "organization":
                        prep = displayData.ltOrg != undefined ? displayData.ltOrg : displayData.linkText
                        break
                    case "place":
                        prep = displayData.ltPlace != undefined ? displayData.ltPlace : displayData.linkText
                        break
                    case "item":
                        prep = displayData.ltItem != undefined ? displayData.ltItem : displayData.linkText
                        break
                    default:
                        prep = displayData.linkText
                }
            }

            if (!prep) prep = ""
            article = prep + " " + article
        }

        return article.trim()
    }


    // this formats a name object given the format options and returns a string
    // name = { name: the actual name, linkTarget: the target file, if there is one, article: the article, linkText: the linkText }

    formatName(name, formatSpecifier) {

        function toFirstUpper(inStr) {
            if (!inStr) return inStr
            let newStr = inStr.trim();
            return newStr.charAt(0).toUpperCase() + newStr.slice(1);
        }

        if (!name || !name.name) {
            return ""
        }

        // the format looks like: [linkText] [article] [[file|alias]]

        let formattedName = "";
        let specifier = formatSpecifier ?? ""
        let initialUpper = specifier.includes("u")

        // we include the link text if we (a) have a q but (b) do not have a negation (Q)
        if (specifier.includes("q") && !specifier.includes("Q") && name.linkText) {
            let linkText = name.linkText ?? ""
            if (initialUpper) {
                linkText = toFirstUpper(linkText)
                initialUpper = false;
            }

            formattedName = linkText + " "
        }


        if (specifier.includes("a")) {
            let article = name.indefiniteArticle ?? ""
            // title case expects the article to be upper
            if (initialUpper || specifier.includes("t")) {
                article = toFirstUpper(article)
                initialUpper = false;
            }

            formattedName += article + " "
        }
        else if (!specifier.includes("x") && name.definiteArticle) {
            let article = name.definiteArticle ?? ""
            // title case expects the article to be upper
            if (initialUpper || specifier.includes("t")) {
                article = toFirstUpper(article)
                initialUpper = false;
            }

            formattedName += article + " "
        }

        let nameStr = name.name
        if (specifier.includes("s")) {
            nameStr = nameStr.toLowerCase()
        } else if (specifier.includes("t")) {
            nameStr = this.#toTitle(nameStr)
        }

        if (initialUpper) {
            nameStr = toFirstUpper(nameStr)
            nameStr = false;
        }

        // avoid creating links in certain cases
        if (specifier.includes("y" && !name.linkTarget)) {
            if (target.includes(",")) specifier = specifier.replace("y", "")
            let fragmentsThatDontAlwaysLink = this.#getElementFromMetadata("fragmentsThatDontAutoLink")
            if (fragmentsThatDontAlwaysLink) {
                for (let word of nameStr.split(' ')) {
                    if (fragmentsThatDontAlwaysLink.includes(word.toLowerCase())) {
                        specifier = specifier.replace("y", "")
                        break
                    }
                }
            }
        }

        // if we have a y we always generate a link
        if (specifier.includes("y")) {
            if (!name.linkTarget || name.linkTarget == nameStr) {
                formattedName += "[[" + nameStr + "]]"
            } else {
                // we have a link target that doesn't match
                formattedName += "[[" + name.linkTarget + "|" + nameStr + "]]"
            }
        } else if (specifier.includes("n")) {
            // never link
            formattedName += nameStr
        } else {
            // link if we have a target, not otherwise
            if (!name.linkTarget) {
                formattedName += nameStr
            } else if (name.linkTarget == nameStr) {
                formattedName += "[[" + nameStr + "]]"
            } else {
                // we have a link target that doesn't match
                formattedName += "[[" + name.linkTarget + "|" + nameStr + "]]"
            }
        }

        return formattedName
    }

    #getLinkText(pageMetadata, sourceType) {
        // given a page, and a origin page, get the link text describing the "link" between these pages
        
        let displayData = this.getDisplayData(pageMetadata)
        
        let prep = ""
        switch (sourceType) {
            case "person":
                prep = displayData.ltPerson != undefined ? displayData.ltPerson : displayData.linkText
                break
            case "organization":
                prep = displayData.ltOrg != undefined ? displayData.ltOrg : displayData.linkText
                break
            case "place":
                prep = displayData.ltPlace != undefined ? displayData.ltPlace : displayData.linkText
                break
            case "item":
                prep = displayData.ltItem != undefined ? displayData.ltItem : displayData.linkText
                break
            default:
                prep = displayData.linkText
        }

        return prep ?? ""
    }

    #getIndefArt(inputString) {
        
        // indefinte article
        let lowered = inputString.toLowerCase()        
        if (lowered.startsWith("uni")) {
            return "a"
        } else if (lowered[0] == "a" || lowered[0] == "e" || lowered[0] == "i" || lowered[0] == "o" || lowered[0] == "u") {
            return "an"
        } else {
            return "a"
        }
    }

    #getDefArt(inputString) {
        // given an input string this returns the article

        if (!inputString) return ""
        
        if (/[A-Z~]/.test(inputString)) {
            // capital letters, calculate a definite article
            let wordCount = inputString.split(' ').length
            if (wordCount > 1) return "the"
            return ""
        } else {
            return "the"
        }
    }

    // this returns a name object for a string
    // name = { name: the actual name, linkTarget: the target file, if there is one, linkText: the linkText }
    // overrides providers the option to replace the name itself, the article, or the linkText
    //  { alias:, article:, linkText: }
    getNameObject(target, sourceType, overrides) {

        if (!overrides) overrides = {}

        // this gets the canonical name of a potential link
        if (!target || target == "Untitled") {
            return {
                name: overrides.alias ?? "",
                linkTarget: undefined,
                indefiniteArticle: "",
                definiteArticle: "",
                linkText: overrides.linkText ?? ""
            }
        }

        let fileData = this.getFileForTarget(target)

        if (!fileData) {
            // we don't have a target
            return {
                name: overrides.alias ?? target,
                linkTarget: undefined,
                definiteArticle: this.#getDefArt(overrides.alias ?? target),
                indefiniteArticle: this.#getIndefArt(overrides.alias ?? target),
                linkText: ""
            }
        }

        // we do have a target
        let frontmatter = fileData.frontmatter
        let selectedDescriptiveName = overrides.alias ?? (fileData.isAlias ? target : fileData.filename)
        if (selectedDescriptiveName === fileData.filename) {
            if (frontmatter.title && frontmatter.name) {
                selectedDescriptiveName = frontmatter.title + " " + frontmatter.name
            }
            else if (frontmatter.name) {
                selectedDescriptiveName = frontmatter.name
            } else if (frontmatter.campaign && frontmatter.sessionNumber) {
                selectedDescriptiveName = frontmatter.campaign + " " + frontmatter.sessionNumber
            }
        }

        let displayDefaults = this.getDisplayData(frontmatter)
        let defArt = ""
        let indefArt = ""

        if ("indefArt" in displayDefaults) {
            indefArt = displayDefaults.indefArt ?? ""
        } else {
            indefArt = this.#getIndefArt(selectedDescriptiveName)
        }
        
        
        if ("defArt" in displayDefaults) {
            defArt = displayDefaults.defArt ?? ""
        } else {
            defArt = this.#getDefArt(selectedDescriptiveName)
        }

        return {
            name: selectedDescriptiveName,
            definiteArticle: defArt,
            indefiniteArticle: indefArt,
            linkTarget: fileData.filename,
            linkText: overrides.linkText ?? this.#getLinkText(fileData.frontmatter, sourceType)
        }

    }

    // This returns a "name" for either a page or a string

    getName(target, format = "", alias = undefined, linkTextOverride = undefined, sourcePageType = undefined) {


        let nameObject = this.getNameObject(target, sourcePageType, {
            alias: alias,
            linkText: linkTextOverride
        })

        return this.formatName(nameObject, format)

        // this gets the canonical name of a potential link
        if (!target || target == "Untitled") return undefined

        let linkType = this.#getLinkType(format)
        let casing = this.#getCasing(format)
        let articleType = this.#getArticleType(format)
        let includePreposition = this.#getIncludePreposition(format)

        if (linkType == this.CreateLink) {
            if (target.includes(",")) linkType = this.LinkIfValid
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

        let fileData = this.getFileForTarget(target)

        if (!fileData) {
            return this.#processDescriptiveName(alias ?? target, undefined, this.#getArticle(alias ?? target, undefined, articleType, includePreposition, linkTextOverride, sourcePageType), linkType, casing, format.includes("u"))
        }

        let frontmatter = fileData.frontmatter
        let selectedDescriptiveName = alias ?? (fileData.isAlias ? target : fileData.filename)

        if (!fileData.isAlias && !alias) {
            if (frontmatter.title && frontmatter.name) {
                selectedDescriptiveName = frontmatter.title + " " + frontmatter.name
            }
            else if (frontmatter.name) {
                selectedDescriptiveName = frontmatter.name
            } else if (frontmatter.campaign && frontmatter.sessionNumber) {
                selectedDescriptiveName = frontmatter.campaign + " " + frontmatter.sessionNumber
            }
        }

        return this.#processDescriptiveName(selectedDescriptiveName, fileData.filename, this.#getArticle(selectedDescriptiveName, frontmatter, articleType, includePreposition, linkTextOverride, sourcePageType), linkType, casing, format.includes("u"))
    }
}