async function setTestDate(tp) {

    const { DateManager } = customJS

    let date = await tp.system.prompt("Enter new fantasy calendar date override: (YYYY, YYYY-MM, or YYYY-MM-DD, or blank to clear)")

    let normalized = DateManager.normalizeDate(date)

    if (normalized) {
        customJS.state.overrideDate = normalized
    } else {
        customJS.state.overrideDate = undefined
    }

}
module.exports = setTestDate;