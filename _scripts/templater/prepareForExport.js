async function processLinksInFile(tfile, checkRooted, campaign, notice) {
    let root = window.app.vault.getRoot().path

    const { NameManager } = customJS

    notice.setMessage("Checking links in file\n\n" + tfile.name.padEnd(100, " "))

    console.log("Processing file " + tfile.name)

    let metadata = app.metadataCache.getFileCache(tfile)
    if (checkRooted && metadata && metadata.frontmatter && metadata.frontmatter.rooted) return

    await app.vault.process(tfile, (data) => {
        let currentContents = data.split('\n');

        // the end of the yaml -- this is 0-counting, so if the file is just a yaml start and end it will be 1
        let indexOfYamlEnd = currentContents.findIndex((f, i) => i > 0 && f == "---");

        if (indexOfYamlEnd > 0) {
            let yaml = currentContents.filter((v, i) => i >= 0 && i < indexOfYamlEnd)
            let sharedYamlIdx = yaml.findIndex(f => f.trim().startsWith("rooted"))
            if (sharedYamlIdx >= 0) {
                currentContents[sharedYamlIdx] = "rooted: true"
            } else {
                currentContents.splice(1, 0, "rooted: true")
                indexOfYamlEnd++
            }
        } else {
            currentContents.splice(0, 0, "---")
            currentContents.splice(0, 0, "rooted: true")
            currentContents.splice(0, 0, "---")
        }
        return currentContents.join("\n");
    })

    if (metadata && metadata.frontmatter && metadata.frontmatter.excludeRooted) {
        if (metadata.frontmatter.excludeRooted.some(f => f === campaign)) return
    }

    if (metadata && metadata.links) {
        for (let link of metadata.links) {
            // quick search            
            let tfile = window.app.metadataCache.getFirstLinkpathDest(link.link, root)
            if (tfile) {
                await processLinksInFile(tfile, true, campaign, notice)
            }
        }
    }
}

async function prepareForExport(tp, headerType) {

    const { DateManager } = customJS
    const { OutputHandler } = customJS

    let date = await tp.system.prompt("Enter new fantasy calendar date override: (YYYY, YYYY-MM, or YYYY-MM-DD, or blank to clear)")
    let campaign = await tp.system.prompt("Enter a campaign key for rooted exclusion calculations: ")

    let normalized = DateManager.normalizeDate(date)

    if (normalized) {
        customJS.state.overrideDate = normalized
    } else {
        customJS.state.overrideDate = DateManager.getTargetDateForPage(undefined)
    }


    const files = app.vault.getMarkdownFiles()
    let processed = 0
    let errors = 0

    var notice = new Notice("Making headers static", 0)
    for (let i = 0; i < files.length; i++) {
        break
        await app.vault.process(files[i], (data) => {
            let md = app.metadataCache.getFileCache(files[i])
            if (md && md.frontmatter && md.frontmatter.tags && md.frontmatter.headerVersion) {
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
            }
            processed++
            return data
        })

        notice.setMessage("Making headers static\nProcessing file " + (files[i].name.padEnd(100, " ")) + "\n\n" + processed + " of " + files.length + "\n\nErrors: " + errors)
    }

    notice.hide()

    new Notice("Headers updated.")


    var notice = new Notice("Making DataView queries static", 0)
    for (let i = 0; i < files.length; i++) {
        await app.vault.process(files[i], async (data) => {
            let md = app.metadataCache.getFileCache(files[i])

            const dataviewJsPrefix = "dataviewjs";
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


}
module.exports = prepareForExport;