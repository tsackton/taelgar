function sanitizeQuery(query) {
    let isInsideCallout = false;
    const parts = query.split("\n");
    const sanitized = [];

    for (const part of parts) {
        if (part.startsWith(">")) {
            isInsideCallout = true;
            sanitized.push(part.substring(1).trim());
        } else {
            sanitized.push(part);
        }
    }
    let finalQuery = query;
    if (isInsideCallout) {
        finalQuery = sanitized.join("\n");
    }
    return { isInsideCallout, finalQuery };
}

function surroundWithCalloutBlock(input) {
    const tmp = input.split("\n");
    return " " + tmp.join("\n> ");
}

async function prepareForExport(tp, headerType) {

    await forceLoadCustomJS()

    const metadataFilePath = app.vault.configDir + "/metadata.json";
    let metadataFile = await app.vault.adapter.read(metadataFilePath);
    customJS.state.coreMeta = JSON.parse(metadataFile)

    const { OutputHandler } = customJS
    const { DateManager } = customJS
    const { WhereaboutsManager } = customJS

    let websiteDate = ""
    let staticify_whereabouts = false
    let staticify_dataview = true
    try {
        let metadataFile = await app.vault.adapter.read(app.vault.configDir + "/../../website.json");
        let websiteData = JSON.parse(metadataFile)
        websiteDate = websiteData.export_date
        staticify_whereabouts = websiteData.staticify_whereabouts ?? false
        staticify_dataview = websiteData.staticify_dataview ?? true
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
        let processFrontmatter = !dateValue.isCreated || (staticify_whereabouts && md.frontmatter && md.frontmatter.whereabouts && Array.isArray(md.frontmatter.whereabouts))


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
                if (!("activeYear" in frontmatter)) {
                    let pageDates = DateManager.getPageDates(frontmatter)
                    if (pageDates.startDate) {
                        frontmatter["activeYear"] = pageDates.startDate.year
                    }
                }

                if (frontmatter.whereabouts) {

                    let wb = WhereaboutsManager.getWhereabouts(frontmatter)

                    frontmatter["whereabouts_current"] = wb.current.location
                    frontmatter["whereabouts_home"] = wb.home.location
                    frontmatter["whereabouts_origin"] = wb.origin.location
                }
            });
        }

        notice.setMessage("Making headers static\nProcessing file " + (files[i].name.padEnd(100, " ")) + "\n\n" + processed + " of " + files.length + "\n\nErrors: " + errors)
    }

    notice.hide()

    new Notice("Headers updated.")

    if (staticify_dataview) {

        processed = 0
        var notice = new Notice("Making DataView queries static", 0)
        for (let i = 0; i < files.length; i++) {

            let origText = await app.vault.read(files[i])
            let replacedText = origText

            const dataviewPrefix = "dataview";
            const dataViewRegex = new RegExp(`\`\`\`${dataviewPrefix}\\s(.+?)\`\`\``, "gsm");
            const dataviewMatches = origText.matchAll(dataViewRegex);

            let hasMatch = false
            let errors = 0

            for (const queryBlock of dataviewMatches) {

                try {
                    const block = queryBlock[0];
                    const query = queryBlock[1];
                    const { isInsideCallout, finalQuery } = sanitizeQuery(query);
                    let markdown = await window.app.plugins.plugins.dataview.api.tryQueryMarkdown(finalQuery, files[i].path);
                    if (isInsideCallout) {
                        markdown = surroundWithCalloutBlock(markdown);
                    }
                    replacedText = replacedText.replace(block, markdown);
                    hasMatch = true
                } catch (e) {
                    errors++
                    console.log(e)
                    return queryBlock[0];
                }
            }

            if (hasMatch) {
                await app.vault.process(files[i], data => {
                    if (data === origText) {
                        return replacedText
                    }

                    console.log("Did not replace text in file because the data has changed during processing")
                    console.log(files[i])
                    errors++
                    return data
                })
            }

            processed++
            notice.setMessage("Making DataView queries static\nProcessing file " + (files[i].name.padEnd(100, " ")) + "\n\n" + processed + " of " + files.length + "\n\nErrors: " + errors)
        }
        notice.hide()
    }
   
    new Notice("Headers updated.")


    customJS.state.overrideDate = undefined

    tp.user.shutdownApp()
}
module.exports = prepareForExport;