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
	return {isInsideCallout, finalQuery};
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
    try {
        let metadataFile = await app.vault.adapter.read(app.vault.configDir + "/../../website.json");
        let websiteData = JSON.parse(metadataFile)
        websiteDate = websiteData.export_date
        staticify_whereabouts = websiteData.staticify_whereabouts
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


    var notice = new Notice("Making DataView queries static", 0)
    for (let i = 0; i < files.length; i++) {
        await app.vault.process(files[i], async (data) => {
            let md = app.metadataCache.getFileCache(files[i])

            const dataviewJsPrefix = "dataview";
            const dataViewJsRegex = new RegExp(`\`\`\`${escapeRegex(dataviewJsPrefix)}\\s(.+?)\`\`\``, "gsm");
            const dataviewJsMatches = text.matchAll(dataViewJsRegex);

            for (const queryBlock of dataviewJsMatches) {
                try {
                    const block = queryBlock[0];
                    const query = queryBlock[1];

                    const div = createEl("div");
                    const component = new Component();
                    await window.app.plugins.plugins.dataview.api.executeJs(query, div, component, path);
                    component.load();
                    const markdown = div.innerHTML
                    replacedText = replacedText.replace(block, markdown);
                } catch (e) {
                    logs({ settings: properties.settings, e: true }, e);
                    notif({ settings: properties.settings }, error);
                    return queryBlock[0];
                }
            }


            processed++
            return data
        })

        notice.setMessage("Making DataView queries static\nProcessing file " + (files[i].name.padEnd(100, " ")) + "\n\n" + processed + " of " + files.length + "\n\nErrors: " + errors)
    }

    notice.hide()

    new Notice("Headers updated.")


    customJS.state.overrideDate = undefined

    tp.user.shutdownApp()
}
module.exports = prepareForExport;