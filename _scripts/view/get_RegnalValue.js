function get_RegnalValue(metadata) {

    function groupBy(list, keyGetter) {
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


    const { DateManager } = customJS
    const { LocationManager } = customJS
    const { NameManager } = customJS

    if (!metadata.leaderOf) return ""

    let targetDate = DateManager.getTargetDateForPage(metadata)
    let pageDates = DateManager.getPageDates(metadata, targetDate)

    let lines = []


    // this is some squirelly Javascript to effectively group the leader sections by common start / end title, so we can show common stuff in a list
    let grouped = groupBy(metadata.leaderOf, f => f.title + "_" + f.start + "_" + f.end)

    grouped.forEach(leaderOf => {
        let displayOverride =
        {
            pagePast: "<title> of <loclist> (reigned until <endDate>)",
            pageCurrent: "<title> of <loclist> (since <startDate>, <length> years ago)",
            pagePastWithStart: "<title> of <loclist> <startDate> - <endDate> (<length> years)"
        }

        let first = leaderOf.first()
        let start = DateManager.normalizeDate(first.start) ?? DateManager.normalizeDate(metadata.reignStart)
        let end = DateManager.normalizeDate(first.end) ?? DateManager.normalizeDate(metadata.reignEnd) ?? pageDates.endDate
        let title = first.title ?? metadata.title ?? "Leader"

        let dateInfo = {
            startDate: start,
            endDate: end,
            isCreated: true,
            isAlive: undefined,
            age: undefined
        }

        DateManager.setPageDateProperties(dateInfo, targetDate)

        let places = []

        leaderOf.forEach(item => {
            if (item.place) {
                places.push(LocationManager.getLocationName(item.place, "preserve", 1, "always"))
            }
        })

        let lastPlace = places.pop()
        let locString = undefined

        if (lastPlace) {
            let remaining = places.join(", ")
            if (remaining) {
                locString = remaining + " and " + lastPlace
            } else {
                locString = lastPlace
            }

            displayOverride.pagePast = displayOverride.pagePast.replace("<title>", title).replace("<loclist>", locString)
            displayOverride.pageCurrent = displayOverride.pageCurrent.replace("<title>", title).replace("<loclist>", locString)
            displayOverride.pagePastWithStart = displayOverride.pagePastWithStart.replace("<title>", title).replace("<loclist>", locString)
            displayOverride.pageNotExistError = ""

            if (dateInfo.startDate.display == "") {
                lines.push("<title> of <loclist>".replace("<title>", title).replace("<loclist>", locString))
            } else {
                let description = NameManager.getDescriptionOfDateInformation(metadata, dateInfo, displayOverride)
                if (description.length > 0)
                    lines.push(description)
            }
        }
    })

    return lines.join("\n")

}

return get_RegnalValue(dv.current())