function get_PageDatedValue(file, metadata) {

    const { DateManager } = customJS
    const { StringFormatter } = customJS
    const { NameManager } = customJS

    let dateInfo = DateManager.getPageDates(metadata)
    let pageDisplayData = NameManager.getDisplayData(metadata)

    if (!dateInfo.isCreated) return "**(page is future dated)**"

    if (dateInfo.endDate && dateInfo.endDate.display == "") {
        formatStr = pageDisplayData.pagePast
    }
    else if (dateInfo.isAlive) {
        if (!dateInfo.startDate) {
            // we have a death date in the future and no start date, output nothing
            return ""
        }
        formatStr = pageDisplayData.pageCurrent
    }
    else if (dateInfo.age || (dateInfo.age == 0 && dateInfo.startDate?.display?.length > 0)) {
        formatStr = pageDisplayData.pagePastWithStart
    }
    else if (dateInfo.endDate) {
        formatStr = pageDisplayData.pagePast
    }
    else {
        return ""
    }

    return StringFormatter.getFormattedString(formatStr, { name: file, frontmatter: metadata })
}

return get_PageDatedValue(dv.current().file.name, dv.current())