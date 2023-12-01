class NameManager {

    LowerCase = "lower"
    TitleCase = "title"
    PreserveCase = "preserve"
    InitialUpperCase = "initialUpper"
    CreateLink = "always"
    NoLink = "never"
    LinkIfValid = "exists"

    #getIncludePreposition(format) {

        return format.includes("q")
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


    #getArticle(descriptiveName, metadata, articleType, includePreposition) {

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
            if ("prep" in displayData) {
                if (displayData.prep) {
                    article = displayData.prep + " " + article
                }
            }
        }

        return article.trim()
    }

    // linkType = "never" | "always" | "exists"
    // casing = "title" | "lower" | "preserve" | "initialUpper"
    // articleType = "def" | "indef" | "none"
    getName(target, format = "", alias = undefined) {

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
            return this.#processDescriptiveName(alias ?? target, undefined, this.#getArticle(alias ?? target, undefined, articleType, includePreposition), linkType, casing, format.includes("u"))
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
        
        return this.#processDescriptiveName(selectedDescriptiveName, fileData.filename, this.#getArticle(selectedDescriptiveName, frontmatter, articleType, includePreposition), linkType, casing, format.includes("u"))
    }
}