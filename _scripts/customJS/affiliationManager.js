class AffiliationManager {

    #getPartOfChain(partOfPiece, targeDate, thisDepth, maxDepth, linkType, casing) {

        const { NameManager } = customJS

        if (thisDepth == maxDepth) return ""
        if (!partOfPiece) return ""
        if (partOfPiece == "Taelgar") return ""

        let nameSection = NameManager.getName(partOfPiece, linkType, casing)
        let file = NameManager.getFileForTarget(partOfPiece)

        // we can't keep going, because this piece doesn't exist
        if (!file) {
            // lets see if we have a match to our capital letter check
            let match = new RegExp("[~A-Z]{1}").exec(partOfPiece)
            if (match && match.index > 0) {
                return partOfPiece.substring(0, match.index) + " " + this.#getPartOfChain(partOfPiece.substring(match.index), targeDate, thisDepth, maxDepth, linkType, casing)
            }

            return nameSection
        } else {
            let nextLevel = file.frontmatter.partOf

            if (NameManager.getPageType(file.frontmatter) == "place") {
                return nameSection
            }

            if (nextLevel) {
                return nameSection + ", " + this.#getPartOfChain(nextLevel, targeDate, thisDepth + 1, maxDepth, linkType, casing)
            }

            return nameSection
        }
    }

    #groupBy(list, keyGetter) {
        const map = new Map();
        list.forEach((item) => {
            const key = keyGetter(item);
            const collection = map.get(key);
            if (!collection) {
                map.set(key, [item]);
            } else {
                collection.push(item);
            }
        });
        return map;
    }

    #normalizeAffiliation(affiliation, pageDates, pageTitle, defaultStart) {

        const { DateManager } = customJS
        let minDate = DateManager.normalizeDate("0001", false)
        let maxDate = DateManager.normalizeDate("9999", true);
        defaultStart = DateManager.normalizeDate(defaultStart, false)

        let result = undefined

        if (typeof affiliation === 'string' || affiliation instanceof String) {
            result =
            {
                startDate: defaultStart ??  minDate,
                endDate: pageDates.endDate ?? maxDate,
                org: affiliation,
            }
        }
        else {
            result =
            {
                startDate: DateManager.normalizeDate(affiliation.start, false) ?? defaultStart ?? minDate,
                endDate: DateManager.normalizeDate(affiliation.end, true) ?? pageDates.endDate ?? maxDate,
                org: affiliation.org,
                type: affiliation.type,
                title: affiliation.title
            }
        }

        if (!result.org && affiliation.place) {
            // this came from leaderOf
            result.org = affiliation.place
            if (!result.type) result.type = "leader"
        }

        if (result.type == "leader" && !affiliation.title) {
            result.title = pageTitle
        }

        if (!result.type) result.type = "member"
        if (!result.title) result.title = result.type

        return result
    }

    getPrimaryAffiliations(metadata, targeDate) {
        // we ignore titles for primary
        return this.getAffiliations(metadata, targeDate).filter(f => f.type == "primary")
    }

    getNonPrimaryAffiliations(metadata, targeDate) {
        return this.getAffiliations(metadata, targeDate).filter(f => f.type != "primary")
    }

    getFormattedPrimaryAffiliations(metadata, targeDate) {
        return this.getPrimaryAffiliations(metadata, targeDate).map(f => {
            const { NameManager } = customJS
            return NameManager.getName(f.org)
        }).join(' and ').trim()
    }

    getFormattedNonPrimaryAffiliations(metadata, targetDate) {

        const { StringFormatter } = customJS
        const { DateManager } = customJS
        let displayOptions =
        {
            noDates: "<affiliationtitle:t> of <org>",
            pagePast: "<affiliationtitle:t> of <org> (until <endDate>)",
            pageCurrent: "<affiliationtitle:t> of <org> (since <startDate>, <length> ago)",
            pagePastWithStart: "<affiliationtitle:t> of <org> <startDate> - <endDate> (<length>)"
        }

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        if (!targetDate) targetDate = DateManager.getTargetDateForPage(metadata)

        let nonPrimary = this.getNonPrimaryAffiliations(metadata, targetDate)
        let grouped = this.#groupBy(nonPrimary, f => f.title + "_" + f.startDate.display + "_" + f.endDate.display)

        let lines = []
        grouped.forEach(group => {

            const { DateManager } = customJS
            const { NameManager } = customJS

            let affs = []
            let first = group.first()

            group.forEach(item => {
                console.log(item)
                if (item.org) {
                    affs.push(customJS.NameManager.getName(item.org))
                }
            })

            let lastPlace = affs.pop()
            let locString = undefined

            if (lastPlace) {
                let remaining = affs.join(", ")
                if (remaining) {
                    locString = remaining + " and " + lastPlace
                } else {
                    locString = lastPlace
                }
            }

            let dateInfo = {
                startDate: first.startDate,
                endDate: first.endDate,
                isCreated: true,
                isAlive: undefined,
                age: undefined
            }

            DateManager.setPageDateProperties(dateInfo, targetDate)

            let formatStr = displayOptions.noDates

            if (dateInfo.startDate.display && dateInfo.endDate.display) {
                formatStr = dateInfo.isAlive ? displayOptions.pageCurrent : displayOptions.pagePastWithStart
            } else if (dateInfo.startDate.display) {
                // we have a start but no end
                formatStr = dateInfo.isAlive ? displayOptions.pageCurrent : displayOptions.noDates
            } else if (dateInfo.endDate.display) {
                formatStr = dateInfo.isAlive ? displayOptions.noDates : displayOptions.pagePast
            } else {
                formatStr = displayOptions.noDates
            }

            lines.push(StringFormatter.getFormattedString(formatStr, { frontmatter: metadata }, targetDate, dateInfo,
                {
                    affiliationtitle: first.title,
                    org: locString
                }))
        })

        return lines.join("\n")
    }

    getAffiliationPartOf(metadata, linkType, casing) {

        if (metadata.partOf) {
            return this.#getPartOfChain(metadata.partOf, undefined, 0, undefined, linkType, casing)
        }

        return ""
    }

    getAffiliations(metadata, targetDate) {

        const { DateManager } = customJS

        if (targetDate) targetDate = DateManager.normalizeDate(targetDate)
        if (!targetDate) targetDate = DateManager.getTargetDateForPage(metadata)

        // this does some normalizing so I can test without changing all the pages
        let affList = []

        let pageDates = DateManager.getPageDates(metadata, targetDate)

        if (metadata.leaderOf) {
            for (let item of metadata.leaderOf) {
                let aff = this.#normalizeAffiliation(item, pageDates, metadata.title, metadata.reignStart)
                console.log(aff)
                if (aff.startDate.sort <= targetDate.sort) {
                    affList.push(aff)
                }
            }
        }

        if (metadata.affiliations) {
            for (let item of metadata.affiliations) {
                let aff = this.#normalizeAffiliation(item, pageDates, metadata.title)
                console.log(aff)
                if (aff.startDate.sort <= targetDate.sort) {
                    affList.push(aff)
                }
            }
        }

        return affList
    }

}