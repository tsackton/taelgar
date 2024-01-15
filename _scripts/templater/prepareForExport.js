async function prepareForExport(tp, headerType) {

    const { OutputHandler } = customJS
    const { DateManager } = customJS

    let websiteDate = ""
    try {
        let metadataFile = await app.vault.adapter.read(app.vault.configDir + "/../../website.json");
        let websiteData = JSON.parse(metadataFile)
        websiteDate = websiteData.export_date
    }
    catch { }

    let defaultExport = websiteDate ?? ""

    let date = await tp.system.prompt("Enter new fantasy calendar date override: (YYYY, YYYY-MM, or YYYY-MM-DD, or blank to clear)", defaultExport)
    let normalized = DateManager.normalizeDate(date)


    if (normalized) {
        customJS.state.overrideDate = normalized
    } else {
        customJS.state.overrideDate = DateManager.getTargetDateForPage(undefined)
    }


    const files = app.vault.getMarkdownFiles()
    let processed = 0
    let errors = 0

    var notice = new Notice("Link checking skipped. Making headers static", 0)

    for (let i = 0; i < files.length; i++) {
        let md = app.metadataCache.getFileCache(files[i])

        let processHeader = md && md.frontmatter && md.frontmatter.tags && md.frontmatter.headerVersion
        let dateValue = md.frontmatter ? DateManager.getPageDates(md.frontmatter) : { isCreated: true }
        let processFrontmatter = !dateValue.isCreated


        if (processHeader) {
            await app.vault.process(files[i], (data) => {
                try {
                    let newC = OutputHandler.regenerateHeader(data, files[i].name, md.frontmatter, headerType)
                    processed++
                    return newC.join("\n");
                }
                catch (error) {
                    console.log("Failed to update file " + files[i].name)
                    console.log(error)
                    errors++;
                }
                processed++
                return data
            })
        }

        if (processFrontmatter) {
            await app.fileManager.processFrontMatter(files[i], frontmatter => {
                const { DateManager } = customJS

                if (!frontmatter) return
                if ("activeYear" in frontmatter) return

                let pageDates = DateManager.getPageDates(frontmatter)
                if (pageDates.startDate) {
                    frontmatter["activeYear"] = pageDates.startDate.year
                }
            });
        }

        notice.setMessage("Making headers static\nProcessing file " + (files[i].name.padEnd(100, " ")) + "\n\n" + processed + " of " + files.length + "\n\nErrors: " + errors)
    }

    notice.hide()

    new Notice("Headers updated.")

    customJS.state.overrideDate = undefined

    //tp.user.terminate()
}
module.exports = prepareForExport;